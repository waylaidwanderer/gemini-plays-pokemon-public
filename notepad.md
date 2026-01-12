# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics
- FLOOR: Standard traversable.
- WALL: Impassable.
- WATER: Requires SURF.
- TALL_GRASS: Wild encounters.
- DOOR/WARP/CAVE/LADDER: Entry/exit points.
- LEDGE_HOP_DOWN: One-way traversal (North to South only).
- FLOOR_UP_WALL/FLOOR_DOWN_WALL/FLOOR_LEFT_WALL/FLOOR_RIGHT_WALL: Block movement in specified direction.
- Diglett's Cave: FLOOR_UP_WALL at (15, 34) is NOT jumpable from North. (Turn 42449)

## Strategy: Remaining Kanto Journey
- Badges: Volcano (Cinnabar/Seafoam), Earth (Viridian).
- Cinnabar Access: Route 19 blocked (Turn 42376). Detour: Fly Vermilion -> Diglett's Cave -> Route 2 -> Viridian -> Pallet -> Surf south.

## Route 2 Investigation (Started Turn 42471)
- Nugget House (Fisher): (15, 15). Obtained Nugget.
- Route 2 Gatehouse (South): (16, 27) / (17, 27).
- Scientist (Gatehouse): Prof. Oak's Aide. Mentioned Oak's Lab in Pallet Town. (Turn 42518)
- Southern Route 2 Observations:
    - Item Ball at (14, 50).
    - Cut Tree at (12, 50).
    - Bug Catcher at (10, 45).
    - Viridian City Entrance at (10, 53).
- Obstacles:
    - Walls at X=12, 13 block Westward movement.
    - Ledges at Y=21, 23 are one-way South.
- Entry/Exit:
    - North: Pewter City (8, 0).
    - East: Diglett's Cave (12, 7).
    - South: Gatehouse (16, 27) / (17, 27).

## Diglett's Cave (Started Turn 42430)
- Topology: Tiered layout requires specific ladders to reach the exit.
- Connections: (5, 31) <-> (17, 33), (3, 3) <-> (17, 3).
- Exit: (15, 5) via ladder at (3, 3).

## Battle and Pokemon Information
### Party Movesets
- Calcifer (Typhlosion): Flamethrower, Return, Smokescreen, Thunderpunch.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- LAPIS (Poliwag): Waterfall, Surf, Hypnosis, Whirlpool.
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.

### Significant Battles (Kanto)
- Erika, Janine, Brock, Misty, Lt. Surge, Sabrina defeated.

## PC Box Status
- Box 1: 9/20 full. Includes GORP (Snorlax Lv50), Selkie (Seel), Delta (Mantine).

---
**Lesson Log:**
- Verification: Always test ledge jumpability before assuming a path is valid.
- Notepad: Be extremely precise with `old_text` for `replace` actions.
- Bag Management: Item Pocket limit is 20 unique items. (Turn 42486)
- NPC Interaction: Talk to Professors and Aides; they often provide useful context or rewards.