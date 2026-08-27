import mgba
import time

# We are in the moves menu.
# Button list with proper in-emulator sleeps:
# 1. B (to return to main battle menu)
# 2. sleep 500
# 3. Down (move to ITEM)
# 4. sleep 150
# 5. Right (move to RUN)
# 6. sleep 150
# 7. A (select RUN)
# 8. sleep 2500 (wait for escape animation and text)
# 9. A (dismiss escape text)
# 10. sleep 1000 (let overworld load)

buttons = [
    "B", "sleep 500",
    "Down", "sleep 150",
    "Right", "sleep 150",
    "A", "sleep 2500",
    "A", "sleep 1000"
]

print("Executing escape sequence in emulator...")
mgba.press_buttons(buttons)
time.sleep(0.5)

pos = mgba.get_coordinates()
print("Position after escape:", pos)
