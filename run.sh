#!/bin/bash

# Function to check if a command is available
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install SQLite3 if not installed
if ! command_exists sqlite3; then
    echo "Installing SQLite3..."
    sudo apt-get update
    sudo apt-get install -y sqlite3
fi

# Install Python3 if not installed
if ! command_exists python3; then
    echo "Installing Python3..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

# Clone the GitHub repository
echo "Cloning the Iotta GitHub repository..."
git clone https://github.com/Mtoal087/Iotta.git

echo "Setup complete!"
