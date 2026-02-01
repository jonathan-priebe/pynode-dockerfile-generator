# CI/CD Pipeline

## Workflows Overview

Four automated workflows run on push/PR to `main`:

| Workflow | Purpose | Tools |
|----------|---------|-------|
| **Build and Push** | Build & publish Docker image | Docker, GHCR |
| **Lint** | Code quality checks | Black, isort, Flake8, MyPy |
| **Code Security** | Python security analysis | Bandit, pip-audit |
| **Trivy Scan** | Container vulnerability scanning | Trivy |

## 1. Build and Push

**File:** `.github/workflows/build.yml`

**Triggers:**
- Push to `main`
- Version tags (`v*.*.*`)
- Manual (`workflow_dispatch`)

**Process:**
1. Checkout code
2. Login to GHCR with `GITHUB_TOKEN`
3. Build Docker image from `docker/Dockerfile`
4. Push to `ghcr.io/<repo>` with multiple tags

**Tags Generated:**
- `latest` - Most recent build
- `<commit-sha>` - Specific commit
- `<ref-name>` - Branch/tag name

## 2. Lint

**File:** `.github/workflows/lint.yml`

**Tools:**
- **Black** - Code formatting (88 char line length)
- **isort** - Import sorting (Black profile)
- **Flake8** - PEP 8 compliance (ignores E203, W503)
- **MyPy** - Static type checking

**Configuration:**
- `isort --profile black` ensures compatibility
- All checks must pass for merge

## 3. Code Security

**File:** `.github/workflows/code-security.yml`

**Tools:**
- **Bandit** - SAST for Python
  - Finds: SQL injection, hardcoded secrets, shell injection
  - Generates JSON artifact
- **pip-audit** - Dependency CVE scanner
  - Checks `requirements.txt` against CVE database

**Artifacts:**
- `bandit-security-report.json` uploaded for review

## 4. Trivy Security Scan

**File:** `.github/workflows/trivy_scan.yml`

**Process:**
1. Build Docker image
2. Scan with Trivy (SARIF format)
3. Upload to GitHub Security tab
4. Re-scan with table output
5. **Fail on CRITICAL/HIGH** vulnerabilities

**Integration:**
- Results visible in Security → Code scanning alerts
- Blocks merge if critical issues found

## Best Practices

**Branch Protection:**
- Require all workflows to pass before merge
- Enforce status checks

**Security:**
- All workflows use `GITHUB_TOKEN` (auto-provided)
- No hardcoded secrets
- Minimal permissions (`contents: read`, `packages: write`)

**Optimization:**
- Workflows run in parallel
- Use caching where applicable
- Fail fast on errors

## Continuous Deployment

Currently manual deployment via:
1. Push to `main` triggers build
2. Image pushed to GHCR
3. Users pull `latest` tag

**Future:** Add release automation with GitHub Releases and semantic versioning.
