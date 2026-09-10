# Cerulean Cave (Unknown Dungeon) 1F - Layout & Notes

## Entrance & Basin Topology
- South Entrance/Exit Warp: (24, 17) / (25, 17) [Connects to Cerulean City NW water pool at (4, 11)].
- Entrance Basin (rows 12-16, cols 21-25): Walkable floor enclosed by:
  - North: Ledge at (21, 11) jumping South to (21, 12); solid rocks at (22..23, 11) and (23..25, 12); water canal at (24..25, 10..11).
  - South: Wall barrier at (21..23, 16); open passage via cols 24-25 to entrance warp (24..25, 17).
  - West: Solid rock spine at (20, 6..15) separating East basin from West platform. Tile (20, 12) is solid rock.
  - East: Solid rock wall at col 26.
- Upper Landing (rows 6-9, cols 21-25):
  - Ladder B at (23, 7) ascends to 2F (22, 6).
  - North Shoreline at Row 6 (cols 21-25): Open northern boundary facing Row 5 water canal (cols 17-25, row 5).
  - South Ledge at (21, 11): One-way jump South into lower entrance basin.

## Ladder Connectivity Matrix (1F <-> 2F & B1F)
- Ladder B: (23, 7) <-> 2F (22, 6) [Ascends to 2F East landing].
- Ladder C: (18, 9) <-> 2F (19, 7) [Ascends directly to 2F Central Hub / North Highway base].
- Ladder E: (7, 1) <-> 2F (9, 1) [Ascends to 2F NW Row 1 North Highway].
- Ladder D: (27, 1) <-> 2F (29, 1) [Isolated NE landing].
- Ladder A2: 1F Western Ridge landing <-> 2F (3, 11) [SW Sector target ladder down from 2F to 1F Western Ridge].
- Ladder to B1F: Located on 1F Western Ridge adjacent to Ladder A2 landing; leads directly down to Mewtwo's lair on B1F.

## Verified Impassable Collision Barriers (1F)
- (20, 6) is solid rock blocking direct westward passage from (21, 6) to (18, 6).
- (20, 13) is solid rock blocking westward passage at row 13. Row 14 ((21, 14) -> (20, 14)) connects the eastern basin to the western corridor.
- Column 21 Passage: (21, 11) is a bidirectional ramp/passage connecting the lower entrance basin (21, 12) directly to the upper landing (21, 7..10).
- Wall at (21..23, 16) blocks direct downward movement from (21..23, 15) to (21..23, 16).
- Shoreline/cliff at (24..25, 13) and (21, 5) blocks northward surfing/walking.
- Columns 19-20 rock spine at rows 6-12 separates East and West platforms on 1F.
## Verified Waterway Topology & Canal Navigation (Turns 42200-42211)
- **Canal Boarding Point**: From the Upper Landing at (25, 8), stepping South onto the ledge at (25, 9) allows using SURF directly into the water canal at (25, 10).
- **Eastern Water Canal**: Continuous open water across cols 25-29 at rows 10-11. Connects north via cols 28-29 (rows 6-10) directly to the Northern Canal junction at (28, 5).
- **Northern Water Highway**: Continuous 2-tile wide water channel spanning rows 4-5 from (28, 4..5) westward to (14, 4..5).
- **Central Bypass (Row 6-7 Channel)**: Rock island at (10..13, 4..5) blocks direct row 4-5 passage. Water bypasses south via rows 6-7 (cols 10-15) directly into the western water channel at (8, 6).
- **Western Water Channel**: Open water running south along cols 8-9 (rows 6-10) bordering the Western Ridge (cols 4-6, rows 6-10) and Central Platform (cols 11-13, rows 8-10).
- **NE Isolated Landing**: Ladder D at (27, 1) is situated on the elevated northeast landing overlooking the canal at row 3.
- **Central Platform Ramp & Ladder C Corridor (Turns 42218-42220)**:
  - From the western water canal at (11, 14), stepping Up onto (11, 13) ascends the ramp onto the Central Platform at (11, 12).
  - Central Platform spans cols 11-13, rows 9-12.
  - From (11, 9), Row 9 runs continuously east across cols 11..18 directly to Ladder C at (18, 9), providing ground access to Ladder C to ascend to 2F (19, 7).
- **NW Upper Platform (Verified Turn 42262)**:
  - Spans cols 5-16, rows 0-2. Walkable cave floor.
  - Ladder E at (7, 1) ascends to 2F (9, 1).
  - South Ledge at (15, 3): One-way jump South from (15, 2) over ledge into the Northern Water Highway at (15, 4).
- **Western Cliff Barrier (Verified Turn 42273)**:
  - Column 7 (rows 10-16) is a continuous solid cliff barrier separating the water channel (cols 8-11) from the Western Ridge (cols 4-6). There is no shoreline access from (8, 14..15) into (7, 14..15).
- **Central Platform South Ramp & Row 17 Highway (Verified Turn 42376)**:
  - From Ladder C at (18, 9), walking south down the platform to (17, 14) leads to the South Ramp at (17, 15).
  - Descending ramp (17, 15) steps down onto (17, 16), and stepping Down to Row 17 (15, 17) enters the continuous southern ground highway spanning west across (1..15, 17) towards the Western Ridge (cols 1-6).
- **Western Ridge South Ramp & Access (Verified Turn 42377)**:
  - From Row 17 at (2, 17), walking North through (2, 16..15) and (1, 14) leads to the Western Ridge Ramp at (1, 13).
  - Ascending ramp (1, 13) steps up onto (1, 12) on the elevated Western Ridge (cols 0-6, rows 0-12), providing direct ground access to the B1F ladder and Mewtwo's lair!
- **Western Ridge Ladder Confirmed (Turn 42380)**:
  - Ladder located at (3, 11) on the elevated Western Ridge.
  - Open continuous ridge floor extends north across cols 1..6, rows 1..12.
- **Western Ridge Wall & North Exploration (Turn 42382)**:
  - (0, 8) and (1..6, 7) are solid purple rock walls blocking direct westward/northward access from (1, 8).
  - Open floor extends east along Row 8 across cols 1..6. Scouting east towards col 6+ to find passage around Row 7 rock wall.
- **Western Ridge Dual Ladders & B1F Topology (Verified Turn 42383)**:
  - Ladder A2 at (3, 11): Connects to 2F SW Sector (TM14 room).
  - Ladder to B1F at (0, 6): Connects directly down to Cerulean Cave B1F (Mewtwo's lair).
  - Passage from South Western Ridge to North Western Ridge: From (5, 8), head east along Row 8 to (7, 8), then north along Column 7 around the rock spine to reach Row 6 and Ladder (0, 6).
- **Western Ridge South Sector Verified (Turn 42387)**:
  - (3, 11) is standard cave floor on 1F (no ladder warp). The South Western Ridge (cols 1-6, rows 8-12) is an isolated elevated plateau accessed via South Ramp at (1, 13).
  - To access North Western Ridge (cols 0-6, rows 0-6) and the B1F ladder: Route via Ladder C (18, 9) -> 2F Central Hub -> 2F North Highway -> Ladder E (9, 1) -> 1F NW Landing (7, 1) -> Walk West along Row 1 (6, 1 -> 1, 1) -> South to Row 6.