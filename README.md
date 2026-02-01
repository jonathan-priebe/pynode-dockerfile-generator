## pynode-dockerfile-generator
**Simple Dockerfile template generator for Python and Node.js**

A lightweight and efficient tool that generates clean, ready-to-use Dockerfile templates for Python and Node.js projects. Perfect for rapid prototyping, consistent DevOps workflows, and avoiding repetitive boilerplate.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Install from source](#install-from-source)
- [Usage](#usage)
  - [Basic syntax](#basic-syntax)
  - [Examples](#examples)
  - [Command reference](#command-reference)

## Features

- Supports modern Python and Node.js environments  
- Produces minimal, production-ready Dockerfiles  
- Eliminates copy-paste errors and speeds up project setup

## Installation

### Prerequisites
- Python 3.12 or higher
- pip package manager

### Install from source
```bash
# Clone the repository
git clone https://github.com/yourusername/pynode-dockerfile-generator.git
cd pynode-dockerfile-generator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Usage

### Basic syntax
```bash
dockerfile-generator create  [OPTIONS]
```

### Examples
```bash
# Generate Python Dockerfile with latest version
dockerfile-generator create python

# Generate Python 3.10 Dockerfile with Alpine Linux
dockerfile-generator create python -lv 3.10 --flavor alpine

# Generate Node.js 18 Dockerfile with custom output file
dockerfile-generator create node -lv 18 -o MyNodeImageDefinition.Dockerfile
```

### Command reference

#### create

Creates a Dockerfile template for the specified language.

**Arguments:**
- `language` - Required. Either `python` or `node`

**Options:**
- `-lv, --language-version` - Version of Python or Node.js (default: `latest`)
- `--flavor` - Linux distribution variant (e.g., `alpine`, `slim`)
- `-o, --output-file` - Output file path (default: `<timestamp>.Containerfile`)
- `-h, --help` - Show help message