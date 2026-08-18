# Scratchpad - Rock Tunnel 1F Southern Exit Route

## Current Position & Active Route
- Current Location: Rock Tunnel 1F (x=3, y=15)
- Active Plan: Defeat wild Machop, descend col 3 to row 18, cross east along row 18 to Central Thoroughfare (cols 8-11), descend to row 21, and follow verified corridor east to the South Exit at (37, 17).

## Empirical Collision Matrix (Physically Verified Coordinates)
- Passable Walkways (Verified):
  - (3..5, 14..15), (4, 5..14)
  - (2..4, 15..18)
  - (7..11, 6), (11, 8..6)
  - (11..16, 16), (17..21, 16)
  - (8..11, 14..21), (2..21, 21)
- Collision Walls & Blockers (Verified):
  - (5, 16): Solid rock protrusion (bumped Turn 4761)
  - (6, 14), (6, 15): Solid rock divider (bumped Turn 4758, 4761)
  - (7, 5): Solid rock wall (bumped Turn 4742)
  - (17, 15): Solid rock wall (bumped Turn 4715)
  - (2..7, 22..23), (17..23, 22..23): Solid rock boundary
  - (22..23, 16..22): Vertical rock pillar
  - (8..9, 1..5): Rock obstacle east of Ladder 2 (5, 3)

## Incremental Traversal Protocol
1. Press 'A' to execute Tackle and defeat wild Machop.
2. Clear victory text to restore overworld at (3, 15).
3. Walk 3 steps Down along col 3 to (3, 18).
4. Walk 5 steps East along row 18 to (8, 18).
5. Walk 3 steps Down along col 8 to (8, 21).
6. Walk East along row 21 to (21, 21).
7. Probe connection from (21, 21) to col 24 and row 17 -> South Exit at (37, 17).