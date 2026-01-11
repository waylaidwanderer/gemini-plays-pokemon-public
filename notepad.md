# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics (Verified Traversability)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF (requires Move + Badge). Verified.
- TALL_GRASS / LONG_GRASS: Traversable.
- grass: Traversable.
- DOOR / WARP / CAVE: Entry points.
- LADDER: Traversable.
- COUNTER: Impassable. Interact from front tile.
- LEDGE_HOP_DOWN: One-way jump down (North to South).
- FLOOR_UP_WALL: Impassable from North (ledge collision).
- CUT_TREE: Impassable until CUT is used; becomes traversable FLOOR.
- OBJECTS (NPCs/Items): Impassable.

## Progress Tracking
- **Objective: Defeat Misty at Cerulean Gym**
  - Started: Turn 41251
- **Find Misty Quest:** Completed Turn 41238.

## Party Management
- **HM Users:** ICARUS (FLY), LAPIS (SURF/WATERFALL/WHIRLPOOL), KIMCHI (CUT/FLASH), GNEISS (STRENGTH/ROCK SMASH).

## Quest Log & Battle History
- **Kanto Gyms:**
  - Vermilion (Lt. Surge): DEFEATED.
  - Saffron (Sabrina): DEFEATED.
  - Pewter (Brock): DEFEATED.
  - Cerulean (Misty): Target.
- **Recent Battles (Route 25):**
  - #1 Dudley, #2 Ellen, #3 Joe, #4 Laura, #5 Lloyd, #6 Shannon, #7 Pat: DEFEATED.
  - Prize Giver: Kevin: DEFEATED.

## Cerulean City & Surroundings
- **Misty:** Returned to Cerulean Gym after being interrupted at (46, 9) on Route 25.
- **Gramps (Bill's House):** Wants to see a Pokémon with a "long tongue" (Lickitung).

## General Lessons & Error Log
- **Radio UI:** Press 'Down' to move focus from tabs to the dial.
- **Snorlax:** Occupies (34,8)-(35,9). Interact from (34,10) Up or (36,8) Left.
- **Diglett's Cave:** (3, 3) <-> (17, 3) is an internal loop. Northern exit is (15, 5) warp carpet.
- **Button Mixing:** Never mix directional and action buttons in a single `press_buttons` call.
- **Menu Sequence:** Ensure dialogue is clear before menu inputs. Break sequences into small chunks.
## Strategy for Misty (Cerulean Gym)
- **Typing:** Misty uses Water-types.
- **Counter:** Lead with Calcifer (ThunderPunch) or Kimchi (Petal Dance).
- **Avoid:** Do not use Gneiss (Rock/Ground) as he is double-weak to Water.
- **Backup:** Xenon can provide status support with Hypnosis if needed.
- **Preparation Plan:** Use Protein on Calcifer to boost ThunderPunch stat.
- **Error Log (Turn 41290):** Accidentally used Protein on LAPIS instead of Calcifer due to incorrect menu indexing in the Pokémon selection screen. Always verify cursor position before confirming item use.