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
- Party Menu (Persistent): 1-6. Pokemon, 7. CANCEL. (Up from 1 -> 7).
- Sub-menus: Pressing Up from item 1 wraps to the bottom.
- Bag (Items): Scrolling list. Cursor persists on last item.
- Fly Map: New Bark Town (East), Cianwood (West). ~25 Lefts to reach western edge.

# Strategy: Fly to Cianwood (Suicune Pursuit)
- Time Tracking: Started Turn 50620.
- Plan:
  1. Open Start Menu -> POKEMON.
  2. Select ICARUS (Slot 6) -> FLY.
  3. Navigate Map to Cianwood (Far West) -> Confirm.
  4. Move to (14, 10) in Cianwood to trigger Suicune.
- Prep: Lead Calcifer for Eusine battle.

# Area Notes: Cianwood City
- Lugia Speech House: Whirl Islands legend (Silver Wing/Whirlpool required).
- Pharmacy: Secretpotion for Amphy.
- Mania's House: Mania wants his Shuckle back.
- Rock Smash: Boulders north of town.

# Progress Tracking
- Smashed Rocks: (5, 29), (4, 25), (8, 16), (9, 17).

# Trainer Rosters
- Eusine (Suicune Hunter): Drowzee, Haunter, Electrode. (Last seen: Ecruteak Gym). Will battle in Cianwood.

# Fly Map Navigation (Verified)
- New Bark Town to Cianwood: [Pending verification of exact presses]
- Observation: Map cursor may require a delay or specific text clearance before moving.

# Fly Map Responsiveness
- Observation: Map may require a delay (sleep) after opening before accepting directional input.
- Current Test: sleep 2000ms followed by 20x Left presses.
- Goal: Verify if cursor moves and identifies cities between New Bark Town and Cianwood.