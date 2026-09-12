# Cerulean Cave (Unknown Dungeon) 1F - Layout & Topology

## Overview
- Ground floor of Cerulean Cave (Unknown Dungeon).
- Connects to Cerulean City NW waterway pool at (24, 17) / (4, 11 outside).
- Features an extensive northern and central water canal system, elevated central bridge, and multiple ladders ascending to 2F.

## Verified Ladders Matrix (1F <-> 2F)
1. **Ladder B**: Located at (23, 7) <-> 2F (22, 6) [SE elevated terrace].
2. **Ladder C**: Located at (18, 9) <-> 2F (19, 7) [Central sector, connects west on 2F to NW Sector & Ladder A].
3. **Ladder D**: Located at (27, 1) <-> 2F (29, 1) [NE terrace, accessed via water canal & ramp (23, 3)].
4. **Ladder E**: Located at (7, 1) <-> 2F (9, 1) [NW terrace, elevated ledge].

## Verified Ramps (1F)
- **Central South Ramp (21, 11)**: Connects ground floor (21, 14..12) south to elevated bridge platform (21, 10).
- **East Water Ramp (25, 9)**: 3-horizontal-line ramp connecting central bridge (25, 8) down to eastern water canal at (25, 10).
- **North Terrace Ramp (23, 3)**: 3-horizontal-line ramp connecting northern water canal (23, 4) up to NE terrace (23, 2) leading to Ladder D at (27, 1).
- **Central Terrace Ramp (11, 13)**: 3-horizontal-line ramp connecting southern water canal (11, 14) up to central terrace (11, 12).
- **North Pocket Ramp (15, 3)**: Connects northern canal (15, 4) up to northern pocket (11..16, 0..2).

## Verified Boundaries & Collision Constraints (1F)
- **Western Cliff Barrier (Column 7)**: Solid rock cliff edge runs along column 7 across rows 6–14; stepping Left from water canal (cols 8–10) into column 7 is blocked.
- **Row 14 East Barrier**: (12..14, 14) are solid rock walls blocking direct eastward water navigation from (11, 14).
- **Central Terrace Highway**: Columns 11–13 (rows 8–12) and Column 16 (rows 9–12) form open cave floor connecting ramp (11, 13) at (11, 12) via (16, 12) -> (16, 9) -> (18, 9) directly to Ladder C.
## Verified Empirical Barriers (Turn 48054)
- (19, 9): Solid rock wall immediately east of Ladder C (18, 9) on 1F blocks direct eastward movement on Row 9. To reach the bridge/ladders from Ladder C, navigate west through Column 16 to Row 12 at (16..21, 12) and ascend ramp (21, 11).