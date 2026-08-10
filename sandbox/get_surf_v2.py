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

# Path from current (8, 10) to Secret House door at (5, 13)
route = [
    (8, 10),
    (8, 9), # UP
    (7, 9), (6, 9), (5, 9), (4, 9), (3, 9), # LEFT to col 3
    (3, 10), (3, 11), (3, 12), (3, 13), # DOWN to row 13
    (4, 13), (5, 13) # RIGHT to the door
]

def get_dir(curr, target):
    cx, cy = curr
    tx, ty = target
    if tx > cx: return "Right"
    if tx < cx: return "Left"
    if ty > cy: return "Down"
    if ty < cy: return "Up"
    return None

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(3):
        press_buttons(["B", "sleep 300"])
    press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    for _ in range(4):
        press_buttons(["B", "sleep 300"])
    print("RUN sequence finished.")

curr = get_coordinates()
print(f"Starting Secret House run from {curr}")

route_idx = 0
for idx, coord in enumerate(route):
    if curr == coord:
        route_idx = idx
        break

print(f"Matched route index: {route_idx}")

stuck_count = 0
max_stuck = 3

while route_idx < len(route):
    target = route[route_idx]
    curr = get_coordinates()
    
    if curr == target:
        print(f"Arrived at target {target} (index {route_idx})")
        route_idx += 1
        stuck_count = 0
        continue
        
    direction = get_dir(curr, target)
    if direction is None:
        print(f"Error: Direction is None. Current {curr}, Target {target}. Exiting.")
        break
        
    print(f"Moving {direction} from {curr} towards {target}")
    press_buttons([direction, "sleep 350"])
    
    new_curr = get_coordinates()
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Stuck count: {stuck_count}")
        if stuck_count >= max_stuck:
            if target == (5, 13):
                print("Trying to press UP to enter Secret House...")
                press_buttons(["Up", "sleep 1000"])
                after_up = get_coordinates()
                if after_up != curr:
                    print(f"Entered Secret House successfully! New coordinates: {after_up}")
                    break
                    
            run_away()
            after_run = get_coordinates()
            if after_run != curr:
                print(f"Moved after run sequence! New position: {after_run}")
                for idx, coord in enumerate(route):
                    if after_run == coord:
                        route_idx = idx
                        break
            stuck_count = 0
    else:
        stuck_count = 0

# If we reached (5, 13), try entering
curr = get_coordinates()
if curr == (5, 13):
    print("Arrived at (5, 13). Pressing UP to enter Secret House...")
    press_buttons(["Up", "sleep 1000"])
    after_up = get_coordinates()
    print(f"Final coordinates: {after_up}")
else:
    print(f"Did not reach (5, 13). Current position: {curr}")
