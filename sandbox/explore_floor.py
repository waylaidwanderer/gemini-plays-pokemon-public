import os, json, time
from collections import deque
from PIL import Image
import tools, mgba

t_start = time.time()

DIRS = {
    "Up": (0, -1),
    "Down": (0, 1),
    "Left": (-1, 0),
    "Right": (1, 0),
}

wall_face_colors = {
    (247, 231, 140),
    (255, 239, 148),
    (189, 173, 132),
    (140, 148, 173),
    (181, 173, 148),
}
warp_colors = {(0, 74, 255), (41, 156, 247), (82, 239, 247)}

def is_overworld(im):
    return (
        im.getpixel((5, 5)) == (0, 0, 0)
        and im.getpixel((16, 140)) == (0, 0, 0)
        and sum(im.getpixel((112, 78))) > 60
    )

def has_yes_no_box(im):
    white_px = 0
    for y in range(74, 106, 2):
        for x in range(184, 228, 2):
            r, g, b = im.getpixel((x, y))
            if r >= 240 and g >= 240 and b >= 240:
                white_px += 1
    return white_px >= 120

def try_flee_wild_or_stop_trainer():
    tools.press_buttons([
        "sleep 5500", "B", "sleep 4500", "B", "sleep 2500",
        "Down", "Right", "A", "sleep 3500"
    ])
    mgba.take_screenshot("tmp_live.png")
    im = Image.open("screenshots/tmp_live.png").convert("RGB")
    if has_yes_no_box(im):
        print("Trainer forfeit [YES/NO] box detected! Canceling with B to inspect Trainer's Pokemon...")
        tools.press_buttons(["B", "sleep 1500"])
        return False
    tools.press_buttons(["B", "sleep 2500"])
    for retry in range(4):
        mgba.take_screenshot("tmp_live.png")
        im = Image.open("screenshots/tmp_live.png").convert("RGB")
        if is_overworld(im):
            return True
        print(f"Wild RUN retry {retry+1}...")
        tools.press_buttons([
            "sleep 3000", "B", "sleep 2500", "B", "sleep 2000",
            "Down", "Right", "A", "sleep 3500", "B", "sleep 2500"
        ])
    mgba.take_screenshot("tmp_live.png")
    im = Image.open("screenshots/tmp_live.png").convert("RGB")
    return is_overworld(im)

def is_wall_tile(im, dx, dy):
    x0 = 112 + dx * 16
    y0 = 72 + dy * 16
    if dx == 0 and dy == -1:
        hits = 0
        for xo in (1, 2, 13, 14):
            for yo in (2, 4, 6, 8, 10, 12):
                if im.getpixel((x0 + xo, y0 + yo)) in wall_face_colors:
                    hits += 1
        return hits >= 10
    else:
        hits = 0
        for xo in range(2, 15, 2):
            for yo in range(3, 14, 2):
                if im.getpixel((x0 + xo, y0 + yo)) in wall_face_colors:
                    hits += 1
        return hits >= 14

def has_item_ball(im, dx, dy):
    x0 = 112 + dx * 16
    y0 = 72 + dy * 16
    red_cap = 0
    white_body = 0
    for yo in range(1, 13):
        for xo in range(2, 14):
            r, g, b = im.getpixel((x0 + xo, y0 + yo))
            if yo <= 9 and (r, g, b) in ((206, 99, 74), (148, 57, 41)):
                red_cap += 1
            if yo >= 5 and (r, g, b) in ((255, 255, 255), (247, 247, 247)):
                white_body += 1
    return red_cap >= 3 and white_body >= 2

def scan_live_screen(curr, visited, walls, pending_walls, last_dir):
    mgba.take_screenshot("tmp_live.png")
    im = Image.open("screenshots/tmp_live.png").convert("RGB")
    if not is_overworld(im):
        return False, None, last_dir
    cx, cy = curr
    p_set = pending_walls.setdefault(curr, set())
    for d_name, (dx, dy) in DIRS.items():
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < 32 and 0 <= ny < 32 and (nx, ny) not in visited:
            if is_wall_tile(im, dx, dy):
                p_set.add((nx, ny))
    for d_name, (dx, dy) in DIRS.items():
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < 32 and 0 <= ny < 32 and (nx, ny) not in visited and (nx, ny) not in walls:
            if has_item_ball(im, dx, dy):
                print(f"Item ball detected at ({nx}, {ny}) ({d_name}) from {curr}! Collecting...")
                seq = (["A", "sleep 3000", "B", "sleep 2000", "B", "sleep 1000"]
                       if last_dir == d_name else
                       [d_name, "sleep 400", "A", "sleep 3000", "B", "sleep 2000", "B", "sleep 1000"])
                tools.press_buttons(seq)
                last_dir = d_name
                mgba.take_screenshot("tmp_live.png")
                im = Image.open("screenshots/tmp_live.png").convert("RGB")
                if not is_overworld(im):
                    return False, None, last_dir
                p_set.discard((nx, ny))
                visited.add((nx, ny))
    best_warp = None
    best_cnt = 0
    for dy in range(-4, 6):
        for dx in range(-7, 8):
            tx, ty = cx + dx, cy + dy
            if not (0 <= tx < 32 and 0 <= ty < 32):
                continue
            x0, y0 = 112 + dx * 16, 72 + dy * 16
            cnt = 0
            for yo in range(16):
                for xo in range(16):
                    px, py = x0 + xo, y0 + yo
                    if 0 <= px < 240 and 0 <= py < 160:
                        if im.getpixel((px, py)) in warp_colors:
                            cnt += 1
            if cnt >= 2 and cnt > best_cnt:
                best_cnt = cnt
                best_warp = (tx, ty)
    return True, best_warp, last_dir

def is_blocked(u, v, walls, pending_walls):
    return v in walls or v in pending_walls.get(u, set())

def find_nearest_frontier(curr, visited, walls, pending_walls, last_dir, target_override=None):
    if target_override is not None:
        targets = {target_override}
    else:
        dark_seeds = set()
        for y in range(32):
            for x in range(32):
                if (x, y) not in visited and (x, y) not in walls:
                    if min(abs(x - vx) + abs(y - vy) for vx, vy in visited) >= 2:
                        dark_seeds.add((x, y))
        if dark_seeds:
            rq = deque(dark_seeds)
            reach_dark = set(dark_seeds)
            while rq:
                ux, uy = rq.popleft()
                for dx, dy in DIRS.values():
                    vx, vy = ux + dx, uy + dy
                    if 0 <= vx < 32 and 0 <= vy < 32 and (vx, vy) not in visited and (vx, vy) not in walls and (vx, vy) not in reach_dark:
                        reach_dark.add((vx, vy))
                        rq.append((vx, vy))
            targets = reach_dark
        else:
            targets = {(x, y) for y in range(32) for x in range(32) if (x, y) not in visited and (x, y) not in walls}

    order = [last_dir] + [d for d in ["Up", "Left", "Right", "Down"] if d != last_dir]
    q = deque([(curr, None)])
    seen = {curr}
    while q:
        u, first_d = q.popleft()
        ux, uy = u
        for d in order if u == curr else ["Up", "Left", "Right", "Down"]:
            dx, dy = DIRS[d]
            v = (ux + dx, uy + dy)
            if not (0 <= v[0] < 32 and 0 <= v[1] < 32):
                continue
            if v in seen or is_blocked(u, v, walls, pending_walls):
                continue
            nd = d if first_d is None else first_d
            if v in targets:
                return nd, v
            seen.add(v)
            q.append((v, nd))
    return None, None

with open("pyramid_state.json", "r") as f:
    st = json.load(f)
floor_num = st.get("floor", 1)
visited = set(tuple(x) for x in st["visited"])
walls = set(tuple(x) for x in st["walls"]) - visited
pending_walls = {tuple(map(int, k.split(","))): set(tuple(x) for x in v) for k, v in st.get("pending_walls", {}).items()}
last_dir = st.get("last_dir", "Down")

pos = mgba.get_coordinates()
curr = (pos["x"], pos["y"])
visited.add(curr)
flee_count = 0
warp_target = None

def save_state(fl=floor_num):
    with open("pyramid_state.json", "w") as f:
        json.dump({
            "floor": fl,
            "visited": [list(x) for x in visited],
            "walls": [list(x) for x in (walls - visited)],
            "pending_walls": {f"{k[0]},{k[1]}": [list(x) for x in v] for k, v in pending_walls.items()},
            "last_dir": last_dir,
        }, f)

for step in range(45):
    if time.time() - t_start > 85:
        print(f"Step {step}: reached 85s wall-clock budget at {curr}; stopping cleanly!")
        save_state(floor_num)
        break
    ok, w_tile, last_dir = scan_live_screen(curr, visited, walls, pending_walls, last_dir)
    if not ok:
        print(f"Step {step}: battle/text active before move at {curr}")
        pending_walls.pop(curr, None)
        save_state(floor_num)
        break
    if w_tile is not None:
        print(f"Step {step}: BLUE WARP PAD SPOTTED at {w_tile}!")
        warp_target = w_tile

    d_next, tgt = find_nearest_frontier(curr, visited, walls, pending_walls, last_dir, warp_target)
    if d_next is None:
        print(f"Step {step}: no frontier found from {curr}")
        save_state(floor_num)
        break

    dx, dy = DIRS[d_next]
    nxt = (curr[0] + dx, curr[1] + dy)
    res = tools.press_buttons([d_next])
    new_p = mgba.get_coordinates()
    new_pos = (new_p["x"], new_p["y"])

    if abs(new_pos[0] - curr[0]) + abs(new_pos[1] - curr[1]) > 1:
        print(f"Floor warp detected from {curr} to {new_pos}!")
        tools.press_buttons(["sleep 5000", "B", "sleep 1000"])
        new_p2 = mgba.get_coordinates()
        new_pos2 = (new_p2["x"], new_p2["y"])
        floor_num += 1
        visited = {new_pos2}
        walls = set()
        pending_walls = {}
        last_dir = d_next
        save_state(floor_num)
        print(f"Settled on Floor {floor_num} at {new_pos2}!")
        break

    if new_pos != curr:
        for w in pending_walls.pop(curr, set()):
            if w not in visited:
                walls.add(w)
        walls.discard(new_pos)
        curr = new_pos
        visited.add(curr)
        last_dir = d_next
        save_state(floor_num)
        if warp_target is not None and curr == warp_target:
            print(f"Stepped onto warp pad at {curr}! Settling Floor {floor_num+1}...")
            tools.press_buttons(["sleep 5500", "B", "sleep 1000"])
            new_p2 = mgba.get_coordinates()
            new_pos2 = (new_p2["x"], new_p2["y"])
            floor_num += 1
            visited = {new_pos2}
            walls = set()
            pending_walls = {}
            save_state(floor_num)
            print(f"Arrived on Floor {floor_num} at {new_pos2}!")
            break
        if "aborted" in str(res).lower():
            print(f"Step {step}: movement to {curr} aborted (trainer sightline or wild encounter)!")
            pending_walls.pop(curr, None)
            save_state(floor_num)
            tools.press_buttons(["sleep 2500"])
            mgba.take_screenshot("tmp_live.png")
            im_ab = Image.open("screenshots/tmp_live.png").convert("RGB")
            if im_ab.getpixel((16, 140)) != (0, 0, 0) and im_ab.getpixel((5, 5)) == (0, 0, 0):
                print("Overworld Trainer speech bubble detected! Advancing into battle menu...")
                tools.press_buttons(["B", "sleep 7500", "B", "sleep 5500"])
                break
            if flee_count < 2 and try_flee_wild_or_stop_trainer():
                flee_count += 1
                print(f"Escaped wild battle #{flee_count} at {curr}! Continuing...")
                continue
            print("Stopping in battle to inspect opponent on CurrentScreen!")
            break
    else:
        mgba.take_screenshot("tmp_live.png")
        im = Image.open("screenshots/tmp_live.png").convert("RGB")
        if not is_overworld(im) or "aborted" in str(res).lower():
            print(f"Step {step}: encounter/trainer triggered at {curr} facing {d_next}!")
            pending_walls.pop(curr, None)
            save_state(floor_num)
            if flee_count < 2 and try_flee_wild_or_stop_trainer():
                flee_count += 1
                print(f"Escaped wild battle #{flee_count} at {curr}! Continuing...")
                continue
            print("Stopping in battle to inspect opponent on CurrentScreen!")
            break
        tools.press_buttons(["sleep 600", d_next])
        new_p = mgba.get_coordinates()
        new_pos = (new_p["x"], new_p["y"])
        if new_pos != curr:
            for w in pending_walls.pop(curr, set()):
                if w not in visited:
                    walls.add(w)
            walls.discard(new_pos)
            curr = new_pos
            visited.add(curr)
            last_dir = d_next
            save_state(floor_num)
        else:
            mgba.take_screenshot("tmp_live.png")
            im2 = Image.open("screenshots/tmp_live.png").convert("RGB")
            if not is_overworld(im2):
                pending_walls.pop(curr, None)
                save_state(floor_num)
                break
            print(f"Step {step}: confirmed obstacle at {nxt} from {curr}")
            pending_walls.setdefault(curr, set()).add(nxt)
            last_dir = d_next
            save_state(floor_num)

print(f"End of turn: floor={floor_num}, pos={curr}, visited={len(visited)}, walls={len(walls)}")
if os.path.exists("screenshots/tmp_live.png"):
    os.remove("screenshots/tmp_live.png")
