import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Starting exact buy ticket sequence from Welcome prompt...")
    # Press A 10 times with very safe 1.1 second delays to ensure warp
    for i in range(1, 11):
        print(f"Pressing A {i}/10...")
        bridge.press_buttons(["A", "sleep 600"])
        time.sleep(1.1)
        
        pos = get_pos()
        print(f"Position: {pos}")
        if pos is not None and pos != (3, 2):
            # If we warp, our position will change from (3, 2) inside the Gatehouse
            print(f"SUCCESS! Warp occurred to: {pos}")
            return
            
    print("Completed 10 presses without warp.")

if __name__ == "__main__":
    main()
