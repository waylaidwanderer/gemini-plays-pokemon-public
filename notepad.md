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
  - Boulder 8: (8, 14) (Off-screen)
- 2F Pits (All empty after reset):
  - Pit (2, 5) -> 1F (2, 6)
  - Pit (8, 3) -> 1F (7, 6)
  - Pit (8, 7) -> 1F (7, 7)
- Strategy: Fill all three pits to complete the bridge to Clair.
- Verified Mechanics:
  - Silver blocks are WALLS. (Turn 29653)
  - Row 0 Tests: (5, 0) WALL, (7, 0) WALL, (9, 0) WALL.
  - Column 9 Test: (9, 4) is a WALL.
  - Pushing a boulder: First press pushes it, second press moves player into its old tile.
  - All pits are empty after gym reset. (Turn 29620)
  - Row 13 passage at (4, 13) connects east/west sections.
- Potential Boulder Paths:
  - Pit (8, 7): Boulder 8 (8, 14) -> (8, 12) -> (9, 12)? -> (7, 12) -> (6, 12) -> (6, 7) -> (8, 7).
  - Pit (2, 5): Boulder 6 (3, 3) -> (3, 1) -> (1, 1) -> (1, 5) -> (2, 5)?
  - Pit (8, 3): Boulder 7 (8, 1) -> (8, 2) -> (8, 3)? (Requires 8, 0 passable).

# Battle Lessons
- Item Scarcity: Running out of Revives/Max Potions is lethal. Always stock up before major battles. (Turn 29510)
- Type Effectiveness: Dragon resists Fire/Electric. Use physical neutral moves (Return) for better DPS. (Turn 29459)

# Type Effectiveness (Verified)
- Dragon resists: Fire, Water, Electric, Grass. (Verified vs Dragonair, Turn 29459)
- Kingdra (Water/Dragon) resists: Fire (1/4x), Water (1/4x), Electric (1/2x), Grass (1/2x).
- Normal & Ground: Neutral vs Dragon.

# Boulder Puzzle Manual Analysis (Turn 29650)
- Observation: Row 0 tiles (silver blocks) are marked as WALL. Boulder 7 at (8, 1) cannot be pushed down from Row 1.
- Hypothesis 1: Row 0 tiles are actually passable FLOOR. (DENIED - Turn 29675-29680)
- Hypothesis 2: Boulder 7 must be pushed around the gym via Column 9 or Row 13.
- Strategy for Pit (2, 5): 
  1. Push Boulder 6 (3, 3) down to (3, 11). (Wait, (3, 8) is WALL).
  2. Alternative: Push Boulder 6 UP to (3, 1), then LEFT to (1, 1).
- Strategy for Pit (8, 7):
  1. Push Boulder 8 (8, 14) up to (8, 12), then LEFT to (6, 12) (Requires (9, 12) passable).
  2. Push up to (6, 7), then RIGHT into pit.