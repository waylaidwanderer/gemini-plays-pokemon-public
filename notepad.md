# Tile Mechanics
- FLOOR: Traversable. Standard ground.
- WALL: Impassable. Collision block.
- DOOR: Warp tile. Leads to a building or interior.
- TALL_GRASS (Grass): Traversable. Triggers wild Pokémon encounters.
- WATER: Requires HM SURF to traverse.
- LEDGE: One-way jump. Traversable only from the jumping side.
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt.
- WARP_CARPET: Warp tile at map boundaries/edges.
- FLOOR_UP_WALL: Special floor that blocks movement North (Up) and blocks entry from the North (Down).
- LEDGE_HOP_DOWN: One-way ledge. Jump Down only.
- LEDGE_HOP_RIGHT: One-way ledge. Jump Right only.
- LEDGE_HOP_LEFT: One-way ledge. Jump Left only.
- COUNTER: Impassable. Used to interact with NPCs behind them. Stand adjacent and face the counter to talk.
- STAIRCASE: Warp tile. Leads to a different floor or area.
- ESCALATOR: Warp tile. Automatically moves player between floors.

# Type Effectiveness Chart (Verified)
- Fire -> Grass: Super effective.
- Water -> Fire: Super effective.
- Electric -> Water: Super effective.
- Ground -> Poison: Super effective.
- Psychic -> Poison: Super effective.
- Ghost -> Psychic: Super effective.
- Ice -> Flying: Super effective.
- Fighting -> Normal: Super effective.
- Water -> Water: Not very effective.
- Fire -> Fire: Not very effective.

# Pokemon Information & Movesets
- Party (6/6): ICARUS (Lv19 Pidgeotto), Calcifer (Lv64 Typhlosion), KIMCHI (Lv52 Gloom), GNEISS (Lv55 Graveler), GORP (Lv50 Snorlax), XENON (Lv44 Haunter).

# Legendary Hunt Strategy
- Lead: ICARUS (Lv 19) with Super Repel to filter for Lv 40 Roamers on Route 37.
- Backup Lead: XENON (Haunter) for Hypnosis (if Master Ball is saved).
- Movement: Ecruteak Shuffle (Route 37 <-> Ecruteak City).
- Target: Raikou (Master Ball), Entei (Hypnosis + Ultra/Great Balls).
- Suicune Strategy: Static encounter at Tin Tower in Crystal. Requires Clear Bell and defeating the Wise Trio.

# Roamer Tracking
- Route 37: 0 encounters.
- Route 36: 0 encounters.
- Route 38: 0 encounters.

# Lessons Learned
- Precise menu navigation is critical; verify menu state after every 1-2 inputs.
- Fly Usage: Must be outdoors to use Fly.
- Suicune (Crystal): Suicune is NOT a roamer in Crystal; it is found at Tin Tower.
- Repel Trick: Use a lead Pokémon with a level between the local wild encounters and the target legendary (e.g., Lv 19 Pidgeotto for Lv 40 Roamers on Route 37).
- Menu Order: POKEDEX (0), POKEMON (1), PACK (2), POKEGEAR (3), GEM (4), SAVE (5), OPTION (6), EXIT (7).
- Menu Memory: The main menu cursor does NOT reset to POKEDEX. It stays on the last selected option.
- Navigation Reset: If a menu navigation fails, immediately back out to the overworld (multiple 'B' presses) to reset state.
- Super Repel Application (from POKEDEX/Index 0): [Start, Down x2, A, Down x20, Up x1, A, A, A]. Break into chunks < 50 buttons.

# Legendary Hunt Execution
- Start Turn: 44521.
- Use 'grass_pacer' on Route 37 to trigger encounters while Repel is active.
- If Repel wears off, immediately re-apply from the Pack.
- If a roamer is encountered, use the Master Ball (for Raikou) or Hypnosis (for Entei).
- Roamers cannot be tracked on the Pokegear Map until the first encounter occurs.
- After every 50-100 steps without an encounter, transition maps (Ecruteak Shuffle) to redistribute roamers.
- Current Method: Ecruteak Shuffle (Route 37 <-> Ecruteak City).

# Technical & Tool Development
- Custom Tools: Access script arguments via 'input_data' dictionary.
- Menu Navigator Strategy: Prepend several 'Up' or 'Down' presses to guarantee a starting point if memory is unreliable.
- Pack Navigator Strategy: Prepend 20 'Down' presses to reach 'CANCEL', then 'Up' once to reach the bottom-most item (Super Repel).

# Tool Usage Lessons
- Turn 44558: 'menu_navigator_v2' failed due to 50-button safety limit. Break deep menu navigation into smaller chunks (e.g., 15-20 buttons per turn).
- Turn 44558: Main menu cursor confirmed at POKEDEX (Index 0) after backing out.

# Failed Hypotheses & Attempts
- Menu Navigation: Multiple failures due to cursor memory and tool button limits. Verified that the main menu cursor persists and deep navigation must be split into chunks < 50 buttons.
- Turn 44634: Successfully reached Super Repel in PACK.
- Strategy: Use Super Repel -> Resume Ecruteak Shuffle.
- Lead: ICARUS (Lv 19).
- Current state: PACK menu open, cursor on SUPER REPEL.
- Step 1: Use Super Repel and return to overworld.
- Step 2: Pace in grass at (6, 3) or (6, 5).
- Step 3: Transition to Ecruteak City and back to shuffle roamer positions.