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
Menu Mechanics: 
- Start Menu (Slot 1-8): 1. POKEDEX, 2. POKEMON, 3. PACK, 4. POKEGEAR, 5. PLAYER, 6. SAVE, 7. OPTION, 8. EXIT. (Wraps 1 <-> 8).
- Party Menu (Slot 1-7): 1-6. Pokemon, 7. CANCEL. (Wraps 1 <-> 7).
- Persistence: Both menus remember their last cursor position.
- Fly Strategy: Attempt #23. Current State: Pokedex entry for Kadabra. Strategy: B(x3) to exit Pokedex -> Move to (14, 10) -> Start -> Up(x8) (Reset to Pokedex) -> Down (Pokemon) -> A -> Up(x7) (Reset to Slot 1) -> Up(x2) (Slot 6 Icarus) -> A -> A (FLY) -> Left(x20) -> A -> A -> A.
- Total Fly failures: 21. Turn: #51044. Goal: Cianwood (14, 10). Logic: Absolute resets are the only way to handle persistent menu memory.
- Sighting Trigger: Move to (14, 10) in Cianwood. Lead: Calcifer.
- Whirl Islands Legend: Learned from Lugia Speech House. Needs Silver Wing and a move for whirlpools.
- Mania's House: Mania wants his Shuckle back.
- Rock Smash: Boulders north of Cianwood can be crushed.
- Photo Studio: Fishing Guru is inside.
- Poke Seer: Lives in Cianwood.
- Pharmacy: Secretpotion for Amphy? (Wait, I already have the badges, but Amphy is in the lighthouse in Olivine).
- Olivine Lighthouse: Amphy needs medicine from Cianwood Pharmacy. (Verify if completed).
- Kurt & Oak: They are long-time acquaintances.
- Elm & Oak: Elm was Oak's assistant.
- Radio Show: Oak was convinced by Mary.
- Suicune: Sighted in Cianwood, Ecruteak, and Mt. Mortar. Next sighting: Cianwood (14, 10).
- Eusine: Following Suicune. Will battle in Cianwood. Lead: Calcifer.
- Suicune Quest Start: Turn #50620.
- Fly Strategy failure count: 21. Attempting v24.0 (Absolute Manual).