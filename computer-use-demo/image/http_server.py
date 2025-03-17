import os
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler


class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6


def run_server():
    os.chdir(os.path.dirname(__file__) + "/static_content")
    # Get hostname from environment variable or default to "::" (all IPv6 interfaces)
    hostname = os.environ.get('COMPUTER_USE_DEMO_HOST', '::')
    port = int(os.environ.get('COMPUTER_USE_DEMO_PORT', 8080))
    server_address = (hostname, port)
    httpd = HTTPServerV6(server_address, SimpleHTTPRequestHandler)
    print(f"Starting HTTP server on {hostname or '::'} port {port}...")  # noqa: T201
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
