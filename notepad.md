# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Gain EXP for FLAREE in Viridian Forest. Earn funds for Potions/Poké Balls on Route 2 / in Pewter City.
*   **Tertiary Goal:** Reach Pewter City.

# Key Learnings & Game Mechanics
*   **Youngster Gym Escort Event (Pewter City):** Youngster NPC (ID 5, usually at (36,17)) triggers escort at/near (38,19) from west/south-west. Avoid trigger zone.
*   **Path Execution:** Full validated button sequences for path segments MUST be provided in one turn.
*   **Map Tile Changes (Pewter City):** Various tiles changed type. Triggers unknown.
*   **Ledge Mechanics:** One-way (downwards only). Cannot move UP onto a ledge from a lower Y.
*   **NPC Blockers (Pewter City):** Youngster (ID 5) at (36,17), Super Nerd (ID 3) at (28,18) make their tiles non-navigable.
*   **Data Trust:** Game State Information is absolute truth.
*   **Movement Mechanic:** 1st press TURNS if not facing, 2nd press MOVES. (Pikachu rule is separate).
*   **Blocked Movement Message:** Refers to tile player *ends up facing* after a move/turn.
*   **Level Cap:** 0 badges = Lv12. EXP gain stops at cap. Wild battles give no money.

# Navigation Strategy & Best Practices
*   **Proactive Agent Use:** Use `map_analyzer_agent` for complex routes.
*   **Segmented & Validated Paths:** Break long paths, validate with `move_validator_agent`, execute full segment.
*   **Meticulous Tile Verification:** Check `navigable="true"` and `type` in XML.
*   **Map Marker Usage:** 🚫 (dead ends/impassable), 📍 (nav points), 🚪 (used warps), ☠️ (defeated trainers), ❗/💁 (event NPCs/blockers), 🚧 (ledges).

# Pokémon Center Tasks (DEFERRED until functional PC found)
*   **Agent Management (CRITICAL - ON HOLD):**
    *   Verify Active Agent List.
    *   **Define/Update/Delete Agents (DECIDE & IMPLEMENT/DISCARD - ON HOLD):**
        *   `scripted_event_tracker_agent`: **Define** (High Priority).
        *   `route_progress_analyzer_agent`: **Define** (High Priority).
        *   `map_tile_change_correlator_agent`: **Define if possible** (Medium Priority).
        *   `battle_outcome_predictor_agent`: **Define** (High Priority).
        *   `full_notepad_organizer_agent`: **Define** (High Priority).
        *   `dynamic_blocker_pathing_agent`: **Define** (Medium Priority).
        *   `hm_usage_advisor_agent`: **Define** (Medium Priority, for later).
        *   `map_analyzer_agent` prompt: **CRITICAL UPDATE** - Emphasize `navigable="true"`, segmented paths.
        *   `npc_interaction_planner_agent` prompt: Update for path to interaction spot.
        *   `exploration_planner_agent` prompt: Update for strict navigability, ledge handling, direct pathing to known coords if no unseen.
        *   Low-Usage Agents (`item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`): **Update prompts** or **delete**.
        *   `advanced_pathfinder_agent` / `direct_pathing_agent`: Verify existence and delete if found/unused. Remove references from notepad if confirmed non-existent.

# Inventory & Finances
*   POKé BALL x1
*   Money: ¥156

# Pokedex Status
*   Caught: 3/151 (PIKACHU, ODDISH, VULPIX)

# Party Updates (Latest)
*   SPROUT (ODDISH): Lv12 (33/37 HP, EXP: 973) | Moves: TACKLE, POISONPOWDER, LEECH SEED (Level Cap Reached)
*   SPBARKY (PIKACHU): Lv12 (39/39 HP, EXP: 1728) | Moves: THUNDERSHOCK, TAIL WHIP, QUICK ATTACK, THUNDER WAVE (Level Cap Reached)
*   FLAREE (VULPIX): Lv7 (24/24 HP, EXP: 343) | Moves: EMBER, TAIL WHIP, QUICK ATTACK

# Key Journey Events & Map Discoveries
*   **Pewter City Navigation:** Repeatedly blocked by Youngster escort event and dynamic tile changes. Learned to use `map_analyzer_agent` and validate paths. Pewter PC non-functional.
*   **Route 2:** Caught FLAREE (Vulpix). Navigated ledges.
*   **Viridian Forest:** Trained SPROUT to Lv12. Defeated Bug Catchers & Youngsters. Encountered several non-battling NPC blockers. Noted impassable tiles: (9,27), (11,27), (13,31), (19,21), (25,17), (27,18 sign), (28,45), (29,21), (15,47), (17,33 sign), (16,32).
*   **Viridian City Pokecenter Navigation:** Multiple attempts to reach Pokecenter due to ledges and impassable walls. Eventually succeeded.
*   **Pathing Issues:** `map_analyzer_agent` path to Viridian Pokecenter was flawed or incompletely executed. `exploration_planner_agent` failed to path to known exit (Turn 4698).
*   **Current Location:** Viridian Forest (16,33), blocked trying to move to (16,32 - impassable).

# Notepad Strategy
*   Use `append` for new info. Use `overwrite` for full cleanups when feasible and content is prepared.