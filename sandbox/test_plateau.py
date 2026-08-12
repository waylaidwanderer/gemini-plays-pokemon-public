import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Wild battle/interaction detected! Executing RUN sequence...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def test_climb():
    # 1. Walk Left from (28, 16) to (24, 16)
    # 2. Walk Up to (24, 15) and (24, 14) onto the Plateau
    # 3. Explore the boundaries on the plateau
    
    path_to_stairs = [
        "Left", "Left", "Left", "Left", # To (24, 16)
        "Up" # To (24, 15) (stairs)
    ]
    
    print("Walking to the stairs...")
    for direction in path_to_stairs:
        walk_step(direction)
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        print(f"Current pos: {pos}")
        
    # We should be on the stairs or plateau now. Let's walk UP more to be firmly on the plateau.
    print("Taking steps UP on the plateau...")
    for _ in range(3):
        walk_step("Up")
        pos = get_pos()
        if pos is None:
            run_away()
            pos = get_pos()
        print(f"Current pos on plateau: {pos}")

if __name__ == "__main__":
    test_climb()
