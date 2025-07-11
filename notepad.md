# I. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls, except for Pikachu.
- **Grass:** Walkable tiles where wild Pokémon can be encountered.
- **Water:** Surfable tiles. To initiate SURF, I must be on a `ground` or `steps` tile adjacent to water and use the move from the party menu.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
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
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move).
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
- **Immediate Maintenance is Paramount:** Deferring tool/agent/notepad maintenance is a critical process failure. It MUST be performed as the highest priority upon identifying an issue. I have repeatedly made this mistake and must be vigilant in correcting it.
- **Agent Trust is Mandatory:** I MUST trust my custom agents' advice, even if it contradicts my own intuition. Their purpose is to perform complex reasoning I cannot. If an agent is wrong, I must refine it, not ignore it. Ignoring agent advice is a critical process failure.
- **Mandatory Agent Usage:** I must always defer to my specialized agents for tasks they are designed for. Manual intervention in such cases is a critical process failure.

# III. Active Hypotheses & Tests
- **Hypothesis:** The Secret Key is located in the Power Plant.
- **Test:** Navigate to the Power Plant and explore it thoroughly.

# IV. Goal Revisions & Strategic Shifts
- **Badge Count Correction:** I previously believed I had all 8 badges. I have re-evaluated and confirmed I only have 6. My new primary goal is to obtain the Volcano and Earth badges. The immediate objective is to find the Secret Key for the Cinnabar Gym.

# V. Archive: Solved Puzzles & Abandoned Strategies
- **Pathfinding Tool Catastrophe (Turns 64411-64534):** My initial pathfinding tools (`find_path`, `v2`, `v3`) were fundamentally flawed and led to an unproductive loop of failed navigation and attempted fixes. This was a critical process failure where I ignored documented conclusions and persisted with a broken strategy. **Lesson:** Trust documented conclusions and do not repeat failed strategies. A robust, new tool (`find_path_v4`) was successfully developed in turn 64569 to correct this.
- **Seafoam Islands B4F Path (DISPROVEN):** The western and eastern sections of Seafoam Islands B4F are completely isolated from each other.
- **Pikachu Puzzle Room (SOLVED):** The puzzle required having the starter Pikachu (SPARKY) in the lead. Interacting with the NPC Pikachu under this condition caused it to disappear, solving the puzzle.
- **Pokémon Mansion 1F - Gate Puzzle (SOLVED):** The mansion's gates are a complex puzzle. The switch at (3, 6) toggles the state of both the western gates (17,8 & 18,8) and the eastern gates (25,14 & 26,14). However, there are also positional triggers. Walking in the central corridor around (12,8) closes the western gates. Walking in the eastern corridor around (27,10) closes the eastern gates. The solution is to flip the switch to open the desired set of gates and then approach them without crossing the trigger lines for the other set.

# VI. Future Development & Ideas
- **Prerequisites Check:** Before entering new dungeons or major areas, I must verify that all necessary HMs (Flash, Cut, Surf, Strength) and key items are in my party or inventory to avoid backtracking.
- **Puzzle Solver Agent:** Create an agent that takes a description of a room/puzzle (tile types, object locations, NPC dialogue) and suggests testable hypotheses for how to solve it. This could help when I'm stuck on environmental puzzles by providing structured, logical steps for experimentation.

# VII. Discovered Exceptions & Glitches
- **Walk-Through NPCs:** Some NPCs that block paths are not solid and can be walked through. Confirmed with the Super Nerd at (4, 6) in Rock Tunnel B1F, who remains stationary and can be passed by walking directly onto his tile. This appears to be an exception, not a general rule for all blocking NPCs.

# III. Active Hypotheses & Tests
- **Hypothesis:** The Secret Key is located in the Power Plant.
- **Test:** Navigate to the Power Plant and explore it thoroughly.
- **Contingency Hypothesis:** If the Secret Key is not in the Power Plant, it may be held by an NPC on Cinnabar Island or hidden elsewhere in the world, requiring more widespread exploration.