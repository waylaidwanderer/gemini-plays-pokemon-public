# Victory Road Master Strategy & Puzzle Log

## Core Dungeon Rules (Verified Turn 32306)
- Native floor boulders and switches reset upon floor transitions (ladders/stairs/Dig/Escape Rope).
- Pit-Dropped Boulders: Once dropped through a pit from 3F to 2F, the boulder permanently persists on 2F at (23, 16) across inter-floor ladder transitions during the dungeon visit.
- Each floor's native puzzle must be completed in one continuous session on that floor.

## Floor-by-Floor Master Solutions

1. **1F Master Solution** (COMPLETED):
   - Strength activated by ATLAS.
   - Initial State: Boulder 1 @ (5, 15). Target: Switch @ (17, 13).
   - Push sequence: Down 1 to (5, 16) -> East 4 to (9, 16) -> North 2 to (9, 14) -> East 7 to (16, 14) -> North 2 to (16, 12) -> bypass via col 14 to (15, 12) -> East 1 to (17, 12) -> reposition to (17, 11) -> South 1 onto Switch (17, 13).
   - Shutters opened -> ascend Ladder (1, 1) to 2F (0, 8).

2. **2F Master Solution** (COMPLETED):
   - Initial State: Arrive at (0, 8). Boulder 2 @ (4, 14). Switch 1 @ (1, 16).
   - Push sequence: From (5, 14) push Left 1 to (3, 14) -> reposition to (3, 13) -> push Down 2 to (3, 16) -> reposition to (4, 16) -> push Left 2 onto Switch 1 (1, 16).
   - Shutter 1 at (5, 10) and Shutter 3 at (21, 15) opened.
   - Route to Upper Plateau & Ladder A: From (5, 8) east to (17, 8) -> north along column 17 to (17, 2) -> east along row 2 to (28, 2) -> south to (28, 8) -> west to Ladder A at (23, 7) -> ascend to 3F.

3. **3F Master Topology & Pit Drop Solution**:
   - 3F Sectors:
     - Upper Dark Plateau / NW Room: accessed via NW Ladder (2, 0), Ladder A (23, 7), and Ladder NE (27, 7).
     - Lower Purple Floor / Pit Room: contains Pit Boulder @ (22, 15) and The Pit @ (23, 15).
   - Route to Pit Drop:
     1. Ascend to 3F via Ladder A at (23, 7).
     2. Activate Strength with ATLAS.
     3. Walk to Pit Room at (21, 15) facing East beside Pit Boulder at (22, 15).
     4. Push Right 1 time: Pit Boulder falls into Pit at (23, 15)!
     5. Step Right 1 time into Pit at (23, 15) -> Drop to 2F!

4. **2F Fallen Boulder to Indigo Plateau Exit**:
   - Dropping boulder from 3F SE room hole lands on 2F at (23, 16).
   - Push fallen boulder onto switch on 2F to lower Shutter at (27, 10) blocking Ladder NE.
   - Ascend via Ladder NE at (27, 7) to reach 3F final exit sector and exit to Indigo Plateau!
