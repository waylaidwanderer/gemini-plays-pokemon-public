# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Current Status
- Location: Viridian Forest (Map ID 51) at (19,45).
- Badges: 0
- Level Cap: 12 (Next Gym: Brock, Ace Lv12)
- Money: ¥1175

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv8 (25/28 HP, EXP: 530/800 to Lv9) | Moves: THUNDERSHOCK, GROWL, QUICK ATTACK, THUNDER WAVE

## Game Mechanics & Rules Summary
- Battle Style: Set. No items in battle. Level caps apply.
- HMs: Forgettable, menu-use, not PC-storable.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses.
- EXP. All obtainable without special requirements.
- Poison: 1 HP lost per 4 steps outside battle.
- STAT Experience: Significant stat boosts from battling/leveling.
- Enemy Trainer PP: Unlimited.
- PC Log Off: Saves game.
- CUT: Bug-type HM.
- Evolution: By training.
- Status Conditions: SLP (AWAKENING), BRN (BURN HEAL), PSN (ANTIDOTE), FRZ (ICE HEAL), PAR (PARLYZ HEAL).
- Wild Battle Escapes: Speed-dependent. If lead Pokémon's Speed >= wild's, escape is guaranteed. Otherwise, chance increases with attempts.
- Pokémon Nicknaming: Always do it.

## Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger like exit mats/gatehouses).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only. Cannot move 'up' onto a ledge tile from lower ground. To jump down, be on higher ground adjacent to the ledge, move onto the ledge tile.
- **NPC Blocking**: NPCs can block paths. Player cannot move onto a tile occupied by a stationary NPC if it's the first step of a path from pathfinder or by pressing in their direction when adjacent and facing them. Dialogue loops cannot be broken by re-interacting.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.

## Type Matchup Discoveries (Verified)
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

## Key NPCs & Info Log (Condensed)
- Youngster (Route 1, (6,27)): Gave Potion.
- Youngster (Route 1, (16,14)): Explained STAT Experience.
- Girl (Viridian School, (4,6)): CUT is Bug HM.
- Girl (Viridian School, (5,6)): Pokémon evolve by training.
- Old Man (Viridian City, now (20,14)): Path to Route 2 unblocked after coffee. Gave catching tutorial (failed catch, mentioned START+A on STATS for growth potential).
- Viridian Mart Clerk: Sells Poké Balls after Oak's Parcel delivery.
- Youngster (Viridian Forest, (17,44)): Dialogue 'They're out for POKéMON fights!'. Does not battle on 'A' interaction or by walking onto tile. (Attempted interaction 3 times - dialogue only).

## Agent Strategy & Ideas
### Active/Available Agents:
1.  **Level Cap Compliance Agent** (`level_cap_compliance_checker`): Defined. Checks Pokémon levels against current cap. Should test soon.
2.  **Item Finder Agent** (`item_finder_agent`): Defined. Locates items/buildings. Value needs re-evaluation for current tasks.

### Future Agent Ideas:
1.  **Viridian Forest Navigator**: Helps navigate Viridian Forest. (Consider defining soon if forest proves complex).

### Discontinued Agents:
-   `route_pathfinder`: Consistently failed.
-   `exploration_prioritizer_agent`: Often gave unhelpful suggestions.

### General Agent Notes:
-   Ensure system prompts are robust and include all necessary game context.
-   Input schemas should not include auto-provided variables like `map_xml_string` for code-enabled agents.

## World Knowledge Graph (WKG) Best Practices
- Record inter-map transitions (map boundary, warps) immediately using `manage_world_knowledge`.
- Use descriptive names and tags for nodes.
- Include exact coordinates and connection types.
- Note `destination_entry_point` for warps when known.

## Map Marker Best Practices
- Mark defeated trainers (☠️), used warps (🚪), key info NPCs (💡/💬), signs (ℹ️), obstacles (🚧), items given by NPCs (🎁).
- Use distinct emojis and concise labels. Delete redundant markers.

## Lessons Learned & Strategy Refinements
-   **Trust Game State**: GSI is absolute truth for dynamic data (NPCs, items, map connections reachability).
-   **Pathing**: Double-check tile types (especially ledges) before committing to a path. NPCs can block movement. Repeatedly trying to move onto a blocking NPC or through a dialogue loop is inefficient.
-   **Critical Path**: Prioritize objectives that unblock main progression.
-   **Efficiency**: Plan longer movement sequences. Avoid repeated interactions if the first attempt yields no new info. Record failed interaction attempts.
-   **Hypothesis Testing**: Form hypotheses, test systematically, document failures and attempt counts.
-   **Route 22**: Was a detour. Path to Pewter is North from Viridian City via Route 2 / Viridian Forest.
-   **Mart Exit (Viridian)**: Exits to (30,21) outside Mart, not School House. WKG/Marker updated.
-   **Route 1 Ledge Navigation**: Multiple failed attempts to navigate ledges before finding correct paths. Improved understanding: cannot move 'up' onto a ledge from lower ground.
-   **Viridian Forest Gate Warp**: The warp at (5,1) in the South Gate was impassable. Used (6,1) successfully.
-   **NPC Interaction**: If an NPC dialogue repeats and no battle/event occurs, do not re-interact. Mark and move on.

## Current Exploration Plan (Viridian Forest)
- Systematically explore unseen tiles.
- Look for items (especially Antidotes, Potions), battle trainers for EXP, and find the North exit.
- Consider catching a new Pokémon (e.g., Caterpie, Weedle, Mankey if available).
- Monitor SPARKY's level (currently Lv8, cap 12).