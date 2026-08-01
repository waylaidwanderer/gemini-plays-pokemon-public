import mgba

def main():
    print("=== Probing Column 27/28 Building Boundary ===")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")

    # Walk Left from (53, 15) to (28, 15)
    mgba.press_buttons(["Left"] * 25)
    pos = mgba.get_coordinates()
    print(f"At Col 28 Row 15: {pos}")

    # Probe Left at Row 15
    mgba.press_buttons(["Left"])
    pos = mgba.get_coordinates()
    print(f"Probe Left on Row 15: {pos}")

    # Step Up to Row 14
    mgba.press_buttons(["Up"])
    pos = mgba.get_coordinates()
    print(f"At Row 14: {pos}")

    # Probe Left at Row 14
    mgba.press_buttons(["Left"])
    pos = mgba.get_coordinates()
    print(f"Probe Left on Row 14: {pos}")

    # Try probing Up/Down along Col 28 to find any door or pass
    mgba.press_buttons(["Down"])
    pos = mgba.get_coordinates()
    print(f"Row 15 again: {pos}")

if __name__ == "__main__":
    main()
