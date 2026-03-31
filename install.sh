#!/usr/bin/env bash

set -e  # Exit on error

echo "Starting server setup"
sleep 1

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 is not installed. Please install it first."
    exit 1
fi

echo "Python found: $(python3 --version)"
sleep 1

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "venv already exists, skipping creation!"
fi
sleep 1

# Activate venv
echo "Activating virtual environment..."
source venv/bin/activate
sleep 1

# Upgrade pip
echo "Installing and upgrading pip..."
pip install --upgrade pip
sleep 1

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found, installing Django only..."
    pip install django
fi
sleep 1

# Move into project folder
if [ -f "floorball_stats/manage.py" ]; then
    cd floorball_stats
else
    echo "Could not find manage.py in expected location."
    exit 1
fi

# Run migrations
echo "Running migrations to create database..."
python manage.py migrate
sleep 1

# Start server
echo "Starting server..."
echo "Open: http://127.0.0.1:8000/"
sleep 1

python manage.py runserver
