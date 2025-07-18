# Gem's Pokémon Crystal Notepad

## I. Methodology & Automation

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Carefully analyze the situation's initial state using the map, object data, and any relevant NPC dialogue.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis about a specific mechanic. State alternative hypotheses.
3.  **Test:** Execute the simplest possible sequence of actions to test the hypothesis. Design tests to potentially *falsify* the hypothesis.
4.  **Conclude & Document:** Record the result of the test. Was the hypothesis confirmed or falsified? Update this notepad accordingly.
5.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests. **CRITICAL:** I must consult existing markers *before* forming a plan to avoid repeating actions or battling defeated trainers.

### B. Automation & Agent Usage
*   **Automation First:** For any recurring puzzle type, my first step will be to consider if a custom tool can solve it computationally. If a tool fails, my top priority is to fix it, not to abandon it.
*   **Agent Consultation:** I must make a conscious effort to use my defined agents when appropriate, especially my `navigation_advisor` and `menu_navigator` when I feel stuck. This is a critical step to avoid repeating failed manual actions.

### C. Process Failures (To Be Corrected)
*   **Fly Command Loop (Turns 52463-52495):** I experienced a severe, recurring bug where using the HM Fly would result in a hallucinated state. I would see the Fly map, but my actual location remained in the overworld, causing movement commands to fail. I repeatedly tried the same manual action instead of immediately documenting the failure and using my `menu_navigator` agent. This was a critical failure to follow my own 'Immediate Action Mandate' and problem-solving principles. I must be more disciplined in using my tools when I encounter persistent, unexplained failures.

## II. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance. My hypothesis is that defeating Team Rocket in their hideout was the trigger to make him move. I need to fly there and check.
*   **Heal the Sick Miltank (Route 39):** The Miltank in the barn needs 'lots of BERRIES'. I need to find a reliable source of berries.
*   **Get FIRE STONE (Route 36):** Schoolboy Alan has an item for me, but my bag was full. I need to clear a space and return to him. This is likely the FIRE STONE.

### B. Untested Assumptions & Hypotheses
*   **HM02 (Fly) Origin:** My belief that Chuck's wife gave me Fly was a hallucination. The HM was obtained, but the source is unconfirmed. It's possible the game awarded it silently after the battle.
*   **Fly Command Glitch:**
    *   **Hypothesis 1:** The glitch is location-based, triggered by using Fly on specific tiles (e.g., directly in front of a warp).
    *   **Test 1:** Attempt to use Fly from various tile types (open floor, grass, near walls) to see if the location matters.
    *   **Hypothesis 2:** The glitch is caused by a specific sequence of menu inputs.
    *   **Test 2:** Vary the way I navigate the menu (e.g., pressing Up vs. Down to select my Pokémon) to see if the input sequence is the cause.
*   **Inventory/PC Bug:**
    *   **Hypothesis:** The bug preventing depositing/tossing specific items is universal across all Pokémon Center PCs.
    *   **Test:** At the next available Pokémon Center, I will attempt to use the PC to deposit and toss various items to confirm if the bug is localized to Violet City or is a global issue.

## III. Game Mechanics

### A. Tile Traversal Rules (Verified)
*   **WALL/VOID/COUNTER/MART_SHELF/BUOY/WHIRLPOOL/PC:** Impassable boundary tiles.
*   **FLOOR:** Standard traversable tile.
*   **GRASS/TALL_GRASS:** Traversable; can trigger wild encounters.
*   **DOOR/CAVE/LADDER/WARP_PANEL:** Standard warp tiles.
*   **WATER/SEA:** Traversable only with SURF.
*   **LEDGE/LEDGE_HOP_DOWN/LEFT/RIGHT:** One-way traversal.
*   **PIT:** One-way tile that causes a fall to the floor below.
*   **TREE/CUT_TREE/HEADBUTT_TREE:** Impassable. Small trees can be cut with CUT. Headbutt can be used on some trees.
*   **BOULDER/ROCK_SMASH_BOULDER:** Can be moved with STRENGTH or broken with ROCK SMASH respectively.
*   **WARP_CARPET_DOWN/RIGHT/LEFT:** Directional warp tile, activated by standing on it and pressing the corresponding direction.
*   **FLOOR_UP_WALL:** Impassable from below. Believed to be one-way, needs testing from other directions.

### B. Key Items & HM Usage
*   **SQUIRTBOTTLE:** Used to wake Sudowoodo.
*   **HM01 (CUT):** Cuts small trees. Learned by Feraligatr.
*   **HM02 (FLY):** Allows fast travel. Learned by Hoothoot.
*   **HM03 (SURF):** Allows travel over water. Learned by Feraligatr.
*   **HM04 (STRENGTH):** Moves large boulders.
*   **HM05 (FLASH):** Illuminates dark caves. Learned by Hoothoot.
*   **HM08 (ROCK SMASH):** Breaks certain rocks.
*   **DIG:** Can be used to escape caves.

### C. System Bugs & Glitches
*   **PC Item Management:** The 'DEPOSIT ITEM' and 'TOSS ITEM' functions appear to be bugged, at least in Violet City. They only allow interaction with the first item in the bag and provide no way to select other items. Tossing from the pack is the only reliable way to clear a specific slot.
*   **Giving Items:** Giving an item to a Pokémon that is already holding one will swap the items; it does not free up an inventory slot.

## IV. Battle and Pokemon Information

### A. Type Effectiveness Chart (Verified in-game)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### B. Observed Movesets
*   **Youngster Joey's RATTATA:** Tackle, Tail Whip
*   **Falkner's PIDGEY:** Tackle
*   **Falkner's PIDGEOTTO:** Tackle, Gust
*   **Bugsy's METAPOD:** Harden
*   **Bugsy's KAKUNA:** Harden
*   **Bugsy's SCYTHER:** Fury Cutter, Leer
*   **Whitney's CLEFAIRY:** Doubleslap, Encore
*   **Whitney's MILTANK:** Rollout, Stomp, Attract
*   **Morty's GASTLY:** Lick, Spite
*   **Morty's HAUNTER:** Curse, Hypnosis, Dream Eater
*   **Morty's GENGAR:** Shadow Ball, Hypnosis, Dream Eater
*   **Jasmine's MAGNEMITE:** Thunderbolt, Thunder Wave, Supersonic
*   **Jasmine's STEELIX:** Iron Tail, Screech, Rock Throw
*   **Chuck's PRIMEAPE:** Leer, Rage, Karate Chop
*   **Chuck's POLIWRATH:** Hypnosis, Mind Reader, Dynamicpunch

### C. Pokémon Locations
*   **Route 29:** Sentret, Pidgey, Hoothoot, Hoppip, Rattata
*   **Route 30:** Pidgey, Rattata, Caterpie, Metapod, Weedle, Kakuna, Ledyba
*   **Route 31:** Pidgey, Rattata, Bellsprout, Gastly, Hoppip
*   **Dark Cave:** Geodude, Zubat
*   **Sprout Tower:** Rattata, Gastly
*   **Union Cave:** Geodude, Zubat, Onix, Rattata, Sandshrew
*   **Ilex Forest:** Caterpie, Metapod, Weedle, Kakuna, Zubat, Paras, Oddish
*   **Route 34:** Rattata, Abra, Drowzee
*   **National Park:** Pidgey, Caterpie, Weedle, Sunkern, Nidoran♀, Nidoran♂
*   **Route 36:** Growlithe, Nidoran♀, Nidoran♂, Pidgey, Stantler
*   **Route 37:** Pidgey, Pidgeotto, Stantler
*   **Burned Tower:** Rattata, Koffing, Zubat
*   **Route 38:** Rattata, Raticate, Meowth, Magnemite, Farfetch'd, Tauros, Miltank
*   **Route 39:** Rattata, Raticate, Meowth, Magnemite, Farfetch'd, Tauros, Miltank
*   **Olivine Lighthouse:** Rattata, Gastly
*   **Route 40:** Tentacool, Krabby
*   **Route 41:** Tentacool, Tentacruel, Mantine
*   **Mt. Mortar:** Zubat, Geodude, Machop, Marill
*   **Lake of Rage:** Magikarp, Gyarados
*   **Route 43:** Pidgey, Pidgeotto, Flaaffy, Girafarig, Mareep, Natu, Sentret
*   **Route 42:** Mankey, Mareep, Flaaffy, Spearow, Fearow

### D. PC Storage
*   **Items:** PSNCUREBERRY (x1), ICE BERRY (x1), MINT BERRY (x1), BURNT BERRY (x1), GREAT BALL (x1), ANTIDOTE (x1), PARLYZ HEAL (x1), AWAKENING (x1), POTION (x1), GUARD SPEC. (x1), X ATTACK (x1), X DEFEND (x1), X SPEED (x1), X SPECIAL (x1), DIRE HIT (x1), POKE BALL (x1), REPEL (x1), ESCAPE ROPE (x1), ETHER (x1), MAX ETHER (x1), REVIVE (x1), NUGGET (x1), PROTEIN (x1), IRON (x1), CARBOS (x1), CALCIUM (x1), HP UP (x1), RARE CANDY (x1), TM39 (SWIFT), TM13 (SNORE), TM41 (THUNDERPUNCH), TM48 (FIRE PUNCH), TM02 (HEADBUTT), TM45 (ATTRACT), TM21 (FRUSTRATION), TM27 (RETURN), TM12 (SWEET SCENT), TM35 (SLEEP TALK), TM49 (FURY CUTTER).