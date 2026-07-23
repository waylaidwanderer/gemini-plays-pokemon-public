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
- **Starter Pokémon:** Squirtle (Lv 9) [Level 9 reached on Turn 388]
  - **Nickname:** SHELLSHOCK
  - **Moves:** Tackle, Tail Whip, Bubble
  - **HP:** 23/29 [Verified Turn 389]
- **Route 1 Geometry:** South-facing ledges at y=27 (gap at x=6..8), y=23 (gap at x=12..15), y=19 (gap at x=4..5), and y=13 (gap at x=15..16) [Verified Turns 189-217].
- **Viridian City Overworld:** South Entrance at (21,35). Pokémon Center Door at (23,25). Pokémart Door at (29,19). Ledge gap at X=19, Y=27.
- **Key Items:** Pokédex (Obtained from Prof. Oak on Turn 265).
- **Inventory:** 5 Poké Balls (Bought in Viridian Pokémart on Turn 286), 1 Potion.

<hr>

<h1><code>Scratchpad/Route2_Geometry</code></h1>

# Viridian Forest Topology & Active Routing Scratchpad

## Verified Master Topology (Viridian Forest)
- Map Dimensions: 34 x 48 tiles.
- South Gatehouse Entrance: (17, 47) [Bottom Right].
- North Gatehouse Exit Door: (2, 1) / (1, 0) [Top Left].
- West Highway (Column 1/2): Uninterrupted vertical lane running from Y=25 all the way North to Exit Door at (2,1)/(1,0)!
- Central Crossing Discovered at Turn 443: Row 24/25 (X=2..6) is an OPEN PASSAGE connecting Center Lane (Column 6) to West Highway (Column 2)!
- Item Ball 3: Spotted at (4, 24) on the central crossing!

## Final Execution Plan to Exit Viridian Forest
1. Current position: (6, 25).
2. Walk Up to (6, 24), Left to (5, 24) facing Item Ball at (4, 24).
3. Press A to collect Item Ball at (4, 24).
4. Walk Left across (4, 24) and (3, 24) to Column 2 (2, 24).
5. Walk North up Column 2 from (2, 24) straight to North Gatehouse Exit Door at (2, 1) / (1, 0)!

<hr>