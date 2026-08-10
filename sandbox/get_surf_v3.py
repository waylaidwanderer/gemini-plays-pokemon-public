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

# Clean up obsolete get_surf_v2.py
if os.path.exists('get_surf_v2.py'):
    os.remove('get_surf_v2.py')
    print("Deleted obsolete get_surf_v2.py")

# Correct, complete, and highly optimized Safari Speedrun Route V3
route = [
    # --- PHASE 1: Safari Zone Center (East) to Area 1 (East) ---
    (27, 0),
    (27, 1), (27, 2), (27, 3), (27, 4), (27, 5), (27, 6), (27, 7), (27, 8), (27, 9), (27, 10),
    (28, 10), (29, 10), (30, 10), # Transition to Area 1 (East) at (0, 22)

    # --- PHASE 2: Area 1 (East) to Area 2 (North) ---
    (0, 22),
    (0, 23), (0, 24),
    (1, 24), (2, 24), (3, 24), (4, 24), (5, 24), (6, 24), (7, 24), (8, 24), (9, 24), (10, 24), (11, 24), (12, 24), (13, 24), (14, 24), (15, 24), (16, 24), (17, 24), (18, 24), (19, 24), (20, 24),
    (20, 23), (20, 22), (20, 21),
    (20, 20), # Climb stairs
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
    (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (-1, 5),

    # --- PHASE 3: Area 2 (North) to Area 3 (West) Northern compartment ---
    (39, 31),
    (38, 31), (37, 31), (36, 31), (35, 31), (34, 31), (33, 31), (32, 31), (31, 31), (30, 31), (29, 31), (28, 31), (27, 31), (26, 31), (25, 31), (24, 31), (23, 31), (22, 31),
    (22, 30), (22, 29), (22, 28), (22, 27), (22, 26), (22, 25), (22, 24), (22, 23),
    (22, 22), # Climb stairs
    (21, 22), (20, 22), (19, 22), (18, 22), (17, 22), (16, 22),
    (16, 23), (16, 24), (16, 25), (16, 26), (16, 27),
    (16, 28), # Descend stairs
    (16, 29), (16, 30), (16, 31), (16, 32), (16, 33),
    (15, 33), (14, 33), (13, 33), (12, 33), (11, 33), (10, 33), (9, 33), (8, 33),
    (8, 34), (8, 35), (8, 36), # Transition into Area 3 (West) at (26, 0) - Column 8!

    # --- PHASE 4: Area 3 (West) Northern compartment to Plateau Crossing ---
    (26, 0),
    (26, 1), (26, 2), (26, 3), (26, 4),
    (25, 4), (24, 4), (23, 4), (22, 4), (21, 4),
    (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 10), (21, 11), (21, 12), (21, 13), (21, 14), (21, 15), (21, 16), (21, 17), (21, 18),
    (20, 18), (19, 18), (18, 18), (17, 18), (16, 18), (15, 18), (14, 18), (13, 18), (12, 18), (11, 18), (10, 18), (9, 18), (8, 18), (7, 18), (6, 18),
    (6, 19),
    (6, 20), # Descend stairs to southern ground level!

    # --- PHASE 5: Area 3 (West) Southern compartment - Collect Gold Teeth ---
    (6, 21), (6, 22), (6, 23), (6, 24), (6, 25), (6, 26), # DOWN to row 26
    (7, 26), (8, 26), (9, 26), (10, 26), (11, 26), (12, 26), (13, 26), (14, 26), (15, 26), (16, 26), (17, 26), (18, 26), (19, 26), # RIGHT to col 19
    (19, 25), (19, 24), (19, 23), (19, 22), (19, 21), (19, 20), (19, 19), (19, 18), (19, 17), # At Gold Teeth!

    # --- PHASE 6: Walk to Secret House Entrance at (5, 13) ---
    (19, 18), (19, 19), (19, 20), (19, 21), (19, 22), (19, 23), (19, 24), (19, 25), (19, 26),
    (18, 26), (17, 26), (16, 26), (15, 26), (14, 26), (13, 26), (12, 26), (11, 26), (10, 26), (9, 26), (8, 26), (7, 26), (6, 26), (5, 26),
    (5, 25), (5, 24), (5, 23), (5, 22), (5, 21), (5, 20), (5, 19), (5, 18), (5, 17), (5, 16), (5, 15), (5, 14),
    (5, 13) # Enter Secret House!
]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(3):
        press_buttons(["B", "sleep 300"])
    press_buttons(["Right", "sleep 200", "Down", "sleep 200", "A", "sleep 1200"])
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
    best_idx = None
    min_dist = 999
    for idx, coord in enumerate(route):
        dist = abs(curr[0] - coord[0]) + abs(curr[1] - coord[1])
        if dist <= 2 and dist < min_dist:
            min_dist = dist
            best_idx = idx
    return best_idx

curr = get_coordinates()
print(f"Starting Golden Speedrun V3 from {curr}")

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
        # Check if we transitioned maps (which results in non-contiguous coordinate jumps)
        if route_idx + 1 < len(route):
            next_target = route[route_idx + 1]
            if curr == next_target:
                print(f"Map transition / Warp detected! Jumped to {next_target} (index {route_idx + 1})")
                route_idx += 2
                stuck_count = 0
                continue
        print(f"Error: Direction is None. Current {curr}, Target {target}. Exiting.")
        break
        
    print(f"Moving {direction} from {curr} towards {target}")
    press_buttons([direction, "sleep 350"])
    
    new_curr = get_coordinates()
    
    if new_curr == curr:
        stuck_count += 1
        print(f"Stuck! Didn't move. Current {curr}, Target {target}. Stuck count: {stuck_count}")
        if stuck_count >= max_stuck:
            # Check if we are at (19, 17) which is the Gold Teeth
            if curr == (19, 17):
                print("Trying to press A to pick up Gold Teeth...")
                press_buttons(["A", "sleep 1000"])
                press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
                route_idx += 1
                stuck_count = 0
                continue
                
            # Check if we are at (5, 13) which is the Secret House door
            if curr == (5, 14) and target == (5, 13):
                print("Trying to press UP to enter Secret House...")
                press_buttons(["Up", "sleep 1000"])
                after_up = get_coordinates()
                if after_up != curr:
                    print(f"Entered Secret House! New coordinates: {after_up}")
                    break
                    
            run_away()
            after_run = get_coordinates()
            if after_run != curr:
                idx = align_with_route(after_run)
                if idx is not None:
                    route_idx = idx
                    print(f"Re-aligned with route at index {route_idx} after run away.")
                else:
                    print("Could not align with route after run away, exiting.")
                    break
            stuck_count = 0
    else:
        stuck_count = 0
        dist = abs(new_curr[0] - curr[0]) + abs(new_curr[1] - curr[1])
        if dist > 1:
            print(f"Map Transition detected! Jumped from {curr} to {new_curr}")
            idx = align_with_route(new_curr)
            if idx is not None:
                route_idx = idx
                print(f"Aligned with route at index {route_idx} after transition.")
            else:
                print("Transitioned but could not align with route. Exiting.")
                break

print(f"Final coordinates: {get_coordinates()}")
