import mgba
import time
from PIL import Image

def press_and_wait(button, delay=0.2):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def is_textbox_open():
    screenshot_path = mgba.take_screenshot()
    img = Image.open(screenshot_path)
    w, h = img.size
    scale_x = w / 160.0
    scale_y = h / 144.0
    
    # Check sample pixels in the bottom textbox region
    test_coords = [
        (int(x * scale_x), int(y * scale_y))
        for x in [20, 40, 60, 80, 100, 120, 140]
        for y in [120, 130]
    ]
    
    white_count = 0
    for px, py in test_coords:
        p = img.getpixel((px, py))
        if isinstance(p, tuple):
            if p[0] > 240 and p[1] > 240 and p[2] > 240:
                white_count += 1
        else:
            if p > 240:
                white_count += 1
                
    return white_count >= len(test_coords) - 1

def sweep_roof_for_vending():
    print("Starting comprehensive sweep of the Roof from:", get_pos())
    
    # BFS to discover all reachable tiles on the Roof
    start = get_pos()
    queue = [start]
    visited = {start}
    parent = {start: None}
    
    # Simple queue-based traversal
    while queue:
        curr = queue.pop(0)
        cx, cy = curr
        
        # Navigate to the target tile 'curr'
        # To do this safely, we can backtrack to start and replay the path,
        # or just find a path from our current position.
        # Replaying path from start is extremely reliable!
        path = []
        node = curr
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
        
        # Move to start (if we are not there)
        # We can just reset to start by walking. Or since we are doing BFS,
        # we can just walk from our actual current position to 'curr' step-by-step.
        # Let's write a simple step-by-step path follower from actual current position.
        actual_x, actual_y = get_pos()
        print(f"Navigating from actual ({actual_x}, {actual_y}) to BFS target ({cx}, {cy})...")
        
        # Simple step-by-step movement along the path
        for target_node in path:
            tx, ty = target_node
            ax, ay = get_pos()
            if ax != tx or ay != ty:
                # Walk 1 step to target_node
                dx = tx - ax
                dy = ty - ay
                if dx > 0: press_and_wait("Right")
                elif dx < 0: press_and_wait("Left")
                elif dy > 0: press_and_wait("Down")
                elif dy < 0: press_and_wait("Up")
                
                # Check if we successfully reached the tile
                nx, ny = get_pos()
                if nx != tx or ny != ty:
                    print(f"Failed to step onto ({tx}, {ty}) from ({ax}, {ay}). Aborting this branch.")
                    break
        
        # Verify we arrived at 'curr'
        ax, ay = get_pos()
        if ax != cx or ay != cy:
            continue
            
        # We are at 'curr'! Test all 4 directions for vending machine
        print(f"Testing tile ({cx}, {cy}) for vending machine...")
        for direction in ["Up", "Right", "Down", "Left"]:
            # Turn to face direction by pressing it (might take a step, but we check and backtrack)
            press_and_wait(direction)
            time.sleep(0.1)
            
            # If we stepped, we are at a new tile. Let's step back or handle it.
            nx, ny = get_pos()
            if nx != cx or ny != cy:
                # We stepped! So the path in that direction is open.
                # Since it's open, there is NO wall/machine there.
                # Let's add it to the BFS queue if we haven't visited it yet!
                neighbor = (nx, ny)
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = curr
                    queue.append(neighbor)
                
                # Step back to 'curr'
                back_dir = "Down" if direction == "Up" else "Up" if direction == "Down" else "Left" if direction == "Right" else "Right"
                press_and_wait(back_dir)
            else:
                # We didn't step! There is a solid obstacle or wall in this direction.
                # Let's test if it's a vending machine by pressing A!
                print(f"  Solid obstacle in direction {direction}. Pressing A to test...")
                press_and_wait("A", 0.5)
                
                if is_textbox_open():
                    print(f"SUCCESS! Found interactive object at ({cx}, {cy}) facing {direction}!")
                    # Keep the menu open and exit!
                    return True
                else:
                    # Press B to make sure no dialog got opened (e.g. standard signpost)
                    press_and_wait("B", 0.2)
                    
    print("Sweep completed. No interactive vending machine found.")
    return False

sweep_roof_for_vending()
