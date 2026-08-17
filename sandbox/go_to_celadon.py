import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def navigate_to_celadon():
    print("Navigating to Celadon City...")
    
    # 1. Walk right to Column 8
    # Currently at (2, 14). Let's walk right 6 steps to reach Column 8 at (8, 14)
    for i in range(6):
        press_and_wait("Right")
        pos = mgba.get_coordinates()
        print(f"Step {i+1} Right: at ({pos['x']}, {pos['y']})")
        
    # 2. Walk up to Row 10
    # From (8, 14), we want to walk up to Row 10. Let's do it step by step.
    for i in range(4):
        press_and_wait("Up")
        pos = mgba.get_coordinates()
        print(f"Step {i+1} Up: at ({pos['x']}, {pos['y']})")
        
    # 3. From (8, 10), let's walk left to Celadon City
    # Saffron West Gatehouse is to the right at (12, 10). Celadon is to the left (west).
    # Let's walk left continuously until we transition maps!
    # Celadon is west of Route 7, so walking left from x=8 should transition us.
    print("Walking left to Celadon...")
    for i in range(12):
        press_and_wait("Left")
        pos = mgba.get_coordinates()
        print(f"Step {i+1} Left: at ({pos['x']}, {pos['y']})")
        # Check if coordinates indicate we transitioned maps (e.g. x > 15 or map name change)
        # In Celadon City, our coordinates would warp. Let's take a screenshot and check coordinates.
        if pos['x'] > 15 or pos['x'] < 0:
            print("Map transition detected!")
            break

    mgba.take_screenshot()

navigate_to_celadon()
