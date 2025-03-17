#!/usr/bin/env python3
import os
import sys

# Get environment variables with defaults
INTERFACE_HOST = os.environ.get('COMPUTER_USE_DEMO_INTERFACE_HOST', 'localhost')
STREAMLIT_PORT = os.environ.get('STREAMLIT_SERVER_PORT', '8501')
NOVNC_PORT = os.environ.get('COMPUTER_USE_DEMO_NOVNC_PORT', '6080')

# Template for index.html
INDEX_TEMPLATE = f"""<!doctype html>
<html>
    <head>
        <title>Computer Use Demo</title>
        <meta name="permissions-policy" content="fullscreen=*" />
        <style>
            body {{
                margin: 0;
                padding: 0;
                overflow: hidden;
            }}
            .container {{
                display: flex;
                height: 100vh;
                width: 100vw;
            }}
            .left {{
                flex: 1;
                border: none;
                height: 100vh;
            }}
            .right {{
                flex: 2;
                border: none;
                height: 100vh;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <iframe
                src="http://{INTERFACE_HOST}:{STREAMLIT_PORT}"
                class="left"
                allow="fullscreen"
            ></iframe>
            <iframe
                id="vnc"
                src="http://{INTERFACE_HOST}:{NOVNC_PORT}/vnc.html?&resize=scale&autoconnect=1&view_only=1&reconnect=1&reconnect_delay=2000"
                class="right"
                allow="fullscreen"
            ></iframe>
            <button
                id="toggleViewOnly"
                style="position: absolute; top: 10px; right: 10px; z-index: 1000"
            >
                Toggle Screen Control (Off)
            </button>
            <script>
                document
                    .getElementById("toggleViewOnly")
                    .addEventListener("click", function () {{
                        var vncIframe = document.getElementById("vnc");
                        var button = document.getElementById("toggleViewOnly");
                        var currentSrc = vncIframe.src;
                        if (currentSrc.includes("view_only=1")) {{
                            vncIframe.src = currentSrc.replace(
                                "view_only=1",
                                "view_only=0",
                            );
                            button.innerText = "Toggle Screen Control (On)";
                        }} else {{
                            vncIframe.src = currentSrc.replace(
                                "view_only=0",
                                "view_only=1",
                            );
                            button.innerText = "Toggle Screen Control (Off)";
                        }}
                    }});
            </script>
        </div>
    </body>
</html>
"""

def main():
    # Directory where HTML files should be generated
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static_content')
    
    # Ensure the directory exists
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    # Write the index.html file
    with open(os.path.join(static_dir, 'index.html'), 'w') as f:
        f.write(INDEX_TEMPLATE)
    
    print(f"Generated HTML files in {static_dir} using host {INTERFACE_HOST}")

if __name__ == "__main__":
    main() 