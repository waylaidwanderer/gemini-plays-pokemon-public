# Gem's Pokémon Crystal Adventure Log

# I. Core Gameplay & Strategy

## A. Key Lessons & Behavioral Directives
*   **Data Management is Paramount:** All data management tasks (notepad updates, marker placement, tool fixes) MUST be performed IMMEDIATELY in the turn of discovery. Deferring these tasks is a critical failure. I must use smaller, targeted edits (`replace`, `append`) if a full `overwrite` fails.
*   **Trust Verified Tools:** My custom tools are more reliable than my perception or general system alerts. Once a tool's output is verified (e.g., confirming tiles are unreachable), I must trust that result until new information suggests otherwise. Repeatedly re-verifying a trusted tool is inefficient.
*   **Efficient Agent Use:** I must use my reasoning agents (`battle_strategist`, etc.) for complex situations, not trivial ones. My own judgment is sufficient for simple encounters.
*   **Tool Synchronization is CRITICAL:** Tools with shared logic (like pathfinding and exploration) MUST be updated together. A failure to synchronize them leads to contradictory results and wasted time.
*   **Scientific Method:** When debugging or solving puzzles, I must form a clear hypothesis and test it methodically. Jumping to conclusions leads to wasted time.
*   **PP Management:** I must not allow my lead Pokémon to run out of all attacking moves while in a dungeon. Retreating to heal is crucial for resource management.
*   **HM Usage:** HM moves can be used by fainted Pokémon.

## B. Tile Traversal Rules
*   **Traversable:** FLOOR, TALL_GRASS, LONG_GRASS, DOOR, CAVE, LADDER.
*   **Impassable:** WALL, WINDOW, PC, VOID, CUT_TREE, SIGN, BOOKSHELF, BLACKBOARD, MART_SHELF, WATER, BUOY, TV, TOWN_MAP, RADIO, INCENSE_BURNER, COUNTER, BIRD, HEADBUTT_TREE, FRUIT_TREE.
*   **One-Way Traversal:**
    *   LEDGE_HOP_DOWN: Can only be entered from above.
    *   LEDGE_HOP_RIGHT: Can only be entered from the left.
    *   LEDGE_HOP_LEFT: Can only be entered from the right.
    *   FLOOR_UP_WALL: Can only be entered from below. It is a one-way tile that acts as a ledge you jump up.
*   **Warp Carpets:** One-way warps activated by pressing the corresponding direction (e.g., WARP_CARPET_RIGHT requires pressing 'Right').

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
*   **Current Quest:** Get HM01 Cut by having the apprentice in Ilex Forest return to his boss.

## B. NPC Hints & Lore
*   A Fisher in Union Cave at (14, 19) mentioned that strange roars can be heard from deep within the cave on weekends.

# IV. Hypotheses & Tests
*   **Hypothesis (Failed):** Interacting with the apprentice, then the boss, then the apprentice again, then the boss again would progress the quest. **Result:** Both NPCs are stuck in a dialogue loop, repeating the same lines. The quest did not advance.
*   **Current Hypothesis:** The quest requires a specific sequence of interactions. Now that I have spoken to the boss *after* speaking to the apprentice post-puzzle, I must return to the apprentice one more time to trigger him to return to the kiln.
*   **Past Hypothesis (Disproven):** I missed a trigger inside the Slowpoke Well.
    *   **Result:** Re-exploring the well confirmed no new triggers. My exploration tool confirmed all unseen areas were unreachable.
*   **Past Hypothesis (Disproven):** Kurt or his granddaughter in his house would trigger the next event.
    *   **Result:** They gave generic dialogue.
*   **Past Hypothesis (Disproven):** The unseen areas of Slowpoke Well are reachable.
    *   **Result:** Multiple tool checks confirmed they are blocked by water and boulders.

### E. Tile Mechanics To Test
*   **FLOOR_UP_WALL:** My pathfinder previously treated this as a one-way tile. I removed this rule for debugging. I need to conduct a systematic in-game test to determine its actual traversal properties (e.g., can it be entered from below? from the sides? can it be exited in any direction?).