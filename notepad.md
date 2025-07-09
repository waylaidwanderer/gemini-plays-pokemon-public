## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Grass:** Walkable tiles where wild Pokémon can be encountered.
- **Water:** Surfable tiles. To initiate SURF, I must be adjacent to a water tile and use the move from the party menu. Only Water-type Pokémon can use SURF in the field.
- **Gates (`closed_gate`/`open_gate`/`gate_offscreen`):** `closed_gate` tiles are impassable. `open_gate` tiles are open and act as `ground`. `gate_offscreen` represents a gate whose state is unknown because it's not on screen. The state of these can be toggled by switches or other triggers.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message. The tile at (4, 5) in the Trashed House is an invisible wall.
- **Hidden Passages:** Some maps contain hidden passages that allow traversal through what appear to be solid walls.
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

## II. Current Hypotheses & Puzzles

### A. Primary Hypothesis: Exploring Route 20
- **Objective:** Fully explore Route 20 to find clues or items.
- **Current Hypothesis:** The Secret Key for Cinnabar Gym is not on Cinnabar Island. Exploring other areas, like Route 20 and the Power Plant, is the next logical step.
- **Test Plan:** Systematically explore Route 20, battle all trainers, and investigate the Seafoam Islands.

## III. Tool & Agent Development Log

### A. Tool Maintenance Log
- **`find_path` tool failures (Turns 59503 - 59576):** The tool has repeatedly failed due to a flawed script. The issues included: not automatically finding adjacent paths to impassable tiles, not recognizing `cuttable` tiles, and not handling one-way `ledge` traversal. These issues were fixed through multiple, delayed revisions.
- **`exploration_assistant_agent` failures (Turns 59551, 59554):** The agent initially used flawed fuzzy logic to match markers to sprites, resulting in useless plans. It was refined to require exact coordinate matching.

## IV. Lessons Learned & Process Improvement
- **Immediate Maintenance is Paramount:** The repeated failure to fix `find_path` immediately was a critical process violation. Tool/agent/notepad maintenance MUST be performed as the highest priority upon identifying an issue. Deferring these tasks is unacceptable.
- **Thorough Tool Testing:** After creating or modifying a tool, I must test it in various scenarios, including edge cases, to ensure it is robust.
- **Challenge Assumptions:** My initial assumption that the Secret Key *must* be on Cinnabar Island led to wasted time. I need to be more open to non-local solutions and rigorously test my core beliefs.
- **Critical Process Failure (Turns 60052-60124):** I repeatedly deferred immediate and necessary maintenance on my `find_path` tool and `battle_strategist_agent`. Instead of fixing them the moment a flaw was identified, I attempted manual workarounds, which is a severe violation of my operational directives. This pattern of creating mental to-do lists instead of taking immediate action must be corrected.

## V. Archive: Solved Puzzles & Disproven Hypotheses
- **Secret Key (Power Plant - DISPROVEN):** Explored the Power Plant and battled the trainer Craig. No key was found.
- **Paused Puzzle: Route 9 Trainer (Cool Trainer M2):** Paused after 4 failed hypotheses. The trigger is not obvious.
- **Secret Key (Cinnabar Coast - DISPROVEN):** Surfed along the entire coastline of Cinnabar Island and found no hidden paths or items.
- **Secret Key (Mr. Fuji - DISPROVEN):** Spoke to Mr. Fuji in Lavender Town. He provided only his standard post-rescue dialogue about the POKé FLUTE.
- **Secret Key (Cinnabar Lab - DISPROVEN):** Concluded the Secret Key is not in the Cinnabar Lab after interacting with all NPCs and objects.
- **Secret Key (Pokemon Mansion - DISPROVEN):** Concluded the Secret Key is not in the Pokémon Mansion after a thorough search of all floors and switches.
- **Secret Key (Cinnabar Island - DISPROVEN):** After a thorough search of the Pokémon Mansion and Cinnabar Lab, I have concluded the key is not on the island.
- **Cinnabar Lab (Photo - DISPROVEN):** Interacted with the photo of Dr. Fuji at (4, 3). It provided only flavor text.
- **Cinnabar Gym (Bypass - CONFIRMED):** The scripted event at the gym door (19, 5) can be bypassed by using SURF from the eastern coast to navigate to the western side of the island.
- **Pokemon Mansion B1F (Gate Switch):** A switch at (19, 26) toggles two sets of gates using a 'prime and trigger' mechanic. Flip the switch to prime a set, then walk to them to open.
- **Pokemon Mansion 1F (Statue Switch):** A secret statue switch at (3, 6) opens the eastern gates at (17,8).
- **Pokemon Mansion 3F (Alternating Gates - SOLVED):** The switch at (11, 6) toggles two sets of gates. Activating it opens the northern gates at (16, 5-6) and closes the southern gates at (16, 11-12).
- **Pokemon Mansion 1F (Alternating Gates - Confirmed):** Walking through the gates at (17, 8) and (18, 8) causes them to close. This confirms the alternating door mechanic is present on this floor, likely controlled by the statue switch at (3, 6).

## VI. Future Agent & Tool Ideas
- **Inventory Advisor Agent:** An agent that analyzes my inventory and Pokémon to suggest optimal TM usage or stat-booster allocation for long-term team planning.
- **Navigation Planner Agent:** An agent that can create multi-step navigation plans that incorporate using HMs like SURF and FLY, breaking down complex routes into a sequence of traversable paths.
- **Find HM Spot Tool:** A tool that can scan adjacent tiles to find a valid location to initiate an HM field move like SURF or CUT. This would prevent wasting time on repeated failed attempts.