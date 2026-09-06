# Victory Road Master Strategy & Puzzle Log

## Core Dungeon Rules (Verified Turn 31589)
- Warping or changing floors (ladders/stairs/Dig/Escape Rope) resets all boulder positions and switches on the departed floor.
- Each floor's puzzle must be completed in one continuous session on that floor.

## Floor-by-Floor Master Solutions

1. **1F Master Solution**:
   - Strength activated by ATLAS.
   - Initial State: Boulder 1 @ (5, 15). Target: Switch @ (17, 13).
   - Push sequence: Down 1 to (5, 16) -> East 4 to (9, 16) -> North 2 to (9, 14) -> East 7 to (16, 14) -> North 2 to (16, 12) -> bypass via col 14 to (15, 12) -> East 1 to (17, 12) -> reposition to (17, 11) -> South 1 onto Switch (17, 13).
   - Shutters opened -> ascend Ladder (1, 1) to 2F (0, 8).

2. **2F Master Solution**:
   - Initial State: Arrive at (0, 8). Boulder 2 @ (4, 14). Switch 1 @ (1, 16).
   - Push sequence: From (5, 14) push Left 1 to (3, 14) -> reposition to (3, 13) -> push Down 2 to (3, 16) -> reposition to (4, 16) -> push Left 2 onto Switch 1 (1, 16).
   - Shutter 1 at (5, 10) and Shutter 3 at (21, 15) opened.
   - Path to 3F: Walk through Shutter 1 (5, 10) to row 8 -> East to (14, 8) -> South to (14, 12) -> East to (20, 12) -> bypass trainer via (20, 14) -> (21, 14) -> South through Shutter 3 (21, 15) to (21, 16) -> East to (29, 16) -> North along col 29 to (29, 11) -> West to **Ladder NE at (27, 7)** -> ascend to 3F Upper Dark Plateau (27, 7).

3. **3F Master Topology & Pit Drop Solution**:
   - 3F is divided into two distinct sectors:
     - Upper Dark Plateau / NW Room: accessed via NW Ladder (2, 0) and Ladder NE (27, 7). Contains Boulder 1 and Switch (3, 5).
     - Lower Purple Floor / Pit Room: accessed via Ladder B at (25, 14) from 2F. Contains Pit Boulder @ (22, 15) and The Pit @ (23, 15).
   - Route to Pit Drop:
     1. Ascend Ladder B at (25, 14) from 2F to 3F SE Room.
     2. Activate Strength with ATLAS.
     3. Walk from (25, 14) to (21, 14) -> Down 1 to (21, 15) (facing East beside Pit Boulder at (22, 15)).
     4. Push Right 1 time: Pit Boulder falls into Pit at (23, 15)!
     5. Step Right 1 time into Pit at (23, 15) -> Drop to 2F!

4. **2F Fallen Boulder to Indigo Plateau Exit**:
   - Land on 2F at (22, 16) with fallen boulder at (23, 16).
   - Push fallen boulder East along Row 16 from (23, 16) to (28, 16) (STOP AT COL 28!).
   - Reposition behind it at (28, 17) facing North.
   - Push North 5 times along Column 28: (28, 16) -> (28, 11).
   - Reposition to (29, 11) facing West.
   - Push West across Row 11 onto Switch Plate!
   - Ascend platform to the exit ladder -> Route 23 North / Indigo Plateau!
