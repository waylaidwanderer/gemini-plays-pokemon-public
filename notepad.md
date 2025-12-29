# Tile Mechanics (Global)
- FLOOR: Traversable. Standard ground.
- WALL: Impassable. Silver blocks, statues, and boundaries.
- PIT: Warp tile. Falling through takes you to the floor below (landing on specific tiles).
- LADDER: Warp tile. Used to travel between floors.
- BOULDER: Object. Impassable. Can be pushed with Strength.
- NPC: Object. Impassable. Acts as a wall even when defeated.
- ICE: Sliding mechanic (Ice Path).
- ROCK: Destructible with ROCK SMASH.
- WATER: Requires Surf to traverse.
- BOULDER BRIDGES: Boulders in pits act as passable FLOOR.

# Blackthorn Gym Layout & Boulders
- 2F Boulders (Initial Positions):
  - Boulder 6: (3, 3)
  - Boulder 7: (6, 1)
  - Boulder 8: (8, 14)
- 2F Pits:
  - Pit (2, 5) -> 1F (2, 6)
  - Pit (8, 3) -> 1F (7, 6)
  - Pit (8, 7) -> 1F (7, 7)
- Verified Mechanics (2F):
  - Silver blocks (Row 0) are WALLS. Boulders in Row 1 cannot be pushed DOWN.
  - Column 9: Dead end at (9, 4). (9, 12)-(9, 17) are WALLS.
  - Column 2: Wall from (2, 10) to (2, 17).
  - Row 13: Passage at (4, 13) connects east and west sections. (2, 13) is a WALL.
  - Gym Reset: Exiting and re-entering resets all boulders to initial positions.

# Strategy: Gym Leader Clair
- Battle Strategy (Turn 29637):
  1. Lead GNEISS (Lv45). Use EARTHQUAKE vs Dragonairs.
  2. Vs Kingdra: Switch to Calcifer. Use SMOKESCREEN 3-4 times.
  3. Switch to GNEISS. Use DEFENSE CURL then ROLLOUT.
  4. Keep HP > 50% with Hyper Potions.

# Type Effectiveness (Verified)
- Dragon resists: Fire, Water, Electric, Grass.
- Kingdra (Water/Dragon) resists: Fire (1/4x), Water (1/4x), Electric (1/2x), Grass (1/2x).
- Normal & Ground: Neutral vs Dragon.

- Hypothesis: Tile (8, 9) is a fake wall.
  - Test: Stand at (7, 9) and press Right.
  - Result: DENIED (Turn 29767).
- Hypothesis: Tile (7, 10) is a fake wall.
  - Test: Stand at (6, 10) and press Right.
  - Result: [Pending].
- Failed Hypotheses:
  1. Row 0 is passable (Tested - Denied).
  2. NPC Cody at (4, 1) is passable (Denied Turn 29751).
  3. Tile (4, 2) is a fake wall (Denied Turn 29748).
  4. Tile (6, 3) is a fake wall (Denied Turn 29747).
  5. Tile (4, 3) is a fake wall (Denied Turn 29758).
  6. Tile (4, 4) is a fake wall (Denied Turn 29759).
  7. Tile (4, 5) is a fake wall (Denied Turn 29762).
  8. Tile (4, 6) is a fake wall (Denied Turn 29763).
  9. Tile (8, 9) is a fake wall (Denied Turn 29767).

# Navigation Insights
- 1F Partition: Row 11 is a solid wall from (2,11) to (9,11).
- 1F Access: Must use 2F detour to move between top and bottom halves of 1F. (Verified Turn 29706)