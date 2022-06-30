import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json

hostName = "localhost"
serverPort = 8080

user = os.environ.get("USERNAME")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
ip_location = f"C:/Users/{user}/Documents/ip.json"
json.dump(ip, open(ip_location, "w"))
os.system("start chrome http://localhost:8080/")

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<p>HI! YOUR IP IS...</p>", "utf-8"))
        self.wfile.write(bytes(f"<p>{ip}.</p>", "utf-8"))
        self.wfile.write(bytes(f"<p>NOW PISS OFF</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
