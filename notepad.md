# Pokédex & Badges
*   Badges: Boulder Badge
*   Pokedex: 10/151 (Target: Complete)

# Current Team & Training Focus (Strategic Notes)
*   BELLA (GLOOM Lv21): (66/66 HP) | Moves: STUN SPORE (26 PP), ACID (21 PP), LEECH SEED (10 PP), ABSORB (18 PP)
*   ZAPPY (PIKACHU Lv17): (18/50 HP) | Moves: THUNDERSHOCK (19 PP), DOUBLE TEAM (15 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP)
*   NINA (NIDORAN♀ Lv12): (14/36 HP) | Moves: GROWL (40 PP), DOUBLE KICK (26 PP), POISON STING (35 PP), BITE (25 PP). Keep for Ground/Poison typing.
*   ECHO (ZUBAT Lv11): (6/30 HP) | Moves: LEECH LIFE (25 PP), SUPERSONIC (20 PP), GUST (31 PP). Flying type coverage.
*   LUNA (CLEFAIRY Lv11): (37/37 HP) | Moves: POUND (35 PP), GROWL (40 PP), WATER GUN (25 PP), MEGA PUNCH (20 PP).
*   SIR (PARAS Lv13): (24/34 HP) | Moves: STUN SPORE (30 PP), ABSORB (25 PP), LEECH LIFE (25 PP), POISONPOWDER (35 PP).

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
*   **Current Location:** Mt. Moon 1F (ID: 59) at (17,8) - Party critically injured.
*   **Immediate Navigation Plan:** Follow Phase 1 of 'Mt. Moon Navigation Strategy (Post-Critique - DETAILED EXIT PLAN)' to reach warp (26,16) on Mt. Moon 1F.

# Current Goals (Revised Turn 8701 - POST-CRITIQUE)
*   **Primary Goal:** Reach the Pokémon Center on Route 4 (Before Mt. Moon) to heal the party. (ABSOLUTE TOP PRIORITY)
*   **Secondary Goal:** Exit Mt. Moon and reach Route 4.
*   **Tertiary Goal:** Reach Cerulean City and train key team members (especially ZAPPY and BELLA) to Lv20-21 to challenge Gym Leader Misty (Ace Starmie Lv21, Player Cap 21).

# Gameplay Notes & Strategy
## Navigation & Exploration
*   **CRITICAL:** Trust the **annotated screen** for immediate obstacles over map memory if there's a conflict.
*   The North map connection from Route 3 leads to the *lowest tier* of 'Route 4 (Before Mt. Moon)', forming a loop for upper Route 4/western Mt. Moon access.
*   When on Route 4 (Before Mt. Moon) upper tiers, navigate eastward by descending ledges.
*   **Path Planning in Notepad:** Actively use the notepad to *plan out* complex navigation paths *before* execution, not just for post-mortem analysis or general strategy. Break down long paths into smaller, verifiable segments in the notepad.
*   **Multi-Tile Warps:** Be consistently aware of 2-step activation (onto tile, then into boundary/direction).
*   **Item Acquisition:** Key items like fossils, if pick-ups, will be visible item sprites on the map and listed in the `Map Sprites` section *after the trigger event*. Do not interact with empty ground tiles expecting items.

## Battle Strategy
*   Improve precision in battle menu navigation.
*   Be mindful of type matchups and PP conservation. Internalize ROM hack type changes.
*   **Risk Assessment:** Avoid switching in Pokémon with critically low HP against opponents that can KO them. Prioritize running from battles when party HP is critical.
*   **Healing Priority:** Prioritize reaching a Pokémon Center quickly if key Pokémon are critically injured.

## ROM Hack Specifics
*   **General Changes:** Old Rod (Viridian Mart), HMs forgettable/menu use, TMs repurchasable, Trade evos by level.
*   **Type Matchup Changes (CRITICAL TO MEMORIZE):** Ghost (Special) SE vs Psychic. Bug no longer SE vs Poison. Grass is 0.25x vs Poison/Flying (e.g., Zubat). Poison attacks NVE vs Zubat (Poison/Flying). Bug SE vs Poison (likely 2x, resulting in 4x vs Grass/Poison like Gloom).
*   **Stat Boosts:** Pikachu, Farfetch’d, Venomoth, Onix.
*   **Level Caps:** Misty (Starmie Lv21 -> Cap 21), Lt. Surge (Raichu Lv28 -> Player Cap 24).

## PC Interaction Notes
*   Pewter City PC is on the far right (east side) of the Pokecenter.
*   'SOMEONE's PC' for Pokémon Storage. 'Gem's PC' for Item Storage.

# Agent Development & Usage
*   **Current Agents (10/10):** `level_up_move_advisor_agent`, `next_battle_action_advisor_agent`, `exploration_prioritizer_agent`, `tm_learning_advisor_agent`, `objective_validator_agent`, `dungeon_navigator_agent`, `team_composition_advisor_agent`, `item_use_advisor_agent`, `trainer_data_logger_agent`, `gym_leader_strategist_agent`.
*   **High Usage Agents to Monitor & Reduce Reliance:**
    *   `dungeon_navigator_agent` (106 uses): MASSIVELY REDUCE RELIANCE. Prioritize manual pathfinding for ALL short-to-medium paths. Break complex paths into small, verifiable segments. Always double-check agent output.
    *   `next_battle_action_advisor_agent` (24 uses): DRASTICALLY REDUCE RELIANCE. Make manual battle decisions for ALL common wild Pokémon and obvious scenarios (e.g., running with a critically injured party).
*   **Agent Slot Management:** 10/10 agents defined. Candidates for deletion if a slot is needed: `team_composition_advisor_agent`, `tm_learning_advisor_agent`, `item_use_advisor_agent` (due to low usage).
*   **`exploration_prioritizer_agent` Limitations:** Ensure its prompt correctly guides its Python code to prioritize `game_state_reachable_unseen_tiles_json` over map XML `navigable` status for those specific tiles.

# Future Agent Ideas (Brainstorming)
*   **Escape Route Planner Agent:** (PRIORITY TO DEFINE AFTER PARTY IS HEALED) Given current map and party health, prioritizes finding the *absolute fastest* way to a known Pokémon Center, considering items like Escape Ropes/Dig if available. For dire situations.

# Completed Objectives & Discoveries
*   Defeated Brock, obtained Boulder Badge.
*   Explored parts of Route 3 and Mt. Moon 1F, B1F, B2F.
*   Exited Mt. Moon (western exit) onto Route 4 (Before Mt. Moon).
*   Confirmed Route 3 (North) to Route 4 (Before Mt. Moon) (South) map connection forms a loop.
*   Deposited WIGGLES (Caterpie Lv4) into PC Box 3. Withdrew SIR (Paras Lv13) from PC Box 1.
*   Healed party at Mt. Moon Pokecenter (most recently turn 7866).
*   Obtained Helix Fossil from Mt. Moon B2F after defeating Super Nerd (ID 1).

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
*   Cool Trainer F (ID 1) at (Route 4 Before Mt. Moon, 10,9) - **UNENGAGEABLE / NOT DEFEATED.** (Player choice to avoid).

# Navigation Rules & Insights
*   NPCs on `navigable: false` tiles are impassable physical obstacles, even if defeated or non-battling.
*   Ledge tiles marked `navigable="true"` can be occupied (e.g., by jumping down onto them), but upward movement onto a ledge from below is prevented by game physics, even if the tile's `navigable` attribute is true. The game's movement denial takes precedence over the XML's `navigable` flag for directional traversal of ledges from below.
*   Defeated trainers may sometimes remain as physical obstacles on their tile; their tile will remain `navigable: false` in map memory.
*   Mt. Moon 1F: Tile (8,19) is impassable, blocking direct southward movement from (8,18).
*   **Segmented Dungeons (CRITICAL - REINFORCED):** Complex dungeons like Mt. Moon are NOT single, continuous maps per floor. They are composed of *multiple, often isolated segments on the exact same floor level*. Access to these different segments is *exclusively* via specific warps (ladders, stairs, holes) from other floors or other segments of the same floor. It's impossible to walk from one isolated segment to another on the same floor without using a warp. Systematically explore each available warp from your current segment to discover connections to other segments or floors. Note the destination of each warp. If a warp leads to an already explored or unhelpful segment, return immediately and try a different warp. Do not assume all parts of a floor are interconnected or that all warps on a floor are reachable from any given point on that floor.
*   **1x1 Warp Activation:** Be more consistent with 1x1 warp activation, especially considering Pikachu's position. Stepping off and then back on is the reliable method if unsure.

# Self-Correction & Critique Learnings
- Path Planning: Meticulously examine map data (`map_xml_string`/annotated screen) *before* committing to movement. Identify clear, navigable corridors. Break down navigation into smaller, verifiable segments, especially in complex areas. If a path is blocked, backtrack to a known navigable area and re-evaluate the entire route, considering completely different approaches.
- Prioritize Healing: When party health is critical across multiple Pokémon, finding a Pokémon Center becomes the absolute top priority over other exploration or objectives.
- Trust Game State: Information like `reachable: no` for NPCs/warps should be treated as authoritative. Avoid wasting turns trying to interact with or path to targets marked as currently inaccessible.

# Gameplay Reminders (Post-Reflection Turn 8367)
*   **Reachable Unseen Tiles List:** Always use the *current* list from the Game State Information for exploration planning. This list is dynamic and can change frequently.
*   **Navigation Goal Coordinates:** Ensure `navigation_goal_coordinates` are always confirmed `navigable: true` in the map XML or are part of the current 'Reachable Unseen Tiles' list from Game State to avoid pathing errors.

# Mt. Moon Navigation Strategy (Post-Critique - DETAILED EXIT PLAN)
**Overall Goal:** Exit Mt. Moon to reach Route 4 Pokémon Center and heal critically injured party.
**RUN FROM ALL WILD ENCOUNTERS.**

**Phase 1: Mt. Moon 1F (Current Segment) to Target Warp (26,16) via Northern Loop**
*   Current Location: (16,20) as of Turn 8729.
*   Target Warp: (26,16) on Mt. Moon 1F (leads to B1F eastern segment, entry_point 4).
*   Path from (16,20) to (26,16):
    1.  (16,20) -> (16,16) (4 steps: Up x4).
    2.  (16,16) -> (17,16) (1 step: Right).
    3.  (17,16) -> (17,8)  (8 steps: Up x8).
    4.  (17,8)  -> (31,8)  (14 steps: Right x14).
    5.  (31,8)  -> (31,16) (8 steps: Down x8).
    6.  (31,16) -> (26,16) (5 steps: Left x5). [Enter Warp]

**Phase 2: Mt. Moon B1F (Eastern Segment) - REVISED**
*   Arrived at Mt. Moon B1F (26,16) (from 1F warp at (26,16), entry_point 5).
*   **Problem:** The planned target warp at B1F (26,10) is `reachable: no` according to game state. Phase 2 of original plan is invalid.
*   **Revised Plan:** Return to Mt. Moon 1F via the warp at B1F (26,16).
    1.  Step off current warp (26,16) B1F, then step back on to use it. This will return player to Mt. Moon 1F at (26,16).
    2.  Re-evaluate exit strategy from Mt. Moon 1F (26,16).

**Phase 3: Mt. Moon 1F (Eastern Segment - Current Location (26,16)) to Route 4 Exit**
*   Current Location: (26,16) on Mt. Moon 1F (arrived from B1F warp at (26,16), which corresponds to Mt. Moon 1F warp entry_point 4).
*   Target Warps (Exit to Route 4): (15,36) or (16,36) on Mt. Moon 1F.
*   Path from (26,16) to (15,36) or (16,36): To be planned once off the current warp tile and after defining the escape agent. The immediate next step is to move off (26,16).
*   RUN FROM ALL WILD ENCOUNTERS.

**Contingency:** If any segment of this path is blocked by an obstacle not in map memory (but visible on annotated screen), re-evaluate only the blocked segment and find a local detour. Prioritize annotated screen for immediate obstacles.