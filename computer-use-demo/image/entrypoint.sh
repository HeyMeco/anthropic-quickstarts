#!/bin/bash
set -e

# Set default hostname if not provided
export COMPUTER_USE_DEMO_HOST="${COMPUTER_USE_DEMO_HOST:-::}"
export COMPUTER_USE_DEMO_INTERFACE_HOST="${COMPUTER_USE_DEMO_INTERFACE_HOST:-localhost}"
export COMPUTER_USE_DEMO_PORT="${COMPUTER_USE_DEMO_PORT:-8080}"
export COMPUTER_USE_DEMO_VNC_HOST="${COMPUTER_USE_DEMO_VNC_HOST:-localhost}"
export COMPUTER_USE_DEMO_VNC_PORT="${COMPUTER_USE_DEMO_VNC_PORT:-5900}"
export COMPUTER_USE_DEMO_NOVNC_PORT="${COMPUTER_USE_DEMO_NOVNC_PORT:-6080}"
export STREAMLIT_SERVER_PORT="${STREAMLIT_SERVER_PORT:-8501}"

./start_all.sh
./novnc_startup.sh

# Generate HTML files with correct hostnames/ports
python generate_html.py

# Start HTTP server
python http_server.py > /tmp/server_logs.txt 2>&1 &

python -m streamlit run computer_use_demo/streamlit.py > /tmp/streamlit_stdout.log &

echo "✨ Computer Use Demo is ready!"
echo "➡️  Open http://${COMPUTER_USE_DEMO_INTERFACE_HOST}:${COMPUTER_USE_DEMO_PORT} in your browser to begin"

# Keep the container running
tail -f /dev/null
