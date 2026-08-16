import mgba
import time

print("--- AUTOMATING TEACHING SURF (HM03) TO SHELLBY ---")

# 1. Open the Start menu
mgba.press_buttons(["Start", "sleep 500"])

# 2. Go to ITEM
# Press Up several times to force cursor to POKEDEX (top)
for _ in range(7):
    mgba.press_buttons(["Up"])
    time.sleep(0.1)
time.sleep(0.3)

# Press Down 2 times to go to ITEM, and press A
mgba.press_buttons(["Down", "Down", "sleep 100", "A", "sleep 500"])

# 3. Find HM03 in the bag list (Down 9 times from the top)
print("Scrolling to HM03...")
for _ in range(9):
    mgba.press_buttons(["Down"])
    time.sleep(0.2)
time.sleep(0.4)

# Press A to select HM03
mgba.press_buttons(["A", "sleep 500"])

# Select USE (Option 1)
mgba.press_buttons(["A", "sleep 1000"])

# 4. We are in the party screen.
# Slot 1: TRUFFLE
# Slot 2: SHELLBY
# Press Down to highlight SHELLBY, and press A
print("Selecting SHELLBY...")
mgba.press_buttons(["Down", "sleep 100", "A", "sleep 1000"])

# 5. Confirm "Teach?" by pressing A
mgba.press_buttons(["A", "sleep 1000"])

# 6. We are in the move list.
# 1. Hydro Pump
# 2. Ice Beam
# 3. Bite
# 4. Water Gun
# Press Down 3 times to highlight Water Gun, and press A
print("Selecting Water Gun to forget...")
for _ in range(3):
    mgba.press_buttons(["Down"])
    time.sleep(0.2)
time.sleep(0.4)

mgba.press_buttons(["A", "sleep 1000"])

# 7. Confirm "Forget Water Gun?" by pressing A
print("Confirming forget...")
mgba.press_buttons(["A", "sleep 1500"])

# 8. Clear "SHELLBY learned SURF!" by pressing A
print("Clearing learned message...")
mgba.press_buttons(["A", "sleep 1000"])

# 9. Press B multiple times to close all menus and return to overworld
print("Exiting to overworld...")
for _ in range(4):
    mgba.press_buttons(["B"])
    time.sleep(0.5)

print("Teach Surf complete!")
mgba.take_screenshot()
