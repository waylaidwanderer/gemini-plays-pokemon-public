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
  - Test 1 (Turn 29675): (5, 0) is a WALL.
  - Test 2 (Turn 29678): (7, 0) is a WALL.
  - Pushing a boulder: First press pushes it, second press moves player into its old tile.
  - All pits are empty after gym reset. (Turn 29620)
  - Column 4 is mostly WALL, gap at Row 13.
  - Column 9 is a north-south corridor.
- Layout Corrections:
  - (4, 1) is Cody (Wall).
  - (4, 11) is Fran (Wall). Gap to east is at Row 13.
  - Row 13 passage at (4, 13) connects east/west sections.
  - Boulder 7 was pushed Right from (6, 1) to (8, 1) (Turns 29674-29675).

# Battle Lessons
- Item Scarcity: Running out of Revives/Max Potions is lethal. Always stock up before major battles. (Turn 29510)
- Type Effectiveness: Dragon resists Fire/Electric. Use physical neutral moves (Return) for better DPS. (Turn 29459)

# Type Effectiveness (Verified)
- Dragon resists: Fire, Water, Electric, Grass. (Verified vs Dragonair, Turn 29459)
- Kingdra (Water/Dragon) resists: Fire (1/4x), Water (1/4x), Electric (1/2x), Grass (1/2x).
- Normal & Ground: Neutral vs Dragon.

# Boulder Puzzle Manual Analysis (Turn 29650)
- Observation: Row 0 tiles (silver blocks) are marked as WALL. Boulder 7 at (8, 1) cannot be pushed down from Row 1.
- Hypothesis 1: Row 0 tiles are actually passable FLOOR. (DENIED - Turn 29675, 29678)
- Test 3: Check (9, 0) for passability.
- Hypothesis 2: Boulder 7 must be pushed around the gym via Column 9 or Row 13.
- Strategy for Pit (2, 5): 
  1. Push Boulder 6 (3, 3) down to (3, 11).
  2. Push left at (3, 11) to (1, 11) (requires Fran defeated).
  3. Push up to (1, 5), then right into pit.
- Strategy for Pit (8, 7):
  1. Push Boulder 8 (8, 14) up to (8, 10), then left to (6, 10).
  2. Push up to (6, 7), then right into pit.