import mgba
import time

def press_and_screenshot(btn, label, delay=1.0):
    print(f"Pressing {btn} for {label}...")
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

# Currently at (26, 14) facing UP.
print("--- STEP-BY-STEP MENU NAVIGATION TEST FOR CUT ---")

# 1. Open Start menu
press_and_screenshot("Start", "start_menu")

# 2. Press Down to highlight POKEMON
press_and_screenshot("Down", "highlight_pokemon")

# 3. Press A to select POKEMON
press_and_screenshot("A", "pokemon_menu")

# 4. Press Down to highlight TRUFFLE (Slot 2)
press_and_screenshot("Down", "highlight_truffle")

# 5. Press A to select TRUFFLE
press_and_screenshot("A", "truffle_submenu")

# 6. Press Down to highlight CUT
press_and_screenshot("Down", "highlight_cut")

# 7. Press A to execute CUT
press_and_screenshot("A", "cut_execution", delay=3.0)

# 8. Press B to clear text
press_and_screenshot("B", "clear_text_1")
press_and_screenshot("B", "clear_text_2")

print("Test complete!")
