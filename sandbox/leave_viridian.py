import mgba
import time
import os

def leave_viridian_correct():
    print("Cleaning up old files...")
    for f in ["check_trainer_card.py", "leave_pallet.py", "check_trainer_card.pyc", "leave_pallet.pyc"]:
        p = os.path.join("sandbox", f)
        if os.path.exists(p):
            try:
                os.remove(p)
                print(f"Deleted {f}")
            except Exception as e:
                print(f"Error deleting {f}: {e}")
        # also check root sandboxed directory
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f"Deleted {f}")
            except Exception as e:
                print(f"Error deleting {f}: {e}")

    print("Leaving Viridian City...")
    
    # 1. Left 2 times to (18, 12)
    for _ in range(2):
        mgba.press_buttons(["Left"])
        time.sleep(0.15)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # 2. Down 18 times to (18, 30)
    for _ in range(18):
        mgba.press_buttons(["Down"])
        time.sleep(0.15)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # 3. Right 2 times to (20, 30)
    for _ in range(2):
        mgba.press_buttons(["Right"])
        time.sleep(0.15)
        
    print(f"At: {mgba.get_coordinates()}")
    
    # 4. Down 6 times to transition to Route 1 (y=35, then y=36)
    for _ in range(6):
        mgba.press_buttons(["Down"])
        time.sleep(0.15)
        
    print(f"Final Position: {mgba.get_coordinates()}")

leave_viridian_correct()
