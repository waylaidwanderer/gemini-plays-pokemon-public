import mgba
import time

print("Opening START menu and POKéMON menu, then stopping so we can see it...")
mgba.press_buttons(["Start", "sleep 500", "Down", "sleep 200", "A", "sleep 800"])
