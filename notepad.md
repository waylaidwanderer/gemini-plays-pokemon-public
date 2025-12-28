# Tile Mechanics (Global)
- FLOOR: Traversable. (Verified: Turn 29224)
- WALL: Impassable. (Verified: Turn 29307)
- PIT: Warp tile. Falling through takes you to the floor below. (Verified: Turn 29374)
- LADDER: Warp tile. Used to travel between floors. (Verified: Turn 29242)
- BOULDER: Object. Impassable. Can be pushed with Strength. (Verified: Turn 29284)
- ICE: Sliding mechanic (Ice Path). (Verified: Turn 28256)
- ROCK: Destructible with ROCK SMASH. (Verified: Turn 29041)
- WATER: Requires Surf to traverse. (Verified: Turn 26645)
- WARP: Static transition between maps/locations. (Verified: Turn 29125)
- BOULDER BRIDGES: In Blackthorn Gym, boulders in pits (1F 2,6; 7,6; 7,7) act as passable FLOOR. (Verified: Turn 29431)

# Blackthorn City Discoveries
- Pokemon Center: (21, 29).
- Emy's House: (29, 23). Inside: Lass wants to trade DODRIO for female DRAGONAIR.
- Sign at (34, 24): "A Quiet Mountain Retreat"
- Ice Path Exit: (36, 9) on map 5_10.
- Move Deleter's House: (9, 31).
- Dragon Speech House: (13, 21). Inside: Granny and Dratini.
- Blackthorn Gym Entrance: (18, 11). Sign at (17, 13).
- Trainers Defeated: Paul (1, 14) on 1F, Mike (6, 6) on 1F, Fran (4, 11) on 2F, Cody (4, 1) on 2F, Lola (9, 2) on 1F.
- Gym Guide (7, 15) advice: Dragon-type Pokemon are weak against Ice-type moves.

# Current Strategy: Challenge Clair
- Status: Party fully healed.
- Goal: Defeat Gym Leader Clair.
- Plan:
  1. Navigate to (5, 4) on 1F.
  2. Interact with Clair (5, 3).
  3. Win the Rising Badge.

# Blackthorn Gym Layout Theory
- 1F Layout: West side contains Ladder (1, 7). East side island contains Ladder (7, 9).
- 2F Layout: Quadrants NW, NE, SW, SE. Row 13 connects East and West sides.
- Pit Destinations:
  - 2F Pit (2, 5) -> 1F (2, 6) [Entry 5]
  - 2F Pit (8, 7) -> 1F (7, 7) [Entry 6]
  - 2F Pit (8, 3) -> 1F (7, 6) [Entry 7]

# Reflection & Lessons
- **NPC Collision:** Defeated NPCs still occupy their tiles and are impassable objects. Always path around them. (Turn 29424)
- **Warp Safety:** Entry points on 1F (6, 7, 5) correspond to specific pits on 2F. Verified via entry point data. (Turn 29374)