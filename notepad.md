# Tile Mechanics
- **WALL:** Impassable.
- **FLOOR:** Walkable.
- **WARP_CARPET_DOWN:** Exits map (requires entering from North?).
- **LADDER:** Changes floor.

# Objectives & Progress
- **Primary:** Rescue the Director (held in Underground Warehouse).
- **Current Task:** Access the Southeast Underground section to find Switch 2 & 3.
- **Key Item:** BASEMENT KEY (Obtained).

# Dept Store Basement Puzzle (Solved)
- **Solution:** Stand at (4, 7) to "watch" the Black Belt (ID 6). This opens the North Gate at (10, 8).
- **Outcome:** Accessed the area behind the gate. Found a Blue Barrier at Row 4 blocking the path to the item and ladder at (17, 2).
- **Deduction:** The ladder at (17, 2) is likely an entrance from the Warehouse, not an exit. Need to access Warehouse from Underground.

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
- **Observation:** Avoiding line of sight (Col 8) kept North Gate CLOSED.
- **Refined Hypothesis:** The gates might default to CLOSED. Walking on Column 9 (Main Path) triggers the "Open South / Close North" state.
- **The "Watcher" Clue:** Black Belt (ID 6) at (4, 8) says he stops working if watched. If he controls the gates (or the North gate), "stopping work" might OPEN it.
- **Plan:**
    1. Reset Room (Elevator 1F -> B1F) to ensure clean state.
    2. Navigate to (4, 7) to stand directly in front of ID 6 (assuming he faces UP).
    3. Check if North Gate (10, 8) opens.
    4. If not, try standing at (5, 8) (Side view) again and checking the gate.
- **Stealth Route:** From Elevator (10, 4) -> (9, 4) -> (8, 4) -> (8, 8). This avoids Column 9 entirely (Row 5+), preventing the alarm trigger.
- **Observation:** Black Belt (ID 6) rotates. Was facing UP, now facing LEFT.
- **Hypothesis Adjustment:** He might need to "see" me when he rotates to face me. Standing at (4, 7) puts me in his UP line of sight.
- **Current Action:** Verifying solidity of Blue Barrier at Row 4 (Cols 15-17).
- **Hypothesis:** One of these tiles might be a door or false wall.
- **Next:** If wall is solid, explore the South part of the East Room (Rows 6-18) for switches or items.
- **Observation:** North Gate (10, 8) is OPEN. South Gate (10, 12) is CLOSED.
- **Goal:** Reach Ladder at (17, 2).
- **Conclusion:** The Blue Barrier at Row 4 is solid and blocks access to the North.
- **Deduction:** The Ladder at (17, 2) is an *entrance* from the Warehouse (accessed via Underground Switch 1 area), not an exit from here.
- **Next Step:** Return to Underground. Find the path to the Warehouse and the Director.
- **Hypothesis:** The "Locked Door" in the Underground (which I have the key for) leads to the area containing the Director and the other side of this ladder.