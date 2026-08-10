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
    
    # Parse JSON body (robustly handling chunked transfer encoding)
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

# The complete route to Area 3 (West) (26, 0)
route = [
    # Safari Zone Center
    (15, 25),
    (15, 24), (15, 23), (15, 22), (15, 21),
    (16, 21), (17, 21), (18, 21), (19, 21), (20, 21), (21, 21), (22, 21),
    (22, 20), (22, 19), (22, 18), (22, 17), (22, 16), (22, 15), (22, 14), (22, 13), (22, 12), (22, 11), (22, 10),
    (23, 10), (24, 10), (25, 10), (26, 10), (27, 10), (28, 10), (29, 10), (30, 10),

    # Area 1 (East)
    (0, 22),
    (1, 22), (2, 22), (3, 22), (4, 22), (5, 22), (5, 21), (6, 21), (7, 21), (7, 22), (8, 22), (9, 22), (10, 22), (11, 22), (12, 22), (13, 22), (14, 22), (15, 22), (16, 22), (17, 22), (18, 22), (19, 22), (20, 22),
    (20, 21),
    (20, 20),
    (19, 20), (18, 20), (17, 20), (16, 20), (15, 20), (14, 20), (13, 20), (12, 20),
    (12, 21),
    (12, 22),
    (11, 22), (10, 22), (9, 22), (8, 22),
    (8, 21), (8, 20), (8, 19), (8, 18), (8, 17), (8, 16), (8, 15), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (8, 8),
    (9, 8), (10, 8), (11, 8), (12, 8),
    (12, 7), (12, 6),
    (13, 6), (14, 6), (15, 6), (16, 6), (17, 6),
    (17, 7), (17, 8),
    (18, 8), (19, 8), (20, 8),
    (20, 7), (20, 6), (20, 5), (20, 4), (20, 3),
    (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3), (9, 3), (8, 3), (7, 3),
    (7, 4), (7, 5),
    (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5),

    # Area 2 (North)
    (39, 31),
    (38, 31), (37, 31), (36, 31), (35, 31), (34, 31), (33, 31), (32, 31), (31, 31), (30, 31), (29, 31), (28, 31), (27, 31), (26, 31), (25, 31), (24, 31), (23, 31), (22, 31), (21, 31), (20, 31), (19, 31), (18, 31), (17, 31), (16, 31), (15, 31), (14, 31), (13, 31), (12, 31), (11, 31), (10, 31), (9, 31), (8, 31),
    (8, 32), (8, 33), (8, 34), (8, 35), (8, 36)
]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    # Gen 1 battle escape: B multiple times, then Down/Right/A to RUN
    for _ in range(3):
        press_buttons(["B", "sleep 300"])
    press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
    # Clear got away safely text
    for _ in range(4):
        press_buttons(["B", "sleep 300"])
    print("RUN sequence finished.")

def get_dir(curr, target):
    cx, cy = curr
    tx, ty = target
    if tx > cx: return "Right"
    if tx < cx: return "Left"
    if ty > cy: return "Down"
    if ty < cy: return "Up"
    return None

def align_with_route(curr):
    for idx, coord in enumerate(route):
        if curr == coord:
            return idx
    return None

curr = get_coordinates()
print(f"Starting at overworld coordinate: {curr}")

route_idx = align_with_route(curr)
if route_idx is None:
    print("Error: Starting position not in route. Exiting.")
    exit(1)

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
        # Check if we transitioned to next coordinate
        if route_idx + 1 < len(route):
            next_target = route[route_idx + 1]
            if curr == next_target:
                print(f"Auto-transitioned/Warped to next target {next_target}!")
                route_idx += 2
                stuck_count = 0
                continue
        print(f"Error: Direction is None. Current {curr}, Target {target}. Exiting.")
        break
        
    print(f"Moving {direction} from {curr} towards {target}")
    press_buttons([direction, "sleep 300"])
    
    new_curr = get_coordinates()
    
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Didn't move. Current {curr}, Target {target}. Stuck count: {stuck_count}")
        if stuck_count >= max_stuck:
            run_away()
            # Recheck alignment
            after_run = get_coordinates()
            if after_run != curr:
                print(f"Moved after run sequence! New position: {after_run}")
                idx = align_with_route(after_run)
                if idx is not None:
                    route_idx = idx
                    print(f"Re-aligned with route at index {route_idx}")
                else:
                    print("Could not align after run sequence, exiting.")
                    break
            stuck_count = 0
    else:
        stuck_count = 0
        # Map transition detection via coordinate distance
        dist = abs(new_curr[0] - curr[0]) + abs(new_curr[1] - curr[1])
        if dist > 1:
            print(f"Map Transition detected! Moved from {curr} to {new_curr}")
            idx = align_with_route(new_curr)
            if idx is not None:
                route_idx = idx
                print(f"Aligned with route at index {route_idx} after transition")
            else:
                print("Transitioned but could not align with route. Exiting.")
                break

print("Finished walk_safari script.")
