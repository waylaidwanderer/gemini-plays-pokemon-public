# Blackthorn Gym - Battle with Leader Clair
- Primary Goal: Acquire the Rising Badge (Started Turn 35145)
- Battle Task: Defeat Kingdra (Started Turn 35185)
- Current Turn: 35208

## Battle Strategy: Gym Leader Clair
- Opponent: Leader Clair
- Pokémon 1: Dragonair (Lv37). (FAINTED)
- Pokémon 2: Kingdra (Lv40). Moves: Surf, Smokescreen, Dragonbreath. (HP: 100%)
- Status: Xenon fainted. Calcifer (Lv49) at 127/155 HP. Kimchi (Lv33) at 48/87 HP.
- Strategy: Calcifer is back in. Thunderpunch for neutral damage and paralysis chance.
- Plan: Use Thunderpunch (Turn 35208).
- Note: Kingdra is Water/Dragon. Weak only to Dragon-type moves in Gen 2. Electric/Grass are neutral due to Water typing. (Grass resists Water).

## Tile Mechanics
- FLOOR: Standard traversable tile. Verified Turn 35145. No special properties.
- WALL: Impassable boundary. Verified Turn 35145. Prevents movement.
- LADDER: Warp between floors (1F/2F). Verified Turn 35145.
- WARP_CARPET_DOWN: Exit from the Gym. Verified Turn 35145.
- HOLE: Found on 2F. Falling through leads to 1F. Verified Turn 34794. One-way transition down.
- LAVA/WATER: Impassable hazard. Verified Turn 35145. Must navigate around or bridge.

## Blackthorn Gym Puzzle (2F)
- Status: Strength INACTIVE (on 1F)
- Goal: Return to 2F after the battle and reactivate Strength.
- Correct Boulder Positions (Reset State): B6(3,3), B7(6,1), B8(8,14).
- Pits: P1(8,3), P2(2,5), P3(8,7).

## Post-Battle Tasks
- Mark impassable wall coordinates on 2F: (4,9), (4,10), (4,12), (6,2), (6,3), (7,11), (8,9), (9,13).

## Lessons Learned
- Trust Game State: Collision types in Game State are absolute truth.
- Strength: Reactivate after floor changes.
- Reachability: The player can reach Clair on 1F by walking around the right edge (Column 9).
- Kingdra Typing: Water/Dragon. Neutral to Electric/Grass/Ice. Resists Fire/Water 4x. Weak to Dragon.