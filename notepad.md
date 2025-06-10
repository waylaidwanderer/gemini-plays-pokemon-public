# Pokédex & Badges
*   Badges: Boulder Badge
*   Pokedex: 10/151 (Target: Complete)

# Current Team & Training Focus (Strategic Notes)
*   BELLA (GLOOM Lv21): (66/66 HP) | Moves: STUN SPORE (30 PP), ACID (29 PP), LEECH SEED (10 PP), ABSORB (25 PP)
*   ZAPPY (PIKACHU Lv17): (50/50 HP) | Moves: THUNDERSHOCK (30 PP), DOUBLE TEAM (15 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP)
*   NINA (NIDORAN♀ Lv12): (36/36 HP) | Moves: GROWL (40 PP), DOUBLE KICK (30 PP), POISON STING (35 PP), BITE (25 PP). Keep for Ground/Poison typing.
*   ECHO (ZUBAT Lv11): (30/30 HP) | Moves: LEECH LIFE (25 PP), SUPERSONIC (20 PP), GUST (35 PP). Flying type coverage.
*   LUNA (CLEFAIRY Lv11): (37/37 HP) | Moves: POUND (35 PP), GROWL (40 PP), WATER GUN (25 PP), MEGA PUNCH (20 PP).
*   SIR (PARAS Lv13): (34/34 HP) | Moves: STUN SPORE (30 PP), ABSORB (25 PP), LEECH LIFE (25 PP), POISONPOWDER (35 PP).

# Key Items & TMs (Strategic Notes)
*   OLD ROD x1
*   POKé BALL x5
*   TM34 (BIDE) x1 - Evaluate for team.
*   HP UP x1 - Used on ZAPPY.
*   RARE CANDY x1 - Save for strategic use.
*   MOON STONE x1 - Potential use on LUNA (Clefairy) or NINA (Nidoran♀) after evolution to Nidorina for Nidoqueen.
*   TOWN MAP x1
*   HELIX FOSSIL x1 - Obtained from Mt. Moon B2F.

# Current Location & Navigation Plan
*   **Current Location:** Route 3 (ID: 14) at (62,9) - Exploring grass for training/catches.
*   **Immediate Navigation Plan:** Continue exploring grass patches on Route 3, then proceed east towards Mt. Moon's eastern entrance.

# Current Goals
*   **Primary Goal:** Reach Cerulean City and obtain the Cascade Badge from Misty.
*   **Secondary Goal:** Train key team members (ZAPPY, BELLA, NINA) on Route 3 and the eastern part of Mt. Moon to prepare for Gym Leader Misty (Ace Starmie Lv21, Player Cap 21).
*   **Tertiary Goal:** Catch new Pokémon on Route 3 or within Mt. Moon if any are available and strategically beneficial.

# Gameplay Notes & Strategy
## Navigation & Exploration
*   The North map connection from Route 3 leads to the *lowest tier* of 'Route 4 (Before Mt. Moon)', forming a loop for upper Route 4/western Mt. Moon access.
*   When on Route 4 (Before Mt. Moon) upper tiers, navigate eastward by descending ledges.
*   **Path Planning in Notepad:** Actively use the notepad to *plan out* complex navigation paths *before* execution, especially for multi-step movements in unfamiliar terrain. Break down long paths into smaller, verifiable segments. This must be consistently applied (ref: critique on Route 3 navigation turns 8879-8884).
*   **Item Acquisition:** Key items like fossils, if pick-ups, will be visible item sprites on the map and listed in the `Map Sprites` section *after the trigger event*.
*   **`navigation_goal_coordinates` Warnings:** Pay close attention to system warnings about `navigation_goal_coordinates` being non-navigable. Understand the distinction between NPC sprite `reachable: yes` status and underlying map tile `navigable: false` status. An NPC on a non-navigable tile cannot be pathfinding target for movement, even if the sprite itself is marked reachable (interaction might still be possible if adjacent and facing).

## Battle Strategy
*   Improve precision in battle menu navigation.
*   Be mindful of type matchups and PP conservation. Internalize ROM hack type changes.
*   **Risk Assessment:** Avoid switching in Pokémon with critically low HP against opponents that can KO them. Prioritize running from battles when party HP is critical (unless training goals override).
*   **Healing Priority:** Prioritize reaching a Pokémon Center quickly if key Pokémon are critically injured and no immediate training/objective outweighs this.

## ROM Hack Specifics
*   **General Changes:** Old Rod (Viridian Mart), HMs forgettable/menu use, TMs repurchasable, Trade evos by level.
*   **Type Matchup Changes (CRITICAL TO MEMORIZE):** Ghost (Special) SE vs Psychic. Bug no longer SE vs Poison. Grass is 0.25x vs Poison/Flying (e.g., Zubat). Poison attacks NVE vs Zubat (Poison/Flying). Bug SE vs Poison (likely 2x, resulting in 4x vs Grass/Poison like Gloom).
*   **Stat Boosts:** Pikachu, Farfetch’d, Venomoth, Onix.
*   **Level Caps:** Misty (Starmie Lv21 -> Cap 21), Lt. Surge (Raichu Lv28 -> Player Cap 24).

## PC Interaction Notes
*   Pewter City PC is on the far right (east side) of the Pokecenter.
*   'SOMEONE's PC' for Pokémon Storage. 'Gem's PC' for Item Storage.

# Agent Development & Usage
*   **Current Agents (10/10):** `level_up_move_advisor_agent`, `next_battle_action_advisor_agent`, `exploration_prioritizer_agent`, `tm_learning_advisor_agent`, `objective_validator_agent`, `dungeon_navigator_agent`, `item_use_advisor_agent`, `trainer_data_logger_agent`, `gym_leader_strategist_agent`, `escape_route_planner_agent`.
*   **High Usage Agents to Monitor & Reduce Reliance:**
    *   `dungeon_navigator_agent` (107 uses): MASSIVELY REDUCE RELIANCE. Prioritize manual pathfinding for ALL short-to-medium paths. Break complex paths into small, verifiable segments. Always double-check agent output.
    *   `next_battle_action_advisor_agent` (24 uses): DRASTICALLY REDUCE RELIANCE. Make manual battle decisions for ALL common wild Pokémon and obvious scenarios.
*   **Agent Slot Management:** 10/10 agents defined. Candidates for deletion if a slot is needed: `item_use_advisor_agent` (1 use), `tm_learning_advisor_agent` (2 uses). Periodically review if these are providing sufficient value.
*   **`exploration_prioritizer_agent` Limitations:** Ensure its prompt correctly guides its Python code to prioritize `game_state_reachable_unseen_tiles_json` over map XML `navigable` status for those specific tiles.
*   **`objective_validator_agent` Potential Use:** Consider using to validate tile navigability for a `navigation_goal_coordinate` *before* setting it, especially if targeting an NPC on a tile that might be `navigable: false` in map XML.
*   **Agent Prompts:** Periodically review agent system prompts for clarity and to ensure they contain all necessary game-specific context if not passed via input (since agents are otherwise contextless).

# Agent Development & Usage Notes (Post-Critique Turn 8900)
*   **Gym Leader Strategist:** Utilize `gym_leader_strategist_agent` before challenging Misty to evaluate its effectiveness.
*   **Reduce Reliance:** Actively work to reduce reliance on `dungeon_navigator_agent` (current uses: 107) and `next_battle_action_advisor_agent` (current uses: 24). Make manual decisions where possible.
*   **Evaluate Low-Usage Agents:** Critically assess the value of `item_use_advisor_agent` (current uses: 1) and `tm_learning_advisor_agent` (current uses: 2). Delete if not providing significant benefit to free up agent slots if new agents are to be defined.

# Completed Objectives & Discoveries
*   Defeated Brock, obtained Boulder Badge.
*   Explored parts of Route 3 and Mt. Moon 1F, B1F, B2F.
*   Exited Mt. Moon (western exit) onto Route 4 (Before Mt. Moon).
*   Confirmed Route 3 (North) to Route 4 (Before Mt. Moon) (South) map connection forms a loop.
*   Deposited WIGGLES (Caterpie Lv4) into PC Box 3. Withdrew SIR (Paras Lv13) from PC Box 1.
*   Healed party at Mt. Moon Pokecenter.
*   Obtained Helix Fossil from Mt. Moon B2F after defeating Super Nerd (ID 1).
*   Successfully navigated from Route 4 (Before Mt. Moon) to Route 3.

# Trainer Battle Intel
*Self-correction: Be more precise with Trainer IDs and locations when logging. Verify against Game State if unsure.*
## Route 3 Trainers
*   Youngster (ID 2) at (Route 3, 11,7) - Defeated.
*   Youngster (ID 3) at (Route 3, 15,5) - Defeated.
*   Cool Trainer F (ID 4) at (Route 3, 17,10) - Defeated.
*   Youngster (ID 5) at (Route 3, 20,6) - Defeated.
*   Youngster (ID 7) at (Route 3, 23,10) - Non-battling (dialogue only).
*   Youngster (ID 8) at (Route 3, 25,7) - Defeated.
*   Cool Trainer F (ID 9) at (Route 3, 34,11) - Defeated.
## Mt. Moon 1F Trainers
*   Bug Catcher (ID 6) at (Mt Moon 1F, 8,25) - Defeated.
*   Lass (Cool Trainer F, ID 5) at (Mt Moon 1F, 17,24) - Defeated.
*   Super Nerd (ID 4) at (Mt Moon 1F, 25,32) - Defeated.
*   Bug Catcher (ID 8) at (Mt Moon 1F, 32,29) - Defeated.
*   Lass (Cool Trainer F, ID 3) at (Mt Moon 1F, 31,5) - Defeated.
*   Youngster (ID 2) at (Mt Moon 1F, 14,17) - Defeated.
*   Hiker (ID 1) at (Mt Moon 1F, 6,8) - Defeated.
*   Youngster (ID 7) at (Mt Moon 1F, 31,28) - Non-battling (gives dialogue: "This cave leads to CERULEAN CITY!").
## Mt. Moon B2F Trainers
*   Rocket Grunt (ID 3) at (Mt Moon B2F, 16,23) - Defeated. ("Darn it all! My associates won't stand for this!")
*   Rocket Grunt (ID unknown) at (Mt Moon B2F, approx. 28,18) - Defeated. Used Rattata Lv13, Zubat Lv13.
*   Super Nerd (ID 1, sprite MTMOONB2F_SUPER_NERD) at (Mt Moon B2F, 13,9) - Defeated. Pokémon: GRIMER Lv12, VOLTORB Lv12, MAGNEMITE Lv12. Guarded fossils, took Dome Fossil after player took Helix Fossil.
*   Super Nerd (ID 4, sprite MTMOONB2F_ROCKET2) at (Mt Moon B2F, 30,12) - UNDEFEATED / CURRENTLY UNREACHABLE. Dialogue ("If you find a fossil, give it to me and scram!") was a pre-battle taunt. May or may not be relevant now that a fossil is obtained.
*   Rocket Grunt (ID 5, sprite MTMOONB2F_ROCKET3) at (Mt Moon B2F, 30,18) - Non-battling / Dialogue Loop. Bypassed.
## Route 4 (Before Mt. Moon) Trainers
*   Cool Trainer F (ID 1, sprite ROUTE4_COOLTRAINER_F1) on Route 4 (Before Mt. Moon) - Conclusively determined to be non-battling or already defeated. Numerous interaction attempts (turns 8841-8859) failed due to her constant movement and non-responsiveness. No longer a target for battle.

# Navigation Rules & Insights
*   NPCs on `navigable: false` tiles are impassable physical obstacles, even if defeated or non-battling. Their tile will remain `navigable: false` in map memory.
*   Ledge tiles marked `navigable="true"` can be occupied (e.g., by jumping down onto them), but upward movement onto a ledge from below is prevented by game physics, even if the tile's `navigable` attribute is true. The game's movement denial takes precedence over the XML's `navigable` flag for directional traversal of ledges from below.
*   Mt. Moon 1F: Tile (8,19) is impassable, blocking direct southward movement from (8,18).
*   **Segmented Dungeons (CRITICAL - REINFORCED):** Complex dungeons like Mt. Moon are NOT single, continuous maps per floor. They are composed of *multiple, often isolated segments on the exact same floor level*. Access to these different segments is *exclusively* via specific warps. Systematically explore each available warp from your current segment to discover connections to other segments or floors.
*   **1x1 Warp Activation:** Be more consistent with 1x1 warp activation, especially considering Pikachu's position. Stepping off and then back on is the reliable method if unsure.

# Self-Correction & Critique Learnings
*   Path Planning: Meticulously examine map data (`map_xml_string`/annotated screen) *before* committing to movement. Identify clear, navigable corridors. Break down navigation into smaller, verifiable segments. If a path is blocked, backtrack to a known navigable area and re-evaluate the entire route, considering completely different approaches.
*   Prioritize Healing: When party health is critical across multiple Pokémon, finding a Pokémon Center becomes the absolute top priority over other exploration or objectives, unless a very specific, short-term, high-value objective can be completed first.
*   Trust Game State: Information like `reachable: no` for NPCs/warps should be treated as authoritative. Avoid wasting turns trying to interact with or path to targets marked as currently inaccessible.

# Gameplay Reminders (Post-Reflection Turn 8367)
*   **Reachable Unseen Tiles List:** Always use the *current* list from the Game State Information for exploration planning. This list is dynamic and can change frequently.
*   **Navigation Goal Coordinates:** Ensure `navigation_goal_coordinates` are always confirmed `navigable: true` in the map XML or are part of the current 'Reachable Unseen Tiles' list from Game State to avoid pathing errors.

*   **`objective_validator_agent` Potential Use:** Consider using to validate tile navigability for a `navigation_goal_coordinate` *before* setting it, especially if targeting an NPC on a tile that might be `navigable: false` in map XML, even if the sprite is `reachable: yes`.
*   **Agent Prompts:** Periodically review agent system prompts for clarity and to ensure they contain all necessary game-specific context if not passed via input (since agents are otherwise contextless).

*   Super Nerd (ID 1) at (Route 3, 58,12) - Non-battling (dialogue: "Whew... I better take a rest... Groan... That tunnel from CERULEAN takes a lot out of you!").