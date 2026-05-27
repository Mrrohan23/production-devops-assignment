from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
import requests

app = FastAPI()

Instrumentator().instrument(app).expose(app)

class PromptRequest(BaseModel):
    prompt: str

@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI DevOps Assignment</title>

        <style>

            body {
                font-family: Arial;
                background-color: #f4f4f4;
                padding: 40px;
            }

            .container {
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }

            textarea {
                width: 100%;
                height: 120px;
                padding: 10px;
                font-size: 16px;
            }

            button {
                margin-top: 15px;
                padding: 12px 20px;
                background: black;
                color: white;
                border: none;
                cursor: pointer;
                font-size: 16px;
            }

            .response {
                margin-top: 30px;
                background: #eeeeee;
                padding: 20px;
                border-radius: 8px;
                white-space: pre-wrap;
            }

        </style>
    </head>

    <body>

        <div class="container">

            <h1>Production AI DevOps Assignment</h1>

            <p>FastAPI + Ollama + Docker + NGINX + Monitoring</p>

            <textarea id="prompt" placeholder="Ask something..."></textarea>

            <button onclick="generateResponse()">
                Generate Response
            </button>

            <div class="response" id="response">
                AI response will appear here...
            </div>

        </div>

        <script>

            async function generateResponse() {

                const prompt = document.getElementById("prompt").value;

                const responseDiv = document.getElementById("response");

                responseDiv.innerHTML = "Generating response...";

                const response = await fetch("/ai", {

                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        prompt: prompt
                    })
                });

                const data = await response.json();

                responseDiv.innerHTML = data.response || data.error;
            }

        </script>

    </body>
    </html>
    """

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/ai")
def ai_response(data: PromptRequest):

    try:

        response = requests.post(
            "http://host.docker.internal:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": data.prompt,
                "stream": False
            },
            timeout=120
        )

        result = response.json()

        return {
            "response": result.get("response", "No response generated")
        }

    except Exception as e:

        return {
            "error": str(e)
        }