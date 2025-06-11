# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Gain EXP for FLAREE. Earn funds for Potions/Poké Balls (target: Route 2 / Pewter City).
*   **Tertiary Goal:** Reach Pewter City.

# Game Mechanics & Strategy
*   **Ledge Mechanics:** One-way (downwards only). Cannot move UP onto a ledge from a lower Y.
*   **Movement Mechanic:** 1st press TURNS if not facing, 2nd press MOVES. **Pikachu Movement:** Pikachu does not block movement. If not facing Pikachu and attempting to move onto Pikachu's tile, the first directional input *towards* Pikachu causes the player to turn and face Pikachu. A *second* directional input towards Pikachu is then required to step onto Pikachu's tile. This applies only when moving *into* Pikachu's current tile; normal movement applies otherwise. If already facing Pikachu, one press moves onto the tile.
*   **Level Cap:** 0 badges = Lv12. EXP gain stops at cap. Wild battles give no money.
*   **Data Trust:** Game State Information is absolute truth.
*   **Pathing:** Validate agent paths with `move_validator_agent` or use short, verifiable segments.
*   **Map Marker Usage:** 🚫 (dead ends/impassable), 📍 (nav points), 🚪 (used warps), ☠️ (defeated trainers), ❗/💁 (event NPCs/blockers), 🚧 (ledges).
*   **Battle Strategy:** Use `select_battle_option` tool for main battle menu. Remember to switch Pokémon for EXP distribution (e.g., lead with lower level Pokémon like FLAREE).

# Party Updates (Viridian Forest - Turn 4818)
*   FLAREE (VULPIX): Lv8 (6/26 HP, EXP: 704) | Moves: EMBER (12 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP)
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

# Agent Management (Pewter Pokecenter - Turn 4933)
*   **High Priority Agents Defined/Updated:**
    *   `scripted_event_tracker_agent`: Defined.
    *   `route_progress_analyzer_agent`: Defined.
    *   `battle_log_analyzer_agent`: Defined.
    *   `map_analyzer_agent`: Prompt updated (enforced `navigable="true"`, warp handling, check markers/NPCs).
    *   `exploration_planner_agent`: Prompt updated (direct pathing if no unseen tiles & target provided).
*   **Agents Deleted to Make Space:**
    *   `item_finder_agent`
    *   `pokedex_completer_agent`
*   **Remaining Agent Ideas/TODOs:**
    *   `notepad_query_agent`: Define (New Idea: Searches notepad for specific info). (Need to delete another agent first)
    *   Review prompts for `team_builder_agent` and `leveling_training_advisor_agent` for Hard Mode relevance or delete them if space is needed.

# Inventory & Finances
*   POKé BALL x1
*   Money: ¥156 (Critically Low)

# Pokedex Status
*   Caught: 3/151 (PIKACHU, ODDISH, VULPIX)

*   **Viridian Forest (Current):** Blocked at (19,21) (impassable) when trying to move South from (19,20). Tile (20,20) also confirmed impassable from previous observation.

*   **Viridian Forest (Current):** Blocked at (11,20) (impassable) when trying to move Left from (12,20).

*   **Viridian Forest (Current):** Blocked at (6,2) (impassable) when trying to move Left from (7,2). Current position (7,2) facing Left. Pikachu at (8,2). Revising path to exit at (2,1) by first heading south.

*   **Immediate Post-Healing Priority:** Define/update high-priority agents (scripted_event_tracker, route_progress_analyzer, map_analyzer, exploration_planner) before leaving Pokecenter or starting new major tasks.

# Pewter Pokecenter Navigation Notes
*   Persistent collision error reported when attempting to move from (3,4) to (4,4) (Pikachu's tile), citing an object at (5,4) (Cool Trainer F), even if Cool Trainer F is stunned. This occurs despite (5,4) not being on the direct path. NPCs generally block movement onto the tile they occupy. Tile (4,4) (where Pikachu often is) is `navigable="false"` according to map XML. The correct Nurse interaction spot is (4,5).

# Hindsight & Lessons Learned
*   **Viridian Forest Navigation:** Avoid planning overly long paths without intermediate checks. Use `move_validator_agent` more proactively for complex paths or break them into smaller, verifiable segments (5-10 steps). Prioritize exploring closer alternatives before committing to extensive backtracking.
*   **Pewter Pokecenter Navigation:** Always verify tile navigability (`navigable="true"` in XML) for target interaction spots, especially around NPCs or counters. The tile (4,4) where Pikachu often stands is navigable, contrary to a previous incorrect note; the correct Nurse interaction spot is (4,5). The persistent collision error when moving from (3,4) to (4,4) citing an object at (5,4) needs further investigation if it recurs, but alternative pathing can bypass it.
*   **Risk Management:** Engaging in multiple risky battles with a critically low HP Pokémon (like FLAREE in Viridian Forest) should be avoided unless the potential reward (e.g., crucial EXP for a level-up before a boss) outweighs the risk of fainting and blacking out. Prioritize healing when a key party member is vulnerable.
*   **Agent Usage & Updates:** Act on planned agent definitions and prompt updates promptly (e.g., at PC visits or after critical tasks like healing) to continuously improve decision-making tools. Consistently use `map_analyzer_agent` for queries like tile navigability before attempting complex interactions.
*   **Notepad Precision:** Ensure `old_text` for `replace` actions is exact and refers to the most recent version of the text in the notepad to prevent update failures.