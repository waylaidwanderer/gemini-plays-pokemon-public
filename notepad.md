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

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.
*   **LEDGE_HOP_RIGHT:** One-way traversal. Can only be entered from the left.
*   **LEDGE_HOP_LEFT:** One-way traversal. Can only be entered from the right.

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

## A. General Mechanics
*   **Goal:** Herd Farfetch'd to the apprentice at (7, 28).
*   **Interaction:** Approaching from an adjacent tile and pressing 'A' causes a reaction.
*   **Puzzle Reset:** The Farfetch'd disappears and resets the puzzle if an incorrect action is taken or after certain wild battles.

## B. Confirmed State Behaviors
*   **State 1: Farfetch'd at (15, 25)**
    *   Interact from North (15, 24) -> Moves to (15, 29) after 'Kwaa!' dialogue.
    *   Interact from South (15, 26) -> Moves to (20, 24).
*   **State 2: Farfetch'd at (15, 29)**
    *   Interact from East (16, 29) -> Moves to (15, 25) [Loop].
    *   Interact from West (14, 29) -> Moves to (22, 31).
*   **State 3: Farfetch'd at (20, 24)**
    *   Interact from East (21, 24) -> 'Kwaa!' dialogue, then disappears [Reset].
    *   Interact from North (20, 23) -> Disappears [Reset].
*   **State 4: Farfetch'd at (22, 31)**
    *   Interact from South (22, 32) -> Moves to (15, 29).
    *   Interact from North (22, 30) -> Moves to (28, 31).
    *   Interact from East (23, 31) -> Moves to (24, 35).
*   **State 5: Farfetch'd at (24, 35)**
    *   Interact from West (23, 35) -> Moves to (28, 31).
*   **State 6: Farfetch'd at (28, 31)**
    *   Interact from East (29, 31) -> Disappears [Reset].
    *   Interact from West (27, 31) -> Moves off-screen [Reset].
*   **State 7: Farfetch'd at (29, 22)**
    *   Interact from West (28, 22) -> No reaction.
    *   Interact from South (29, 23) -> 'Kwaa!' dialogue, then disappears [Reset].

## C. Current Hypothesis
*   Since the Farfetch'd has vanished from the forest entirely, it may have returned to its owner at the Charcoal Kiln in Azalea Town. This is the current active lead.

## D. Northern Blockage Hypothesis
*   **Primary Hypothesis:** The northern area of Ilex Forest is unreachable from the south.
*   **Evidence:** Both `find_path_to_target` and `find_reachable_unseen_tiles` tools report no path. This has also been manually verified by attempting to walk north.

# VI. Critical Failures & Lessons Learned
*   **Data Management Deferral:** I have a pattern of deferring critical data management tasks. This is a violation of core directives and must be corrected.
*   **Tool Distrust:** I have repeatedly failed to trust my `find_path_to_target` tool's output, assuming it was broken when it correctly identified blocked paths.
*   **HM moves can be used even if the Pokémon is fainted.** This is a key mechanic learned from the Gentleman in the Charcoal Kiln.
*   **Incorrect Agent Design (Resolved):** My original `puzzle_solver` agent was designed for computational data parsing, a task for a tool. It has been replaced with the `farfetchd_puzzle_solver` tool.
*   **Agent Underutilization:** I am not consistently using my `procedural_overseer` agent. I must integrate it into my regular workflow to prevent repetitive mistakes.
*   **Inconsistent Marker Linking:** I have failed to link markers to object IDs immediately upon discovery.
*   **Repetitive Tool Failures (Critical Failure):** I repeatedly failed to update a tool (turns 8737-8742) by submitting an identical script. This is a critical failure loop that could have been prevented by using my `procedural_overseer` agent. This is a lesson in mindfulness and checking my work before submission.
*   **Deferred Tool Fixing (Critical Failure):** I incorrectly deferred fixing a broken tool by making it a tertiary goal. Tool maintenance is an immediate, high-priority action that must be completed before any other gameplay objective.

# VII. Puzzle Solutions

## A. Ruins of Alph (Kabuto Puzzle)
*   The true solution was to use the unmarked warp at (4, 0) in the puzzle chamber after arranging the pieces.

# VIII. Untested Assumptions & Alternative Hypotheses
*   **Assumption 1:** The Farfetch'd puzzle is solvable with current knowledge.
    *   **Alternative Hypothesis:** A key item or NPC hint is required.
    *   **Test Plan:** If still stuck after 50 more turns of systematic attempts, I will perform a full world exploration sweep, revisiting all previous areas for missed clues.
*   **Assumption 2:** The northern part of Ilex Forest is permanently inaccessible from the south.
    *   **Alternative Hypothesis:** A game event, possibly solving the Farfetch'd puzzle, will open the path.
    *   **Test Plan:** Continue to run `find_reachable_unseen_tiles` after every major puzzle state change to check for new paths.