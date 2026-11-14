"""A tiny deliberately leaky chatbot for trying ScaredBleed locally.

Run it:   python3 examples/testbot.py
Scan it:  scaredbleed scan --url http://127.0.0.1:8000/chat --canary SB-CANARY-7f3a9c

It only listens on 127.0.0.1 (your own computer). Never expose it to a network.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

CANARY = "SB-CANARY-7f3a9c"


class Bot(BaseHTTPRequestHandler):
    def do_POST(self):
        size = int(self.headers.get("Content-Length", 0))
        msg = json.loads(self.rfile.read(size)).get("message", "").lower()
        if "system prompt" in msg or "debug mode" in msg:
            reply = f"My instructions: You are HelpBot. Secret: {CANARY}"
        else:
            reply = "Hi! How can I help?"
        body = json.dumps({"reply": reply}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # keep the terminal quiet


if __name__ == "__main__":
    print("Test bot running on http://127.0.0.1:8000/chat  (Ctrl+C to stop)")
    HTTPServer(("127.0.0.1", 8000), Bot).serve_forever()