## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Water:** Surfable tiles. To initiate SURF, I must be adjacent to a water tile and use the move from the party menu. Only Water-type Pokémon can use SURF in the field.
- **Gates (`closed_gate`/`open_gate`/`gate_offscreen`):** `closed_gate` tiles are impassable. `open_gate` tiles are open and act as `ground`. `gate_offscreen` represents a gate whose state is unknown because it's not on screen. The state of these can be toggled by switches or other triggers.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message.
- **Hidden Passages:** Some maps contain hidden passages that allow traversal through what appear to be solid walls. These can be found using the `advanced_pathfinder` tool.

### B. Confirmed ROM Hack Changes
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying**
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); **Ice !> Gyarados (Water/Flying)**; Poison !> Poison.
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **HYPNO immune to STUN SPORE** (powder moves); **MUK immune to THUNDER WAVE** (Electric-type status move).
- **Misc:** Ground is RESISTANT (0.5x) to Fire, NOT immune.

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **Warp Reuse:** To reuse a warp you just came through, you must step off the warp tile and then back on to trigger it.

## II. Active Puzzles & Hypotheses

### A. Active Puzzle: The Secret Key
- **Objective:** Find the 'Secret Key' for the Cinnabar Gym.
- **Current Leading Hypothesis:** The key is located within the Cinnabar Lab.
- **Test Plan:**
    1. Systematically re-explore every floor (1F, 2F, 3F, B1F).
    2. Interact with every single object (statues, diaries, beds, etc.).
    3. Test every switch multiple times to understand its full effect, including potential effects on other floors.
- **Untested Assumption:** The key is *definitely* in the mansion.
- **Falsification Test:** If a thorough search of the mansion yields no key, I must conclude the assumption is wrong and explore other locations on Cinnabar Island (like the Lab again) or even other towns.

## III. Tool & Agent Development Log

### A. Agent/Tool Brainstorming
- **Idea: `stuck_situation_advisor_agent`:** Create an agent that analyzes the current situation when progress is stalled. It would take the player's position, goal, and known obstacles as input and suggest alternative strategies, such as using HMs in creative ways, looking for hidden paths, or re-evaluating core assumptions.

## IV. Archive

### A. Solved Puzzles Archive
- **Pokemon Mansion B1F (Gate Switch):** A switch at (19, 26) toggles two sets of gates using a 'prime and trigger' mechanic. Flip the switch to prime a set, then walk to them to open.
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).
- **Pokemon Mansion 3F (Alternating Gates - SOLVED):** The switch at (11, 6) toggles two sets of gates. Activating it opens the northern gates at (16, 5-6) and closes the southern gates at (16, 11-12).
- **Pokemon Mansion 1F (Alternating Gates - Confirmed):** Walking through the gates at (17, 8) and (18, 8) causes them to close. This confirms the alternating door mechanic is present on this floor, likely controlled by the statue switch at (3, 6).
- **Idea: `general_party_advisor_agent`:** Create an agent to recommend optimal party composition for general exploration, suggesting swaps from the PC based on the Pokémon and trainer types expected in upcoming routes or dungeons.
- **Cinnabar Lab (Photo):** Interacted with the photo of Dr. Fuji at (4, 3). It provided only flavor text. Hypothesis that it held the key is **disproven**.