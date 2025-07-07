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

## II. Key Items & TMs
*   **COIN CASE:** Allows playing at the Game Corner.
*   **HM01 (CUT):** Clears small trees. Requires Hive Badge.
*   **SQUIRTBOTTLE:** Used to clear the Sudowoodo on Route 36.
*   **TM08 (ROCK SMASH):** Attack that may lower DEFENSE. Can shatter small rocks.
*   **TM28 (DIG):** Powerful GROUND move. Can escape caves.
*   **TM45 (ATTRACT):** Infatuates opposite-gender Pokémon.
*   **TM49 (FURY CUTTER):** Gets stronger with each consecutive hit.

## III. Active Puzzles & Hypotheses

### Ruins of Alph Inner Chamber Puzzle
*   **Goal:** Solve the puzzle to exit the chamber.
*   **Clues:**
    *   Scientist mentioned a strange radio signal is key.
    *   Inscriptions on the wall spell 'LIGHT' and 'ESCAPE'.
    *   Certain floor tiles act as push-down traps, not warps.
*   **Primary Hypothesis (Testing Now):** Tune the Pokégear radio to a specific, strange frequency inside the chamber.
*   **Alternative Hypothesis #1:** The solution involves interacting with the statues in a specific sequence (e.g., spelling out 'LIGHT' or 'ESCAPE' by touching the statues in order).
*   **Alternative Hypothesis #2:** A specific item is required. Could be an item I already have or one I need to find.
*   **Failed Attempts:**
    *   Using FLASH.
    *   Using DIG.
    *   Randomly interacting with statues.
    *   Walking on the push-down floor tiles.

### Team Rocket in Goldenrod
*   **Goal:** Get past the Team Rocket grunt blocking the Radio Tower.
*   **Primary Hypothesis:** Progress is tied to an event in the Goldenrod Underground.
*   **Alternative Hypothesis:** The trigger is an NPC or event elsewhere in Goldenrod City. If the Underground is a confirmed dead end, I must systematically re-talk to every NPC in the city.

## IV. Agent & Tool Development Ideas

## V. Misc Info & Reminders
*   **Bug-Catching Contest:** Tuesday, Thursday, Saturday in National Park.
*   **Goldenrod Dept. Store Sale:** Camper Todd will call about sales.
*   **Radio Tower Side Quest:** Buena's BLUE CARD password show.
*   **SLOWPOKETAIL:** For sale on Route 32. Purpose unknown.

## VI. Learnings & Mistakes
*   **Major Hallucination (Turn 26485-26490):** Misidentified my location on Route 36, thinking I was in Violet City. I must verify my location after every map transition.
*   **Critical Hallucination (Turn 26788):** Attempted to use a non-existent tool (`stun_npc`). I must only use tools provided in the game context.
*   **Procedural Lapses:** I have repeatedly deferred actions instead of acting immediately. This must be corrected. I will act on new information and documentation needs in the same turn they arise.
### Verified Tile Types (Update)
*   **Push-Down Trap:** A floor tile that appears to be a warp but only pushes the player down one tile. It is a one-way interaction; the tile cannot be re-entered from below.

### Procedural Reminders
*   If I am stuck in a repetitive action loop, I must use the `quest_strategist` agent to generate new hypotheses.
*   Pokégear Navigation: Use 'Right'/'Left' to cycle main functions (Clock, Map, Phone, Radio). Use 'B' to exit sub-menus like the phone contact list.

### Quest Strategist Insights (Turn 26934)
*   **New Hypothesis (Top Priority):** The Pokégear functions (Clock, Map, Phone, Radio) might be navigated using **vertical inputs (Up/Down)** instead of horizontal ones. This is a completely new approach to test.