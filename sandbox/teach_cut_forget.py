import mgba
import time

def press_and_screenshot(btn, label, delay=1.0):
    print(f"Pressing {btn} for {label}...")
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

print("--- TEACHING CUT AND FORGETTING POISONPOWDER ---")

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
press_and_screenshot("A", "dialog_wants_to_learn", delay=2.0)

# 9. Press A to clear "TRUFFLE wants to learn CUT!"
press_and_screenshot("A", "dialog_already_knows_4", delay=2.0)

# 10. Press A to clear "But, TRUFFLE already knows 4 moves!" and prompt Yes/No
press_and_screenshot("A", "prompt_forget_yes_no", delay=2.0)

# 11. Press A to select YES (which is the default highlighted option)
press_and_screenshot("A", "move_list_forget", delay=2.0)

# 12. Press Down once to highlight POISONPOWDER (second move)
press_and_screenshot("Down", "highlight_poisonpowder")

# 13. Press A to select POISONPOWDER to forget
press_and_screenshot("A", "dialog_poof_1", delay=2.0)

# 14. Press A to clear "1, 2 and... Poof!"
press_and_screenshot("A", "dialog_forgot_move", delay=2.0)

# 15. Press A to clear "TRUFFLE forgot POISONPOWDER!"
press_and_screenshot("A", "dialog_learned_cut", delay=2.0)

# 16. Press A to clear "And... TRUFFLE learned CUT!"
press_and_screenshot("A", "finished_learning", delay=2.0)

# 17. Press B multiple times to exit to overworld
for i in range(5):
    press_and_screenshot("B", f"exit_{i+1}", delay=0.5)

print("Done!")
