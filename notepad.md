# Gem's Pokémon Crystal Journey

## 🌍 Global Status & Goals
- **Primary Goal:** Win 7 battles in a row at the Battle Tower (Level 20).
- **Current Task:** Battle Tower Challenge (Level 20).
- **Status:** Attempt 69 - Prep (Equip Items).
- **Team:** Rumpus, Flux, Bahamut.
- **Location:** Battle Tower Lobby.

## 🏰 Battle Tower Master Guide (Level 20)
### 📋 Status
- **Status:** Attempt 70 - Prep (Equipping Items).
- **Action:** Equip: PrzCure(Rumpus), Mint(Flux), DragonFang(Bahamut).
- **Reason:** Re-equipping for Battle Tower.

### ⚔️ Consolidated Mechanics
- **Items:** Items persist between runs unless consumed. ALWAYS CHECK.
- **Healing:** Auto-heal after run.
- **Level:** Manual Select L:20.
- **Speed:** Opponents have Max DVs. Assume slower unless +25 Base Speed.
- **Counter:** Reflects Physical. Use Special vs Blissey/Wobbuffet.

### ⚠️ Threat Intel
- **Schoolboy Walker:** Nidoking (EQ/Blizzard), Aerodactyl (EQ?).
- **Swimmer Dykstra:** Steelix (EQ/Swagger), Pikachu (T-Bolt), Gyarados (Hyper Beam).
- **General Threats:**
  - **Miltank:** EQ, Attract. Counter: Vortex.
  - **Starmie:** Surf, Psychic. Counter: Flux.
  - **Blissey:** Counter, Psychic. Counter: Flux (Toxic).
  - **Nidoking:** EQ, Blizzard. Counter: Rumpus (Strength).
  - **Gyarados:** Hyper Beam. Counter: Rumpus.
  - **Lapras:** Blizzard. Counter: Flux.

## 📝 Quest & Event Log
- **Status:** Post-Game (Red Defeated).
- **Ruins of Alph:** 9 Unown Forms. Inner Chamber Unlocked.

## Global Game Mechanics
### General Mechanics
- **Physics:** Boulders cannot push other boulders. You must occupy the tile 'behind' a boulder to push it.
- **'Scoot' Mechanic:** Leaving and re-entering a map refreshes map state (e.g., moving NPCs).
- **Warp Verification:** Game State 'Warps' list is the source of truth.
- **Key Items:** Passive upgrades (e.g., Radio Card) may not list in inventory.

## System & Tool Documentation

### Tool Usage
- **Movement:** Use the `find_path` tool to calculate a path. Manually copy the returned coordinates into the `path_plan` output field. Set `buttons_to_press` to `["path"]` to execute. NEVER mix with tool calls.
- **Auto-Press:** Custom tools returning buttons (e.g. `select_move`) need `autopress_buttons: true`. System tools (e.g. `select_battle_option`) ignore this.
- **Blind Inputs:** Blind menu macros (`press_sequence`) are unreliable due to wrapping and cursor memory. Use manual verification.
- **Specific Tools:**
  - `hunt_routine`: Context-aware; avoids walls.
  - `find_path`: Outputs coordinates; do not use `autopress_buttons`.
  - `select_move`: Automates move selection. Requires `autopress_buttons: true`.
  - `select_battle_option`: Automates main menu selection (FIGHT/PKMN/PACK/RUN).
  - `press_sequence`: Executes button macros. Requires `autopress_buttons: true`.
  - `select_item`: Scans screen for item and navigates to it. Requires `autopress_buttons: true`.
  - `battle_advisor`: Agent for Battle Tower strategy (Team: Rumpus/Bahamut/Flux).

### Menu & UI Mechanics
- **Start Menu Order:** Pokedex, Pokemon, Pack, Pokegear (4th), Status, Save, Option, Exit.
- **Wrapping:** Menus wrap around (Up at top -> Bottom).
- **Cursor Memory:** The game remembers the last cursor position. **WARNING:** The Start Menu WRAPS. Do NOT blindly mash 'Up'. Visually confirm cursor position.
- **UI Mixed State:** Pokegear menu header can persist over text boxes. Press 'B' aggressively to clear.
- **Pokegear Navigation:** Horizontal ROW [BACK | MAP | PHONE | RADIO]. Navigation wraps/clamps. Reliable path to Radio: Reset to BACK (Left x3), then RADIO (Right x3).
- **Radio Tuning:** 'A' toggles Manual/Preset. 'Up/Down' cycles presets. 'Right' moves needle manually. Tune to 20.0 for Poké Flute. Phone calls reset frequency.

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
- **FLOOR_UP_WALL:** Context Dependent. Ridge. Usually impassable from South/Sides, traversable from North.
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
- **Gen 2 Physical Types:** Normal, Fighting, Flying, Ground, Rock, Bug, Ghost, Poison, Steel. (Triggers Counter).
- **Gen 2 Special Types:** Water, Grass, Fire, Ice, Electric, Psychic, Dragon, Dark. (Triggers Mirror Coat).
- **Counter Strategy:** Reflects Physical damage (2x). Use Low Power Physical moves or Special moves to minimize recoil.

## Strategy Notes
- **Surfing:** Pathfinding must strictly separate Land/Water.
- **Team:** Rumpus (Lead - Tauros), Vortex (Pivot - Pidgeotto), Bahamut (Special - Dratini).

## Johto History
- **Cleared:** National Park, Cianwood, Mahogany, Goldenrod, Rocket Base, Ice Path, Blackthorn.
- **Key Items:** HM06 (Whirlpool), Rising Badge, Dratini.
- **Tin Tower:** Paused. Need Rainbow Wing (Catch Raikou, Entei, Suicune).

## Lessons Learned
- **Fly Strategy:** The Fly map cursor is unreliable (sticks/drops inputs). Always visually verify destination. **Rule:** If Fly fails twice, abandon and walk/ride if the destination is nearby.
- **Fly Mechanics:** Fly destinations are only unlocked by entering the city's Pokémon Center. Visiting the city map is not enough (missed Pallet, Viridian, Pewter).
- **Item Verification:** Passive upgrades (e.g., Radio Card) often don't appear in the inventory; trust NPC dialogue.

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

## Johto Atlas
### Olivine Area (Routes 39 & 40)
- **Route 39:** 
  - **Geography:** Moomoo Farm located here.
  - **Trainers:** Psychic Norman (13, 7) [Defeated], Pokefan F (4, 22) [Night-only].
  - **Wild Pokemon:** Magnemite (Caution: Flee chance, Sonicboom), Meowth, Raticate, Miltank, Tauros.
  - **Resources:** Moomoo Milk (Farmer), Fruit Trees.
- **Route 40:** Battle Tower Entrance at (9, 5).

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
- **Resources:**
  - Red Apricorn: (13, 5)
  - Black Apricorn: (15, 7)
  - Blue Apricorn: (16, 5)
### Battle Tower Mechanics
- **Auto-Heal:** Party is fully healed after every challenge (win or loss).
- **Item Persistence:** Items are returned to bag after every run. MUST RE-EQUIP ALL.
- **Rules:** No duplicate held items. Level 20 must be selected manually (Up from L:10).
- **Saving:** Forced save before entry.
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

- **CRITICAL:** Battle Tower Level 20 Miltank has **EARTHQUAKE**. Counters Flux/Magnemite perfectly.
- Battle Update: Vortex fainted to Miltank (Thunder). Miltank moves: Thunder, Earthquake, Attract. Accuracy: -1. Rumpus (Paralyzed, Infatuated) vs Miltank (Critical HP).
- **Mechanic Correction:** ICE BERRY cures BURN, not Freeze. It does NOT reduce Ice damage. Use BURNT BERRY for Freeze (not currently owned).
- **Item Discovery:** Vortex was holding a **METAL COAT** (Boosts Steel moves). Swapped for BERRY for Battle Tower survival.
### Battle Tower Menu Mechanics
- **L:20 Selection:** From default (L:10), press **Up** once to reach L:20.
- **Navigation:** Up increments (10->20), Down decrements/wraps (10->100).

### Inventory Lessons
- **Bag Sorting:** Items in the Gen 2 bag are not always strictly alphabetical. New items are often added to the bottom. Always scroll through the ENTIRE list if an item is missing from the top.
- **Pokemon Menu Priority:** Field moves (e.g., Strength, Fly) appear at the TOP of the individual Pokemon menu, pushing STATS, SWITCH, and ITEM down. Always check for field moves before navigating.
### Battle Lessons
- **Vs Swagger:** If your Pokémon is Confused and Attack boosted (+2), SWITCH OUT to a safe pivot immediately. Do not risk the self-hit, especially against low HP opponents.
- **Battle Note:** Flux's Toxic failed against Umbreon ('It didn't affect'). Potential causes: Substitute, Safeguard, or Accuracy drop causing a 'miss' (though usually says 'missed'). Investigate.
- **Opponent Move:** Umbreon knows Mud-Slap.
- **Battle Log:** Rumpus hit by Mud-Slap (-1 Acc). Umbreon recovering with Leftovers.
- Round 1 (Sage): Wigglytuff used Hyper Beam. Rumpus (22/64 HP). Wigglytuff recharging.
- Round 1 (Sage): Wigglytuff recovered with Gold Berry. Rumpus (22/64 HP).
- Round 1 (Sage): Flux switched in. Tanked Hyper Beam (21/45 HP). Wigglytuff Recharging.
 Flux consumed Berry (31/45 HP). Plan: Toxic.
 Strategy: Sonicboom to chip/stall. Flux sacrifices if needed.
- **Battle Log:** Opponent Azumarill used Rain Dance.
- **Battle Log:** Azumarill used Blizzard (OHKO on Bahamut). Intel: Knows Rain Dance, Blizzard.
- **Battle Log:** Bahamut fainted. Switched to Flux. Rain Dance active.
- **Battle Log:** Flux fainted to Rain-boosted Surf. Rumpus sent in as last resort.

- **Level Select:** Scroll Up for L:20.
- **Battle Log (Attempt 53):** Beauty's Blissey knows Psychic. Did not use Counter Turn 1.
**CRITICAL LESSON - BATTLE TOWER SPEED:**
- Opponents likely have MAX DVs and Stat XP. Assume we are SLOWER than the opponent unless we have a massive base speed advantage. Speed ties are losses.
- Miltank knows Earthquake/Thunder/Attract.
- Blissey knows Psychic/Submission.
- Lapras: Blizzard.
- Lapras: Confuse Ray, Gold Berry.
- Lapras used Blizzard (Heavy damage to Flux).
- Lapras used Confuse Ray. Flux Confused.
- Flux landed Crit Thundershock (SE).
- Lapras used Blizzard (Missed).
- Flux hurt itself in confusion.
- Round 1 (Super Nerd): Lapras missed Blizzard. Flux hurt itself (23/45 HP).
- Round 1 (Super Nerd): Rumpus fainted to Alakazam (Psychic). Alakazam at full HP. Bahamut sent in.
- Round 1 (Juggler Fairfield): Quagsire (Rain Dance, Amnesia, Surf), Starmie (Psychic, likely Surf). Rain stopped. Flux used Berry.
Flux fainted to Psychic (Outsped). Bahamut in vs Full HP Starmie.
### PC Management Lesson
- **Lesson:** 'MOVE PKMN W/O MAIL' is unreliable for simple depositing via blind macros. Use 'DEPOSIT PKMN' instead.
- **Battle Intel:** Level 20 Blissey outspeeds Level 20 Vortex (Pidgeotto). Vortex Speed is 36. Blissey likely max DVs/Stat Exp.
- **Correction:** Vortex was holding a BERRY, not Metal Coat. Healed to 33/61 HP.
- **Status Update (Attempt 60):** Vortex needs Berry. Rumpus has Przcureberry. Metal Coat lost.
- **Tool Reliability:** Deleted `give_held_item` due to fragility with cursor memory. Future menu tools must aggressively reset cursor position (e.g. multiple 'Up' presses) before navigation.
- **Swimmer Dykstra:** Steelix (Earthquake/Swagger/Iron Tail).
- Round 1 (Walker): Nidoking Blizzard hit Vortex through -1 Acc (OHKO). Vortex FNT.