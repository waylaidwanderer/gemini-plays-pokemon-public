import bridge
import time

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def test_pocket_collisions():
    print("Starting pocket collision probe...")
    # We are currently at (25, 24)
    # Let's try walking Left to (24, 24)
    print("Attempting Left to (24, 24)...")
    bridge.press_buttons(["Left", "sleep 350"])
    pos = get_pos()
    print(f"Current position: {pos}")
    
    if pos == (24, 24):
        # We are at (24, 24). Let's try walking Left to (23, 24)
        print("Attempting Left to (23, 24)...")
        bridge.press_buttons(["Left", "sleep 350"])
        pos = get_pos()
        print(f"Current position: {pos}")
        
        if pos == (23, 24):
            # Try walking Left to (22, 24) (should be signpost)
            print("Attempting Left into signpost at (22, 24)...")
            bridge.press_buttons(["Left", "sleep 350"])
            print(f"Position after Left: {get_pos()}")
            
            # Try walking Down to (23, 25) (fence)
            print("Attempting Down into fence at (23, 25)...")
            bridge.press_buttons(["Down", "sleep 350"])
            print(f"Position after Down: {get_pos()}")
            
            # Try walking Up to (23, 23) (ledge)
            print("Attempting Up into ledge at (23, 23)...")
            bridge.press_buttons(["Up", "sleep 350"])
            print(f"Position after Up: {get_pos()}")
            
            # Walk back Right to (24, 24)
            bridge.press_buttons(["Right", "sleep 350"])
            
        pos = get_pos()
        if pos == (24, 24):
            # Try walking Down to (24, 25) (fence)
            print("Attempting Down into fence at (24, 25)...")
            bridge.press_buttons(["Down", "sleep 350"])
            print(f"Position after Down: {get_pos()}")
            
            # Try walking Up to (24, 23) (ledge)
            print("Attempting Up into ledge at (24, 23)...")
            bridge.press_buttons(["Up", "sleep 350"])
            print(f"Position after Up: {get_pos()}")
            
            # Walk back Right to (25, 24)
            bridge.press_buttons(["Right", "sleep 350"])
            
    pos = get_pos()
    if pos == (25, 24):
        # Try walking Down to (25, 25) (fence)
        print("Attempting Down into fence at (25, 25)...")
        bridge.press_buttons(["Down", "sleep 350"])
        print(f"Position after Down: {get_pos()}")
        
        # Try walking Up to (25, 23) (ledge)
        print("Attempting Up into ledge at (25, 23)...")
        bridge.press_buttons(["Up", "sleep 350"])
        print(f"Position after Up: {get_pos()}")
        
        # Walk Right to (26, 24)
        bridge.press_buttons(["Right", "sleep 350"])
        
    pos = get_pos()
    if pos == (26, 24):
        # Try walking Down to (26, 25) (fence)
        print("Attempting Down into fence at (26, 25)...")
        bridge.press_buttons(["Down", "sleep 350"])
        print(f"Position after Down: {get_pos()}")
        
        # Try walking Up to (26, 23) (ledge)
        print("Attempting Up into ledge at (26, 23)...")
        bridge.press_buttons(["Up", "sleep 350"])
        print(f"Position after Up: {get_pos()}")
        
        # Walk back Left to (25, 24) to return to start
        bridge.press_buttons(["Left", "sleep 350"])

    print(f"Collision probe finished. Final position: {get_pos()}")

if __name__ == "__main__":
    test_pocket_collisions()
