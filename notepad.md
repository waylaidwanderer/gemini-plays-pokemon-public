# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics (Verified Behavior)
- FLOOR: Standard traversable tile. No special effects.
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

## Battle and Pokemon Information
### Party Movesets
- Calcifer (Typhlosion): Flamethrower (0 PP), Return, Smokescreen, Thunderpunch.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- LAPIS (Poliwag): Waterfall, Surf, Hypnosis, Whirlpool.
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.

### Significant Battles
- Erika (Celadon Gym): Defeated with Fire-type moves. Lv 42-46 team.
- Rival Silver (Mt. Moon): Defeated.

## Evolution Methods
- Poliwag -> Poliwhirl -> Poliwrath (Water Stone) or Politoed (Trade with King's Rock). (Source: Fisher at 26,11)
- Gloom -> Vileplume (Leaf Stone) or Bellossom (Sun Stone).
- Haunter -> Gengar (Trade).
- Graveler -> Golem (Trade).

## PC Storage
### Box 1 (Current) (9/20)
- GORP (SNORLAX): Lv50 (Male)
- AAAAAAAAAA (SPINARAK): Lv13 (Male)
- GLAIVE (SCYTHER): Lv14 (Female)
- SELKIE (SEEL): Lv24 (Female)
- DELTA (MANTINE): Lv20 (Male)
- RANGOON (KRABBY): Lv22 (Female)
- NOMURA (TENTACOOL): Lv17 (Female)
- Ravioli (KRABBY): Lv10 (Male)
- Ouroboros (DRATINI): Lv15 (Male)

## Economy & Shopping
- Celadon Dept Store: Inventory for 2F, 3F, 4F, 5F, 6F documented in previous turns.
- Evolution Stones: Not available in Celadon Dept Store.

## Celadon City Investigation (Started Turn 41409, Jan 11 3:10 PM)
- Mansion Roof House: Pharmacist (3,2) tells "terrifying tale" ONLY at night.
- Gym Access: Path behind southern hedges (Cut tree at 28,35). Follow path west to (5,35), then north through gap in ledge at (5,33). Warp at (10, 29).

## Route 17 (Cycling Road) Mechanics
- Downhill Coasting: The player automatically moves South.
- Moving North: Requires constant Up input. (Verified Turn 42121)

## Kanto Secrets & NPC Schedules
- Daisy Oak (Pallet Town): Has tea every day from 3:00 PM to 4:00 PM. (Source: Chad)
- Pallet Town: Not yet visited. Cannot Fly there until visited on foot.
- Soul Badge: Fuchsia City Gym Leader Janine.

## Fuchsia City Journey (Started Turn 42062, Jan 11 4:01 PM)
- Strategy: Traverse Route 16, 17, and 18 via Cycling Road.
- Requirement: Bicycle (Confirmed in Key Items).
- Goal: Reach Fuchsia City, defeat Janine for the Soul Badge.

## Strategy for Remaining Kanto Journey
- Objective: Defeat Janine (Fuchsia), Blaine (Cinnabar/Seafoam), Blue (Viridian).
- Strategic Plan:
    1. Celadon (Rainbow) - DONE.
    2. Fuchsia (Soul) - Cycling Road (Route 16-18).
    3. Cinnabar/Seafoam (Volcano).
    4. Viridian (Earth).
- Rematches: Alan (Route 36) wants a battle.

## General Lessons & Error Log
- NPC Interaction: Face the counter tile in front of NPCs (Nurses, Clerks, etc.) then press A.
- Ledges: Hop down south only.
- Menu Navigation: Use single `press_buttons` to verify menu state during complex sequences. Avoid long `press_menu_buttons_v3` chains when stuck.
- Menu Cursors: Verify cursor position before committing to a long button sequence.
- Thirsty Girl (6F): Does not exist in Crystal version. (Verified Turn 41936)

---
(Note: Removed completed action logs for Game Corner and Prize Exchange to reduce bloat.)
## Route 17 Navigation Warning (Turn 42126)
- Physics Trap: Avoid column 6 at Y=53. Blocked by Biker Glenn (5, 53) and Water (6, 54).
- Downhill mechanic makes Northward recovery extremely difficult.
- Recommendation: Stick to far left lane (X=2-5) or far right lane (X=14-17?) for safety.