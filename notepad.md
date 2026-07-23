<h1><code>Main</code></h1>

# Pokémon Blue - Adventure Journal & Master Index

## Player & Campaign Setup
- **Player Name:** BLUE
- **Rival Name:** RED
- **Text Speed:** FAST (Configured in Options on Turn 2)
- **Starting Item:** Potion withdrawn from Bedroom PC (Turn 13)

## Key Locations & Coordinates
- **Pallet Town Overworld:**
  - Player's House Exit Door Mat: (3,7) / (3,8) -> spawns at (5,6)
  - Statue / Fence Line: Blocks x=0..9 at y=1
  - North Exit Gap to Route 1: x=10, x=11 (y=1, y=0)
  - Oak Trigger Tile: (10,1) / (10,0)
- **Oak's Lab (Map Coordinates):**
  - Table Row: y=3
  - Left Pokéball (6,3): Charmander
  - Middle Pokéball (7,3): Squirtle
  - Right Pokéball (8,3): Bulbasaur
- **Viridian City Overworld:** South Entrance at (21,35). Pokémon Center Door at (23,25). Pokémart Door at (29,19). Ledge gap at X=19, Y=27 [Verified Turn 243].
- **Pewter City Overworld:**
  - Pokémon Center Door: (13,25) [Verified Turn 495]
  - Pewter Gym Door: (16,17) [Verified Turn 504/521]
  - Pewter Gym Courtyard Corridor: Column 10 (x=10, y=15..18) -> Row 18 (x=10..16) [Verified Turn 521]

## Current Progress & Party
- **Badges:** 1 (Boulder Badge) [Obtained from Brock on Turn 565]
- **Starter Pokémon:** Wartortle (Lv 20) [Level 20 reached on Turn 997]
  - **Nickname:** SHELLSHOCK
  - **Moves:** Tackle, Tail Whip, Bubble, Water Gun
  - **HP:** 64/64 HP (Lv 21) [Fully Healed on Turn 1534 after blackout]
- **Route 1 Geometry:** South-facing ledges at y=27 (gap at x=6..8), y=23 (gap at x=12..15), y=19 (gap at x=4..5), and y=13 (gap at x=15..16) [Verified Turns 189-217].
- **Key Items:** Pokédex (Obtained from Prof. Oak on Turn 265).
- **Inventory:** 5 Poké Balls, TM34 (Bide), TM01 (Mega Punch), Ether, Escape Rope, HP Up, 0 Potions.

<hr>

<h1><code>Locations/Route_3</code></h1>

# Route 3 Map & Tier Connections

## Overview & Elevation Tiers
Route 3 is structured into 3 horizontal elevation tiers:
- **Tier 1 (Top / Rows 4-6):** Main upper highway running East to Mt. Moon. Passes above tree barriers at Column 17 (open Y=4,5) and Column 23 (open Y=4,5).
  - *Trainers:*
    - Bug Catcher #1 at (10,6) [Defeated Turn 674 - Caterpie, Weedle]
    - Youngster at (14,4) [Defeated Turn 685 - Rattata, Ekans]
    - Bug Catcher #2 at (19,5) [Defeated Turn 702 - Lv 9 Weedle, Kakuna, Caterpie]
    - Lass at (20,4) [Defeated Turn 712 - Lv 10 Rattata, Nidoran♂]
    - Bug Catcher #3 at (24,6) [Defeated Turn 735 - Lv 11 Caterpie, Metapod]
- **Tier 2 (Middle / Rows 8-10):** Connected to Pewter City exit at (0,10).
  - *Trainers:* Lass at (16,9) [Defeated Turn 593], Youngster at (22,9).
  - *Boundaries:* Separated from Tier 1 by Row 7 south-facing ledges. Separated from Tier 3 by Row 11 ledges.
- **Tier 3 (Bottom / Rows 12-13):** Lower corridor from X=10 to X=22. Bounded South by Row 14 mountain rock wall, East by Column 23 trees, West by Column 9 rock wall.

## Verified Connections & Passageways
- **Two-Way Slope Passage at (15,11):** [Verified Turn 629] Tile (15,11) is a two-way two-step slope/stairs passage connecting Tier 3 at (15,12) back UP to Tier 2 at (15,10).
- **Row 11 Ledges:** Tiles (10..14, 11) and (16..22, 11) are one-way south-facing ledges going from Tier 2 down to Tier 3.
- **Two-Way Slope Passage at (11,7):** [Verified Turn 637] Tile (11,7) is a two-way slope/stairs passage connecting Tier 2 at (11,8) UP to Tier 1 at (11,6).
- Lass at (33,10) [Defeated Turn 743 - Lv 14 Jigglypuff]
- Column 38 vertical wall blocks Rows 6-12; upper corridor continues East through Rows 4-5 at Column 38.
- **Column 50 Mountain Wall:** [Verified Turn 748] Rock wall blocks Rows 3-9 at X=50; open passage East is at Row 10 (50,10).
- Youngster at (57,11) facing West.
- **Column 66 Eastern Wall:** [Verified Turn 762/773] Column 66 is a solid rock wall blocking Rows 6-14.
- **Tile (48,7) Ledge:** [Verified Turn 780] Tile (48,7) is a solid ledge blocking upward movement from (48,8).
- **Row 7 Ledge at Columns 34-37:** [Verified Turn 1569] Row 7 at Columns 34-37 is a south-facing one-way ledge going DOWN from Tier 1 (Row 6) to Tier 2 (Row 8).
- **Tile (57,7) Ledge:** [Verified Turn 784] Tile (57,7) is a solid south-facing ledge blocking upward movement from (57,8).
- **Route 4 Transition Corridor at (58,8):** [Verified Turn 785] Tile (58,8) is an open upper path bypassing the Row 7 ledge, connecting to (59,8) and the northbound Route 4 highway!
- **Route 4 North Exit at (59,7)-(59,3):** [Verified Turn 787] Column 59 at Row 7 is an open two-way passage leading North through (59,6), (59,5), (59,4), and (59,3) into Route 4!
- **Tree Wall at (9,10)-(9,11):** [Verified Turn 869] Column 9 has trees at Y=10 and Y=11 blocking Row 10/11 path. Row 8 and Row 9 (X=9, Y=8..9) are open to reach X=11.
- **Ledge at (25,14):** [Verified Turn 891] Tile (25,14) is a south-facing ledge that blocks downward movement from Row 13 to Tier 3.
- **Tile (24,7) Ledge:** [Verified Turn 1605] Tile (24,7) is a south-facing one-way ledge blocking Upward movement from (24,8).

<hr>

<h1><code>Locations/Route_4</code></h1>

# Route 4 Map & Points of Interest

## Geometry & Ledges
- **Row 15 Ledge:** [Verified Turn 790] Row 15 has a south-facing ledge blocking upward movement at Columns 6-9. Columns 10-11 provide an open, two-way gap at Row 15 connecting South Route 4 to North Route 4!
- **Row 11 Ledge:** [Verified Turn 791] Row 11 has a south-facing ledge at Columns 6-11. Columns 12-13 provide an open, two-way gap at Row 11 connecting to North Route 4!
- **Mt. Moon Entrance at (18,5):** [Verified Turn 798] Cave entrance doorway located at X=18, Y=5 on Route 4!

<hr>

<h1><code>Locations/Mt_Moon_1F</code></h1>

# Mt. Moon 1F Map & Points of Interest

## Entrance & Entrance Corridor
- **Route 4 Cave Entrance Warp at (14,35):** [Verified Turn 799] Spawns facing North at X=14, Y=35 inside Mt. Moon 1F. Exit warp to Route 4 is directly South at (14,36).
- **Entrance Corridor:** Column 14 extends North from (14,35) into the main 1F cave chamber.
- **Signpost at (15,23):** [Verified Turn 807] Signpost reads: "Beware! ZUBAT is a blood sucker!"
- **Row 21 Wall Boundary:** [Verified Turn 809] Row 21 is a solid purple rock wall blocking Row 21 across Columns 10-19. Open horizontal corridor runs West/East along Row 22.
- **Rock Pillar at (8,22)-(9,23):** [Verified Turn 814] Rock wall blocks Columns 8-9 on Rows 21-23. Passage West is via Row 24 (Columns 10-6).
- Bug Catcher at (7,23) [Defeated Turn 822 - Lv 11 Weedle, Lv 11 Kakuna].
- **Column 6 North Corridor:** [Verified Turn 823] Column 6 is open across Rows 20-24, connecting Row 24 around the rock wall into the western chamber.
- Picked up Item Ball at (2,20) [Turn 825].
- **Decorative / Non-functional Ladder at (25,15):** [Verified Turn 1009] Graphic tile at (25,15) is non-functional and does NOT warp to B1F.
- **Central Rock Wall Boundary (Columns 22-23):** [Verified Turn 1012-1014] Solid purple rock wall spans Columns 22-23 from Row 14 down to Row 25. Open passage from East alcove back West is at Row 26.
- **Western Chamber (Rows 16-20, Columns 2-7):** [Verified Turn 825] Large open chamber in north-western section of 1F.
- **Western Alcove Cleared:** [Verified Turn 827] Rows 16-19 west of Column 8 are solid rock wall. Western alcove (Columns 2-7, Rows 20-24) contains Item Ball (picked up) and Bug Catcher (defeated).
- Lass at (16,23) [Defeated Turn 837 - Lv 14 Clefairy].
- **Eastern Corridor (Row 24, Columns 17-21):** [Verified Turn 839] Open hallway on Row 24 leading East from (16,24) to (21,24).
- **Column 22 Vertical Wall:** [Verified Turn 841] Solid purple rock wall blocks East at Column 22/23 (Rows 20-28). Path turns North along Column 21 at (21,20).
- **Eastern Chamber (Rows 11-28, Columns 24-30):** [Verified Turn 852] Large open eastern hall. Columns 24-30 are open cave floor extending North towards top-right corner.
- Lass at (30,6): [Defeated Turn 943 - Lv 11 Oddish, Lv 11 Bellsprout].
- Rocket Grunt at (15,23) [Defeated Turn 1044 - Lv 11 Sandshrew, Rattata, Zubat].
- **Wall Signpost at (15,23):** [Verified Turn 1639] Signpost on wall reads "Beware! ZUBAT is a blood sucker!" (Not a ladder).
- **Functional Ladder to B1F at (13,27):** [Verified Turn 1672] Ladder graphic tile located at X=13, Y=27 on Mt. Moon 1F warps directly down to B1F.
- Picked up Item Ball at (25,21) [Turn 1332 - Escape Rope].
- **Decorative Ladder at (21,17):** [Verified Turn 1653] Blue ladder graphic at (21,17) is in an isolated alcove (Cols 20-21 bounded by Col 22-23 wall).
- **West Wall at (13,24):** [Verified Turn 1346] Tile (13,24) is blocked by a rock wall.
- **Row 19 Northern Corridor:** [Verified Turn 1364] Row 19 is an open horizontal corridor across Columns 21-29 leading West directly to ladder tile at (21,17).
- **Enclosed Platform at (25,21):** [Verified Turn 1364] Stairs at (25,23) lead up to platform at (25,21), which is bounded North by Row 20 wall. Exit platform down stairs to Row 24.
- **Row 28 Boundary (Columns 25-31):** [Verified Turn 1371] Solid rock wall blocks South at Row 28 across Columns 25-31.

- **Western Highway (Columns 10-11):** [Verified Turn 1383] Columns 12-13 at Rows 19-22 form a rock cliff face. Columns 10-11 are open smooth floor extending North from Row 23 to Row 18.
- **Central Wall Boundary (Row 20-21):** Central and Eastern Row 20-21 are blocked by rock wall.

<hr>

<h1><code>Locations/Mt_Moon_B1F</code></h1>

# Mt. Moon B1F Map & Points of Interest

## Entrance & Corridors
- **1F Ladder Warp at (13,27):** [Verified Turn 1048] Arrived in Mt. Moon B1F via ladder at (15,27) on 1F, spawning at X=13, Y=27 in B1F.
- **South Corridor (Rows 26-27, Columns 10-27):** [Verified Turn 1048-1057] Open horizontal corridor along bottom wall connecting Column 10 to Column 27.
- **East Vertical Passage (Columns 24-27, Rows 15-27):** [Verified Turn 1056-1065] Open vertical passage extending North from South corridor at (26,27) up to Row 15.
- **Decorative Ladder Graphic at (25,15):** [Verified Turn 1063/1404] Graphic tile at (25,15) is decorative/non-functional and does NOT warp.
- **Top Horizontal Corridor (Rows 2-7, Columns 20-37):** [Verified Turn 1066-1081] Large open upper chamber/corridor spanning Rows 2-7 across Columns 20 to 37.
- **East Wall Boundary (Column 38):** [Verified Turn 1070] Solid purple rock wall at Column 38 blocks East across Rows 6-14.
- **Rock Pillars/Boundaries:**
  - Row 8-9 rock wall blocks Rows 8-9 across Columns 20-29 [Verified Turn 1066].
  - Central rock pillar at Columns 32-33 (Rows 12-14) [Verified Turn 1068].
- **Ladder Tile at (17,11):** [Discovered Turn 1085] Ladder graphic tile located at X=17, Y=11 in Mt. Moon B1F.
- **Ladder at (17,11) WARPS:** [Verified Turn 1090] Functional ladder warp at (17,11) in B1F transitions map, spawning at (25,9) in B2F/lower chamber.
- **Reciprocal Ladder Warp at (25,9):** [Verified Turn 1142] Ladder at (25,9) in B1F warps to (17,11) in B2F.
- **East Chamber Wall at Column 26:** [Verified Turn 1148] Column 26 is solid rock wall blocking East at Rows 7-12. The (25,9) ladder chamber is bounded East by Column 26.
- **West Chamber Wall at Column 13:** [Verified Turn 1151] Column 13 is solid rock wall blocking West at Rows 4-12.
- **Row 20 Wall Block:** [Verified Turn 1220] Rows 20-22 are solid rock wall across Columns 10-17.
- **West Wall Columns 8-9:** [Verified Turn 1221] Columns 8-9 are solid rock wall across Rows 18-23.
- **Column 2 Dead End:** [Verified Turn 1227] Column 2 is a dead-end alcove at Row 17.
- **Row 8 Bypass at Col 25:** [Verified Turn 1302] Ladder tile at (25,9) on B1F is directly below (25,8). When navigating East along Row 8 to Col 26, do not press Down until reaching (26,8) to avoid accidental warp at (25,9).
- **East Passage Connection:** Columns 34-37 are open cavern floor across Rows 7-27. Columns 32-33 contain a continuous rock wall/pillar spanning Rows 12-27.
- **Row 10 Central Bypass:** [Verified Turn 1318] Row 10 is open floor across Cols 26-34, providing the horizontal bypass across the Central Rock Pillar (Cols 32-33).
- **Item Ball at (36,23):** [Verified Turn 1313/1324] Item Ball at (36,23) contained Escape Rope.

<hr>

<h1><code>Locations/Mt_Moon_B2F</code></h1>

# Mt. Moon B2F Map & Points of Interest

## Geometry & Points of Interest
- **Spawn Ladder at (25,9):** [Verified Turn 1090] Arrived from B1F ladder at (17,11), spawning at X=25, Y=9 in B2F.
- **Corridor Chamber (Rows 8-11, Columns 17-25):** [Verified Turn 1093] Open floor chamber connecting (25,9) West to (17,11).
- **Ladder Tile at (17,11):** [Discovered Turn 1093] Ladder graphic tile located at X=17, Y=11 in Mt. Moon B2F.
- **B2F Ladder Warp at (17,11) -> (25,9):** [Verified Turn 1095] Ladder at (17,11) warps to main B2F chamber, spawning at X=25, Y=9.
- Picked up Item Ball at (29,5) [Turn 1115 - TM01 Mega Punch].
- **Spotted NPC at (29,11):** [Spotted Turn 1095] Trainer/Grunt sprite at X=29, Y=11 in B2F.
- **Rocket Grunt at (29,10):** [Defeated Turn 1106 - Lv 12 Zubat, Lv 12 Ekans].
- **Upper Platform Dead End:** [Verified Turn 1154] Upper platform spans Columns 27-30 at Rows 5-6, bounded North by Row 4 wall, West by Col 26 wall, East by Col 31 wall. Only contained TM01 at (29,5).
- **East Wall Boundary at Column 36:** [Verified Turn 1158] Column 36 is a solid rock wall blocking East across all rows. The entire B2F section (Columns 14-35) is an isolated side-room containing TM01 Mega Punch and Rocket Grunt.
- **Row 12 Solid Wall Face:** [Verified Turn 1291] Row 12 is a solid rock wall face across Columns 22-31 blocking downward movement. Open South Passage is at Columns 32-33 leading to stairs at (32,15)-(33,15) into the lower B2F cavern!
- **West Wall Boundary at Column 23:** [Verified Turn 1182] Column 23 is a solid rock wall blocking West across Rows 5-13.
- **Enclosed B2F Side-Room:** [Verified Turn 1195] B2F room (Cols 24-35, Rows 5-11) is fully enclosed by Col 23 West wall, Col 36 East wall, Row 4 North wall, and Row 12 South wall.
- **South Passage at Columns 32-33:** [Verified Turn 1193] Columns 32-33 provide an open floor passage on Row 12 leading South directly to stairs at (32,15)-(33,15) into the main lower cavern.
- **B2F Connector vs Main Cavern Discovered:** [Verified Turn 1250] Ladder (17,11) in B2F Connector Room warps to B2F Main Cavern at (25,9), where Column 26+ is open floor leading East to South Passage at (32,12).
- **B2F South Passage Discovered:** [Verified Turn 1504] Column 17 is a wide-open vertical corridor extending South across Rows 12-19+ (Columns 13-17 floor).
- **Row 20 Boundary:** [Verified Turn 1509] Row 20 is a solid rock wall face across Columns 13-18. B2F South passage turns West along Row 19 (Cols 13-17).

<hr>