# Gem's Pokémon Crystal Journey

## 🌍 Global Status & Goals
- **Primary Goal:** Win 7 battles in a row at the Battle Tower (Level 20).
- **Current Task:** Challenge Battle Tower Level 20.
- **Status:** Battle Tower Level 20. Round 1. Party: Rumpus, Bahamut, Vortex.
- **Location:** Battle Tower Lobby.

## 🏆 Battle Tower Challenge (Level 20)
- **Status:** Preparation Phase (Rumpus).
- **Strategy:**
  1. **Train Rumpus:** Get Tauros to Lv20. (Strength Taught). **CRITICAL:** STOP EXACTLY AT LV20. Exceeding Lv20 (even by 1) DISQUALIFIES him.
  2. **Team:** Rumpus (Lead/Sweeper), Bahamut (Priority/Paralysis), Vortex (Ground Immunity/Fly). [Verified: Flux Deposited, Bahamut Withdrawn]

### Known Threats & Counter-Strategies
- **Blissey:** High HP, **Counter**. 
  - **RULE:** DO NOT use Physical/Normal moves (Sonicboom, Strength, Fly, Extremespeed) or you will die. 
  - **Strategy:** Use Special moves (Thundershock, Dragonbreath, Mud-Slap) or Toxic.
- **Alakazam:** Fast, Elemental Punches. Low Def.
  - **Strategy:** Survive a hit and OHKO with Physical moves (Strength, Fly).
- **Aerodactyl:** Fast, Earthquake. 
  - **Strategy:** Switch to Vortex immediately (Immune to Ground).
- **Azumarill:** Tanky, Blizzard/Surf.
  - **Strategy:** Use Electric moves. Beware Blizzard on Dragons/Birds.
- **Starmie:** Fast, Surf/Psychic.
  - **Strategy:** Thunder Wave is priority.
- **Umbreon:** Toxic/Protect stall.
  - **Strategy:** Toxic it back with Flux, or brute force.
- **Miltank:** Earthquake user.
  - **Strategy:** Vortex (Immune) or kill fast.

### Non-Combatant NPCs (Don't check again)
- **Battle Tower Outside:** Youngster (6, 12), Beauty (12, 10), Sailor (12, 18).
- **Route 40:** Lass (13, 4).

## 📝 Quest & Event Log

- **Ruins of Alph:** Unown Mode unlocked. 9 Forms caught. "Strange presence" in Inner Chamber. Scientists researching.
- **Kanto Campaign:** 8 Badges obtained. Red defeated.
- **Copycat (Saffron):** Pass obtained. Magnet Train active.

### Current Logs
- **Location:** Battle Tower Lobby.
- **Status:** Ready to challenge Level 20.
- **Last Loss:** Scientist Thurman (Exeggutor).
  - **Lesson:** Exeggutor outspeeds team. Flux (Steel) is the hard counter. Switch immediately.

## Global Game Mechanics
### General Mechanics
- **Physics:** Boulders cannot push other boulders. You must occupy the tile 'behind' a boulder to push it.
- **'Scoot' Mechanic:** Leaving and re-entering a map refreshes map state (e.g., moving NPCs).
- **Warp Verification:** Game State 'Warps' list is the source of truth.
- **Key Items:** Passive upgrades (e.g., Radio Card) may not list in inventory.

### Pokegear & Radio Systems
- **Menu Layout:** Horizontal ROW [BACK | MAP | PHONE | RADIO]. Navigation wraps/clamps. 'B' exits to Overworld. 
- **Navigation:** Blind inputs unreliable. Reliable path to Radio: Reset to BACK (Left x3), then RADIO (Right x3). Use `press_sequence`.
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
- **Team:** Bahamut (Lead/Train), Vortex (Flying), Gauss (Electric/Steel), Lucre (Pickup/Train).

## Johto History
- **Cleared:** National Park, Cianwood, Mahogany, Goldenrod, Rocket Base, Ice Path, Blackthorn.
- **Key Items:** HM06 (Whirlpool), Rising Badge, Dratini.
- **Tin Tower:** Paused. Need Rainbow Wing (Catch Raikou, Entei, Suicune).

## Lessons Learned
- **Fly Strategy:** The Fly map cursor is unreliable (sticks/drops inputs). Always visually verify destination. **Rule:** If Fly fails twice, abandon and walk/ride if the destination is nearby.
- **Fly Mechanics:** Fly destinations are only unlocked by entering the city's Pokémon Center. Visiting the city map is not enough (missed Pallet, Viridian, Pewter).
- **Item Verification:** Passive upgrades (e.g., Radio Card) often don't appear in the inventory; trust NPC dialogue.
- **Tool Usage:** The pathfinding tool is `find_path`. It outputs a coordinate list for `path_plan`. Do NOT use `autopress_buttons: true` with it.
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
## Route 19
- **Summary:** Explored. East side is a dead end. West side access confirmed tricky.
## Route 15
- **Structure:** Split into Upper (North) and Lower (South) paths.
- **Upper Path:** Westbound only (Ledges jump Left).
- **Lower Path:** Eastbound (Traversable).
- **Item:** Ball at (12, 5) on Upper Path (currently unreachable).
- Defeated Teacher Colette (Clefairy Lv36).
- Route 15 Wild Encounters: Nidorina, Pidgeotto.

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

### Menu Navigation
- **Start Menu Order:** Pokedex, Pokemon, Pack, Pokegear (4th), Status, Save, Option, Exit.
- **Cursor Memory:** The game remembers the last cursor position. Always visually confirm or reset cursor (e.g., press Up x5) before navigating blind.

- Fly Map Navigation: From Indigo Plateau, 'Down' jumps directly to Cinnabar Island. 'Right' does nothing. This confirms intermediate towns (Pewter, Viridian, Pallet) are skipped if not visited properly.
## Victory Road Gate
- **Status:** Exploring.
- **Geography:**
  - East Exit: Route 22.
  - West Exit: Likely Route 28 (Mt. Silver).
  - North Exit: Likely Victory Road.
  - South Exit: Route 26.
- **Observations:** Black Belt guard at (12, 5) is gone (likely due to 16 badges). Path West appears open.

## Route 28
- **Mechanic Discovery:** WARP_CARPET_DOWN tiles may require walking 'Down' into a visual wall to trigger, rather than just walking onto them.
- **Status:** Exploring West. Confirmed 'ROUTE 28' via sign at (31, 5).

### Menu Navigation
- **Wrapping:** Menus wrap around! Pressing 'Up' at the top moves to the bottom. Do not blindly mash 'Up' to reset cursor position.
- **Tool Usage Correction:** Must set `buttons_to_press` to `["tool"]` when using `press_sequence` or any tool that presses buttons. Putting manual buttons in `buttons_to_press` overrides the tool.
- **Strategy Update:** Fly failed. Proceeding on foot via Victory Road.
### Mechanic Correction
- **Capture Sequence:** In this version, the Nickname prompt appears **BEFORE** the 'Sent to Bill's PC' message, even if the party is full. Do not assume auto-transfer skips the nickname.
- Capture Mechanic: Nickname prompt occurs BEFORE transfer to PC, regardless of party size.

# Post-Game Exploration
**Status:** Red Defeated. Credits rolled. Resuming at Mt. Silver.
**Current Objective:** Battle Tower Challenge (Level 20).
**Strategy:** Enter Battle Tower.
**Quest Log:**
- **GS Ball:** CANCELLED (Unobtainable).
- **Route 36:** Sudowoodo event complete. Path to Ecruteak City is CLEAR. Fruit Tree at (21, 4) contains ICE BERRY.
 Reward: TM13 (Snore). Farmer now sells Moomoo Milk.
- **Fly Map:** Cursor behavior is quirky; verify location before flying.

## Route 39 & 40 (Olivine Area)
- **Route 39:** Psychic Norman (13, 7) Defeated. Moomoo Farm visited.
- **Wild Intel:** Magnemites here can FLEE (approx 10% chance). Catch quickly. Moves: Supersonic, Sonicboom.
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

# Battle Tower Intel
- **General Strategy:** Lead Rumpus (Strength/Sweeper). Bahamut (Priority/TWave). Vortex (Ground Immunity/Fly).
- **Known Threats:**
  - **Aerodactyl:** Earthquake, Hyper Beam. (Switch to Vortex).
  - **Starmie:** Surf, Psychic. Fast. (Paralyze with Bahamut).
  - **Azumarill:** Blizzard, Surf. (Counters Dragons).
  - **Alakazam:** Psychic, Elemental Punches. (Hit hard with Strength/Extremespeed).

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

- Picked up MINT BERRY from Route 39 tree.
- **Navigation Insight:** Wild encounters interrupt `find_path` execution. When actively hunting in tall grass, use `press_sequence` (e.g., 'Up, Down, Up, Down') instead of target coordinates to avoid 'Movement Blocked' errors.

- **Lesson:** Always set `autopress_buttons: true` when calling custom tools that return button sequences.
- **Battle Tower Menu:** Level Selection uses 'Up'/'Down' to toggle levels (e.g., 10 -> 20). Press 'A' to confirm.
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
- **Unown Collection:** 9 Caught (ALPHA, LEXICON, GLYPH, DORMA, ICON, ARCANE, SIGIL, CIPE, RUNE). Progress updated from PC Box.
- **Hypothesis:** Must speak to Scientist to update progress, or need more than 5.
- **Unown Mode:** Unlocked (likely with 3 forms). Records forms in catch order.
- **Tool Usage Lesson:** Custom tools that return button sequences (like `press_sequence`) MUST be called with `autopress_buttons: true` to actually execute the presses. System tools do not require this.
- **Encounter:** Wild Unown (Form 'L'?). Attempting capture.
- Scientist 3 (Left): "The UNOWN you catch will all be recorded. Check to see how many kinds exist."
- Scientist 3 (Left): "I wonder how many kinds of POKéMON are in the RUINS?"
- Kabuto Item Room: Found Heal Powder at (2, 4).
- **Battle Tower Gatehouse:** Rocker mentions special gifts for win streaks.
- **Phone Call:** Joey (Route 30) called. Flavor text about Rattata and Hoothoot.

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
- **Lesson:** Inventory limit is strict (20 slots). Stacks count as 1 slot. Always check space before foraging. A full pack prevents looting fruit trees.
- **Resources:**
  - Red Apricorn: (13, 5)
  - Black Apricorn: (15, 7)
  - Blue Apricorn: (16, 5)
### Recent Lessons & Anomalies
- **Anomaly:** Twins Ann & Anne on Route 37 are labeled as 'WEIRD_TREE' in the game state object list.
- **Lesson:** Inventory limit is strict (20 slots). Stacks count as 1 slot. Always check space before foraging.
- **Progress:** Deposited Nugget, Rare Candy, Protein (x2).
- **PC/Party Management:** Always verify the 'Party' list in Game State Information before attempting to withdraw Pokémon. Misremembering party state leads to wasted turns.
- **Item Discovery:** Bahamut (Dratini) came holding a **Dragon Fang**.
- **Battle Tower Mechanics:** Auto-heals party after a challenge (win or loss).
- **Encounter:** Wild Magnemite on Route 39! Switching to Bahamut to catch.
- **Route 39:** Retreated to Olivine City to heal Gauss (7/38 HP).
## New Discoveries
- **Route 39:** Meowth (Wild), Raticate (Wild).
- **Lucre (Meowth):** Lv16. Scratch, Growl, Bite.
- **Event:** Dunsparce Swarm reported in Dark Cave (Violet Entrance) by Anthony.
- **Tool Rule:** `autopress_buttons: true` is ONLY for Custom Tools (e.g., `select_move`). System tools (e.g., `select_battle_option`) fail/ignore if this is set.
- Status: Rumpus healed. Moving to Route 39 to grind XP.
- **Note:** Umbreon holds Leftovers.
- **Battle Update:** Vortex Badly Poisoned by Umbreon. Switching to Bahamut to reset Toxic counter and attempt Thunder Wave.
- **Battle Update:** Umbreon used Attract (Failed). Bahamut paralyzed Umbreon with Thunder Wave. Umbreon moves known: Toxic, Protect, Attract.
- **Battle Update:** Bahamut used Extremespeed (Crit). Umbreon used Toxic (Bahamut Badly Poisoned). Umbreon recovered with Leftovers.
- **NPC Blockades:** Erratic NPCs in narrow paths can disrupt navigation. Use `stun_npc` to freeze them, then recalculate the path to go around.
- **Route 39:** Pokefan F at (4, 22) is a Night-only battler.
## Route 39 Observations
- **Threats:** Magnemite (Sonicboom/Steel). Avoid with Rumpus.
- **Trainers:** Pokefan F (4, 22) is Night-only.
- **Log:** Bought 10 Super Potions in Olivine Mart.
- **Lesson:** Blind menu macros (press_sequence) are FAILING for Party Switching. I must use MANUAL, step-by-step button presses with visual verification for this task to avoid loops.
- **Lesson:** Menus often remember cursor position. Always use 'Up' multiple times to reset the cursor to the top before navigating lists.
## 🛡️ Battle Tower Threat Analysis (Consolidated)
- **Blissey:** High HP, **Counter**. NEVER use Physical/Normal moves (Sonicboom, Strength, Fly). Use Special (Thundershock, Dragonbreath).
- **Alakazam:** Fast, Elemental Punches. Weak Def. Counter: Physical moves (Strength, Fly).
- **Aerodactyl:** Fast, Earthquake. Counter: Vortex (Immune).
- **Starmie:** Fast, Surf/Psychic. Counter: Bahamut (TWave).
- **Umbreon:** Toxic/Protect Stall. Counter: Toxic back.
- **Heracross:** Megahorn (Huge Dmg). Counter: Vortex (Fly).
- **Hitmonchan:** Elemental Punches. Counter: Vortex (Fly).
- **Lapras:** Blizzard, Quick Claw.
- **Non-Combatants:** Youngster (6,12), Beauty (12,10), Sailor (12,18), Lass (13,4).
- **Tool Note:** `hunt_routine` is now context-aware and avoids walls automatically.
- Phone Call: Anthony (Route 33) mentions seeing many Geodude (Possible Swarm?).
### Route 39 Grinding Plan
- **Target:** Train Rumpus (Tauros) to Level 20 EXACTLY.
- **XP Sources:**
  - Tauros (~180-200 XP)
  - Miltank (~200 XP)
  - Pidgeotto (~100 XP)
  - Magnemite (Avoid/Run - Sonicboom danger/Steel resist)
- **Strategy:** Use `hunt_routine` in tall grass. Heal at Olivine Center if HP < 30.
- **Battle State Awareness:** Failed to notice battle text 'Rumpus used STRENGTH!' was still active before attempting `hunt_routine`. MUST verify Screen Text indicates 'FIGHT/PKMN/PACK/RUN' or 'Wild X appeared' before assuming control.

### Battle Tower Attempt 1 Analysis
- **Result:** Loss vs Picnicker Diaz (Round 1).
- **Opponent Team:** Nidoking (Earthquake, Blizzard), Quagsire (Earthquake).
- **Fatal Flaws:**
  - Flux (Magnemite) is 4x weak to Ground (Earthquake). Died instantly.
  - Vortex (Pidgeotto) died to surprise Blizzard coverage from Nidoking.
  - Rumpus (Tauros) lacked coverage to finish quickly.
- **Adjustment:** Swap Flux -> Bahamut (Dratini). Bahamut brings Extremespeed (Priority) and better neutral bulk, though still weak to Ice. Flux's Ground weakness is too exploitable here.