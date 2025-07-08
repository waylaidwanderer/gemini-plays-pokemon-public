# Gem's Pokémon Crystal Notepad

## I. Core Directives & Principles
*   **Act Immediately:** As an LLM, I have no concept of 'later'. Any task I decide on (agent/tool creation/refinement, documentation) MUST be performed in the current turn. Deferring tasks is a critical failure.

## II. Strategic Plan
*   **Primary Goal: Obtain the next badge in Ecruteak City**
    *   **Plan:** Travel from Goldenrod City through Route 35, National Park, and Route 36 to reach Ecruteak City.
*   **Secondary Goal: Hatch the ODD EGG**
    *   **Plan:** Keep the egg in my party while traveling to accumulate steps.
*   **Tertiary Goal: Investigate the Radio Tower in Goldenrod City**
    *   **Plan:** Return to Goldenrod City after obtaining the next badge and explore the Radio Tower now that I have the Plain Badge.

## III. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.
- **Obvious Tile Test:** Even if a tile seems obviously impassable (e.g., WALL), I must attempt to walk into it once to be 100% certain.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `VOID`, `MART_SHELF`, `WATER` (without Surf), `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `COUNTER`.
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters), `LONG_GRASS` (Wild Encounters), `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile).
*   **One-Way Ledges:** 
    * `LEDGE_HOP_DOWN/LEFT/RIGHT`.
    * `FLOOR_UP_WALL`: A one-way ledge that can only be hopped **UP**. It is impassable from above (acts as a wall). Confirmed in Union Cave B1F and Slowpoke Well B1F.
*   **Special Requirement:** `CUT_TREE` (Requires HM01 Cut).
*   **Complex Tiles:**
    *   `WARP_CARPET_LEFT/DOWN/RIGHT`: Activated by pressing the indicated direction while standing on the tile.
    *   `Push-Down Trap`: A `FLOOR` tile that, when stepped on, pushes the player down one tile. It is a one-way interaction.
    *   `Interactable Warp (FLOOR)`: Some FLOOR tiles that are also warps do not activate on entry. They must be interacted with by pressing 'A' to trigger an event or text. (e.g., Ruins of Alph Inner Chamber @ (15, 3)).

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
    *   **ODD EGG:** A special egg received from the Day-Care Man.
    *   **HARD STONE:** Powers up rock-type moves.
    *   **PRZCUREBERRY:** Cures paralysis.
*   **Haircuts:** Increases a Pokémon's happiness.
*   **Pokégear Phone Menu:** When the 'Whom do you want to call?' text box is active, you cannot use the D-pad to switch functions. You MUST press 'B' to cancel and return to the main Pokégear screen before you can navigate to the radio.

## IV. Key Items & TMs
*   **COIN CASE:** Allows playing at the Game Corner.
*   **HM01 (CUT):** Clears small trees. Requires Hive Badge.
*   **SQUIRTBOTTLE:** Used to clear the Sudowoodo on Route 36.
*   **TM08 (ROCK SMASH):** Attack that may lower DEFENSE. Can shatter small rocks.
*   **TM12 (SWEET SCENT):** Lures wild POKéMON.
*   **TM28 (DIG):** Powerful GROUND move. Can escape caves.
*   **TM45 (ATTRACT):** Infatuates opposite-gender Pokémon.
*   **TM49 (FURY CUTTER):** Gets stronger with each consecutive hit.

## V. Future Development Ideas
*   **Auto-Travel Tool:** Create a tool to automate travel through high-encounter areas. It would take a destination coordinate, call the pathfinder, and then execute the path. If interrupted by a wild battle, it would automatically select 'RUN' and then re-call the pathfinder from the new position to continue the journey. This would streamline long trips significantly.
*   **Exploration Manager Agent:** An agent to consult when stuck. It would analyze the current location, available paths, and key items to suggest novel exploration strategies or alternative hypotheses to test, preventing getting stuck in loops.
*   **Phone Call Summarizer Agent:** An agent to parse phone call text and extract key information (e.g., trainer name, location, request) to avoid reading through lengthy dialogues.
*   **Shop Navigator Tool:** A tool that parses shop menus to find a specific item and outputs the button presses needed to select and purchase it.
*   **Map Marker Cleaner Agent:** An agent that analyzes map markers and suggests redundant ones for deletion (e.g., a '🎁' marker for an item that also has a '✅' marker).

## VI. Archive: Solved Puzzles & Procedural Failures
*   **Hypothesis Testing To-Do:**
    *   Test `LEDGE_HOP_LEFT` at Ilex Forest (14, 14) by attempting to move right against it.
*   **Skepticism Reminder:** Do not assume all NPCs are trainers. Some provide hints or flavor text. Wasting turns trying to battle a non-battling NPC is inefficient.
*   **Failure Log (Turns ~28533-28564):** Wasted significant time attempting to buy Repels at Violet City Mart based on an unverified assumption. **Lesson: Verify information before committing to a multi-step plan. A bigger city's Department Store is a more reliable source for a wider variety of items.**
*   **Failure Log (Turns ~28488-28532):** Failed to use REPELs, leading to numerous wasteful encounters on Route 32. **Lesson: Verify consumable inventory before long trips.**
*   **Failure Log (Turns ~28680-28689):** Got stuck in a repetitive loop of running from wild Pokémon in Union Cave instead of making progress. **Lesson: If a strategy (like brute-force running) fails repeatedly, change tactics. Engage with other elements on the map (like trainers) to break the loop.**
*   **Failure Log (Turns ~28701-28705):** Got stuck in a dialogue loop with a non-battling trainer in Union Cave. **Lesson: If dialogue repeats without initiating a battle, the NPC is not a trainer. Correct map markers and move on.**
*   **Failure Log (Turn ~28849):** Pathfinder v7 failed to recognize a '☠️' marker on a defeated trainer (Schoolboy Alan) as an impassable obstacle, leading to a blocked path. This indicates a critical flaw in my tool's logic or my application of it, which must be addressed immediately.
*   **Failure Log (Turn ~28849):** Pathfinder v7 failed to recognize a '☠️' marker on a defeated trainer (Schoolboy Alan) as an impassable obstacle, leading to a blocked path. This indicates a critical flaw in my tool's logic or my application of it, which must be addressed immediately.
*   **Failure Log (Turn ~28849):** Pathfinder v7 failed to recognize a '☠️' marker on a defeated trainer (Schoolboy Alan) as an impassable obstacle, leading to a blocked path. This indicates a critical flaw in my tool's logic or my application of it, which must be addressed immediately.
*   **Failure Log (Turn ~28867):** The `explore_unseen` logic in pathfinder_v7 failed, incorrectly reporting no reachable unseen areas. This points to a bug in the entry-point calculation. The tool must be simplified to path directly to the nearest unseen tile.