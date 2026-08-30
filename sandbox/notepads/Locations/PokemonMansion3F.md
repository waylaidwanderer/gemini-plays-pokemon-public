# Pokémon Mansion 3F - Map & Navigation Log

## Physical Barriers & Solid Walls (Verified Turn 66718)
- **Column 1 Row 9 is a Solid Wall:** Column 1 Row 9 is NOT a shutter gate. It is a permanent, solid partition wall that blocks vertical passage across Row 9 on Columns 1-7 in both State A and State B.
- **Row 12 Column 2 Shutter Gate:** Walkable in State A, CLOSED and impassable in State B.
- **Column 10 Vertical Corridor:** Column 10 is completely open and walkable on Rows 9-16 on 3F West (unlike 2F West where it is blocked by rubble), providing the primary vertical passage between the northern and southern halves of 3F West.
- **Row 8 Debris:** Blocked by solid rubble on Columns 8-11, making Row 8 impassable horizontally on these columns.
- **Column 12 Vertical Passage:** Completely open vertically on Rows 6-12, providing an alternate vertical passage on 3F West.
- **Row 1 Horizontal Corridor:** Completely open horizontally across 3F East and 3F West, but Column 22 on Row 1 is blocked horizontally by the recessed staircase structure at (22, 1). To cross between 3F East and 3F West, you must use Row 3.

## 3F East - Mapping & Boundaries
- **Column 22 Partition Wall:** Solid vertical wall separating Columns 23-28 from Columns 15-21 on Rows 4-11.
- **Row 3 Horizontal Opening:** Row 3 is completely open across Column 22, allowing horizontal passage between 3F West/Middle and the northeastern Scientist room.
- **The Pitfall Trap location:** Located on Column 26. Walking down Column 26 in State A (stepping on (26, 3) or (26, 6)) drops the player to 1F East inside the fenced room.

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
4. **Access Balcony:** Land on 3F East at (22, 1). Walk down Column 25 (which is completely open to Row 16). Since the balcony shutter gates at (20, 17) and (21, 17) are OPEN in State A, walk through them to the balcony at (19, 18) and drop to B1F West to retrieve the Secret Key!

## Shutter Gate at (3, 6) Local Verification Logic (Verified Turn 67240)
- **Mewtwo Switch Gate at (3, 6) on 3F West:**
  - **State A:** CLOSED. Vertical and horizontal passage between `(2, 6)` and `(3, 6)` is completely BLOCKED by the closed shutter gate.
  - **State B:** OPEN. Completely walkable and passable.
  - **The Switch Gate Verification Protocol:**
    - To 100% verify that State A is active locally after toggling, try to step Right from `(2, 6)` to `(3, 6)`.
    - If you are BLOCKED (position remains at `(2, 6)`), then State A is active!
    - If you successfully step to `(3, 6)`, then State B is active!

## Critical Switch Mechanics & Verification Constraints (Verified Turn 67356)
- **4 A-Press Sequence Required:** To fully toggle any Mewtwo Switch statue (e.g. at (2, 5) or (12, 11)) and cleanly restore the overworld without leaving dialogue boxes open, a strict 4 A-press sequence is REQUIRED:
  1. **A-Press 1:** Interacts with the statue. "A secret switch!" text scrolls onto screen.
  2. **A-Press 2:** Advances text. YES/NO menu appears.
  3. **A-Press 3:** Selects YES (default). "Who wouldn't?" text scrolls onto screen.
  4. **A-Press 4:** Dismisses the textbox and restores the overworld.
- **Generous Delays (Minimum 1.5–2.5 seconds) are Mandatory:** You must sleep for at least 1.5 to 2.5 seconds between EACH A-press to allow text scrolling, menu animations, and redraws to complete. Pressing A too quickly will cause inputs to be swallowed, leaving the dialogue open and swallowing subsequent directional inputs.
- **Local Verification via (21, 2) Shutter Gate:** On 3F East, the local gate at (21, 2) is closed in State B and open in State A. Attempting to step Left from (22, 2) to (21, 2) is blocked in State B and successful in State A. This allows immediate local state verification without walking back to 3F West!
- **State A Traversal to Balcony (No Pitfall Needed):** If the gate at (21, 2) is open (State A), you can walk horizontally along Row 2 directly to Column 10 on 3F West, walk down Column 10 to Row 16, and walk Right directly to the balcony at (19, 18) to drop to B1F West. Falling through the Column 26 pitfall is completely unnecessary if we are already on 3F East in State A!
## Global Mewtwo Switch Operational Mechanics (Verified Turn 67428)
- **Single Global State:** All Mewtwo statues across all floors of the Pokémon Mansion are globally linked. Interacting with ANY statue toggles the entire mansion between State A and State B.
- **Accidental Reversals:** Toggling a switch twice (or toggling different switches sequentially) will revert the mansion back to its original state. Always perform a single toggle and then verify locally at the (21, 2) gate.

## 3F West State B Separation Wall (Verified Turn 67428)
- **Column 9 Partition Wall:** Column 9 is a solid vertical brick wall on Rows 3-7, and is blocked by rubble on Row 8.
- **Crossing Constraints in State B:** Because of the Column 9 wall, the only way to cross horizontally between 3F East (Columns 10-28) and 3F West (Columns 1-8) in State B is via **Row 1 or Row 2**. Crossing below Row 3 is completely blocked.
- **NPC at (3, 3):** There is an NPC (trainer) standing at (3, 3) on 3F West. Column 3 is therefore blocked, but the parallel Column 4 is completely open on Rows 2-5, allowing clean vertical bypass.