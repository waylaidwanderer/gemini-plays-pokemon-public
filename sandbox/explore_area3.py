import socket
import json
import os
import time

def send_bridge_request(endpoint, data=None):
    host = "127.0.0.1"
    port = int(os.environ.get("EMULATOR_BRIDGE_PORT", 9102))
    if data is not None:
        payload = json.dumps(data)
        request = (
            f"POST {endpoint} HTTP/1.1\\r\\n"
            f"Host: {host}:{port}\\r\\n"
            f"Content-Type: application/json\\r\\n"
            f"Content-Length: {len(payload)}\\r\\n"
            f"Connection: close\\r\\n\\r\\n"
            f"{payload}"
        )
    else:
        request = (
            f"GET {endpoint} HTTP/1.1\\r\\n"
            f"Host: {host}:{port}\\r\\n"
            f"Connection: close\\r\\n\\r\\n"
        )
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((host, port))
    s.sendall(request.encode('utf-8'))
    response = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk
    s.close()
    parts = response.split(b"\\r\\n\\r\\n", 1)
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

# Route to bottom of west stairs at (6, 20) in Area 3 (West)
route = [
    (26, 0),
    (25, 0), (24, 0), (23, 0), (22, 0), (21, 0),
    (21, 1), (21, 2), (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 10), (21, 11), (21, 12), (21, 13), (21, 14), (21, 15), (21, 16), (21, 17), (21, 18),
    (21, 17), # UP onto stairs
    (21, 16), # UP onto plateau
    (20, 16), (19, 16), (18, 16), (17, 16), (16, 16), (15, 16), (14, 16), (13, 16), (12, 16), (11, 16), (10, 16), (9, 16), (8, 16), (7, 16), (6, 16),
    (6, 17), (6, 18), (6, 19), (6, 20)
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
print(f"Starting Area 3 walk at {curr}")

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
    press_buttons([direction, "sleep 300"])
    
    new_curr = get_coordinates()
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Stuck count: {stuck_count}")
        if stuck_count >= max_stuck:
            run_away()
            after_run = get_coordinates()
            if after_run != curr:
                print(f"Moved after run sequence! New position: {after_run}")
                for idx, coord in enumerate(route):
                    if after_run == coord:
                        route_idx = idx
                        print(f"Re-aligned with route at index {route_idx}")
                        break
            stuck_count = 0
    else:
        stuck_count = 0

print(f"Arrived at bottom of west stairs: {get_coordinates()}")
