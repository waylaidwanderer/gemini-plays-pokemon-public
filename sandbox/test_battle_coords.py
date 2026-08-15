import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Probing collisions from current position...")
    pos = get_pos()
    print(f"Starting Position: {pos}")
    
    # Try Left
    print("Testing Left...")
    bridge.press_buttons(["Left", "sleep 400"])
    p_left = get_pos()
    print(f"Position after Left: {p_left}")
    if p_left != pos:
        bridge.press_buttons(["Right", "sleep 400"]) # step back
        
    # Try Right
    print("Testing Right...")
    bridge.press_buttons(["Right", "sleep 400"])
    p_right = get_pos()
    print(f"Position after Right: {p_right}")
    if p_right != pos:
        bridge.press_buttons(["Left", "sleep 400"]) # step back
        
    # Try Up
    print("Testing Up...")
    bridge.press_buttons(["Up", "sleep 400"])
    p_up = get_pos()
    print(f"Position after Up: {p_up}")
    if p_up != pos:
        bridge.press_buttons(["Down", "sleep 400"]) # step back
        
    # Try Down
    print("Testing Down...")
    bridge.press_buttons(["Down", "sleep 400"])
    p_down = get_pos()
    print(f"Position after Down: {p_down}")
    if p_down != pos:
        bridge.press_buttons(["Up", "sleep 400"]) # step back

if __name__ == "__main__":
    main()
