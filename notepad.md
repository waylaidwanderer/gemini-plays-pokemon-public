# Gem's Journey in Pokémon Crystal

## Game Mechanics
- Menu Controls: 'Up' moves forward (Sat -> Sun -> Mon), 'Down' moves backward.
- Tool Usage: Must pass 'autopress_buttons: true' to execute returned button sequences.

## Tile Mechanics
- FLOOR: Traversable. Standard walking tile.
- WALL: Impassable.
- STAIRCASE: Traversable. Warps to another floor.
- WARP_CARPET_DOWN: Traversable. Warps to a different map.
- DOOR: Traversable. Warps to indoor maps.
- LEDGE_HOP_DOWN/LEFT/RIGHT: One-way traversable (jump down). Impassable from other directions.
- TALL_GRASS: Traversable. Contains wild Pokemon encounters.

## Current Plan
- Return to Professor Elm in New Bark Town to deliver the Mystery Egg.

## Pokemon Locations
- Route 29: Hoppip (Splash), Sentret, Pidgey
- Route 30: Caterpie, Pidgey

## Route 29 Navigation Log
- **East Section:** Bypass trees at x=37 by going south to y=16.
- **Middle Section (Ledge Puzzle):** Access North Path via gap at x=31. Loop East behind ledges to x=42, then North to y=8 to head West.
- **North Path (Westbound):**
  - Blockage at x=33 (y=3-5): Bypass via South at y=6.
  - Tree Zig-Zag (x=20-23): Path blocked at y=4 (x=23) and y=5 (x=20). weave between them.
  - Ledges at x=15: Block Westward movement. Bypass via South at y=6.
  - One-Way Ledges at x=8 (y=6-8): Allow Westward movement (Jump Left).
- **Dead Ends/Blockades:**
  - Lower path (y=15) dead-ends at x=14.
  - x=21 blocked by CUT_TREE.
  - Corridor at x=49 (North) is a dead end.
  - Plateau at (12-14, 2-4) accessible only from North/West (Fruit Tree/Cooltrainer).
- Route 29 Sign at (3, 5): CHERRYGROVE CITY - NEW BARK TOWN
- Route 29: SW pocket at (4-7, 10-15) is a dead end with tall grass. No items found.
## Cherrygrove City
- Arrived from Route 29 via East exit.
- Need to find Mr. Pokemon's house (north of here?).
- Need to find a Pokemon Center to heal.
- Cherrygrove Locations Identified:
  - Pokemon Center: (29, 3)
  - Mart: (17, 7)
  - Guide Gent's House: (25, 9)
  - Sea/Water: South side of city
- Received MAP CARD from Guide Gent.
- Guide Gent's tour finished. He went into his house at (25, 9).
- Healed at Pokemon Center. Now seeking exit to Route 30 (North).
- Found exit to Route 30 at x=16 on North side of Cherrygrove.
- Entered Route 30. Heading North to find Mr. Pokemon's house.
- Route 30 Entrance: Path straight North is blocked by ledges. Exploring East through grass to find a way around.
- Route 30: Ledges block x=6-11. Gap North exists at x=12-13 (Tall Grass).
- Route 30 Sign at (9, 43): "ROUTE 30" / "VIOLET CITY - CHERRYGROVE CITY".
- Found a house at (7, 39). Investigating.
- Found Fruit Tree at (5, 39).
- Found House at (7, 39) which might be Mr. Pokemon's.
- Entered 'Route30BerryHouse'. Confirmed this is NOT Mr. Pokemon's house. The man inside teaches about Berries.
- NPC located at (2, 3) gave me a BERRY and explained they drop from trees.
- Path North at x=5 (Rows 23-26) is blocked by a Pokemon Battle (Youngsters + Monsters). Must find alternate route to the East.
- Checked path North. Sign at (13, 29) says 'MR.POKéMON'S HOUSE STRAIGHT AHEAD!'. Navigating North along x=14.
- Path North at x=14 is blocked by a wall at y=19.
- Detoured East through Tall Grass (x=17-19) and found Mr. Pokemon's House at (17, 5).
- Received urgent phone call from Professor Elm. Something terrible has happened at the lab. Returning immediately.
- Route 30 Return Trip: Head South along x=12 to row 44 (Floor path), then West to x=6, then South over ledges to exit. Path avoids tall grass.