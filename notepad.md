## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Grass:** Walkable tiles where wild Pokémon can be encountered.
- **Water:** Surfable tiles. To initiate SURF, I must be adjacent to a water tile and use the move from the party menu.
- **Gates (`closed_gate`/`open_gate`/`gate_offscreen`):** `closed_gate` tiles are impassable. `open_gate` tiles are open and act as `ground`. `gate_offscreen` represents a gate whose state is unknown because it's not on screen. The state of these can be toggled by switches or other triggers.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message. The tile at (4, 5) in the Trashed House is an invisible wall.
- **Hidden Passages:** Some maps contain hidden passages that allow traversal through what appear to be solid walls.
- **Cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after cutting.
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles.
- **Elevated Ground:** Walkable ground at a different elevation, accessible only via `steps`.
- **Water Current:** A scripted event on some water tiles that forces movement in a specific direction, blocking passage. Confirmed on Seafoam Islands B4F at (21,17) and (22,17).

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
- **Warp Reuse:** To reuse a warp you just came through, you must step off the warp tile and then back on to trigger it.

## II. Current Hypotheses & Puzzles

- **Primary Hypothesis:** The Secret Key is likely located somewhere in the Seafoam Islands, obtainable after solving the boulder puzzles which control the water currents.
- **Current Objective:** Escape the trapped western section of Seafoam Islands B4F by blacking out. This area is a one-way trap, likely entered by falling through a hole from B3F.

## III. Lessons Learned & Process Improvement
- **Trust The Data, Not Perception:** My biggest failure was hallucinating a path on Seafoam Islands B4F for over 40 turns. I repeatedly ignored my `find_path` tool's correct output because my manual map analysis was wrong. I must always trust the game state data and my tools over my own flawed perception.
- **Immediate Maintenance is Paramount:** The repeated failure to fix tools and agents immediately was a critical process violation. Tool/agent/notepad maintenance MUST be performed as the highest priority upon identifying an issue. Deferring these tasks is unacceptable.
- **Agent vs. Tool Distinction:** I correctly identified that an agent should not be used for a computational task (parsing map XML). This is a fundamental understanding that must be adhered to. Agents are for reasoning and planning; tools are for computation and data processing.
- **Challenge Assumptions:** My initial assumption that the Secret Key *must* be on Cinnabar Island led to wasted time. My assumption that I could navigate out of the western part of B4F was also wrong. I need to be more open to non-local solutions and rigorously test my core beliefs.

## IV. Archive: Solved Puzzles & Disproven Hypotheses
- **Secret Key (Power Plant - DISPROVEN):** Explored the Power Plant and battled the trainer Craig. No key was found.
- **Secret Key (Cinnabar Island - DISPROVEN):** Thoroughly explored Cinnabar Lab and Pokémon Mansion. No key was found.
- **Secret Key (Mr. Fuji - DISPROVEN):** Spoke to Mr. Fuji in Lavender Town. He provided only his standard post-rescue dialogue.
- **Seafoam Islands B4F Path (DISPROVEN):** The western and eastern sections of Seafoam Islands B4F are completely isolated from each other. There is no path between them on this floor. The southern warps are blocked by a scripted water current.