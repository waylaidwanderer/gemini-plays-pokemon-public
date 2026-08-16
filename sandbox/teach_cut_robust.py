import mgba
import time

def press_and_screenshot(btn, label, delay=1.0):
    print(f"Pressing {btn} for {label}...")
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

print("--- TEACHING CUT STEP-BY-STEP ---")

# 1. Open Start menu
press_and_screenshot("Start", "start_menu")

# 2. Press Down twice to highlight ITEM
press_and_screenshot("Down", "start_down_1")
press_and_screenshot("Down", "start_down_2")

# 3. Press A to select ITEM
press_and_screenshot("A", "item_menu_open")

# 4. Press Down once to highlight HM01 (which is the second item)
press_and_screenshot("Down", "highlight_hm01")

# 5. Press A to open HM01 options
press_and_screenshot("A", "hm01_options")

# 6. Press A to select USE (first option)
press_and_screenshot("A", "party_select_screen")

# 7. Press Down once to highlight TRUFFLE (second slot)
press_and_screenshot("Down", "highlight_truffle")

# 8. Press A to select TRUFFLE
press_and_screenshot("A", "teach_cut_dialog_1", delay=2.0)

# 9. Press A to clear the "TRUFFLE learned CUT!" dialog
press_and_screenshot("A", "teach_cut_dialog_2", delay=2.0)

# 10. Press B multiple times to exit to overworld
press_and_screenshot("B", "exit_1")
press_and_screenshot("B", "exit_2")
press_and_screenshot("B", "exit_3")
press_and_screenshot("B", "exit_4")

print("Done teaching CUT!")
