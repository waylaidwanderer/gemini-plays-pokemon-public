import bridge

def walk_down_to_ground():
    print("Walking down column 24 to reach Row 22 ground level...")
    # Walk Down 9 steps from (24, 13) to (24, 22)
    buttons = ["Down", "sleep 350"] * 9
    res = bridge.press_buttons(buttons)
    print(f"Response: {res}")
    print(f"Current coordinates: {bridge.get_coordinates()}")

if __name__ == "__main__":
    walk_down_to_ground()
