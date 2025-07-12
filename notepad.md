# I. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls, except for Pikachu.
- **Grass:** Walkable tiles where wild Pokémon can be encountered.
- **Water:** Surfable tiles. To initiate SURF, I must be **facing the water** on a `ground` or `steps` tile and then use the move from the party menu.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. 
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message. The water on Seafoam Islands B4F has a scripted current that prevents surfing south.
- **Hidden Passages:** Some maps contain hidden passages that allow traversal through what appear to be solid walls.
- **Invisible Barriers:** Some areas contain invisible, impassable barriers that are not tied to a specific tile type. Their presence may be linked to NPC positions or other puzzle mechanics.
- **Cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after cutting.
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles.
- **Elevated Ground:** Walkable ground at a different elevation, accessible only via `steps`.
- **Secret Switches:** Some statues contain hidden switches. Activating them can toggle the state of nearby gates, opening new paths. 
- **Warp Tiles:** Instantaneous teleporters between maps or within the same map. Must step off and back on to reuse.
- **Hole Tiles:** One-way warps that cause the player to fall to the floor below, often into isolated areas.
- **Unknown Tiles:** Tiles not yet seen (`seen="false"`). Treated as impassable until explored.
- **Positional Triggers:** Specific tiles that, when stepped on, can open or close gates or trigger other events elsewhere on the map. The effect may be reversed by stepping off the tile, or it may be permanent until another trigger is activated. Example: Stepping on (11, 4) on Pokemon Mansion 3F opens the gates at (16, 5) and (16, 6).
- **Gate Offscreen/Closed/Open:** Gates whose state (unknown, impassable, or passable) depends on whether they are on-screen and whether a controlling switch has been activated.

## B. Confirmed ROM Hack Changes
### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground
- **Immunities:** Flying-type immune to Ground-type moves; Ground-type Pokémon are immune to Electric-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move).

### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **Run from Battle Mechanic:** Attempting to switch Pokémon from the party screen can sometimes result in running from the battle instead.

## C. Area & Navigation Insights
- **Rock Tunnel B1F:** This area is divided into multiple isolated sections. The eastern ladder at (34, 26) is not accessible from the central corridor entrance.

# II. Current Puzzles & Hypotheses

## Pokemon Mansion 3F - Moving Super Nerd Puzzle
- **Observation:** The Super Nerd at (7, 12) moves based on my position. His movement seems designed to block me, but the core mechanic is a 'reset' based on my own position.
- **Key Discovery (Hypothesis 4 Confirmed):** The Super Nerd's reset position is dependent on my X-coordinate when I step off row 12 to trigger the reset. Resetting from X=8 put him at (6, 12). Resetting from X=10 put him at (9, 12).
- **Active Hypothesis:** I need to find the correct X-coordinate to stand on when I trigger the reset, which will move the Super Nerd to a position that unblocks the path at (2, 12).
- **Test Plan:** Systematically test reset positions by moving along row 12, stepping up to row 11 to trigger the reset, and documenting the Super Nerd's new position each time.

# III. Future Development Ideas
- **`puzzle_solver_tool`:** Create a computational tool that can analyze NPC movement patterns based on player input logs to solve herding or path-blocking puzzles more efficiently.

# IV. Archive: Solved Puzzles & Invalidated Hypotheses
- **Seafoam Islands B4F Path:** The western and eastern sections are completely isolated from each other.
- **Pikachu Puzzle Room (SOLVED):** Required starter Pikachu (SPARKY) in the lead to make the NPC Pikachu disappear. The reward for solving this puzzle is a RARE CANDY at (11, 3), NOT the Secret Key.
- **Rock Tunnel B1F - Walk-Through NPC (INVALIDATED):** My previous note claimed the Super Nerd at (4, 6) was walkable. Repeated attempts (Turns 64707, 64708, 64709) have proven this false. He consistently blocks movement.
- **Hypothesis (INVALIDATED):** The hole at (13, 15) on 3F leads to the Secret Key. (Test: Jumped down hole. Conclusion: Landed in isolated room on 1F. No key.)
- **Hypothesis (INVALIDATED):** The Secret Key is located somewhere in Diglett's Cave. (Test: Systematically explore with Itemfinder. Conclusion: No key found.)
- **Hypothesis (INVALIDATED):** The Secret Key is in the western area of the Pokémon Mansion B1F. (Test: Explored west of gates at (14, 23). Conclusion: Dead end with Full Restore.)
- **Hypothesis (INVALIDATED):** The Scientist at (28, 12) in the B1F isolated room has a way out. (Test: Talked to Scientist. Conclusion: Generic dialogue. Trapped, had to black out.)
- **Moving Super Nerd Puzzle - Hypothesis (INVALIDATED):** I can solve the puzzle by herding the Super Nerd into the eastern corner. (Test: Attempted to move west. Conclusion: Blocked by invisible walls at (3,12) and (4,12).)

# V. Core Principles & Lessons Learned
- **Immediate Maintenance is Paramount:** Deferring tool/agent/notepad maintenance is a critical process failure. I must be vigilant in correcting this.
- **Agent Trust is Mandatory:** I MUST trust my custom agents' advice, even if it contradicts my own intuition. Their purpose is to perform complex reasoning I cannot. If an agent is wrong, I must refine it, not ignore it.
- **Mandatory Agent Usage:** I must always defer to my specialized agents for tasks they are designed for. Manual intervention in such cases is a critical process failure.
- **Confirmation Bias Warning:** I exhibited significant confirmation bias during the Diglett battles (Turns 65244-65253) and the Super Nerd puzzle. I repeatedly trusted my flawed assumptions instead of direct feedback from the game. **Lesson:** The game's outcome is the ultimate source of truth. If a tool or agent's advice is proven wrong by the game, I must immediately distrust it, refine it, and re-evaluate my strategy based on the observed facts.
- **CRITICAL MISTAKE (Turn 65511):** I hallucinated having 8 badges and overwrote my notepad with incorrect goals. I must always verify assumptions against the game state.
- **CRITICAL HALLUCINATION (Turn 66661):** I hallucinated an NPC's location and created a faulty map marker. I must be more diligent in verifying my assumptions against the game state data.
- **Blackout Strategy is Unreliable:** Attempting to intentionally lose a wild battle is not a reliable method for escaping a location.
- **Documentation Failure (Turn 67591):** I failed to consult my own map marker ('🚫 Isolated Dead End from 2F') and wasted time trying to find a non-existent path. I must check my markers before planning any navigation.
- **Faulty Tool Deletion:** Do not rely on faulty tools; they must be fixed or replaced immediately.