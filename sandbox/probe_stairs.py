import mgba
import time

def main():
    print(f"Current position: {mgba.get_coordinates()}")
    # Step Down to (7, 11)
    print("Stepping Down to (7, 11)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    print(f"Current position: {mgba.get_coordinates()}")
    
    # Step Up to (7, 10) to trigger warp
    print("Stepping Up to (7, 10) to trigger warp...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    print(f"Current position after warp attempt: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
