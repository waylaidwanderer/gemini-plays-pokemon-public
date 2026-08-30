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


## Verified Collision Boundaries & Topography
- Empirical Test (Turn 21017): Shutter at (21, 17) is CLOSED in State A; stepping Down into (21, 17) resulted in a 0-tile collision.
 (Turns 20980-21000)
- Central Hallway (cols 4-7, rows 10-27): Southern end dead-ends at solid wall at (4..7, 27). No stairs at south end of central carpet.
- Column 12 Thoroughfare: Open from row 1 to row 12; BLOCKED at row 13 by solid horizontal wall at (11..17, 13).
- Row 13 Bypass: Open passage between upper (rows 9-12) and lower (rows 14-27) corridors is at cols 8-10 (8..10, 13).
- Column 11 Wall Divider: Solid vertical wall from row 14 down to row 24, dividing col 10 from cols 12-15.
- Northwest Room: Green display table at (4, 6..7); large wooden table at (6..7, 4..5); rubble at (1..3, 2..3); Mewtwo statue switch at (2, 5) / (2, 4).