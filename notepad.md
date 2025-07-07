## I. Core Protocols & Game Philosophy
- **Immediate Data Management:** I will use `define_map_marker` and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **Agent & Tool Protocol:** Agent and tool refinement is an IMMEDIATE action. If a tool is faulty or a better one can be conceived, I MUST define/redefine it on the IMMEDIATE next turn.
- **Hypothesis-Driven Gameplay:** I will rigorously document my hypotheses, tests, and conclusions in my notepad. I will avoid repeating failed strategies and will pivot to new goals if progress stalls after multiple documented attempts.

## II. Tool Development Log
- **pathfinder:** REFINED (T54601). Added more robust parsing logic to correctly handle impassable objects and improve error logging.

## III. Game Mechanics & Battle Intel
### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Water Tiles (Silph Co.):** The water tiles on the first floor of Silph Co. are purely cosmetic and function as `impassable` walls.
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.
- **Gates:** `closed_gate` tiles are impassable barriers. `open_gate` tiles are unlocked and function as `ground`. Some are opened by switches, others require a KEY CARD.
- **Elevators (Silph Co.):** Require interaction with the control panel to select a floor, then moving onto the warp tile at the back.
- **Saffron Gym Teleporters:** 1x1 warp tiles. To use a warp, move onto the tile. If already on a warp, move off and back on to trigger.
- **2x1 Warps (Cinnabar Lab):** To use these horizontal floor warps, stand on one of the two tiles and press into the impassable boundary (e.g., Down).

### B. Confirmed ROM Hack Changes
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying** (confirmed: KADABRA's PSYBEAM vs ECHO's GOLBAT)
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); **Ice !> Gyarados (Water/Flying)** (confirmed: NEPTUNE's AURORA BEAM vs Fisherman's GYARADOS); Poison !> Poison (confirmed: ECHO's SLUDGE vs MUK).
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **Electric is effective vs Sabrina's Psychic team, confirming Psychic types are NOT immune to Electric.**; **HYPNO immune to STUN SPORE** (powder moves); **MUK immune to THUNDER WAVE** (Electric-type status move).

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts (e.g., from MINIMIZE).
- **Struggle:** A Pokémon with 0 PP for all moves will use Struggle, which has low accuracy and causes recoil damage.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **HM Usage:** Flash, Cut, and Fly MUST be taught to a Pokémon to be used in the field.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any that participated via switch-in.
- **PC Box Full:** When a Pokémon is caught and the active PC box is full, the caught Pokémon is still sent to the PC, but the active box must be changed manually later.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center. You respawn in front of the trainer you lost to.

#### B3. NPC & Item Interactions
- **NPC Catch Event:** Some NPCs can trigger a Pokémon 'catch' event upon interaction (e.g., Rocker in Safari Zone East Rest House gave a CHANSEY).
- **Eevee Evolution:** An NPC in Safari Zone North mentioned Eevee can evolve into Flareon or Vaporeon, suggesting multiple evolution paths via stones.
- **EXP.ALL:** Gives EXP to all party Pokémon, even non-participants, but reduces the total EXP gained per Pokémon. Best used for targeted training.

## IV. Puzzle & Hypothesis Log
### A. Solved Puzzles & Confirmed Mechanics
- **Pokemon Mansion 1F Puzzle System:** Confirmed 'alternating doors' mechanic. The switch at (3, 6) toggles the western gates (17, 8) and the southern gates (25, 14) inversely. (Confirmed T53932)
- **Pokemon Mansion Puzzle (Floors 2-3):** The mansion uses an 'alternating doors' system controlled by switches.
  - **2F Switch (3, 12):** Toggles northern gates (10, 5/6) and southern gates (8, 23/24). (Confirmed T53987)
  - **3F Switch (11, 6):** Toggles central gates (16, 5/6) and southern gates (16, 11/12). (Confirmed T52735)
- **Saffron Gym Puzzle:** Path to Sabrina was blocked until Silph Co. was cleared, which unlocked the correct teleporter path. (Confirmed T51442)
- **Silph Co. Puzzles (4F & 10F):** CARD KEY was required for many gates. Defeating Giovanni (11F) was the main trigger to activate the correct teleporter paths on 10F. (Confirmed T51271, T51442)

### B. In-Progress Puzzles & Active Hypotheses
#### B1. Pokemon Mansion B1F
- **Current Hypothesis (T54630):** The B1F puzzle is a large loop with three sets of gates (western, northern, eastern) controlled by a single switch at (19, 26). The puzzle operates on a two-step 'prime and trigger' mechanic. **Step 1:** Flipping the switch 'primes' one set of gates (e.g., western). **Step 2:** Walking to that specific set of gates triggers them to open. This was confirmed to work for the northern gates (T54600) and the western gates (T54630). The Secret Key must be located in the final section accessible after navigating this loop correctly.

## V. Future Development & Testing Protocols
### A. Agent Ideas
- **Dungeon Navigator Agent:** For complex, multi-floor puzzles like the Pokémon Mansion, a more advanced agent could be beneficial. It would need to process map data across multiple floors, track switch states, and understand non-linear connections (warps, holes, proximity triggers) to suggest optimal paths or solutions.
### B. Puzzle Testing Protocols
- **Rigorously Falsify Hypotheses:** When a puzzle mechanic is discovered (e.g., a proximity trigger for gates), I must actively try to disprove the initial conclusion. For example, test if other tiles or actions also trigger the event, not just the one first observed. This will prevent confirmation bias.

## VI. To-Do List
### C. Future Tests & Agent Development
- **Dungeon Navigator Agent Idea:** For future complex areas, define an agent that can process map data across multiple floors, track switch/gate states, and understand non-linear connections (warps, holes, proximity triggers) to suggest optimal paths or puzzle solutions.
- **B1F Puzzle Falsification Test:** Once healed, return to B1F. To disprove confirmation bias, perform a falsification test: Flip the switch to prime one set of gates (e.g., northern), but then walk to a different set (e.g., western). The hypothesis predicts the western gates will remain closed. This will provide stronger confirmation of the 'prime and trigger' mechanic.