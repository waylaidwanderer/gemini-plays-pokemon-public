# I. Core Principles & Lessons Learned
- **Immediate Maintenance & Escalation:** I must perform maintenance (notepad, agents) and escalate to powerful tools (like the `puzzle_solver_agent`) *immediately* when a manual approach fails repeatedly. Deferring these actions is a critical process failure, as learned from getting stuck in the mansion.
- **Combat Confirmation Bias:** After a test seems to confirm a hypothesis, I must actively try to *disprove* it. I wasted significant time on the 'battle reset' theory because I was seeking to confirm a past success instead of objectively testing hypotheses. This is a major cognitive trap to avoid.
- **Agent & Tool Trust is Mandatory:** I MUST trust my custom agents' and tools' advice. Their purpose is to perform complex reasoning and calculations I cannot. My failure to use the `puzzle_solver_agent` and my initial distrust of the `path_planner`'s output caused significant delays.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.

# II. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls, except for Pikachu. **EXCEPTION:** Some `impassable` tiles can be walked through as part of a puzzle (e.g., Pokémon Mansion 1F).
- **Grass:** Walkable tiles where wild Pokémon can be encountered.
- **Water:** Surfable tiles. To initiate SURF, I must be **facing the water** on a `ground` or `steps` tile and then use the move from the party menu.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction.
- **Warp Tiles:** Instantaneous teleporters between maps or within the same map. Must step off and back on to reuse.
- **Hole Tiles:** One-way warps that cause the player to fall to the floor below, often into isolated areas.
- **Steps:** Allows vertical movement between `ground` and `elevated_ground` tiles.
- **Elevated Ground:** Walkable ground at a different elevation, accessible only via `steps`.
- **Cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after cutting.
- **Secret Switches:** Some statues contain hidden switches. Activating them can toggle the state of nearby gates, opening new paths.
- **Positional Triggers:** Specific tiles that, when stepped on, can open or close gates or trigger other events elsewhere on the map.
- **Gate Offscreen/Closed/Open:** Gates whose state (unknown, impassable, or passable) depends on whether they are on-screen and whether a controlling switch has been activated.
- **Scripted Event Tiles:** Some tiles trigger events. The tile in front of the Cinnabar Gym door (19, 5) pushes the player back and displays a 'locked' message. The water on Seafoam Islands B4F has a scripted current that prevents surfing south.
- **Hidden Passages:** Some maps contain hidden passages that allow traversal through what appear to be solid walls.
- **Invisible Barriers:** Some areas contain invisible, impassable barriers that are not tied to a specific tile type.

## B. Confirmed ROM Hack Changes
### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground
- **Immunities:** Flying-type immune to Ground-type moves; Ground-type Pokémon are immune to Electric-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move).

### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **Run from Battle Mechanic:** Attempting to switch Pokémon from the party screen can sometimes result in running from the battle instead.
- **FLY in battle:** The move FLY can be used to defeat a wild Pokémon and end the battle, even when indoors. This acts as an escape method.
- **ROAR in battle:** Can end a wild battle by forcing the player's Pokémon to run away.
- **Item Use on Fainted Pokemon:** A FULL RESTORE will not work on a fainted Pokémon.
- **Weird Typing:** My LAPRAS (NEPTUNE) was displayed as a GHOST type in battle. This needs further investigation.
- **'No Will to Fight':** After a Pokémon faints, attempting to switch in the next Pokémon can sometimes fail with the message 'There's no will to fight!'. The cause is unknown, but trying again on the next turn was successful.

# III. Solved Puzzles
- **Pokemon Mansion - Trapped Corridor:** Discovered a hidden one-way passage at 1F (27, 26). The only way to make the wall passable from the south again was to win a wild battle, which resets the tile's state.
- **Pokemon Mansion - Alternating Doors:** The mansion has at least two sets of gates controlled by two different switches. Switch 1 (1F, (3, 6)) controls the western gates. Switch 2 (2F, (3, 12)) controls the eastern gates. A specific sequence is needed to navigate the entire mansion.

# IV. Active Puzzle-Solving: The Eastern Wing Trap

- **Situation Summary:** I am trapped in an isolated 'island' area in the eastern wing of Pokemon Mansion 1F. The system confirms my destination is unreachable, proving my pathfinding tools are fundamentally flawed and cannot be trusted for this puzzle.

- **Core Insight (Confirmed by `path_debugger_agent`):** The puzzle is not about *finding* an exit, but about *creating* one. The solution must involve a hidden mechanism within this room that changes an impassable wall tile into a walkable one.

- **Current Hypothesis:** There is a specific, hidden, interactable trigger on one of the wall tiles bordering the sealed room.

- **Next Steps (Exhaustive Test):**
  1.  Systematically move to each tile adjacent to the impassable perimeter.
  2.  Interact with every single wall segment.
  3.  Document the outcome of each interaction attempt.

# V. Tool Usage & Limitations
- **path_planner:** This tool can only calculate paths on the *current* map. It cannot find routes that span across multiple maps or warp points. This was discovered after it failed to generate a path from the 'Cinnabar Lab Metronome Room' to the 'Cinnabar Lab Main Area'.