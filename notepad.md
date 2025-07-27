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
*   **Interaction:** Pressing 'A' on an adjacent tile to the Farfetch'd causes it to react. A non-moving 'Kwaa!' interaction, followed by clearing the dialogue box, can trigger a move.
*   **Reset Condition:** The puzzle resets if an incorrect action is taken or sometimes after a wild battle.

## B. Interaction Log (Grouped by Farfetch'd Position)

### State: (15, 25)
*   **Interact from N (15, 24):** Moves to (15, 29).
*   **Interact from S (15, 26):** 'Kwaa!', then clearing dialogue -> Moves to (20, 24).

### State: (15, 29)
*   **Interact from N (15, 28):** Disappears [New Location Unknown].
*   **Interact from S (15, 30):** 'Kwaa!', then clearing dialogue -> Moves to (15, 25).
*   **Interact from E (16, 29):** Moves to (15, 25) [Loop].
*   **Interact from W (14, 29):** 'Kwaa!', then clearing dialogue -> Disappears [New Location Unknown]

### State: (20, 24)
*   **Interact from N (20, 23):** 'Kwaa!', then clearing dialogue -> Disappears [New Location Unknown].
*   **Interact from E (21, 24):** 'Kwaa!', then clearing dialogue -> Disappears [New Location Unknown].

### State: (22, 31)
*   **Interact from N (22, 30):** 'Kwaa!', then clearing dialogue -> Moves to (28, 31).
*   **Interact from S (22, 32):** 'Kwaa!', then clearing dialogue -> Moves to (15, 29).
*   **Interact from E (23, 31):** Moves to (24, 35).

### State: (24, 35)
*   **Interact from W (23, 35):** Moves to (28, 31).
*   **Interact from E (25, 35):** 'Kwaa!', then clearing dialogue -> Moves to (22, 31).

### State: (28, 31)
*   **Interact from N (28, 30):** 'Kwaa!', then clearing dialogue -> Moves to (24, 35).
*   **Interact from S (28, 32):** No movement ['Kwaa!'].
*   **Interact from E (29, 31):** Disappears [Reset].
*   **Interact from W (27, 31):** Disappears [Reset].

### State: (29, 22)
*   **Interact from S (29, 23):** 'Kwaa!', then clearing dialogue -> Disappears [New Location Unknown].
*   **Interact from W (28, 22):** Disappears, reappears at (28, 31).

## C. Confirmed Blockages
*   **Western Path (Y=23):** The western path from (0,23) to (9,23) is confirmed to be unreachable from the central forest area. Verified with `verify_reachability_of_tiles` tool (Turn 10666). The system alert can be ignored.

# VI. Future Improvements & Hypotheses

## A. Tool Development Ideas
*   **General Puzzle Tool:** The `farfetchd_puzzle_solver` is too specific. Consider creating a more general tool, like `get_adjacent_traversable_tiles`, that can be used for any object or puzzle element.

## B. New Puzzle Hypotheses
*   **Ilex Forest Puzzle (Non-Linearity):** My current assumption is that the Farfetch'd puzzle is strictly linear. An alternative hypothesis is that it's non-linear, or that wild battles reset it to a specific *intermediate* state, not always the beginning. If my current approach fails, I should test this by intentionally triggering a battle after a successful move to observe the reset behavior.