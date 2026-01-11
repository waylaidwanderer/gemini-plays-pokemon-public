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
- **Objective: Defeat Misty at Cerulean Gym**
  - Started: Turn 41251
  - Current Status: In battle with Misty (Turn #41327).
- **Find Misty Quest:** Completed Turn 41238 at Cerulean Cape.

## Party Management
- **Calcifer (Lv 59):** Typhlosion. Primary attacker. ThunderPunch (Electric, 11 PP) for Water-types.
- **Kimchi (Lv 46):** Gloom. Grass/Poison. Petal Dance (Grass) for Quagsire (4x weak).
- **Xenon (Lv 44):** Haunter. Ghost/Poison. Hypnosis (Psychic) + Dream Eater (Psychic).
- **Lapis (Lv 12):** Poliwag. HM slave (Surf, Whirlpool, Waterfall).
- **Gneiss (Lv 54):** Graveler. Rock/Ground. Avoid Water battles.
- **Icarus (Lv 19):** Pidgeotto. HM slave (Fly).

## Quest Log & Battle History
- **Kanto Gyms:**
  - Vermilion (Lt. Surge): DEFEATED.
  - Saffron (Sabrina): DEFEATED.
  - Pewter (Brock): DEFEATED.
  - Cerulean (Misty): In progress.
- **Route 25 Trainers:** Dudley, Ellen, Joe, Laura, Lloyd, Shannon, Pat, Kevin: ALL DEFEATED.
- **Cerulean Gym Trainers:**
  - Swimmer Briana (1, 9): DEFEATED.
  - Swimmer Diana (4, 6): DEFEATED.
  - Swimmer (8, 9): Not yet battled.

## Strategy for Misty (Cerulean Gym)
- **Typing:** Misty uses Water-types.
- **Counter:** Lead with Calcifer (ThunderPunch) or Kimchi (Petal Dance).
- **Quagsire (Water/Ground):** Immune to Electric. Resistance to Fire. Use Kimchi's Petal Dance.
- **Starmie:** Likely her ace. ThunderPunch should be effective.

## General Lessons & Error Log
- **Radio UI:** Press 'Down' to move focus from tabs to the dial.
- **Snorlax:** Occupies (34,8)-(35,9). Interact from (34,10) Up or (36,8) Left.
- **Diglett's Cave:** Northern exit is (15, 5) warp carpet.
- **Button Mixing:** Never mix directional and action buttons in a single `press_buttons` call.
- **Menu Indexing:** (Turn 41290) Accidentally used Protein on LAPIS. Always verify cursor position.
- **Move Info:** Hypnosis is Psychic-type. Calcifer's ThunderPunch PP is limited (11/15).