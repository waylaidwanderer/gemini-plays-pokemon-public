import mgba
import time

def press_and_screenshot(btn, label, delay=1.0):
    print(f"Pressing {btn} for {label}...")
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

print("--- VERIFYING TRUFFLE'S MOVESET ON TURN 41846 ---")

# 1. Open Start menu
press_and_screenshot("Start", "start_menu")

# 2. Force cursor to POKEDEX (top) by pressing UP 7 times
for i in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.2)
print("Cursor forced to top (POKEDEX)")

# 3. Press Down once to highlight POKEMON (POKEDEX -> POKEMON)
press_and_screenshot("Down", "pokedex_to_pokemon")

# 4. Press A to select POKEMON
press_and_screenshot("A", "pokemon_menu")

# 5. Press Down once to highlight TRUFFLE (second slot)
press_and_screenshot("Down", "highlight_truffle")

# 6. Press A to select TRUFFLE
press_and_screenshot("A", "truffle_submenu")

# 7. Press Down twice to highlight STATS (Option 3)
press_and_screenshot("Down", "stats_down_1")
press_and_screenshot("Down", "stats_down_2")

# 8. Press A to select STATS
press_and_screenshot("A", "stats_screen_1", delay=2.0)

# 9. Press A to go to page 2 of stats
press_and_screenshot("A", "stats_screen_2", delay=2.0)

# 10. Press B multiple times to exit to overworld
press_and_screenshot("B", "exit_1")
press_and_screenshot("B", "exit_2")
press_and_screenshot("B", "exit_3")
press_and_screenshot("B", "exit_4")

print("Moveset check complete!")
