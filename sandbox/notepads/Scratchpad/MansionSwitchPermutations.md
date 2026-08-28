# Pokémon Mansion - Multi-Floor Switch & Barrier Permutations

## Overview
- Switches on Mewtwo statues toggle global shutter states across all floors (1F, 2F, 3F, B1F).
- Entering Mansion from exterior resets all switches to State A (Default).

## Empirical Barrier State Matrix

| Floor | Barrier Location | State A (Default) | State B (Toggled) |
|---|---|---|---|
| 1F | Shutter at (24..25, 13) [Enclosed Wing to B1F Stairs] | **OPEN** | CLOSED (Verified Turn 18520, 18673) |
| 2F | Doorways at (4, 7) and (6, 7) | **OPEN** (Verified Turn 18581) | CLOSED |
| 2F | Shutter at (21, 17) [West-East Divider] | **CLOSED** (Verified Turn 18601) | OPEN |
| 2F | Shutter at (26..27, 27) [Southeast Corner] | **CLOSED** (Verified Turn 18598) | OPEN |
| 3F | Shutter at (15, 10..11) | **CLOSED** | OPEN (Verified Turn 18658) |

## Balcony Pit Drop Empirical Matrix (3F -> Destination)
| Departure Tile (Floor 3F) | Landing Tile (Floor, X, Y) | Resulting Area / Access | Status |
|---|---|---|---|
| 3F (16, 14) [Leftmost Pit Drop] | 1F (16, 14) | 1F South Wing (TM03, Scientist Ted) | Confirmed (Turns 18495, 18661) |
| 3F (17, 14) [Center Pit Drop] | TBD | Testing for 1F Northern Wing / B1F access | Pending |
| 3F (18, 14) / (19, 14) [Right Pit Drop] | TBD | Testing for 1F Northern Wing / B1F access | Pending |

## Execution Protocol
1. Ascend to 3F (6, 2) via 2F (6, 1).
2. Toggle switch at (10, 5) to State B (opens (15, 11) shutter).
3. Walk through (15, 11) into balcony room.
4. Position at (18, 13) or (17, 13) and jump down into pit from right side.
5. Record landing coordinates and proceed to B1F staircase.