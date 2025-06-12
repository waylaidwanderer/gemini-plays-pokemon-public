# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv8 (25/28 HP, EXP: 530/800 to Lv9) | Moves: THUNDERSHOCK, GROWL, QUICK ATTACK, THUNDER WAVE
2. (Newly caught Oddish - will nickname SPROUT): Lv6

## Game Mechanics & Rules Summary
- Battle Style: Set. No items in battle. Level caps apply.
- HMs: Forgettable, menu-use, not PC-storable.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses.
- EXP. All obtainable without special requirements.
- Poison: 1 HP lost per 4 steps outside battle. SPARKY is currently poisoned.
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
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger like exit mats/gatehouses). Specific warps can be impassable tiles themselves (e.g. Viridian Forest South Gate north warp at (5,1)).
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
- Old Man (Viridian City, now (20,14)): Path to Route 2 unblocked after coffee. Gave catching tutorial (failed catch, mentioned START+A on STATS for growth potential). No longer blocks path.
- Viridian Mart Clerk: Sells Poké Balls after Oak's Parcel delivery.
- Youngster (Viridian Forest, (17,44)): Dialogue 'They're out for POKéMON fights!'. Does not battle on 'A' interaction or by walking onto tile. (Attempted interaction 3 times - dialogue only). Marked with 💬.

## Current Area Focus: Viridian Forest (Map ID 51)
- Objective: Find items (Antidotes, Potions), battle trainers for EXP, catch new Pokémon, and locate the North exit to Route 2.
- SPARKY is poisoned; need to be mindful of HP or find an Antidote.
- Consider pathing carefully due to maze-like structure.

## Agent Strategy & Ideas
### Active/Available Agents:
1.  **Level Cap Compliance Agent** (`level_cap_compliance_checker`): Defined. Checks Pokémon levels against current cap.
2.  **Item Finder Agent** (`item_finder_agent`): Defined. Locates items/buildings in towns. Value re-evaluation needed for current tasks (forest exploration).
3.  **Viridian Forest Navigator** (`viridian_forest_navigator`): Defined. Analyzes Viridian Forest map data to suggest navigation paths. (Consider using for current forest exploration).

## Lessons Learned & Strategy Refinements
-   **Trust Game State**: GSI is absolute truth for dynamic data (NPCs, items, map connections reachability).
-   **Pathing**: Double-check tile types (especially ledges) before committing to a path. NPCs can block movement. Repeatedly trying to move onto a blocking NPC or through a dialogue loop is inefficient.
-   **Critical Path**: Prioritize objectives that unblock main progression.
-   **Efficiency**: Plan longer movement sequences. Avoid repeated interactions if the first attempt yields no new info. Record failed interaction attempts.
-   **Hypothesis Testing**: Form hypotheses, test systematically, document failures and attempt counts.
-   **Route 22**: Was a detour. Path to Pewter is North from Viridian City via Route 2 / Viridian Forest. (Old Man unblocked).
-   **Mart Exit (Viridian)**: Exits to (30,21) outside Mart. WKG/Marker updated.
-   **Route 1 Ledge Navigation**: Cannot move 'up' onto a ledge from lower ground.
-   **Viridian Forest Gate Warp**: The warp at (5,1) in the South Gate was impassable from (5,2). Used (6,1) successfully. (5,1) might be an exit-only from the forest side or require a different approach.
-   **NPC Interaction**: If an NPC dialogue repeats and no battle/event occurs, do not re-interact. Mark and move on. (e.g., Viridian Forest Youngster ID 1). (Failed interaction attempts: 3).
-   **Pathing to Trainer Tips Sign (Viridian Forest (19,46))**: Multiple attempts (Turns 900-905) due to misjudging obstacles and Pikachu's position. Need more careful short-range pathing.

## World Knowledge Graph (WKG) Best Practices
- Record inter-map transitions (map boundary, warps) immediately using `manage_world_knowledge`.
- Use descriptive names and tags for nodes.
- Include exact coordinates and connection types.
- Note `destination_entry_point` for warps when known.

## Map Marker Best Practices
- Mark defeated trainers (☠️), used warps (🚪), key info NPCs (💡/💬), signs (ℹ️), obstacles (🚧), items given by NPCs (🎁).
- Use distinct emojis and concise labels. Delete redundant markers.

- Viridian Forest: Tile (16,32) confirmed impassable (blocked upward movement from (16,33)).

- Viridian Forest: Tile (6,33) confirmed impassable (blocked westward movement from (7,33)).

- Viridian Forest: Item Poké Ball at (2,32) appears to block movement despite GSI saying 'reachable'. Failed to move onto tile 2 times. (Turns 948, 949).

- Viridian Forest: Item Poké Ball at (26,12) blocked movement. SUCCESS: Interacting with 'A' (Turn 977) picked up Potion. Tile is now clear. This confirms some items need 'A' interaction, not just walking over.

## Reflection Insights (Turn 975)
- Item Interaction Hypothesis: If GSI says an item tile is 'reachable' but movement is blocked, I might be missing a specific interaction method (e.g., pressing 'A' on the tile, specific facing) rather than the item itself being an impassable barrier. Need to test this if direct movement fails again on an agent-suggested path over an item.
- New Agent Idea: 'Trainer Battle Strategist' - could analyze enemy teams and suggest matchups/moves for complex fights. Requires careful schema and prompt design.

- Viridian Forest: Agent `viridian_forest_navigator` path to (26,8) failed. Tile (26,8) is impassable. This is the second flawed path from this agent. (Turn 979).

- Viridian Forest: Tile (16,9) confirmed impassable (blocked westward movement from (17,9)).