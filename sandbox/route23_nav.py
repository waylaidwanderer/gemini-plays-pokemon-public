import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    return p['x'], p['y']

def clear_dialogue_or_battle():
    # Attempt to clear dialogue first with A/B, then try RUN if in battle
    mgba.press_buttons(["A", "sleep 150", "B", "sleep 150", "A", "sleep 150", "B", "sleep 150"])
    # Run from battle: Down -> Right -> A
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A", "sleep 400", "B", "sleep 200", "B", "sleep 100"])

def start_surf():
    print("Initiating SURF with HYDROS...")
    # Start -> Down to POKéMON -> A -> HYDROS is slot 1 -> A -> In Gen 1 field menu for water: SURF is top option -> A
    # Then text appears "HYDROS used SURF!" -> press A/B to advance
    mgba.press_buttons([
        "Start", "sleep 250",
        "Down", "sleep 150",
        "A", "sleep 350",
        "A", "sleep 350",
        "A", "sleep 400",
        "A", "sleep 400",
        "B", "sleep 300",
        "B", "sleep 300"
    ])

def move_step(d):
    old_x, old_y = get_pos()
    mgba.press_buttons([d, "sleep 200"])
    new_x, new_y = get_pos()
    if (new_x, new_y) == (old_x, old_y):
        # We might have hit a dialogue or wild battle
        clear_dialogue_or_battle()
        mgba.press_buttons([d, "sleep 200"])
        new_x, new_y = get_pos()
    return new_x, new_y

def walk_path(waypoints, max_total_steps=120):
    total = 0
    for wx, wy in waypoints:
        while total < max_total_steps:
            x, y = get_pos()
            if x == wx and y == wy:
                print(f"Reached waypoint ({wx}, {wy})")
                break
            
            if x < wx:
                d = "Right"
            elif x > wx:
                d = "Left"
            elif y < wy:
                d = "Down"
            elif y > wy:
                d = "Up"
            
            move_step(d)
            total += 1
        if total >= max_total_steps:
            print(f"Reached max steps budget! Pos: {get_pos()}")
            break

print("Ready.")
