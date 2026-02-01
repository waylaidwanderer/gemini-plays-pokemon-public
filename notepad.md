# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026
- Current Leg: Route 42 Surfing
- Current Task: Investigate radio signal in Mahogany Town (Lance's Lead)
- **Gym**: Located at (7, 13).
- **Lake of Rage**: Locals mention it (Route 43 North).
- **Route 42**: Came from West.

### Important Mechanics & Notes
- **Hiker Benjamin**: Sells RageCandyBars at (19,8). STOP BUYING.
- **Gatehouse (15, 13)**: Pokemon Center (Sign says POKE).
- **Route 42 Navigation**: Path East is blocked by trees at x=18. Must go South to y=16/17 to bypass.
- **Route 42 Secrets**: Fake tree at (7, 5) leads to Mt. Mortar upper entrance.
- **Mt. Mortar**:
  - Explored 1F and Upper area partially.
  - "Angry Gyarados" event blocks inner path.
  - Exits known: (9, 51) West, (17, 35) Middle?
- **Mahogany Town**:
  - Nurse Joy is MISSING from the Pokemon Center. Cannot heal here.
  - Gentleman reports Team Rocket at Lake of Rage.
  - Team Rocket has returned.
  - Need to investigate Lake of Rage (North).
### Tile Mechanics
- **Route 42 (TYPE_3fe2)**: Can be shoreline or water. Test via bumping/interaction, don't assume.
- Route 42 Obstacles:
  - (7, 12): Small Tree (TYPE_2889).
  - (8, 13): Big Tree (TYPE_80fc), not cuttable.
  - (7, 14): Small Tree (TYPE_2889).
  - Boxed in at (7, 13). Must backtrack West to escape.
- **Route 42 (East Side) Obstacles**:
  - (45, 9): Small Tree (TYPE_2889) in the water.
  - (47, 8): Swimmer Simon (Glitchy interaction).
- **Route 43 (Map 9_5)**:
  - Connects Mahogany Town (South) to Lake of Rage (North).
  - **Trainers**: Pokemaniacs Ron, Ben, Camper Spencer (Defeated).

### Tile Mechanics
- **Walkable Trees (TYPE_fed7)**: These tiles look like trees but are walkable. Essential for navigating Route 30 and Route 43 to bypass obstacles.
- **Map 9_6 Identification**: This is the **Lake of Rage** area (or entrance). It has water, rain/snow, and the "Angry Gyarados" event. It is NOT Mt. Mortar inner cave as previously thought.
- Detour: Fly to Cherrygrove City to trade Red Scale for Exp. Share with Mr. Pokemon (Route 30). Then Fly to Mahogany.
- Route 31 Connection: The Cut tree at (25, 10) on Map 26_2 connects to the WEST side of Route 30 (x=5), creating a loop. The East side entrance (Mr. Pokemon) must be further East.
- **Fly Menu Navigation**: Use **UP/DOWN** buttons to select towns. Left/Right does not work.
- **Route 30 Mechanics**: Confirmed that `TYPE_fed7` tiles are walkable trees. Path to Mr. Pokemon: Go East to x=17, then North. Must dogleg East at (17, 18) to bypass walls at (17, 17)/(17, 16), then cut back West at (18, 14).
- **Exp. Share**: Obtained and equipped on Bolin (Sandshrew).
- **Current Location**: Team Rocket HQ - B1F (Computer Room).
- **Goal**: Disable statue alarms. DONE (Computer at 19,11).
- **Warp Panel Hint**: Scientist warned of a warp panel "up ahead".

### Team Rocket HQ (Map 3_49)
- **Start Time**: Turn ~22050.
- **Entrance**: Stairs from Souvenir Shop.
- **Mechanics**:
  - **Statue Alarms**: Passing in front of Persian statues (e.g., at x=6) triggers Grunt battles. They respawn indefinitely until a "secret switch" is found.
  - **Traps**: Floor traps exist.
  - (2, 4): Koffing/Geodude?
  - (1, 8): Voltorb Trap (Can't Run).
  - (5, 8): Koffing Trap (Can't Run?).
  - (5, 10): Geodude Trap (Can't Run).
  - (4, 11): Koffing Trap (Can't Run).
- **Goal**: Find the "secret switch" (Suspicious machine found at 24, 5).
- **Exploration Note**: West corridor (x<6) is a dead end with a trap at (2,4). Lower corridor accessed via gap at (9, 4).
- **Statue Alarm**: x=24 statues are ACTIVE. Triggered battle at (24, 6). Likely infinite respawn.
- **Statue Alarm**: Expecting battle at x=6 (Active).
- **Battle Menu Mechanics**: 
  - The move selection menu is a **Vertical List**.
  - **Cursor Memory**: The cursor **remembers the last used move** position within the battle. It does NOT reset to the top when re-entering the FIGHT menu.
  - To re-use the same move: Just press 'A'.
  - To switch moves: You must account for the current cursor position.
  - Wraps: Up from Top -> Bottom, Down from Bottom -> Top.