# Dept Store Basement Notes

## Key Information
- **Goal:** Reach East side (Items/Ladder/Uniform?).
- **Current State:**
    - Top Gates (10, 8-9): OPEN (Floor).
    - Bottom Gates (10, 12-13): CLOSED (Wall/Box).
    - East Room Access: Top accessible, Bottom blocked.
    - North East Item/Ladder: Blocked by Wall at Row 4.

## Puzzle Status: FAILED Hypotheses
1. **NPC Facing Direction:** Making NPCs face specific directions (Up/Left/Right) did NOT open gates.
2. **NPC Position:** NPC 5's patrol loop (9, 9 to 9, 11) does NOT seem to trigger gates.
3. **"Behind the Scenes":** Entering the East Room (out of sight) did NOT change gate state.
4. **Map Reload:** Exiting/Re-entering via Elevator did NOT reset gate state.
5. **Machoke:** Pushing the Machoke (7, 7) failed (Solid Object).
6. **Hidden Items:** "Junk" hint checked at (11, 12) inside cage. Found nothing.
7. **Watching NPC 6:** Standing at (5, 8) facing Left did NOT toggle gates.

## Current Strategy: Physical Interaction
- **Hypothesis:** The "Junk" refers to the boxes in the West Room (`6, 8-11`) being pushable.
- **Action:** Test Pushing these boxes with Strength.
- **Plan:**
    1. Push Box at `(6, 8)` from North (`6, 7`) and West (`5, 8`).
    2. If fails, leave area to search for external triggers.

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
- **BOXES:** Function as WALL tiles. Testing if pushable.
- **Action:** Moved to `(5, 8)`. Interacted (Right+A) with Box `(6, 8)`.
- **Reason:** "Junk" hint + "Take it" -> Suggests interactable object (maybe Uniform?).
- **Hypothesis:** One of these boxes contains the Team Rocket Uniform.
- **Action:** Attempting to PUSH Box `(6, 8)` DOWN from `(6, 7)`.
- **Method:** Walk Down into the box. Strength is active.
- **Hypothesis:** These boxes are the "Junk" and can be moved to clear a path or reveal something.
- **Action:** Opening Menu to use Itemfinder manually.
- **Reason:** 'Select' button was mapped to Bicycle (Oak's Warning), so previous Itemfinder check was invalid.
- **Goal:** Conclusively test for hidden items in the "Junk" area.
- **Action:** Pressed A on Itemfinder in Menu.
- **Goal:** Check for hidden items near `(6, 7)`.
- **Hypothesis:** "Junk" hint implies hidden item.
- **Action:** Selected "USE" for Itemfinder.
- **Expectation:** Dialogue box with result.
- **Next:** If negative, I'm leaving B1F to check the Radio Tower entrance directly. I need to confirm if I can enter the building.
- **Result:** Itemfinder returned "Nope!". No hidden items near `(6, 7)`.
- **Conclusion:** "Junk" hint does NOT refer to a hidden item.
- **Last Resort:** Attempt to PUSH Box `(6, 8)` DOWN.
- **Reason:** I was distracted by Itemfinder before executing this push. If this fails, I am aborting the B1F puzzle entirely.
- **Exit Strategy:** Elevator to 1F -> Exit Dept Store -> Check Radio Tower.
- **Action:** Retrying Box Push at `(6, 8)` from the West `(5, 8)`.
- **Reason:** Previous attempt failed due to navigation error (I was at `6, 7`).
- **Logic:** If this is the "Junk" I can take, maybe I can push it aside.
- **Next:** If this is a WALL, I am leaving to the Underground.