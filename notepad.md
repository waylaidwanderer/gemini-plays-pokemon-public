# Game Mechanics & Systems
## Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY: Impassable.
- WATER: Traversable via Surf.
- LEDGE_HOP_DOWN: One-way (South).
- FLOOR_UP_WALL (Terrace): One-way (North).
- ROCK (Object): Traversable after Rock Smash.

## Menu Mechanics
- Start Menu (Persistent): 1. Pokedex, 2. Pokemon, 3. Pack, 4. Pokegear, 5. Player, 6. Save, 7. Option, 8. Exit.
- Party Menu (Persistent): 1-6. Pokemon, 7. Cancel.
- Gorp (Snorlax) Menu: 1. SURF, 2. STATS, 3. SWITCH, 4. MOVE, 5. ITEM, 6. CANCEL.
- Fly Map: New Bark Town (East), Cianwood (West).

# Strategy: Fly to Cianwood (Suicune Pursuit)
- Time Tracking: Started Turn 50620.
- Plan:
  1. Fly to Cianwood (Far West on map).
  2. Move to (14, 10) in Cianwood to trigger Suicune sighting.
- Prep: Lead Calcifer for Eusine battle.

# Area Notes: Cianwood City
- Lugia Speech House: Whirl Islands legend (Silver Wing/Whirlpool required).
- Pharmacy: Secretpotion for Amphy.
- Mania's House: Mania wants his Shuckle back.
- Rock Smash: Boulders north of town.

# Progress Tracking
- Smashed Rocks: (5, 29), (4, 25), (8, 16), (9, 17).
- Fly Attempt Status: 24 failures. Transitioning to step-by-step manual navigation.
## Menu Relational Behavior
- Start Menu: Pressing Up from Pokedex (1) wraps to EXIT (8).
- Party Menu: Pressing Up from Slot 1 wraps to CANCEL (7).
- Bag (Items): Vertical list with scrolling. Cursor persists on last item selected.
- Sub-menus: Usually 4-6 items. Pressing Up from item 1 wraps to the bottom item.
- Fly Map: Cursor starts at current location. Left moves west. A selects.