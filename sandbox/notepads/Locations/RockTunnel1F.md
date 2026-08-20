# Rock Tunnel 1F - Points of Interest & Topology

## Standardized Ladder Connectivity Matrix
- **North Entrance**: Located at (15, 3). Connects to Route 10 (North).
- **Ladder 1 Arrival**: 1F (37, 3) is the arrival tile from B1F (33, 25) [NE 1F <- SE B1F]. Note: Stepping on (37, 3) on 1F does not warp down (tested Turn 7968).
- **Ladder 2**: 1F (27, 3) <-> B1F (5, 3) [North-Central 1F <-> North-West B1F]. Connects north-central 1F to NW B1F.
- **Ladder 3**: 1F (23, 11) <-> B1F (17, 11) [Central 1F <-> Central B1F]. Connects central 1F to central B1F.
- **Ladder 4**: 1F (3, 3) <-> B1F (37, 17) [North-West 1F <-> East-Central B1F]. Connects B1F eastern exit passage to 1F final exit sector.
- **1F South Exit**: Western / Column 14 Corridor south to Route 10 South and Lavender Town!

## Verified Corridors & Collision Bounds
1. North Entrance Corridor (rows 2-7, cols 15-23):
   - East-west passage running from entrance (15, 3) east to column 23.
   - Solid vertical rock wall at cols 12-13 divides central and western sectors.
2. Western Corridor (cols 2-5, rows 2-33):
   - Passage south from Ladder 4 at (3, 3) through rows 2-21.
   - Western pocket at (2..5, 17..21) is bounded to the west by cols 0-1 and south by rows 22-23 rock wall.
   - Rows 10-13 form a wide open 4-tile high passage connecting Western Corridor (cols 2-5) to Central Basin (cols 8-11).
3. Central Thoroughfares & Basin (cols 8-17, rows 9-28):
   - Vertical and horizontal corridors connecting central ladder (23, 11) and north entrance (15, 3).
   - Rows 14-17 form an 8-tile wide open thoroughfare across cols 8-15 connecting Central Basin to Column 14 Exit Corridor.
   - Rows 24-27 form a 10-tile wide open basin across cols 2-11.
   - Solid rock wall at row 28 across cols 2-13.
4. Central-East Corridors (cols 14-19, rows 13-27):
   - Upper corridor (rows 14-21) and lower corridor (rows 24-27) are separated by a solid rock barrier at rows 22-23 across cols 12-19.
   - Connected to Central Basin via row 14-17 open thoroughfare.
   - Lower corridor (rows 24-27) contains open floor at (14..16, 28) extending south.
5. Eastern Sector (cols 26-37, rows 1-13):
   - Separated from western/central sector by impassable rock walls at cols 12-13 and cols 24-25.
   - Ladder 1 Arrival located at (37, 3) from B1F (33, 25) [1-way arrival on 1F].
   - Ladder 2 located at (27, 3) connects to B1F (5, 3).

## Verified Trainers & Encounters
- PokéManiac Ashton: Located at (23, 8) facing North [Defeated Turn 3145]. Team: Cubone Lv 23, Slowpoke Lv 23. Reward: ¥1150.
- Hiker #1: Located at (5, 15) [Defeated Turn 3654]. Team: Onix Lv 20, Geodude Lv 20. Reward: ¥700.
- Jr. Trainer Female #1: Located at (10, 15) [Defeated Turn 3879]. Team: Jigglypuff Lv 21, Pidgey Lv 21, Meowth Lv 21. Reward: ¥420.
- Hiker #2: Located at (6, 10) facing Down [Defeated Turn 4163]. Team: Geodude Lv 21, Geodude Lv 21, Graveler Lv 21. Reward: ¥735.
- PokéManiac #3: Located at (3, 8) in the Western Corridor [Defeated Turn 5682]. Team: Slowpoke Lv 20, Slowpoke Lv 20, Slowpoke Lv 20. Reward: ¥1000.
6. Central Rock Barrier (rows 8-9, cols 19-25):
   - Solid horizontal rock barrier across rows 8-9 (cols 19-25) separates North Corridor (rows 2-7) from Central Corridor (rows 10-13) on the east side. Access between north and south on 1F is via the western corridor (cols 14-17). [Verified Turn 8446]
7. Eastern Sector Hall (rows 10-19, cols 26-37):
   - Rows 10-13 form an open horizontal highway connecting cols 26-37.
   - Rock barrier at rows 14-15 spans cols 23-31, with clear eastern bypass across cols 32-37.
   - Rows 16-19 form a massive 10-tile wide open hall across cols 28-37 extending south. [Verified Turn 8469]
8. Southern Avenue & Rock Pillar (rows 19-27, cols 20-29):
   - Columns 20-25 form a wide open 6-tile highway across rows 19-27 heading south.
   - Columns 26-27 form a vertical rock pillar across rows 20-27 dividing the western avenue (cols 20-25) from the eastern hall (cols 28-37).
   - Both avenues extend south past row 27. [Verified Turn 8475]
9. South Exit Corridor Analysis:
   - Row 28 forms a continuous solid rock barrier across cols 2-27.
   - The only open path extending south past row 28 on 1F is the Eastern Sector Hall (cols 28-37, rows 28-35+). [Verified Turn 8484]
10. Western-Eastern Divider (rows 20-27, cols 26-27):
    - Solid 2-tile wide vertical rock wall across cols 26-27 continuously separates Western Avenue (cols 20-25) from Eastern Hall (cols 28-37) across all rows 20 to 27. [Empirically Verified Turn 8498]