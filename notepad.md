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
- **Spinner:** Forces movement in a specific direction.
- **Elevated Ground:** Walkable ground at a different elevation. HM Surf cannot be initiated from this tile type. Movement between `elevated_ground` and `ground` is only possible via `steps`.
- **Gate (`gate_offscreen`, `closed_gate`):** Barriers that may open or close based on game events. Off-screen gates are treated as potentially open for pathfinding unless proven otherwise.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle.
- **Party Planning:** Always confirm all required HMs (Fly, Surf, Strength, Cut) are present in the party *before* leaving a Pokémon Center.
- **Dynamic Map Elements:** Some map elements, like trees, can appear dynamically (e.g., Fuchsia City at (19,20)).

# III. Tool Development & Usage

## A. Custom Tools
- **`pathfinder`:** This tool has been updated to correctly handle all traversal logic, including HMs, and now outputs a JSON array of coordinates for the path_plan, making it more reliable.
- **`spinner_maze_solver`:** Untested. I MUST use this tool at the next spinner maze encountered (Viridian Gym) to validate its functionality.

## B. Agent & Tool Usage Notes
- Proximity of recommended locations from agents should be considered for efficiency.
- I must fix failing tools immediately using my `code_debugger_agent` instead of deferring the task or attempting manual fixes.

# IV. Puzzles & Hypotheses

## A. Fuchsia City Secret Pokémon (at (26, 7))
- **Observation:** An item ball at (26, 7) is in an enclosed area. A Youngster at (25, 9) states, "That item ball in there is really a POKéMON."
- **Hypothesis 1 (Failed):** The signs next to the other Pokémon exhibits must be read in a specific order to unlock the enclosure.
- **Hypothesis 2 (Untested):** Interaction with the Pokémon in the enclosures is required, not the signs.
- **Hypothesis 3 (Untested):** A specific Pokémon must be in the party to trigger an event.

## B. Seafoam Islands Puzzle
- **Observation:** The Seafoam Islands are split into eastern and western sections on every floor explored so far (1F, B1F, B2F). Direct horizontal travel between them is impossible.
- **Hypothesis 1 (Confirmed):** The connection between the east and west sections is on a lower floor (B3F). I successfully navigated this by surfing from the eastern side on B3F.

## C. Untested Assumptions
- **Conclusion:** Pokémon Mansion 2F is a more efficient grinding spot than 1F due to higher-level and more varied encounters like Magmar yielding more EXP.

# V. Strategic Plans & Lessons Learned

## A. Training for Giovanni (Level Cap: 55)
- **Current Plan:** Grind in Pokémon Mansion until the party reaches the level cap.

## B. Lessons Learned
- **Confirmation Bias:** I exhibited confirmation bias when debugging the `pathfinder` tool. I assumed it was still broken after a fix and ignored evidence to the contrary. I must actively try to disprove my own assumptions and trust the data.
- **Tool Maintenance Protocol:** When a tool fails, I must immediately use the `code_debugger_agent` for a systematic diagnosis. Manual, incremental fixes are inefficient and error-prone. Tool reliability is a higher priority than immediate gameplay progression.
- **Real-Time Documentation:** All discoveries, failures, plans, and lessons learned must be documented in the notepad on the turn they occur, not summarized later.

## C. Agent Usage Notes
- I have a `training_spot_advisor_agent` that I should use to find optimal grinding locations instead of manual exploration. I will use this next time I need to train.