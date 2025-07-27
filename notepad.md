# Gem's Pokémon Crystal Adventure Log

# I. Game Mechanics & Systems

## A. Tile Traversal Rules
*   **Traversable:** FLOOR, TALL_GRASS, LONG_GRASS, DOOR, CAVE, LADDER.
*   **Impassable:** WALL, WINDOW, PC, VOID, CUT_TREE, SIGN, BOOKSHELF, BLACKBOARD, MART_SHELF, WATER, BUOY, TV, TOWN_MAP, RADIO, INCENSE_BURNER, COUNTER, BIRD, HEADBUTT_TREE.
*   **One-Way Traversal:**
    *   LEDGE_HOP_DOWN: Can only be entered from above.
    *   LEDGE_HOP_RIGHT: Can only be entered from the left.
    *   LEDGE_HOP_LEFT: Can only be entered from the right.
    *   FLOOR_UP_WALL: Can only be entered from below.
*   **Warp Carpets:** One-way warps activated by pressing the corresponding direction (e.g., WARP_CARPET_DOWN requires pressing 'Down').

## B. Key Mechanics & Lessons Learned
*   **HM Usage:** HM moves can be used by fainted Pokémon.
*   **Tool Trust:** My custom tools, especially pathfinders, are more reliable than generic system alerts. I must trust their output, as they analyze the direct game data.
*   **Data Management:** All data management tasks (notepad updates, marker placement) MUST be performed immediately in the turn of discovery. Deferring these tasks is a critical failure.
*   **Agent Utilization:** I must consistently use my `procedural_overseer` agent to prevent repetitive, failing loops.
*   **PP Management:** I must not allow my lead Pokémon to run out of all attacking moves while in a dungeon. Retreating to heal is crucial for resource management.

# II. Battle Information

## A. Verified Type Matchups
*   Ghost has NO EFFECT on Normal.
*   Normal has NO EFFECT on Ghost.
*   Unown's Hidden Power (type unknown) can be super-effective against Fire.

## B. Gym Leader Teams
*   **Falkner (Violet City):** Pidgey (Lv7), Pidgeotto (Lv9).
*   **Bugsy (Azalea Town):** Metapod (Lv14), Kakuna (Lv14), Scyther (Lv16).

# III. Story & Quests

## A. Current Quest
*   **Rescue the Apprentice:** Solve the Farfetch'd herding puzzle in Ilex Forest to get HM01 (Cut).

## B. Side Quests & Leads
*   **The Strange Tree:** A strange tree on Route 36 is blocking the way to Goldenrod City. This is my main path forward after Ilex Forest.

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
    *   From W (14, 29) -> 'Kwaa!' then clearing dialogue -> Disappears [NEW DISCOVERY! Location unknown].
    *   From S (15, 30) -> 'Kwaa!', then clearing dialogue -> Moves to (15, 25) [NEW DISCOVERY!].
*   **State (20, 24):**
    *   From E (21, 24) -> 'Kwaa!' [Verified, pending dialogue clear].
    *   From N (20, 23) -> Disappears [New Location Unknown, 'Kwaa!'] [Verified].
*   **State (22, 31):**
    *   From S (22, 32) -> No movement ['Kwaa!'], then clearing dialogue causes it to disappear [NEW DISCOVERY! Did not reappear at (28, 31)].
    *   From N (22, 30) -> 'Kwaa!', then clearing dialogue -> Moves to (28, 31) [CONFIRMED SEQUENCE!].
    *   From E (23, 31) -> Moves to (24, 35).
*   **State (28, 31):**
    *   From E (29, 31) -> Disappears [Reset].
    *   From W (27, 31) -> Disappears [Reset].
    *   From S (28, 32) -> No movement ['Kwaa!'] [Verified].
    *   After 'Kwaa!' from N (28, 30), clearing dialogue -> Moves to (24, 35) [CONFIRMED SEQUENCE!].
*   **State (24, 35):**
    *   From W (23, 35) -> Moves to (28, 31).
    *   From E (25, 35) -> 'Kwaa!', then clearing dialogue -> Moves to (22, 31) [CONFIRMED SEQUENCE!].
*   **State (29, 22):**
    *   From W (28, 22) -> Disappears, reappears at (28, 31).
    *   From S (29, 23) -> Disappears [New Location Unknown, 'Kwaa!'] [Verified].

## C. Puzzle Hypotheses
*   **Hypothesis 1 (Confirmed):** The puzzle state is changed by 'Kwaa!' interactions. A non-moving 'Kwaa!' interaction, followed by clearing the dialogue box, can trigger a move. This is a complex, state-based mechanic.
*   **Hypothesis 2 (Current):** The puzzle is solvable with a specific sequence of directional interactions. I need to continue methodically testing interaction points.

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