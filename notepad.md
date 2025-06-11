# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds (¥) for Potions and train SPROUT (Oddish) to an effective level for the Gym battle by exploring Route 2 (south of Pewter City).
*   **Tertiary Goal:** Locate a functional Pokémon Center PC to perform critical agent management tasks.

# Current Tactical Plan
1.  **Current:** Continue training SPROUT (Oddish) on Route 2 by battling wild Pokémon. SPROUT's HP is currently 19/28.
2.  **Next:** If SPROUT's HP becomes critically low (e.g., below 10 HP or unable to withstand another likely hit), return to Pewter City Pokémon Center to heal.
3.  **Contingency:** During training, if SPROUT is at risk of fainting, switch to SPBARKY or FLAREE to finish the battle or run. Prioritize SPROUT's EXP gain but be more cautious about type disadvantages and low HP situations, especially against Fire-types like Vulpix.

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

# Pokémon Center Tasks (DEFERRED until functional PC found)
*   **Heal Pokémon (DONE).**
*   **Agent Management (CRITICAL - ON HOLD):
    *   **Verify Active Agent List:** Confirm the actual list of currently active custom agents via PC. Previous attempts to delete `advanced_pathfinder_agent` and `direct_pathing_agent` failed as they were not found.
    *   **Action 'Agent Ideas Brainstorm' (DECIDE & IMPLEMENT/DISCARD - ON HOLD):**
        *   `scripted_event_tracker_agent`: **Define** (High Priority). Tracks proximity to known scripted event trigger zones.
        *   `route_progress_analyzer_agent`: **Define** (High Priority). Tracks route completion, unbattled trainers (if data available).
        *   `pewter_city_escape_planner_agent`: **Discard for now**. A well-instructed `map_analyzer_agent` should suffice.
        *   `map_tile_change_correlator_agent`: **Define if possible** (Medium Priority). Attempts to find patterns in dynamic tile changes.
        *   `boulder_puzzle_solver_agent`: Discard for now.
        *   `risk_assessor_agent`: Discard for now.
    *   **Agent Updates/Deletions (IMPLEMENT - ON HOLD):**
        *   `map_analyzer_agent` prompt: **CRITICAL UPDATE** - Emphasize *MUST* check `navigable="true"` for *every* tile in path from `map_xml_string`. Paths with non-navigable tiles are unacceptable. Suggest generating long paths in segments.
        *   `npc_interaction_planner_agent` prompt: Update to provide path to interaction spot, not just the spot.
        *   `exploration_planner_agent`: Update prompt for strict navigability (`navigable="true"` for all tiles) and better ledge handling.
        *   Low-Usage Agents (`item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`): **Update prompts** with full game context (Hard Mode, level caps, current progression) or **delete** if still not useful.
        
        *   `advanced_pathfinder_agent` / `direct_pathing_agent`: **Verify existence and delete** if found and unused.
*   **Financial Planning (DEFERRED):** Re-assess funds and purchase Potions if affordable.

# Current Pokémon Status
*   SPROUT (ODDISH): Lv8 (19/28 HP, EXP: 378) | Moves: TACKLE (31 PP), POISONPOWDER (35 PP), LEECH SEED (8 PP)
*   SPBARKY (PIKACHU): Lv12 (39/39 HP, EXP: 1728). **AT LEVEL CAP (12).** ACCURACY Lowered. Moves: THUNDERSHOCK (29 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP)
*   FLAREE (VULPIX): Lv7 (24/24 HP, EXP: 343) | Moves: EMBER (25 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP)

# Inventory & Finances
*   POKé BALL x1
*   Money: ¥156

# Hard Mode Rules & ROM Hack Changes (Summary)
*   Battle Style: Set. No items in battle. Level caps apply (current 0 badges: 12).
*   HMs: Forgettable, menu use, not PC storable. All 151 obtainable. Trade evos by level. Smarter AI. Tougher bosses. EXP. All early.

# Pewter City Navigation Saga (Summary)
*   Numerous attempts to exit east manually were blocked by previously unknown impassable tiles (e.g., X=19 wall, Y=22 wall, various individual tiles like (32,13), (30,24), (31,25), (35,26), (26,18)) and NPC blockers (Super Nerd at (28,18), Youngster at (36,17)).
*   The Youngster (ID 5) scripted escort event to the Gym is a major recurring obstacle, triggering multiple times when attempting to path east.
*   Map tiles have changed dynamically, requiring path adjustments (e.g., X=27 opening up, (34,20), (35,23) becoming impassable).
*   Key Learning: Proactive use of `map_analyzer_agent` for complex paths and strict adherence to full, validated path execution are essential.

# Pokémon Center Notes
*   **Pewter City Pokémon Center PC (Visual: (9,3)):** Appears non-functional. Game state (Turn 4048) shows 'no background objects' in this Pokecenter, despite a visual PC. Attempting to interact with 'A' while at (9,4) facing up yielded no result. Unable to manage agents here. Will need to find another functional PC.

# Route 2 Encounters
*   Encountered wild Vulpix (Lv7) in grass patch on Route 2 (west side). Plan: Paralyze with THUNDER WAVE (SPBARKY), weaken with THUNDERSHOCK (SPBARKY), then attempt to catch with POKé BALL. Vulpix is a new Pokédex entry.

# Agent Ideas Brainstorm (From Mandatory Reflection - Deferred until functional PC)
*   `scripted_event_tracker_agent`: **Define** (High Priority). Tracks proximity to known scripted event trigger zones (e.g., Youngster escort in Pewter City (38,19)). Input: Player position, known trigger zones. Output: Warning if approaching trigger, suggested safe alternative path segments.
*   `route_progress_analyzer_agent`: **Define** (High Priority). Tracks route completion, unbattled trainers (if data available from game state/notes), and items yet to be collected on a route. Input: Current route ID, player notes on defeated trainers/collected items. Output: Summary of route progress, list of remaining objectives on route.
*   **Existing Agent Updates (Deferred until functional PC):**
    *   `map_analyzer_agent` prompt: **CRITICAL UPDATE** - Emphasize *MUST* check `navigable="true"` for *every* tile in path from `map_xml_string`. Paths with non-navigable tiles are unacceptable. Suggest generating long paths in segments. Incorporate explicit avoidance of known NPC trigger zones.
    *   `npc_interaction_planner_agent` prompt: Update to provide path to interaction spot, not just the spot itself. Consider NPC movement patterns if data becomes available.
    *   `exploration_planner_agent` prompt: Update for strict navigability (`navigable="true"` for all tiles) and better ledge handling (no upward ledge movement). Ensure it prioritizes unseen tiles that lead to undiscovered map connections or unvisited warps.
    *   Low-Usage Agents (`item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`): **Update prompts** with full game context (Hard Mode, level caps, current progression, specific ROM hack changes if known) or **delete** if still not useful after prompt improvements.
    
    *   `advanced_pathfinder_agent` / `direct_pathing_agent`: **Verify existence and delete** if found and unused.

# Route 2 Encounters
*   Encountered wild Vulpix (Lv7) in grass patch on Route 2 (west side at (2,7)). Plan: Paralyze with THUNDER WAVE (SPBARKY), weaken with THUNDERSHOCK (SPBARKY), then attempt to catch with POKé BALL. Vulpix is a new Pokédex entry. **Successfully caught Vulpix, named FLAREE.**

# Pokedex Status
*   Caught: 3/151 (PIKACHU, ODDISH, VULPIX)

# Pewter City Navigation Saga (Continued)
*   Turn 4192: Attempt to move Down from (14,32) to (14,33) in Pewter City was blocked as tile (14,33) is impassable. Required re-routing to reach southern exit.