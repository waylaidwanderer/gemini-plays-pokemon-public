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
  - Sequence using UP from New Bark Town: New Bark -> Ecruteak -> Azalea -> Mahogany -> Olivine -> Silver Cave -> Goldenrod.
  - UP cycles through fly points.
  - Current Position: Fly map at Goldenrod City.
  - Goal: Cianwood City.

# Strategy: Fly to Cianwood (Suicune Pursuit)
- Time Tracking: Started Turn 50620 (Current Turn: 51130).
- Status: Item Crisis Resolved. Master Ball and Leftovers restored.
- Plan:
  1. Confirm Cianwood City on Fly map (In progress).
  2. Move to (14, 10) in Cianwood to trigger Suicune sighting.
- Prep: Lead Calcifer for Eusine battle.

# Progress Tracking
- Smashed Rocks (Cianwood): (5, 29), (4, 25), (8, 16), (9, 17).
- Defeated Swimmer Mathew (17, 46).
- Fly attempt count: 26 (Success on map navigation).
## Menu Relational Behavior
- Start Menu: Pressing Up from Pokedex (1) wraps to EXIT (8).
- Party Menu: Pressing Up from Slot 1 wraps to CANCEL (7).
- Bag (Items): Vertical list with scrolling. Cursor persists on last item selected.
- Sub-menus: Usually 4-6 items. Pressing Up from item 1 wraps to the bottom item.
- Fly Map (Johto Cycle): UP cycles through cities. Verified Sequence: New Bark -> Ecruteak -> Azalea -> Mahogany -> Olivine -> Silver Cave -> Goldenrod -> Violet -> Cianwood.