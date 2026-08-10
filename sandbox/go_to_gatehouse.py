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

# Path from current (5, 14) to Safari Zone Gatehouse door at (18, 3) in Fuchsia City
route = [
    (5, 14),
    (4, 14), (3, 14), # LEFT to col 3
    (3, 13), (3, 12), (3, 11), (3, 10), (3, 9), # UP to row 9
    (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), # RIGHT to col 8
    (8, 8), # UP to row 8
    (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), # RIGHT to col 16
    (16, 7), (16, 6), # UP to row 6
    (17, 6), (18, 6), # RIGHT to col 18
    (18, 5), (18, 4), # UP to row 4
    (18, 3) # UP to enter Gatehouse door
]

def get_dir(curr, target):
    cx, cy = curr
    tx, ty = target
    if tx > cx: return "Right"
    if tx < cx: return "Left"
    if ty > cy: return "Down"
    if ty < cy: return "Up"
    return None

curr = get_coordinates()
print(f"Starting Gatehouse run from {curr}")

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
            if target == (18, 3):
                print("Trying to press UP to enter Safari Gatehouse...")
                press_buttons(["Up", "sleep 1000"])
                after_up = get_coordinates()
                if after_up != curr:
                    print(f"Entered Gatehouse successfully! New coordinates: {after_up}")
                    break
                    
            print("Trying to clear stuck state with a B press...")
            press_buttons(["B", "sleep 300"])
            stuck_count = 0
    else:
        stuck_count = 0

print(f"Pathing finished. Current position: {get_coordinates()}")
