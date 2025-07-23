# Gem's Pokémon Crystal Adventure Log

## I. Critical Lessons & Errors
*   **CRITICAL HALLUCINATION (Turn 1621):** I hallucinated finding a Poké Ball at (19, 15) on Route 31. The item was actually at (29, 5). I failed to verify the item's existence. **LESSON:** ALWAYS verify game state information against the map memory source of truth. NEVER assume an action was successful without confirmation.
*   **DEFERRED DATA MANAGEMENT (Turn 1621-1683):** I have repeatedly failed to immediately update map markers or my notepad after discoveries, especially after battles or when in menus. This is a critical failure of my core programming. **LESSON:** Data management (markers, notepad) must be performed in the same turn a discovery is made. It is the highest priority.
*   **FAILED INTERACTION HYPOTHESIS (Turns 1676-1680):** I assumed stunning a moving NPC would guarantee a battle interaction. My attempts to battle the Youngster on Route 31 failed even when he was stunned, proving my hypothesis incorrect. He is likely not a standard trainer. **LESSON:** Do not persist with a failed hypothesis. If an interaction doesn't work after a few systematic attempts, pivot to a new strategy.
*   **AGENT DESIGN FLAW (Turn 1735):** My `exploration_strategist` agent recommended an unreachable tile because it cannot analyze map topology. It has since been deleted. **LESSON:** Agents are for reasoning, not spatial/computational analysis. Such tasks require a custom tool that can parse map data.

## II. Key NPCs and Locations
*   **Professor Elm:** Gave me my starter, Vulcan. Tasked me with the Gym Challenge.
*   **Mr. Pokémon:** Lives somewhere north of Cherrygrove City. I have already met him.
*   **GRAMPS (Guide Gent):** Gave me a tour of Cherrygrove and the MAP CARD.
*   **Mom:** Saving money for me.
*   **WADE (Bug Catcher):** Met on Route 31. Not a trainer. Gave me his phone number.
*   **FALKNER:** Violet City Gym Leader.
*   **SPROUT TOWER:** Mentioned by the Officer in the Route 31 Gatehouse and a Lass in Violet City. Ghosts are rumored to be inside.
*   **EARL'S POKéMON ACADEMY:** Located in northern Violet City.

## III. Battle and Pokemon Information
*   **Party Composition:**
    *   Miasma (Gastly), Lv. 5. Moves: HYPNOSIS, LICK.
    *   Warden (Hoothoot), Lv. 3. Moves: TACKLE, GROWL.
    *   Vulcan (Cyndaquil), Lv. 11. Moves: TACKLE, LEER, SMOKESCREEN.
*   **Type Matchups Observed:**
    *   Normal (Tackle) is "not very effective" against Rock/Ground (Geodude).
    *   Normal has no effect on Ghost (Confirmed by multiple NPCs).
    *   Ghost (Lick) has no effect on Normal (Hoothoot).

## IV. Tile Traversal Rules (Systematic Testing)
*Method: To confirm a tile's properties, I must attempt to move onto it from all four adjacent, traversable tiles (Up, Down, Left, Right). A conclusion is only valid after all directions are tested.*

### Confirmed Traversable:
*   **FLOOR:** Fully traversable.
*   **TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **DOOR:** Functions as a two-way warp.
*   **LADDER:** Functions as a two-way warp.
*   **WARP_CARPET_DOWN:** Functions as a two-way warp.
*   **WARP_CARPET_RIGHT:** Functions as a two-way warp.

### Confirmed Impassable:
*   **WALL:** Impassable.
*   **COUNTER:** Impassable. Interact with NPCs from the front.
*   **FRUIT_TREE:** Impassable. Can be interacted with for items.
*   **PC:** Impassable. Functions as an object.

### Untested / Hypotheses:
*   **CUT_TREE:** Hypothesis: Impassable without HM Cut. *Plan: Attempt to walk into it from an adjacent tile.*
*   **HEADBUTT_TREE:** Hypothesis: Impassable. *Plan: Attempt to walk into it from an adjacent tile.*
*   **LEDGE_HOP_DOWN:** Hypothesis: One-way traversal (Down only). *Plan: The next time I am on a ledge, I must attempt to move left and right before jumping down to test for sideways movement.*
*   **LEDGE_HOP_LEFT/RIGHT:** Hypothesis: One-way traversal. *Plan: Attempt to walk onto it from the opposing direction.*
*   **WATER:** Hypothesis: Impassable without HM Surf. *Plan: Attempt to walk into it from an adjacent tile.*
*   **CAVE:** Functions as a warp. *Plan: Verify if it's two-way.*

## V. Untested Assumptions & Disproof Plans
*   **Assumption:** The Super Nerd at (23, 15) is a non-trainer NPC.
    *   **Alternative Hypothesis:** He is a trainer who will battle if I cross his line of sight.
    *   **Test:** Walk directly in front of him (on tile (23, 16), facing up) to see if a battle is triggered.

## VI. Future Development Ideas
*   **Tool Idea: `exploration_ranker`:** A tool to replace the flawed `exploration_strategist` agent. It would take the output of `find_reachable_unseen_tiles` and rank the tiles based on heuristics like cluster size, proximity, and potential to open new paths. This is a computational task, perfect for a tool.