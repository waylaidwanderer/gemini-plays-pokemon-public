# I. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting !> Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.

## B. Trainer Rosters & Movesets
### Giovanni (Viridian Gym - Level Cap: 55)
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
- **Water:** Requires HM Surf to traverse. To use Surf from a land tile, you must be standing on a 'ground', 'water', or 'steps' tile adjacent to water, face the water, and use the HM from the party menu.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps or areas within a map.
- **Steps:** Allows vertical and horizontal movement between 'steps' and adjacent 'ground' or 'elevated_ground' tiles.
- **Spinner (up, down, left, right):** Forces movement in a specific direction.
- **Spinner Stop:** A tile that halts movement from a spinner.
- **Elevated Ground:** Walkable ground at a different elevation. Movement between `elevated_ground` and `ground` is only possible via `steps`.
- **Gate (`gate_offscreen`, `closed_gate`):** Barriers that may open or close based on game events.

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** This message appears only when the cursor in the party menu is on an already fainted Pokémon. It is a UI error, not a gameplay mechanic.

# III. Tool Development & Usage

## A. Custom Tools & Agents
- My agents (`battle_strategist_agent`, etc.) are for high-level reasoning.
- My tools (`pathfinder`, etc.) are for complex computational tasks.
- **Tool Limitations:** My `pathfinder` tool cannot account for scripted environmental barriers (like the strong current in Seafoam Islands). For such puzzles, I must rely on manual exploration and hypothesis testing.

## B. Future Development Ideas
- **Boulder Puzzle Solver Tool:** A tool to analyze map XML and provide step-by-step solutions for boulder puzzles. (Critique noted this is a computational task, better for a tool than an agent).

# IV. Puzzles & Hypotheses

## A. Seafoam Islands Puzzle
- **Observation:** The Seafoam Islands dungeon is split into non-contiguous eastern and western sections on each floor.
- **Observation (B4F):** Attempting to use Surf from the steps at (8, 12) is blocked by the message 'The current is much too fast!'.
- **Hypothesis 1:** The boulders on the floors must be pushed into holes to alter the current.
- **Hypothesis 2 (Confirmed):** The western boulder puzzle area is inaccessible from the eastern ladders. The correct path requires finding an alternate route from a higher floor.
- **Test (Hypothesis: Surf from Elevated Ground):** Attempted to use Surf from `elevated_ground` tile at (8, 7) on B4F. **Result:** Failed. The game message 'No SURFing on [Pokemon] here!' appeared. **Conclusion:** Surfing is not possible from `elevated_ground`.
- **Test (Hypothesis: Hidden Wall Passage on B4F):** Systematically attempted to walk through the western 'impassable' wall on the eastern B4F platform. **Result:** Failed. All tiles were impassable as marked. **Conclusion:** There is no hidden passage in that wall.

## B. Fuchsia City Secret Pokémon (at (26, 7))
- **Observation:** An item ball at (26, 7) is in an enclosed area. A Youngster at (25, 9) states, "That item ball in there is really a POKéMON."
- **Hypothesis (Untested):** Interaction with the Pokémon in the enclosures is required, not the signs.

# V. Strategic Plans & Lessons Learned

## A. Current Plan: Seafoam Islands Exploration
- **Immediate Goal:** Backtrack to B2F to find an alternate route to the western section of the lower floors to solve the boulder puzzle.

## B. Lessons Learned
- **Confirmation Bias:** I exhibited confirmation bias by repeatedly trying to fix my `pathfinder` tool for a scripted event it couldn't handle, instead of accepting the evidence and changing my strategy.
- **Strategic Flexibility:** If a strategy is failing repeatedly (like trying to cross the strong current), I must pivot to a different approach (like backtracking) to maintain progress.
- **Trust the Game State:** I must trust the game state information (e.g., 'reachable unseen tiles') over my own visual perception, as it may reveal paths or possibilities I have missed.
- **LLM Reality:** Data management tasks (notepad, agents, tools) must be performed immediately and not deferred.