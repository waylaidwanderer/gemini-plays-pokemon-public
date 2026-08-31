import mgba
import time

def main():
    print("Coordinates before:", mgba.get_coordinates())
    # Try walking Left twice, then Down three times, checking coordinates at each step.
    for step in ["Left", "Left", "Down", "Down", "Down"]:
        mgba.press_buttons([step])
        time.sleep(0.5)
        print(f"Pressed {step}, current coords:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
