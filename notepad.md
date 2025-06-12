# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv12 (38/38 HP, EXP: 1728) | Moves: THUNDERSHOCK (22 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (18 PP) - AT LEVEL CAP (0 Badges)
2. SPROUT (ODDISH): Lv7 (25/25 HP, EXP: 245) | Moves: TACKLE (35 PP), POISONPOWDER (35 PP)
3. PIP (PIDGEY): Lv7 (23/23 HP, EXP: 236) | Moves: GUST (35 PP), SAND-ATTACK (15 PP)

## Game State
- Badges: 0
- Current Level Cap: 12 (Next: 21 after 1st badge)

## Current Financial Status & Needs
- Money: ¥33 (Critically Low!)
- Needs: Earn Pokedollars for Potions, Poké Balls, other essentials.

## Training Priorities
- SPROUT (ODDISH): Lv7 -> Needs significant training for Brock (Rock/Ground).
- PIP (PIDGEY): Lv7 -> Needs training.
- SPARKY (PIKACHU): At cap, less effective vs Brock.

## Game Mechanics & Rules Summary
- Battle Style: Set. No items in battle. Level caps apply.
- HMs: Forgettable, menu-use, not PC-storable. CUT is Bug-type.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses, unlimited enemy PP.
- EXP. All obtainable without special requirements.
- Poison: 1 HP lost per 4 steps outside battle.
- STAT Experience: Significant stat boosts from battling/leveling.
- PC Log Off: Saves game.
- Evolution: By training.
- Status Conditions: SLP (AWAKENING), BRN (BURN HEAL), PSN (ANTIDOTE), FRZ (ICE HEAL), PAR (PARLYZ HEAL).
- Wild Battle Escapes: Speed-dependent. If lead Pokémon's Speed >= wild's, escape is guaranteed. Otherwise, chance increases with attempts.
- Pokémon Nicknaming: Always do it when prompted.
- DV Checking: Hold START, then press A on STATS in Pokémon menu.

## Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger like exit mats/gatehouses).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only.
- **NPC Interaction & Blocking**: Dialogue loops cannot be broken by re-interacting. NPCs can block paths.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.
- **Item Interaction**: Some items require 'A' interaction.

## Type Matchup Discoveries (Verified)
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

## Defeated Trainers
- Bug Catcher (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (31,34) in Viridian Forest. (Marker ☠️ set)
- Cooltrainer F (ID 5, LASS) at (3,42) in Viridian Forest. (Marker ☠️ set)
- Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest (battle triggered at (2,19)). (Marker ☠️ set)

## Agent Management & TODOs
### Defined Agents:
1.  **Level Cap Compliance Agent** (`level_cap_compliance_checker`)
2.  **Item Finder Agent** (`item_finder_agent`)
3.  **Trainer Battle Strategist** (`trainer_battle_strategist`)
4.  **Map Exploration Strategist** (`map_exploration_strategist_agent`)
5.  **Path Simplifier Agent** (`path_simplifier_agent`)
6.  **Wild Encounter Evaluator Agent** (`wild_encounter_evaluator_agent`)

### Agent Development - Prioritized:
1.  **WKG Transition Recorder Agent**: Implement ASAP to ensure accurate WKG. (Defined this turn)
2.  **Capability Checker Agent**: Implement next. (Input: HMs, badges, obstacle. Output: Can pass?)

### Agent Development - Future Consideration:
-   **Pokédex Completion Strategist**: Suggests where to hunt for new Pokémon.

### Agent Review TODOs:
- `map_exploration_strategist_agent`: Review prompt/code due to frequent failures. Default to manual pathing if unreliable.
- `item_finder_agent`: Review prompt for better city building identification.
- `trainer_battle_strategist` & `wild_encounter_evaluator_agent`: Re-evaluate utility and prompts for current needs.

### General TODOs:
- Systematically mark used warps (both ends) with 🚪 emoji, noting destination map and coordinates/entry point, using WKG for reference.
- Actively seek info on Brock's Pokémon types/weaknesses.
- Be more proactive in using map markers for key NPC info (ℹ️) or strategic points.

## Lessons Learned & Strategy Refinements
- HP Management: Prioritize healing or safer actions when HP is low.
- Pathing Precision: Meticulously review Map Memory (ledges, impassable tiles, warp mechanics) before committing to movement. **Verify current map_id and position from Game State frequently, especially after warps, to avoid hallucinations.**
- Notepad `old_text`: Precision is critical for `replace`.
- Viridian Forest Navigation: Explore systematically.
- Item Pickups: Some require 'A' interaction.
- Warp Navigation: Be careful with facing direction and multi-step warps. Confirm tile types and warp mechanics. If an NPC is on a warp tile, try the other tile of a 2-wide warp or path around.
- Agent Usage: If an agent is unreliable, default to manual planning. Consider agents for specialized 'thinking' tasks or to automate repetitive WKG updates.
- WKG Workflow: Use the `wkg_transition_recorder_agent` once implemented. Capture node IDs from `add_node` calls to streamline edge creation if doing manually.
- Nicknaming UI: Pay closer attention to avoid errors.
- Failed Hypotheses: Document attempts. E.g., Exiting Pewter Mart - multiple attempts failed due to mislocating self or NPC blocking specific warp tiles. Current hypothesis: exit via (4,8) or (5,8) by careful pathing around NPCs.

## Behavioral Guidelines (Internalized)
- Gem persona: cute, expressive gamer girl. Avoid 3rd person, excessive exclamations, conversational softeners.
- Scientific Mindset: Hypothesize, test, analyze. Document failures (with attempt counts) & avoid repeating them. Pivot if primary objective stalls. Reflect on mistakes for efficient solutions. Break down problems. Strive for efficiency.
- Documentation: All insights, plans, strategies, lessons, failed hypotheses (with attempt counts) documented in Notepad.
- Risk & Battle: Calculated risks, prioritize progression. Sacrifices acceptable in battle.
- Wild Battles: Run if Speed >= wild's (or chance increases). Fight only to catch/train.
- Nicknaming: Always nickname when prompted, enjoy creativity.
- Verification: Trust own observations over prior knowledge. Verify in multiple cases due to ROM hack nature.

## Pewter Mart Exit Strategy (Post-Critique Turn 1651)
- **CRITICAL:** Verify `map_id` and `player_position` from Game State *every turn* before planning.
- Current plan: If on a warp tile, face correct direction and activate. If not, path to an unoccupied warp tile, prioritizing (5,8) if (4,8) is blocked or problematic.
- Document all failed exit attempts with specific reasons if identifiable.

## Lessons Learned & Strategy Refinements (Updates)
- Pewter Mart Exit Loop: MAJOR issue. Numerous failed attempts (conservatively 20+ turns) due to misreading location, NPC blocking, and flawed pathing. Must break this loop by careful verification and adaptive pathing.

## General TODOs (Additions)
- Review and revise prompts for `map_exploration_strategist_agent` and `item_finder_agent` based on critique of frequent failures.
- Implement `Capability Checker Agent` after reaching Pewter City and stabilizing.
- Prioritize earning money (currently ¥33) and training SPROUT (Lv7) & PIP (Lv7) once in Pewter City.