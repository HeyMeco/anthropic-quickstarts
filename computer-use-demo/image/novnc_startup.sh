#!/bin/bash
echo "starting noVNC"

# Get VNC hostname from environment variable or default to localhost
VNC_HOST="${COMPUTER_USE_DEMO_VNC_HOST:-localhost}"
VNC_PORT="${COMPUTER_USE_DEMO_VNC_PORT:-5900}"
NOVNC_PORT="${COMPUTER_USE_DEMO_NOVNC_PORT:-6080}"

# Start noVNC with explicit websocket settings
/opt/noVNC/utils/novnc_proxy \
    --vnc ${VNC_HOST}:${VNC_PORT} \
    --listen ${NOVNC_PORT} \
    --web /opt/noVNC \
    > /tmp/novnc.log 2>&1 &

# Wait for noVNC to start
timeout=10
while [ $timeout -gt 0 ]; do
    if netstat -tuln | grep -q ":${NOVNC_PORT} "; then
        break
    fi
    sleep 1
    ((timeout--))
done

echo "noVNC started successfully on port ${NOVNC_PORT}"
