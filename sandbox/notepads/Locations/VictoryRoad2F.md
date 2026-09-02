# Victory Road 2F - Layout & Notes

## General Information
- Ladder down to 1F: Located at (0, 8) [Arrived Turn 22565]

## Baseline Floor Geometry & Objects
- Ladder up to 3F (Northwest): Located at (1, 1) in northwest corner of upper corridor [Observed Turn 22702]
- Ladder up to 3F (Southeast): Located at (25, 14) in southeast clearing [Observed Turn 22840]
- Blackbelt: Located at (4, 2) facing South [Observed Turn 22692].
- Boulder 1: Default initial location at (5, 5) [Observed Turn 22565].
- Boulder 2: Default initial location at (4, 14) on Lower Highway [Observed Turn 22705].
- Shutter 1: Located at (5, 10) (Opened by Switch Plate (1, 16)) [Verified Turn 22814].
- Switch Plate 1: Located at (1, 16) in southwest corner [Verified Turn 22814].
- Switch Plate (Upper): Located at (9, 11) (circular red/yellow plate) [Observed Turn 22586].
- Moltres: Located at (11, 5) on elevated plateau [Observed Turn 22580].
- Shutter 2: Located at (15, 15) in eastern sector.
- Shutter 3: Located at (21, 15) in eastern sector.
- Item Ball: Located at (18, 9) in eastern sector.
- Trainer: Located at (19, 8) facing Down/Left.
- Boundary / Elevation Step: (23, 14) separates lower row 14 from ladder platform at (25, 14).

## Defeated Trainers (2F)
- [x] Blackbelt: (9, 9) [Defeated Turn 22819]. Roster: Machoke Lv 43, Machop Lv 43, Machoke Lv 43. Reward: �1075.
- [x] Juggler: (21, 13) [Defeated Turn 22845]. Roster: Drowzee Lv 41, Hypno Lv 41, Kadabra Lv 41 x2. Reward: �1435.

## Terrace & Elevation Topology
- Row 7/8 Boundary: An impassable cliff wall spanning columns 4-12. Stepping South from row 7 to row 8 is strictly blocked.
- Terrace (3..7, 5..7) Exits:
  - West Corridor: (3, 7) -> (3, 8..11) connects to the lower western highway and Shutter 1 (5, 10).
  - North Gap: (5, 4) connects to row 3.

## Verified Northwest Sector Topology & Boulder 1
- Upper Corridor: Rows 1-3 (cols 1-6) contain:
  - Blackbelt trainer at (4, 2)
  - Ladder to 3F (NW) at (1, 1)
  - Eastward extension towards Moltres and eastern 2F plateau
## Verified Corridor Traversal & Elevation Topology
- (4..12, 10) is a solid rock wall; Shutter 1 at (5, 10) is the sole opening connecting the central sector (rows 8-9) to lower western highway (row 11).
- (9, 7) is a solid impassable cliff obstacle; row 8 does NOT connect north to row 2 via column 9.
- (23, 14) is an empirically verified one-way ledge facing west (Turn 23433: stepping East from (22, 14) is blocked); direct entry from lower floor (22, 14) onto ladder platform (24..26, 12..14) is impossible. Access to the SE ladder (25, 14) requires traversing the Northern Upper Corridor (rows 1-3) from the west and walking South down the platform (cols 24-26).
- Northern Upper Corridor Access: From the NW terrace (3..7, 5..7), stand at (6, 5) and push Boulder 1 West from (5, 5) to (4, 5). This opens the (5, 4) -> (5, 3) vertical bottleneck onto row 3, allowing unrestricted eastward traversal across rows 1-3 to the Eastern Platform.
- Column 9 & 10 Corridor: Columns 9 and 10 form a completely open, unobstructed 2-tile wide vertical highway connecting the Central Corridor at (9..10, 8) directly north to the Northern Upper Corridor at (9..10, 2..3), bypassing the terrace/Boulder 1 bottleneck entirely.
- Primary 2F Progression Route: Solve Boulder 2 puzzle on Lower Highway to open Shutter 1 at (5, 10), walk through Shutter 1 into Central Corridor, ascend Column 9 corridor to Northern Upper Corridor (row 2-3), and traverse East to SE 3F ladder at (25, 14) (or West to NW 3F ladder at (1, 1)).