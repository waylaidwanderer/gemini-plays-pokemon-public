import mgba
import time

def leave_viridian_final():
    print("Walking south to Route 1 from (32, 10)...")
    
    # 1. Walk Left to Column 20
    # We are at (32, 10)
    for _ in range(12):
        mgba.press_buttons(["Left"])
        time.sleep(0.12)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # 2. Walk Down to Row 35
    for _ in range(25):
        mgba.press_buttons(["Down"])
        time.sleep(0.12)
        
    print(f"At southern road: {mgba.get_coordinates()}")
    
    # 3. Walk Down into Route 1
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    print(f"Transitioned to Route 1! Current position: {mgba.get_coordinates()}")

leave_viridian_final()
