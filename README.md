# Production AI DevOps Assignment

## Overview

This project demonstrates production-style deployment of an AI backend application using:

- FastAPI
- Docker
- Docker Compose
- PostgreSQL
- Redis
- NGINX Reverse Proxy
- Grafana
- Prometheus
- Cloudflare Tunnel
- GitHub Actions CI/CD
- Ollama LLM Integration

---

# Architecture

Internet → Cloudflare → NGINX → FastAPI AI Backend → Ollama  
                                                     → PostgreSQL  
                                                     → Redis  

---

# Features

- AI/LLM backend deployment
- Dockerized infrastructure
- Reverse proxy using NGINX
- PostgreSQL integration
- Redis caching
- Monitoring using Grafana & Prometheus
- Health check endpoint
- Automated backups
- GitHub Actions CI/CD
- Cloudflare public HTTPS access
- Security-focused deployment

---

# Start Application

```bash
docker-compose up -d --build
```

---

# Application URLs

Main App:  
http://localhost

Swagger Docs:  
http://localhost/docs

Health Endpoint:  
http://localhost/health

Grafana:  
http://localhost:3000

Prometheus:  
http://localhost:9090

Production Domain:  
https://ai.yourdomain.com

---

# AI Endpoint

POST /ai

Example:

```json
{
  "prompt": "Explain Docker"
}
```

---

# Monitoring

- Prometheus metrics
- Grafana dashboards

---

# Logging

```bash
docker logs fastapi_app
docker logs nginx_proxy
```

---

# Security

- Docker container isolation
- Environment variables
- UFW firewall
- fail2ban support
- Reverse proxy architecture

---

# Cloudflare Integration

- HTTPS enabled
- Cloudflare Tunnel configured
- DNS managed by Cloudflare
- SSL/TLS encryption
- DDoS protection
- WAF support

---

# Automated Backup

```bash
chmod +x backup.sh
./backup.sh
```

Cron Job Example:

```bash
0 2 * * * /home/user/devops-assignment-cloudflare/backup.sh
```

---

# Zero Downtime Strategy

- Rolling deployment approach
- Blue/Green deployment support
- Kubernetes migration ready

---

# CI/CD

GitHub Actions pipeline automatically builds containers on push to main branch.

---

# Screenshots

## Running Containers

![Docker Containers](screenshots/docker-ps.png)

---

## Main Application

![Application Home](screenshots/app-home.png)

---

## Swagger API Documentation

![Swagger Docs](screenshots/swagger-docs.png)

---

## AI Endpoint Response

![AI Endpoint](screenshots/ai-endpoint.png)

---

## Health Check Endpoint

![Health Check](screenshots/health-check.png)

---

## Grafana Dashboard

![Grafana](screenshots/grafana.png)

---

## Prometheus Monitoring

![Prometheus](screenshots/prometheus.png)

---

## Cloudflare HTTPS Access

![Cloudflare HTTPS](screenshots/cloudflare-https.png)

---

## GitHub Actions CI/CD

![GitHub Actions](screenshots/github-actions.png)

---

## UFW Firewall

![UFW](screenshots/ufw.png)

---

## fail2ban Protection

![fail2ban](screenshots/fail2ban.png)

---

# Production Deployment Notes

This setup simulates a real-world production AI deployment using local Ubuntu infrastructure with public HTTPS access through Cloudflare Tunnel.