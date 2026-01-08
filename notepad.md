# Blackthorn Gym - Battle with Leader Clair
- Primary Goal: Acquire the Rising Badge (Started Turn 35145)
- Battle Task: Defeat Dragonair #2 (Started Turn 35212)
- Current Turn: 35216

## Battle Strategy: Gym Leader Clair
- Opponent: Leader Clair
- Pokémon 1: Dragonair (Lv37). Moves: Thunder Wave, Surf. (FAINTED)
- Pokémon 2: Kingdra (Lv40). Moves: Surf, Smokescreen, Dragonbreath. (FAINTED)
- Pokémon 3: Dragonair (Lv37). Moves: Thunder Wave. (HP: 100%)
- Status: Xenon fainted. Calcifer (Lv49) at 127/155 HP (PAR). Kimchi (Lv34) at 51/90 HP.
- Strategy: Calcifer is paralyzed. Use Full Heal (Turn 35216) to restore speed. Return is neutral damage.
- Plan: Find Full Heal in bag, use on Calcifer. Then use Return.
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

## Lessons Learned
- Trust Game State: Collision types in Game State are absolute truth.
- Strength: Reactivate after floor changes.
- Reachability: The player can reach Clair on 1F by walking around the right edge (Column 9).
- Kingdra Typing: Water/Dragon. Neutral to Electric/Grass/Ice. Resists Fire/Water 4x. Weak to Dragon.
- Dragonair Typing: Dragon. Resists Fire, Water, Electric, Grass. Weak to Ice, Dragon. Neutral to Normal/Physical.