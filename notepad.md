# I. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls, except for Pikachu.
- **Grass:** Walkable tiles where wild Pokémon can be encountered.
- **Water:** Surfable tiles. To initiate SURF, I must be **facing the water** on a `ground` or `steps` tile and then use the move from the party menu.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. 
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message. The water on Seafoam Islands B4F has a scripted current that prevents surfing south.
- **Hidden Passages:** Some maps contain hidden passages that allow traversal through what appear to be solid walls.
- **Cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after cutting.
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles.
- **Elevated Ground:** Walkable ground at a different elevation, accessible only via `steps`.
- **Secret Switches:** Some statues contain hidden switches. Activating them can toggle the state of nearby gates, opening new paths. 
- **Warp Tiles:** Instantaneous teleporters between maps or within the same map. Must step off and back on to reuse.
- **Hole Tiles:** One-way warps that cause the player to fall to the floor below, often into isolated areas.
- **Unknown Tiles:** Tiles not yet seen (`seen="false"`). Treated as impassable until explored.
- **Gate Offscreen:** A gate (either open or closed) that is not currently visible on the screen. Its state is unknown until it is brought into view. Should be treated as walkable by pathfinding tools.
- **Closed/Open Gate:** An impassable/passable gate that is currently visible on the screen. It may require a switch or key to open, or be controlled by a positional trigger.

## B. Confirmed ROM Hack Changes
### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground
- **Immunities:** Flying-type immune to Ground-type moves; Ground-type Pokémon are immune to Electric-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move).
- **Misc:** Ground is RESISTANT (0.5x) to Fire, NOT immune.

### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **Warp Reuse:** To reuse an instant warp you just came through, you must step off the warp tile and then back on to trigger it.

## C. Area & Navigation Insights
- **Rock Tunnel B1F:** This area is divided into multiple isolated sections. The eastern ladder at (34, 26) is not accessible from the central corridor entrance.

# II. Process & Strategy Insights
- **Immediate Maintenance is Paramount:** Deferring tool/agent/notepad maintenance is a critical process failure. I have repeatedly made this mistake and must be vigilant in correcting it.
- **Agent Trust is Mandatory:** I MUST trust my custom agents' advice, even if it contradicts my own intuition. Their purpose is to perform complex reasoning I cannot. If an agent is wrong, I must refine it, not ignore it. Ignoring agent advice is a critical process failure.
- **Mandatory Agent Usage:** I must always defer to my specialized agents for tasks they are designed for. Manual intervention in such cases is a critical process failure.

# III. Active Hypotheses & Tests
- **Hypothesis (INVALIDATED):** The Secret Key was on the S.S. Anne dock.
  - **Test:** Entered the S.S. Anne warp.
  - **Conclusion:** The ship departed. This was a one-time event and did not yield the key.
- **Hypothesis (INVALIDATED):** The Secret Key is located somewhere in Diglett's Cave.
  - **Test:** Systematically explore Diglett's Cave using the Itemfinder.
  - **Conclusion:** No key found.
- **Hypothesis (INVALIDATED - Attempt 1):** The Secret Key is a hidden item on Pokémon Mansion 2F.
  - **Test:** Used Itemfinder at (4, 22) near the diary.
  - **Conclusion:** Itemfinder did not respond. No hidden item found.
- **Hypothesis (PARTIALLY VALIDATED):** There is a hidden item on Pokémon Mansion 3F.
  - **Test:** Used Itemfinder at (6, 13) near the diary.
  - **Conclusion:** Itemfinder responded. There is an item nearby.
- **Hypothesis (INVALIDATED):** The hidden item is on the tile at (6, 13).
  - **Test 1:** Interact with (6, 13) while facing the diary at (7, 13). **Result:** Read the diary.
  - **Test 2:** Interact with (6, 13) while facing away from the diary at (5, 13). **Result:** Nothing happened.
  - **Conclusion:** The item is not picked up by standing on the tile and pressing A.
- **Hypothesis (INVALIDATED):** The hidden item is on tile (6, 13) and must be interacted with from an adjacent tile.
  - **Test:** Move to (6, 12) and interact with the empty space at (6, 13).
  - **Conclusion:** Nothing happened.
- **Hypothesis (INVALIDATED):** The hidden item is on tile (6, 12).
  - **Test:** Interact with the current tile (6, 12).
  - **Conclusion:** Nothing happened.
- **Hypothesis (INVALIDATED):** The hidden item is on the tile at (6, 13) and is picked up by standing on it.
  - **Test:** Stood on (6, 13) and pressed A.
  - **Conclusion:** Nothing happened.
- **Hypothesis (INVALIDATED):** The hidden item is revealed by interacting with Pikachu, who is at (6, 12).
  - **Test:** Faced Pikachu from (6, 13) and pressed A.
  - **Conclusion:** Nothing happened. The item is not obtained by interacting with Pikachu.
- **Hypothesis (ACTIVE):** The Scientist's hint ('Try jumping off!') is the key. The hidden item is in an area only accessible by falling through a specific hole on 3F.
  - **Test:** Systematically explore the rooms below each hole.
  - **Conclusion:** In progress.
  - **Test:** Systematically explore the remaining floors.
  - **Conclusion:** In progress.

# IV. Archive: Solved Puzzles & Lessons Learned
- **Seafoam Islands B4F Path:** The western and eastern sections are completely isolated from each other.
- **Pikachu Puzzle Room (SOLVED):** Required starter Pikachu (SPARKY) in the lead to make the NPC Pikachu disappear.
- **Pokémon Mansion 1F - Gate Puzzle (SOLVED):** A combination of a single switch and positional triggers control the gates.
- **Rock Tunnel B1F - Walk-Through NPC (INVALIDATED):** My previous note claimed the Super Nerd at (4, 6) was walkable. Repeated attempts (Turns 64707, 64708, 64709) have proven this false. He consistently blocks movement.
- **CRITICAL MISTAKE (Turn 65511):** I hallucinated having 8 badges and overwrote my notepad with incorrect goals. The game state clearly shows I have 6 badges. This was a critical failure in verifying my assumptions. I am reverting my goals to reflect the correct game state.

# V. NPC Trades
- **Route 5 (Underground Path):** Little Girl wants Cubone, offers Machoke.

# VI. Future Development & Lessons

## B. Process Lessons
- **Confirmation Bias Warning:** I exhibited significant confirmation bias during the Diglett battles (Turns 65244-65253). I repeatedly trusted my flawed agent's advice instead of the direct feedback from the game. **Lesson:** The game's outcome is the ultimate source of truth. If a tool or agent's advice is proven wrong by the game, I must immediately distrust it, refine it, and re-evaluate my strategy based on the observed facts. Repeating a failed action based on a flawed tool is a critical process failure.