# Goldenrod Radio Tower Takeover
## Strategy (HOW)
- Map 3_54 Switch Puzzle: Switches 1, 2, and 3 control shutters.
- Solution Goal: Reach the warehouse entrance (likely far south/west).
- Resource Management: Visit Goldenrod Dept. Store to buy Hyper Potions and Revives using ¥88139.

# Global Knowledge
## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable. In Map 3_54, certain WALL tiles are dynamic shutters controlled by switches.
- COUNTER: Interact from the front.
- LADDER/STAIRS: Warps.

## Progress Tracking
- Badges: 7/16.
- PC: SHUCKIE (Lv15), ROCKY (Lv6), EGG (Lv5), XFDW (Lv16), FRITTATA (Lv5).

# Switch Room Puzzle (Map 3_54)
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Grunt Hint: "Change the order of switching. That'll change the ways the shutters open and close."

## Shutter Logic (Verified)
- Switch 1: Toggles (16, 6) and (17, 6).
- Switch 3 (ON -> OFF): Opens (10, 6) and (10, 7).
- Switch 3 (OFF -> ON): Opens (12, 8) and (12, 9).
- Switch 2 (ON -> OFF): Closes (10, 6) and (10, 7).

## Current State (Turn 9181)
- Switch States: Sw1 OFF, Sw2 OFF, Sw3 ON.
- Shutter Status:
  - (10, 6), (10, 7): WALL (Closed)
  - (16, 6), (17, 6): WALL (Closed)
  - (12, 8), (12, 9): FLOOR (Open)