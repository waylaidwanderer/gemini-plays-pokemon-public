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
- **Tool Development:** My `pathfinder` tool is buggy. It incorrectly generates paths through impassable tiles. It still cannot account for scripted barriers like the strong current, so manual exploration is sometimes needed.
- **Agent Usage Reminder:** I must use my `menu_navigator_agent` for all complex menu tasks to avoid manual errors.
- **Future Development Ideas:** A tool to analyze map XML and provide step-by-step solutions for boulder puzzles.

# IV. Puzzles & Lessons Learned

## A. Seafoam Islands Puzzle
- **Hypothesis 1 (Disproven):** The exit is on the eastern side of the cave. This was disproven when the path was blocked by a strong current on B4F.
- **Hypothesis 2 (Active):** I need to solve a second boulder puzzle on the upper floors (B1F, B2F, B3F) to stop the western current on B4F.
- **Untested Hypothesis:** The ladder at (26, 5) on B4F is the exit.

## B. Fuchsia City Secret Pokémon (at (26, 7))
- **Observation:** An item ball at (26, 7) is in an enclosed area. A Youngster at (25, 9) states, "That item ball in there is really a POKéMON."

## C. Strategic Lessons
- **Confirmation Bias:** I exhibited confirmation bias by assuming my initial pathing ideas were the only solution, instead of trusting game state data when it contradicted my tools. I must actively try to disprove my own hypotheses.
- **Strategic Flexibility:** If a strategy is failing repeatedly, I must pivot to a different approach.
- **Trust the Game State:** I must trust the game state information (e.g., 'navigable warps') over my own interpretations or tool outputs, as it is the absolute source of truth.
- **LLM Reality:** Data management tasks (notepad, agents, tools) must be performed immediately and not deferred.