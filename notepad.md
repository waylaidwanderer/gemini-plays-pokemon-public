# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds (¥) for Potions and train SPROUT (Oddish) to an effective level for the Gym battle.
*   **Tertiary Goal:** Systematically explore all 'Reachable Unseen Tiles' in new areas and investigate 'Reachable Undiscovered Map Connections' as they become available.

# Current Strategic Focus
*   **Immediate Priority:** Exit Pewter City via the eastern map connection to explore the new route for resources.
*   **Resource Gathering:** On any new route, prioritize battling trainers for money and EXP for SPROUT.
*   **Gym Preparation:** Re-evaluate readiness for Brock after SPROUT is leveled and funds are secured.
*   **Continuous Learning:** Mark obstacles, learn from pathing failures, and adapt strategies.

# Pokémon Center Tasks (Next Visit)
*   **Heal Pokémon.**
*   **Agent Management (CRITICAL):
    *   **Verify Active Agent List:** Confirm the actual list of currently active custom agents via PC.
    *   **Low-Usage Agent Review:** Re-evaluate `item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`. Improve their prompts (ensure full game context like Pokemon Yellow Legacy Hard Mode rules, level caps, etc.) or delete to free slots.
    *   **Address 'Agent Ideas Brainstorm':** Make decisions on defining new agents (requires deletion if at limit) or explicitly discard these ideas.
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
*   **Meticulous Tile-by-Tile Verification (ABSOLUTE PRIORITY):** Before *any* movement segment, consult map memory (XML) and verify `navigable="true"` and `type` of *every single tile*. **XML is sole truth for player movement, overriding visual cues or screen logs.**
*   **Short, Verifiable Segments:** Path segments MUST be short (3-5 tiles max or single clear areas), especially in dense/unfamiliar locations. Each chunk 100% confirmed navigable from XML *before* execution. Break down longer paths.
*   **Use `move_validator_agent` (CRITICAL):** Before executing *any* planned path segment longer than a single step, use `move_validator_agent` to confirm path validity against the map XML. This is essential to prevent wasted turns.
*   **Re-validate After Interruptions:** If a validated path fails or is interrupted, DO NOT assume the remainder is valid. Re-validate from the new position or break the remaining path into smaller, individually validated segments.
*   **Proactive `map_analyzer_agent` Use:** For complex routes or finding paths between known points when manual pathing is difficult, use `map_analyzer_agent` instead of repeated failed self-plotted paths.
*   **Navigable `navigation_goal_coordinates`:** Ensure `navigation_goal_coordinates` always target a navigable tile, not an NPC or impassable tile.
*   **Map Marker Usage (IMMEDIATE & ABSOLUTE):** *Immediately* mark confirmed dead ends/impassable tiles (🚫), key navigational turns/points (📍), important warps (🚪), defeated trainers (☠️), and event-triggering/blocking NPCs (❗ or ℹ️) after discovery/use. Essential for spatial understanding.
*   **Pikachu Interaction:** Account for turning mechanic if moving onto Pikachu's tile from a non-facing direction.
*   **`navigable="false"` is Absolute:** If XML shows `navigable="false"`, it is IMPASSABLE by player. Trust this attribute explicitly.
*   **Full Path Execution:** When a multi-step path is validated, provide the *entire* sequence of button presses in the `buttons_to_press` array for that turn. Partial execution can lead to unintended consequences (e.g., game retaining and attempting the full validated path).

# Recent Events & Learnings (Pewter City)
*   **Pathing Challenges:** Multiple pathing attempts within Pewter City (to Super Nerd at (27,26) and eastern exit) failed due to unexpected impassable tiles (e.g., (27,24), (32,13), (30,24), (31,25), (18,22), (19,19)-(19,21), (14,22), (23,18), (12,22), (18,15), (23,24), (35,26), (23,17) Mart wall, (28,18) Super Nerd tile). This highlights the need for more careful pre-validation checks and shorter path segments.
*   **Youngster Gym Escort Event (Turns 3841-3865, 3881-3883, 3910-3912):** Youngster NPC (ID 5), previously a Gym Guide, initiated dialogue multiple times and forcibly moved the player. First, he moved the player from near the eastern exit to (12,19) in front of the Pewter Gym. After the player attempted to leave east again, he re-initiated dialogue and moved the player from (38,19) to (30,19). His final dialogue each time was "If you have the right stuff, go take on BROCK!". The Youngster (ID 5) is now located at (36,17) according to the game state, his original position blocking eastward travel along row 17.
*   **Strategy Shift (Reaffirmed):** Due to repeated pathing failures within Pewter City and the critical need for funds/EXP, the strategy remains to prioritize exploring the eastern 'Reachable Undiscovered Map Connection'.

# Pewter City Navigation Anomalies (Turn 3855)
*   **Unexpected Movement Jump:** During the execution of the `map_analyzer_agent`'s path on turn 3854, the 'Screens During Movement' log showed an unexplained jump from (20,22) to (22,23) when the intended move was to (20,23). This resulted in landing at (22,24) instead of the agent's target (20,23). This was likely a pathing execution error on my part or a misinterpretation of agent output, not a game glitch.
*   **XML vs. Screen Discrepancy:** The `map_xml_string` for Pewter City listed tile (13,13) as 'impassable' and `navigable="false"`. However, the 'Screens During Movement' log for turn 3854 clearly showed the player sprite on (13,13) and the tile visually appearing as navigable ground. **The map XML is the absolute source of truth for navigability; visual cues or screen logs can be misleading.**

# Critical Pathing Learnings (Turn 3860)
*   **`move_validator_agent` Path Retention:** The game may retain and attempt to execute the *full* path validated by `move_validator_agent`, even if only a partial button sequence is provided in the `buttons_to_press` for a turn. This can lead to unintended movements. Best practice is to re-validate or use very short, certain segments if a long path is broken, or ensure the full validated sequence is provided in one turn.

# Agent Ideas Brainstorm (To Action at PC)
*   `route_progress_analyzer_agent`: Analyzes a new route for key features. (Consider defining)
*   `risk_assessor_agent`: Evaluates risk of major battles. (Consider defining)
*   `scripted_event_predictor_agent`: Attempts to predict scripted events. (Consider defining or discarding)
*   `boulder_puzzle_solver_agent`: Assists with boulder puzzles. (Consider defining or discarding)

# Archived Learnings & Notes (Condensed)
*   Older battle logs, detailed early game event triggers, specific NPC dialogue not immediately relevant. Repel Mechanics: Lead Pokémon level must be *strictly greater* than wild Pokémon level. `exploration_planner` Misuse: Agent is strictly for 'Reachable Unseen Tiles', not for paths to known, seen tiles.

# Tile Traversal & Movement Rules
*   **Ledges:** Confirmed one-way movement. Cannot move UP onto a ledge tile from a tile with a higher Y-coordinate. Example: Blocked from moving Up from (29,31) to ledge at (29,30) in Pewter City (Turn 3894).