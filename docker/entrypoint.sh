#!/bin/bash
set -e

# Execute the dockerfile-generator command with all passed arguments
exec dockerfile-generator "$@"
