# Game Mechanics & Systems
## Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY: Impassable.
- WATER: Traversable via Surf.
- LEDGE_HOP_DOWN: One-way (South).
- FLOOR_UP_WALL (Terrace): One-way (North).
- ROCK (Object): Traversable after Rock Smash.

## Fly Map Reference
- New Bark Town: Far East.
- Cianwood City: Far West.
- Navigation: Open Pokemon Menu -> Select Flyer -> FLY -> Move cursor to target city -> A.

# Active Strategy: The Suicune Pursuit
- **Primary Goal:** Trigger Suicune sighting in Cianwood City.
- **Target Coordinate:** (14, 10) in Cianwood (Northern coastline).
- **Pathing:** Rows 13-15.
- **Battle Prep:** Lead with Calcifer (Lv64 Typhlosion) for Eusine (Drowzee, Haunter, Electrode).

# Area Notes: Cianwood City
- **Dead Ends:** (11, 15) cliff pocket.
- **Exploration Targets:** Row 15 gaps (X=13, 15), Row 13 gaps (X=13, 15).
- **Sighting Trigger:** Move to (14, 10).

# Progress Tracking
- Started Suicune Quest: Turn #50620. (Current Turn: #51000)
- Smashed Rocks (Cianwood): (5, 29), (4, 25), (8, 16), (9, 17). Verified as FLOOR.
- Defeated Trainers (Route 41): Swimmer Mathew (17, 46).
Item Crisis Management:
1. Recover Master Ball from Gorp.
   - Start Menu: Down x2 (from EXIT to POKEMON) -> A.
   - Party Menu: A (Select GORP Slot 5 - assumed persistent).
   - Gorp Menu: Down x3 (to ITEM) -> A.
   - Item Menu: Down (to TAKE) -> A.
2. Restore Leftovers to Gorp.
   - Select GORP -> ITEM -> GIVE -> LEFTOVERS.
3. Fly to Cianwood.
   - Select ICARUS -> FLY -> Left x20.
Total Fly failures: 23. Current Turn: #51059. Goal: Recover Master Ball.
Logic: Manual navigation to handle persistent cursors and verify each step.
Suicune: Cianwood (14, 10). Prep: Lead Calcifer.
Whirl Islands: Needs Silver Wing/Whirlpool.
Progress: Rocks smashed (5,29, 4,25, 8,16, 9,17). Mathew defeated.
Menu Persistence confirmed: Start menu remembers last position. Party menu remembers last position. Sub-menus remember last position.
Gorp Menu: 1. SURF, 2. STATS, 3. SWITCH, 4. ITEM, 5. CANCEL.
Icarus Menu: 1. FLY, 2. STATS, 3. SWITCH, 4. MOVE, 5. ITEM, 6. CANCEL. (FLY is Slot 1).
Logic: Breaking the sequence to handle text boxes and verify state. Step 1: Recover Master Ball.