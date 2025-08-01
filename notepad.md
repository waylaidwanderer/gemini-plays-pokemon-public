# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Off-Screen State Changes:** An object's state will not update in the map data until it is visible on-screen.
- **Boulder Pushing:** A boulder can be pushed from an adjacent tile by facing it and pressing the corresponding direction. The game's behavior regarding player movement is inconsistent. Sometimes the player moves into the boulder's vacated space, and sometimes they do not, possibly to prevent the player from getting trapped. This mechanic requires further observation.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. It is NOT possible to step down from an `elevated_ground` tile to an adjacent `ground` tile.
- `steps`: Allows movement between `ground` and `elevated_ground` in both directions.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier that acts as a one-way ramp. It is possible to move from it onto `elevated_ground` (elevation 2), but it is NOT possible to move from it directly back down to `ground` or to enter it from ANY adjacent `ground` tile.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `cuttable`: A tree that can be removed with the HM Cut.
- `ladder_up`: Warps to a higher floor.
- `ladder_down`: Warps to a lower floor.

# II. Battle Intel
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

## B. Strategic Notes
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Struggle is only used automatically when a Pokémon is out of PP for ALL of its moves.
- **Full Heal Mechanic:** This item ONLY cures status conditions. It does NOT restore HP. This was verified by attempting to use it on multiple injured Pokémon with no status effects, which resulted in the message 'It won't have any effect.'

# III. Current Strategy: Victory Road 2F Puzzle (Agent-Assisted)
- **High-Level Goal:** Solve the two-boulder puzzle to open the path forward.
- **Agent Analysis:** The puzzle requires pairing Boulder B2 at (6,6) with Switch S2 at (10,17), and Boulder B1 at (5,15) with Switch S1 at (2,17). B2 must be moved first along a complex eastern route to avoid traps.
- **Strategic Plan (Sub-Goals):**
    1. Move boulder B2 (6,6) east along the y=7 corridor to the vertical channel at x=22.
    2. Push boulder B2 down the x=22 channel to the horizontal corridor at y=13.
    3. Maneuver boulder B2 west along the y=13 corridor to the vertical channel at x=16.
    4. Push boulder B2 down the x=16 channel to the switch row at y=17.
    5. Push boulder B2 left from (16,17) to its final position on switch S2 (10,17).
    6. Move boulder B1 (5,15) down and left to its final position on switch S1 (2,17).

# V. Tool & Agent Principles
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback (like validation warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.

# VI. Archived Lessons
- Victory Road 1F Puzzle: Solved.