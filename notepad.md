# Game Mechanics & Systems
## Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY: Impassable.
- WATER: Traversable via Surf.
- LEDGE_HOP_DOWN: One-way (South).
- FLOOR_UP_WALL (Terrace): One-way (North).
- ROCK (Object): Traversable after Rock Smash.

## Menu Mechanics
- Start Menu (Persistent): 1. POKEDEX, 2. POKEMON, 3. PACK, 4. POKEGEAR, 5. PLAYER, 6. SAVE, 7. OPTION, 8. EXIT.
- Party Menu (Persistent): 1-6. Pokemon, 7. CANCEL.
- Fly Map (Johto):
  - Cursor cycles through cities.
  - Multiple presses (approx 2-3) of a direction may be required to reach the next city node.
  - Sequence using UP from New Bark Town: New Bark -> Ecruteak -> Azalea -> Mahogany -> Olivine -> Silver Cave -> Goldenrod -> Violet -> Cianwood.
  - UP cycles through fly points. Approx 5-10 presses per jump.
  - Current Position: Cianwood City (23, 44).
  - Goal: Cianwood City (14, 10).

# Strategy: Fly to Cianwood (Suicune Pursuit)
- Time Tracking: Started Turn 50620.
- Fly Attempt Status: SUCCESS. Landed in Cianwood City at (23, 44) on Turn 51131.
- Total Fly Failures: 26.
- Plan:
  1. Move to (14, 10) in Cianwood to trigger Suicune sighting.
  2. Prepare for battle with Eusine (Lead Calcifer).
- Prep: Lead Calcifer (Lv64 Typhlosion) for Eusine battle.

# Progress Tracking
- Smashed Rocks: (5, 29), (4, 25), (8, 16), (9, 17).
- Defeated Swimmer Mathew (17, 46).
- Arrived in Cianwood via Fly: Turn 51131.

# Fly Map Discovery: Johto City Cycle
- Sequence using UP: New Bark -> Ecruteak -> Azalea -> Mahogany -> Olivine -> Silver Cave -> Goldenrod -> Violet -> Cianwood.
- Each jump requires approx 5-10 presses of UP.
- This cycle bypasses the need for complex grid navigation.