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

## Current Progress & Party
- **Starter Pokémon:** Squirtle (Lv 7)
  - **Nickname:** SHELLSHOCK
  - **Moves:** Tackle, Tail Whip
  - **HP:** 23/23
- **Route 1 Geometry:** South-facing ledges at y=27 (gap at x=6..8), y=23 (gap at x=12..15), y=19 (gap at x=4..5), and y=13 (gap at x=15..16).
- **Viridian City Overworld:** South Entrance at (21,35). Pokémon Center Door at (23,25). Pokémart Door at (29,19). Ledge gap at X=19, Y=27.
- **Key Items:** Pokédex (Obtained from Prof. Oak on Turn 265).
- **Inventory:** 5 Poké Balls (Bought in Viridian Pokémart on Turn 286), 1 Potion.

<hr>

<h1><code>Scratchpad/Route2_Geometry</code></h1>

# Route 2 Geometry & Exploration Log
- Turn 290: Entered Route 2 from Viridian City at (8, 71).
- Turn 291: Verified row 61 is a continuous south-facing ledge across X=2..11.
- Turn 293: Column 12 is a vertical tree line (Y=60..71).
- Turn 295: Signpost at (5, 65) reads 'ROUTE 2 VIRIDIAN CITY - PEWTER CITY'.
- Turn 301: Investigating gatehouse pillars/archway at (6, 70..71).
- Turn 302: Verified (6, 70..71) are wooden fence posts. Path at column 7 (7, 70..73) is open.
- Turn 303: Stepped south on column 7, warped to new map section at (17, 0). Inspecting signpost at (19, 1).
- Turn 305: Read Trainer Tips signpost at (19, 1). Approaching NPC at (17, 5).
- Turn 306: Talked to Coffee Man at (16, 5) in Viridian City north. Text: 'Ahh, I've had my coffee now...'
- Turn 308: Confirmed map warp connection: Viridian City North (17,0) <-> Route 2 (7,71/74).
- Turn 309: Initiated systematic sweep of row 61 ledge (testing X=9, 10, 11, 7, 6, 5, 3, 2).
- Turn 310: DISCOVERED GAP IN ROW 61 LEDGE AT X=6! Successfully passed north to (3, 57) on Route 2.
- Turn 311: Reached (3, 48) facing row 47 ledge. Identified open gap at X=8, Y=47 in front of Viridian Forest Gatehouse.

<hr>