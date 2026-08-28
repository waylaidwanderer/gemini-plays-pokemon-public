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

## Verified Solution Sequence (Turn 19046)
1. 3F right balcony drop at (19, 14) landed at 1F (18, 14) [North Landing Sector].
2. North Landing Sector connects via row 10 (9, 10) gap directly to 1F/2F stairs at (5, 10).
3. Toggled 2F Mewtwo statue switch at (2, 11) to State A.
4. In State A, 1F shutter gate at (24..25, 13) is OPEN.
5. In State A, traverse south along column 10 to row 22, walk east across the open row 22 hallway to column 25, and ascend north up column 25 to descend the staircase at (25, 14) into B1F!

## Verified 1F Thoroughfares & Route to B1F
- North Thoroughfare (Row 3): cols 12-27 open horizontal hallway.
- Northeast Room Doorway: (26, 4) leads south into Northeast Chamber (cols 24-28, rows 4-10).
- Row 8 Divider: Wall barrier at (20..21, 8) and (24..28, 8). Passable north-south gap at (18..19, 8).
- Column 12: Wall barrier at (12, 12..13); not a continuous north-south thoroughfare to South Wing.
- Switch at (15, 11): State A (Default) opens shutter at (24..25, 13).
- B1F Staircase: Located at 1F (25, 14).