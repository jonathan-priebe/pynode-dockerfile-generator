FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY src/ ./src/
COPY setup.py .

# Install the package
RUN pip install --no-cache-dir -e .

# Add Group & User for better security
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Copy entrypoint script and set permissions
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && chown appuser:appgroup /entrypoint.sh

# Create output directory with correct permissions
RUN mkdir -p /output && chown appuser:appgroup /output

USER appuser:appgroup

# Set working directory to output folder
WORKDIR /output

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Default command (can be overridden)
CMD ["--help"]
