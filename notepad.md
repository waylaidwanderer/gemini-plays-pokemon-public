# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon. It is a cursor error, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points for SURF.
- **Boulder Pushing:** Activate Strength from the party menu. Face the boulder and press the directional button. The boulder moves one tile, but the player's position does not change.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `elevated_ground`: Walkable, different elevation. Movement to a lower elevation is *only* possible via `steps` tiles or `cleared_boulder_barrier` tiles. Direct movement to a lower `ground` tile is impossible.
- `steps`: Allows movement between elevations.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: Acts as a one-way ramp. It is only possible to move DOWN from an elevated area onto this tile, not UP from a lower area.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `ladder_up` / `ladder_down`: Warps between floors.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

## B. Trainer Battle Rules
- **No Respawns:** Defeated trainers do NOT respawn. They become permanent obstacles that are impassable by normal movement.

# III. Puzzle Mechanics & Key Discoveries

- **Victory Road 1F - Western Platform:** This area contains the ladder to 2F at (2, 2). It is the only way to progress to the next floor, but it is inaccessible until the central barrier at (10, 13) is opened.
- **Victory Road 2F - Western Trap:** This puzzle requires a two-step "prime and trigger" mechanic. Pushing the boulder onto the switch at (2, 17) primes the trap. Leaving the floor and re-entering triggers the event, opening the barrier at (8, 9) and (8, 10).
- **Victory Road 3F - Hole Puzzle:** Pushing the boulder at (14, 13) south into the hole at (14, 15) causes it to drop to the floor below, affecting a puzzle there.

# IV. Current Objectives & Hypotheses

## Victory Road 1F Puzzle - RE-EVALUATION
- **Primary Obstacle:** Reaching the ladder to 2F at (2, 2).
- **Corrected Understanding:** My previous conclusion that I was trapped on the western side of Victory Road 1F was INCORRECT. The game state confirms a path forward exists. The defeated NPC at (7, 11) must not be a permanent, impassable blocker for the entire path, or there is an alternate route on the platform I have missed.
- **Current Objective:** Systematically re-explore the western upper platform to find the navigable path to the ladder at (2, 2).

# V. Future Development Ideas