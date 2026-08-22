# Cinnabar Island - Overworld Map & Landmarks

## Warp Locations & Door Coordinates
- **Pok�mon Mansion Entrance:** Located at `(6, 3)`. Stepping UP into `(6, 3)` warps the player inside Mansion 1F West at the doormat `(2, 7)`.
  - *Asymmetrical Warp Note:* Exiting the Mansion from the doormat `(2, 7)` warps the player outside to `(6, 10)` in front of the Pok�mon Lab door!
- **Pok�mon Lab Entrance:** Located at `(6, 9)`. Stepping UP into `(6, 9)` warps the player inside the Pok�mon Lab lobby at `(2, 7)`.
- **Pok�mon Center Entrance:** Located at `(11, 11)`. Stepping UP into `(11, 11)` warps the player inside the Pok�mon Center lobby at `(3, 7)`.
- **Pok� Mart Entrance:** Located at `(15, 11)`. Stepping UP into `(15, 11)` warps the player inside the Pok� Mart lobby at `(3, 7)`.
- **Cinnabar Island Gym Entrance:** Located at `(18, 4)`. Currently locked and requires the Secret Key to open.

## Shoreline & Collision Boundaries
- **Western Coastline:** Columns 2 and 3 have deep water tiles.
- **Shore Cliff Boundary:** Column 4 Row 12 and Column 5 Row 12 are solid shore cliffs and block all horizontal traversal.
- **Walkable West Passage:** Column 4 is open vertically from Row 11 up to Row 4. Crossing from Column 6 (Lab hallway area) to Column 4 must be done on Row 11 `(6, 11) -> (5, 11) -> (4, 11)` to bypass the solid shore cliff.

## Safety Bypass Route to enter the Mansion safely from (6, 10):
1. From `(6, 10)`, walk DOWN to `(6, 11)`.
2. Walk LEFT to Column 4: `(5, 11) -> (4, 11)`.
3. Walk UP Column 4 to Row 4: `(4, 11) -> (4, 4)`.
4. Walk RIGHT to Column 6: `(5, 4) -> (6, 4)`.
5. Walk UP into `(6, 3)` to enter the Mansion!
