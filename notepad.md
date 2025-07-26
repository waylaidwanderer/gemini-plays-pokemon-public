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

### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.
*   **LEDGE_HOP_RIGHT:** One-way traversal. Can only be entered from the left.
*   **LEDGE_HOP_LEFT:** One-way traversal. Can only be entered from the right.
*   **FLOOR_UP_WALL:** Confirmed one-way traversal. Can only be entered from below. Impassable from all other directions.

### Untested Tile Assumptions:
*   **HEADBUTT_TREE:** Confirmed impassable by attempting to walk into it.

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

# V. Untested Assumptions & Hypotheses
*   **Primary Hypothesis for HM01:** The Farfetch'd puzzle is a sequential teleportation puzzle that, when solved, will yield HM01 (Cut).
*   **Alternative Hypothesis for HM01:** The Farfetch'd puzzle is a red herring or optional. An alternative path to Goldenrod City or another method of obtaining HM01 exists. 
    *   **Test:** If the puzzle becomes impossible or I get stuck in a loop, I must explore all other paths to their absolute ends. This includes the Unexplored Warp at (3, 43) and the unseen tiles at the south of the forest (20, 36) through (28, 36).

# VI. Critical Failures & Lessons Learned
*   **Data Management Deferral:** I have a pattern of deferring critical data management tasks (like updating my notepad or linking map markers) instead of performing them immediately. This is a violation of core directives and must be corrected. I must act immediately on new information.
*   **Tool Distrust:** I have repeatedly failed to trust my `find_path_to_target` tool's output, assuming it was broken when it correctly identified blocked paths. I must trust my tool's output and analyze the map more carefully before assuming a bug.
*   **HM moves can be used even if the Pokémon is fainted.** This is a key mechanic learned from the Gentleman in the Charcoal Kiln.
*   **Incorrect Agent Design (Resolved):** My original `puzzle_solver` agent was designed to perform computational data parsing, which is a task for a tool. It has since been deleted and replaced with the `farfetchd_puzzle_solver` tool, which correctly handles map analysis.
*   **Agent Underutilization:** I am not consistently using my `procedural_overseer` agent. I need to integrate it into my regular workflow to prevent repetitive mistakes.
*   **Inconsistent Marker Linking:** I have failed to link markers to object IDs immediately upon discovery (e.g., Lost Apprentice, Item Ball). This is a critical data management failure that must be rectified.

# VII. Puzzle Solutions

## A. Ruins of Alph (Kabuto Puzzle)
*   The true solution was to use the unmarked warp at (4, 0) in the puzzle chamber after arranging the pieces.

# VIII. Exploration Notes
*   **Dead Ends:** Route 32 Pier, Union Cave B1F (from 1F ladder), Azalea Pokecenter 2F are all confirmed dead ends for now.
*   **Unexplored Areas:** 
    *   Unexplored Warp at (3, 43) in Ilex Forest.
    *   Unseen tiles at the south of Ilex Forest, starting around (20, 36).
*   **Deferred Tool Fixing:** In turn 8073, I identified that my `farfetchd_puzzle_solver` tool was faulty but deferred fixing it. This is a major violation of core directives and must not be repeated. Faulty tools must be fixed immediately.
*   **Procedural Overseer Reminder:** I must make it a habit to use the `procedural_overseer` agent before committing to any long path to check for repetitive, failing loops (like being constantly interrupted by wild battles).