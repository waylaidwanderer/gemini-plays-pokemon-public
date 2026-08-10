import mgba
import time

print("Testing transition from Center to Area 1 (East)...")

# Current position: (15, 25)
# Walk UP 3 steps to (15, 22)
print("Walking UP to Row 22...")
for _ in range(3):
    mgba.press_buttons(["Up"])
    time.sleep(0.6)

# Walk RIGHT along Row 22 to transition (up to 16 steps)
print("Walking RIGHT along Row 22...")
for step in range(16):
    coords_before = mgba.get_coordinates()
    mgba.press_buttons(["Right"])
    time.sleep(0.6)
    coords_after = mgba.get_coordinates()
    print(f"Step {step+1}: {coords_before} -> {coords_after}")
    
    # If x decreased significantly or changed to 0/1, it means we transitioned!
    if coords_after['x'] < coords_before['x'] and coords_after['x'] <= 1:
        print("TRANSITIONED TO AREA 1 (EAST)!")
        break

final_coords = mgba.get_coordinates()
print(f"Final coordinates: {final_coords}")
