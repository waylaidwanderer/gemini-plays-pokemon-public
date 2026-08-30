# Pokémon Mansion 2F - Layout & Exploration

## Overview
- Second floor of the ruined Pokémon Mansion.
- Features marble floors, Mewtwo statue switch, eastern computer wing, and stairs connecting 1F and 3F.

## Layout & Landmarks

### West / Central Sector
- Stairs down to 1F: (5, 10) [Arrival from 1F at (5, 11)]
- Wall Divider at Row 9: Solid horizontal wall across (3..7, 9) dividing south hallway from northwest room.
- Main South Corridor: (4..7, 10..27) red carpet hallway.
- Connecting East-West Corridor: Row 11 (cols 4-12) connects main hall to column 12 thoroughfare.

### Northwest Room
- Boundaries: cols 1-8, rows 1-7
- Interior: Rubble at (1..3, 2..3), wooden table at (6..7, 4..5), doorway at (4, 6..7).
- Mewtwo Statue Switch: Located at (2, 4..5) (base/switch at (2, 5), head at (2, 4)). Interactable from (2, 6) facing Up or (3, 5) facing Left. Verified Turn 19501.
- Note: Thoroughfare along row 1 (cols 4-12).

### Stairs to 3F
- **East Wing Stairs**: Located at (21, 23) behind the (21, 17) shutter gate (OPEN in State B). Leads up to 3F Northeast Sector.
- **Southwest Wing Stairs**: Located at (7, 10) in the central sector (immediately adjacent to 1F descending stairs at (5, 10)). Accessible from main hallway (cols 4-7, rows 10-11) or via col 12 thoroughfare -> row 11 -> (7, 11) -> (7, 10). Arrival on 3F: Southwest Wing at (7, 11) [Dead-end sector with TM09 Take Down and research journal].

### East Wing (Explored Turns 18593-18750)
- Thoroughfare Column 12: Unobstructed north-south corridor connecting row 11 to row 1, bypassing all rubble at rows 8-9.
- Computer terminals along row 2: (13, 2), (15, 2), (17, 2), (19, 2)
- Item Ball: (14, 3) [Collected Turn 18593]
- Shutter Barrier (North-Central): (20..21, 17) [OPEN in State A, CLOSED in State B]; Passage at (24..25, 17) [CLOSED in State A, OPEN in State B]
- Shutter Barrier (Southeast): (26..27, 27) [CLOSED in State A, OPEN in State B]
- Doorway connections: (26..27, 4), (24..25, 13)
- Corridors: Row 1 (cols 4-27), Row 3 (cols 10-27), Row 16 (cols 21-28), Col 26 (rows 4-12, 14-26)

- Shutter Barrier (North-Central Row 7): (16..17, 7) [OPEN in State A, CLOSED in State B] (Empirically verified Turn 19581).

- Shutter Barrier (Row 8): (18..19, 8) [OPEN in State A, CLOSED in State B] (Empirically verified Turn 19604).

## State & Switch Mechanics
- State A (Default): Doorway (26..27, 4) and (4, 7) OPEN; Shutter at (9, 4..5) OPEN; Shutters at (21, 17) and (26..27, 27) CLOSED.
- State B (Toggled): Shutter at (21, 17) OPEN; Shutter at (26..27, 27) CLOSED/Solid; Shutter at (9, 4..5) CLOSED (verified Turn 19762).
- Column 9 Divider: Vertical wall at rows 0-3 and rows 6-8. Open hallway gap connecting West and East wings is at rows 4-5 (cols 6-12) with shutter gate at (9, 4..5).


## Verified Collision Boundaries & Topography (Empirical Verification)
- Column 11 Wall: Continuous solid divider wall from row 14 down to the south boundary wall at row 27. Columns 8-10 are a dead end at the southern boundary.
- State A Direct Path to 3F Stairs:
  1. From 2F arrival at (5, 11), walk north to (5, 5).
  2. Walk east through the open shutter gate at (9, 4..5) to (16, 5).
  3. Walk south through the open shutter gate at (16..17, 7) into cols 12-17.
  4. Walk south down to row 20 at (16, 20).
  5. Walk east along row 20 to (21, 20).
  6. Walk south down col 21 to (21, 23) and ascend stairs to 3F!
- State B Features: Opens passage at (24..25, 17) into southeast wing; closes (9, 4..5), (16..17, 7), and (18..19, 8).