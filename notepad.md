# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Warp tile. Falling through takes you to the floor below.
- LADDER: Warp tile. Used to travel between floors.
- BOULDER: Object. Impassable. Can be pushed with Strength.
- ICE: Sliding mechanic (Ice Path).
- ROCK: Destructible with ROCK SMASH.
- WATER: Requires Surf to traverse.
- WARP: Static transition between maps/locations.
- BOULDER BRIDGES: Boulders in pits (1F 2,6; 7,6; 7,7) act as passable FLOOR.

# Blackthorn City Discoveries
- Pokemon Center: (21, 29).
- Emy's House: (29, 23). Trade DODRIO for female DRAGONAIR.
- Move Deleter's House: (9, 31).
- Dragon Speech House: (13, 21).
- Blackthorn Gym Entrance: (18, 11).
- Trainers Defeated: Paul (1, 14) on 1F, Mike (6, 6) on 1F, Lola (9, 2) on 1F, Fran (4, 11) on 2F, Cody (4, 1) on 2F.
- Gym Guide (7, 15) advice: Dragon-type Pokemon are weak against Ice-type moves.

# Strategy: Challenge Clair
- Status: Party fully healed.
- Goal: Defeat Gym Leader Clair at (5, 3) on 1F.
- Plan:
  1. Navigate to (5, 4) on 1F.
  2. Interact with Clair (5, 3).
  3. Defeat Clair and obtain the Rising Badge.

# Blackthorn Gym Layout Theory
- 1F Layout: Mainland (Rows 12-17) and Island (Rows 2-10) are isolated on 1F.
- Connection: Travel between Mainland and Island requires detour through 2F via ladders at (1, 7) and (7, 9).
- Pit Destinations:
  - 2F Pit (2, 5) -> 1F (2, 6)
  - 2F Pit (8, 7) -> 1F (7, 7)
  - 2F Pit (8, 3) -> 1F (7, 6)

# Reflection & Lessons
- **NPC Collision:** Defeated NPCs still occupy their tiles and are impassable objects. Always path around them. (Turn 29424)
- **Warp Safety:** Entry points on 1F (6, 7, 5) correspond to specific pits on 2F. (Turn 29374)