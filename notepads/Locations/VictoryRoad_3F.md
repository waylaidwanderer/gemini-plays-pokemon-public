# Victory Road 3F Location Records (Map 0_198)

## Column 13 Passability Test
- **Conclusion**: Column 13 is a 100% verified dead end below Row 13. Horizontal bypass on Row 12 is blocked by walls on both sides ((12, 12) and (14, 12) are TYPE_2889). We cannot go south on foot from 3F West without solving the 2F puzzle to open the northeast barrier. We must backtrack to 2F.
- **Passability Database (3F Column 13)**:
  - (13, 7): [x] Passable
  - (13, 8): [x] Passable
  - (13, 9): [x] Passable
  - (13, 10): [x] Passable
  - (13, 11): [x] Passable
  - (13, 12): [ ] Occupied by Boulder C4
  - (13, 13): [x] Passable floor
  - (13, 14): [ ] IMPASSABLE - Solid rock wall (TYPE_2889)
  - (13, 15): [ ] IMPASSABLE - Solid rock wall (TYPE_2889)

## 3F East Geographic Boundaries and Obstacles (Verified Turn 101739)
- **Row 12 Solid Horizontal Wall (Columns 16-21)**: Row 12 is occupied by a continuous, impassable horizontal rock wall of TYPE_2889 across all Columns from 16 to 21. Standing at (20, 11) or (21, 11) and attempting to walk Down results in a physical collision against this solid rock wall, preventing direct vertical progression to the southern ground area (Rows 13-15).
- **Column 24 Solid Vertical Wall (Rows 11-15)**: Column 24 is occupied by a continuous, impassable vertical rock wall of TYPE_2889 across all Rows from 11 to 15. This completely isolates the left side of 3F East (Column 23 and below) from the right side of 3F East (Column 25 and above) on ground level, making the northern bypass via Row 2 strictly mandatory to cross between them on foot on 3F East.

## 3F East Geography Connections (Verified Turn 102114)
- **Ladder to 2F East**: Located at (27, 15) on 3F East.
  - Leads directly down to 2F East (Map 0_194) at (26, 14) on the plateau level behind the gated barrier.
  - Note: Taking this ladder transitions maps, resetting all overworld boulders on all maps.

## 3F East Boulder C2 Double-Push Puzzle (Verified Turn 102158)
- **Problem**: The Column 24 vertical rock wall completely divides 3F East, and Boulder C2 at (24, 10) blocks the only ground-level path past it on the east side of Row 10.
- **Solution**:
  1. Stand at (25, 10) facing Left and activate STRENGTH from the POKéMON party menu.
  2. Push the boulder Left once to (23, 10), step forward to (24, 10), and push it Left again to (22, 10).
  3. This clears Column 23, opening a bidirectional path around the Column 24 vertical wall via the southern Row 13 ground corridor.
## Central Plateau Blockage and Geography (Verified Turn 102227)
- **Column 11 Solid Vertical Wall (Rows 6-11)**: Column 11 is occupied by a continuous, impassable vertical rock wall of TYPE_2889 across all Rows from 6 to 11. Testing on Turn 102227 confirmed that walking Right (East) from (10, 10) results in a solid collision bump, proving that Column 11 is not a jump-down ramp or slope and the eastern edge of this central plateau (Column 10) is completely blocked horizontally.

## 3F West Boulder C1 Puzzle (Solved Turn 102347)
- **Problem**: Lowering the barrier blocking the ladder to 2F East at (23, 7).
- **Solution**:
  1. Climb to the western plateau, cross it, and descend the plateau stairs at (17, 5) to the ground floor of 3F West at (17, 6).
  2. Stand south of Boulder C1 (initially at (22, 3)), activate STRENGTH, and push Boulder C1 Up to (22, 1).
  3. Push Boulder C1 Left along the Row 1 corridor to Column 6.
  4. Bypass the Column 5 rock wall by pushing the boulder Down to Row 2 at (6, 2).
  5. Push the boulder Left along Row 2 to Column 2 at (2, 2).
  6. Push the boulder Down Column 2 to (2, 5).
  7. Walk to (1, 5) and push the boulder Right onto Switch C1 at (3, 5) (Solved on Turn 102347).
  8. This successfully lowers the central/eastern barrier on 3F East, opening access to the ladder at (23, 7).
## Geographic Wall Obstacles (Verified Turn 102747 & 102227)
- **Column 8 Solid Rock Wall (Rows 2-9)**: Column 8 features an impassable vertical cliff/rock wall that completely blocks horizontal passage between the left and right halves of 3F East ground floor across Rows 2-9.
- **Column 11 Solid Vertical Wall (Rows 6-11)**: Column 11 consists of a continuous, impassable vertical rock wall of TYPE_2889 across Rows 6-11, completely blocking any horizontal transition on the central plateau.