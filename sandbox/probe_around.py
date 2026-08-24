import mgba
import sys

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    # Dismiss any text with B
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 2500"])
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])

def try_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    if pos_before == pos_after:
        # Check if we got into a battle
        mgba.press_buttons(["sleep 150"])
        pos_now = get_pos()
        if pos_now == pos_before:
            # Blocked by wall or battle
            # Try to press B just in case
            mgba.press_buttons(["B", "sleep 150"])
            pos_now2 = get_pos()
            if pos_now2 == pos_before:
                return False, "BLOCKED"
        # If we got into a battle, flee and return block status
        run_from_battle()
        return False, "BATTLE"
    else:
        # Step succeeded, step back to restore position
        opp_dir = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}[direction]
        mgba.press_buttons([opp_dir, "sleep 450"])
        return True, f"OPEN to {pos_after}"

pos = get_pos()
print(f"Current Position: {pos}")

for d in ["Up", "Down", "Left", "Right"]:
    ok, status = try_step(d)
    print(f"Direction {d:5}: {status}")
