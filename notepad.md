# Gem's Pokémon Crystal Journey

## 🌍 Global Status & Quests
- **Kanto Campaign:** Obtain 8 Badges.
- **Copycat (Saffron):** Quest Complete. Magnet Train Pass Obtained.
- **Rematches:** Anthony (Route 33) [Spearow Swarm], Joey (Route 30).

## 📍 Current Mission: Kanto Journey
**Status:** In Saffron City. Heading North to Route 5.
**Objective:** Travel to Cinnabar Island (Blaine).
**Action Plan:**
1. Traverse Route 8 -> Saffron City -> Route 5 -> Cerulean City -> Route 4 -> Pewter City -> Route 2 -> Viridian City -> Route 1 -> Pallet Town.
2. Surf South to Cinnabar Island.

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
- **path:** Harness Feature. Automatically moves along the `path_plan` coordinate list. NOT a custom tool.

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
- **ICE:** Slippery. Slide until hitting a wall or non-ice tile.
- **LEDGE_HOP_DOWN:** One-way jump South.
- **TALL_GRASS:** Walkable (Wild Encounters).
- **WATER:** Traversable (Surf required).
- **FLOOR_UP_WALL:** Context Dependent. Verified TRAVERSABLE on Victory Road (3_91) at (13, 38). IMPASSABLE in Dragon's Den B1F, Route 10 North, Route 9, Diglett's Cave (3_84) at (12, 24), and Route 3 (18, 12).
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
- **Item Verification:** Passive upgrades (e.g., Radio Card) often don't appear in the inventory; trust NPC dialogue.
- **Tool Usage:** `find_path` outputs a coordinate list for `path_plan`. Do NOT use `autopress_buttons: true` with it.
- **Menu Navigation:** Blind menu macros are unreliable due to wrapping and cursor memory. Always use `navigate_menu` or visual feedback tools.

## Trainer Rosters
- **Cerulean Gym (Misty):** Golduck (Lv42), Quagsire (Lv42), Lapras (Lv44), Starmie.
- **Saffron Gym:** Defeated.

### Elite Four Strategy
- Defeated.

## Recent Victories
- **Misty:** Defeated (Cascade Badge).
- **Champion Lance:** Defeated.
- **Lt. Surge:** Defeated.

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
- **navigate_menu:** Robustly selects menu options by reading screen text.
- **escape_collision:** Escapes slope collision locks using rapid directional bursts.

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