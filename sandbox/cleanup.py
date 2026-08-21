import os
import shutil

def cleanup_workspace():
    print("Starting workspace cleanup...")
    
    # 1. Delete specific files lacking .md extension or duplicates
    files_to_delete = [
        "notepads/Locations/FuchsiaGym",
        "notepads/Locations/SafariZone",
        "notepads/Scratchpad/SafariZone_Route",
        "notepads/Scratchpad/SafariZone_Route.md",
        "check_b1f_path.py",
        "compare_states.py",
        "inspect_walk.py",
        "solve_b1f_switch.py",
        "test_all_columns.py",
        "test_row11.py"
    ]
    
    for f in files_to_delete:
        p = os.path.join("notepads", f) if "/" in f and not f.startswith("notepads/") else f
        # Normalize path
        p = f if f.startswith("notepads/") else p
        if os.path.exists(p):
            try:
                if os.path.isdir(p):
                    shutil.rmtree(p)
                    print(f"Deleted directory: {p}")
                else:
                    os.remove(p)
                    print(f"Deleted file: {p}")
            except Exception as e:
                print(f"Error deleting {p}: {e}")
                
    # Also let's check for any other directories like Locations/SafariZone without .md
    dirs_to_delete = [
        "notepads/Locations/SafariZone",
        "Locations/SafariZone",
        "Locations/SafariZone_Area1_East_Boundaries",
        "Scratchpad/SafariZone_Route"
    ]
    for d in dirs_to_delete:
        if os.path.exists(d):
            try:
                if os.path.isdir(d):
                    shutil.rmtree(d)
                    print(f"Deleted directory: {d}")
                else:
                    os.remove(d)
                    print(f"Deleted file: {d}")
            except Exception as e:
                print(f"Error deleting {d}: {e}")

cleanup_workspace()
