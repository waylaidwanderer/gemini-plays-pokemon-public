# Victory Road 1F - Layout & Notes

## General Information
- South exit / entrance: Route 23 at (8, 17)

## Observed Layout & Physical Features
- Entrance mat: (8..9, 17) (Safe to stand on; exit warp only triggers when stepping South off row 17 into row 18).
- Row 16 Corridor: Columns 1-9 across row 16 are completely open floor. (10..11, 16) is a 2x2 rock obstacle.
- Row 14 Highway: Columns 8-17 across row 14 form an open horizontal highway connecting the foyer (col 8) to the Eastern Switch Chamber (col 17). Note: (6..7, 14) and (6, 15) are solid rock obstacles blocking row 14 westward.
- Eastern Chamber: Columns 14-17 (rows 11-16). Contains Switch Plate at (17, 15). (15, 13) is a solid rock wall; detour via col 14: (16, 14) -> (14, 14) -> (14, 12) -> (15, 12).
- Boulder 1 (Default Start): (5, 15).
- Western Corridor: Columns 1-3 (rows 10-16). Contains Switch Plate at (1, 16) and Western Boulder (Boulder 2) at (2, 10).
- Shutters: Shutter (5, 13) and Shutter (7, 7) lowered permanently for current visit when Switch (17, 15) is depressed by Boulder 1!
- Elevated Plateau: Connected via lowered Shutter (5, 13) -> Row 12 Cross-Highway (5..12, 12) -> Col 11 North Avenue (11, 6..12) -> Row 6 West Avenue (7..11, 6) -> lowered Shutter (7, 7) -> Row 8 lower floor (3..7, 8) -> Col 3 North Avenue (3, 1..8) -> SW 2F Ladder at (1, 1) (enters 2F at (0, 8)).

## Verified Master Boulder Solution Protocol
- Initial State: Boulder 1 at (5, 15), Player at (5, 14), Strength active.

### Atomic Checkpoints:
1. **Checkpoint 1 (Push Down to Row 16)**:
   - From (5, 14) facing Down: Push Down 1 time. [Boulder at (5, 16), Player at (5, 15)]
   - Reposition: Up 1 to (5, 14) -> Left 1 to (4, 14) -> Down 2 to (4, 16) facing East.
2. **Checkpoint 2 (Push East along Row 16 to Col 9)**:
   - From (4, 16) facing East: Push East 4 times along row 16. [Boulder at (9, 16), Player at (8, 16)]
3. **Checkpoint 3 (Push North along Col 9 to Row 14)**:
   - Reposition: Down 1 to (8, 17) -> Right 1 to (9, 17) facing North.
   - From (9, 17) facing North: Push North 2 times. [Boulder at (9, 14), Player at (9, 15)]
4. **Checkpoint 4 (Push East along Row 14 to Col 16)**:
   - Reposition: Down 1 to (9, 16) -> Left 1 to (8, 16) -> Up 2 to (8, 14) facing East.
   - From (8, 14) facing East: Push East 7 times along row 14. [Boulder at (16, 14), Player at (15, 14)]
5. **Checkpoint 5 (Push North along Col 16 to Row 12)**:
   - Reposition: Down 1 to (15, 15) -> Right 1 to (16, 15) facing North.
   - From (16, 15) facing North: Push North 2 times. [Boulder at (16, 12), Player at (16, 13)]
6. **Checkpoint 6 (Push East to Col 17 & Lock onto Switch (17, 13))**:
   - Reposition (Detour around (15, 13) wall): Down 1 to (16, 14) -> Left 2 to (14, 14) -> Up 2 to (14, 12) -> Right 1 to (15, 12) facing East.
   - From (15, 12) facing East: Push East 1 time to (17, 12). [Boulder at (17, 12), Player at (16, 12)]
   - Reposition: Up 1 to (16, 11) -> Right 1 to (17, 11) -> Down 1 to (17, 14) facing South.
   - From (17, 14) facing South: Push South 1 time onto Switch (17, 15). [Boulder at (17, 15) SWITCH DEPRESSED, Player at (17, 14)]
7. **Checkpoint 7 (Ascent to 2F Southwest Ladder at (1, 1))**:
   - From (17, 12): Left 3 to (14, 12) -> Down 2 to (14, 14) -> West 9 to (5, 14) -> North 2 through lowered Shutter (5, 13) onto elevated cross-highway at (5, 12) -> East 6 to (11, 12) -> North 6 to (11, 6) -> West 4 to (7, 6) -> South 2 through lowered Shutter (7, 7) to lower cave floor (7, 8) -> West 4 to (3, 8) -> North 7 along col 3 to (3, 1) -> Left 2 through (2, 1) onto 2F Ladder at (1, 1) [Transitions to 2F at (0, 8)]!