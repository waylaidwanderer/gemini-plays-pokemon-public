# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.
- **Obvious Tile Test:** Even if a tile seems obviously impassable (e.g., WALL), I must attempt to walk into it once to be 100% certain.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `VOID`, `MART_SHELF`, `COUNTER`, `WATER`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters), `LONG_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile).
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`.
*   **Complex Tiles:**
    *   `FLOOR_UP_WALL`: One-way ledge. Enter from below/sides. Cannot exit by moving up.
    *   `WARP_CARPET_LEFT/DOWN/RIGHT`: Activated by pressing the indicated direction while standing on the tile.
    *   `Push-Down Trap`: A `FLOOR` tile that, when stepped on, pushes the player down one tile. It is a one-way interaction; the tile cannot be re-entered from below to trigger the effect again.

### Untested Tile Types (High Priority)
* `RAILING`: Goldenrod Dept. Store Roof.
* `PIPE_HORIZONTAL`/`PIPE_VERTICAL`: Underground.
* `LINK_CABLE`/`TRADE_MACHINE`: Pokecenter 2F.
* `CUT_TREE`: Route 36.
* `Puzzle Floor Tiles`: Ruins of Alph chamber.
* `PC`: Ruins of Alph Research Center.

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
*   **Haircuts:** Increases a Pokémon's happiness.
*   **Pokégear Phone Menu:** When the 'Whom do you want to call?' text box is active, you cannot use the D-pad to switch functions. You MUST press 'B' to cancel and return to the main Pokégear screen before you can navigate to the radio.

## II. Key Items & TMs
*   **COIN CASE:** Allows playing at the Game Corner.
*   **HM01 (CUT):** Clears small trees. Requires Hive Badge.
*   **SQUIRTBOTTLE:** Used to clear the Sudowoodo on Route 36.
*   **TM08 (ROCK SMASH):** Attack that may lower DEFENSE. Can shatter small rocks.
*   **TM28 (DIG):** Powerful GROUND move. Can escape caves.
*   **TM45 (ATTRACT):** Infatuates opposite-gender Pokémon.
*   **TM49 (FURY CUTTER):** Gets stronger with each consecutive hit.

## III. Current Objectives & Hypotheses

### Primary Objective: Find Ecruteak City
*   **Current Location:** Ruins of Alph Inner Chamber
*   **Primary Hypothesis:** The path to Ecruteak City is connected to the Ruins of Alph, and solving this puzzle is mandatory.
*   **Alternative Hypothesis 1:** The Ruins of Alph is a side area. The main path might be elsewhere, possibly an unexplored path on Route 36.
*   **Alternative Hypothesis 2:** I am not trapped in this room. The warp-back was a one-time event, and I can leave via the ladder at (10, 13).

### Ruins of Alph Inner Chamber Puzzle
*   **Current Hypothesis:** The puzzle is solved by tuning the Pokégear radio to the mysterious transmission.
*   **Alternative Hypothesis:** The radio is a red herring. The puzzle involves interacting with the statues in a specific sequence, or using an item I don't possess yet.

### Team Rocket in Goldenrod
*   **Goal:** Get past the Team Rocket grunt blocking the Radio Tower.
*   **Status:** On hold. Progress is likely tied to a story event I haven't triggered yet.

## IV. Agent & Tool Development Ideas
*   **`menu_navigator_agent`:** An agent to plan the sequence of button presses for complex menu navigation tasks.
*   **`party_lead_advisor_agent`:** An agent to suggest the best lead Pokémon for a given situation (e.g., escaping wild battles, specific trainer types).

## V. Misc Info & Reminders
*   **Bug-Catching Contest:** Tuesday, Thursday, Saturday in National Park.
*   **Goldenrod Dept. Store Sale:** Camper Todd will call about sales.
*   **Radio Tower Side Quest:** Buena's BLUE CARD password show.
*   **SLOWPOKETAIL:** For sale on Route 32. Purpose unknown.

## VI. Learnings & Mistakes
*   **Critical Procedural Failure (Turns ~27050-27128):** I failed to immediately document the solution to the Pokégear phone menu loop (pressing 'B' to cancel). This led to a prolonged behavioral loop and wasted ~50 turns. I must document new mechanics or solutions in the same turn I discover them. Deferring this action is not a valid strategy.
*   **Major Hallucination (Turn 26485-26490):** Misidentified my location on Route 36, thinking I was in Violet City. I must verify my location after every map transition.
*   **Critical Hallucination (Turn 26788):** Attempted to use a non-existent tool (`stun_npc`). I must only use tools provided in the game context.