import mgba

def main():
    print("=== Route 8 Basin Probing Part 2 ===")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")

    # Walk Left from (38, 15) as far as possible
    path_left_20 = ["Left"] * 20
    mgba.press_buttons(path_left_20)
    pos = mgba.get_coordinates()
    print(f"Pos after walking 20 Left on Row 15: {pos}")

    # Try stepping Up
    mgba.press_buttons(["Up"])
    pos = mgba.get_coordinates()
    print(f"Pos after Up: {pos}")

if __name__ == "__main__":
    main()
