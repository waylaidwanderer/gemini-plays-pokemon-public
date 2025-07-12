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
- **FLY in battle:** The move FLY can be used to defeat a wild Pokémon and end the battle, even when indoors. This acts as an escape method.

## C. Area & Navigation Insights
- **Rock Tunnel B1F:** This area is divided into multiple isolated sections. The eastern ladder at (34, 26) is not accessible from the central corridor entrance.

# II. Current Puzzles & Hypotheses
- **Pokemon Mansion 1F - Escape the East Wing:** I am currently trapped in the eastern wing of the mansion. The exit appears to be a `closed_gate` at (27, 28) and (28, 28). There are no visible switches. Pikachu is standing at (28, 27). Hypothesis: The solution involves interacting with or moving through Pikachu.

# IV. Archive: Solved Puzzles & Invalidated Hypotheses
- **Pokemon Mansion 3F - Moving Super Nerd Puzzle:** Solved. The solution was to leave the floor and return, which resets the NPC's position.
- **Pokemon Mansion 1F - Gate Puzzles:** Solved. The switch at (3, 6) toggles the state of the eastern gates at (25, 14)/(26, 14) and the western gates at (17, 8)/(18, 8). This is an alternating door puzzle confirmed by both observation and NPC dialogue. Stepping on certain tiles also triggers gate closures, requiring careful navigation.

# V. Core Principles & Lessons Learned
- **Immediate Maintenance is Paramount:** I must be vigilant in performing maintenance tasks (notepad, agents, tools) immediately. Deferring them is a critical process failure. I failed at this by not immediately fixing my `pathfinder` tool and notepad.
- **Agent Trust is Mandatory:** I MUST trust my custom agents' advice, even if it contradicts my own intuition. Their purpose is to perform complex reasoning I cannot. If an agent is wrong, I must refine it, not ignore it.
- **Confirmation Bias is Dangerous:** My `pathfinder` tool wasn't broken, my understanding of the map was. I assumed the tool was failing because it didn't match my visual interpretation, leading to wasted time. **Lesson:** Trust the tool's output over visual inspection, as it reads the ground-truth map data. A systematic, evidence-based debugging process (using diagnostic tools and agents) is essential.

# VI. Reminders
- **Team Composition:** Use the `team_composition_advisor_agent` to prepare for the Cinnabar Gym battle against Blaine.
- **Pokemon Mansion 2F - Super Nerd Confirmation:** Spoke to the Super Nerd at (5, 18). He confirmed the alternating door mechanic with the dialogue: 'Switches open and close alternating sets of doors!' This validates my existing puzzle hypothesis but offers no new clues about the SECRET KEY.