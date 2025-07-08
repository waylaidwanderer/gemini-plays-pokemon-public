# Gem's Pokémon Crystal Notepad

## I. Core Directives & Principles
*   **Act Immediately:** As an LLM, I have no concept of 'later'. Any task I decide on (agent/tool creation/refinement, documentation) MUST be performed in the current turn. Deferring tasks is a critical failure.

## II. Strategic Plan
*   **Primary Goal: Obtain the next badge in Ecruteak City**
    *   **Current Hypothesis:** Having exhausted all paths from the National Park, the correct path must be at the junction on Route 36 where the Sudowoodo was.
*   **Secondary Goal: Train the newly hatched ELEKID.**
    *   **Plan:** Keep ELEKID in the party to gain experience from battles.
*   **Tertiary Goal: Investigate the Radio Tower in Goldenrod City**
    *   **Plan:** Return to Goldenrod City after obtaining the next badge and explore the Radio Tower now that I have the Plain Badge.

## III. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.
- **Obvious Tile Test:** Even if a tile seems obviously impassable (e.g., WALL), I must attempt to walk into it once to be 100% certain.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `VOID`, `MART_SHELF`, `WATER` (without Surf), `BUOY`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `COUNTER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `WALL (Fence Appearance)` (Confirmed impassable, even at gaps between posts).
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters), `LONG_GRASS` (Wild Encounters), `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`.
*   **Warps:** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile).
*   **One-Way Ledges:** 
    * `LEDGE_HOP_DOWN/LEFT/RIGHT`.
    * `FLOOR_UP_WALL`: A one-way ledge that can only be hopped **UP**. It is impassable from above (acts as a wall). Confirmed in Union Cave B1F and Slowpoke Well B1F.
*   **Special Requirement:** `CUT_TREE` (Requires HM01 Cut).
*   **Complex Tiles:**
    *   `WARP_CARPET_LEFT/RIGHT`: Activated by pressing the indicated direction while standing on the tile.
    *   `WARP_CARPET_DOWN`: Activated by pressing 'Down' while standing on the tile.
    *   `Push-Down Trap`: A `FLOOR` tile that, when stepped on, pushes the player down one tile. It is a one-way interaction.
    *   `Interactable Warp (FLOOR)`: Some FLOOR tiles that are also warps do not activate on entry. They must be interacted with by pressing 'A' to trigger an event or text. (e.g., Ruins of Alph Inner Chamber @ (15, 3)).

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable and function as walls.
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP.
    *   **ODD EGG:** A special egg received from the Day-Care Man. Hatched into ELEKID.
    *   **HARD STONE:** Powers up rock-type moves.
    *   **PRZCUREBERRY:** Cures paralysis.
    *   **HYPER POTION:** Restores 200 HP.
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

## V. Archive: Solved Puzzles & Procedural Failures
*   **Skepticism Reminder:** Do not assume all NPCs are trainers. Some provide hints or flavor text. Wasting turns trying to battle a non-battling NPC is inefficient. (e.g., Super Nerd in Violet City).
*   **Failure Log (Navigation):** Wasted many turns attempting to find Ecruteak City by heading east on Route 36. This path leads to Violet City. The correct path must lie elsewhere. **Lesson: If a path repeatedly fails to lead to the desired destination, I must abandon the hypothesis and explore other routes instead of persisting.**
*   **Failure Log (Pathfinder v7):** The `explore_unseen` logic in the pathfinder has repeatedly failed due to overly simplistic assumptions. The 'closest unseen' logic failed because it didn't account for pathability. The 'entry point' logic failed because my strategic understanding of the map was flawed. **Lesson: The tool's failure is often a symptom of my own flawed strategy. I must verify my assumptions about the map before blaming the tool.**