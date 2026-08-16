import mgba
import time

def press_and_screenshot(btn, label, delay=1.0):
    print(f"Pressing {btn} for {label}...")
    mgba.press_buttons([btn])
    time.sleep(delay)
    path = mgba.take_screenshot()
    print(f"Screenshot [{label}]: {path}")

print("--- CHECKING OUR BADGES ---")
# Open Start menu
press_and_screenshot("Start", "start_menu")

# Press UP 7 times to force cursor to the top (POKEDEX)
for i in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.2)
print("Cursor forced to top (POKEDEX)")

# Press Down 3 times to highlight ACE (our trainer card)
# POKEDEX -> POKEMON -> ITEM -> ACE
press_and_screenshot("Down", "pokedex_to_pokemon")
press_and_screenshot("Down", "pokemon_to_item")
press_and_screenshot("Down", "item_to_ace")

# Press A to select ACE
press_and_screenshot("A", "trainer_card", delay=2.0)

# Press B multiple times to exit
press_and_screenshot("B", "exit_1")
press_and_screenshot("B", "exit_2")
print("Done checking badges!")
