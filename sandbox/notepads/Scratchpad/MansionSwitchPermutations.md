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
| 3F | Shutter at (10, 3) | **CLOSED** | OPEN (Verified Turn 18484) |

## Optimal Secret Key Route
1. Enter 1F in State A (Default).
2. Ascend to 2F via (5, 10).
3. Walk to (6, 1) on 2F in State A (doorways open) and ascend to 3F (6, 2).
4. DO NOT toggle switch on 3F!
5. Drop down balcony pit (rows 6-7, cols 6-9) to 1F (16, 14).
6. Pass through OPEN shutter at (24..25, 13) into northern chamber to B1F stairs.
