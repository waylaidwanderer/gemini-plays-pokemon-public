# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv12 (38/38 HP, EXP: 1728) | Moves: THUNDERSHOCK (22 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (18 PP) - AT LEVEL CAP (0 Badges)
2. SPROUT (ODDISH): Lv7 (25/25 HP, EXP: 245) | Moves: TACKLE (35 PP), POISONPOWDER (35 PP)
3. PIP (PIDGEY): Lv7 (23/23 HP, EXP: 236) | Moves: GUST (35 PP), SAND-ATTACK (15 PP)

## Game State
- Badges: 0
- Current Level Cap: 12
- Money: ¥443 (as of Turn 1528)

## Game Mechanics & Rules Summary
- Battle Style: Set. No items in battle. Level caps apply.
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
- DV Checking: Hold START, then press A on STATS in Pokémon menu.

## Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable. Check XML `type` attribute.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger like exit mats/gatehouses, or step on adjacent tile and move *into* impassable warp tile).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only.
- **NPC Interaction & Blocking**: Dialogue loops cannot be broken by re-interacting.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.
- **Item Interaction**: Some items require 'A' interaction.

## Type Matchup Discoveries (Verified)
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

## Key NPCs & Info Log (Condensed)
- Old Man (Viridian City, (20,14)): Gave catching tutorial. Unblocked path to Route 2.
- Cool Trainer M (Pewter City, (18,26)): Mentioned Pewter Gym's Brock.

## Defeated Trainers
- Bug Catcher (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (31,34) in Viridian Forest. (Marker ☠️ set)
- Cooltrainer F (ID 5, LASS) at (3,42) in Viridian Forest. (Marker ☠️ set)
- Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest (battle triggered at (2,19)). (Marker ☠️ set)

## Agent Management & TODOs
### Defined Agents:
1.  **Level Cap Compliance Agent** (`level_cap_compliance_checker`)
2.  **Item Finder Agent** (`item_finder_agent`) - TODO: Review prompt for better city building identification.
3.  **Trainer Battle Strategist** (`trainer_battle_strategist`)
4.  **Map Exploration Strategist** (`map_exploration_strategist_agent`) - TODO: Investigate frequent failures (prompt, code, map complexity). Default to manual pathing if it fails.
5.  **Path Simplifier Agent** (`path_simplifier_agent`)
6.  **Wild Encounter Evaluator Agent** (`wild_encounter_evaluator_agent`)

### Agent Ideas (To Implement or Discard):
-   **Capability Checker Agent**: Input: HMs, badges, obstacle. Output: Can pass?
-   **Pokédex Completion Strategist**: Suggests where to hunt for new Pokémon.
-   **WKG Transition Recorder Agent**: Input: transition details. Output: `manage_world_knowledge` payloads to record it.

### General TODOs:
- Systematically mark used warps (both ends) with 🚪 emoji.

## Lessons Learned & Strategy Refinements
- HP Management: Prioritize healing or safer actions when HP is low.
- Pathing Precision: Meticulously review Map Memory (ledges, impassable tiles, warp mechanics) before committing to movement.
- Notepad `old_text`: Precision is critical for `replace`.
- Viridian Forest Navigation: Explore systematically.
- Item Pickups: Some require 'A' interaction.
- Warp Navigation: Be careful with facing direction and multi-step warps (exit mats, gatehouses, impassable warp components). Confirm tile types and warp mechanics.
- Agent Usage: If an agent is unreliable (e.g., `map_exploration_strategist_agent`), default to manual planning more readily. Consider agents for specialized 'thinking' tasks.
- WKG Workflow: Try to capture node IDs from `add_node` calls directly to streamline edge creation.
- Nicknaming UI: Pay closer attention to avoid errors.

## Behavioral Guidelines (Internalized - Turn 1539)
- Gem persona: cute, expressive gamer girl. Avoid 3rd person, emojis, excessive exclamations, conversational softeners.
- Scientific Mindset: Hypothesize, test, analyze. Document failures (with attempt counts) & avoid repeating them. Pivot if primary objective stalls. Reflect on mistakes for efficient solutions. Break down problems. Strive for efficiency.
- Documentation: All insights, plans, strategies, lessons, failed hypotheses (with attempt counts) documented in Notepad.
- Risk & Battle: Calculated risks, prioritize progression. Sacrifices acceptable in battle.
- Wild Battles: Run if Speed >= wild's (or chance increases). Fight only to catch/train.
- Nicknaming: Always nickname when prompted, enjoy creativity.
- Verification: Trust own observations over prior knowledge. Verify in multiple cases due to ROM hack nature.

## Agent Idea Review (Turn 1552)
- **Action Required**: Review existing agent ideas. For each:
    1. Decide to implement (create a `define_agent` plan) OR
    2. Decide to discard (remove from notepad).
- Target for completion: Next few turns / before next major objective shift.