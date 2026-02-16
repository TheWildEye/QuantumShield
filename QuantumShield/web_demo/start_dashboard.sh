#!/bin/bash

echo "======================================"
echo "KEMTLS Dashboard Startup"
echo "======================================"
echo ""

# Check if we're in the right directory
if [ ! -f "app_enhanced.py" ]; then
    echo "ERROR: app_enhanced.py not found!"
    echo "Please run this script from the web_demo directory"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
python3 -c "import flask; import flask_sock" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
fi

echo "✓ Dependencies OK"
echo ""
echo "Starting KEMTLS Dashboard Server..."
echo ""
echo "Dashboard URL: http://localhost:9000/dashboard"
echo "Original Demo: http://localhost:9000/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "======================================"
echo ""

# Run the enhanced app
python3 app_enhanced.py
