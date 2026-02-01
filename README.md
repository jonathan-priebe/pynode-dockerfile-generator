# pynode-dockerfile-generator

**Automatically create production-ready Dockerfile templates for Python and Node.js**

A lightweight CLI tool that generates clean, minimal Dockerfile templates with customizable versions and distribution flavors. Eliminate repetitive boilerplate and maintain consistent Docker configurations across your projects.

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [CLI Usage](#cli-usage)
  - [Docker Usage](#docker-usage)
  - [Examples](#examples)
- [Command Reference](#command-reference)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- Support for Python and Node.js environments
- Customizable language versions (e.g., 3.12, 20, latest)
- Multiple distribution flavors (alpine, slim, etc.)
- Production-ready, minimal Dockerfile templates
- Docker and Docker Compose support
- Easy-to-use CLI with comprehensive help

## Quick Start

### Prerequisites
- Python 3.12 or higher
- pip package manager

### Using CLI (Python installed)

```bash
# Clone the repository
git clone https://github.com/yourusername/pynode-dockerfile-generator.git
cd pynode-dockerfile-generator

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the tool
pip install -e .

# Generate Python Dockerfile with version 3.12 and slim variant
dockerfile-generator create python -lv 3.12 --flavor slim

# Generate Node.js Dockerfile with alpine
dockerfile-generator create nodejs -lv 20 --flavor alpine
```

### Using Docker (No Python required)

```bash
# Build the Docker image
docker build -f docker/Dockerfile -t dockerfile-generator .

# Generate Dockerfile templates
docker run --rm -v $(pwd):/output dockerfile-generator create python -lv 3.12 --flavor slim
```

### Get Help

```bash
# CLI help
dockerfile-generator -h
dockerfile-generator create -h

# Docker help
docker run --rm dockerfile-generator -h
```

## Usage

### CLI Usage

**Basic Syntax:**
```bash
dockerfile-generator create <language> [OPTIONS]
```

**Arguments:**
- `<language>` - Required. Either `python` or `nodejs`

**Options:**
- `-lv, --language-version TEXT` - Version of Python/Node.js (default: latest)
- `--flavor TEXT` - Distribution variant (e.g., alpine, slim)
- `-o, --output-file PATH` - Output file path (default: `<timestamp>.Containerfile`)
- `-h, --help` - Show help message

### Docker Usage

```bash
# Using Docker directly
docker run --rm -v $(pwd):/output dockerfile-generator create python -lv 3.12 --flavor slim
# Ensure the current folder has its permissions set to chmod 777

# Using Docker Compose
docker-compose run --rm dockerfile-generator create nodejs -lv 20 --flavor alpine
```

Generated files are saved to the mounted output directory.

### Examples

```bash
# Generate Python Dockerfile with latest version
dockerfile-generator create python

# Generate Python 3.12 with slim variant
dockerfile-generator create python -lv 3.12 --flavor slim

# Generate Node.js 20 with Alpine Linux
dockerfile-generator create nodejs -lv 20 --flavor alpine

# Custom output file
dockerfile-generator create python -lv 3.11 -o MyPythonApp.Dockerfile

# Using Docker
docker run --rm -v $(pwd):/output dockerfile-generator create nodejs -lv 18
```

## Command Reference

### Main Command

```bash
dockerfile-generator COMMAND [ARGS] [OPTIONS]...
```

**Options:**
- `-h, --help` - Show help and exit

**Commands:**
- `create` - Create a new Dockerfile template

### create Command

Creates a Dockerfile template for the specified language.

```bash
dockerfile-generator create <language> [OPTIONS]
```

**Supported Languages:**
- `python` - Python Dockerfile templates
- `nodejs` - Node.js Dockerfile templates

**Options:**
| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--language-version` | `-lv` | Language version (e.g., 3.12, 20) | latest |
| `--flavor` | | Distribution flavor (alpine, slim) | none |
| `--output-file` | `-o` | Output file path | `<timestamp>.Containerfile` |
| `--help` | `-h` | Show command help | |

## Project Structure

```
pynode-dockerfile-generator/
├── src/
│   └── dockerfile_generator/
│       ├── cli.py                     # CLI interface
│       ├── generator.py               # Core generation logic
│       └── templates/
│           ├── python.dockerfile.j2   # Python template
│           └── nodejs.dockerfile.j2   # Node.js template
├── docs/                              
│   ├── cicd.md                        
│   ├── cli-implementation.md          
│   └── containerization.md            
├── docker/
│   ├── Dockerfile                     # Container image
│   └── entrypoint.sh                  # Container entrypoint
├── docker-compose.yml                 # Docker Compose config
├── requirements.txt                   # Python dependencies
├── setup.py                           # Package setup
└── README.md                          # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## test note