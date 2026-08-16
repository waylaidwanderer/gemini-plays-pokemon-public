import mgba
import time

def press_and_screenshot(btn, label, delay=1.0):
    print(f"Pressing {btn} for {label}...")
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

print("--- TEACHING CUT NOW (ROBUST) ---")

# 1. Open Start menu
press_and_screenshot("Start", "start_menu")

# 2. Force cursor to POKEDEX (top) by pressing UP 7 times
for i in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.2)
print("Cursor forced to top (POKEDEX)")

# 3. Press Down twice to highlight ITEM (POKEDEX -> POKEMON -> ITEM)
press_and_screenshot("Down", "pokedex_to_pokemon")
press_and_screenshot("Down", "pokemon_to_item")

# 4. Press A to select ITEM
press_and_screenshot("A", "item_menu_open")

# 5. Press Down once to highlight HM01 (second item)
press_and_screenshot("Down", "highlight_hm01")

# 6. Press A to open options, and A again to select USE
press_and_screenshot("A", "hm01_options")
press_and_screenshot("A", "party_select")

# 7. Press Down once to highlight TRUFFLE (second slot)
press_and_screenshot("Down", "highlight_truffle")

# 8. Press A to select TRUFFLE and teach CUT
press_and_screenshot("A", "teach_cut_dialog_1", delay=2.0)
press_and_screenshot("A", "teach_cut_dialog_2", delay=2.0)

# 9. Press B multiple times to exit to overworld
press_and_screenshot("B", "exit_1")
press_and_screenshot("B", "exit_2")
press_and_screenshot("B", "exit_3")
press_and_screenshot("B", "exit_4")

print("Done teaching CUT!")
