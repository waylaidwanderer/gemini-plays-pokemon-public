# Gem's Pokémon Crystal Adventure Log

## I. Critical Lessons & Errors
*   **CRITICAL HALLUCINATIONS (Turns 1621 & 2043):** I have hallucinated my position and the location of items. **LESSON:** Always trust the game state information over my own memory. Verify everything.
*   **DEFERRED DATA MANAGEMENT (Turns 1621-1683):** I have repeatedly failed to immediately update map markers or my notepad after discoveries. **LESSON:** Data management (markers, notepad) must be performed in the same turn a discovery is made. It is the highest priority.

## II. Key NPCs and Locations
*   **Professor Elm:** Gave me Vulcan. Tasked me with the Gym Challenge.
*   **Mr. Pokémon:** Met him north of Cherrygrove. Task complete.
*   **Mom:** Saving my money.
*   **WADE (Bug Catcher):** Met on Route 31. Gives phone calls.
*   **FALKNER:** Violet City Gym Leader.
*   **SPROUT TOWER:** Cleared! The Elder gave me an HM.
*   **EARL'S POKéMON ACADEMY:** Located in northern Violet City.

## III. Battle and Pokemon Information
*   **Type Matchups Observed:**
    *   Normal is "not very effective" against Rock/Ground.
    *   Normal has no effect on Ghost.
    *   Ghost (Lick) has no effect on Normal.
    *   Grass (Vine Whip) is "not very effective" against Ghost/Poison.
*   **Moveset Notes:**
    *   Miasma (Gastly) learned SPITE at Lv. 8.

## IV. Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **WARP_CARPET_DOWN:** Functions as a two-way warp.
*   **WARP_CARPET_RIGHT:** Functions as a two-way warp.

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **FRUIT_TREE:** Impassable. Can be interacted with for items.
*   **PC:** Impassable. Functions as an object.
*   **VOID:** Impassable. Appears as a black abyss.

### Untested / Hypotheses:
*   **LADDER:** Hypothesis: Functions as a two-way warp. *Plan: Attempt to use from both ends.*
*   **CUT_TREE:** Hypothesis: Impassable without HM Cut. *Plan: Attempt to walk into it from an adjacent tile.*
*   **HEADBUTT_TREE:** Hypothesis: Impassable. *Plan: Attempt to walk into it from an adjacent tile.*
### Confirmed One-Way:
*   **LEDGE_HOP_DOWN:** One-way traversal. Can only be entered from above.

### Untested / Hypotheses:
*   **LADDER:** Hypothesis: Functions as a two-way warp. *Plan: Attempt to use from both ends.*
*   **CUT_TREE:** Hypothesis: Impassable without HM Cut. *Plan: Attempt to walk into it from an adjacent tile.*
*   **HEADBUTT_TREE:** Hypothesis: Impassable. *Plan: Attempt to walk into it from an adjacent tile.*
*   **LEDGE_HOP_LEFT/RIGHT:** Hypothesis: One-way traversal. *Plan: Attempt to walk onto it from the opposing direction.*
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*
*   **CAVE:** Functions as a warp. *Plan: Verify if it's two-way.*
*   **STATUE:** Hypothesis: Non-interactive decoration. *Plan: Interact with a statue to test for any effect.*
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*
*   **CAVE:** Functions as a warp. *Plan: Verify if it's two-way.*
*   **STATUE:** Hypothesis: Non-interactive decoration. *Plan: Interact with a statue to test for any effect.*

## V. Future Development Ideas & Tasks
*   **Task: `marker_fix`:** The marker for the Sage at (12, 3) on SproutTower2F is not linked to its object ID. Must re-define the marker with the correct `object_id` as soon as the Sage is on-screen again.

## VI. Hypothesis Testing
*   **Sprout Tower 1F Exit (Turn 2124):**
    *   **Hypothesis:** The Sage at (3, 5) is a trainer blocking the exit path.
    *   **Test:** Interacted with the Sage.
    *   **Result:** The Sage only provided dialogue ('All living beings coexist...'). He did not initiate a battle.
    *   **Conclusion:** Hypothesis is **false**. The path is not blocked by a trainer battle at this location.

## VII. Gym Battle Strategy
*   **Violet City Gym (Falkner):**
    *   **Known Info:** Uses Flying-type Pokémon.
    *   **My Team:**
        *   Vulcan (Cyndaquil, Fire): Has type advantage with Ember.
        *   Miasma (Gastly, Ghost/Poison): Resistant to Normal-type attacks, but vulnerable to Flying. Lick won't work on Pidgey/Pidgeotto (Normal/Flying). Hypnosis could be useful.
        *   Warden (Hoothoot, Normal/Flying): No clear advantage or disadvantage.
    *   **Plan:** Lead with Vulcan to sweep with Ember. Keep Miasma in reserve for status effects if needed.

## Turn 2203 Reflection
*   **Agent Failure:** `battle_strategist` failed with a server error. I am refining its prompt to be more aware of stat changes.
*   **Gym Puzzle Hypothesis:** My current assumption is that defeating all trainers is the only way to reach the leader. An alternative hypothesis is that there is a hidden switch or puzzle. I will test this by interacting with the gym statues after defeating the trainers.

## VIII. Future Agent Ideas (From Reflection)
*   **Team Composition Advisor:** An agent that takes my current party and PC box Pokémon and suggests an optimal team for upcoming challenges like Gyms.
*   **Nickname Generator:** A creative agent to suggest fun, unique nicknames for newly caught Pokémon, to enhance the stream experience.

## IX. Agent Refinement Log
*   **`battle_strategist` Flaw (Turn 2275):** The agent recommended switching to a Lv 3 Warden to 'preserve' a damaged Miasma. This is a strategic error, as it would sacrifice Warden for no gain. The preservation rule is too rigid and lacks strategic context.
*   **Refinement (Turn 2281):** Updating the agent's prompt to consider the strategic value of a sacrifice. It should weigh the level and potential of the Pokémon being switched in against the risk to the current Pokémon. A low-level, non-viable Pokémon should not be considered a safe switch.
*   **Spite Failure (Turn 2294):**
    *   **Hypothesis:** Spite fails to affect a sleeping target.
    *   **Test:** Used Spite on a sleeping Pidgeotto.
    *   **Result:** The move failed with the message "It didn't affect Enemy PIDGEOTTO!".
    *   **Conclusion:** The hypothesis is likely true. Spite seems to require the target to be awake or to have just used a move.

## X. Battle Mechanics (Hypotheses & Findings)
*   **Spite Failure (Turn 2294):**
    *   **Hypothesis:** Spite fails to affect a sleeping target.
    *   **Test:** Used Spite on a sleeping Pidgeotto.
    *   **Result:** The move failed with the message "It didn't affect Enemy PIDGEOTTO!".
    *   **Conclusion:** Hypothesis is likely true. Spite appears to require the target to be awake.
*   **CRITICAL HALLUCINATION (Turn 2375):** I hallucinated being in a battle when I was not. **LESSON:** Double-check the game state before taking any action. The system warnings are a source of truth.

## XI. Reflection & Maintenance Log (Turn 2411)
*   **Data Management Failure:** I have been deferring marker updates and clean-up. This is a critical error. All data management must be done immediately.
*   **Marker Cleanup:** Deleted redundant 'Fruit Tree' marker and inaccurate 'Unbeaten Trainer' marker.
*   **Tool Creation:** Created `find_reachable_unseen_tiles` to automate exploration planning.
*   **Agent Refinement:** Updated `battle_strategist` prompt to better evaluate strategic switching, preventing sacrifices of low-level Pokémon.
*   **Untested Assumptions:** My belief that certain tiles are impassable without HM moves is untested. I must systematically test all tile types on this route.

## XI. Ledge Traversal Test (Route 31)
*   **Hypothesis:** The `LEDGE_HOP_DOWN` tile at (7, 9) is a one-way traversal point. It can be entered from above (from (7, 8)), but not from below (cannot move from (7, 9) to (7, 8)).
*   **Test Plan:**
    1.  Move Down from (7, 8) to (7, 9).
    2.  Attempt to move Up from (7, 9) to (7, 8).

## XII. NPC Interaction Log
*   **Youngster (Route 31, ID 2):** Interaction only triggers dialogue about finding a Pokémon in Dark Cave to take on Falkner. Does not initiate a battle. Marker updated to reflect this.

## XIII. Immediate Tile Testing Plan (Route 31)
*   **`CUT_TREE` at (13, 5) - Test Complete:**
    *   **Hypothesis:** Impassable without HM Cut.
    *   **Test:** Attempted to walk into the tree from (12, 5).
    *   **Result:** Movement was blocked.
    *   **Conclusion:** Confirmed that `CUT_TREE` is an impassable tile. It likely requires a special ability like HM Cut to remove, but this remains unverified.
*   **`HEADBUTT_TREE` at (13, 4) - Test Complete:**
    *   **Hypothesis:** Impassable but potentially interactable.
    *   **Test 1:** Attempted to walk into the tree from (12, 4). Result: Movement blocked.
    *   **Test 2:** Interacted with the tree using 'A'. Result: No interaction occurred.
    *   **Conclusion:** Confirmed that `HEADBUTT_TREE` is an impassable and non-interactive tile. It likely requires a special ability like HM Headbutt, but this remains unverified.