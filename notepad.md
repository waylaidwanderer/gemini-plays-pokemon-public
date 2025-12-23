# Tile Mechanics
- **WALL:** Impassable.
- **FLOOR:** Walkable.
- **WARP_CARPET_DOWN:** Exits map (requires entering from North?).
- **LADDER:** Changes floor.

# Objectives & Progress
- **Primary:** Rescue the Director (held in Underground Warehouse).
- **Current Task:** Access the Southeast Underground section to find Switch 2 & 3.
- **Key Item:** BASEMENT KEY (Obtained).

# Puzzle Strategy
- **Goal:** Reach the Northeast section via the North Gate (Row 8).
- **Current State:** North Gate (10, 8) is CLOSED. South Gate (10, 12) is OPEN.
- **Hypothesis:** The gates toggle based on where the Black Belt sees the player.
    - Being seen at North (Row 8/9) -> Closes North, Opens South.
    - Being seen at South (Row 11/12) -> Closes South, Opens North.
- **Result:** Failed. Standing at (9, 11) also did not close the South Gate. The gates do not seem to toggle based on simple proximity or line of sight in this way.
- **New Plan:**
    1. Talk to the moving Black Belt (ID 5) at (9, 10). Maybe interaction triggers the switch or gives a clue.
    2. If that fails, try approaching the Black Belt from the side (Col 8 -> Row 10) or from the North (reset room first).
    3. Alternative: Check if there's a switch on the wall or elsewhere.

# Completed Notes (Archive)
- **Rival Battle:** Defeated Silver (Golbat, Haunter, Feraligatr, Sneasel, Magnemite). Muscle (Machoke) swept.
- **Switch 1:** Found at (16, 1) via Ladder at (22, 27). Turned ON. Did not open the main shutter.
- **Exploration:** Checked Warehouse Room (Map 3_53). North wall shutters are closed. West/Southwest ladders explore.

# Important Locations
- **Switch 1:** Map 3_54 (via 3_53 ladder). ON.
- **Director:** Warehouse (locked behind shutters).
- **Dept Store Basement:** Likely route to switches.
- **Problem:** Rocket Grunt at (16, 23) blocks the path to the East side (Dept Store). He does not battle.
- **Solution:** Use the Underground to bypass the blockade.
- **Plan:**
    1. Re-enter Underground via South Entrance (11, 29).
    2. Traverse Main Tunnel to the **Northwest Ladder** (3, 2).
    3. Enter North Entry Room (3_54).
    4. Force the **North Exit Warp** (21, 29) to trigger (it must work).
    5. This will emerge at Goldenrod City (9, 5) (North side).
    6. Cross East along Row 8 to reach the Dept Store.

# Puzzle Mechanics
- **Shifting Walls:** The boxes in the center room (Cols 10-11, Rows 8-12) toggle between WALL and FLOOR. Likely linked to NPC movement or position. Currently, the South path (Rows 10-12) is OPEN, and the North path (Rows 8-9) is CLOSED.
- **Correction:** Previous test failed because auto-pathing routed through (9, 8), triggering the trap.
- **Retest:** Manual pathing: Elevator (Reset) -> (8, 4) -> (8, 8). Avoid (9, 8) entirely.
- **Clue:** Black Belt says "Our policy is to work behind the scenes where no one can see us!"
- **Interpretation:** Being "seen" (Line of Sight) triggers the gates to close.
- **Refined Plan:** Reset the room via Elevator. Then, strictly adhere to Column 8 (Left Wall) to approach the North Gate. Do NOT step on Column 9.
- **Hypothesis:** Staying out of the Black Belt's line of sight (Col 9) will keep the North Gate open.