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

def surf():
    print("Initiating SURF with HYDROS...")
    # Start -> Pokémon (A) -> HYDROS (A) -> SURF (Down, Down, A or Down, A depending on menu)
    # Blastoise moves: Double-Edge, Ice Beam, Bite, Surf
    # HYDROS submenu: STATS, SWITCH, CANCEL or Field Move SURF!
    # Field moves on Pokemon menu appear at top or:
    # Let's check Pokemon menu: Select HYDROS (A) -> Menu options: [SURF, STATS, SWITCH, CANCEL]
    # For Surf, if on water edge, SURF is the first option!
    mgba.press_buttons([
        "Start", "sleep 250",
        "Down", "sleep 150", # cursor on POKéMON
        "A", "sleep 350",    # open POKéMON menu
        "A", "sleep 300",    # select HYDROS (Slot 1)
        "Down", "sleep 200", # In Gen 1, when facing water, does SURF appear? Actually, SURF is a field move: options are STATS, SWITCH, SURF or SURF is at top.
        # Wait, in Gen 1, if you can Surf, SURF is option 1 or option 2?
        # Let's check: in Gen 1, field move is at the TOP above STATS! So "A" selects SURF immediately!
        # Wait! If SURF is at top, pressing Down would move off it.
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

def walk_path(waypoints, max_total_steps=100):
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

print("Initial Pos:", get_pos())
