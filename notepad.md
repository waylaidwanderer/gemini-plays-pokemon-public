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
*   **Warp Carpets:** One-way warps activated by pressing the corresponding direction.
    *   WARP_CARPET_RIGHT: Requires pressing 'Right'.
    *   WARP_CARPET_DOWN: Requires pressing 'Down'.
    *   WARP_CARPET_LEFT: Requires pressing 'Left'.
*   **To Be Tested:**
    *   FRUIT_TREE: Need to test if this is a traversable tile or an impassable object. There's one on Route 33 I can test when I pass through.

## B. Key Mechanics & Lessons Learned
*   **HM Usage:** HM moves can be used by fainted Pokémon.
*   **Tool Trust:** My custom tools are more reliable than my perception. I must trust their output to verify my assumptions, not the other way around. Blaming the tool should be a last resort after all environmental possibilities have been exhausted.
*   **Scientific Method:** When debugging or solving puzzles, I must form a clear hypothesis and test it methodically. Jumping to conclusions (e.g., assuming a tool is bugged when the path is simply blocked) leads to wasted time.
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
*   **Find an alternate route to Goldenrod City:** The path through Route 36 is blocked by a strange tree. The solution is likely in Goldenrod City, so I need to find another way there, possibly via the National Park.

## B. Stalled Quests
*   **Rescue the Apprentice (HM01 Cut):** The Farfetch'd herding portion of the puzzle in Ilex Forest is complete, but the apprentice and his boss are in a dialogue loop, blocking the quest reward.

# VI. Tool Development
*   The hyper-specific `puzzle_strategist` agent was deleted. It has been replaced by the more general-purpose `get_adjacent_traversable_tiles` tool, which can be used for any future interaction-based puzzles.
*   **Idea:** Create a 'debugging_assistant' agent. It would take a failing tool's code and a hypothesis for the failure, then generate a series of `run_code` tests to methodically isolate the bug.
*   **Idea:** Create a 'reflection_assistant' agent. It would take the 50-turn reflection questions and my recent turn history as input, then generate a preliminary analysis of my performance, forcing me to confront any strategic loops or unaddressed issues more directly.
*   **Tool Synchronization:** Tools with shared logic (like pathfinding and exploration) MUST be updated together. A failure to synchronize them can lead to contradictory results and wasted time.

# V. Lessons Learned
*   **Tool Synchronization is CRITICAL:** My `find_path_to_target` and `find_reachable_unseen_tiles` tools fell out of sync. A bug fix in one was not applied to the other, leading to contradictory outputs and wasted turns. Shared logic must be updated everywhere simultaneously.
*   **Trust Verified Tools Over General Alerts:** The system's 'unseen tile' alert only indicates *potential* reachability. My verified tools correctly determined these tiles were unreachable. I must trust my own verified data over general system hints.

# VII. New Agent Ideas
*   **Exploration Validator:** An agent that takes the output of `find_reachable_unseen_tiles`, automatically runs `get_adjacent_traversable_tiles` on each, and then uses `find_path_to_target` to return a final, verified list of reachable exploration targets. This would automate my entire validation loop.