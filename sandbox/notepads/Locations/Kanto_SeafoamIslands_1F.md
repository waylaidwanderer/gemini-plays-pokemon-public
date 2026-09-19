# Seafoam Islands 1F Geography & Layout

## Overview
- Ground floor of Seafoam Islands cavern complex.
- South-Western Entrance: Connected to Route 20 western dock; entrance threshold at (26, 17) [Turn 29159].
- South exit: Leads out to Route 20 western pier at (58, 9).

## Key Landmarks & Layout
- Southwest Entrance Enclosure: Cols 21..27, rows 12..16. Enclosed by row 11 cliff (north), col 28 wall (east), row 16 wall (south), and col 20 dividing wall (west).
- Ladder 1 (SW): Located at (23, 15), descends to B1F.
- Ladder 2 (East): Located at (25, 14), descends to B1F.
- Ladder 3 (North): Located at (25, 3..4), descends to B1F.
- Eastern Docks & Corridors:
  - Northern open hallway at rows 7..8 (cols 21..28).
  - Dividing rock wall at row 5 (cols 20..28).
  - Col 20 dividing rock wall extends rows 2..9 and 12..15.
- Central Subterranean Waterway [Audited Turn 29184]:
  - Open water canal spanning cols 15..23, rows 8..11 (and cols 18..19, rows 6..7).
    - Eastern Dock: Wooden stairs at (23, 9) enters water at (23, 10).

## Wild Encounters
- Psyduck (Lv 30) [Encountered Turn 29161].
- Krabby (Lv 28) [Encountered Turn 29165].
- Krabby (Lv 31) [Encountered Turn 29175].

## Rapid Water Current Mechanic [Empirically Verified Turns 29185, 29413]
- Tile (15, 8) in front of dock (15, 7) triggers an automatic rapid water current forced movement script.
- Scripted Trajectory: (15, 8) -> South along col 15 to (15, 11) -> East along row 11 to (20, 11) -> South down col 20 to (20, 16) -> Drops over waterfall into B4F subterranean lake at (20, 15).
- Dock at (15, 7) cannot be boarded from the south water canal while the upper current is active.
