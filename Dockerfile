# Use Ubuntu 22.04 as base image
FROM ubuntu:24.04

# Set environment variables to avoid interactive dialog during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package repository and install packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    git \
    git-extras && \
    # Clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a new user 'appuser'
RUN useradd -m appuser

# Switch to the new user
USER appuser

# Set the working directory
WORKDIR /home/appuser

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment
ENV PATH="/home/appuser/venv/bin:$PATH"

# Copy your Flask app to the container
COPY --chown=appuser:appuser . /home/appuser/app

# Install Python dependencies within the virtual environment
RUN pip install --no-cache-dir -r /home/appuser/app/requirements.txt

# Set the environment variable for Flask
ENV FLASK_APP=/home/appuser/app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port your app runs on
EXPOSE 5000

# Set the working directory to your app directory
WORKDIR /home/appuser/app

# Set the default command to run your app
CMD ["flask", "run", "--host=0.0.0.0"]
