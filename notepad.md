# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred. Use Fly for distance.
- **Menu Verification:** Use short sequences (1-5 buttons). Verify focus indicators.
- **Internal Upgrades:** EXPN Card is a software upgrade (not an item).

## Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable. Collision is consistent.
- WATER: Traversable with SURF (requires Move + Storm Badge).
- TALL_GRASS / LONG_GRASS: Traversable.
- DOOR / WARP: Step on to enter buildings/areas.
- LADDER / PIER: Traversable. Pier stops surfing.
- CAVE: Warp tile.
- COUNTER: Impassable. Interact from front tile.
- WARP_CARPET: Warp at map edges.
- WARP_CARPET_DOWN: Exit tile. (Verified at Diglett's Cave northern exit).
- LEDGE: One-way jump down. (To be verified in Kanto).

## Menu Mechanics
- **Start Menu Order:** 1. POKEDEX, 2. POKEMON, 3. PACK, 4. POKEGEAR, 5. GEM, 6. SAVE, 7. OPTION, 8. EXIT.
- **Pokegear Radio:** 20.0 (Poke Flute) is top center in Kanto. Requires EXPN Card.

## Party Management
- **Lead Pokémon:** XENON (HAUNTER Lv44).
- **HM Users:** ICARUS (FLY), LAPIS (SURF, WATERFALL, WHIRLPOOL), KIMCHI (CUT, FLASH), GNEISS (STRENGTH).

## Quest Log
- **Kanto Gyms:**
  - Vermilion (Lt. Surge): DEFEATED.
  - Saffron (Sabrina): DEFEATED.
  - Cerulean (Misty): Target. Last seen "on a date" somewhere north?

## General Lessons & Error Log
- **Radio UI Focus:** Need to press 'Down' to move focus from the tabs (MAP/PHONE/RADIO) to the tuning dial. (Turn 40554).
- **Snorlax Interaction:** Occupies (34,8) to (35,9). Interact from (34,10) facing Up or (36,8) facing Left.
- **Sequence Errors:** Be careful with `press_menu_buttons_v2`. Large sequences can lead to turn mismatches if text boxes appear unexpectedly.
- **Diglett's Cave internal loop:** (3, 3) <-> (17, 3). Does not exit the cave. (Turn 40617).

## Time Tracking
- Current Goal (Pewter City): Started Turn 40584.

## Strategy for Misty & Cerulean Badge
- **Objective:** Find Misty on Route 25 to return her to Cerulean Gym.
- **Path:**
  1. Exit Diglett's Cave to Route 2 (north).
  2. Travel north to Pewter City.
  3. Head east through Route 3 and Mt. Moon to reach Cerulean City.
  4. Go north to Route 24, then east on Route 25 to the cape.
  5. Talk to Misty, then return to Cerulean Gym.
- **Preparation:** Buy Repels in Pewter City to speed up travel.