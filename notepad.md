# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds (¥) for Potions and train SPROUT (Oddish) to an effective level for the Gym battle by exploring the route east of Pewter City.
*   **Tertiary Goal:** Systematically explore all 'Reachable Unseen Tiles' in new areas and investigate 'Reachable Undiscovered Map Connections' as they become available.

# Current Strategic Focus & Key Learnings
*   **Immediate Priority:** Successfully navigate out of Pewter City via the eastern map connection to explore the new route for resources. This is critical as current funds (¥156) and SPROUT's level (Lv7) are insufficient for Brock.
*   **Resource Gathering:** On any new route, prioritize battling trainers for money and EXP for SPROUT.
*   **Gym Preparation:** Re-evaluate readiness for Brock after SPROUT is leveled and funds are secured.
*   **Youngster Gym Escort Event (Recurring):** Youngster NPC (ID 5) has repeatedly initiated dialogue and forcibly moved the player to the Pewter Gym entrance. His final dialogue is "If you have the right stuff, go take on BROCK!". His position after this event varies (e.g., (18,19) then (36,17)). A robust strategy is needed to bypass his trigger zones or known locations when attempting to exit east.
*   **Path Execution & Discrepancies:** Errors in translating coordinate paths to button presses or misinterpreting current position can lead to 'unexpected jumps' or perceived XML vs. Screen discrepancies. Trust Game State and XML data as absolute truth over visual interpretations.
*   **Tile Traversal & Movement Rules:**
    *   **Ledges:** Confirmed one-way movement. Cannot move UP onto a ledge tile from a tile with a higher Y-coordinate. Example: Blocked from moving Up from (29,31) to ledge at (29,30) in Pewter City.
*   **Map Tile Changes:** Some map tiles in Pewter City have changed from 'impassable' to 'ground' (e.g., (27,15)-(27,18)) or vice-versa (e.g., (34,20), (35,15)-(35,16), (35,21), (35,22)) during gameplay. The triggers for these changes are unknown and require careful observation.

# Pokémon Center Tasks (Next Visit)
*   **Heal Pokémon.**
*   **Agent Management (CRITICAL):
    *   **Verify Active Agent List:** Confirm the actual list of currently active custom agents via PC. Previous attempts to delete `advanced_pathfinder_agent` and `direct_pathing_agent` failed as they were not found.
    *   **Low-Usage Agent Review & Update:** Re-evaluate `item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`. Improve their system prompts to include full game context (Pokemon Yellow Legacy Hard Mode rules, level caps, etc.) or delete to free slots.
    *   **Update `npc_interaction_planner_agent` prompt:** Instruct it to provide a path to the interaction spot if possible, or clarify its limitations.
    *   **Update `map_analyzer_agent` prompt:** Emphasize providing paths as sequences of navigable coordinates and suggest breaking very long paths into segments.
    *   **Investigate `exploration_planner_agent`:** Review its prompt for robustness, especially concerning ledges, and check its Python code if possible, given its previous failure. If unfixable, delete.
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
*   **Meticulous Tile-by-Tile Verification (ABSOLUTE PRIORITY):** Before *any* movement segment, consult map memory (XML) and verify `navigable="true"` and `type` of *every single tile*. **XML is sole truth for player movement, overriding visual cues or screen logs.** Trust Game State and XML data as absolute truth over visual interpretations during movement.
*   **Short, Verifiable Segments:** Path segments MUST be short (3-5 tiles max or single clear areas), especially in dense/unfamiliar locations. Each chunk 100% confirmed navigable from XML *before* execution. Break down longer paths.
*   **Use `move_validator_agent` (CRITICAL):** Before executing *any* planned path segment longer than a single step, use `move_validator_agent` to confirm path validity against the map XML. This is essential to prevent wasted turns.
*   **Re-validate After Interruptions:** If a validated path fails or is interrupted, DO NOT assume the remainder is valid. Re-validate from the new position or break the remaining path into smaller, individually validated segments.
*   **Proactive `map_analyzer_agent` Use:** For complex routes or finding paths between known points (especially after a few manual attempts with short segments fail), use `map_analyzer_agent` instead of repeated failed self-plotted paths. Carefully translate its coordinate paths to button presses, possibly validating in chunks.
*   **Navigable `navigation_goal_coordinates`:** Ensure `navigation_goal_coordinates` always target a navigable tile, not an NPC or impassable tile.
*   **Map Marker Usage (IMMEDIATE & ABSOLUTE):** *Immediately* mark confirmed dead ends/impassable tiles (🚫), key navigational turns/points (📍), important warps (🚪, with destination), defeated trainers (☠️), and event-triggering/blocking NPCs (❗ or ℹ️) after discovery/use. Ensure NPC location markers are updated based on the *latest* Game State Information.
*   **Pikachu Interaction:** Account for turning mechanic if moving onto Pikachu's tile from a non-facing direction.
*   **`navigable="false"` is Absolute:** If XML shows `navigable="false"`, it is IMPASSABLE by player. Trust this attribute explicitly.
*   **Full Path Execution:** When a multi-step path is validated, provide the *entire* sequence of button presses in the `buttons_to_press` array for that turn. Partial execution leads to path desynchronization and wasted turns.

# Recent Events (Pewter City - Pathing Focus)
*   **Current Location:** (28,19) facing Up. Pikachu at (28,20). Super Nerd (ID 3) at (28,18) blocks path North.
*   **Pathing Challenges:** Multiple pathing attempts within Pewter City (to Super Nerd at (27,26) and eastern exit) failed due to unexpected impassable tiles and NPC blockers. Known impassable tiles include: (27,24), (32,13), (30,24), (31,25), (18,22), (14,22), (23,18), (12,22), (18,15), (23,24), (23,17), (19,20), (19,19), (26,18), (35,26) (ground but impassable), (19,21) (wall), (34,20), (35,15), (35,16), (35,21), (35,22).
*   **NPC Blockers:** Youngster (ID 5) at (36,17) blocks row 17. Super Nerd (ID 3) at (28,18) blocks row 18 and is on an impassable tile.

# Agent Ideas Brainstorm (To Action at PC)
*   `route_progress_analyzer_agent`: Analyzes a new route for key features. (Consider defining)
*   `risk_assessor_agent`: Evaluates risk of major battles. (Consider defining)
*   `scripted_event_tracker_agent`: Attempts to predict/analyze scripted NPC events. System Prompt Idea: "You are a Scripted Event Tracker. Input: player map/pos, description of unexpected NPC interaction/movement. Analyze this and `map_xml_string`. Output JSON: likely trigger (tile, LoS), NPC ID/name, event sequence summary, implications (new blocks, unlocks), recurrence. Output Schema: `{"type":"object","properties":{"event_name":{"type":"string"},"trigger_description":{"type":"string"},"npc_involved_id":{"type":"integer","nullable":true},"npc_involved_name":{"type":"string","nullable":true},"event_sequence_summary":{"type":"string"},"implications":{"type":"string"},"is_recurring_event":{"type":"boolean"}},"required":["event_name","trigger_description","event_sequence_summary","implications","is_recurring_event"]}` (Consider defining)
*   `boulder_puzzle_solver_agent`: Assists with boulder puzzles. (Consider defining or discarding)

*   **Map Tile Change (Pewter City, Turn 3956):** Tile (35,23) changed from 'ground' to 'impassable' while moving.

# Recent Events & Learnings (Continued)
*   **Youngster Gym Escort Event (Recurring - Turn 3961):** Youngster NPC (ID 5) intercepted me again near the eastern side of Pewter City while I was at (38,19). He repeated his dialogue ("You're a trainer right? BROCK's looking for new challengers! Follow me!" then "If you have the right stuff, go take on BROCK!") and forcibly moved me, this time to (30,19) facing Left. His final position after this event is listed as (36,17) in the game state. This recurring event is a major impediment to exiting east and requires a more robust circumvention strategy. The trigger seems to be proximity to him when he is in his 'guide' mode near the eastern part of the city.