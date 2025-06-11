# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds (¥) for Potions and train SPROUT (Oddish) to an effective level for the Gym battle.
*   **Tertiary Goal:** Systematically explore all 'Reachable Unseen Tiles' in new areas and investigate 'Reachable Undiscovered Map Connections' as they become available.

# Current Strategic Focus
*   **Immediate Priority:** Exit Pewter City via the eastern map connection to explore the new route.
*   **Resource Gathering:** On the new route, prioritize battling trainers to earn money (for Potions) and gain EXP for SPROUT.
*   **Gym Preparation:** Once SPROUT is adequately leveled (closer to cap) and funds are secured, re-evaluate readiness for Brock's Gym.
*   **Continuous Learning:** Mark impassable tiles and significant NPC locations/behaviors. Refine pathing strategies based on successes and failures.

# Pokémon Center Tasks (Next Visit)
*   **Heal Pokémon.**
*   **Agent Management (CRITICAL):
    *   **Verify Active Agent List:** Before any further agent deletions or definitions, I *must* check the PC to confirm the actual list of currently active custom agents. My notes about `advanced_pathfinder_agent` and `direct_pathing_agent` were incorrect as they weren't found.
    *   **Low-Usage Agent Review:** Re-evaluate `item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`. Improve their prompts/utility for active use (ensure prompts include full game context like Pokemon Yellow Legacy Hard Mode rules), or delete them to free up agent slots (currently at 10/10 limit, assuming no phantom agents).
    *   **Address 'Agent Ideas Brainstorm':** Make decisions on defining new agents (requires deletion of existing agent(s) if limit is met) or explicitly discard these ideas.
    *   Investigate `exploration_planner_agent` failure on Turn 3777 if it's to be relied upon.
*   **Financial Planning:** Re-assess funds and purchase Potions if affordable.

# Current Pokémon Status
*   SPROUT (ODDISH): Lv7 (25/25 HP, EXP: 262). Moves: TACKLE, POISONPOWDER.
*   SPBARKY (PIKACHU): Lv12 (39/39 HP, EXP: 1728). **AT LEVEL CAP (12).** Moves: THUNDERSHOCK, TAIL WHIP, QUICK ATTACK, THUNDER WAVE.

# Inventory & Finances
*   POKé BALL x2
*   Money: ¥156

# Hard Mode Rules & ROM Hack Changes (Summary)
*   Battle Style: Set. No items in battle. Level caps apply (current 0 badges: 12. Brock's Ace Onix Lv14 -> cap before Brock: 14).
*   HMs: Forgettable, menu use, not PC storable. All 151 obtainable. Trade evos by level. Smarter AI. Tougher bosses. EXP. All early.

# Navigation Strategy & Best Practices (CRITICAL - MUST ADHERE)
*   **Meticulous Tile-by-Tile Verification (ABSOLUTE PRIORITY):** Before *any* movement segment, consult map memory (XML) and verify `navigable="true"` and `type` of *every single tile*. XML is sole truth for player movement.
*   **Short, Verifiable Segments:** Path segments MUST be short (3-5 tiles max) or cover single, clear small areas, especially in dense or unfamiliar locations. Each chunk 100% confirmed navigable from XML *before* execution. Break down longer paths.
*   **Use `move_validator_agent` (CRITICAL):** Before executing *any* planned path segment longer than a single step, use `move_validator_agent` to confirm path validity against the map XML. This is essential to prevent wasted turns.
*   **Map Marker Usage (IMMEDIATE & ABSOLUTE):** *Immediately* mark confirmed dead ends/impassable tiles (🚫), key navigational turns/points (📍), important warps (🚪), defeated trainers (☠️), and event-triggering/blocking NPCs (❗ or ℹ️) after discovery/use. Essential for spatial understanding.
*   **Pikachu Interaction:** Account for turning mechanic if moving onto Pikachu's tile from a non-facing direction.
*   **`navigable="false"` is Absolute:** If XML shows `navigable="false"`, it is IMPASSABLE by player. Trust this attribute explicitly.
*   **Full Path Execution:** When a multi-step path is validated (e.g., by `move_validator_agent`), provide the *entire* sequence of button presses in the `buttons_to_press` array for that turn. Partial execution can lead to unintended consequences.
*   **Complex Route Planning:** For navigating complex areas or finding paths around multiple obstacles, consider using `map_analyzer_agent` to request a path between two known navigable points if direct pathing or `exploration_planner_agent` (for unseen tiles) is insufficient. Always break down long suggested paths into smaller, verifiable segments.

# Recent Events & Learnings (Pewter City)
*   **Pathing Challenges:** Multiple pathing attempts within Pewter City (to Super Nerd at (27,26) and eastern exit) failed due to unexpected impassable tiles (e.g., (27,24), (32,13), (30,24), (31,25), (18,22), (19,19)-(19,21), (14,22), (23,18)). This highlights the need for more careful pre-validation checks and shorter path segments.
*   **Youngster Gym Escort Event (Turns 3841-3865):** Youngster NPC (ID 5), previously a Gym Guide, initiated dialogue multiple times and forcibly moved the player, eventually to (12,19), directly in front of the Pewter Gym. His final dialogue was "If you have the right stuff, go take on BROCK!". The Youngster (ID 5) is now located at (36,17) according to the game state, his original position blocking eastward travel along row 17.
*   **Strategy Shift (Reaffirmed):** Due to repeated pathing failures within Pewter City and the critical need for funds/EXP, the strategy remains to prioritize exploring the eastern 'Reachable Undiscovered Map Connection'.

# Pewter City Navigation Anomalies (Turn 3855)
*   **Unexpected Movement Jump:** During the execution of the `map_analyzer_agent`'s path on turn 3854, the 'Screens During Movement' log showed an unexplained jump from (20,22) to (22,23) when the intended move was to (20,23). This resulted in landing at (22,24) instead of the agent's target (20,23).
*   **XML vs. Screen Discrepancy:** The `map_xml_string` for Pewter City listed tile (13,13) as 'impassable' and `navigable="false"`. However, the 'Screens During Movement' log for turn 3854 clearly showed the player sprite on (13,13) and the tile visually appearing as navigable ground. This suggests an inaccuracy in the provided XML for that specific tile.

# Critical Pathing Learnings (Turn 3860)
*   **`move_validator_agent` Path Retention:** The game may retain and attempt to execute the *full* path validated by `move_validator_agent`, even if only a partial button sequence is provided in the `buttons_to_press` for a turn. This can lead to unintended movements, warps, or blocks if the full path isn't re-evaluated after partial execution or if the game state changes. Best practice is to re-validate or use very short, certain segments if a long path is broken.

# Agent Ideas Brainstorm
*   `route_progress_analyzer_agent`: Analyzes a new route to identify key features like trainer density, item locations, wild Pokémon levels, and potential dead ends based on initial exploration and map XML. Helps prioritize exploration paths on new routes.
*   `risk_assessor_agent`: Evaluates the risk of a major battle (Gym, Rival) based on current party, level cap, opponent data, and available healing items. Suggests if it's advisable to proceed or if more preparation is needed.
*   `scripted_event_predictor_agent`: Attempts to predict or analyze scripted events based on NPC dialogue, unusual NPC movements, and current game state. Output could be hypotheses about triggers or outcomes.
*   `boulder_puzzle_solver_agent`: Assists in solving boulder puzzles by analyzing boulder positions, switches, and barriers on the map XML.

# Archived Learnings & Notes (Condensed)
*   Older battle logs, detailed early game event triggers, specific NPC dialogue not immediately relevant. Repel Mechanics: Lead Pokémon level must be *strictly greater* than wild Pokémon level. `exploration_planner` Misuse: Agent is strictly for 'Reachable Unseen Tiles', not for paths to known, seen tiles.