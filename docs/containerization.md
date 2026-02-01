# Containerization

## Docker Image

**Base Image:** `python:3.12-slim`
- Minimal footprint
- Official Python image
- Regular security updates

### Build Strategy

**Installation:**
```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
COPY setup.py .
RUN pip install --no-cache-dir -e .
```

### Security

**User Management:**
- Creates `appuser:appgroup` for security
- Entrypoint script owned by appuser
- Output directory with correct permissions

**Permissions:**
```dockerfile
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && chown appuser:appgroup /entrypoint.sh
RUN mkdir -p /output && chmod 777 /output
USER appuser:appgroup
```

### Entrypoint

**Shell script wrapper:**
```dockerfile
ENTRYPOINT ["/entrypoint.sh"]
CMD ["--help"]
```

**entrypoint.sh:**
```bash
#!/bin/bash
set -e
exec dockerfile-generator "$@"
```

Allows passing all arguments to the CLI while maintaining proper process handling.

## Docker Compose

**Configuration:**
- Pulls from GHCR: `ghcr.io/jonathan-priebe/pynode-dockerfile-generator:latest`
- Named volume: `dockerfile-output` for persistence

**Usage Pattern:**
```bash
docker-compose run --rm dockerfile-generator create python -lv 3.12 --flavor slim
```

## Registry

**GitHub Container Registry (GHCR):**
- Public registry
- Automated builds via GitHub Actions
- Tags: `latest`, `<commit-sha>`, `<ref-name>`

## Optimization

**.dockerignore:**
- Minimal context (excludes .git, .venv, output/)
- Faster builds
- Smaller context uploads
