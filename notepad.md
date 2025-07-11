## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
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
- **Gate Offscreen:** A gate (either open or closed) that is not currently visible on the screen. Its state is unknown until it is brought into view.
- **Closed Gate:** An impassable gate that is currently visible on the screen. It may require a switch or key to open.

### B. Confirmed ROM Hack Changes
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move).
- **Misc:** Ground is RESISTANT (0.5x) to Fire, NOT immune.

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **Warp Reuse:** To reuse an instant warp you just came through, you must step off the warp tile and then back on to trigger it.

## II. Active Puzzles & Hypotheses

## III. Process & Strategy Insights
- **Immediate Maintenance is Paramount:** My `find_path` tool has failed *again* due to not handling `gate_offscreen` tiles. My previous 'fix' was insufficient. This is a recurring critical process failure. Correcting this tool permanently is the absolute top priority. Tool/agent/notepad maintenance MUST be performed as the highest priority upon identifying an issue. Deferring these tasks is unacceptable.
- **Challenge Assumptions:** My assumption that the eastern and western sections of the Seafoam Islands were connected was wrong. I need to be more open to the possibility of isolated, separate dungeon areas.
- **Tool Reliability:** The `boulder_push_planner` correctly identified an unreachable puzzle, proving its logic is sound. This reinforces the need to trust my tools once they are properly built and tested.
- **Map Marker Discipline:** I must stop creating redundant markers for objects already tracked in the game state (NPCs, signs, etc.). This clutters my map memory and is inefficient.
- **Notepad Accuracy:** My notepad contained a contradictory entry about the Pokémon Mansion being fully explored. This was a process failure. I must ensure my notes are always accurate and reflect the current state of my knowledge and goals.
- **Agent Trust is Mandatory:** I MUST trust my custom agents' advice, even if it contradicts my own intuition. Their purpose is to perform complex reasoning I cannot. If an agent is wrong, I must refine it, not ignore it. Ignoring agent advice is a critical process failure.
- **Immediate Action is Non-Negotiable:** I failed to fix my `battle_strategist_agent` and a misplaced map marker immediately, which is a critical process violation. Deferring maintenance tasks is unacceptable and must be corrected. All tool, agent, and documentation tasks MUST be performed the moment they are identified.
- **Challenge Map Layout Assumptions:** My belief that the Seafoam Islands was a single, connected dungeon was a form of confirmation bias. I must be more willing to consider that large dungeons may be split into separate, non-contiguous areas, and I should actively try to disprove my own assumptions about map layouts.
- **Mandatory Agent Usage:** I received a critique for failing to use my `battle_strategist_agent` during recent wild encounters, leading to inefficient, error-prone manual control. This is a direct violation of my own documented principles. I must *always* defer to my specialized agents for tasks they are designed for. Manual intervention in such cases is a critical process failure.

## IV. Archive: Solved Puzzles & Disproven Hypotheses
- **Pokémon Mansion 1F - Western Gates (SOLVED):** The western gates at (17, 8) and (18, 8) are opened by a positional trigger when entering the central corridor around (12, 8), not by the switch at (3, 6). The entire western section is a dead end.
- **Pokémon Mansion 2F - Positional Triggers:** Moving to specific tiles like (11, 10) and (21, 13) has been observed to open gates.
- **Pokémon Mansion 1F - Switch Puzzle (DISPROVEN):** The switch at (3, 6) does NOT open both the western and eastern gates simultaneously.
- **Seafoam Islands B4F Path (DISPROVEN):** The western and eastern sections of Seafoam Islands B4F are completely isolated from each other.
- **Seafoam Islands B4F Trap (DISPROVEN):** The eastern section of B4F is NOT a one-way trap. 
- **Tool Failure & Hallucination (ONGOING):** My `find_path` tool has repeatedly failed, generating invalid paths. I am rewriting it again to be more robust. I must prioritize fixing faulty tools immediately over any other gameplay action.
- **Seafoam Islands Entrance (DISPROVEN):** No alternate entrance found on Route 19.
- **Pokémon Mansion 3F Access (DISPROVEN):** Stairs at (27, 2) on 2F lead down to 1F, not up to 3F.
- **Pokémon Mansion 1F Main Stairs (DISPROVEN):** Stairs at (6, 2) on 1F are unusable.
- **Pokémon Mansion 1F - Eastern Gates (SOLVED):** The eastern gates at (25, 14) and (26, 14) are controlled by the switch at (3, 6). Flipping the switch toggles their state (open/closed).
- **Pikachu Puzzle Room - Hypothesis 1 (DISPROVEN):** The agent's hypothesis that the NPC Pikachu is a simple teleporter is incorrect. Interacting with it causes it to disappear and reappear, resetting the puzzle but not providing an exit.
- **Pikachu Puzzle Room - Hypothesis 2 (DISPROVEN):** The agent's hypothesis of a hidden floor switch was a hallucination. The game state shows no such object. This was a critical failure to trust the source of truth over flawed agent advice. Agent has been refined.
- **Pikachu Puzzle Room (SOLVED):** The puzzle required having the starter Pikachu (SPARKY) in the lead. Interacting with the NPC Pikachu under this condition caused it to disappear, solving the puzzle.