import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Talking to clerk again...")
    bridge.press_buttons(["Left", "sleep 300", "A", "sleep 1200"])
    time.sleep(2.0)
    
    pos = get_pos()
    print(f"Position: {pos}")
    # Take screenshot
    bridge.send_request("/api/screenshot")

if __name__ == "__main__":
    main()
