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
- Current Turn: 42162
- Time Elapsed: ~100 turns
- Status: At the bottom of Route 17, attempting to exit to Route 18.

## Strategy for Navigating Route 17 (Bottom Area)
- Observation: Row 85 is a WALL barrier from X=5 to X=19. Row 84 at X=16, 17, 18, 19 is also a WALL.
- Hypothesis: To reach the exit at (17, 82) or (17, 83), I must move North to Row 83 or 82 where the path East is clear.
- Plan: Move North to Row 82, then East to X=17. This avoids the wall blockages at Row 84 (16, 84).
- Physics: Constant Southward drift requires rapid Northward inputs.
- Start Turn: 42154. Current Attempt: 4.

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
- Next Step: Pass through Route 18 Gate to reach Fuchsia City.

---
## Route 17 Navigation Warning (Turn 42126)
- Physics Trap: Avoid column 6 at Y=53. Blocked by Biker Glenn (5, 53) and Water (6, 54).
- Downhill mechanic makes Northward recovery extremely difficult.
- Recommendation: Stick to far left lane (X=2-5) or far right lane (X=14-17) for safety.
## Route 17-18 Gatehouse Status
- Status: Inside Route 17-18 Gatehouse (Turn 42165). Route 17 traversal completed.
- Goal: Find exit to Route 18 and reach Fuchsia City.
- NPC: Officer at (5, 2).
- Tile: WARP_CARPET_LEFT (Standard warp tile).