import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        bridge.press_buttons(["sleep 50"])
    return None

def handle_battle():
    print("Wild battle detected! Escaping...")
    # Escapes from Safari Zone battle
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    escape_sequence = [
        "Down", "sleep 200",
        "Right", "sleep 200",
        "A", "sleep 1500"
    ]
    bridge.press_buttons(escape_sequence)
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 200"])
    bridge.press_buttons(["sleep 500"])

def main():
    print("=== FAST STEP BURNING TO EXIT SAFARI ZONE ===")
    
    # We are currently at (19, 24) in Area 3 (West).
    # First, let's walk back to (0, 11) in Safari Zone Center to be safe from grass and walls.
    # Path: Right to (21, 24) -> Right 2 steps.
    # Up to (21, 23) -> Up 1 step.
    # Right to (30, 23) -> Right 9 steps (transition to Center at (0, 11)).
    pos = get_pos()
    print("Starting pos:", pos)
    
    if pos == (19, 24):
        print("Walking to transition...")
        path = ["Right", "Right", "Up", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right"]
        for step in path:
            curr = get_pos()
            if curr is None:
                handle_battle()
                continue
            bridge.press_buttons([step])
            bridge.press_buttons(["sleep 150"])
            
    # Now we are inside Center, likely around (0, 11) or (1, 11)
    # Let's burn the remaining steps by walking back and forth between Column 1 and Column 2 on Row 11.
    print("Burning remaining steps...")
    step_toggle = True
    
    # We will press buttons up to 90 times per script execution to stay under the 100 limit.
    for i in range(85):
        pos = get_pos()
        if pos is None:
            handle_battle()
            continue
            
        # If we get warped out, pos will be inside the Gatehouse (around (4, 3))
        if pos[1] < 10 or pos[0] > 10:
            # We warped out!
            print(f"We have warped out of Safari Zone! Position is {pos}")
            break
            
        direction = "Right" if step_toggle else "Left"
        bridge.press_buttons([direction])
        bridge.press_buttons(["sleep 150"])
        step_toggle = not step_toggle
        
    print("Step burning cycle completed. Current position:", get_pos())

if __name__ == "__main__":
    main()
