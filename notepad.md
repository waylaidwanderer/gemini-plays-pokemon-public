# Dept Store Basement Notes

## Key Information
- **Goal:** Reach East side (Items/Ladder/Uniform?).
- **Current State:**
    - Top Gates (10, 8-9): OPEN (Floor).
    - Bottom Gates (10, 12-13): CLOSED (Wall/Box).
    - East Room Access: Top accessible, Bottom blocked.
    - North East Item/Ladder: Blocked by Wall at Row 4.

## Puzzle Status: FAILED Hypotheses
1. **NPC Facing Direction:** Making NPCs face specific directions did NOT open gates.
2. **NPC Position:** NPC 5's patrol loop (9, 9 to 9, 11) does NOT seem to trigger gates.
3. **"Behind the Scenes":** Entering the East Room (out of sight) did NOT change gate state.
4. **Map Reload:** Exiting/Re-entering via Elevator did NOT reset gate state.
5. **Machoke:** Pushing the Machoke (7, 7) failed (Solid Object).
6. **Hidden Items:** "Junk" hint checked at (11, 12) inside cage. Found nothing.

## Current Strategy: Strength
- **Hypothesis:** The "Junk" refers to the boxes themselves acting as boulders.
- **Action:** Using STRENGTH to push the boxes at (10, 12) and (10, 13).
- **Plan:**
    1. Navigate to (9, 12).
    2. Walk Right into (10, 12) to PUSH.
    3. If that works, path opens to South East.

## Dialogue Log
- **NPC 5 (Middle):** "Our policy is to work behind the scenes where no one can see us!"
- **NPC 6 (Top Left):** "I lose my passion for work if someone's watching."
- **NPC 7 (Bottom Left):** "The stuff on the ground's junk. Take it if you want it!"

## Map Features
- **Elevator:** Warps to other floors.
- **Ladder (17, 2):** To 1F (Blocked).
- **Boxes:** (10, 8-9) and (10, 12-13).

## Tile Mechanics
- **WALL:** Impassable.
- **FLOOR:** Walkable.
- **WARP_CARPET_UP:** Walkable, triggers warp.
- **LADDER:** Interactable/Walkable, triggers warp.
- **BOXES:** Function as WALL tiles unless pushed?