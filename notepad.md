# Gem's Pokémon Crystal Knowledge Base

## Global Tile Mechanics
- FLOOR: Standard traversable tile. No special effects.
- FLOOR (Route 17): Downhill coasting mechanic (automatic South movement). North movement requires constant input. (Verified Turn 42121)
- WALL: Impassable collision. Blocks all movement.
- WATER: Impassable on foot. Requires SURF to traverse.
- TALL_GRASS / grass: Standard traversable tile. May trigger wild encounters.
- DOOR / WARP / CAVE: Entry/exit points. Stepping on them triggers a map transition.
- WARP_CARPET_DOWN: Entry/exit point. Functions like a DOOR/WARP.
- LADDER / STAIRCASE: Vertically connects different maps or floors.
- COUNTER: Impassable collision. Blocks movement but allows interaction with NPCs behind it if faced from an adjacent tile.
- MART_SHELF: Impassable collision. Blocks all movement.
- LEDGE_HOP_DOWN: One-way traversal. Can only be crossed from North to South.
- FLOOR_LEFT_WALL / FLOOR_RIGHT_WALL / FLOOR_UP_WALL: Collision that blocks movement in the specified direction.
- WARP_CARPET: (7,3) and (8,3) in Celadon Dept Store 5F are traversable floor tiles, not active warps. (Verified Turn 41878)
- OBJECTS (NPCs/Items): Impassable collision. Must be navigated around. Interaction possible from adjacent tiles.
- PC / BOOKSHELF: Impassable collision. Interaction possible from adjacent tiles.

## Fuchsia City Journey Tracking
- Start Turn: 42062
- Current Turn: 42192
- Status: Talking to a Youngster in Fuchsia City.

## Battle and Pokemon Information
### Party Movesets
- Calcifer (Typhlosion): Flamethrower (0 PP), Return, Smokescreen, Thunderpunch.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- LAPIS (Poliwag): Waterfall, Surf, Hypnosis, Whirlpool.
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.

### Significant Battles
- Erika (Celadon Gym): Defeated.
- Rival Silver (Mt. Moon): Defeated.
- Biker Charles (6, 80): Defeated.
- Bird Keeper Bob (13, 6): Defeated with Calcifer's Thunderpunch. Team: Noctowl (Lv34).

## Evolution Methods
- Poliwag -> Poliwhirl -> Poliwrath (Water Stone) or Politoed (Trade with King's Rock).
- Gloom -> Vileplume (Leaf Stone) or Bellossom (Sun Stone).
- Haunter -> Gengar (Trade).
- Graveler -> Golem (Trade).

## PC Storage
- Box 1: GORP (Snorlax Lv50), etc. (9/20 full)

## Economy & Shopping
- Celadon Dept Store: Large selection, no evolution stones.

## Celadon City Investigation
- Mansion Roof House: Storyteller NPC only active at night.
- Gym Access: Requires Cut and navigating through the southern garden.

## Kanto Secrets & NPC Schedules
- Daisy Oak (Pallet Town): Tea time 3-4 PM daily.
- Soul Badge: Fuchsia City Gym (Leader Janine).

## Strategy for Remaining Kanto Journey
- Goals: Fuchsia (Soul), Cinnabar/Seafoam (Volcano), Viridian (Earth).
- Next Step: Defeat trainers on Route 18 and reach Fuchsia City.

## General Lessons & Error Log
- NPC Interaction: Face the counter tile in front of NPCs (Nurses, Clerks, etc.) then press A.
- Ledges: Hop down south only.
- Menu Navigation: Use single `press_buttons` to verify menu state.
- Route 17 Physics: Downhill mechanic requires consistent Northward inputs or rapid tapping to overcome drift.
## Fuchsia City Exploration (Started Turn 42186)
- Objective: Find Pokemon Center and Gym.
- Observation: City has a complex layout with many interior fences/walls.
- Interaction Log:
    - Youngster (Object 1): Moving around near (24, 19).
- Map Progress: 19.6% explored.