# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.
- **Obvious Tile Test:** Even if a tile seems obviously impassable (e.g., WALL), I must attempt to walk into it once to be 100% certain.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `VOID`, `MART_SHELF`, `COUNTER`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters), `LONG_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `STAIRCASE` (Move onto tile).
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`.
*   **Complex Tiles:**
    *   `FLOOR_UP_WALL`: One-way ledge. Enter from below/sides. Cannot exit by moving up.
    *   `WARP_CARPET_LEFT/DOWN`: Activated by pressing the indicated direction while standing on the tile.

### Untested Tile Types (High Priority)
* `RAILING`: Located on the Goldenrod Dept. Store Roof.
* `PIPE_HORIZONTAL`
* `PIPE_VERTICAL`
* `WATER`
* `LINK_CABLE`: Located on Pokecenter2F.
* `TRADE_MACHINE`: Located on Pokecenter2F.
* `CUT_TREE`: Seen on Route 36. Must test passability when reachable.
* `Puzzle Floor Tiles`: In Ruins of Alph chamber.
* `PC`: In Ruins of Alph Research Center.

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
*   **Vending Machine Drinks:** Can refresh tired POKéMON.
*   **Hidden Items:** Must be interacted with from an adjacent tile.
*   **Haircuts:** Increases a Pokémon's happiness.
*   **Pokégear UI:** The Phone function has a modal sub-menu that disables directional buttons. Must press 'B' to exit.

## II. Key Items & TMs
*   **COIN CASE:** Allows playing at the Game Corner.
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge.
*   **SQUIRTBOTTLE:** Used to clear the Sudowoodo on Route 36.
*   **TM08 (ROCK SMASH):** Attack that may lower DEFENSE. Can shatter small rocks.
*   **TM28 (DIG):** Powerful GROUND move. Can escape caves.
*   **TM45 (ATTRACT):** Infatuates opposite-gender Pokémon.
*   **TM49 (FURY CUTTER):** Gets stronger with each consecutive hit.

## III. Active Puzzles & Hypotheses
*   **Radio Tower Side Quests:** Received a BLUE CARD from Buena on the 2nd floor. I can earn points by giving her passwords from the radio and trade them for prizes.
*   **Goldenrod Dept. Store Sale:** Camper Todd called to let me know there's a bargain sale on now.
*   **Team Rocket in Goldenrod:** The Radio Tower entrance is blocked by a Grunt. The Underground seems to be the only other lead. My current hypothesis is that solving a puzzle in the Underground will clear the path in the Radio Tower.
    *   **Alternative Hypothesis:** The trigger for the Team Rocket event is an NPC or event elsewhere in Goldenrod City, and the Underground is a side area. If the Underground is a dead end, I must systematically re-talk to every NPC in the city.
* **Ruins of Alph Puzzle:** The chamber I am in has a puzzle on the north wall. Hypothesis: solving this puzzle is required to progress.
    * **Alternative Hypothesis:** The puzzle is optional, and the real path is through one of the other warps in this area.

## IV. Agent & Tool Development

### Development Ideas
*   **`city_explorer_agent`:** Takes a city name and list of warps as input, then suggests a prioritized order for exploration.
*   **`pokedex_analyst_agent`:** Analyzes the Pokedex and current location to suggest which Pokémon to target for capture.

## V. Misc Info
*   The Bug-Catching Contest is held on Tuesday, Thursday, and Saturday in the National Park.

## VI. Learnings & Mistakes
* **Major Hallucination (Turn 26485-26490):** I mistakenly believed I was in Violet City after taking a map connection from Route 36. I was actually in a small, isolated section of Route 36 the whole time. This led to several wasted turns trying to explore unreachable warps. I must be more careful verifying my location after map transitions and pay attention to system warnings about my position.
* **Interaction Failures:** I have repeatedly failed to interact with NPCs because I was not facing them correctly. I must ensure I am facing the target before pressing 'A'.