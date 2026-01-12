# Gem's Pokémon Crystal Knowledge Base

## Global Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL: Impassable collision.
- WATER: Requires SURF.
- TALL_GRASS: Traversable, wild encounters.
- DOOR/WARP/CAVE/LADDER: Entry/exit points.
- LEDGE_HOP_DOWN: One-way traversal (North to South only).
- FLOOR_UP_WALL/FLOOR_DOWN_WALL/FLOOR_LEFT_WALL/FLOOR_RIGHT_WALL: Block movement in specified direction. In Diglett's Cave, FLOOR_UP_WALL is NOT jumpable from the North. (Turn 42449)

## Strategy: Remaining Kanto Journey
- Badges needed: Volcano (Cinnabar/Seafoam), Earth (Viridian).
- Cinnabar Access Strategy:
    - Route 19 is blocked by construction. (Turn 42376)
    - detour: Fly to Vermilion -> Diglett's Cave -> Route 2 -> Viridian -> Pallet -> Surf south to Cinnabar.

## Diglett's Cave Investigation (Started Turn 42430)
- Goal: Exit to Route 2 at (15, 5).
- Internal Connections:
    - Ladder at (5, 31) <-> Ladder at (17, 33).
    - Ladder at (3, 3) <-> Ladder at (17, 3).
- Path to Exit: From (17, 3), move Down, Left, Down, Left to reach (15, 5).
- Blockages:
    - (15, 34) is a wall/ledge that cannot be jumped from the North. (Turn 42449)
    - (17, 33) area is isolated from the exit.

## Battle and Pokemon Information
### Party Movesets
- Calcifer (Typhlosion): Flamethrower, Return, Smokescreen, Thunderpunch.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- LAPIS (Poliwag): Waterfall, Surf, Hypnosis, Whirlpool.
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.

### Significant Battles (Kanto)
- Erika (Celadon), Janine (Fuchsia), Brock (Pewter), Misty (Cerulean), Lt. Surge (Vermilion), Sabrina (Saffron). All defeated.

## PC Box Status
- Box 1: 9/20 full. Includes GORP (Snorlax Lv50), Selkie (Seel), Delta (Mantine).

---
**Lesson Log:**
- Diglett's Cave Topology: The cave is split into tiers. Ladders connect these tiers. Tier 1 (Entry) -> Tier 2 (Ladder 5,31) -> Tier 3 (Ladder 3,3) -> Exit.
- Verification: Always test ledge jumpability before assuming a path is valid.