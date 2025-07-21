# I. Game Mechanics & Discoveries

## A. Verified Tile Mechanics
- **Ground:** Standard walkable tile.
- **Impassable:** Walls, objects, etc. Cannot be entered.
- **Grass:** Tall grass for wild Pokémon encounters.
- **Ledge:** Can be jumped down (one-way). Moving down into a ledge tile moves the player two tiles down.
- **Cuttable Tree:** Requires HM Cut to pass. Becomes `ground` after cutting, but respawns on map change.
- **Water:** Requires HM Surf to traverse. To use Surf, you must be standing on a 'ground', 'water', or 'steps' tile adjacent to water, face the water, and use the HM from the party menu.
- **Boulder:** Requires HM Strength to move.
- **Hole:** Warps player to a lower floor or a specific spot.
- **Ladder (Up/Down):** Warps player between floors.
- **Warp:** An instant transition point between maps or areas.
- **Steps:** Allows vertical and horizontal movement between 'steps' and adjacent 'ground' or 'elevated_ground' tiles.
- **Spinner (up, down, left, right):** Forces movement in a specific direction.
- **Spinner Stop:** A tile that halts movement from a spinner.
- **Elevated Ground:** Walkable ground at a different elevation. Movement between `ground` and `elevated_ground` is only possible via `steps`.
- **Gate (`gate_offscreen`, `closed_gate`, `open_gate`):** Barriers that may open or close based on game events. `gate_offscreen` is treated as open for pathfinding.
- **Boulder Switch & Barrier:** `boulder_switch` tiles are activated when a boulder is pushed onto them, which typically changes a `boulder_barrier` tile into a `cleared_boulder_barrier` tile (effectively `ground`).

## B. General Heuristics & Rules
- **PC Interaction:** To use a PC, stand on the tile directly below it, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu outside of battle. Fainted Pokémon can use field moves.
- **"No Will to Fight" Message (Correction):** This message appears only when the cursor in the party menu is on an already fainted Pokémon. It is a UI error, not a gameplay mechanic.
- **Surf Mechanic:** You cannot initiate Surf from an `elevated_ground` tile. You must be on a `ground`, `steps`, or `grass` tile adjacent to water.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting !> Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.

## B. Trainer Rosters & Movesets
*This section is for recording the teams and moves of significant trainers (Gym Leaders, Rivals) after a battle is concluded.*
### Viridian Gym - Giovanni (Rematch)
- **Team:** NIDOKING (Lv54), DUGTRIO (Lv53), NIDOQUEEN (Lv54), PERSIAN (Lv55)
- **Observed Moves:**
  - NIDOKING: Ice Beam, Blizzard, Thunderbolt, Earthquake
  - DUGTRIO: Fissure, Slash, Earthquake, Rock Slide
  - NIDOQUEEN: Ice Beam, Earthquake, Thunderbolt, Body Slam
  - PERSIAN: Bubblebeam, Slash, Hyper Beam, Thunderbolt

## C. Battle Lessons
- **Level Disparity vs. Type Immunity:** A massive level gap can be more dangerous than type disadvantage. Switching in a low-level Pokémon (e.g., Lv 17 GALE) against a high-level opponent (e.g., Lv 53 Dugtrio) is extremely risky, even if the low-level Pokémon has type immunity to the opponent's primary STAB moves. Neutral coverage moves can still result in a one-hit KO if the level difference is significant. Survivability must be assessed holistically, considering HP, defensive stats, and the level gap, not just type matchups.

# III. Strategic Lessons & Reflections

## A. CRITICAL FAILURE ANALYSIS: Confirmation Bias in Seafoam Islands (Turns ~89480-89516)
- **The Failure:** I wasted significant time exploring the eastern side of the Seafoam Islands based on a flawed hypothesis. I repeatedly descended into isolated, dead-end rooms, ignoring system warnings, my own tool's output, and map data that indicated these paths were not viable for crossing the cave system.
- **Root Cause - Confirmation Bias:** I became fixated on the idea that the eastern descent was the solution and failed to abandon the hypothesis after the first few failed tests. Instead of accepting the dead ends and repeated `pathfinder` failures as proof my hypothesis was wrong, I treated them as minor setbacks or tool bugs and kept looking for another eastern path. This is a classic case of confirmation bias.
- **The Lesson:** A single failed test is strong evidence against a hypothesis. Multiple failures are conclusive proof. I must be more willing to abandon a failing strategy immediately and pivot to a new one. I must trust the data (map, system warnings, tool outputs) over my own intuition. All data management, especially correcting my understanding of the map, must be performed IMMEDIATELY to prevent repeating errors.

## B. Tool Development Log
- **Pathfinder & Boulder Puzzle Solver:** Both tools initially had a bug where their internal pathfinding logic couldn't handle land-to-water SURF transitions. This has been fixed.
- **Boulder Puzzle Solver Failures (1F):** The solver repeatedly timed out or failed on the 1F puzzle. This was not a tool bug, but a signal that my hypothesis was wrong. I assumed the puzzle was solvable immediately. **The lesson is to treat repeated tool failures not as a sign to keep trying, but as evidence that my fundamental understanding of the puzzle's state is incorrect. I must be more willing to abandon a failing hypothesis and pivot to exploration.**
- **Pathfinder Bug Fix (Turn 89499):** The `pathfinder` tool was unable to find a path to a 'hole' tile because the `is_traversable` function did not recognize 'hole' as a valid land tile to move onto from 'ground'. I updated the `is_traversable` function to include 'hole' in the set of `valid_land_types` and added a condition to allow movement between 'ground' and 'hole' tiles. The lesson is that my custom tools need to be robust enough to handle all known tile types.

# IV. Strategic Reflections (Post-Turn 89880)
- **Menu Efficiency:** Cycling through the Fly menu was inefficient. I must be more systematic in menu navigation to avoid wasting turns, concluding an option is unavailable after one full cycle rather than repeated presses.
- **Assumption Testing:** I am assuming Victory Road is the best training location. This is an unverified assumption. **Test:** Upon arrival, I will assess the wild Pokémon levels and EXP yield to confirm this hypothesis. If it's not optimal, I will seek alternative locations.