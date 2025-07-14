# I. Core Principles & Lessons Learned
- **Immediate Maintenance & Escalation:** I must perform maintenance (notepad, agents) and escalate to powerful tools (like the `puzzle_solver_agent`) *immediately* when a manual approach fails repeatedly. Deferring these actions is a critical process failure.
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
- **Pokemon Mansion - Alternating Doors:** Confirmed by a Super Nerd on 2F. The mansion has at least two sets of gates controlled by two different switches. Switch 1 (1F, (3, 6)) controls one set of gates. Switch 2 (2F, (3, 12)) controls another set. Activating a switch toggles the state of its corresponding doors.
- **Pokemon Mansion 1F - Eastern Wing Gate & Positional Trigger:** The gate at (25, 14) is controlled by the switch at (3, 6). Additionally, a positional trigger at (12,10) on 1F closes the gates at (17,8) and (18,8). The switch at (3,6) re-opens them. Direct interaction with the gate does not work.

# IV. Tool Usage & Limitations
- **Type Matchup Correction:** Previously noted that RATICATE's DIG (Ground) being super-effective against SPARKY (Electric) was unusual. This is actually the standard, correct type matchup. My understanding was flawed.
- **THUNDERBOLT vs. DIG:** THUNDERBOLT can hit an opponent while it is underground using DIG. This is contrary to standard mechanics and resulted in an accidental knockout when trying to faint.

# V. Active Puzzles
## A. Pokemon Mansion 3F - Trapped Eastern Corridor
- **Observation:** Trapped in a corridor on the eastern side of 3F after a series of warps. No visible exits.
- **Hypothesis 1 (Failed):** A hidden switch is on the northern wall.
  - **Test:** Interacted with every tile of the northern wall.
  - **Conclusion:** No switches found.
- **Hypothesis 2 (Failed):** A hidden pitfall trap is on the floor.
  - **Test:** Walked over every single floor tile.
  - **Conclusion:** No pitfalls found.
- **Hypothesis 3 (Failed):** A secret passage exists in the southern wall.
  - **Test:** Systematically attempted to walk south into every tile of the southern wall from x=2 to x=6.
  - **Conclusion:** The wall is solid. All simple hypotheses for escape have been exhausted.
- **Hypothesis 4 (Failed):** The southern wall is a one-way ledge.
  - **Test:** Attempted to walk south into the impassable wall at (2, 18).
  - **Conclusion:** The wall is impassable, not a ledge. The 'jumping off' hint may apply elsewhere or be metaphorical.
- **Hypothesis 5 (Failed):** The corridor is an intentional trap, requiring a field move like Dig to escape.
  - **Test:** Checked inventory for TM28 (Dig). It is not present.
  - **Conclusion:** This escape method is not currently possible.
- **Hypothesis 6 (Failed):** There is a hidden switch on one of the floor tiles in the corridor.
  - **Test:** Stood on each tile from (2, 17) to (6, 17) and pressed the A button.
  - **Conclusion:** No switches found.
- **Hypothesis 7 (Failed):** A secret passage exists in the eastern or western walls.
  - **Test:** Interacted with the eastern wall at (7, 17) and the western wall at (1, 17).
  - **Conclusion:** No switches or passages found.
- **Hypothesis 8 (Failed):** Accidentally won the battle while trying to faint.
  - **Test:** Found a wild Raticate and deliberately tried to lose the battle to trigger a 'black out'.
  - **Conclusion:** The test is invalid and needs to be repeated.
- **Hypothesis 9 (Active):** The 'black out' escape mechanic failed previously due to an unknown condition (accidentally winning), but re-testing it is necessary as game states can change.
  - **Test Plan:** Find a wild Pokémon and deliberately lose the battle to trigger a 'black out'.
- **New Immunity Observed:** POISON GAS (Poison) had no effect on REVENANT (MAROWAK, Ground-type).