import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    for _ in range(4):
        pos = bridge.get_coordinates()
        if pos is not None:
            return pos[0], pos[1]
        time.sleep(0.1)
    return None

def main():
    print("Probing path to the right and down...")
    pos = get_pos()
    print("Start pos:", pos)
    if pos is None:
        return
        
    # Let's walk Right, then Down
    path = ["Right", "Down", "Down", "Down", "Down", "Down"]
    for i, d in enumerate(path):
        p = get_pos()
        bridge.press_buttons([d])
        time.sleep(0.5)
        new_p = get_pos()
        print(f"Step {i}: Walked {d}, pos changed from {p} to {new_p}")
        if new_p == p:
            print("Blocked!")
            break

if __name__ == "__main__":
    main()
