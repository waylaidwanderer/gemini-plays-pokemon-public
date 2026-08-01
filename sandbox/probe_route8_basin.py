import mgba

def main():
    print("=== Route 8 Basin Probing Script ===")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")

    # Walk Left from (53, 14) to (28, 14)
    path_left = ["Left"] * 25
    mgba.press_buttons(path_left)
    pos = mgba.get_coordinates()
    print(f"Pos after walking 25 Left: {pos}")

    # Try stepping Down to (28, 15)
    mgba.press_buttons(["Down"])
    pos = mgba.get_coordinates()
    print(f"Pos after Down: {pos}")

    # Try stepping Left from Row 15
    mgba.press_buttons(["Left"])
    pos = mgba.get_coordinates()
    print(f"Pos after Left on Row 15: {pos}")

if __name__ == "__main__":
    main()
