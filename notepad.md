# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics (Verified Traversability)
- FLOOR: Traversable. Standard movement.
- WALL: Impassable. Blocks all movement.
- WATER: Traversable with SURF (requires Move + Badge).
- TALL_GRASS / LONG_GRASS: Traversable. Wild encounters possible.
- grass: Traversable. Standard movement.
- DOOR / WARP / CAVE: Entry points to different maps or areas.
- LADDER: Traversable. Moves between floors.
- COUNTER: Impassable. Interact from the tile directly in front.
- LEDGE_HOP_DOWN: One-way jump down (North to South).
- FLOOR_UP_WALL: Impassable from North (ledge collision type).
- CUT_TREE: Impassable until CUT is used; then becomes FLOOR.
- OBJECTS (NPCs/Items): Impassable. Interact from adjacent tile.
- WARP_CARPET_DOWN: Traversable. Exit point. (Verified at Pokecenter exit)
- PC / BOOKSHELF: Impassable. (Verified at Pokecenter)

## Progress Tracking
- **Find Misty Quest:** Completed Turn 41238 at Cerulean Cape.
- **Misty Defeated:** Turn 41351. Received Cascade Badge.
- **Cerulean Gym Cleanup:** COMPLETED (Turn 41366). All trainers handled.

## Party Management
- **Calcifer (Lv 60):** Typhlosion. Flamethrower, Return, Smokescreen, ThunderPunch.
- **Kimchi (Lv 46):** Gloom. Grass/Poison. (Healed at Turn 41380).
- **Xenon (Lv 44):** Haunter. Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- **Lapis (Lv 12):** Poliwag. Surf, Whirlpool, Waterfall.
- **Gneiss (Lv 54):** Graveler. Earthquake, Rollout, Strength.
- **Icarus (Lv 19):** Pidgeotto. Fly.

## Quest Log & Battle History
- **Kanto Gyms:**
  - Pewter (Brock): DEFEATED.
  - Cerulean (Misty): DEFEATED.
  - Vermilion (Lt. Surge): DEFEATED.
  - Saffron (Sabrina): DEFEATED.
  - Celadon (Erika): Next target.

## Celadon City Journey
- Start Turn: 41371
- Objective: Defeat Erika.
- Route: Cerulean -> Route 5 -> Saffron -> Route 7 -> Celadon.
- Strategy: 
  1. Head South from Cerulean to Route 5.
  2. Pass through Route 5 to Saffron City.
  3. Head West from Saffron (Route 7) to Celadon City.
- Contingency: If Saffron gate is blocked, use the Underground Path.
- Prep: Healed at Cerulean Pokecenter (Turn 41380).

## General Lessons & Error Log
- **Inventory Sorting:** Items are NOT sorted alphabetically in-game. Prompt inventory list is sorted for readability and does not reflect in-game order.
- **Radio UI:** Press 'Down' to move focus from tabs to the dial.
- **Snorlax:** Caught at (34, 8) on Route 11.
- **Diglett's Cave:** Northern exit is (15, 5) warp carpet.
- **Button Mixing:** Never mix directional and action buttons in a single `press_buttons` call.
- **Menu Indexing:** (Turn 41290) Accidentally used Protein on LAPIS. Always verify cursor position.