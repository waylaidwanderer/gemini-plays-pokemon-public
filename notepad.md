# Blackthorn Gym 1F - Battle with Clair
- Current Turn: 35161

## Battle Strategy: Gym Leader Clair
- Opponent: Leader Clair
- Pokémon 1: Dragonair (Lv37). Moves: Thunder Wave, Surf.
- Status: Xenon was paralyzed by Thunder Wave, but cured with a Full Heal (Turn 35160).
- Strategy: Xenon (Haunter) use Night Shade for fixed 36 HP damage. GNEISS (Graveler) is the primary backup using Earthquake or Rollout for neutral physical damage. Calcifer (Typhlosion) use Return. Avoid using Fire, Water, Electric, or Grass moves as they are resisted by Dragonair.
- Note: Initial status moves (Hypnosis, Thunder Wave) failed early on, possibly due to a hidden Safeguard. Dragonair later successfully paralyzed Xenon.

## Blackthorn Gym Puzzle (2F)
- Status: Strength INACTIVE (on 1F)

### Tile Mechanics
- FLOOR: Traversable. Collision type is absolute truth.
- WALL: Impassable. Trust Game State 'type' attribute.
- PIT (2F): Warp to 1F. Boulders fill them to create paths on 1F.
- LADDER: Warp between floors. Resets boulders on 2F.
- NPCs: Act as walls.

### Correct Boulder Positions (2F Reset State)
- B6 (ID 6): (3, 3) [Verified]
- B7 (ID 7): (6, 1) [Verified]
- B8 (ID 8): (8, 14) [Verified]

### Pits (2F Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Lessons Learned
- Trust Game State: 'WALL' and 'FLOOR' labels are the source of truth.
- B6 reset position is (3, 3).
- Strength: Reactivate after floor changes.
- Reachability: The player can reach Clair on 1F by walking around the right edge (Column 9).