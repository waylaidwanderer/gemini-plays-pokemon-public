## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Grass:** Walkable tiles where wild Pokémon can be encountered.
- **Water:** Surfable tiles. To initiate SURF, I must be on a `ground` or `steps` tile adjacent to water and use the move from the party menu.
- **Gates (`closed_gate`/`open_gate`/`gate_offscreen`):** `closed_gate` tiles are impassable. `open_gate` tiles are open and act as `ground`. `gate_offscreen` represents a gate whose state is unknown. The state of these can be toggled by switches or other triggers.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message. The water on Seafoam Islands B4F has a scripted current that prevents surfing south.
- **Hidden Passages:** Some maps contain hidden passages that allow traversal through what appear to be solid walls.
- **Cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after cutting.
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles.
- **Elevated Ground:** Walkable ground at a different elevation, accessible only via `steps`.
- **Secret Switches:** Some statues contain hidden switches. Activating them can toggle the state of nearby gates, opening new paths. The switch at (3, 6) on 1F controls the gates at (17, 8) and (18, 8).

### B. Confirmed ROM Hack Changes
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move).
- **Misc:** Ground is RESISTANT (0.5x) to Fire, NOT immune.

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **Warp Reuse:** To reuse an instant warp you just came through, you must step off the warp tile and then back on to trigger it.

## II. Current Hypotheses & Puzzles

- **Primary Hypothesis:** The Secret Key is located somewhere within the Pokémon Mansion. The southern corridor on 1F, accessed via the switch at (3, 6), leads to a new section of 1F and eventually the basement (B1F). The next logical step is to explore the second floor.
- **Pokémon Mansion 2F Layout:** The second floor is divided into at least two separate, non-contiguous sections. The warp to the third floor at (7, 2) is unreachable from the initial entry point.

## III. Process & Strategy Insights
- **Immediate Maintenance is Paramount:** My repeated failure to fix my `find_path` tool immediately was a critical process violation. The tool failed to account for elevation changes, attempting to path directly between `ground` and `elevated_ground`. This has now been corrected. Tool/agent/notepad maintenance MUST be performed as the highest priority upon identifying an issue. Deferring these tasks is unacceptable.
- **Challenge Assumptions:** My assumption that the eastern and western sections of the Seafoam Islands were connected was wrong. I need to be more open to the possibility of isolated, separate dungeon areas.
- **Automation Opportunity:** Manually planning boulder pushes is inefficient. The `boulder_push_planner` tool should automate this. A future `puzzle_strategist_agent` could provide high-level plans for entire floors.
- **Tool Reliability:** The `boulder_push_planner` correctly identified an unreachable puzzle, proving its logic is sound. This reinforces the need to trust my tools once they are properly built and tested.
- **Map Marker Discipline:** I must stop creating redundant markers for objects already tracked in the game state (NPCs, signs, etc.). This clutters my map memory and is inefficient.
- **Notepad Accuracy:** My notepad contained a contradictory entry about the Pokémon Mansion being fully explored. This was a process failure. I must ensure my notes are always accurate and reflect the current state of my knowledge and goals.
- **Agent Trust is Mandatory:** I MUST trust my custom agents' advice, even if it contradicts my own intuition. Their purpose is to perform complex reasoning I cannot. If an agent is wrong, I must refine it, not ignore it. Ignoring agent advice is a critical process failure.
- **Immediate Action is Non-Negotiable:** I failed to fix my `battle_strategist_agent` and a misplaced map marker immediately, which is a critical process violation. Deferring maintenance tasks is unacceptable and must be corrected. All tool, agent, and documentation tasks MUST be performed the moment they are identified.
- **Challenge Map Layout Assumptions:** My belief that the Seafoam Islands was a single, connected dungeon was a form of confirmation bias. I must be more willing to consider that large dungeons may be split into separate, non-contiguous areas, and I should actively try to disprove my own assumptions about map layouts.
- **Mandatory Agent Usage:** I received a critique for failing to use my `battle_strategist_agent` during recent wild encounters, leading to inefficient, error-prone manual control. This is a direct violation of my own documented principles. I must *always* defer to my specialized agents for tasks they are designed for. Manual intervention in such cases is a critical process failure.

## IV. Untested Assumptions & Test Plans
- **Ground vs. Poison:** I am assuming Ground-type moves are super-effective against Poison-types based on standard Pokémon knowledge. This is not confirmed in this ROM hack. 
  - **Test Plan:** The next time CRAG faces a pure Poison-type, I will use EARTHQUAKE and observe the battle text for effectiveness.

## V. Archive: Solved Puzzles & Disproven Hypotheses
- **Secret Key (Power Plant - DISPROVEN):** Explored the Power Plant and battled the trainer Craig. No key was found.
- **Secret Key (Cinnabar Lab - DISPROVEN):** Thoroughly explored Cinnabar Lab. No key was found.
- **Secret Key (Mr. Fuji - DISPROVEN):** Spoke to Mr. Fuji in Lavender Town. He provided only his standard post-rescue dialogue.
- **Seafoam Islands B4F Path (DISPROVEN):** The western and eastern sections of Seafoam Islands B4F are completely isolated from each other. There is no path between them on this floor.
- **Seafoam Islands B4F Trap (DISPROVEN):** The eastern section of B4F is NOT a one-way trap. The game state has confirmed a path to the southern warps exists, despite the water current.
- **Tool Failure & Hallucination (RESOLVED):** My `find_path` tool was critically flawed and repeatedly caused me to hallucinate that I was trapped. I have since rewritten and verified the tool's logic, and it is now reliable. This serves as a reminder to always trust game state data over faulty tools and to prioritize immediate maintenance.
- **Seafoam Islands Entrance (DISPROVEN):** Thoroughly explored Route 19 and found no alternate entrance to the Seafoam Islands. This hypothesis is incorrect.
- **Pokémon Mansion 3F Access (DISPROVEN):** The main staircase on the eastern side of 2F at (27, 2) leads *down* to 1F, not up to 3F. This hypothesis is incorrect.
- **Pokémon Mansion 1F Main Stairs (DISPROVEN):** The main stairs on 1F at (6, 2) are unusable. Attempting to ascend results in being blocked. This path is not viable.