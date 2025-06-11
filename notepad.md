# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Gain EXP for FLAREE. Earn funds for Potions/Poké Balls (target: Route 2 / Pewter City).
*   **Tertiary Goal:** Reach Pewter City.

# Game Mechanics & Strategy
*   **Ledge Mechanics:** One-way (downwards only). Cannot move UP onto a ledge from a lower Y.
*   **Movement Mechanic:** 1st press TURNS if not facing, 2nd press MOVES. (Pikachu rule is separate).
*   **Level Cap:** 0 badges = Lv12. EXP gain stops at cap. Wild battles give no money.
*   **Data Trust:** Game State Information is absolute truth.
*   **Pathing:** Validate agent paths with `move_validator_agent` or use short, verifiable segments.
*   **Map Marker Usage:** 🚫 (dead ends/impassable), 📍 (nav points), 🚪 (used warps), ☠️ (defeated trainers), ❗/💁 (event NPCs/blockers), 🚧 (ledges).
*   **Battle Strategy:** Use `select_battle_option` tool for main battle menu. Remember to switch Pokémon for EXP distribution (e.g., lead with lower level Pokémon like FLAREE).

# Party Updates (Post Pidgey Battle - Turn 4809)
*   FLAREE (VULPIX): Lv8 (6/26 HP, EXP: 645) | Moves: EMBER (14 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP)
*   SPBARKY (PIKACHU): Lv12 (38/39 HP, EXP: 1728) | Moves: THUNDERSHOCK (29 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP) (Level Cap Reached)
*   SPROUT (ODDISH): Lv12 (33/37 HP, EXP: 973) | Moves: TACKLE (30 PP), POISONPOWDER (35 PP), LEECH SEED (10 PP) (Level Cap Reached)

# Post-Viridian Forest Plan Notes
*   Immediately reorder party to lead with FLAREE after current battle/task.
*   Solidify plan for acquiring funds on Route 2/Pewter City: identify specific trainers to battle or item sale strategy.

# Key Journey Events & Map Discoveries
*   **Viridian Forest Training (Current):** SPROUT reached Lv12 cap. FLAREE gaining EXP from wild battles. Navigating towards northern exit.
*   **Pewter City Navigation:** Repeatedly blocked by Youngster escort event and dynamic tile changes. Learned to use `map_analyzer_agent` and validate paths. Pewter PC non-functional.
*   **Route 2:** Caught FLAREE (Vulpix). Navigated ledges.
*   **Viridian Forest (Previous):** Trained SPROUT to Lv12. Defeated Bug Catchers & Youngsters. Encountered several non-battling NPC blockers. Noted impassable tiles: (9,27), (11,27), (13,31), (19,21), (25,17), (27,18 sign), (28,45), (29,21), (15,47), (17,33 sign), (16,32), (20,36), Youngster (ID1) at (17,44) is a blocker.
*   **Viridian City Pokecenter Navigation:** Multiple attempts to reach Pokecenter due to ledges and impassable walls. Eventually succeeded.

# Agent & Pathing Notes
*   **`map_analyzer_agent` Issues:** Provided flawed paths multiple times (e.g., Turn 4706 to Viridian Pokecenter, Turn 4707 in Viridian Forest to (20,36), Turn 4707 path to (2,1)). Paths need strict validation (use `move_validator_agent`) or execution in smaller, verifiable segments. Prompt needs update (navigability, warps).
*   **`exploration_planner_agent` Limitation:** Failed to path to known exit when no unseen tiles (Turn 4698). Prompt needs update for direct pathing scenarios.
*   **Youngster Gym Escort Event (Pewter City):** Youngster NPC (ID 5, usually at (36,17)) triggers escort at/near (38,19) from west/south-west. Avoid trigger zone.

# Agent Management Plan (Next PC Visit)
*   **High Priority Agents to Define/Update:**
    *   `scripted_event_tracker_agent`: Define.
    *   `route_progress_analyzer_agent`: Define.
    *   `battle_log_analyzer_agent`: Define (New Idea: Parses battle text into structured summary).
    *   `notepad_query_agent`: Define (New Idea: Searches notepad for specific info).
    *   `map_analyzer_agent`: Critical prompt update (enforce `navigable="true"`, warp handling, check markers/NPCs).
    *   `exploration_planner_agent`: Prompt update (direct pathing if no unseen tiles & target provided).
*   **Medium Priority Agents to Review/Update/Delete:**
    *   Low-usage agents (`item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`): Review prompts for Hard Mode relevance or delete.
    *   `hm_usage_advisor_agent`: Define (for later game).
*   Consolidate all agent idea notes from other sections here.

# Inventory & Finances
*   POKé BALL x1
*   Money: ¥156 (Critically Low)

# Pokedex Status
*   Caught: 3/151 (PIKACHU, ODDISH, VULPIX)

*   **Viridian Forest (Current):** Blocked at (19,21) (impassable) when trying to move South from (19,20). Tile (20,20) also confirmed impassable from previous observation.

*   **Viridian Forest (Current):** Blocked at (11,20) (impassable) when trying to move Left from (12,20).

*   **Viridian Forest (Current):** Blocked at (6,2) (impassable) when trying to move Left from (7,2). Current position (7,2) facing Left. Pikachu at (8,2). Revising path to exit at (2,1) by first heading south.