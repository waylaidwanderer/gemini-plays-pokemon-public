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
- **Starter Pokémon:** Wartortle (Lv 18) [Level 18 reached on Turn 765]
  - **Nickname:** SHELLSHOCK
  - **Moves:** Tackle, Tail Whip, Bubble, Water Gun
  - **HP:** 55/55 HP [Healed at Route 4 Poké Center Turn 794]
- **Route 1 Geometry:** South-facing ledges at y=27 (gap at x=6..8), y=23 (gap at x=12..15), y=19 (gap at x=4..5), and y=13 (gap at x=15..16) [Verified Turns 189-217].
- **Key Items:** Pokédex (Obtained from Prof. Oak on Turn 265).
- **Inventory:** 5 Poké Balls (Bought in Viridian Pokémart on Turn 286), TM34 (Bide) [Obtained from Brock on Turn 565].

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
- **Row 7 Ledge Gap at Columns 34-37:** [Verified Turn 744] Row 7 has an open two-way gap at X=34..37 connecting Tier 2/3 (Row 8-10) UP to Tier 1 upper highway (Row 4-6).
- **Tile (57,7) Ledge:** [Verified Turn 784] Tile (57,7) is a solid south-facing ledge blocking upward movement from (57,8).
- **Route 4 Transition Corridor at (58,8):** [Verified Turn 785] Tile (58,8) is an open upper path bypassing the Row 7 ledge, connecting to (59,8) and the northbound Route 4 highway!
- **Route 4 North Exit at (59,7)-(59,3):** [Verified Turn 787] Column 59 at Row 7 is an open two-way passage leading North through (59,6), (59,5), (59,4), and (59,3) into Route 4!

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
- **Ladder to B1F at (15,23):** [Verified Turn 801] Ladder located at X=15, Y=23 in the entrance chamber. Trainer NPC located adjacent at (16,23) facing West.

<hr>