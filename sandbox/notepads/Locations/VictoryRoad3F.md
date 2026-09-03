# Victory Road 3F - Layout & Notes

## General Information
- Ladder to 2F (Southeast): Located at (26, 8) (Spawn tile when arriving from 2F is (23, 7))
- Ladder to 2F (Northwest): Located at (2, 0)

## Observed Objects & Geometry
- Northwest Ladder: (2, 0) (connects to 2F NW ladder at (1, 1))
- Southeast Ladder: (26, 8) (connects to 2F SE ladder at (25, 14))
- Boulder 1 (Northeast): (22, 3) on upper plateau
- Shutter 1: (17, 5) [Opened by Switch Plate at (3, 5)] connecting North Central chamber (17, 4) to Central Hall (17, 6) [Verified Turn 24985]
- Western Elevated Bridge: Spans cols 6-7 from row 0 to row 6
- Switch Plate (Southwest): (3, 5) on elevated ledge / western floor
- Item Ball (West): (7, 7) on lower floor adjacent to bridge end
- Item Ball (Central-West): (11, 0) in chamber
- Item Ball (Northeast): (27, 5) [Collected Turn 24557]
- Pit Boulder: Located at (22, 15)
- Hole / Pit: Located at (23, 15)
- Central South Chokepoint: Tile (13, 14) is a solid rock wall

## Defeated Trainers (3F)
- [x] Cooltrainer (M): Located at (28, 5) [Defeated Turn 23834]. Roster: Exeggutor Lv 43, Cloyster Lv 43, Arcanine Lv 43. Reward: 1548 Yen.
- [x] Cooltrainer (F): Located at (13, 3) [Defeated Turn 25004]. Roster: Parasect Lv 43, Dewgong Lv 43, Chansey Lv 43. Reward: 1505 Yen.
- [x] Juggler: Located at (24, 3) [Defeated Turn 24576]. Roster: Mr. Mime Lv 48. Reward: 1680 Yen.

## Verified Collisions & Negative Boundaries (3F)
- Row 11 Rock Wall (cols 6-11): Stepping Down from row 10 at cols 6-10 is blocked by a solid rock wall at row 11.
- Column 8 Rock Divider (rows 6-10): Solid rock wall separating Western Bridge (cols 6-7) from North Central room (cols 9-10).
- Central Boulder (13, 13): Blocked South by rock obstacle at (13, 14); cannot be pushed into row 14 from above.
- Northeast Room East Edge: Columns 29-30 are map boundary rocks; column 28 terminates south at row 5.

## Verified Master Progression Architecture (3F & 2F)
- 2F -> 3F Dual Ladder Connectivity:
  - Ladder A: 2F (27, 7) <-> 3F (23, 7) (Northeast Room / Row 1 Highway / Switch 1 access).
  - Ladder B: 2F (25, 14) <-> 3F (26, 8) (Southeast Chute / Pit Boulder (22, 15) access).
- Master Progression Loop:
  1. From 3F (23, 7), traverse Row 1 Highway to (3, 5) Switch Plate to open barriers.
  2. Take Ladder A back down to 2F at (27, 7).
  3. On 2F, traverse Eastern Corridor (cols 28-29) to (25, 14) [Ladder B].
  4. Climb Ladder B to 3F (26, 8), entering Southeast Chute directly.
  5. Push Pit Boulder (22, 15) into Hole (23, 15).
  6. Jump down Hole (23, 15) to 2F, push fallen boulder onto exit switch, and exit to Indigo Plateau!
