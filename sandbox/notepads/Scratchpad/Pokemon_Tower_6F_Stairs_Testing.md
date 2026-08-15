# Pokémon Tower 6F 7F Staircase Systematic Probing Matrix

## Objective
Locate and verify the active warp tile leading to Pokémon Tower 7F.

## Probing Log
- (9, 16): Stepped onto from (10, 16) via Left. Player stood at (9, 16) facing Left. Pressed Left -> bumped into solid wall (8, 16). Result: No warp.
- Next Tests:
  1. Test South wing corridor tiles: (10, 16), (11, 16), (12, 16), (11, 15), (10, 15).
  2. Test West wing landing: (3, 9) / (4, 9) [Pattern from 2F and 4F].
- Turn 55263: Visual confirmation from CurrentScreen turn 55263: Tile (9, 16) is definitively the 3-step yellow staircase graphic.
- Warp Trigger Analysis: In Gen 1, warps trigger upon taking a valid step that lands on the warp coordinate (9, 16). Player at (11, 16) stepping Left to (10, 16) then Left onto (9, 16) will trigger the active warp to 7F.
- Turn 55265: Stepping from (10, 16) Left onto (9, 16) did not trigger a warp. Testing West wing (3, 9) to verify if 6F follows the even-floor layout (2F/4F UP stairs at 3, 9). Routing from (10, 15) to (6, 6) to probe (3, 9).
- Turns 55265-55275: Systematic probing confirmed: (3, 9) has tombstones (no stairs); (9..12, 16) South corridor is a dead-end floor alcove (no active warp). Moving via Row 10 to probe unexplored Southeast wing (Columns 15..18, Rows 10..16).