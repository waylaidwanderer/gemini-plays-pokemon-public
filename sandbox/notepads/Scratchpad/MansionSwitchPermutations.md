# Pok�mon Mansion - Multi-Floor Switch & Barrier Permutations

## Overview
- Switches on Mewtwo statues toggle global shutter states across all floors (1F, 2F, 3F, B1F).
- Entering Mansion from exterior resets all switches to State A (Default).

## Empirical Barrier State Matrix

| Floor | Barrier Location | State A (Default) | State B (Toggled) |
|---|---|---|---|
| 1F | Shutter at (24..25, 13) [Enclosed Wing to B1F Stairs] | **OPEN** | CLOSED (Verified Turn 18520) |
| 2F | Doorways at (4, 7) and (6, 7) | **OPEN** (Verified Turn 18581) | CLOSED |
| 2F | Shutter at (21, 17) [West-East Divider] | **CLOSED** (Verified Turn 18601) | OPEN |
| 2F | Shutter at (26..27, 27) [Southeast Corner] | **CLOSED** (Verified Turn 18598) | OPEN |
| 3F | Shutter at (15, 10..11) | **CLOSED** | OPEN (Verified Turn 18658) |

## Drop-Off Pit Zones
- 3F Western Pit Gap: cols 6-9, rows 6-7
- 3F Eastern Balcony Drop: cols 16-18, rows 14-15 (requires 3F State B to access via (15, 11) shutter)
  - Testing landing zones: Left drop (16, 14) vs Right drop (17..18, 14) vs landing room mechanics.

## Exploration Plan
1. Drop down eastern balcony drop from 3F.
2. Document exact landing coordinates and test shutter connectivity on the destination floor.
3. Access B1F and retrieve Secret Key.
