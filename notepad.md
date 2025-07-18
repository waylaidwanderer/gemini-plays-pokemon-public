# Gem's Pokémon Crystal Notepad

## II. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance.
*   **Heal the Sick Miltank (Route 39):** The Miltank in the barn needs 'lots of BERRIES'. I need to find a source of berries.
*   **Get FIRE STONE (Route 36):** My item bag is full due to a complex inventory bug. This quest is on hold.

### B. Untested Assumptions & Hypotheses
*   **HM02 (Fly):**
    *   **Hypothesis:** The HM is obtained from Chuck's wife in Cianwood City after defeating him, but the event was bugged.
    *   **Alternative:** The HM is obtained elsewhere. The interaction with Chuck's wife was misremembered or for a different item.
    *   **Test:** After defeating Chuck, if I still don't have Fly, I will speak to every NPC in Cianwood City. If that fails, I will search other locations.
*   **Mahogany Town Gym Block:**
    *   **Hypothesis:** The Fisher will move after I defeat the next Gym Leader (Chuck).
    *   **Alternative:** The trigger is related to the Goldenrod Radio Tower plotline.
    *   **Test:** After defeating Chuck, I will immediately check the Fisher. If he's still there, I will investigate the Radio Tower.
*   **Inventory/PC Bug:**
    *   **Hypothesis:** The bug preventing depositing/tossing specific items is universal.
    *   **Alternative:** The bug is specific to the Violet City Pokémon Center PC or certain items.
    *   **Test:** At the next available Pokémon Center, I will attempt to use the PC to deposit and toss various items.

## II. Game Mechanics

### A. Tile Traversal Rules
*   **WALL/VOID:** Impassable boundary tiles.
*   **FLOOR:** Standard traversable tile.
*   **GRASS/TALL_GRASS:** Traversable; can trigger wild encounters.
*   **DOOR/CAVE/LADDER/WARP_PANEL:** Standard warp tiles. LADDER is a standard two-way warp. DOOR is a standard warp tile that is sometimes locked or blocked by story events.
*   **WATER/SEA:** Traversable only with SURF. Can trigger wild encounters.
*   **LEDGE/LEDGE_HOP_DOWN:** One-way traversal. Can be jumped down but not climbed up.
*   **LEDGE_HOP_LEFT:** One-way traversal. Can be jumped left but not entered from the right.
*   **LEDGE_HOP_RIGHT:** One-way traversal. Can be jumped right but not entered from the left.
*   **PIT:** One-way tile that causes a fall to the floor below.
*   **COUNTER/MART_SHELF/BUOY/WHIRLPOOL:** Impassable. Interacting with NPCs behind counters requires facing the counter tile, not the NPC.
*   **PC:** Impassable. Interacted with by standing on the tile below it, facing up, and pressing 'A'.
*   **TREE/CUT_TREE:** Small trees can be cut with CUT, leaving an impassable stump. To use CUT, the player must be standing on an adjacent tile and facing the tree directly.
*   **BOULDER:** Can be moved with STRENGTH.
*   **HEADBUTT_TREE:** Interactable tree for finding Pokémon. Impassable.
*   **ROCK_SMASH_BOULDER:** Can be crushed with the move ROCK SMASH.
*   **WARP_CARPET_DOWN/RIGHT/LEFT:** Directional warp tile. **Confirmed Mechanic:** Activated by standing on the tile and pressing the corresponding direction button (e.g., 'Down' for WARP_CARPET_DOWN).
*   **FLOOR_UP_WALL:** Impassable from below, acts as a one-way ledge when approached from above.

### B. Key Items & HM Usage
*   **SQUIRTBOTTLE:** Used to wake up the Sudowoodo blocking Route 36.
*   **HM01 (CUT):** Cuts small trees. Learned by Feraligatr.
*   **HM02 (FLY):** Allows instant travel to previously visited towns. Received from Chuck's wife in Cianwood City. **Currently Unreliable.** **Hypothesis:** This is a story-based block, not a bug, possibly related to the Radio Tower or the Mahogany Town Gym. **Test:** After defeating the Mahogany Gym Leader, attempt to use Fly again.
*   **HM03 (SURF):** Allows travel over water. Learned by Feraligatr.
*   **HM04 (STRENGTH):** Moves large boulders.
*   **HM05 (FLASH):** Illuminates dark caves. Learned by Hoothoot.
*   **HM08 (ROCK SMASH):** Can be used to break certain rocks. Received from a Fisher on Route 36.
*   **DIG:** Can be used to escape caves and some buildings, returning to the entrance. Disabled in Cianwood Gym.

### C. Other Systems
*   **Everstone:** A Pokémon holding this item will not evolve.
*   **Phone Calls:** NPCs can call to offer hints, battle rematches, or flavor text.
*   **Happiness:** Increased by haircuts and using items on Pokémon. Required for some evolutions (like Togepi).
*   **Day/Night Cycle:** Affects which Pokémon appear.
*   **Bug-Catching Contest:** Held on Tuesdays, Thursdays, and Saturdays in the National Park.
*   **PC Item Deposit:** The menu navigation seems to be bugged or have a non-intuitive control scheme. **Hypothesis:** The game is returning to the item list without finalizing the deposit. The correct sequence may involve pressing 'B' after confirming quantity, or a specific item cannot be deposited. **Test:** Attempt to deposit a different item (e.g., BERRY).

## I. Methodology & Automation

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Carefully analyze the situation's initial state using the map, object data, and any relevant NPC dialogue.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis about a specific mechanic. State alternative hypotheses.
3.  **Test:** Execute the simplest possible sequence of actions to test the hypothesis. Design tests to potentially *falsify* the hypothesis.
4.  **Conclude & Document:** Record the result of the test. Was the hypothesis confirmed or falsified? Update this notepad accordingly.
5.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests. **CRITICAL:** I must consult existing markers *before* forming a plan to avoid repeating actions or battling defeated trainers.

### B. Automation & Agent Usage
*   **Automation First:** For any recurring puzzle type, my first step will be to define a custom tool to solve it computationally. If a tool fails, my top priority is to fix it, not to abandon it.
*   **Agent Consultation:** I must make a conscious effort to use my defined agents when appropriate, especially my `navigation_advisor` when I feel stuck.
*   **Immediate Action Mandate (CRITICAL):** As an LLM, I have no concept of 'later'. All data management tasks (updating this notepad, placing/deleting markers, fixing tools/agents) **MUST** be performed in the immediate turn of discovery.

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

*   **PC Item Management (Violet City):** The 'DEPOSIT ITEM' and 'TOSS ITEM' functions appear to be bugged. When selected, they only allow interaction with the first item in the bag (e.g., MOON STONE) and provide no way to select other items. This makes the PC unreliable for general inventory management. The only viable workaround is to have a Pokémon hold an item to free up a slot.

**Reflection (Turn 52322):** I got stuck in a loop trying to use the faulty PC in Violet City and completely forgot to consult my `navigation_advisor` agent. This is a major process failure. I must remember to use my agents when I encounter obstacles or feel stuck, instead of just brute-forcing a solution.