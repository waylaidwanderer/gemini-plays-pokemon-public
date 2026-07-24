import mgba
import time

def main():
    print("Starting systematic warp search in the middle section of Mt. Moon 1F...")
    # Bounded area: columns 10 to 21, rows 22 to 29
    # We are currently at (21, 22).
    # Let's perform a snake-like traversal of rows 22 to 29, columns 10 to 21.
    # Rows: 22, 23, 24, 25, 26, 27, 28, 29
    # For each row, we walk left/right across columns 10 to 21.
    # At each step, we check our coordinates. If we warp (or map changes), we print and stop!
    
    current_x = 21
    current_y = 22
    
    # Simple path plan:
    # Row 22: walk Left to 10 (11 steps Left)
    # Row 23: walk Right to 21
    # Row 24: walk Left to 10
    # Row 25: walk Right to 21
    # Row 26: walk Left to 10
    # Row 27: walk Right to 21
    # Row 28: walk Left to 10
    # Row 29: walk Right to 21
    
    path = []
    # Row 22 Left
    path.extend(["Left"] * 11)
    # Move to Row 23
    path.append("Down")
    path.extend(["Right"] * 11)
    # Move to Row 24
    path.append("Down")
    path.extend(["Left"] * 11)
    # Move to Row 25
    path.append("Down")
    path.extend(["Right"] * 11)
    # Move to Row 26
    path.append("Down")
    path.extend(["Left"] * 11)
    # Move to Row 27
    path.append("Down")
    path.extend(["Right"] * 11)
    # Move to Row 28
    path.append("Down")
    path.extend(["Left"] * 11)
    # Move to Row 29
    path.append("Down")
    path.extend(["Right"] * 11)

    print(f"Path has {len(path)} steps.")
    
    # We will execute steps one by one.
    # Since mgba.get_coordinates() might return {'x': 0, 'y': 0} in transitions or can be slow,
    # let's monitor if the map changes or if we end up at a known B1F landing.
    
    step_num = 0
    for move in path:
        # Press the button
        mgba.press_buttons([move, "sleep 250"])
        step_num += 1
        pos = mgba.get_coordinates()
        
        # Check if coordinates look like B1F. 
        # Platform 1 B1F is around row 14-27, columns 13-27.
        # But if we warp, the coordinates will change significantly, or we will be on B1F.
        # Let's print our progress
        print(f"Step {step_num}: {move} -> {pos}")
        
        # If coordinates are 0,0, mGBA might be transitioning. Sleep a bit and check again.
        if pos['x'] == 0 and pos['y'] == 0:
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            print(f"Re-check: {pos}")
            
        # If we are no longer in our starting bounding box (columns 10-21, rows 22-29),
        # we have either warped, hit a wild battle, or hit a wall.
        # Let's check if we warped to B1F:
        # In Mt. Moon, Map ID for B1F is different, but we can't get Map ID directly.
        # However, B1F coordinates for the landing is (13, 27) or (25, 15).
        # If we warp, pos might be (13, 27) or (25, 15), or we might hit a wild battle!
        # If we hit a wild battle, we can't easily move, and coordinates won't change.
        # If we hit a battle, let's stop the script so the main loop can handle it.
        # We can detect if a battle started by seeing if coordinates stop changing or we can't move.
        
if __name__ == "__main__":
    main()
