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
*   **Investigate the Strange Tree:** A strange tree on Route 36 is blocking the way to Goldenrod City. This is my main path forward.

## B. Stalled Quests
*   **Rescue the Apprentice (HM01 Cut):** The Farfetch'd herding portion of the puzzle in Ilex Forest is complete, but the apprentice and his boss are in a dialogue loop, blocking the quest reward.

# VI. Tool Development
*   The hyper-specific `puzzle_strategist` agent was deleted. It has been replaced by the more general-purpose `get_adjacent_traversable_tiles` tool, which can be used for any future interaction-based puzzles.