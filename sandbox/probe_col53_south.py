import mgba

def main():
    print("=== Probing Column 53 South Exit ===")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")

    # Walk Right 13 steps from (40, 14) to (53, 14)
    path_right = ["Right"] * 13
    mgba.press_buttons(path_right)
    pos = mgba.get_coordinates()
    print(f"Pos at (53, 14): {pos}")

    # Step Down to (53, 15)
    mgba.press_buttons(["Down"])
    pos = mgba.get_coordinates()
    print(f"Pos after Down to (53, 15): {pos}")

    # Try stepping Down into (53, 16)
    mgba.press_buttons(["Down"])
    pos = mgba.get_coordinates()
    print(f"Pos after Down into (53, 16): {pos}")

if __name__ == "__main__":
    main()
