import socket
import json
import os
import time

def send_bridge_request(endpoint, data=None):
    host = "127.0.0.1"
    port = int(os.environ.get("EMULATOR_BRIDGE_PORT", 9102))
    
    # Construct raw HTTP payload
    if data is not None:
        payload = json.dumps(data)
        request = (
            f"POST {endpoint} HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            f"Content-Type: application/json\r\n"
            f"Content-Length: {len(payload)}\r\n"
            f"Connection: close\r\n\r\n"
            f"{payload}"
        )
    else:
        request = (
            f"GET {endpoint} HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            f"Connection: close\r\n\r\n"
        )
        
    # Open socket and transmit
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((host, port))
    s.sendall(request.encode('utf-8'))
    
    # Read response
    response = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk
    s.close()
    
    # Parse JSON body
    parts = response.split(b"\r\n\r\n", 1)
    if len(parts) == 2:
        body = parts[1].decode('utf-8')
        start = body.find('{')
        end = body.rfind('}')
        if start != -1 and end != -1:
            json_str = body[start:end+1]
            return json.loads(json_str)
    return {"error": "Invalid HTTP response format"}

def get_coordinates():
    res = send_bridge_request("/api/coordinates")
    if "error" in res:
        print(f"Error getting coordinates: {res['error']}")
        return None
    return (res.get("x"), res.get("y"))

def press_buttons(buttons):
    if isinstance(buttons, str):
        buttons = [buttons]
    return send_bridge_request("/api/press_buttons", {"buttons": buttons})

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(3):
        press_buttons(["B", "sleep 300"])
    press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    for _ in range(4):
        press_buttons(["B", "sleep 300"])
    print("RUN sequence finished.")

curr = get_coordinates()
print(f"Starting grass crossing from {curr}")

stuck_count = 0
while True:
    curr = get_coordinates()
    if curr is None:
        break
        
    # If we transitioned to Area 1 (East), we are done!
    # Area 1 (East) starts at column 0.
    # We can detect transition by checking if x becomes 0 or 1, and the map changed (or we are at (0, 22)/(0, 23))
    if curr == (0, 22) or curr == (0, 23) or curr == (0, 24):
        print(f"Successfully transitioned to Area 1 (East) at {curr}!")
        break
        
    # If we somehow bypassed and went further into Area 1
    if curr[0] == 1 and curr[1] in [22, 23, 24]:
        print(f"Already inside Area 1 (East) at {curr}!")
        break
        
    print(f"Moving Right from {curr}")
    press_buttons(["Right", "sleep 350"])
    new_curr = get_coordinates()
    
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Stuck count: {stuck_count}")
        if stuck_count >= 2:
            run_away()
            after_run = get_coordinates()
            print(f"Position after running: {after_run}")
            
            # Re-align back to walkable rows/cols
            if after_run == (28, 11):
                print("Moving back UP to (28, 10)...")
                press_buttons(["Up", "sleep 350"])
            elif after_run == (29, 11):
                # We are already on Column 29! Just walk Right!
                print("Already on Column 29, row 11. Trying to walk Right to transition...")
                press_buttons(["Right", "sleep 350"])
            stuck_count = 0
    else:
        stuck_count = 0

print(f"Grass crossing finished. Current position: {get_coordinates()}")
