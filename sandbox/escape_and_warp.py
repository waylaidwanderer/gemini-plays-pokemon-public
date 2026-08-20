import mgba
import time
import os
import shutil

def cleanup_workspace():
    print("Cleaning up obsolete workspace files...")
    files_to_delete = [
        "go_to_2f.py",
        "test_stairs_up.py",
        "test_walls.py",
        "run_from_battle.py",
        "walk_step_by_step.py",
        "solve_mansion_final_victory.py"
    ]
    for f in files_to_delete:
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f"Deleted {f}")
            except Exception as e:
                print(f"Error deleting {f}: {e}")
                
    # Clean pycache
    pycache_dir = "__pycache__"
    if os.path.exists(pycache_dir):
        try:
            shutil.rmtree(pycache_dir)
            print("Cleaned __pycache__")
        except Exception as e:
            print(f"Error cleaning pycache: {e}")

def run_from_battle_and_warp():
    print("Starting escape and warp sequence...")
    
    # 1. We are in battle, cursor on FIGHT. Move Down, Right, and press A to escape
    print("Fleeing battle...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    
    # Press B to make sure text is dismissed after running
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Post-battle position:", pos)
    
    # Verify we are on the map
    if pos['x'] == 7 and pos['y'] == 11:
        print("Successfully back on 3F at (7, 11). Walking UP onto stairs at (7, 10)...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0) # wait for warp
        
        new_pos = mgba.get_coordinates()
        print("Position after warp attempt:", new_pos)
        mgba.take_screenshot()
    else:
        print("Unexpected position. Capturing screenshot.")
        mgba.take_screenshot()

if __name__ == "__main__":
    cleanup_workspace()
    run_from_battle_and_warp()
