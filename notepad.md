# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds (¥) for Potions and train SPROUT (Oddish) to an effective level for the Gym battle.
*   **Tertiary Goal:** Systematically explore all 'Reachable Unseen Tiles' in new areas and investigate 'Reachable Undiscovered Map Connections' as they become available.

# Current Strategic Focus
*   **Immediate Priority:** Exit Pewter City via the eastern map connection to explore the new route for resources. This is critical as current funds (¥156) and SPROUT's level (Lv7) are insufficient for Brock.
*   **Resource Gathering:** On any new route, prioritize battling trainers for money and EXP for SPROUT.
*   **Gym Preparation:** Re-evaluate readiness for Brock after SPROUT is leveled and funds are secured.
*   **Continuous Learning:** Mark obstacles, learn from pathing failures, and adapt strategies. Utilize `map_analyzer_agent` for complex paths after initial short-segment manual attempts fail.

# Pokémon Center Tasks (Next Visit)
*   **Heal Pokémon.**
*   **Agent Management (CRITICAL):
    *   **Verify Active Agent List:** Confirm the actual list of currently active custom agents via PC. Previous attempts to delete `advanced_pathfinder_agent` and `direct_pathing_agent` failed as they were not found.
    *   **Low-Usage Agent Review & Update:** Re-evaluate `item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`. Improve their system prompts to include full game context (Pokemon Yellow Legacy Hard Mode rules, level caps, etc.) or delete to free slots.
    *   **Update `npc_interaction_planner_agent` prompt:** Instruct it to provide a path to the interaction spot if possible, or clarify its limitations.
    *   **Update `map_analyzer_agent` prompt:** Emphasize providing paths as sequences of navigable coordinates and suggest breaking very long paths into segments.
    *   **Investigate `exploration_planner_agent`:** Review its prompt for robustness, especially concerning ledges, and check its Python code if possible, given its previous failure.
    *   **Address 'Agent Ideas Brainstorm':** Make decisions on defining new agents (requires deletion if at limit) or explicitly discard these ideas. Prioritize `scripted_event_tracker_agent` and `route_progress_analyzer_agent` if slots become available.
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
*   **Proactive `map_analyzer_agent` Use:** For complex routes or finding paths between known points (especially after a few manual attempts with short segments fail), use `map_analyzer_agent` instead of repeated failed self-plotted paths. Carefully translate its coordinate paths to button presses, possibly validating in chunks.
*   **Navigable `navigation_goal_coordinates`:** Ensure `navigation_goal_coordinates` always target a navigable tile, not an NPC or impassable tile.
*   **Map Marker Usage (IMMEDIATE & ABSOLUTE):** *Immediately* mark confirmed dead ends/impassable tiles (🚫), key navigational turns/points (📍), important warps (🚪, with destination), defeated trainers (☠️), and event-triggering/blocking NPCs (❗ or ℹ️) after discovery/use. Essential for spatial understanding.
*   **Pikachu Interaction:** Account for turning mechanic if moving onto Pikachu's tile from a non-facing direction.
*   **`navigable="false"` is Absolute:** If XML shows `navigable="false"`, it is IMPASSABLE by player. Trust this attribute explicitly.
*   **Full Path Execution:** When a multi-step path is validated, provide the *entire* sequence of button presses in the `buttons_to_press` array for that turn. Partial execution can lead to unintended consequences (e.g., game retaining and attempting the full validated path from an incorrect starting point/facing).

# Recent Events & Learnings (Pewter City)
*   **Pathing Challenges & NPC Blocking:** Multiple pathing attempts within Pewter City (to Super Nerd at (27,26) and eastern exit) failed due to unexpected impassable tiles (e.g., (27,24), (32,13), (30,24), (31,25), (18,22), (19,19)-(19,21), (14,22), (23,18), (12,22), (18,15), (23,24), (35,26), (23,17) Mart wall, (28,18) Super Nerd tile, (19,19) latest). NPCs, particularly Youngster (ID 5), have also dynamically blocked paths.
*   **Youngster Gym Escort Event (Recurring):** Youngster NPC (ID 5), previously a Gym Guide, initiated dialogue multiple times and forcibly moved the player. First, he moved the player from near the eastern exit to (12,19) in front of the Pewter Gym. After the player attempted to leave east again, he re-initiated dialogue (e.g., at (38,19) then (36,18)) and moved the player again, ultimately to (12,19) near the Gym. His final dialogue each time was "If you have the right stuff, go take on BROCK!". The Youngster (ID 5) is now located at (36,17) according to the game state, his original position blocking eastward travel along row 17. Another instance of this Youngster appeared at (18,19) after the latest escort, blocking that tile.
*   **`map_analyzer_agent` Path Execution Issue (Turn 3854):** The agent's suggested path from (12,19) to (20,23) resulted in an unexpected jump from (20,22) to (22,23), landing at (22,24). This requires careful review of how agent paths are translated and executed.
*   **XML vs. Screen Discrepancy (Turn 3854):** Tile (13,13) listed as 'impassable' and `navigable="false"` in XML, but screen log showed player on it. **XML is the absolute source of truth.**
*   **Strategy Shift (Reaffirmed):** Due to repeated pathing failures within Pewter City and the critical need for funds/EXP, the strategy remains to prioritize exploring the eastern 'Reachable Undiscovered Map Connection'.

# Agent Ideas Brainstorm (To Action at PC)
*   `route_progress_analyzer_agent`: Analyzes a new route for key features. (Consider defining)
*   `risk_assessor_agent`: Evaluates risk of major battles. (Consider defining)
*   `scripted_event_tracker_agent`: Attempts to predict/analyze scripted NPC events. System Prompt Idea: "You are a Scripted Event Tracker. Input: player map/pos, description of unexpected NPC interaction/movement. Analyze this and `map_xml_string`. Output JSON: likely trigger (tile, LoS), NPC ID/name, event sequence summary, implications (new blocks, unlocks), recurrence. Output Schema: `{"type":"object","properties":{"event_name":{"type":"string"},"trigger_description":{"type":"string"},"npc_involved_id":{"type":"integer","nullable":true},"npc_involved_name":{"type":"string","nullable":true},"event_sequence_summary":{"type":"string"},"implications":{"type":"string"},"is_recurring_event":{"type":"boolean"}},"required":["event_name","trigger_description","event_sequence_summary","implications","is_recurring_event"]}` (Consider defining)
*   `boulder_puzzle_solver_agent`: Assists with boulder puzzles. (Consider defining or discarding)

# Tile Traversal & Movement Rules
*   **Ledges:** Confirmed one-way movement. Cannot move UP onto a ledge tile from a tile with a higher Y-coordinate. Example: Blocked from moving Up from (29,31) to ledge at (29,30) in Pewter City (Turn 3894).

# Archived Learnings & Notes (Condensed)
*   Older battle logs, detailed early game event triggers, specific NPC dialogue not immediately relevant.
*   Repel Mechanics: Lead Pokémon level must be *strictly greater* than wild Pokémon level.
*   `exploration_planner` Misuse: Agent is strictly for 'Reachable Unseen Tiles', not for paths to known, seen tiles.