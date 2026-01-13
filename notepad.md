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
- Caught Species (32/251).
- Observed Roamer Movesets: (None yet)

# Task: Legendary Hunt
- Start Turn: 44154
- Priority: Raikou (Master Ball).
- Method: Ecruteak Shuffle (Route 37).
- Super Repel status: Out of stock.
- Suicune Strategy: Static encounter at Tin Tower in Crystal. Requires Clear Bell and defeating the Wise Trio.

# Legendary Hunt Strategy
- Lead: ICARUS (Lv 19) with Repel (or Super Repel) to filter for Lv 40 Roamers on Route 37.
- Backup Lead: XENON (Haunter) for Hypnosis (if Master Ball is saved).
- Movement: Ecruteak Shuffle (Route 37 <-> Ecruteak City).

# Roamer Tracking
- Route 37: 0 encounters.
- Route 36: 0 encounters.
- Route 38: 0 encounters.

# Restock Plan (Started: Turn 44430)
1. Travel to Ecruteak City (Completed).
2. Pivot to Olivine City (Completed).
3. Purchase 85 Super Repels at Olivine Mart (In progress).
- Note: If Olivine fails, use `run_code` to scan Mart inventories.
4. Head to Route 37 via Ecruteak City South exit.
5. Resume legendary hunt using the 'grass_pacer' tool.

# Lessons Learned
- Precise menu navigation is critical; verify menu state after every 1-2 inputs.
- PC Storage: Parties must have space before withdrawing; always deposit first if at 6/6.
- Fly Usage: Must be outdoors to use Fly.
- Suicune (Crystal): Suicune is NOT a roamer in Crystal; it is found at Tin Tower.
- Repel Trick: Use a lead Pokémon with a level between the local wild encounters and the target legendary (e.g., Lv 19 Pidgeotto for Lv 40 Roamers on Route 37).
- Menu Order: POKEDEX, POKEMON, PACK, POKEGEAR, [Player Name], SAVE, OPTION, EXIT.
- Text Speed: Fast (Turn 44324).
- Fly Map Navigation: Cursor moves between valid points. 'Up' moves cursor north.
- Super Repel Location: Olivine City Mart (Hypothesis). Ecruteak Mart and Goldenrod Dept Store do NOT sell them in Crystal.