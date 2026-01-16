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
- Suicune Sighting #1: Cianwood City, northern coast (approx 14, 10). Pending.
- Menu Mechanics: Main Menu (8 items) wraps 1 <-> 8. Party Menu (6 items) wraps 1 <-> CANCEL <-> 6.
- Sub-menu Layout (Icarus): FLY, STATS, SWITCH, MOVE, ITEM, CANCEL.
- Suicune Quest Start: Turn #50620. (Current Turn: #51007)
- Fly Strategy: v16.0 failed. Attempt #18 failed due to Menu Persistence. Discovery: The Party Menu cursor remembers its last position (unlike the Start menu, which resets if closed properly, but I'm mashing resets anyway). If the cursor starts on Slot 3, Up(x9) lands on Slot 2 (Haunter) -> STATS. Total Fly failures: 18. Current Turn: #51026. Goal: Cianwood (14, 10). Prep: Calcifer in lead. Focus: SUICUNE. Logic: Clearing the status screen and exiting the lab to reset the overworld state before attempting a manual flight. Precision is key.
- Fly attempts failed: 9.
- Lesson: Party menu cursor persistence vs Start menu reset. Menu wrapping: 1 (Calcifer) <-> 7 (Cancel) in party.
- Icarus is at index 6.
- Item Change: Icarus (Pidgeotto) is holding a POKé BALL. AMULET COIN is in bag.
- Party Order: 1. Calcifer, 2. XENON, 3. KIMCHI, 4. GNEISS, 5. GORP, 6. ICARUS.
- Suicune Quest: Turn #50620. Smashed rocks at (5, 29), (4, 25), (8, 16), (9, 17).
- Suicune Sighting #1: Cianwood City, northern coast (approx 14, 10). Pending.