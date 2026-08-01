import mgba

def main():
    print("=== Testing Route to Underground Path (19, 17) ===")
    pos = mgba.get_coordinates()
    print(f"Start pos: {pos}")

    # Walk Left 27 steps from (46, 14)
    mgba.press_buttons(["Left"] * 27)
    pos = mgba.get_coordinates()
    print(f"Pos after walking Left: {pos}")

    # Try stepping Down continuously
    for i in range(5):
        mgba.press_buttons(["Down"])
        pos = mgba.get_coordinates()
        print(f"Pos after Down step {i+1}: {pos}")

if __name__ == "__main__":
    main()
