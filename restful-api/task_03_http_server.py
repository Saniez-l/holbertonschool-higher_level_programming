#!/usr/bin/python3
"""
Module for api server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Class api server
    """
    def do_GET(self):
        """
        Module api seerver do_GET
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"

            }
            response = json.dumps(sample_data)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000
server_adress = ("", PORT)

httpd = HTTPServer(server_adress, SimpleHTTPRequestHandler)
print("serving at port", PORT)
httpd.serve_forever()
