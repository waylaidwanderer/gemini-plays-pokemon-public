import mgba
import time

def handle_potential_battle_or_dialog():
    # If in battle or dialog, mash B/A or try to run
    for _ in range(3):
        # In case a battle started, try running: Down, Right, A, then mash B
        mgba.press_buttons(["Down", "Right", "A", "sleep 100", "B", "sleep 100", "B", "sleep 100"])

def step_path(button_list):
    for btn in button_list:
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([btn, "sleep 50"])
        pos_after = mgba.get_coordinates()
        if pos_before == pos_after:
            # Didn't move - could be wall, ledge, bike turn, dialog, or battle
            handle_potential_battle_or_dialog()
            # Try pressing button again
            mgba.press_buttons([btn, "sleep 50"])

print("Helper script ready.")
