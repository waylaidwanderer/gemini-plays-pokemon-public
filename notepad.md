# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Warp tile. Falling through takes you to the floor below (landing on specific tiles).
- LADDER: Warp tile. Used to travel between floors.
- BOULDER: Object. Impassable. Can be pushed with Strength.
- NPC: Object. Impassable. Acts as a wall even when defeated. (Verified: Turn 29424)
- ICE: Sliding mechanic (Ice Path).
- ROCK: Destructible with ROCK SMASH.
- WATER: Requires Surf to traverse.
- BOULDER BRIDGES: Boulders in pits (1F 2,6; 7,6; 7,7) act as passable FLOOR.

# Blackthorn City & Gym Discoveries
- Pokemon Center: (21, 29).
- Blackthorn Mart: (15, 29).
- Emy's House: (29, 23). Trade DODRIO for female DRAGONAIR.
- Move Deleter's House: (9, 31).
- Dragon Speech House: (13, 21).
- Blackthorn Gym Entrance: (18, 11).
- Trainers Defeated: Paul (1, 14), Mike (6, 6), Lola (9, 2) on 1F; Fran (4, 11), Cody (4, 1) on 2F.
- Gym Guide (7, 15) advice: Dragon-type Pokemon are weak against Ice-type moves.

# Strategy: Gym Leader Clair (REVISED)
- Battle Strategy (Analyst Turn 29637):
  1. Lead GNEISS (Lv45). Use EARTHQUAKE vs Dragonairs.
  2. If first Dragonair uses Surf, switch to Calcifer to absorb and finish with RETURN.
  3. Use FULL HEALS immediately if paralyzed.
  4. Vs Kingdra: Switch to Calcifer. Use SMOKESCREEN 3-4 times to lower accuracy.
  5. Switch to GNEISS. Use DEFENSE CURL (doubles Rollout power) then ROLLOUT.
  6. Keep HP > 50% with Hyper Potions. Use XENON as fodder for safe healing.

# Blackthorn Gym Layout & Boulders
- 2F Boulders (Current Positions):
  - Boulder 6: (3, 3)
  - Boulder 7: (8, 1)
  - Boulder 8: (8, 14)
- 2F Pits (All empty after reset):
  - Pit (2, 5) -> 1F (2, 6)
  - Pit (8, 3) -> 1F (7, 6)
  - Pit (8, 7) -> 1F (7, 7)
- Strategy: Fill all three pits to complete the bridge to Clair.
- Verified Mechanics (2F):
  - Silver blocks (Row 0) are WALLS. (Turn 29653)
  - Row 0 Tests: (1,0), (3,0), (5,0), (7,0), (9,0) are all confirmed WALLS. (Turns 29675-29685)
  - Column 9: Dead end at (9, 4). (9, 12)-(9, 15) are WALLS.
  - Row 13: Passage at (4, 13) connects east and west sections.
  - Pushing a boulder: First press pushes it, second press moves player into its old tile.
  - Gym Reset: Exiting and re-entering resets all boulders to initial positions.
- Boulder Path Analysis:
  - Pit (8, 7): Reachable from Column 5 -> (6, 7) -> (7, 7) -> push RIGHT.
  - Pit (8, 3): Reachable from (7, 1) -> (7, 2) -> (7, 3) -> push RIGHT.
  - Pit (2, 5): Reachable from (1, 5) or (3, 5).
- Observation: The floor has a blue/white pattern similar to the Ice Path. Cosmetic only for player, but strength moves boulders one tile.

# Battle Lessons
- Item Scarcity: Running out of Revives/Max Potions is lethal. Always stock up before major battles. (Turn 29510)
- Type Effectiveness: Dragon resists Fire/Electric. Use physical neutral moves (Return) for better DPS. (Turn 29459)

# Type Effectiveness (Verified)
- Dragon resists: Fire, Water, Electric, Grass. (Verified vs Dragonair, Turn 29459)
- Kingdra (Water/Dragon) resists: Fire (1/4x), Water (1/4x), Electric (1/2x), Grass (1/2x).
- Normal & Ground: Neutral vs Dragon.

# Boulder Puzzle Manual Analysis (Turn 29687)
- Observation: Boulder 7 at (8, 1) is likely a trap or intended for a specific pit that doesn't require pushing it down.
- New Hypothesis: Boulder 8 (8, 14) is the key to the east side pits.
- Task: Reset Gym. Boulders 7 and 8 are trapped in Column 8 due to Row 0/Column 9 walls.
- Start Time: Turn 29620 (Gym Reset).
- Failed Hypotheses:
  1. Row 0 is passable (Tested - Denied).
  2. Boulder 7 can be pushed into (8, 3) from Row 1 (Requires player in Row 0 - Denied).

# Navigation Insights
- 1F Partition: Row 11 is a solid wall from (2,11) to (9,11).
- 1F Access: The only way to move between the top and bottom halves of 1F is via Column 1 or Column 0.
- 1F Connectivity: The top-right area (where Clair is) is disconnected from Column 1 on 1F.
- Conclusion: To exit the gym from the top-right area, you MUST go to 2F via the (7,9) ladder, walk to the (1,7) ladder, and then descend back to 1F. (Verified Turn 29706)