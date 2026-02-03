# Deployment Guide

Complete guide for deploying the AI Presentation System in various environments.

---

## Table of Contents

- [Local Development](#local-development)
- [Production Deployment](#production-deployment)
- [Cloud Platforms](#cloud-platforms)
- [Docker Deployment](#docker-deployment)
- [Scaling Considerations](#scaling-considerations)
- [Monitoring and Maintenance](#monitoring-and-maintenance)

---

## Local Development

### System Requirements

- **OS**: Linux, macOS, or Windows 10/11
- **Python**: 3.10 or higher
- **RAM**: Minimum 8GB, recommended 16GB
- **Disk**: 5GB free space
- **Network**: Stable internet connection for API calls

### Setup Steps

```bash
# 1. Clone and navigate
git clone https://github.com/glen200392/ai-presentation-system.git
cd ai-presentation-system

# 2. Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development tools

# 4. Set up environment variables
cp .env.example .env
nano .env  # Edit with your configuration

# 5. Run tests
pytest tests/

# 6. Start development server
python -m ai_presentation serve --dev
```

---

## Production Deployment

### Pre-Deployment Checklist

- [ ] All tests passing (`pytest tests/`)
- [ ] Environment variables configured
- [ ] API keys secured (use secrets management)
- [ ] Rate limits configured
- [ ] Logging and monitoring setup
- [ ] Backup strategy defined
- [ ] Error handling tested

### Environment Configuration

```bash
# Production .env example
ENVIRONMENT=production
DEBUG=false

# API Configuration
OPENAI_API_KEY=${SECRET_OPENAI_KEY}
NEBULA_API_KEY=${SECRET_NEBULA_KEY}
API_RATE_LIMIT=100
API_TIMEOUT=60

# System Limits
MAX_CONCURRENT_GENERATIONS=5
MAX_SLIDES_PER_PRESENTATION=100
QUALITY_THRESHOLD=90

# Storage
OUTPUT_DIR=/var/presentations/output
CACHE_DIR=/var/presentations/cache
LOG_DIR=/var/log/ai-presentation

# Security
ALLOWED_HOSTS=your-domain.com
CORS_ORIGINS=https://your-frontend.com
API_KEY_REQUIRED=true
```

### Application Server Setup

Using **Gunicorn** (recommended for production):

```bash
# Install Gunicorn
pip install gunicorn

# Run with workers
gunicorn -w 4 -b 0.0.0.0:8000 \
  --timeout 300 \
  --log-level info \
  --access-logfile /var/log/ai-presentation/access.log \
  --error-logfile /var/log/ai-presentation/error.log \
  ai_presentation.wsgi:application
```

### Nginx Configuration

```nginx
upstream ai_presentation {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name your-domain.com;
    
    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    ssl_certificate /etc/ssl/certs/your-cert.crt;
    ssl_certificate_key /etc/ssl/private/your-key.key;
    
    client_max_body_size 50M;
    
    location / {
        proxy_pass http://ai_presentation;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 300s;
    }
    
    location /static/ {
        alias /var/www/ai-presentation/static/;
        expires 30d;
    }
}
```

---

## Cloud Platforms

### AWS Deployment

#### Using EC2

```bash
# 1. Launch EC2 instance (t3.medium or larger)
# 2. SSH into instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# 3. Install dependencies
sudo apt update
sudo apt install python3.10 python3.10-venv nginx

# 4. Clone and setup
git clone https://github.com/glen200392/ai-presentation-system.git
cd ai-presentation-system
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. Configure systemd service
sudo nano /etc/systemd/system/ai-presentation.service
```

Systemd service file:
```ini
[Unit]
Description=AI Presentation System
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/ai-presentation-system
Environment="PATH=/home/ubuntu/ai-presentation-system/venv/bin"
EnvironmentFile=/home/ubuntu/ai-presentation-system/.env
ExecStart=/home/ubuntu/ai-presentation-system/venv/bin/gunicorn \
  -w 4 -b 127.0.0.1:8000 ai_presentation.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# 6. Enable and start service
sudo systemctl enable ai-presentation
sudo systemctl start ai-presentation
sudo systemctl status ai-presentation
```

#### Using ECS (Docker)

```yaml
# ecs-task-definition.json
{
  "family": "ai-presentation-system",
  "containerDefinitions": [
    {
      "name": "ai-presentation",
      "image": "your-repo/ai-presentation:latest",
      "memory": 4096,
      "cpu": 2048,
      "essential": true,
      "portMappings": [
        {
          "containerPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "ENVIRONMENT",
          "value": "production"
        }
      ],
      "secrets": [
        {
          "name": "OPENAI_API_KEY",
          "valueFrom": "arn:aws:secretsmanager:region:account:secret:openai-key"
        }
      ]
    }
  ]
}
```

### Google Cloud Platform

```bash
# Using Cloud Run
gcloud run deploy ai-presentation \
  --image gcr.io/your-project/ai-presentation \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 4Gi \
  --cpu 2 \
  --timeout 300 \
  --set-env-vars ENVIRONMENT=production
```

### Azure

```bash
# Using Azure App Service
az webapp create \
  --resource-group ai-presentation-rg \
  --plan ai-presentation-plan \
  --name ai-presentation-app \
  --runtime "PYTHON|3.10"

az webapp config appsettings set \
  --resource-group ai-presentation-rg \
  --name ai-presentation-app \
  --settings ENVIRONMENT=production
```

---

## Docker Deployment

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create necessary directories
RUN mkdir -p /app/output /app/cache /app/logs

# Non-root user
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s \
  CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Run application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "ai_presentation.wsgi:application"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  ai-presentation:
    build: .
    ports:
      - "8000:8000"
    environment:
      - ENVIRONMENT=production
      - DEBUG=false
    env_file:
      - .env
    volumes:
      - ./output:/app/output
      - ./cache:/app/cache
      - ./logs:/app/logs
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '1'
          memory: 2G

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - ai-presentation
    restart: unless-stopped
```

---

## Scaling Considerations

### Horizontal Scaling

```yaml
# Kubernetes deployment example
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-presentation
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-presentation
  template:
    metadata:
      labels:
        app: ai-presentation
    spec:
      containers:
      - name: ai-presentation
        image: your-repo/ai-presentation:latest
        resources:
          requests:
            memory: "2Gi"
            cpu: "1"
          limits:
            memory: "4Gi"
            cpu: "2"
        env:
        - name: ENVIRONMENT
          value: "production"
```

### Load Balancing

- Use nginx or HAProxy for request distribution
- Configure health checks on `/health` endpoint
- Implement sticky sessions if needed for stateful operations

### Caching Strategy

```python
# Redis configuration for caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

---

## Monitoring and Maintenance

### Health Checks

```python
# Health check endpoint
@app.route('/health')
def health_check():
    return {
        'status': 'healthy',
        'version': VERSION,
        'agents': get_agent_status(),
        'timestamp': datetime.utcnow().isoformat()
    }
```

### Logging

```python
# logging_config.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/ai-presentation/app.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
}
```

### Monitoring Metrics

Key metrics to track:
- Request rate and latency
- Agent execution time
- Quality scores distribution
- Error rates by type
- Resource usage (CPU, memory, disk)
- API call volumes and costs

### Backup Strategy

```bash
# Backup script
#!/bin/bash
BACKUP_DIR="/backups/ai-presentation"
DATE=$(date +%Y%m%d_%H%M%S)

# Backup configuration
tar -czf "$BACKUP_DIR/config_$DATE.tar.gz" .env agents_config.yaml

# Backup output files (last 30 days)
find ./output -mtime -30 -type f | tar -czf "$BACKUP_DIR/output_$DATE.tar.gz" -T -

# Backup logs
tar -czf "$BACKUP_DIR/logs_$DATE.tar.gz" ./logs/

# Clean old backups (keep 7 days)
find "$BACKUP_DIR" -mtime +7 -delete
```

---

## Security Best Practices

1. **API Keys**: Use environment variables or secrets management (AWS Secrets Manager, Azure Key Vault)
2. **HTTPS**: Always use SSL/TLS in production
3. **Input Validation**: Sanitize all user inputs
4. **Rate Limiting**: Implement per-user rate limits
5. **Access Control**: Require authentication for API endpoints
6. **Logging**: Log security events and access patterns
7. **Updates**: Keep dependencies updated with `pip-audit`

---

## Support

For deployment issues:
- GitHub Issues: https://github.com/glen200392/ai-presentation-system/issues
- Email: glen200392@gmail.com
- Documentation: See [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md)
