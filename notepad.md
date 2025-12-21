# Goldenrod Radio Tower Takeover
## Strategy (HOW)
- Map 3_54 Switch Puzzle: Switches 1, 2, and 3 control shutters.
- Solution Goal: Reach the warehouse entrance (likely far south/west).
- Method: Systematically toggle switches and record the *sequence* to identify the order-dependent behavior.

# Global Knowledge
## Tile Mechanics
- WALL/SHUTTER: Impassable. Shutters in Map 3_54 can be toggled to FLOOR via switches.

## Progress Tracking
- Badges: 7/16.
- PC: SHUCKIE (Lv15), ROCKY (Lv6), EGG (Lv5), XFDW (Lv16), FRITTATA (Lv5).

# Switch Room Puzzle (Map 3_54)
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Grunt Hint: "Change the order of switching. That'll change the ways the shutters open and close."

## Sequence Log & Observations
- State A (Initial): Sw1 ?, Sw2 ON, Sw3 ON.
- Action: Sw3 -> OFF (Turn 9122).
  - Result: Opened (10, 6), (10, 7).
- Action: Sw2 -> OFF (Turn 9140).
  - Result: Closed (10, 6), (10, 7). Opened (6, 8)?
- Action: Sw1 -> ON (Turn 9152).
  - Result: Opened (16, 6), (17, 6).
- Action: Sw1 -> OFF (Turn 9155).
  - Result: Closed (16, 6), (17, 6).

## Current State (Turn 9174)
- Switch States: Sw1 OFF, Sw2 OFF, Sw3 ON.
- Shutter Status: Need to observe Row 6/7/8.
- Note: Toggling Sw3 to ON from the all-OFF state.

## Hypothesized Shutter Tiles
- Sw1: (16, 6), (17, 6)
- Sw2: (10, 6), (10, 7)? (12, 6), (13, 6)?
- Sw3: (10, 6), (10, 7)?
- Note: Order matters. If Sw3 is OFF, Sw2 might behave differently.