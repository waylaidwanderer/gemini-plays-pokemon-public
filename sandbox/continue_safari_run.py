import complete_safari_run
import bridge
import time

def run_remaining():
    print("=== STARTING REMAINING SAFARI RUN FROM AREA 1 (EAST) (0, 23) ===")
    
    print("=== PHASE 2: Area 1 (East) to Area 2 (North) ===")
    if not complete_safari_run.run_path(complete_safari_run.path_area1, check_warp=True):
        return False

    print("=== PHASE 3: Area 2 (North) to Area 3 (West) ===")
    if not complete_safari_run.run_path(complete_safari_run.path_area2, check_warp=True):
        return False

    print("=== PHASE 4: Area 3 (West) Ascent and Descent ===")
    if not complete_safari_run.run_path(complete_safari_run.path_area3_ascent, check_warp=False):
        return False

    print("=== PHASE 5: Walk to Gold Teeth Warp ===")
    if not complete_safari_run.run_path(complete_safari_run.path_to_teeth, check_warp=True):
        return False

    print("=== PHASE 5b: Picking up Gold Teeth inside Center ===")
    if not complete_safari_run.run_path(complete_safari_run.path_center_teeth, check_warp=False):
        return False

    # Stand below Gold Teeth and interact
    pos = complete_safari_run.get_pos()
    print(f"Standing below Gold Teeth at {pos}. Interacting...")
    complete_safari_run.walk_step("Up") # Bumps into item, facing us UP
    time.sleep(0.5)
    bridge.press_buttons(["A", "sleep 1000", "A", "sleep 1000", "B", "sleep 500"])
    print("Gold Teeth picked up!")

    print("=== PHASE 5c: Walking back to warp to Area 3 (West) ===")
    if not complete_safari_run.run_path(complete_safari_run.path_back_to_warp, check_warp=True):
        return False

    print("=== PHASE 6: Walking to Secret House ===")
    if not complete_safari_run.run_path(complete_safari_run.path_to_house, check_warp=True):
        return False

    print("Arrived inside Secret House! Coordinates:", complete_safari_run.get_pos())
    return True

if __name__ == "__main__":
    run_remaining()
