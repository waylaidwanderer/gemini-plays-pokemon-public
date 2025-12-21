# Goldenrod Radio Tower Takeover
## Strategy (HOW)
- Map 3_54 Switch Puzzle: Switches 1, 2, and 3 control shutters.
- Obtain Card Key from real Director in Warehouse.

# Global Knowledge
## Tile Mechanics
- WALL/SHUTTER: Impassable. Shutters (WALL) in Map 3_54 can be toggled to FLOOR via switches.

## Progress Tracking
- Badges: 7/16.
- PC: SHUCKIE (Lv15), ROCKY (Lv6), EGG (Lv5), XFDW (Lv16), FRITTATA (Lv5).
- Battle: Menu transitions need 1000ms delay. Move menu wraps and remembers position.

# Switch Room Puzzle (Map 3_54)
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Grunt Hint: "Change the order of switching. That'll change the ways the shutters open and close."

## Puzzle State Log
- Initial: Sw1 ?, Sw2 ON, Sw3 ON.
- Turn 9122: Sw3 toggled to OFF.
  - Observation: Opened shutters at (10, 6), (10, 7).
- Turn 9140: Sw2 toggled to OFF.
  - Observation: Closed shutters at (10, 6) and (6, 8). (10, 7) also appears CLOSED.
- Turn 9148: Sw1 toggled to OFF (Wait, history says it was turned ON then OFF?). 
- Current State (Turn 9151): Sw1 ON?, Sw2 OFF, Sw3 OFF.

## Observed Shutter Tiles
- (10, 6): Currently WALL (Closed).
- (10, 7): Currently WALL (Closed).
- (6, 8): Currently WALL (Closed).
- (12, 8): Currently WALL (Closed).
- (18, 8): Currently WALL (Closed).
- Note: Need to verify if these are dynamic shutters or static walls.