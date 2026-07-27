import mgba

print("Starting navigation from (20, 10) to (41, 9)...")

# Walk Right 9 times to (29, 10)
mgba.press_buttons(["Right"] * 9)

# Walk Up 1 time to (29, 9)
mgba.press_buttons(["Up"])

# Walk Right 12 times to (41, 9)
mgba.press_buttons(["Right"] * 12)

pos = mgba.get_coordinates()
print(f"Navigation complete. Final coordinates: {pos}")
