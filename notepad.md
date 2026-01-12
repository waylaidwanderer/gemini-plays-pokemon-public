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
- Note: Need to encounter Raikou/Entei once in the wild for them to appear on the Pokegear Map.
- Super Repel status: Out of stock. Heading to Goldenrod Dept. Store.
- Suicune Strategy: Static encounter at Tin Tower in Crystal. Requires Clear Bell (in inventory).

# Legendary Hunt Strategy
- Lead: ICARUS (Lv 19) with Repel to filter for Lv 40 Roamers on Route 37.
- Backup Lead: XENON (Haunter) for Hypnosis (if Master Ball is saved).

# Goldenrod Restock Plan (Started: Turn 44278)
1. Travel to Goldenrod City (Pivoted to biking from New Bark Town on Turn 44319).
2. Navigate to Goldenrod Dept. Store (North of PC).
3. Buy a full stack of Super Repels.
4. Fly back to Ecruteak City (or bike back if Fly remains unreliable).
5. Resume legendary hunt on Route 37 using the 'grass_pacer' tool.

# Fly Strategy (FAILED)
- Target: Goldenrod City (West of New Bark).
- Status: Fly map navigation failed repeatedly (15 attempts, Turn 44260-44310). Cursor stayed on New Bark Town.
- Pivot: Biking to Goldenrod.

# Lessons Learned
- Precise menu navigation is critical; verify menu state after every 1-2 inputs.
- PC Storage: Parties must have space before withdrawing; always deposit first if at 6/6.
- Fly Usage: Must be outdoors to use Fly.
- Suicune (Crystal): Suicune is NOT a roamer in Crystal; it is found at Tin Tower. Route 37 for Raikou/Entei.
- Repel Trick: Use a lead Pokémon with a level between the local wild encounters and the target legendary (e.g., Lv 19 Pidgeotto for Lv 40 Roamers on Route 37).
- Menu Order: POKEDEX, POKEMON, PACK, POKEGEAR, [Player Name], SAVE, OPTION, EXIT.
- Fly map scrolling: Node-based grid movement. Failed to move cursor West from New Bark Town. Verify destination name on screen before pressing A.