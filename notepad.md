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
   - Bx3 (Clear) -> Start -> Up x8 (Reset Main) -> Down (Pokemon) -> A -> 
   - Up x7 (Reset Party) -> Down x4 (Gorp Slot 5) -> A -> 
   - Up x5 (Reset Sub-menu) -> Down x3 (Item) -> A -> 
   - Up x2 (Reset Item-menu) -> Down (Take) -> A -> sleep -> A (Clear text).
2. Restore Leftovers to Gorp.
   - Select Gorp -> Item -> Give -> Items Pocket -> Leftovers -> A -> sleep -> A.
3. Fly to Cianwood.
   - Select Icarus -> Fly -> Left x20 -> A -> sleep -> A -> sleep -> A.

Total Fly failures: 22. Current Turn: #51056. Goal: Recover Master Ball.
Logic: Absolute resets for all menu levels to bypass persistence and ensure correct selection.
Suicune Pursuit: Sighting #1 at Cianwood (14, 10) pending. Eusine battle prep: Lead Calcifer.
Whirl Islands Legend: Needs Silver Wing and Whirlpool.
Cianwood Area: Rock Smash boulders north, Pharmacy for Amphy, Mania's Shuckle.
Progress: Turn #50620 start. Smashed rocks (5, 29), (4, 25), (8, 16), (9, 17). Defeated Mathew.
Menu Mechanics: 
- Start Menu: 1. Pokedex, 2. Pokemon, 3. Pack, 4. Pokegear, 5. Gem, 6. Save, 7. Option, 8. Exit.
- Party Menu: 1. Calcifer, 2. Xenon, 3. Kimchi, 4. Gneiss, 5. Gorp, 6. Icarus, 7. Cancel.
- Gorp Menu: 1. SURF, 2. STATS, 3. SWITCH, 4. ITEM, 5. CANCEL. (ITEM is Slot 4).
- Item Sub-menu: 1. GIVE, 2. TAKE.
- Hallucination Zone: Avoid (14, 10) and (13, 10). Currently at (15, 13). Logic: Breaking the sequence into discrete operations to handle text boxes. Step 1: Recover Master Ball.