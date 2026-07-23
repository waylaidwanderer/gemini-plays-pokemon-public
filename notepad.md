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
- **Starter Pokémon:** Squirtle (Lv 8)
  - **Nickname:** SHELLSHOCK
  - **Moves:** Tackle, Tail Whip, Bubble
  - **HP:** 7/25
- **Route 1 Geometry:** South-facing ledges at y=27 (gap at x=6..8), y=23 (gap at x=12..15), y=19 (gap at x=4..5), and y=13 (gap at x=15..16).
- **Viridian City Overworld:** South Entrance at (21,35). Pokémon Center Door at (23,25). Pokémart Door at (29,19). Ledge gap at X=19, Y=27.
- **Key Items:** Pokédex (Obtained from Prof. Oak on Turn 265).
- **Inventory:** 5 Poké Balls (Bought in Viridian Pokémart on Turn 286), 1 Potion.

<hr>

<h1><code>Scratchpad/Route2_Geometry</code></h1>

# Viridian Forest Topology & Active Routing Scratchpad

## Verified Map Boundaries & Layout (Viridian Forest)
- Entrance South Gatehouse: (17, 47).
- Row 43 Corridor: Open from X=1 to X=17 along southern boundary.
- Column 7 Corridor: Runs north from (7, 39) to (7, 30).
- West Grass Clearing (X=1..8, Y=30..31): Dead-end pocket. Bug Catcher NPC at (1, 31). Blocked by solid tree wall on Row 29 (X=1..9) and map boundary fence at X=0.
- Row 31 Tree Wall: EMPIRICALLY CONFIRMED at Turn 361 that Row 31 (X=10..15) is a continuous solid tree trunk wall. Column 11 CANNOT move north past Y=32.
- Item Ball Location: Visible at (12, 29) inside an enclosed pocket behind log posts at (10, 29)/(13, 29).

## Current Exploration Focus
- Testing Eastward progression past column 12 along Row 33/34 towards X=16+ (Eastern side of Viridian Forest).

<hr>