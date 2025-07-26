# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **LONG_GRASS:** Traversable, can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **CAVE:** Functions as a warp.
*   **LADDER:** Functions as a two-way warp between floors.

### Warp Tiles:
*   **WARP_CARPET_DOWN:** One-way warp. Activated by pressing 'Down'.
*   **WARP_CARPET_LEFT:** One-way warp. Activated by pressing 'Left'.
*   **WARP_CARPET_RIGHT:** One-way warp. Activated by pressing 'Right'.

### Confirmed Impassable:
*   **WALL:** Confirmed impassable. Blocks movement from all directions.
*   **WINDOW:** Impassable. Functions as a wall.
*   **PC:** Impassable. Functions as an object.
*   **VOID:** Impassable. Appears as a black abyss.
*   **CUT_TREE:** Impassable. Likely requires HM Cut.
*   **SIGN:** Impassable. Functions as an object that can be interacted with for text.
*   **BOOKSHELF:** Impassable. Functions as an object that can be interacted with for text.
*   **BLACKBOARD:** Impassable. Functions as an object that can be interacted with for text.
*   **MART_SHELF:** Impassable. Functions as a wall.
*   **WATER:** Confirmed impassable. Blocks movement entirely.
*   **BUOY:** Impassable. Functions as a wall in water.
*   **TV:** Impassable object.
*   **TOWN_MAP:** Impassable object.
*   **RADIO:** Impassable object. Can be interacted with for text.
*   **INCENSE_BURNER:** Impassable object. (Confirmed by attempting to walk into it).
*   **COUNTER:** Confirmed impassable. Functions as a wall.
*   **BIRD:** Impassable object. Functions as a wall.
*   **HEADBUTT_TREE:** Confirmed impassable by attempting to walk into it.
*   **VOID:** Confirmed impassable by observation.

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.
*   **LEDGE_HOP_RIGHT:** One-way traversal. Can only be entered from the left.
*   **LEDGE_HOP_LEFT:** One-way traversal. Can only be entered from the right.
*   **FLOOR_UP_WALL:** One-way traversal. Can only be entered from below (i.e., you can't walk down onto it).

## B. Map Marker Mechanics
*   **Dynamic Nature:** Markers linked to an `object_id` WILL move with the object. This is useful for tracking moving NPCs.

# II. Battle Information

## A. Verified Type Matchups
*   Ghost-type moves have NO EFFECT on Normal-type Pokémon.
*   Normal-type moves have NO EFFECT on Ghost-type Pokémon.
*   Unown's Hidden Power can be super-effective against Fire-type Pokémon (observed against Vulcan). The specific type is unknown, but could be Water, Rock, or Ground.

## B. Gym Leader Teams
*   **Falkner (Violet City):** Pidgey (Lv7), Pidgeotto (Lv9). Primarily Normal/Flying type.
*   **Bugsy (Azalea Town):** Metapod (Lv14), Kakuna (Lv14), Scyther (Lv16).

# III. Badges & Items
*   **Zephyr Badge:** Acquired from Falkner. Raises Pokémon's attack power and allows the use of HM05 (Flash) outside of battle.
*   **Hive Badge:** Acquired from Bugsy. Allows use of HM01 (Cut) outside of battle and makes traded Pokémon up to Lv30 obey.
*   **TM31 (Mud-Slap):** Received from Falkner.
*   **TM49 (Fury Cutter):** Received from Bugsy.
*   **EVERSTONE:** Received from Professor Elm. Prevents a Pokémon holding it from evolving.

# IV. Story Progression

## A. Current Quest
*   **Rescue the Apprentice:** The Charcoal Man's apprentice is lost in Ilex Forest. Finding his runaway Farfetch'd is the primary lead to obtaining HM01 (Cut).

## B. Past Clues & Hints
*   **Strange Tree:** Gramps in the Route 36 Gatehouse mentioned a 'strange tree' blocking a road, which might be why fewer people are visiting the Ruins of Alph. This could be the path forward to Goldenrod City.

# V. Ilex Forest Puzzle: Farfetch'd Herding

## A. Goal & Mechanics
*   **Objective:** Herd the Farfetch'd to the apprentice at (7, 28).
*   **Interaction:** Pressing 'A' on an adjacent tile to the Farfetch'd causes it to react.
*   **Reset Condition:** The puzzle resets if an incorrect action is taken or sometimes after a wild battle.

## B. Interaction Log (State -> Player Action -> Result)
*   **State (15, 25):**
    *   From N (15, 24) -> Moves to (15, 29).
    *   From S (15, 26) -> Moves to (20, 24).
*   **State (15, 29):**
    *   From N (15, 28) -> Disappears [New Location Unknown].
    *   From E (16, 29) -> Moves to (15, 25) [Loop].
    *   From W (14, 29) -> Moves to (22, 31).
*   **State (20, 24):**
    *   From E (21, 24) -> Disappears [Reset].
    *   From N (20, 23) -> Disappears [New Location Unknown, 'Kwaa!'] [Verified].
*   **State (22, 31):**
    *   From S (22, 32) -> No movement ['Kwaa!'], then clearing dialogue causes it to disappear [NEW DISCOVERY!].
    *   From N (22, 30) -> Moves to (28, 31) [Verified].
    *   From E (23, 31) -> Moves to (24, 35).
*   **State (28, 31):**
    *   From E (29, 31) -> Disappears [Reset].
    *   From W (27, 31) -> Disappears [Reset].
    *   From S (28, 32) -> No movement ['Kwaa!'] [Verified].
    *   From N (28, 30) -> Moves to (24, 35) [Verified].
*   **State (24, 35):**
    *   From W (23, 35) -> Moves to (28, 31).
    *   From E (25, 35) -> No movement ['Kwaa!'] [Verified].
    *   After 'Kwaa!', clearing dialogue -> Moves to (22, 31) [NEW DISCOVERY!].
*   **State (29, 22):**
    *   From W (28, 22) -> Disappears, reappears at (28, 31).
    *   From S (29, 23) -> Disappears [New Location Unknown, 'Kwaa!'] [Verified].

## C. Puzzle Hypotheses
*   **Hypothesis 1 (Primary):** The puzzle is solvable with a specific sequence of directional interactions.
*   **Hypothesis 2 (Alternative):** The puzzle solution is time-dependent (e.g., requires specific time of day).
*   **Hypothesis 3 (Alternative):** The puzzle requires a key item I don't possess yet.
*   **Hypothesis 4 (Alternative):** The puzzle's solution may not just be about the direction of interaction, but also about other cues, such as the sounds the Farfetch'd makes ('Kwaa!') or the direction it faces after being pushed. I need to pay closer attention to these details.
*   **Hypothesis 5 (Current):** Leaving and re-entering Ilex Forest may reset the Farfetch'd puzzle, allowing for a fresh attempt.
*   **Hypothesis 6 (Confirmed):** The puzzle state is changed by 'Kwaa!' interactions. A non-moving 'Kwaa!' interaction, followed by clearing the dialogue box, can trigger a move. This is a complex, state-based mechanic.

## D. Confirmed Blockages
*   **Northern Path (Y=23):** The northern path is definitively confirmed to be unreachable from the southern part of the forest. This has been repeatedly verified by my `verify_reachability_of_tiles` tool, which found no valid path. The system alerts are misleading.
*   **Western Path (Y=23):** The western path from (0,23) to (9,23) is confirmed to be unreachable from the central forest area. Verified with `verify_reachability_of_tiles` tool (Turn 9919).

# VI. Critical Failures & Lessons Learned (Consolidated)
*   **Data Management Deferral:** I have a pattern of deferring critical data management tasks, such as immediately updating map markers and notepad entries upon discovery. This is a violation of core directives and must be corrected.
*   **Tool Distrust:** I have repeatedly failed to trust my `find_path_to_target` tool's output, assuming it was broken when it correctly identified blocked paths.
*   **HM moves can be used even if the Pokémon is fainted.** This is a key mechanic learned from the Gentleman in the Charcoal Kiln.
*   **Agent Underutilization:** I am not consistently using my `procedural_overseer` agent. I must integrate it into my regular workflow to prevent repetitive mistakes.
*   **Inconsistent Marker Linking:** I have failed to link markers to object IDs immediately upon discovery.
*   **Repetitive Tool Failures (Critical Failure):** I repeatedly failed to update a tool (turns 8737-8742) by submitting an identical script. This is a critical failure loop that could have been prevented by using my `procedural_overseer` agent. This is a lesson in mindfulness and checking my work before submission.
*   **Deferred Tool Fixing (Critical Failure):** I incorrectly deferred fixing a broken tool by making it a tertiary goal. Tool maintenance is an immediate, high-priority action that must be completed before any other gameplay objective.
*   **Tool Underutilization (Overwatch Critique):** I failed to use my `farfetchd_puzzle_solver` tool when it was applicable, a valid critique from the overwatch system.
*   **Misleading System Alerts (Critical Lesson):** I spent numerous turns debugging a working tool (`find_reachable_unseen_tiles`) because I trusted a generic system alert over my tool's specific, data-driven output. The debug logs eventually proved the tool was correct and the path was blocked. I must trust my verified tools over general system information.

# VII. Puzzle Solutions

## A. Ruins of Alph (Kabuto Puzzle)
*   The true solution was to use the unmarked warp at (4, 0) in the puzzle chamber after arranging the pieces.