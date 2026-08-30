# Pokémon Mansion 3F - Map & Navigation Log

## Physical Barriers & Solid Walls (Verified Turn 66718)
- **Column 1 Row 9 is a Solid Wall:** Column 1 Row 9 is NOT a shutter gate. It is a permanent, solid partition wall that blocks vertical passage across Row 9 on Columns 1-7 in both State A and State B.
- **Row 12 Column 2 Shutter Gate:** Walkable in State A, CLOSED and impassable in State B.
- **Column 10 Vertical Corridor:** Column 10 is completely open and walkable on Rows 9-16 on 3F West (unlike 2F West where it is blocked by rubble), providing the primary vertical passage between the northern and southern halves of 3F West.
- **Row 8 Debris:** Blocked by solid rubble on Columns 8-11, making Row 8 impassable horizontally on these columns.
- **Column 12 Vertical Passage:** Completely open vertically on Rows 6-12, providing an alternate vertical passage on 3F West.
- **Column 19 Row 17 Solid Wall (Verified Turn 67854):** Column 19 Row 17 is a permanent, solid wall/cabinet structure in both State A and State B, blocking direct vertical passage down Column 19 from Row 16 to the balcony.
- **Balcony Access Route (Verified Turn 67854):** To access the balcony drop at (19, 18), we must find a valid way through. However, the exact configuration of balcony gates in State A vs State B is still under investigation.

## 3F East - Mapping & Boundaries
- **Column 22 Partition Wall:** Solid vertical wall separating Columns 23-28 from Columns 15-21 on Rows 4-11.
- **Row 3 Horizontal Opening:** Row 3 is completely open across Column 22, allowing horizontal passage between 3F West/Middle and the northeastern Scientist room.
- **The Pitfall Trap is at (18, 16):** Located on Column 18, Row 16. Walking onto (18, 16) in State A drops the player to 1F East inside the fenced room. (Verified Turn 68591 visually and verified column connections).

## State B Proven Isolation & Blockages (Verified Turn 66911)
- **Western, Central, and Eastern Sections are Isolated:** In State B, 3F is divided into completely isolated vertical strips below Row 3:
  - **Column 11 Partition Wall:** Solid vertical wall on Rows 13-20, blocking horizontal travel.
  - **Column 13 Partition Wall:** Solid vertical wall on Rows 8-12, blocking horizontal travel.
  - **Column 21-23 Rubble:** Blocks Rows 7-13, preventing horizontal travel.
  - **Row 13 Cabinet Barrier:** Solid counters/cabinets block Row 13 vertically on Columns 11-28.
  - **Row 7 Cabinet/Machine Barrier:** Solid counters/consoles block Row 7 vertically on Columns 13-21.
  - **Column 18 Wall:** Solid vertical wall on Row 16.
- **The Balcony is Inaccessible in State B:** Because of the above barriers, the central balcony area cannot be reached from either 3F East or 3F West while in State B.

## The Intended Mansion 3F Puzzle Solution (State A Route)
1. **Toggle Switch to State A:** From 3F East, walk via Column 26 Row 1 and Row 1 horizontally to 3F West Column 2 Row 6, face UP and toggle the Mewtwo switch at (2, 5) to State A (using exactly 5 A-presses since the default is YES).
2. **Fall through Pitfall:** Walk to Column 26 on 3F East and walk Down to trigger the pitfall. In State A, the pitfall is OPEN, and walking onto it drops you to 1F East inside the fenced room.
3. **Ascend via 2F East:**
   - From 1F East fenced room, take the stairs down to B1F East.
   - Walk through 1F West to the stairs up to 2F West.
   - On 2F, since State A gates on Row 11 are OPEN, walk freely to 2F East.
   - Take the northeast stairs at (22, 1) UP to 3F East.
4. **Access Balcony:** Land on 3F East at (22, 1). In State A, walk DOWN Column 27 (since Column 27 is completely open vertically to Row 9, avoiding pitfalls) to Row 9, walk Left to Column 26 at (26, 9), then walk DOWN Column 26 (completely open vertically below Row 9 to Row 16) to Row 16, walk Left along Row 16 to Column 21, walk DOWN Column 21 through the open balcony gates at (21, 17) to Row 18, and walk Left to (19, 18) to trigger the balcony drop warp and drop to B1F West to retrieve the Secret Key! (Note: The shutter gate at (25, 13) is closed in State A, so Column 25 is blocked at Row 13).

## Critical Switch Mechanics & Verification Constraints (Verified Turn 67356)
- **4 A-Press Sequence Required:** To fully toggle any Mewtwo Switch statue (e.g. at (2, 5)) and cleanly restore the overworld without leaving dialogue boxes open, a strict 4 A-press sequence is REQUIRED:
  1. **A-Press 1:** Interacts with the statue. "A secret switch!" text scrolls onto screen.
  2. **A-Press 2:** Advances text. YES/NO menu appears.
  3. **A-Press 3:** Selects YES (default). "Who wouldn't?" text scrolls onto screen.
  4. **A-Press 4:** Dismisses the textbox and restores the overworld.
- **Generous Delays (Minimum 1.5–2.5 seconds) are Mandatory:** You must sleep for at least 1.5 to 2.5 seconds between EACH A-press to allow text scrolling, menu animations, and redraws to complete. Pressing A too quickly will cause inputs to be swallowed, leaving the dialogue open and swallowing subsequent directional inputs.
- **Local Verification via (21, 2) Shutter Gate:** On 3F East, the local gate at (21, 2) is closed in State B and open in State A. Attempting to step Left from (22, 2) to (21, 2) is blocked in State B and successful in State A. This allows immediate local state verification without walking back to 3F West!
- **State A Traversal to Balcony (Via 3F West Stairs):** Once in State A, the stairs at (5, 10) on 3F West connect to 2F West. The balcony at (19, 18) can be reached on 3F East from (5, 10) by walking UP Column 5 to Row 3, RIGHT along Row 3 to Column 25, DOWN Column 25 (where (25, 13) gate is OPEN in State A) to Row 16, LEFT along Row 16 to Column 21, DOWN Column 21 through the open balcony gates at (21, 17) to Row 18, and LEFT to (19, 18) to trigger the balcony drop warp. This route never crosses Column 11 below Row 13, avoiding the permanent vertical partition wall.
## Global Mewtwo Switch Operational Mechanics (Verified Turn 67428)
- **Single Global State:** All Mewtwo statues across all floors of the Pokémon Mansion are globally linked. Interacting with ANY statue toggles the entire mansion between State A and State B.
- **Accidental Reversals:** Toggling a switch twice (or toggling different switches sequentially) will revert the mansion back to its original state. Always perform a single toggle and then verify locally at the (21, 2) gate.

## 3F West State B Separation Wall (Verified Turn 67428)
- **Column 9 Partition Wall:** Column 9 is a solid vertical brick wall on Rows 3-7, and is blocked by rubble on Row 8.
- **Crossing Constraints in State B:** Because of the Column 9 wall, the only way to cross horizontally between 3F East (Columns 10-28) and 3F West (Columns 1-8) in State B is via **Row 1 or Row 2**. Crossing below Row 3 is completely blocked.
- **NPC at (3, 3):** There is an NPC (trainer) standing at (3, 3) on 3F West. Column 3 is therefore blocked, but the parallel Column 4 is completely open on Rows 2-5, allowing clean vertical bypass.
## State A vs State B Gate Configurations & Detours (Verified Turn 68170)
- **Mansion Switch States:**
  - **State B (Default):**
    - Balcony gates at `(20, 17)` and `(21, 17)` are OPEN.
    - Shutter gate at `(25, 13)` on Column 25 is CLOSED (yellow/black striped gate).
    - Shutter gate at `(4, 6)` on 3F West is OPEN.
    - Shutter gates at `(19, 2)` and `(21, 2)` on 3F East are CLOSED.
  - **State A:**
    - Balcony gates at `(20, 17)` and `(21, 17)` are CLOSED (blocked by yellow/black horizontal stripes).
    - Shutter gate at `(25, 13)` on Column 25 is OPEN (completely passable door frame).
    - Shutter gate at `(4, 6)` on 3F West is CLOSED (blocked by green frame).
    - Shutter gates at `(19, 2)` and `(21, 2)` on 3F East are OPEN.

## Verified Detour Routes on 3F East
- **Bypassing Column 9 Partition Wall (Rows 3-7):**
  - Walk UP to Row 1 or Row 2 which are completely open across Column 9.
- **Bypassing Row 4 Horizontal Wall (Columns 22-25):**
  - Walk Right to Column 26. Walk DOWN Column 26 (completely open vertically) to Row 12. Walk Left to Column 25 on Row 12 to resume vertical traversal down Column 25.
- **Bypassing Closed Shutter Gate at (4, 6) in State A:**
  - Walk from `(2, 6)` UP through Column 3 and Column 4 (`(3, 6)` -> `(3, 5)` -> `(4, 5)` -> `(4, 4)` -> `(4, 3)`) to Row 3, completely bypassing the closed gate.