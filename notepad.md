# Blackthorn Gym - Battle with Leader Clair
- Primary Goal: Acquire the Rising Badge (Started Turn 35145)
- Battle Task: Defeat Dragonair #2 (Started Turn 35212)
- Current Turn: 35222

## Battle Strategy: Gym Leader Clair
- Opponent: Leader Clair
- Pokémon 1: Dragonair (Lv37). Moves: Thunder Wave, Surf. (FAINTED)
- Pokémon 2: Kingdra (Lv40). Moves: Surf, Smokescreen, Dragonbreath. (FAINTED)
- Pokémon 3: Dragonair (Lv37). Moves: Thunder Wave, Thunderbolt. (HP: 100%)
- Status: Xenon fainted. Calcifer (Lv49) at 108/155 HP. Kimchi (Lv34) at 51/90 HP.
- Strategy: Calcifer is no longer paralyzed. Dragonair resists Fire and Electric. Calcifer should use Return for neutral physical damage.
- Plan: Use Return to defeat Dragonair.
- Note: Dragonair resists Fire, Water, Electric, Grass (0.5x). Weak to Ice and Dragon (2.0x). Normal is neutral.

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

## Lessons Learned
- Trust Game State: Collision types in Game State are absolute truth.
- Strength: Reactivate after floor changes.
- Reachability: The player can reach Clair on 1F by walking around the right edge (Column 9).
- Type Effectiveness (Gen 2):
    - Dragonair (Dragon): Resists Fire, Water, Electric, Grass (0.5x). Weak to Ice, Dragon (2.0x).
    - Kingdra (Water/Dragon): Resists Fire, Water (0.25x), Electric, Grass (0.5x). Weak to Dragon (2.0x). Ice is neutral (Dragon weak, Water resists).
- Smokescreen: Lowers accuracy. Switching resets stat stages.