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
            f"POST {endpoint} HTTP/1.1" + "\\r\\n" +
            f"Host: {host}:{port}" + "\\r\\n" +
            "Content-Type: application/json" + "\\r\\n" +
            f"Content-Length: {len(payload)}" + "\\r\\n" +
            "Connection: close" + "\\r\\n\\r\\n" +
            payload
        )
    else:
        request = (
            f"GET {endpoint} HTTP/1.1" + "\\r\\n" +
            f"Host: {host}:{port}" + "\\r\\n" +
            "Connection: close" + "\\r\\n\\r\\n"
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

# Explore southern grass towards the southeast where Gold Teeth is located
route = [
    (6, 20),
    (6, 21), (6, 22), # DOWN to row 22
    (7, 22), (8, 22), (9, 22), (10, 22), (11, 22), (12, 22), (13, 22), (14, 22), (15, 22), (16, 22), (17, 22), (18, 22), (19, 22), # RIGHT to col 19
    (19, 21), (19, 20), (19, 19), # Try walking UP to see if Gold Teeth is around (19, 19) or (19, 17)
    (19, 18), (19, 17), (19, 16)
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
print(f"Starting Southern Area exploration at {curr}")

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

print(f"Finished exploration. Final position: {get_coordinates()}")
