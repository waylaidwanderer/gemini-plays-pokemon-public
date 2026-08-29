# Pokémon Mansion - Multi-Floor Switch & Barrier Permutations

## Global Switch Mechanics & Rules (Empirically Verified)
1. **Global Toggle**: Any Mewtwo statue switch flips ALL floors simultaneously between State A (Default) and State B (Toggled).
2. **Exterior Reset**: Leaving the Pokémon Mansion (via front door or DIG) immediately and reliably resets all switches globally to State A (Default). (Verified Turn 18942 via DIG).

## Empirical Barrier State Matrix

| Floor | Barrier Location | State A (Default) | State B (Toggled) |
|---|---|---|---|
| 1F | Shutter at (24..25, 13) [Enclosed Wing to B1F Stairs] | **OPEN** | CLOSED (Verified Turn 18520, 18673, 18935) |
| 1F | Shutter at (26..27, 27) [Southeast Shutter Barrier] | **CLOSED** (Verified Turn 19115) | OPEN |
| 2F | Doorways at (4, 7) and (6, 7) | **OPEN** (Verified Turn 18581) | CLOSED |
| 2F | Shutter at (21, 17) [West-East Divider] | **CLOSED** (Verified Turn 18601) | OPEN |
| 2F | Shutter at (26..27, 27) [Southeast Corner] | **CLOSED** (Verified Turn 18598) | OPEN |
| 3F | Shutter at (15, 10..11) | **CLOSED** | OPEN (Verified Turn 18658, 18898) |

## Balcony Pit Drop Empirical Matrix (3F -> Destination)
| Departure Tile (Floor 3F) | Landing Tile (Floor, X, Y) | Resulting Area / Access | Status |
|---|---|---|---|
| 3F (16, 14) [Left Pit Drop] | 1F (16, 14) | 1F South Wing (TM03, Scientist Ted) | Confirmed (Turns 18495, 18661) |
| 3F (17, 14) [Left/Center Pit Drop] | 1F (16, 14) | 1F South Wing (TM03, Scientist Ted) | Confirmed (Turn 18902) |
| 3F (19, 14) [Right Pit Drop] | 1F (18, 14) | 1F Northern Landing Sector (Journal at (18, 2), Switch at (15, 11)) | VERIFIED (Turn 19000) |

## Step-by-Step Execution Protocol
1. Ascend to 3F (6, 2) via 2F (6, 1).
2. Toggle switch at (10, 5) to State B (opens (15, 11) shutter).
3. Walk east through (15, 11) into Balcony room (cols 16-27).
4. Walk east past column 17 to the RIGHT section of the balcony pit (cols 18-21).
5. Face Down and step south into the right pit drop.
6. Land on 1F behind the closed shutter gate in the northern chamber (rows 10-12).
7. Descend staircase to B1F and retrieve Secret Key.

## Disproven Hypotheses & Pruned Sequences
- Row 22 Eastward Traversal: Disproven on Turn 19384. Column 14 (rows 16-25) is an impassable vertical wall; row 22 does not connect the west and east wings.
- 1F Direct Descent in State A: Disproven on Turn 19433. Row 8 solid wall at (24..28, 8) and rubble field at (22..23, 8..15) block northern descent into the B1F stairwell chamber.

## Empirically Verified 1F Collision & Barrier Matrix
| Feature / Coordinate | Type | Details / Open Passages |
|---|---|---|
| Col 15 (rows 0-5) | Vertical Wall | Blocks east-west traversal at row 3 between west/east sectors. Passable at row 6-7 (15, 6..7). |
| Col 14 (rows 16-25) | Vertical Wall | Blocks east traversal from Central Hall at row 22 into Enclosed East Wing. |
| Row 8 Divider | Horizontal Barrier | Walls/counters at (14..17, 8), (20..21, 8), and (24..28, 8). Passable open gap at (18..19, 8). |
| Row 16 Divider | Horizontal Wall | Solid wall/fence across cols 18-25 dividing upper and lower east wing. |
| Rubble Fields | Blocked Tiles | (22..24, 4..5), (23..27, 6..7), (22, 8..15), (26..28, 9). |
| North Thoroughfare (Row 3) | Open Corridor | Cols 16-27 open east-west corridor above rubble field. |
| East Alcove (cols 27-28, rows 4-7) | Dead-end Alcove | Open at rows 4-7, blocked at south end by (28, 8) solid wall. |
| Shutter at (24..25, 13) | Toggle Gate | OPEN in State A (Default), CLOSED in State B (Toggled). Connects rows 10-12 to row 14. |
| Shutter at (26..27, 27) | Toggle Gate | CLOSED in State A (Default), OPEN in State B (Toggled). Connects Row 27 entrance hall to East Wing. |
| B1F Staircase | Dungeon Transition | Located at 1F (25, 14) inside the Eastern Sector. |