# Goldenrod Underground

## Current Status
- **Location:** Goldenrod Underground Warehouse (3_56).
- **Objective:** Rescue the Director (Likely at 12, 8).
- **Current Task:** Looting item at (18, 15), then circling North to (13, 9) and the Director.

## Warehouse Discoveries
- **Layout:** Western corridor leads to a southern corridor. Central area is walled off. Access to center/north is via a gap at (16, 11).
- **NPCs:**
  - Rocket Grunt (Defeated) at (8, 13).
  - Director (Target) at (12, 8).
  - Rocket Grunt (Target) at (9, 8).
- **Items:**
  - Ultra Ball (Picked up at 2, 1).
  - Item Ball at (13, 9) (Unclaimed).
  - Item Ball at (18, 15) (Unclaimed).

## Switch Room (3_54) Configuration
- **S1 (16, 1):** ON (East Closed / West Open).
- **S2 (10, 1):** ON (Main Power).
- **S3 (2, 1):** ON (Emergency Mode).
- **Emergency Switch (20, 11):** ON.
- **Action (Turn 15069):** Picked up Max Ether at `(18, 15)`.
- **Plan:** Navigate North through the gap at Column 16-18 to reach the Item Ball at `(13, 9)` and the Director at `(12, 8)`.
- **Action (Turn 15079):** Battling Rocket Grunt (Weezing). Keeping Muscle in to use Dig (Super Effective).
- **Plan:** Finish the battle, then proceed West past the Grunt into the central area.
- **Observation (Turn 15092):** Defeated Grunt at `(9, 6)`. He is currently blocking the only known path South to the Director.
- **Hypothesis:** Post-battle script should move him or he should disappear.
- **Action:** Clearing text to trigger any scripts.
- **Correction (Turn 15093):** Grunt at `(9, 6)` did not move. However, Row 5 is open to the East.
- **New Plan:** Bypass the Grunt by taking the route: `(9, 5)` -> East to `(14, 5)` -> South to `(14, 8)` -> West to Director.
- **Success (Turn 15094):** Bypassed the Grunt by taking the Eastern route (Row 5 -> Col 14 -> Row 8).
- **Current Position:** `(14, 8)`.
- **Immediate Goal:** Pick up Item Ball at `(13, 9)` and Rescue Director at `(12, 8)`.
- **Action (Turn 15097):** Picked up TM35 (Sleep Talk) at `(13, 9)`.
- **Next Step:** Talking to the Director at `(12, 8)`.
- **Action (Turn 15100):** Talked to Director. Received **CARD KEY**.
- **Information:** Team Rocket took over Radio Tower to control Pokémon via a signal.
- **Objective:** Go to Radio Tower 3F and use Card Key to open shutters.
- **Plan:** Exit Warehouse via Ladder at `(17, 2)` (likely shortcut), then head to Radio Tower.
- **Objective Update (Turn 15102):** Rescue complete.
- **New Path:** The path East from `(9, 3)` is blocked (Row 3, Col 10-13 are Walls). Must use the northernmost corridor (Row 1) to cross from West to East.
- **Route:** `(13, 8)` -> `(14, 5)` -> `(9, 5)` -> `(9, 1)` -> `(17, 1)` -> `(17, 2)`.
- **Plan:** Executing route to the Ladder.
- **Current State:**
    - **Location:** Goldenrod City (11_2).
    - **Position:** `(9, 15)` (Outside Radio Tower).
    - **Objective:** Enter Radio Tower.
    - **Inventory:** Card Key, Amulet Coin.
- **Plan:**
    1. Detour South to Row 16 to bypass the Rocket Grunt at `(8, 15)`.
    2. Enter Radio Tower at `(5, 15)`.
    3. Proceed to 3F.
- **Transition (Turn 15131):** Entered **Radio Tower 1F (3_17)**.
- **Current Position:** `(2, 7)`.
- **Objective:** Reach 3F to use Card Key.
- **Plan:** Take stairs at `(15, 0)` to 2F. Avoid the Grunt at `(14, 1)` (Marked defeated, but taking safe path via Row 2).
- **Transition (Turn 15132):** Arrived at Radio Tower 2F (3_18).
- **Objective:** Reach stairs to 3F at `(0, 0)`.
- **Plan:** Navigate West across the room. Expecting battles with Rocket Grunts.
- **Current State:**
    - **Location:** Radio Tower 3F (3_19).
    - **Position:** `(11, 4)`.
    - **Objective:** Use Card Key at Slot `(14, 2)`.
    - **Obstacle:** Cooltrainer F (ID 3) moving between `(11, 4)` and `(12, 4)`.
- **Action (Turn 15134):** Navigating around the Cooltrainer via `(11, 3)` to reach `(14, 3)`.
- **Plan:**
    1. Move to `(14, 3)`.
    2. Interact with Card Key Slot `(14, 2)`.
    3. Proceed to 4F.