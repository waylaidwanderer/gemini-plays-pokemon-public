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

## Progress Tracking
- **Find Misty Quest:** Completed Turn 41238 at Cerulean Cape.
- **Misty Defeated:** Turn 41351. Received Cascade Badge.

## Party Management
- **Calcifer (Lv 60):** Typhlosion. Flamethrower (Fire), ThunderPunch (Electric).
- **Kimchi (Lv 46):** Gloom. Grass/Poison. Petal Dance (Grass). (Currently FNT)
- **Xenon (Lv 44):** Haunter. Ghost/Poison. Hypnosis (Psychic) + Dream Eater (Psychic).
- **Lapis (Lv 12):** Poliwag. HM slave (Surf, Whirlpool, Waterfall).
- **Gneiss (Lv 54):** Graveler. Rock/Ground. Avoid Water battles.
- **Icarus (Lv 19):** Pidgeotto. HM slave (Fly).

## Quest Log & Battle History
- **Kanto Gyms:**
  - Pewter (Brock): DEFEATED.
  - Cerulean (Misty): DEFEATED (Turn 41351).
  - Vermilion (Lt. Surge): DEFEATED.
  - Saffron (Sabrina): DEFEATED.
  - Celadon (Erika): Next target.
- **Route 25 Trainers:** Dudley, Ellen, Joe, Laura, Lloyd, Shannon, Pat, Kevin: ALL DEFEATED.
- **Cerulean Gym Trainers:**
  - Swimmer Briana (1, 9): DEFEATED.
  - Swimmer Diana (4, 6): DEFEATED.
  - Swimmer (8, 9): Next target.

## Strategy for Misty (Cerulean Gym) - COMPLETED
- **Typing:** Misty uses Water-types.
- **Counter:** Lead with Calcifer (ThunderPunch) or Kimchi (Petal Dance).
- **Quagsire (Water/Ground):** Defeated.
- **Lapras (Water/Ice):** Defeated.
- **Starmie:** Defeated.

## General Lessons & Error Log
- **Radio UI:** Press 'Down' to move focus from tabs to the dial.
- **Snorlax:** Caught at (34, 8) on Route 11.
- **Diglett's Cave:** Northern exit is (15, 5) warp carpet.
- **Button Mixing:** Never mix directional and action buttons in a single `press_buttons` call.
- **Menu Indexing:** (Turn 41290) Accidentally used Protein on LAPIS. Always verify cursor position.