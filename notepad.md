# Tile Mechanics (Global)
- FLOOR: Traversable. Standard ground.
- WALL: Impassable. Silver blocks, statues, and boundaries.
- PIT: Warp tile. Falling through takes you to the floor below.
- LADDER: Warp tile.
- BOULDER: Object. Impassable. Push with Strength.
- NPC: Object. Impassable.
- BOULDER BRIDGES: Boulders in pits act as passable FLOOR.
- Strength must be re-activated after falling through a pit.

# Blackthorn Gym Layout & Boulders
- 2F Boulders (Initial): Boulder 6 (3,3), Boulder 7 (6,1), Boulder 8 (8,14).
- 2F Pits: Pit (2,5), Pit (8,3), Pit (8,7).
- 1F Bridge: Boulders land at (2,6), (7,6), (7,7) to create path to Clair at (5,3).

# Boulder Puzzle Analysis
- Failed Hypotheses (Confirmed Walls):
  - Row 0: (2,0), (3,0), (5,0), (7,0), (8,0), (9,0)
  - Col 4: (4,2)-(4,7)
  - Col 6: (6,2), (6,3)
  - Misc: (8,9), (7,10), (7,11), (9,16), (2,13)
  - NPCs: Cody (4,1)
- Current Strategy: Use 'puzzle_analyst_v2' to find the missing link.
- Note: Turn 29746 "confirmed" fake wall at (4,3) was a hallucination.

# Strategy: Gym Leader Clair
- Battle Strategy (Turn 29637):
  1. Lead GNEISS (Lv45). Use EARTHQUAKE vs Dragonairs.
  2. Vs Kingdra: Switch to Calcifer. Use SMOKESCREEN 3-4 times.
  3. Switch to GNEISS. Use DEFENSE CURL then ROLLOUT.

# Navigation Insights
- 1F Partition: Row 11 is a wall from (2,11) to (9,11).
- 1F Access: Must use 2F detour (Ladder at 7,9 to Ladder at 1,7) to move between halves.