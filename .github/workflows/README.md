# GitHub Workflows

This directory contains CI/CD workflows for the pynode-dockerfile-generator project.

## Table of Contents

- [Workflows Overview](#workflows-overview)
- [Build and Push](#build-and-push)
  - [Triggers](#triggers)
  - [Image Tags](#image-tags)
  - [Usage](#usage)
  - [Permissions](#permissions)
  - [Making the Package Public](#making-the-package-public)
  - [Manual Workflow Trigger](#manual-workflow-trigger)
- [Lint](#lint)
  - [Linting Tools](#linting-tools)
- [Code Security](#code-security)
  - [Security Tools](#security-tools)
  - [What It Checks](#what-it-checks)
- [Trivy Security Scan](#trivy-security-scan)
  - [What It Scans](#what-it-scans)
  - [Viewing Results](#viewing-results)

## Workflows Overview

| Workflow | File | Purpose |
|----------|------|---------|
| Build and Push | `build.yml` | Build and publish Docker image to GHCR |
| Lint | `lint.yml` | Code quality checks (formatting, linting, type checking) |
| Code Security | `code-security.yml` | Python code security analysis and dependency vulnerability checks |
| Trivy Security Scan | `trivy_scan.yml` | Vulnerability scanning for Docker images |

## Build and Push

**File:** `build.yml`

Automatically builds and publishes the Docker image to GitHub Container Registry (GHCR).

### Triggers

- **Push to main branch** - Automatically builds and pushes on every commit to `main`
- **Version tags** - Triggers on tags matching `v*.*.*` (e.g., `v1.0.0`, `v0.2.1`)
- **Manual trigger** - Can be triggered manually via GitHub Actions UI (`workflow_dispatch`)

### Image Tags

The workflow creates multiple tags for each build:

- `latest` - Always points to the most recent build from `main`
- `<commit-sha>` - Git commit SHA for exact version tracking
- `<ref-name>` - Branch name or tag name (e.g., `main`, `v1.0.0`)

### Usage

**Pull the latest image:**
```bash
docker pull ghcr.io/<username>/pynode-dockerfile-generator:latest
```

**Pull a specific version:**
```bash
docker pull ghcr.io/<username>/pynode-dockerfile-generator:v1.0.0
docker pull ghcr.io/<username>/pynode-dockerfile-generator:<commit-sha>
```

**Run the image:**
```bash
docker run --rm -v $(pwd):/output ghcr.io/<username>/pynode-dockerfile-generator:latest create python -lv 3.12 --flavor slim
```

### Permissions

The workflow requires:
- `contents: read` - Read repository contents
- `packages: write` - Push to GitHub Container Registry

These permissions are automatically provided via `GITHUB_TOKEN`.

### Making the Package Public

By default, packages are private. To make your image public:

1. Go to your repository on GitHub
2. Navigate to **Packages** (right sidebar)
3. Click on your package
4. Go to **Package settings**
5. Scroll to **Danger Zone**
6. Click **Change visibility** → **Public**

### Manual Workflow Trigger

To manually trigger a build:

1. Go to **Actions** tab in your repository
2. Select **Build and Push** workflow
3. Click **Run workflow**
4. Select branch and click **Run workflow**

---

## Lint

**File:** `lint.yml`

Runs code quality checks on every push and pull request to ensure consistent code style and catch potential issues.

### Triggers

- **Push to main branch** - Runs on every commit to `main`
- **Pull requests** - Runs on all PRs targeting `main`

### Linting Tools

The workflow runs the following tools:

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **Black** | Code formatting | `--check` mode, line length: 88 |
| **isort** | Import statement sorting | `--check-only` mode |
| **Flake8** | Style guide enforcement (PEP 8) | Max line length: 88, ignores: E203, W503 |
| **MyPy** | Static type checking | `--ignore-missing-imports` |

---

## Code Security

**File:** `code-security.yml`

Analyzes Python code for security vulnerabilities and checks dependencies for known CVEs.

### Triggers

- **Push to main branch** - Runs on every commit to `main`
- **Pull requests** - Runs on all PRs targeting `main`

### Security Tools

The workflow uses two complementary security tools:

| Tool | Purpose | What It Finds |
|------|---------|---------------|
| **Bandit** | Static Application Security Testing (SAST) | SQL injection, shell injection, hardcoded secrets, unsafe YAML loading, weak cryptography |
| **pip-audit** | Dependency vulnerability scanner | Known CVEs in Python packages (click, jinja2, etc.) |

### What It Checks

**Bandit scans for:**
- Hardcoded passwords and secrets
- SQL injection vulnerabilities
- Shell injection risks
- Unsafe deserialization
- Weak cryptographic practices
- Assert statements in production code
- Insecure temporary file creation

**pip-audit checks for:**
- Known vulnerabilities in installed packages
- CVEs in project dependencies
- Outdated packages with security fixes available

### Viewing Results

**Workflow Logs:**
- Check the Actions tab for detailed output
- Bandit shows security issues with severity levels (HIGH, MEDIUM, LOW)
- pip-audit lists vulnerable packages with CVE IDs

**Artifact Download:**
- Download the `bandit-security-report.json` artifact from the workflow run
- Contains detailed JSON report for further analysis

---

## Trivy Security Scan

**File:** `trivy_scan.yml`

Scans the Docker image for security vulnerabilities using Trivy, an open-source vulnerability scanner.

### Triggers

- **Push to main branch** - Runs on every commit to `main`
- **Pull requests** - Runs on all PRs targeting `main`

### What It Scans

The workflow scans for:

- **Operating system vulnerabilities** - Base image (python:3.12-slim)
- **Application dependencies** - Python packages (click, jinja2)
- **Severity levels** - Focuses on CRITICAL and HIGH vulnerabilities
- **Known CVEs** - Common Vulnerabilities and Exposures database

### Scan Process

1. Builds the Docker image from `docker/Dockerfile`
2. Runs Trivy scan with SARIF output format
3. Uploads results to GitHub Security tab
4. Runs additional scan with table output
5. **Fails the workflow** if CRITICAL or HIGH vulnerabilities are found

### Viewing Results

**GitHub Security Tab:**
1. Go to your repository
2. Click on **Security** tab
3. Select **Code scanning alerts**
4. View Trivy findings with details and remediation advice

**Workflow Logs:**
- Check the Actions tab for table-formatted output
- Shows all detected vulnerabilities with severity levels

