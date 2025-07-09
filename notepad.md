## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Grass:** Walkable tiles where wild Pokémon can be encountered.
- **Water:** Surfable tiles. To initiate SURF, I must be adjacent to a water tile and use the move from the party menu. Only Water-type Pokémon can use SURF in the field.
- **Gates (`closed_gate`/`open_gate`/`gate_offscreen`):** `closed_gate` tiles are impassable. `open_gate` tiles are open and act as `ground`. `gate_offscreen` represents a gate whose state is unknown because it's not on screen. The state of these can be toggled by switches or other triggers.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message.
- **Hidden Passages:** Some maps contain hidden passages that allow traversal through what appear to be solid walls. These can be found using the `advanced_pathfinder` tool.
- **Cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after cutting.
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles.

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
- **Current Hypothesis:** The key is located in the Power Plant on Route 10.
- **Test Plan:** Travel to the Power Plant and explore it thoroughly.

## III. Tool & Agent Development Log

### A. Tool/Agent Ideas
- **`navigation_supervisor_agent`**: A high-level agent that could plan multi-map journeys. It would analyze the goal, check for required HMs, check the party, and use other tools like `find_path` to execute the journey step-by-step, including PC stops if necessary.
- **`hm_checker_agent`:** To quickly identify which Pokémon in the party or PC knows a specific HM.
- **`pc_pokemon_finder`:** To locate a specific Pokémon across all PC boxes.
- **`find_closest_pokecenter`:** A tool to find the nearest Pokémon Center and provide a fly path if available.

### B. Tool Maintenance Log
- **`find_path` tool failures (Turns 59503, 59513, 59519, 59529):** The tool has repeatedly failed. The root cause is a flawed script. The initial issue was that it did not automatically find a path to an adjacent tile when the destination was impassable. After fixing that, it failed again because its list of traversable tiles was incomplete; it did not recognize `cuttable` tiles.
- **`find_path` tool fix (Turn 59530):** The tool's script is being updated to include `cuttable` in its list of walkable tiles. This should resolve the current issue.

## IV. Lessons Learned
- **Immediate Maintenance:** Tool/agent/notepad maintenance must be performed immediately upon identifying an issue. Deferring these tasks is a critical failure. My repeated failure to fix `find_path` is a prime example of this.
- **Thorough Tool Testing:** After creating or modifying a tool, I must test it in various scenarios, including edge cases, to ensure it is robust. Simply fixing the immediate bug is not enough.
- **Confirmation Bias:** My initial assumption that the Secret Key *must* be on Cinnabar Island led me to exhaust all options there before considering outside locations. I need to be more open to non-local solutions suggested by my agents.

## V. Archive: Solved Puzzles & Disproven Hypotheses
- **Secret Key (Cinnabar Coast - DISPROVEN):** Surfed along the entire coastline of Cinnabar Island and found no hidden paths or items.
- **Secret Key (Mr. Fuji - DISPROVEN):** Spoke to Mr. Fuji in Lavender Town. He provided only his standard post-rescue dialogue about the POKé FLUTE.
- **Secret Key (Cinnabar Lab - DISPROVEN):** Concluded the Secret Key is not in the Cinnabar Lab after interacting with all NPCs and objects.
- **Secret Key (Pokemon Mansion - DISPROVEN):** Concluded the Secret Key is not in the Pokémon Mansion after a thorough search of all floors and switches.
- **Cinnabar Lab (Photo - DISPROVEN):** Interacted with the photo of Dr. Fuji at (4, 3). It provided only flavor text.
- **Pokemon Mansion B1F (Gate Switch):** A switch at (19, 26) toggles two sets of gates using a 'prime and trigger' mechanic. Flip the switch to prime a set, then walk to them to open.
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).
- **Pokemon Mansion 3F (Alternating Gates - SOLVED):** The switch at (11, 6) toggles two sets of gates. Activating it opens the northern gates at (16, 5-6) and closes the southern gates at (16, 11-12).
- **Pokemon Mansion 1F (Alternating Gates - Confirmed):** Walking through the gates at (17, 8) and (18, 8) causes them to close. This confirms the alternating door mechanic is present on this floor, likely controlled by the statue switch at (3, 6).
### C. Route 9 Trainer Puzzle
- **Objective:** Trigger battle with Cool Trainer M2 at (32, 8).
- **Hypothesis 1 (Failed):** Approaching from adjacent tiles (32, 7) or (31, 8) will trigger the battle. *Result: Blocked, no battle.*
- **Hypothesis 2 (Failed):** Jumping down the ledge at (33, 6) will trigger the battle. *Result: No battle triggered.*
- **Hypothesis 3 (Active):** The battle trigger is in the trainer's line of sight at (33, 8). *Test Plan: Move from (33, 7) to (33, 8).*