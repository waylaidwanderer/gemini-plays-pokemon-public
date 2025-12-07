# Gem's Pokémon Crystal Journey

## 🌍 Global Status & Quests
- **Kanto Campaign:** Obtain 8 Badges.
- **Copycat (Saffron):** Quest Complete. Magnet Train Pass Obtained.
- **Rematches:** Anthony (Route 33) [Dunsparce Swarm in Dark Cave] (Radio Reset), Joey (Route 30) [Called - Radio Reset].

## Current Mission: Mt. Silver Conquest
**Status:** Silver Cave Outside.
**Objective:** Heal at PokeCenter, then find Western Entrance.
**Action Plan:**
1. Heal at PokeCenter (23, 19).
2. Explore East/South for access to Western area.

### Recent Logs
- **Larvitar Caught:** Nicknamed "BEDROCK". Sent to PC.
- **Silver Cave Room 1:** The Central Plateau (accessed via entrance at 18,11) is a DEAD END containing an Ultra Ball. The Northern and Western sections are walled off from this central area. Must find a different entrance.

## Route 28 Notes
- **Geography:** East Section connects to Victory Road Gatehouse.
- **West Section (Secret Area):** Accessed via path from Silver Cave Outside (cut tree at 34, 23).
  - **Celebrity House:** Located at (7, 3). Contains Cooltrainer F (gives TM47 Steel Wing) and a Fearow (uses Moltres sprite).
- **Landmarks:** Door to Victory Road Gate at (33, 5).

## Silver Cave Outside Notes
- **PokeCenter:** (23, 19). Fly Destination. High Ground.
- **Geography:**
  - High Ground accessible via gaps in ledges at (25, 27) and (23, 23).
  - Route 28 Entrance at Southeast corner (39, 31).
  - **Path North:** Tree cut at (34, 23). Leads to corridor at (39, 21).
  - **Western Entrance:** Likely accessed via Surf or Route 28 West.
- **Encounters:** Ponyta, Tangela, Rapidash.

## Silver Cave Room 1 Notes
- **Geography:** Central Plateau is isolated. High Ground (North) and Low Ground (Southeast) are not connected to the entrance area.
- **Status:** Central Plateau explored (Ultra Ball). Need to find path to North/West areas.
- **Mechanics:** FLOOR_UP_WALL at (9, 20) is traversable from the South (climb up) but blocks movement North (one-way ridge).

## Fuchsia Gym (Cleared)
- **Mechanic:** Invisible walls are present but explicitly marked as `WALL` in the map data. `find_path` tool navigates them perfectly.
- **Status:** Janine Defeated. Soul Badge Obtained.

## Route 17 (Cycling Road)
- **Mechanics:** Slope forces constant Down movement.
- **Escape Strategy:** **Verified:** `escape_collision` tool (Up x10, Side x10, 0ms delay) successfully breaks collision locks.
- **Trainers:**
  - Biker Riley (Weezing Lv34) - Defeated. Acts as a WALL obstacle.

## Route 16 (Archived)
- **East Side:** Cut Tree path leads to Fuchsia Speech House (Dead End).
- **West Side:** Guard script requires BICYCLE to pass. Leads to Route 17.
### Completed Objectives
- **Pewter Gym:** Brock Defeated (Boulder Badge Obtained).
- **Celadon Gym:** Erika Defeated (Rainbow Badge Obtained).

## Pewter City
- **Status:** Explored.
- **Geography:**
  - Pokémon Center: (13, 25).
  - Gym: (16, 17).
  - Mart: (23, 17).
  - Museum: (15, 9).
  - Nidoran House: (29, 13).
- **Key NPCs:** Old Man (Silver Wing Obtained) - (28, 17).

## Route 2 (Traversed)
- **Geography:** Diglett's Cave South (12, 7). Nugget House East (15, 15).
- **Status:** Path to Pewter cleared (Cut Tree removed).

## Archived Logs
- **Johto:** Champion. Rocket Disbanded.
- **S.S. Aqua:** Rescue complete.
- **Power Plant:** Power restored.

## Global Game Mechanics
### General Mechanics
- **Physics:** Boulders cannot push other boulders. You must occupy the tile 'behind' a boulder to push it.
- **'Scoot' Mechanic:** Leaving and re-entering a map refreshes map state (e.g., moving NPCs).
- **Warp Verification:** Game State 'Warps' list is the source of truth.
- **Key Items:** Passive upgrades (e.g., Radio Card) may not list in inventory.

### Pokegear & Radio Systems
- **Menu Layout:** Horizontal ROW [BACK | MAP | PHONE | RADIO]. Navigation wraps/clamps. 'B' exits to Overworld. 
- **Navigation:** Blind inputs unreliable. Reliable path to Radio: Reset to BACK (Left x3), then RADIO (Right x3). Use `force_press_button`.
- **Radio Tuning:** 'A' toggles Manual/Preset. 'Up/Down' cycles presets. 'Right' moves needle manually. Tune to 20.0 for Poké Flute.
- **Interruption Mechanics:** Receiving a phone call ABSOLUTELY resets the radio frequency to default. Must retune to 20.0 after every call before interacting with Snorlax.
- **Start Menu:**
  - **Order:** Pokedex, Pokemon, Pack, Pokegear (4th), Status, Save, Option, Exit.
  - **Cursor Memory:** Remembers last selection. Fix: Force cursor to top (Up x5) before navigating.
- **UI Mixed State:** Pokegear menu header can persist over text boxes. Press 'B' aggressively to clear.

### Tile Mechanics
- **FLOOR:** Walkable.
- **WALL:** Impassable.
- **WINDOW:** Impassable Wall.
- **PIT / HOLE:** Traversable warp.
- **CAVE:** Context Dependent. Usually a warp entrance/exit.
- **ICE:** Slippery. Slide until hitting a wall or non-ice tile.
- **LEDGE_HOP_DOWN:** One-way jump South.
- **TALL_GRASS:** Walkable (Wild Encounters).
- **WATER:** Traversable (Surf required).
- **FLOOR_UP_WALL:** Context Dependent. Verified TRAVERSABLE on Victory Road (3_91) at (13, 38). IMPASSABLE in Dragon's Den B1F, Route 10 North, Route 9, Diglett's Cave (3_84) at (12, 24), Route 3 (18, 12), Route 20 (Seafoam), Silver Cave Outside, and Victory Road (3_91) at (13, 12) (blocking Southbound movement). **In Silver Cave Room 1 (9, 20), it is traversable from the South (climb up) but blocks movement North (one-way ridge).**
- **FLOOR_LEFT_WALL:** Directional Wall. Blocks movement to the LEFT. Verified on Celadon Mansion Roof.
- **FLOOR_RIGHT_WALL:** Directional Wall. Blocks movement to the RIGHT. Verified on Celadon Mansion Roof.
- **LEDGE_HOP_LEFT:** One-way jump Left. Blocks movement from the Left (cannot walk East through it). Verified on Fuchsia City.
- **LEDGE_HOP_RIGHT:** One-way jump Right.
- **ROCK:** Breakable (Rock Smash).
- **BOULDER:** Pushable (Strength).
- **CUT_TREE:** Obstacle. Removable (Cut).
- **WARP_CARPET:** Walk off map to exit.
- **LADDER:** Context Dependent. Usually a warp, but verified as a walkable bridge (FLOOR behavior) on Cerulean Gym (7_6) and Route 24 (7_15).
- **WARP_CARPET_DOWN:** Walk Down to warp.
- **STAIRCASE:** Traversable warp.
- **COUNTER:** Impassable. Allows interaction with Entity on other side.
- **WATER/LAND Interaction:** Moving from Water to Land triggers 'Want to get off?'. Cancel with B to face Land. Moving from Land to Water triggers 'Want to Surf?'. Both prompts override hidden item checks.
- **STATUE:** Interactable. Stand BELOW, face UP, press A.
- **BOOKSHELF:** Impassable Obstacle.
- **Map Markers:** Use simple emojis (e.g., ⭐) to prevent errors.

### Battle Mechanics
- **Switch Prompt:** Defaults to YES. Press B to decline safely.
- **Accuracy Debuffs:** Effective vs strong opponents (e.g. Smokescreen).
- **Type Effectiveness:** Fire is 0.5x effective against Water/Ground (not 0.25x).
- **Weather:** Rain Dance reduces Fire-type damage by 50%.

## Strategy Notes
- **Surfing:** Pathfinding must strictly separate Land/Water.
- **Team:** Paprika (Lead), Basalt (Backup).

## Johto History
- **Cleared:** National Park, Cianwood, Mahogany, Goldenrod, Rocket Base, Ice Path, Blackthorn.
- **Key Items:** HM06 (Whirlpool), Rising Badge, Dratini.
- **Tin Tower:** Paused. Need Rainbow Wing (Catch Raikou, Entei, Suicune).

## Lessons Learned
- **Fly Reliability:** Flying to Silver Cave from Indigo Plateau proved unreliable (likely due to input timing or map constraints). Walking via Victory Road is the robust fallback.
- **Fly Mechanics:** Fly destinations are only unlocked by entering the city's Pokémon Center. Visiting the city map is not enough (missed Pallet, Viridian, Pewter).
- **Item Verification:** Passive upgrades (e.g., Radio Card) often don't appear in the inventory; trust NPC dialogue.
- **Tool Usage:** `find_path` outputs a coordinate list for `path_plan`. Do NOT use `autopress_buttons: true` with it.
- **Menu Navigation:** Blind menu macros are unreliable due to wrapping and cursor memory. Use `force_press_button` with visual verification or manual inputs.

## Trainer Rosters
- **Cerulean Gym (Misty):** Golduck (Lv42), Quagsire (Lv42), Lapras (Lv44), Starmie.
- **Saffron Gym:** Defeated.

### Elite Four Strategy
- Defeated.

## Recent Victories
- **Blaine:** Defeated (Volcano Badge).
- **Janine:** Defeated (Soul Badge).
- **Misty:** Defeated (Cascade Badge).

## Lavender Town
- **Soul House:** Located South-Central. Memorial site.
- **Radio Tower:** Located North.
- **Name Rater:** Likely the house south of the mart.

## Saffron City (Cleared)
- **Gym:** Sabrina Defeated (Marsh Badge).
- **Copycat:** Doll Returned. Train Pass Obtained.
- **Connection:** Magnet Train operational.
- **Notes:** Fisher (PC) confirmed Cerulean Cave collapse.

## Active Custom Tools & Features
- **find_path:** Pathfinding with A*.
- **select_move:** Selects battle moves via screen text.
- **force_press_button:** Automates repetitive inputs.
- **escape_collision:** Escapes slope collision locks using rapid directional bursts.
- **press_sequence:** Executes a comma-separated sequence of buttons and sleep commands.

## Power Plant
- Trade: Gym Guide (5, 5) wants Dugtrio for Magneton.

## Route 10 North
- **Split Layout:** The map is divided into two isolated sections by a vertical wall at x=3 and a horizontal barrier of FLOOR_UP_WALL tiles at y=4.
- **East Section:** Accessed from Route 9 (East). Contains PokeCenter. Dead end.
- **West Section:** Contains Rock Tunnel. Must be accessed from the western side of Route 9.

## Route 8
- **Status:** Traversing West to Saffron City.
- **Geography:**
  - **North Path:** Locked Door (10, 5), Underground Path Sign (11, 7).
  - **South Path:** Cleared. Cut Trees at (27,10) and (21,12) removed.
  - **Exit:** Saffron Gate at (4, 5) via Row 6.
- **Obstacles:**
  - **Biker Gang (x=7):**
    - Zeke (Row 10): Defeated.
    - Harris (Row 9): Defeated.
    - Unnamed (Row 8): Active. Facing Left. Battle inevitable at (6, 8).
- **Tool Usage:** Multiple tool calls in one turn overwrite each other's button outputs. Use `run_code` or a custom tool to chain multiple distinct button actions.
- **Tool Limitations:** `run_code` cannot use `autopress_buttons: true`. To execute complex button sequences, define a custom tool.
- **Sprite Reliability:** Overworld sprites can be misleading (e.g., Firebreather using Fisher sprite). Always trust the battle intro text for accurate trainer identification.

## Celadon City
- **Status:** Exploring South side. Found Prize Room at (23, 19).
- **Locations:**
  - Prize Room: (23, 19).
  - Celadon Cafe: (25, 29).
- **Key NPCs:**
  - Gentleman (PokeCenter): Friendship Rater.
  - Super Nerd (PokeCenter): Eusine? (Mentioned Suicune).
  - Cooltrainer F (PokeCenter): Confirmed Erika uses Grass-types.
  - Gentleman (Prize Room): Wanted Porygon.

## Celadon Mansion
- **Structure:** Split into East (Main) and West (Back) wings, separated by walls.
- **East Wing:** Accessible from City front. Contains Manager Suite (1F), Meeting Room (2F), Dev Room (3F), Roof East.
- **West Wing:** Accessible ONLY via Back Door (East Alley -> North Path -> West Path -> Back Door). Contains isolated stairwell connecting 1F, 2F, 3F, and Roof West.
- **Roof West:** Contains a Door (Penthouse?) and stairs down.
- **NPCs:**
  - 1F: Manager (Granny), Meowth.
  - 3F: Game Freak Staff (Designer, Programmer).
  - Roof: Fisher.
- **Pharmacist (Penthouse):** Tells a scary story only at NIGHT.
- **Shortcuts:** Cut Tree at (28, 35) removed, opening southern path to Gym.
- **Tool Usage:** Custom tools returning button arrays (e.g., `select_move`) MUST be called with `autopress_buttons: true` to execute.
- **Route 16 Correction:**
  - **East Side:** The path behind the Cut tree leads to the Fuchsia Speech House (Dead End).
  - **West Side:** The southern path (previously thought to be a dead end) is the true entrance to Cycling Road.
  - **Requirement:** Must be riding BICYCLE to pass the guard script at x=5.
- **Phone Call:** Picnicker Gina (Route 34) called. Frustrated about not catching Abra. (Note: Calls can trigger on map entry).
- **Fuchsia City Discovery:** Building entrance at (18, 3) is a FALSE door (WALL). Do not attempt to enter.
## Fuchsia Gym (Cleared)
- **Mechanic:** Invisible walls are explicitly marked as `WALL` in map data.
- **Status:** Soul Badge Obtained. Janine & Impostors defeated.
## Route 19
- **Structure:** Split into East (Dead End) and West (Path to Seafoam) sections.
- **East Entrance:** Located at Fuchsia (7, 35). Leads to a dead end.
- **Route 19 Access:** Use the Gatehouse at (7, 35). Inside, exit via the **LEFT DOOR** to reach the traversable West side.
- **Route 19 Access:** Confirmed separate lanes in gatehouse. West lane (x=4) leads to Route 19 West. East lane (x=5) leads to Dead End.
- **Route 19 Correction:** Both gatehouse exits (x=4 and x=5) lead to the same warp at Route 19 (7, 3), which deposits the player on the East (Dead End) side. The West side (with ledges) is inaccessible from this warp. Path North at x=10 needs investigation.
- Fly Map Navigation: At Fuchsia City, 'Left' input resulted in no change (remained at Fuchsia).
## Route 15
- **Structure:** Split into Upper (North) and Lower (South) paths.
- **Upper Path:** Westbound only (Ledges jump Left).
- **Lower Path:** Eastbound (Traversable).
- **Item:** Ball at (12, 5) on Upper Path (currently unreachable).
- Defeated Teacher Colette (Clefairy Lv36).
- Route 15 Wild Encounters: Nidorina, Pidgeotto.

## Route 14
- Status: Just arrived from Route 15 (West). Heading North to Lavender.
## Route 14
- Defeated PokeFan Trevor (Psyduck Lv33).
- Phone Call: Anthony (Route 33) mentioned Hoppip.
- **Route 14 Geography:** The route is vertically divided by a wall at x=10. I am currently on the West path. The West lane is a Dead End. Must use Cut Tree at (11, 14) to access the East lane.
- **TALL_GRASS:** Walkable (Wild Encounters).

## Route 13
- Arrived from Route 14.
- Geography: Fence Maze.
- Trainers:
  - Hiker Kenny (Sandslash, Graveler, Golem) - Defeated at (13, 10).
## Route 13
- **Geography:** Fence Maze with a Zigzag structure (alternating East/West corridors). Fences are `WALL` tiles. Look for gaps at the far East or West ends of each lane.
- **Trainers:**
  - Hiker Kenny (13, 10) - Defeated.
  - Pokefan M (14, 10) - Avoid/Defeated.
  - Pokefan M (25, 6) - Marked.
  - Pokefan M (32, 8) - Marked.
  - Youngster (42, 6) - Marked.
  - Youngster (43, 6) - Marked.
- **Lesson:** Mark trainers as obstacles immediately upon sighting to avoid pathfinding collisions.
## Route 12
- **Status:** Just arrived from Route 13 (South). Heading North.
- **Geography:** Boardwalk/Bridge structure over water.
## Route 12
- **Geography:** Extensive boardwalks connecting small islands. LADDER tiles here act as FLOOR (Boardwalk).
- **Locations:** House at (11, 33).
- **Barriers:** Fisher at (10, 38) blocks the east boardwalk. Item Ball at (5, 43) requires Cut.
- **Super Rod:** Obtained from Fishing Guru on Route 12.
## Route 5
- **Geography:** One-way southbound ledges dominate the center/east (Columns 6-13). Northbound travel to Cerulean City requires using the West path (Columns 1-4).
- **House (10, 11):** Blocked by ledges from the South. Must access from the North (likely via Cerulean).
- **Underground Path:** Not immediately visible, may be closed or moved in this generation.
- **Route 4 Navigation:** Confirmed DEAD END from the East. One-way Eastbound only (ledges). Successfully bypassed via Fly to Pewter City.
- **Current Route:** Pewter City -> Route 2 -> Viridian City -> Route 1 -> Pallet Town -> Surf to Cinnabar Island.
- Route 2: Left Elixer at (14, 50) due to full bag.
## Route 1
- **Status:** Traversing South to Pallet Town.
- **Geography:** Ledges and tall grass.
- **Trainers:**
  - Schoolboy Danny (7, 12) - Defeated.
  - Cooltrainer Quinn (9, 25) - Defeated.
## Pallet Town
- **Status:** Arrived via Route 1.
- **Geography:** Red's House (West), Blue's House (East), Oak's Lab (South).
- **Objectives:** Locate Oak's Lab, Surf South to Cinnabar.
## Route 21
- Debris (LADDER tiles) at (4-7, 14-15) act as obstacles.
- Swimmer Nikki (Seel x2, Dewgong) - Defeated at (11, 16).
## Cinnabar Island
- **Status:** Explored.
- **PokeCenter:** Located at (11, 11).
- **Gym Status:** Destroyed by volcano. Blaine moved to Seafoam Islands (East).
- **Blue:** Found. Declined battle. Said to challenge him at Viridian Gym.
## Route 20
- **Status:** Surfing East to Seafoam Islands.
- **Trainers:**
  - Swimmer Cameron (Marill Lv34) - Defeated.
## Viridian City
- **Status:** Exploring.
- **Geography:**
  - Pokémon Center: (23, 25).
  - Gym: To be located.
- Trainer House: (23, 15).
- Gym: (27, 7). 
- Viridian Gym: (32, 7). Blocked by Gramps at (30, 8).
## Viridian City
- **Geography:**
  - Pokémon Center: (23, 25).
  - Trainer House: (23, 15).
  - Nickname House: (21, 9).
  - Gym: (32, 7). Entrance blocked by Gramps at (30, 8).
- **Strategy:** Navigate around the Gym building (North side) to reach the entrance from the East.
- **Viridian Gym:** Found Blue at (5, 3). Challenging him now.
- **Battle Strategy Update:** Paprika critical. Gyarados too strong. Switching to fodder to stall out Hydro Pump PP (5 total) and heal Paprika with Super Potions.
### Menu Navigation
- **Start Menu Order:** Pokedex, Pokemon, Pack, Pokegear, Status, Save, Option, Exit.
- **Cursor Memory:** The game remembers the last cursor position. Always visually confirm or reset cursor (e.g., press Up x5) before navigating blind.
- **Fly Destination Lock:** Confirmed inability to Fly to Pewter/Viridian/Pallet. Reinforces the rule that entering the Pokémon Center is required to unlock them.
- **Fly Destination Lock:** Confirmed inability to Fly to Pewter/Viridian/Pallet. Reinforces the rule that entering the Pokémon Center is required to unlock them.
- Fly Map Navigation: From Indigo Plateau, 'Down' jumps directly to Cinnabar Island. 'Right' does nothing. This confirms intermediate towns (Pewter, Viridian, Pallet) are skipped if not visited properly.
## Victory Road Gate
- **Status:** Exploring.
- **Geography:**
  - East Exit: Route 22.
  - West Exit: Likely Route 28 (Mt. Silver).
  - North Exit: Likely Victory Road.
  - South Exit: Route 26.
- **Observations:** Black Belt guard at (12, 5) is gone (likely due to 16 badges). Path West appears open.
## Victory Road Gate
- **Warp Anomaly:** Tiles at (1, 7) and (2, 7) are labeled `WARP_CARPET_DOWN` but do not trigger when walked over horizontally. Movement south is blocked by a wall. Investigating exit mechanism (likely walking off map edge).
## Route 28
- **Mechanic Discovery:** WARP_CARPET_DOWN tiles may require walking 'Down' into a visual wall to trigger, rather than just walking onto them.
- **Status:** Exploring West. Confirmed 'ROUTE 28' via sign at (31, 5).
## Silver Cave Room 1
- Protein found at (15, 29).
- Ultra Ball found at (7, 18).
## Silver Cave Outside
- **Status:** Surfing South to find High Ground access.
- **Geography:**
  - Cave Entrance: (18, 11).
  - PokeCenter: (23, 19).
  - Western Shore (x<14): Dead end blocked by ledges to the North.
  - Eastern Shore (Row 28): Landing spot. Path to PokeCenter found via gaps in ledges at (25, 27) and (23, 23). Route 28 likely accessible from the high ground near PokeCenter.
- **Events:**
  - Phone Call: Joey (Route 30). Radio reset.
- **Wild Encounters:** Ponyta, Tangela.
### Menu Navigation
- **Wrapping:** Menus wrap around! Pressing 'Up' at the top moves to the bottom. Do not blindly mash 'Up' to reset cursor position.
- **Tool Usage Correction:** Must set `buttons_to_press` to `["tool"]` when using `press_sequence` or any tool that presses buttons. Putting manual buttons in `buttons_to_press` overrides the tool.
- **Strategy Update:** Fly failed. Proceeding on foot via Victory Road.
### Mechanic Correction
- **Capture Sequence:** In this version, the Nickname prompt appears **BEFORE** the 'Sent to Bill's PC' message, even if the party is full. Do not assume auto-transfer skips the nickname.
- Capture Mechanic: Nickname prompt occurs BEFORE transfer to PC, regardless of party size.
## Route 28 Secret Area
- **Access:** Via secret path from Silver Cave Outside (cut tree at 34, 23).
- **Steel Wing House (19_4):** Located at (7, 3) in the secret area.
  - **NPC:** Cooltrainer F (Celebrity?). Gave TM47 (Steel Wing). Asked for secrecy.
  - **Object:** Fearow (uses Moltres sprite).