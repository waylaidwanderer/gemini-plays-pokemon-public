import socket
import json
import os

def send_request(endpoint, data=None):
    host = "127.0.0.1"
    port = int(os.environ.get("EMULATOR_BRIDGE_PORT", 9102))
    
    # Use raw bytes to avoid ANY string escaping bugs!
    if data is not None:
        payload = json.dumps(data).encode('utf-8')
        request = (
            f"POST {endpoint} HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            f"Content-Type: application/json\r\n"
            f"Content-Length: {len(payload)}\r\n"
            f"Connection: close\r\n\r\n"
        ).encode('utf-8') + payload
    else:
        request = (
            f"GET {endpoint} HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            f"Connection: close\r\n\r\n"
        ).encode('utf-8')
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(25)
    s.connect((host, port))
    s.sendall(request)
    
    response = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk
    s.close()
    
    # Parse JSON body safely
    parts = response.split(b"\r\n\r\n", 1)
    if len(parts) == 2:
        body = parts[1].decode('utf-8')
        start = body.find('{')
        end = body.rfind('}')
        if start != -1 and end != -1:
            return json.loads(body[start:end+1])
    return {"error": "Invalid HTTP response format"}

def get_coordinates():
    res = send_request("/api/coordinates")
    if "error" in res:
        print(f"Error getting coordinates: {res['error']}")
        return None
    return (res.get("x"), res.get("y"))

def press_buttons(buttons):
    if isinstance(buttons, str):
        buttons = [buttons]
    return send_request("/api/press_buttons", {"buttons": buttons})
