import mgba
import time

def press_and_screenshot(btn, label, delay=1.0):
    print(f"Pressing {btn} for {label}...")
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

print("--- CHECKING TRUFFLE'S MOVES ---")
# Currently at (26, 14) facing UP.
press_and_screenshot("Start", "start_menu")
press_and_screenshot("Down", "highlight_pokemon")
press_and_screenshot("A", "pokemon_menu")
press_and_screenshot("Down", "highlight_truffle")
press_and_screenshot("A", "truffle_submenu")

# Press Down twice to highlight STATS (Option 3)
press_and_screenshot("Down", "stats_down_1")
press_and_screenshot("Down", "stats_down_2")
press_and_screenshot("A", "stats_screen_1", delay=2.0)

# Press A or B to go to page 2 of stats (moveset page)
press_and_screenshot("A", "stats_screen_2", delay=2.0)

# Press B to exit back to overworld
press_and_screenshot("B", "exit_1")
press_and_screenshot("B", "exit_2")
press_and_screenshot("B", "exit_3")
press_and_screenshot("B", "exit_4")

print("Done!")
