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

## C. Wild Encounters Log
- **Seafoam Islands 1F:** SLOWPOKE (Lv35), KRABBY (Lv32).
- **Seafoam Islands B1F:** ZUBAT (Lv27), KRABBY (Lv26).
- **Seafoam Islands B2F:** KINGLER (Lv38), SLOWPOKE (Lv35), ZUBAT (Lv27), GOLBAT (Lv36-37).
- **Seafoam Islands B3F:** SEEL (Lv34-35).
- **Seafoam Islands B4F:** SEEL (Lv34), ZUBAT (Lv36).

# III. Puzzles & Exploration

## A. Current Objective: Seafoam Islands
- **Primary Goal:** Solve the main boulder puzzle on Seafoam Islands B3F (West).
- **Current Location:** Western section of the Seafoam Islands.
- **Strategy:** The eastern section is a confirmed dead-end loop. The only way to progress is to exit the cave via the eastern entrance and re-enter from the western cave entrance on Route 20. I am now exploring the western side, which seems to be the correct path.

# IV. Strategic Lessons & Tool Development

## A. CRITICAL FAILURE ANALYSIS: The Seafoam Islands Loop (Turns ~88900-89050)
- **The Failure:** I wasted over 150 turns trapped in a cognitive and physical loop in the eastern Seafoam Islands. I vacillated between two incorrect hypotheses: 1) The area was a dead end, and 2) The eastern and western sections were connected. The first hypothesis was correct, but I abandoned it due to misinterpreting system feedback.
- **Root Cause - Confirmation Bias & Poor Data Management:** My most critical error was ignoring overwhelming evidence that contradicted my flawed second hypothesis. My `pathfinder` tool repeatedly reported "No path found," and the system issued multiple warnings about being in a dead end. Instead of accepting this data as fact, I assumed my tool was bugged and persisted with a flawed strategy. I also failed to update my notepad immediately with the correct "dead end" conclusion, which led me to repeat the same mistakes.
- **The Lesson:** **A tool's failure is a data point about the world, not just a bug.** Repeated failures are strong evidence that my underlying assumption is incorrect. I MUST learn to trust my tools and the game's feedback over my own intuition. All data management, especially correcting my understanding of the map, must be performed IMMEDIATELY to prevent repeating errors.

## B. Tool Development Log
- **Pathfinder Tool:** Its failures in Seafoam were due to my incorrect hypotheses, not bugs. **UPDATE:** The tool had a bug where it couldn't handle land-to-water SURF transitions. This has been fixed.
- **Boulder Puzzle Solver:** Its initial failures were also due to a bug in its internal pathfinding logic, which couldn't handle SURF. This has been fixed.