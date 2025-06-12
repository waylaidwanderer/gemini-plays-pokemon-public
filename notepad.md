# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Current Status
- Location: Route 2 (Map ID 13) at (8,62).
- Badges: 0
- Level Cap: 12
- Money: ¥1175

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv8 (25/28 HP, EXP: 530/800 to Lv9) | Moves: THUNDERSHOCK, GROWL, QUICK ATTACK, THUNDER WAVE

## Current Objectives
- **Primary:** Defeat Brock, the Pewter City Gym Leader.
- **Secondary:** Travel to Pewter City.
- **Tertiary:** Explore Viridian Forest for items and Pokémon.

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
- Wild Battle Escapes: Speed-dependent.
- Pokémon Nicknaming: Always do it.

## Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only. Cannot move 'up' onto a ledge tile from lower ground. To jump down, be on higher ground adjacent to the ledge, move onto the ledge tile.
- **NPC Blocking**: NPCs can block paths. Player cannot move onto a tile occupied by a stationary NPC if it's the first step of a path from pathfinder or by pressing in their direction when adjacent and facing them.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.

## Type Matchup Discoveries
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

## Key NPCs & Info Log (Condensed)
- Youngster (Route 1, (6,27)): Gave Potion.
- Youngster (Route 1, (16,14)): Explained STAT Experience.
- Girl (Viridian School, (4,6)): CUT is Bug HM.
- Girl (Viridian School, (5,6)): Pokémon evolve by training.
- Old Man (Viridian City, now (20,14)): Path to Route 2 unblocked after coffee. Gave catching tutorial.
- Viridian Mart Clerk: Sells Poké Balls after Oak's Parcel delivery.

## Agent Strategy & Ideas
### Active Agent Ideas:
1.  **Level Cap Compliance Agent**: Checks Pokémon levels against current cap. (To be defined this turn)
2.  **Viridian Forest Navigator**: Helps navigate Viridian Forest. (Future idea)
3.  **Obstacle Aware Path Planner**: Simpler pathfinder aware of temporary obstacles. (Future idea)

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
- Mark defeated trainers (☠️), used warps (🚪), key info NPCs (💡), signs (ℹ️), obstacles (🚧), items given by NPCs (🎁).
- Use distinct emojis and concise labels. Delete redundant markers.

## Lessons Learned & Strategy Refinements
-   **Trust Game State**: GSI is absolute truth for dynamic data (NPCs, items).
-   **Pathing**: Double-check tile types (especially ledges) before committing to a path. NPCs can block movement. My pathing on Route 2 around the sign and ledges needs more care.
-   **Critical Path**: Prioritize objectives that unblock main progression (e.g., Old Man in Viridian) before extensive detours like Route 22.
-   **Efficiency**: Plan longer movement sequences. Avoid repeated interactions if the first attempt yields no new info.
-   **Hypothesis Testing**: Form hypotheses, test systematically, document failures and attempt counts.
-   **Route 22**: Was a detour. Path to Pewter is North from Viridian City via Route 2 / Viridian Forest.
-   **Mart Exit (Viridian)**: Exits to (30,21) outside Mart, not School House.