# I. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Ground, Fighting; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting !> Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.

## B. Trainer Rosters & Movesets
### Giovanni (Viridian Gym)
- **Dugtrio (Lv53):** Rock Slide, Earthquake, Fissure, Slash.
- **Nidoqueen (Lv54):** Body Slam, Earthquake, Thunderbolt, Ice Beam.
- **Nidoking (Lv54):** Blizzard, Earthquake, Thunderbolt, Ice Beam.
- **Persian (Lv55):** Bubblebeam, Slash, Hyper Beam, Thunderbolt.

# II. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Becomes `ground` after cutting, but respawns on map change.
- **Water:** Requires HM Surf to traverse. To use Surf from a land tile, you must be standing on a ground tile that is adjacent to a water tile, face the water, and use the HM from the party menu.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps or areas within a map (e.g., doors, cave entrances).
- **Steps:** Allows vertical and horizontal movement between 'steps' and adjacent 'ground' or 'elevated_ground' tiles.
- **Spinner (up, down, left, right):** Forces movement in a specific direction until a `spinner_stop` tile or another obstacle is hit.
- **Spinner Stop:** A tile that halts movement from a spinner.
- **Elevated Ground:** Walkable ground at a different elevation. HM Surf cannot be initiated from this tile type. Movement between `elevated_ground` and `ground` is only possible via `steps`.
- **Gate (`gate_offscreen`, `closed_gate`):** Barriers that may open or close based on game events. Off-screen gates are treated as potentially open for pathfinding unless proven otherwise.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle. Fainted Pokémon can use field moves.
- **Party Planning:** Always confirm all required HMs (Fly, Surf, Strength, Cut) are present in the party *before* leaving a Pokémon Center.
- **Dynamic Map Elements:** Some map elements, like trees, can appear dynamically (e.g., Fuchsia City at (19,20)).

# III. Tool Development & Usage

## A. Custom Tools
- **`pathfinder`:** This tool has been updated to correctly handle all traversal logic, including HMs, and now outputs a JSON array of coordinates for the path_plan, making it more reliable.
- **`spinner_maze_solver`:** This tool calculates paths in spinner mazes. It was buggy, but has been successfully fixed and is now reliable for navigating spinner puzzles.

## B. Agent & Tool Usage Notes
- I must fix failing tools immediately using my `code_debugger_agent` instead of deferring the task or attempting manual fixes.
- Proximity of recommended locations from agents should be considered for efficiency.

# IV. Puzzles & Hypotheses

## A. Fuchsia City Secret Pokémon (at (26, 7))
- **Observation:** An item ball at (26, 7) is in an enclosed area. A Youngster at (25, 9) states, "That item ball in there is really a POKéMON."
- **Hypothesis 1 (Failed):** The signs next to the other Pokémon exhibits must be read in a specific order to unlock the enclosure.
- **Hypothesis 2 (Untested):** Interaction with the Pokémon in the enclosures is required, not the signs.
- **Hypothesis 3 (Untested):** A specific Pokémon must be in the party to trigger an event.

## B. Secret Key Location
- **Discovery:** I already possessed the Secret Key, likely obtained from Giovanni in the Rocket Hideout. The search in the Pokémon Mansion was unnecessary.

# V. Strategic Plans & Lessons Learned

## A. Viridian Gym Strategy (Level Cap: 55)
- **Current Plan:** Challenge Giovanni in the Viridian City Gym. The gym is a spinner maze. I will use the `spinner_maze_solver` tool to navigate it. My team is at a good level, and I have a strong type advantage with REVENANT (Marowak) and CRAG (Golem) against his Ground/Rock-type team.

## B. Lessons Learned
- **Confirmation Bias:** I exhibited confirmation bias when debugging the `pathfinder` tool. I must actively try to disprove my own assumptions and trust the data.
- **Tool Maintenance Protocol:** When a tool fails, I must immediately use the `code_debugger_agent` for a systematic diagnosis.
- **Real-Time Documentation:** All discoveries, failures, plans, and lessons learned must be documented in the notepad on the turn they occur.
- **LLM Reality:** I must perform data management tasks (notepad, agents, tools) immediately and not defer them. Creating mental to-do lists is an invalid strategy.

## C. Agent Usage Notes
- I have a `training_spot_advisor_agent` that I should use to find optimal grinding locations instead of manual exploration. I will use this next time I need to train.