import mgba

def main():
    print("=== Testing Column 29 Gap (29, 13) ===")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")

    # Walk Left 24 steps from (53, 14) to (29, 14)
    path_to_29_14 = ["Left"] * 24
    mgba.press_buttons(path_to_29_14)
    pos = mgba.get_coordinates()
    print(f"Pos at Col 29 Row 14: {pos}")

    # Try stepping Up through (29, 13)
    mgba.press_buttons(["Up"])
    pos = mgba.get_coordinates()
    print(f"Pos after Up into (29, 13): {pos}")

    # Try stepping Up again
    mgba.press_buttons(["Up"])
    pos = mgba.get_coordinates()
    print(f"Pos after second Up: {pos}")

if __name__ == "__main__":
    main()
