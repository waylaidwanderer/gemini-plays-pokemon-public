# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds (¥) for Potions and train SPROUT (Oddish) to an effective level for the Gym battle by exploring the route east of Pewter City.
*   **Tertiary Goal:** Systematically explore all 'Reachable Unseen Tiles' in new areas and investigate 'Reachable Undiscovered Map Connections' as they become available.

# Current Tactical Plan (Focus: Exiting Pewter City East)
1.  **Immediate:** Execute validated path to (20,22) to bypass western Pewter City blockages.
2.  **Next:** From (20,22), plan and validate a path to the eastern map connection at (40,18).
3.  **Contingency:** If further pathing issues arise, use `map_analyzer_agent` proactively to find routes to key intermediate points or the final exit.

# Key Learnings & Game Mechanics
*   **Youngster Gym Escort Event (Recurring & CRITICAL):** Youngster NPC (ID 5, usually at (36,17)) has a scripted event that triggers *precisely at or immediately adjacent to (38,19)* when approached from the west/south-west in eastern Pewter City. He escorts the player to the Pewter Gym entrance (12,19). His final position after the escort can vary (e.g., (36,17) or (18,19) temporarily), but the game state seems to revert him to (36,17) eventually. This event is a major impediment and requires pathing to strictly avoid (38,19) and its immediate vicinity, in addition to his resting spot at (36,17).
*   **Path Execution (CRITICAL):** When a multi-step path is validated (e.g., by `move_validator_agent` or derived from `map_analyzer_agent`), the *entire* sequence of button presses for that path segment MUST be provided in a single turn. Partial execution leads to desynchronization and movement failures.
*   **Map Tile Changes:** Some map tiles in Pewter City have changed type during gameplay.
    *   Previously: (27,15)-(27,18) changed to ground.
    *   (35,15-16,21-23) changed to impassable.
    *   Turn 3978: (27,17) and (27,18) changed from impassable to ground.
    *   Turn 3983: (34,20) changed from ground to impassable.
    *   Turn 3987: (35,20) changed from impassable to ground; (35,21), (35,22), (35,23) changed from ground to impassable.
    *   Turn 3991: (35,16) changed from ground to impassable.
    *   Turn 3995: (35,15) changed from ground to impassable.
    *   The triggers for these changes are unknown. Must be observant of conditions before changes.
*   **Ledge Mechanics:** Confirmed one-way movement (downwards only). Cannot move UP onto a ledge tile from a tile with a higher Y-coordinate (e.g., blocked from (29,31) to (29,30)).
*   **NPC Blockers:** Youngster (ID 5) at (36,17) makes his tile non-navigable. Super Nerd (ID 3) at (28,18) makes his tile non-navigable.
*   **Data Trust:** Game State Information (positions, NPC locations, tile navigability in XML) is the absolute source of truth, overriding visual interpretations, especially during or after complex movements or unexpected events.

# Navigation Strategy & Best Practices (MUST ADHERE)
*   **Proactive Agent Use:** For complex routes or finding paths between known points (especially after 1-2 manual attempts fail), use `map_analyzer_agent` *before* extensive manual trial-and-error. Trust its output but carefully translate coordinates to button presses.
*   **Segmented & Validated Paths:** Break down long paths (especially agent-provided ones) into shorter, manageable segments (e.g., 5-10 tiles or to key turns). Validate *each segment* with `move_validator_agent` before execution. Execute the *full button sequence* for each validated segment in one turn.
*   **Meticulous Tile Verification:** Before *any* movement, consult map memory (XML) and verify `navigable="true"` and `type` of target tiles. `navigable="false"` is absolute.
*   **NPC Circumvention:** For recurring blockers like Youngster (ID 5), use `map_analyzer_agent` to plot routes that definitively bypass known locations or (if identifiable) trigger zones.
*   **Map Marker Usage (IMMEDIATE & CONSISTENT):**
    *   🚫: Confirmed dead ends, impassable tiles/areas, NPC-blocked tiles.
    *   📍: Key navigational turns/points.
    *   🚪: Used warps (mark both entry and arrival, note destination).
    *   ☠️: Defeated trainers (name, location).
    *   ❗/💁: Event-triggering NPCs or significant static blockers (note ID, behavior).
    *   🚧: Ledges (note direction).
    *   Update NPC location markers based on *latest* Game State Information.
*   **Pikachu Interaction:** Account for turning mechanic if moving onto Pikachu's tile from a non-facing direction.

# Pokémon Center Tasks (Next Visit)
*   **Heal Pokémon.**
*   **Agent Management (CRITICAL):
    *   **Verify Active Agent List:** Confirm the actual list of currently active custom agents via PC. Previous attempts to delete `advanced_pathfinder_agent` and `direct_pathing_agent` failed as they were not found.
    *   **Action 'Agent Ideas Brainstorm':** Decide to define or discard each idea.
        *   `scripted_event_tracker_agent`: Define if slot available (High Priority).
        *   `route_progress_analyzer_agent`: Define if slot available (High Priority).
        *   `pewter_city_escape_planner_agent`: Define if slot available (Medium Priority).
        *   `map_tile_change_correlator_agent`: Consider defining or discard (Low Priority).
        *   `boulder_puzzle_solver_agent`: Discard for now.
        *   `risk_assessor_agent`: Discard for now.
    *   **Agent Updates/Deletions:**
        *   `map_analyzer_agent` prompt: Emphasize navigable coordinates, segmented paths.
        *   `npc_interaction_planner_agent` prompt: Instruct to provide path to interaction spot.
        *   `exploration_planner_agent`: Investigate prompt/code for ledges; fix or delete.
        *   Low-Usage Agents (`item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`): Update prompts with full game context (Hard Mode, level caps) or delete.
        *   `pathing_script_analyzer_agent`: Delete (not relevant to current playstyle).
*   **Financial Planning:** Re-assess funds and purchase Potions if affordable.

# Current Pokémon Status
*   SPROUT (ODDISH): Lv7 (25/25 HP, EXP: 262). Moves: TACKLE, POISONPOWDER.
*   SPBARKY (PIKACHU): Lv12 (39/39 HP, EXP: 1728). **AT LEVEL CAP (12).** Moves: THUNDERSHOCK, TAIL WHIP, QUICK ATTACK, THUNDER WAVE.

# Inventory & Finances
*   POKé BALL x2
*   Money: ¥156

# Hard Mode Rules & ROM Hack Changes (Summary)
*   Battle Style: Set. No items in battle. Level caps apply (current 0 badges: 12).
*   HMs: Forgettable, menu use, not PC storable. All 151 obtainable. Trade evos by level. Smarter AI. Tougher bosses. EXP. All early.

# Pewter City Navigation Saga (Summary)
*   Numerous attempts to exit east manually were blocked by previously unknown impassable tiles (e.g., X=19 wall, Y=22 wall, various individual tiles like (32,13), (30,24), (31,25), (35,26), (26,18)) and NPC blockers (Super Nerd at (28,18), Youngster at (36,17)).
*   The Youngster (ID 5) scripted escort event to the Gym is a major recurring obstacle, triggering multiple times when attempting to path east.
*   Map tiles have changed dynamically, requiring path adjustments (e.g., X=27 opening up, (34,20), (35,23) becoming impassable).
*   Key Learning: Proactive use of `map_analyzer_agent` for complex paths and strict adherence to full, validated path execution are essential.

*   **Agent Path Verification (CRITICAL LESSON):** `map_analyzer_agent` (and potentially other pathing agents) may occasionally generate paths containing non-navigable tiles. ALWAYS validate agent-provided paths with `move_validator_agent` before execution. If `map_analyzer_agent` is used, explicitly instruct it to ensure all path segments consist of `navigable="true"` tiles from the map XML. The validator correctly identified that a path from (12,19) to (14,26) via (12,15) included a step to the non-navigable tile (13,15).

*   **Agent Path Verification (RECURRING ISSUE - MORE DETAIL):** `map_analyzer_agent` has repeatedly provided paths containing non-navigable tiles (e.g., (13,15), (16,26), (19,21) for Pewter City paths to Pokémon Center, even when explicitly told to use navigable tiles). ALWAYS validate agent-provided paths with `move_validator_agent` before execution. When using `map_analyzer_agent`, explicitly instruct it to ensure ALL tiles in the generated path have `navigable="true"` in the map XML and to double-check its own output. The validator correctly identified these issues. This underscores the need for extreme caution with agent-generated paths and the importance of the validator.

*   **Agent Path Verification (RECURRING ISSUE - MORE DETAIL):** `map_analyzer_agent` has repeatedly provided paths containing non-navigable tiles (e.g., (13,15), (16,26), (19,21) for Pewter City paths to Pokémon Center, even when explicitly told to use navigable tiles). ALWAYS validate agent-provided paths with `move_validator_agent` before execution. When using `map_analyzer_agent`, explicitly instruct it to ensure ALL tiles in the generated path have `navigable="true"` in the map XML and to double-check its own output. The validator correctly identified these issues. This underscores the need for extreme caution with agent-generated paths and the importance of the validator.