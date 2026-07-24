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
- **Starter Pokémon:** Wartortle (Lv 26) [Level 26 reached on Turn 2518]
  - **Nickname:** SHELLSHOCK
  - **Moves:** Tackle, Bite, Bubble, Water Gun
  - **HP:** Fully Healed at Pewter Center on Turn 2658
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
- **Route 3 One-Way Highway:** [Verified Turn 2700] South-facing ledges on Row 7 and Row 14 prevent returning West to Pewter City once you hop down. Travel East to Mt. Moon is mandatory.

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
- **Row 26 Central Rock Wall Face (Cols 16-23):** [Verified Turn 3641] Solid impassable rock wall face spans Columns 16 through 23 across Row 26. Passage Down from Row 25 to Row 28 is via Column 15 gap on the West or Column 24 gap on the East.
- **Western Chamber (Rows 16-20, Columns 2-7):** [Verified Turn 825] Large open chamber in north-western section of 1F.
- **Western Alcove Cleared:** [Verified Turn 827] Rows 16-19 west of Column 8 are solid rock wall. Western alcove (Columns 2-7, Rows 20-24) contains Item Ball (picked up) and Bug Catcher (defeated).
- Lass at (16,23) [Defeated Turn 837 - Lv 14 Clefairy].
- **Eastern Corridor (Row 24, Columns 17-21):** [Verified Turn 839] Open hallway on Row 24 leading East from (16,24) to (21,24).
- **Column 22 Vertical Wall:** [Verified Turn 841] Solid purple rock wall blocks East at Column 22/23 (Rows 20-28). Path turns North along Column 21 at (21,20).
- **Eastern Chamber (Rows 11-28, Columns 24-30):** [Verified Turn 852] Large open eastern hall. Columns 24-30 are open cave floor extending North towards top-right corner.
- Lass at (30,6): [Defeated Turn 943 - Lv 11 Oddish, Lv 11 Bellsprout].
- Rocket Grunt at (15,23) [Defeated Turn 1044 - Lv 11 Sandshrew, Rattata, Zubat].

- Picked up Item Ball at (25,21) [Turn 1332 - Escape Rope].

- **Row 19 Central Block:** [Updated Turn 1711] Columns 22-23 form a solid rock wall across Rows 14-25, separating the Eastern Chamber (Cols 24-27) from Central Alcove (Cols 20-21).
- **Enclosed Platform at (25,21):** [Verified Turn 1364] Stairs at (25,23) lead up to platform at (25,21), which is bounded North by Row 20 wall. Exit platform down stairs to Row 24.
- **Row 28 Boundary (Columns 25-31):** [Verified Turn 1371] Solid rock wall blocks South at Row 28 across Columns 25-31.

- **Western Highway (Columns 10-11):** [Verified Turn 1383] Columns 12-13 at Rows 19-22 form a rock cliff face. Columns 10-11 are open smooth floor extending North from Row 23 to Row 18.
- **Central Wall Boundary (Row 20-21):** Central and Eastern Row 20-21 are blocked by rock wall.
- **Row 25 Rock Wall (Cols 10-23):** [Verified Turn 1858] Solid rock wall blocks Row 25 across Columns 10 through 23, enclosing the bottom-left corridor (Cols 10-18, Rows 26-27). Passage North opens at Column 24 (Cols 24-27).
- **East Wall at Column 28 (Rows 13-20):** [Verified Turn 3449] Solid purple rock wall face at Column 28 blocks East from Column 27 across Rows 13-20.
- **Eastern Upper Chamber (Rows 11-15, Cols 21-30):** [Verified Turn 1876] Large wide-open cavern spanning Rows 11-15 across Columns 21 to 30. No wall at Row 13 or Col 28 on Rows 11-15; smooth purple floor extends North past Row 11.

- **Rock Wall Barrier (Cols 18-19, Rows 8-23):** [Verified Turns 2229-2249] Solid rock wall spans Columns 18-19 across Rows 8 through 23, blocking Westward passage between Column 20/21 and Column 17. Row 24 connects Column 20 to Column 17.
- **Row 20-28 Central Wall (Cols 22-23):** [Verified Turn 2276] Solid purple rock wall face spans Columns 22-23 across Rows 20 through 28, blocking Westward passage from Column 24 to Column 21 along Row 24.
- **Row 13 Wall Boundary:** [Verified Turn 2376] Rock wall at Row 13 spans Columns 24-27 only. Columns 28-30 are open floor connecting Row 15 to Row 11.
- **Eastern Chamber (Cols 24-27, Rows 14-18):** [Verified Turn 2549] Enclosed side room. Exit is South at (24,26).
- **Row 8-9 Rock Wall (Cols 18-29):** [Verified Turn 2410] Solid rock wall face blocks Rows 8-9 across Columns 18 through 29. Column 30+ is open floor connecting Row 10 North to Row 7 upper corridor.
- **CRITICAL WARP PAIRS:**
  - 1F (13,27) <-> B1F (15,27) [Main Path to B1F & B2F Main Cavern]
  - 1F (17,11) <-> B2F (25,9) [Side Room Loop with TM01 Mega Punch]
- **Column 17 Wall at (17,21):** [Verified Turn 2529] Solid rock wall face at (17,21) blocks Northward movement along Column 17.
- **Row 21 Wall at Col 10:** [Verified Turn 2533] Solid rock wall face at (10,21) blocks Northward movement along Column 10. Western corridor route to Western Chamber is via Row 24 to Column 6.
- **Elevated Platform (24,21):** [Verified Turn 2606] Elevated platform at (24,21) is enclosed by solid rock walls along Row 20 to the North, East, and West (dead end).
- **Row 26 Rock Wall at Col 16-19:** [Verified Turn 2727] Solid rock wall face blocks Row 26 at Col 16-19. Row 24 is the open corridor connecting Col 10 to Col 20.
- **Row 24 Rock Wall at Col 22-23:** [Verified Turn 2729] Solid rock wall face blocks Row 24 at Col 22-23. Row 26 (Cols 20-25) is the open corridor connecting Col 20 East to Col 24.

- **Row 17 Rock Wall Collision at Cols 22-23:** [Verified Turn 2743] Solid purple rock wall blocks Row 17 at Cols 22-23 on 1F, enclosing Eastern Chamber. Exit is South at (24,26).
- **(24,28) Wall Boundary:** [Verified Turn 3024] Solid rock wall face blocks South at Row 28 across Columns 20-29 on 1F.
- **(9,19) Wall Boundary:** [Verified Turn 3059] Solid rock wall face blocks Westward movement at Column 9 on Row 19.
- **Row 19 Rock Wall Boundary (Cols 20-23):** [Verified Turn 3328] Solid rock wall face along Row 19 across Columns 20-23 on 1F.
- **Item Ball at (25,14):** [Verified Turn 3294] Item Ball located at (25,14) on 1F (picked up on Turn 3294).

- **Mountain Wall Barrier Across Rows 20-21 (Cols 10-23):** [Verified Turn 3535] Solid purple rock wall face forms an impassable continuous barrier across Rows 20-21 from Column 10 all the way through Column 23. Northern highway on 1F is via Column 28 (Cols 28-30).
- **Decorative Ladder at (25,15):** [Verified Turn 3686] Tile (25,15) displays ladder graphic but is decorative/non-functional. Functional ladder is at (17,11).

<hr>

<h1><code>Locations/Mt_Moon_B1F</code></h1>

# Mt. Moon B1F Map & Points of Interest

## Entrance & Corridors
- **Functional Ladder at (15,27):** [Verified Turn 3188] Stepping onto ladder at (15,27) on B1F warps up to Mt. Moon 1F at (13,27).
- **South Corridor (Rows 26-27, Columns 10-27):** [Verified Turn 1690] Column 10 dead-ends North at Row 25 (rock wall at 10,25). South Corridor connects Columns 10-27 along Rows 26-27.
- **Column 30 West Wall Face (Rows 20-27):** [Verified Turn 1682] Column 30 has a solid west cliff face blocking eastward movement from Col 29 across Rows 20-27.
- **Row 28 South Ledge at Col 29:** [Verified Turn 1683] Row 28 at (29,28) is a solid cliff face blocking Southward movement from (29,27).
- **Eastern Highway Passage (Cols 34-37, Rows 7-27):** [Disproved Turn 1767] Column 28 is a solid rock wall blocking Row 27 South Corridor from connecting directly to Columns 34-37. Eastern Highway is isolated from South Corridor.
- **Top Horizontal Corridor (Rows 2-7, Columns 20-37):** [Verified Turn 1066-1081] Large open upper chamber/corridor spanning Rows 2-7 across Columns 20 to 37.
- **East Wall Boundary (Column 28 at Rows 12-20):** [Verified Turn 1695] Solid purple rock wall at Column 28 bounds the Eastern Chamber on the East.
- **Eastern Chamber Summary (Cols 24-27, Rows 14-25):** [Verified Turn 1715] Enclosed dead-end room with decorative ladder at (25,15). Only exit is South at (24,26) to South Corridor.
- **Rock Pillars/Boundaries:**
  - Row 8-9 rock wall blocks Rows 8-9 across Columns 20-29 [Verified Turn 1066].
  - Central rock pillar at Columns 32-33 (Rows 12-14) [Verified Turn 1068].
- **Reciprocal Ladder Warp at (25,9):** [Verified Turn 1142] Ladder at (25,9) in B1F warps to (17,11) in B2F.
- **East Chamber Wall at Column 26:** [Verified Turn 1148] Column 26 is solid rock wall blocking East at Rows 7-12. The (25,9) ladder chamber is bounded East by Column 26.
- **West Chamber Wall at Column 13:** [Verified Turn 1151] Column 13 is solid rock wall blocking West at Rows 4-12.
- **Row 20 Wall Block:** [Verified Turn 1220] Rows 20-22 are solid rock wall across Columns 10-17.
- **West Wall Columns 8-9:** [Verified Turn 1221] Columns 8-9 are solid rock wall across Rows 18-23.
- **Column 2 Dead End:** [Verified Turn 1227] Column 2 is a dead-end alcove at Row 17.
- **Row 8 Bypass at Col 25:** [Verified Turn 1302] Ladder tile at (25,9) on B1F is directly below (25,8).
- **Row 10 Central Bypass:** [Verified Turn 1318] Row 10 is open floor across Cols 26-34, providing the horizontal bypass across the Central Rock Pillar (Cols 32-33).
- **Item Ball at (36,23):** [Verified Turn 1313/1324] Item Ball at (36,23) contained Escape Rope.

- **Row 20 North Wall Block (Cols 20-29):** [Verified Turn 2305] Solid purple rock wall face blocks Northward movement at Row 20 across Columns 20 through 29 on B1F. Column 14/15 provides the open vertical highway North connecting South Corridor (Row 26) to Upper Cavern (Rows 18-21).
- **Row 20-21 Rock Wall (Cols 14-20):** [Verified Turn 2316/3389] Solid purple rock wall face blocks North at Rows 20-21 across Columns 14-20. Columns 10-11 on the far West side provide the open vertical highway North connecting South Corridor (Row 26) to Top Corridor (Rows 2-7).
- **Row 8 Solid Rock Wall (Cols 20-29):** [Verified Turn 2452] Solid blue rock wall face blocks Southward movement at Row 8 across Columns 20 through 29. Column 30 is the open vertical corridor connecting Row 7 to Row 10.
- **Column 12-13 Rock Pillar (Rows 23-28):** [Verified Turn 2488] Columns 12-13 are a solid rock pillar face across Rows 23 through 28, blocking Westward movement along South Corridor at Row 27.
- **Rocket Grunt at (15,22):** [Verified Turn 2501] Rocket Grunt located at (15,22) in Upper Cavern section of B1F.
- **Decorative Ladder at (25,15):** [Verified Turn 2643] Tile (25,15) in B1F Eastern Chamber displays a ladder graphic but is decorative/non-functional (stepping on it triggers no warp).
- **Central Cliff Barrier at Cols 30-31:** [Verified Turn 2569] Solid rock cliff face blocks Row 26 Eastward at Column 30 on B1F.
- **Eastern Highway at Cols 28-29:** [Verified Turn 2508] Columns 28-29 form a wide-open vertical corridor extending North from Row 26 up through Row 22+.
- **Row 22 Wall Collision at (27,22):** [Verified Turn 2510] Solid rock wall face at (27,22) blocks Westward movement along Row 22.
- **South Corridor Northern Boundary:** [Verified Turn 2636] Column 10 dead-ends North at (10,25) into a solid purple rock wall face. Rows 20-25 rock walls block direct Northward passage across Columns 10-23 from South Corridor. Northern exit from South Corridor is at Columns 24-25 (Rows 22-25 open floor).
- **B1F South Corridor Isolation:** [Verified Turn 2579] B1F South Corridor (Cols 14-29, Rows 24-27) is enclosed by Row 20-25 rock walls and Col 12-13 / Col 30-31 pillars. Only exit is ladder at (15,27) up to 1F (13,27).
- **Row 21 Wall Collision at (22,21):** [Verified Turn 2578] Solid rock wall face at (22,21) blocks Westward movement along Row 21.
- **B1F Map Boundary West at Col 10:** [Verified Turn 2594] Column 10 is the westmost edge of Mt. Moon B1F. Columns 2-9 do not exist on B1F.
- **South Corridor True Coordinates:** [Verified Turn 2646] Rows 28-30 across Columns 20-25 form the open floor South Corridor extending West under the Row 24-27 rock wall face. Row 26/27 at Cols 20-23 is solid rock wall face.
- **Row 25 Solid Rock Wall Face (Cols 10-23):** [Verified Turn 2758] Solid purple rock wall face blocks Row 25 across Columns 10 through 23 on B1F. Column 15 does NOT connect North past Row 25. Exit North from South Corridor is at Columns 24-25.
- **East Wall Boundary at Col 28 (Rows 17-25):** [Verified Turn 2768] Solid purple rock wall face at Column 28 blocks East from Column 27 across Rows 17-25. Wide Eastern Highway is Columns 24-27 extending North.
- **(25,12) Wall Boundary:** [Verified Turn 2973] Tile (25,12) is an impassable wall face. Column 25 dead-ends South at Row 11.
- **Solid Rock Wall Face at (13,22):** [Verified Turn 3118] Tile (13,22) is solid rock wall face blocking Westward movement from Column 14.
- **Solid Rock Wall Face at (13,26):** [Verified Turn 3101] Tile (13,26) is solid rock wall face blocking Westward movement along Row 26.
- **Solid Rock Wall Face at (26,23) & (27,22):** [Verified Turn 3133] Tiles (26,23) and (27,22) are solid rock wall faces enclosing the upper platform landing. Exit from upper landing is West to (25,22) and Down stairs at (25,23).
- **Solid Rock Wall Face at (30,22)-(34,22):** [Verified Turn 3144] Tiles (30,22) through (34,22) are solid rock wall faces. Column 30 does NOT lead North from Row 22. Eastern corridor route to Top Corridor is via Columns 35-37!
- **Solid Impassable Boundary at (30,25):** [Verified Turn 3149] Tile (30,25) is impassable when attempting to walk East from (29,25).
- **Solid Ledge / Wall Face at (25..31, 28):** [Verified Turn 3158] Row 28 at Columns 25-31 is a solid ledge / wall face blocking Southward movement from Row 27. Exit West from lower room is via Row 27 (Cols 29-25) back toward (15,27).

- **Column 30-31 Cliff Face (Rows 20-28):** [Verified Turn 3412] Columns 30 and 31 on Mt. Moon B1F form a solid impassable blue/purple cliff face spanning Rows 20 through 28, enclosing the South-East cavern (Cols 24-29, Rows 22-27).
- **Ladder Tile at (15,27) Warp Behavior:** [Verified Turn 3712] Tile (15,27) on B1F is the ladder warp back to 1F (13,27). Walking onto (15,27) on B1F immediately triggers map warp.
- **Solid Rock Wall Face at (28,21):** [Verified Turn 3725] Tile (28,21) is a solid rock wall face blocking Northward passage along Column 28.
- **Row 24 Stair Entrance (Cols 25-28):** [Verified Turn 3726] Row 24 is wide open floor connecting Col 28 West to (25,24) at the base of the Upper Platform stairs at (25,23).
- **Solid Rock Boulder at (33,9):** [Verified Turn 4408] Tile (33,9) on B1F is a solid rock boulder/pillar face (impassable).
- **North Wall Barrier (Rows 2-5, Cols 30-39):** [Verified Turn 4409] Rows 2-5 across Columns 30-39 form a solid rock wall face enclosing the top-right corridor.
- **Side-Room Loop Warp:** [Verified Turn 4392] Ladder at (25,9) on B1F warps to B2F (17,11); ladder at (17,11) on B2F warps to B1F (25,9), forming an isolated side-room loop.
- **Solid Wall Collision at (26,10):** [Verified Turn 4446] Tile (26,10) on B1F is a solid rock wall face.

<hr>

<h1><code>Locations/Mt_Moon_B2F</code></h1>

# Mt. Moon B2F Map & Points of Interest

## Geometry & Points of Interest
- **Spawn Ladder at (25,9):** [Verified Turn 1090] Arrived from B1F ladder at (17,11), spawning at X=25, Y=9 in B2F.
- **Corridor Chamber (Rows 8-11, Columns 17-25):** [Verified Turn 1093] Open floor chamber connecting (25,9) West to (17,11).
- **B2F Ladder Warp at (17,11) -> (25,9):** [Verified Turn 1095] Ladder at (17,11) warps to main B2F chamber, spawning at X=25, Y=9.
- Picked up Item Ball at (29,5) [Turn 1115 - TM01 Mega Punch].
- **Rocket Grunt at (29,10):** [Defeated Turn 1106 - Lv 12 Zubat, Lv 12 Ekans].
- **Upper Platform Dead End:** [Verified Turn 1154] Upper platform spans Columns 27-30 at Rows 5-6, bounded North by Row 4 wall, West by Col 26 wall, East by Col 31 wall. Only contained TM01 at (29,5).
- **East Wall Boundary at Column 36 (Rows 12-14):** [Updated Turn 4291] Column 36/37 connects South into the bottom-right exit cavern.
- **Rock Pillar Face at (32,12)-(33,15):** [Verified Turn 3781] Solid rock wall face blocks Rows 12-14 across Columns 30-37.
- **Row 20 Boundary:** [Verified Turn 1509] Row 20 is a solid rock wall face across Columns 13-18. B2F South passage turns West along Row 19 (Cols 13-17).

- **Helix Fossil Status:** [Verified Turn 4331] Checked Bag inventory directly; Helix Fossil is NOT in inventory yet. Must locate Super Nerd in B2F Main Cavern.
- **Column 18 Wall Boundary (Rows 8-15):** [Verified Turn 1940] Column 18 is a solid rock wall face across Rows 8-15, blocking Eastward movement from (17,11) along Row 11.
- **Rocket Grunt #2 at (30,27):** [Spotted Turn 1963] Rocket Grunt at (30,27) facing Right guarding the exit corridor.
- **Picked up Item Ball at (35,31):** [Turn 1965] Collected item from Item Ball at (35,31) in bottom-right B2F chamber.
- **Super Nerd #2 at (24,31):** [Defeated Turn 1999 - Lv 11 Magnemite, Lv 11 Voltorb].
- **(12,15) and (13,15) Wall Boundary:** [Verified Turn 4469] Tiles (12,15) and (13,15) on B2F are solid blue/purple rock wall faces (impassable).
- **CRITICAL WARP PAIRS:**
  - B1F (25,9) <-> B2F (17,11) [Reciprocal 2-ladder side-room loop]
- **Column 18-19 Rock Wall:** [Verified Turn 2182] Solid rock wall spans Columns 18-19 across Rows 11-21. Open South Passage is Column 20 leading directly to Row 23.
- **Row 12 Wall Face (Cols 16-21):** [Verified Turn 2428] Solid rock wall blocks Southward movement along Columns 16-21 at Row 12.

- **(25,9) Rock Wall Face:** [Verified Turn 2992] Tile (25,9) is a solid rock wall face. Row 8-9 blocks Upward movement across Cols 22-29.

- **Column 22-23 Rock Wall Face (Rows 20-27):** [Verified Turn 2863] Solid rock wall face blocks Westward passage at Columns 22-23 across Rows 20 through 27.
- **Col 19 Solid Rock Wall Face (Rows 26-35):** [Verified Turn 2893] Solid purple rock wall face blocks Westward movement across Column 19 on Rows 26-35. Eastern Cavern (Cols 20-35) connects to Western Cavern via Row 7 Upper Corridor (17,7).

- **Column 18-19 Rock Wall Face (Rows 8-14):** [Verified Turn 2913] Solid purple rock wall blocks Rows 8-14 across Columns 18-19. Row 7 connects Column 20 West to Column 17.
- **Northern Bypass (Rows 5-6):** [Verified Turn 4248] Column 23 rock wall face blocks Row 6 at (23,6).
- **South Highway at Columns 20-21:** [Verified Turn 4496] Columns 20 and 21 form an open brown cave floor passage across Rows 18-23 leading South into the B2F Bottom Cavern.

<hr>

<h1><code>Scratchpad/B2F_Routing</code></h1>

- [Turn 4517 Discovered B2F Map Geometry]
  - Row 20 is solid rock wall across Cols 10-18 on B2F.
  - Western Cavern (Cols 10-17, Rows 8-19) connects East to Column 20 via Row 7 Upper Corridor at (17,7).
  - Route from (13,19) to B2F Bottom Cavern:
    1. Walk East to (17,19) and North along Col 17 to (17,12).
    2. Bypass ladder (17,11) via (16,12) -> (16,10) -> (17,10).
    3. Walk North to (17,7), then East along Row 7 to Column 20.
    4. Walk South down Column 20/21 into Bottom Cavern (Rows 25-35) to reach Super Nerd #2 at (24,31) with the Helix Fossil!
- [Turn 4523 Correction] Row 8 is a solid blue rock wall face across Cols 18-25. Row 7 upper corridor continues East past Col 25.
- [Turn 4524 Verified] Column 30 is the open vertical passage connecting Row 7 (30,7) South past Row 8 wall (30,8..12) into the Main Cavern!
- [Turn 4536 Discovered] Row 26 is blue rock wall across Cols 26-29. Column 31 is the open vertical corridor South to Row 31!

<hr>