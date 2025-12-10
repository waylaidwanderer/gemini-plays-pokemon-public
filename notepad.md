# Gem's Pokémon Crystal Journey

## 🌍 Global Status & Quests
- **Kanto Campaign:** Obtain 8 Badges.
- **Copycat (Saffron):** Quest Complete. Magnet Train Pass Obtained.
- **Rematches:** Anthony (Route 33) [Dunsparce Swarm in Dark Cave] (Radio Reset), Joey (Route 30) [Flavor: Rattata/Caterpie - No Rematch].

# 🏆 POKÉMON CRYSTAL: POST-GAME 🏆
**Status:** Red Defeated! The 'mysterious message' was just a tutorial.
**Next Stop:** Ruins of Alph / Ecruteak City.
**Current Objectives:**
1. Locate Larvitar & Organize Team.
2. Train team to Level 20 (Battle Tower Prep).
3. Explore Ruins of Alph.
**The Champion Team:**
- **Paprika (Typhlosion Lv75):** The MVP.
- **Basalt (Geodude):** Support.
- **Vortex (Pidgeotto):** Flyer.
- **Bahamut (Dratini):** The Future.
- **XQH & F:** HM Squad.

**Current Objective:** Challenge Battle Tower (Level 20).
**Strategy:** Equip held items (Quick Claw, Berries). Go to Battle Tower (West of Olivine).
**Team:**
1. Vortex (Pidgeotto) Lv19
2. Bedrock (Larvitar) Lv20
3. Bahamut (Dratini) Lv17
**Status:** Battle Tower (Lobby).
**Battle Tower Rules:**
- 3 Pokémon team.
- All Pokémon must be ≤ Level 20 for the L:20 challenge.

**Observed Threats:**
- **Miltank (Teacher Marino):** Knows Surf (Water) and Thunder (Electric). Wiped Rock/Ground/Flying team. Counter: Dragon type (Bahamut).

### Recent Logs (Archived)
- **Route 38:** Explored. Larvitar "BEDROCK" caught.
- **Phone Calls:** Anthony (Route 33) - Flavor text.

### Current Logs
- **Lesson:** ALWAYS verify Map ID and coordinates against Game State before assuming location to avoid hallucinations (e.g., thinking I'm outside when in PC).
- **Route 29 Navigation:** Northern path (Berry Tree) accessible via Cut Tree at (30, 9) or from New Bark Town (East).
- **Action:** Withdrew XQH (Sandshrew) for Cut. Heading to Route 29.
- **Moomoo Farm:** Quest Complete! Miltank cured. Reward: TM13 (Snore). Farmer now sells Moomoo Milk.

## Mt. Silver & Route 28 (Archived)
- **Status:** Fully Explored. Red Defeated.
- **Route 28:** Secret House (TM47 Steel Wing) accessed via Cut path from Silver Cave Outside.
- **Silver Cave:**
  - **Outside:** PokeCenter (23,19).
  - **Room 1:** East path (x=15) leads North.

## Fuchsia Gym (Cleared)
- **Mechanic:** Invisible walls are present but explicitly marked as `WALL` in the map data. `find_path` tool navigates them perfectly.
- **Status:** Janine Defeated. Soul Badge Obtained.

## Route 17 (Cycling Road)
- **Status:** Traversed. Slope mechanics require `escape_collision` tool.

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
- **FLOOR_UP_WALL:** Context Dependent. Verified TRAVERSABLE on Victory Road (3_91) at (13, 38). IMPASSABLE in Dragon's Den B1F, Route 10 North, Route 9, Diglett's Cave (3_84) at (12, 24), Route 3 (18, 12), Route 20 (Seafoam), Victory Road (3_91) at (13, 12), , **Route 28 (4, 14)**, **Route 28 (30, 12)**, and **Route 28 (31, 12)**. **Silver Cave Outside (5, 30):** Verified as Ridge Base blocking movement from North. **Silver Cave Room 1 (9, 20):** Impassable from South (Ridge Base). Verified.
- **FLOOR_LEFT_WALL:** Directional Wall. Blocks movement to the LEFT. Verified on Celadon Mansion Roof.
- **FLOOR_RIGHT_WALL:** Directional Wall. Blocks movement to the RIGHT. Verified on Celadon Mansion Roof.
- **LEDGE_HOP_LEFT:** One-way jump Left. Blocks movement from the Left (cannot walk East through it). Verified on Fuchsia City.
- **LEDGE_HOP_RIGHT:** One-way jump Right.
- **ROCK:** Breakable (Rock Smash).
- **BOULDER:** Pushable (Strength).
- **CUT_TREE:** Obstacle. Removable (Cut).
- **WARP_CARPET:** Walk off map to exit.
- **LADDER:** Context Dependent. Usually a warp, but verified as a walkable bridge (FLOOR behavior) on Cerulean Gym (7_6) and Route 24 (7_15).
- **WARP_CARPET_DOWN:** Walk Down to warp. May require walking *into* the bottom map edge or wall while standing on the tile to trigger, rather than just landing on it.
- **STAIRCASE:** Traversable warp.
- **COUNTER:** Impassable. Allows interaction with Entity on other side.
- **WATER/LAND Interaction:** Moving from Water to Land triggers 'Want to get off?'. Cancel with B to face Land. Moving from Land to Water triggers 'Want to Surf?'. Both prompts override hidden item checks.
- **STATUE:** Interactable. Stand BELOW, face UP, press A.
- **BOOKSHELF:** Impassable Obstacle.
- **HEADBUTT_TREE:** Obstacle. Interacting may trigger wild encounters.
- **WHIRLPOOL:** Water obstacle. Passable with HM06.
- **WATERFALL:** Water obstacle. Passable with HM07.
- **Map Markers:** Use simple emojis (e.g., ⭐) to prevent errors.

### Battle Mechanics
- **Switch Prompt:** Defaults to YES. Press B to decline safely.
- **Accuracy Debuffs:** Effective vs strong opponents (e.g. Smokescreen).
- **Type Effectiveness:** Fire is 0.5x effective against Water/Ground (not 0.25x).
- **Weather:** Rain Dance reduces Fire-type damage by 50%.
- **Gen 2 Mechanics:** Dark is Special (e.g. Bite). Ghost is Physical.

## Strategy Notes
- **Surfing:** Pathfinding must strictly separate Land/Water.
- **Team:** Paprika (Lead). Basalt (HM Slave/Fodder).

## Johto History
- **Cleared:** National Park, Cianwood, Mahogany, Goldenrod, Rocket Base, Ice Path, Blackthorn.
- **Key Items:** HM06 (Whirlpool), Rising Badge, Dratini.
- **Tin Tower:** Paused. Need Rainbow Wing (Catch Raikou, Entei, Suicune).

## Lessons Learned
- **Fly Strategy:** The Fly map cursor is unreliable (sticks/drops inputs). Always visually verify destination. **Rule:** If Fly fails twice, abandon and walk/ride if the destination is nearby.
- **Fly Mechanics:** Fly destinations are only unlocked by entering the city's Pokémon Center. Visiting the city map is not enough (missed Pallet, Viridian, Pewter).
- **Item Verification:** Passive upgrades (e.g., Radio Card) often don't appear in the inventory; trust NPC dialogue.
- **Tool Usage:** `find_path` outputs a coordinate list for `path_plan`. Do NOT use `autopress_buttons: true` with it.
- **Menu Navigation:** Blind menu macros are unreliable due to wrapping and cursor memory. Use `force_press_button` with visual verification or manual inputs.

## Lavender Town
- **Soul House:** Located South-Central. Memorial site.
- **Radio Tower:** Located North.
- **Name Rater:** Likely the house south of the mart.

## Saffron City (Cleared)
- **Gym:** Sabrina Defeated (Marsh Badge).
- **Copycat:** Doll Returned. Train Pass Obtained.
- **Connection:** Magnet Train operational.
- **Notes:** Fisher (PC) confirmed Cerulean Cave collapse.

## Active Custom Tools
- **find_path:** A* Pathfinding (Outputs coordinates).
- **select_move:** Battle move selection.
- **force_press_button:** Input automation.
- **smart_scroll:** Menu item/move selector.
- **press_sequence:** Button sequence executor.

## Active Custom Agents
(None)

## Battle Tower Challenge (Level 20)
**Goal:** Defeat opponents in the L:20 Class.

### Current Team
1. **Vortex (Pidgeotto) Lv19:** Flying/Normal. Lead.
2. **Bahamut (Dratini) Lv16:** Dragon. Pivot (Resists Water/Electric/Grass/Fire). Thunder Wave support.
3. **Bedrock (Larvitar) Lv20:** Rock/Ground. Sweeper.

**Strategy:** Bahamut covers the team's Water/Electric weakness. Use Thunder Wave to cripple faster threats.
**Status:** Ready for Battle Tower Level 20.

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
- **Summary:** Explored. East side is a dead end. West side access confirmed tricky.
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
- **Start Menu Order:** Pokedex, Pokemon, Pack, Pokegear (4th), Status, Save, Option, Exit.
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
## Silver Cave & Route 28 (Archived)
- **Status:** Fully Explored. Red Defeated.
- **Route 28:** Secret House (TM47 Steel Wing) accessed via Cut path from Silver Cave Outside.
- **Silver Cave:**
  - **Outside:** PokeCenter (23,19).
  - **Room 1:** East path (x=15) leads North.
### Menu Navigation
- **Wrapping:** Menus wrap around! Pressing 'Up' at the top moves to the bottom. Do not blindly mash 'Up' to reset cursor position.
- **Tool Usage Correction:** Must set `buttons_to_press` to `["tool"]` when using `press_sequence` or any tool that presses buttons. Putting manual buttons in `buttons_to_press` overrides the tool.
- **Strategy Update:** Fly failed. Proceeding on foot via Victory Road.
### Mechanic Correction
- **Capture Sequence:** In this version, the Nickname prompt appears **BEFORE** the 'Sent to Bill's PC' message, even if the party is full. Do not assume auto-transfer skips the nickname.
- Capture Mechanic: Nickname prompt occurs BEFORE transfer to PC, regardless of party size.
## Route 28 Secret Area
- **Access:** Via secret path from Silver Cave Outside (cut tree at 31, 24).
- **Steel Wing House (19_4):** Located at (7, 3) in the secret area.
  - **NPC:** Cooltrainer F (Celebrity?). Gave TM47 (Steel Wing). Asked for secrecy.
  - **Object:** Fearow (uses Moltres sprite).
- **Exploration Update:** The landing at (13, 24) leads to an isolated plateau (x=4-10, y=24-29). It is a DEAD END blocked by walls West and a Ridge (FLOOR_UP_WALL) South. Must surf South to bypass the ridge.
- **Silver Cave Outside (Western Shore):**
  - **Central Plateau (x=5-13, y=24-29):** DEAD END. Must jump ledge at (11, 24) to exit.
  - **South Pocket (x=4-15, y=29-30):** DEAD END. Blocked by Ridge South (4, 30) and Wall West (3, 29).
  - **Conclusion:** This entire western landmass seems to be an exit-only loop from Route 28, not an entrance.
- **Silver Cave Outside (South-East):** Path south of ridge (28, 32) is a DEAD END for westward progress. Returning to surf west.
- **Navigation Correction:** The 'Western Landing' at (13, 24) is a one-way exit from the western plateau. It does not provide access TO the area. Access must be found elsewhere, likely north of the Main Cave Entrance.
- **Main Entrance (18, 11 outside -> 9, 33 inside):** DEAD END. Leads to a small foyer. Northern path blocked by one-way ledges at Row 20. Western item (5, 30) blocked by ledge at (7, 30). Must find alternate entrance.
- **Silver Cave Room 1 (Main Entrance):** Confirmed DEAD END. Entrance at (18, 11) leads to a small southern foyer (3_74). Northern path blocked by one-way ledges at Row 20. Western item blocked by ledge. Must find alternate entrance.
- **Route 28 Loop:** The map has a High Ground (North, House) and Low Ground (South, Row 13). It's a one-way loop: Enter via Secret Path -> House -> Jump Ledges -> Lower Area -> Exit via (0, 13) -> Back to Silver Cave Outside (SE).
- **Route 28 High Plateau:** Confirmed that the southern ridge (x=30, 31) is impassable. Cannot jump down to the eastern secluded area from here.
- Western Corridor (14, 11): Visually confirmed blocked by wall at x=15. No external access. Must be accessed from inside.
## Silver Cave Room 2
- **Entrance:** (17, 31). Connects to Room 1 (15, 1).
- **Geography:** Southern area has multiple rows of WARP_CARPET_DOWN tiles. Walls at Row 27 with gaps at x=19 and x=22.
## Silver Cave Room 3
- **Entrance:** (9, 33). Connects to Room 2 (11, 5).
- **Geography:** Large open area. Path leads North.
- **Silver Cave Room 2:** Cleared. Navigated eastern path to obtain Ultra Ball. Exited via North warp.
- **Silver Cave Room 3:** Reached the summit. Red located at (9, 10).
- **Menu Reliability:** Menus have persistent cursor memory and wrapping. Always visually verify cursor position or use 'force_press_button' with delays. Do not rely on blind input sequences.

# Post-Game Exploration
**Status:** Red Defeated. Credits rolled. Resuming at Mt. Silver.
**Current Objective:** Battle Tower Challenge (Level 20).
**Strategy:** Enter Battle Tower.
**Quest Log:**
- **GS Ball:** CANCELLED (Unobtainable).
- **Route 36:** Sudowoodo event complete. Path to Ecruteak City is CLEAR. Fruit Tree at (21, 4) contains ICE BERRY.
- **Moomoo Farm:** Quest Complete! Miltank cured. Reward: TM13 (Snore). Farmer now sells Moomoo Milk.
- **Fly Map:** Cursor behavior is quirky; verify location before flying.

## Route 39 & 40 (Olivine Area)
- **Route 39:** Psychic Norman (13, 7) Defeated. Moomoo Farm visited.
- **Route 40:** Battle Tower Entrance at (9, 5).
- **Battle Tower Menu:** The 'What level do you want to challenge?' text box is NOT blocking. Do NOT press 'A' to advance it, or you will accidentally select the first option (L:10). Wait for the menu to load, then scroll.
- **Battle Tower Menu:** Navigating the level selection is tricky. It seems 'Down' from the start might select 'CANCEL'. Need to verify if L:20 is available or unlocked.
- **Battle Tower Entry:** Select 'Challenge' -> Advance 'Before entering' -> Advance 'Already save file' -> Confirm 'Overwrite' -> Wait for Save (~6s) -> Level Selection Menu.
- **Menu Issue:** Default is 'L:10'. My party (Lv15+) is rejected. 'Down' press might be selecting 'CANCEL' instead of 'L:20'. Investigating menu layout.
- **Menu Verification:** Confirming save to observe the Level Selection menu. Suspect 'L:20' might be missing or in a different slot.
- **Observation:** The Level Selection menu ('What level...') appears after saving, but is immediately canceled by an automated 'B' press. Must act quickly to interact with it.
- **Hypothesis:** The harness is auto-pressing 'B' to clear the 'What level...' text box, inadvertently canceling the menu. 
- **Strategy:** Using a rapid `press_sequence` (Down, A, sleep 200, Down, A) to select Level 20 before the harness can intervene.
- **Investigation:** 'Down' from the level list seems to select 'CANCEL'. Performing a slow scroll observation to map the available level options.

# Battle Tower Lessons (Archived)
- **Summary:** Early attempts failed due to type disadvantages (Water vs Ground/Rock) and level gaps.
- **Key Learnings:**
  - Need balanced coverage; Rock/Ground heavy is risky.
  - Dark is Special in Gen 2.
  - Team needs to be closer to Level 20 cap.
### PC Box 1 Inventory
- M (Caterpie) Lv15
- WEAVER (Spinarak) Lv14
- CHRONO (Hoothoot) Lv16
- GIB RALTAR (Graveler) Lv37
- SHUCKIE (Shuckle) Lv15
- XQH (Sandshrew) Lv12
- F (Psyduck) Lv??
- Paprika (Typhlosion) Lv75
- SIGIL (Unown)
- CIPE (Unown)
- RUNE (Unown)

# Active Training Plan (Completed)
- Team reached target levels. Bedrock (Lv20), Vortex (Lv19), Bahamut (Lv17).
- Ready for Battle Tower.
### Ruins of Alph
- **Kabuto Puzzle:** Solved! Unlocked Inner Chamber (3_27).
- **Kabuto Chamber Secret:** Solved! Escape Rope opened secret passage to Item Room. 
- **Inner Chamber:** "Strange presence" text appeared upon entry (likely Unown).
- **Tool Lesson:** `find_path` tool outputs a list of coordinates, NOT button strings. Do NOT use `autopress_buttons=True` with it; use `path_plan` instead.
- Entered Ruins of Alph Research Center.
### Tile Mechanics Updates
- **BOOKSHELF:** Impassable Obstacle.
- **Interaction Rule:** Computers and wall-mounted objects usually require standing on the tile BELOW them and facing UP.

### Observations
- Research Center Computer: Displays 'RUINS OF ALPH Exploration Year 10'.
## Ecruteak City
- Arrived via Fly.
- Heading West to Route 38 -> Route 39 (Moomoo Farm) for training and delivery.
- **Training Spot:** Route 39 Tall Grass (5, 20). Good for Magnemites/Meowths.
- **Tile Mechanic:** TALL_GRASS is traversable but triggers encounters, interrupting movement tools.

## Route 39 Training Plan
- **Strategy:** Switch-Training. Lead Bahamut (Dratini), switch to Basalt (Geodude) turn 1.
- **Targets:** Magnemite (Use Magnitude), Meowth, Raticate.
- **Avoid:** Miltank, Tauros (High damage risk).
- **Notes:** Vortex is injured, keep safe. Basalt is immune to Electric.
- Picked up MINT BERRY from Route 39 tree. (Likely not the cure for Miltank).
- **Navigation Insight:** Wild encounters interrupt `find_path`/`path_plan` execution. When actively hunting in tall grass, use `press_sequence` (e.g., 'Up, Down, Up, Down') instead of target coordinates to avoid 'Movement Blocked' errors.
- **Quest Status:** Miltank is still sick. Needs standard BERRY. Route 38 tree was empty. Exploring Violet City area.
- **Lesson:** Always set `autopress_buttons: true` when calling custom tools that return button sequences.
- **Quest Status Update:** Miltank is still sick. The Route 38 tree contained a Bitter Berry (not the cure). Now heading to Route 30 to check the Berry tree there.
- **TM08 (Rock Smash):** Obtained from Fisher on Route 36 (44, 9). Allows breaking cracked rocks.
- **WARP_CARPET_LEFT:** Walk Left off the map to exit.
- **Interaction Lesson:** Reading a sign opens a text box that MUST be manually closed (B/A) before movement inputs will register. Always verify screen text state after interaction.
- **Scientist 1:** Surprised by Pokémon in ruins.
- **Scientist 2:** Theorizes Unown are the drawings on the walls come to life, implying many variations exist.
- Research Center Printer: Currently displays 'This doesn't seem to work yet.' Likely requires more Unown progress.
- **Ruins of Alph:** Printer inactive with current Unown (5 types). Scientists dialogue generic. Need to catch more varieties.
- **Ruins of Alph:** Scientist confirmed 'many kinds' of Unown exist. Implies catching different letter variants is key.
- **Stealth Strategy:** Use `stun_npc` to freeze patrolling Scientists to avoid pathfinding blocks.
- **Ruins Mystery:** Unown Dex Unlocked. Printer locked.
- **Unown Collection:** 3 Caught (SIGIL, CIPE, RUNE). Discovered discrepancy: 'L' and 'A' are missing. Need to catch more varieties.
- **Hypothesis:** Must speak to Scientist to update progress, or need more than 5.
- **Unown Mode:** Unlocked (likely with 3 forms). Records forms in catch order.
- **Tool Usage Lesson:** Custom tools that return button sequences (like `press_sequence`) MUST be called with `autopress_buttons: true` to actually execute the presses. System tools do not require this.
- **Encounter:** Wild Unown (Form 'L'?). Attempting capture.
- Scientist 3 (Left): "The UNOWN you catch will all be recorded. Check to see how many kinds exist."
- Scientist 3 (Left): "I wonder how many kinds of POKéMON are in the RUINS?"
- Kabuto Item Room: Found Heal Powder at (2, 4).
- **Battle Tower Gatehouse:** Rocker mentions special gifts for win streaks.
- **Phone Call:** Joey (Route 30) called. Flavor text about Rattata and Hoothoot.
- **Moomoo Farm:** Pokefan F says Miltank won't give milk. This confirms the quest.
- **Route 29 Navigation:** Northern path accessible via Cut (Tree at 30, 9 removed). Proceeding to forage on Route 46.
- **Route 29 Navigation (Eastbound):** Direct path blocked by ledges at x=8 and x=28. Must use the Southern Path (Row 14) to bypass the x=28 barrier, then loop North through the gap at (31, 13) to reach the Cut Tree/Gatehouse.
- **Route 29 Navigation Update:** Cut Tree at (30, 9) removed. Northern path is now accessible from the West.
## Route 46
- **Status:** Explored Southern Basin.
- **Navigation:** One-way Southbound only. Northern section (Berry Tree) is inaccessible from the South. Must access via Dark Cave (Route 31 entrance).
- **Sign:** "MOUNTAIN RD. AHEAD" at (9, 27).
- **Route 30:** Harvested PSNCUREBERRY at (11, 5). Tree is now empty. Heading to Dark Cave via Route 31.
## Dark Cave (Violet Entrance)
- **Status:** Just entered from Route 31.
- **Geography:**
  - Entrance: (3, 15).
  - East Path: Blocked by Rock Obstacle (ID 4) at (7, 14).
  - South Path: Blocked by Ridge (FLOOR_UP_WALL) at (2, 16). Hypothesis: Traversable from North (Down).
- **Goal:** Reach Route 46 (North) via the western path.
- **Dark Cave (Violet Entrance):** The path South from the entrance is blocked by a one-way ridge (FLOOR_UP_WALL) at (2, 16). Cannot reach the western side without Surf or Rock Smash. Returning to Violet City to get HM users.
- **Violet PC:** Deposited Bedrock/Shuckie. Withdrew Gib Raltar. Plan: Withdraw F (Surf) and Chrono (Flash).
- **Route 37 Anomaly:** Twins Ann & Anne are labeled as 'WEIRD_TREE' in the game state object list. Dialogue confirms they are trainers.
### Route 37
- **Fruit Trees:**
  - (13, 5): Red Apricorn (Looted).
  - (15, 7): Black Apricorn (Pack Full, Left Behind).
  - (16, 5): Checking...
- **HEADBUTT_TREE:** Obstacle. Interacting may trigger wild encounters.
- **WHIRLPOOL:** Water obstacle. Passable with HM06.
- **WATERFALL:** Water obstacle. Passable with HM07.
- **WEIRD_TREE Anomaly:** Twins Ann & Anne on Route 37 are labeled as WEIRD_TREE in game state.
- **Lesson:** Always check inventory space before foraging.
### Route 37 Findings
- **Anomaly:** Twins Ann & Anne are labeled as `WEIRD_TREE` in the game state object list.
- **Lesson:** Always check inventory space before foraging. A full pack prevents looting fruit trees.
- **Resources:**
  - Red Apricorn: (13, 5)
  - Black Apricorn: (15, 7)
  - Blue Apricorn: (16, 5)
### Recent Lessons & Anomalies
- **Anomaly:** Twins Ann & Anne on Route 37 are labeled as 'WEIRD_TREE' in the game state object list.
- **Lesson:** Inventory limit is strict (20 slots). Stacks count as 1 slot. Always check space before foraging.
- **Progress:** Deposited Nugget, Rare Candy, Protein (x2).