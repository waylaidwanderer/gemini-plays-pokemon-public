# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv8 (11/28 HP, **POISONED**, EXP: 530/800 to Lv9) | Moves: THUNDERSHOCK, GROWL, QUICK ATTACK, THUNDER WAVE
2. SPROUT (ODDISH): Lv6 (23/23 HP, EXP: 179) | Moves: TACKLE, POISONPOWDER

## Game Mechanics & Rules Summary
- Battle Style: Set. No items in battle. Level caps apply (Current: 12 for 0 badges).
- HMs: Forgettable, menu-use, not PC-storable.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses, unlimited enemy PP.
- EXP. All obtainable without special requirements.
- Poison: 1 HP lost per 4 steps outside battle.
- STAT Experience: Significant stat boosts from battling/leveling.
- PC Log Off: Saves game.
- CUT: Bug-type HM.
- Evolution: By training.
- Status Conditions: SLP (AWAKENING), BRN (BURN HEAL), PSN (ANTIDOTE), FRZ (ICE HEAL), PAR (PARLYZ HEAL).
- Wild Battle Escapes: Speed-dependent. If lead Pokémon's Speed >= wild's, escape is guaranteed. Otherwise, chance increases with attempts.
- Pokémon Nicknaming: Always do it when prompted.

## Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable. Check XML `type` attribute.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger like exit mats/gatehouses). Specific warps can be impassable tiles themselves (e.g. Viridian Forest South Gate north warp at (5,1)).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only. Cannot move 'up' onto a ledge tile from lower ground. To jump down, be on higher ground adjacent to the ledge, move onto the ledge tile.
- **NPC Interaction & Blocking**: 
    - NPCs can block paths. Player cannot move onto a tile occupied by a stationary NPC if it's the first step of a path or by pressing in their direction when adjacent and facing them. (Failed attempts: Youngster ID2, 2 times by movement).
    - Interacting with 'A' when adjacent and facing an NPC can initiate dialogue or battle if movement fails.
    - Dialogue loops cannot be broken by re-interacting.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.
- **Item Interaction**: Some items on the ground (Poké Ball sprites) require pressing 'A' while facing them to pick up; walking over them may not work and can block movement. (Confirmed with Potion at (26,12), Turn 977).

## Type Matchup Discoveries (Verified)
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

## Key NPCs & Info Log (Condensed)
- Youngster (Route 1, (6,27)): Gave Potion (used).
- Youngster (Route 1, (16,14)): Explained STAT Experience.
- Girl (Viridian School, (4,6)): CUT is Bug HM.
- Girl (Viridian School, (5,6)): Pokémon evolve by training.
- Old Man (Viridian City, now (20,14)): Path to Route 2 unblocked after coffee. Gave catching tutorial. No longer blocks path.
- Viridian Mart Clerk: Sells Poké Balls after Oak's Parcel delivery.
- Youngster (Viridian Forest, (17,44)): Dialogue 'They're out for POKéMON fights!'. Does not battle on 'A' interaction or by walking onto tile. (Attempted interaction 3 times - dialogue only). Marked with 💬.

## Current Area Focus: Viridian Forest (Map ID 51)
- Objective: Find the North exit to Route 2. SPARKY is poisoned and low on HP; Potions are scarce.
- Strategy: Prioritize exit. Battle trainers only if necessary or highly advantageous (like current battle for SPROUT EXP).

## Agent Strategy & Ideas
### Defined Agents:
1.  **Level Cap Compliance Agent** (`level_cap_compliance_checker`): Checks Pokémon levels against current cap.
2.  **Item Finder Agent** (`item_finder_agent`): Locates items/buildings in towns. Limited use in current forest environment.
3.  **Viridian Forest Navigator** (`viridian_forest_navigator`): DELETED due to consistent unreliability in Viridian Forest.
4.  **Trainer Battle Strategist** (`trainer_battle_strategist`): Analyzes teams for battle strategy.

### New Agent Ideas (To Be Defined Later):
- EXP Tracker / Grinding Spot Agent: To identify good training locations and track EXP gains. (Idea: Turn 1077)

## Lessons Learned & Strategy Refinements
-   **Trust Game State**: GSI is absolute truth for dynamic data (NPCs, items, map connections reachability).
-   **Pathing**: Double-check tile types (especially ledges and known impassables) before committing to a path. NPCs can block movement. Repeatedly trying to move onto a blocking NPC or through a dialogue loop is inefficient. Record failed interaction attempts.
-   **Item Interaction**: Some items require 'A' button interaction (Confirmed: Potion at (26,12)). Hypothesis: Item at (2,32) may also require 'A' button. (Test deferred due to SPARKY's HP).
-   **Critical Path**: Prioritize objectives that unblock main progression (e.g., forest exit).
-   **Efficiency**: Plan longer movement sequences. Avoid repeated interactions if the first attempt yields no new info. Record failed interaction attempts.
-   **Hypothesis Testing**: Form hypotheses, test systematically, document failures and attempt counts.
-   **Route 22**: Was a detour. Path to Pewter is North from Viridian City via Route 2 / Viridian Forest.
-   **Healing**: Be proactive with healing, especially with poison. Don't wait until critical HP if Potions are available and the situation allows.
-   **Agent Reliability**: Be critical of agent outputs, especially if an agent has a history of failures. Verify paths against map memory or use manual navigation as a backup.

## World Knowledge Graph (WKG) Best Practices
- Record inter-map transitions (map boundary, warps) immediately using `manage_world_knowledge`.
- Use descriptive names and tags for nodes.
- Include exact coordinates and connection types.
- Note `destination_entry_point` for warps when known.

## Map Marker Best Practices
- Mark defeated trainers (☠️), used warps (🚪), key info NPCs (💡/💬), signs (ℹ️), obstacles (🚧), items given by NPCs (🎁), items requiring 'A' interaction (🅰️).
- Use distinct emojis and concise labels. Delete redundant markers (e.g., if XML already clearly states impassable).

## Specific Tile Discoveries (Viridian Forest)
- (16,32) impassable (blocked upward from (16,33)).
- (6,33) impassable (blocked westward from (7,33)).
- (31,6) impassable (blocked westward from (32,6)).
- (32,35) impassable (blocked southward from (32,34)).
- (16,9) impassable (blocked westward from (17,9)).
- (26,8) impassable (agent path failed).
- Item at (2,32) - GSI says 'reachable'. Movement blocked (2 attempts). Hypothesis: Needs 'A' interaction. (Marked 🚧, will change to 🅰️ if hypothesis is correct after testing).