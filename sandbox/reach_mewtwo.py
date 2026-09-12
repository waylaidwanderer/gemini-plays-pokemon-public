import mgba
import time

def handle_battle():
    # Attempt to flee: Down, Right, A, then mash B
    mgba.press_buttons(["Down", "Right", "A", "sleep 100", "B", "sleep 100", "B", "sleep 100", "B"])

def step_buttons(btn_list):
    for btn in btn_list:
        pos_before = mgba.get_coordinates()
        mgba.press_buttons([btn, "sleep 50"])
        pos_after = mgba.get_coordinates()
        if pos_before == pos_after:
            # Check if battle or obstruction
            handle_battle()
            mgba.press_buttons([btn, "sleep 50"])

print("Navigator loaded.")
