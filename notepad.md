# Gem's Pokémon Crystal Journey

## Current Goals
- [ ] Earn the Mineral Badge (Primary)
- [ ] Retrieve SecretPotion from Cianwood (Secondary)
- [ ] Check Battle Tower & Surf to Cianwood (Immediate)

## Status & Quests
- **Location:** Battle Tower Lobby.
- **Objective:** Travel to Cianwood City via Surf to get medicine for Jasmine's Ampharos.
- **Current Task:** Traveling to Cianwood City.
- **Backlog:**
  - Cure Miltank at Moomoo Farm (Needs more berries).

## Ecruteak City
- **Status:** Visited.
- **Gym:** Cleared. Defeated Leader Morty (Fog Badge).
- **Geography:** Historic city with traditional architecture.
- **Landmarks:**
  - City Sign at (15, 21).
  - Dance Theater at (23, 21). (Contains Kimono Girls & Gentleman with HM/Gift quest).
  - Pokémon Center at (23, 27).
  - House at (13, 27).
  - Lugia House at (5, 21).
- **NPCs:** Gramps (20, 21), Lass (19, 29).
- **Dance Theater Interior:**
  - **NPCs:** Gentleman (7, 10), Cooltrainer M (10, 10), Granny (3, 6).
  - **Objects:** Rhydon Sprite (6, 8) (Flavor text only).
  - **Layout:** Stage north of fancy panels at Row 6.
- **Quests:**
  - **Kimono Girls:** Defeated all 5. Received HM03 (Surf).
  - **Lake of Rage:** Gym Guide mentioned Gyarados swarm/conspiracy.
- **Events:**
  - Met Bill in PC. Time Capsule active tomorrow.

## Goldenrod City
- **Status:** Arrived. Entrance from Route 34 at (18, 35).

## Quest Log
- **Badges:** Zephyr (Violet), Hive (Azalea), Plain (Goldenrod).
- **Events:**
  - Defeated Rival Silver (Azalea Town).
  - Cleared Sprout Tower (Flash) & Slowpoke Well.
  - Defeated Leader Bugsy.
  - Paprika evolved into Quilava.
  - Received Mystery Egg.
  - Found Revive at (20, 32).
  - Solved Farfetch'd puzzle in Ilex Forest.
  - Defeated Kimono Girls (Naoko, Sayo, Zuki, Kuni, Miki).
  - Quest Complete: Defeated all 5 Kimono Girls. Received HM03 (Surf).

## Global Game Mechanics
### Tile Mechanics
- **FLOOR:** Walkable. Standard movement.
- **WALL:** Impassable.
- **PIT / HOLE:** Traversable warp. Falling in warps player to the floor below. Essential for some puzzles.
- **INVISIBLE_FLOOR (Ecruteak Gym):** Traversable only on specific tiles. Stepping on the wrong tile warps player to start. Safe path must be discovered.
- **LEDGE_HOP_DOWN:** Walkable only from the tile directly above. Acts as a WALL from all other directions. Automatically jumps the player down one tile.
- **HEADBUTT_TREE:** Impassable. Treated as a solid obstacle.
- **TALL_GRASS / LONG_GRASS:** Walkable. Contains wild Pokémon encounters.
- **WARP_CARPET (DOWN/UP/LEFT/RIGHT):** Walk 'off' the map edge in the direction of the carpet to exit. Merely standing on the tile is insufficient.
- **DOOR / LADDER / STAIRS / CAVE:** Walk onto to warp to a new area or floor.
- **COUNTER:** Impassable. Interact with NPCs from the adjacent tile facing the counter.
- **PC / SIGNS / OBJECTS:** Impassable. Interact from adjacent tile.
- **FAKE_HOLE:** Tiles appearing as holes/warps in Burned Tower B1F (e.g. 10,8) are traversable floors. Verify with Game State Warps list.
- **WATER:** Traversable using Surf. Contains wild Pokémon and Swimmers.

### Battle Mechanics
- **Menu Navigation:** ALWAYS use `select_battle_option` for the main battle menu. Never use raw directional inputs here.
- **Cursor Memory:** The move cursor remembers the last used move. ALWAYS check cursor position before selecting!
- **Switch Prompt:** Defaults to YES. Press B to decline safely.
- **Accuracy Debuffs:** Effective vs strong opponents (e.g. Smokescreen).

## Strategy Notes
- Team Strategy: Paprika (Quilava) is the carry and current lead. Basalt (Geodude) has Magnitude.
- Tactics: Use Flame Wheel on Morty's Ghosts.
- Protocol: Mark NPCs immediately.
- **Position Verification:** When movement is interrupted (e.g. by new object), immediately check actual coordinates. Do not assume movement completed.
- Record new Pokémon discoveries immediately, even during battle.
- Always verify object existence before interacting.
- **NPC Interaction:** Use `stun_npc` on moving NPCs to ensure successful interaction.
- **Smokescreen Survival:** Against stronger/type-advantaged opponents, stacking accuracy debuffs is a verified survival strategy.
- **Marking Protocol:** Mark objects *immediately* upon sighting to capture their ID. If a battle starts, the opportunity might be lost if you leave the map.
- **Missing Data:** Firebreather Walt on Route 35 (likely Object ID 6) was not marked as defeated before leaving the map.

## Route 34
- **Geography:** South end connects to Ilex Forest Gate.
- **Status:** Defeated Picnicker Gina, Youngster Ian, & Camper Todd. Paprika Lv23. Exploring East side. Finding exit.
- **Quest:** Gina called (Turn 2936) offering an item on Route 34.
- **Berry Mechanics:** Berry trees regenerate new berries every day. Note which trees bear which berries.
- **Items:** Item ball at (7, 30) blocked by fake tree at (8, 24). Likely requires Surf.

## Day Care Center
- Entered main building. Gramps (Day Care Man) and Granny are inside.
- **Exits:** Side (Left) to Yard, Front (Down) to Route 34.
- **Day Care Mechanics:** The side exit (WARP_CARPET_RIGHT) leads to the Day Care Yard/West Route 34.
- **Fake Tree at (8, 24):** The tree-like object at (8, 24) in the Day Care Yard is NOT cuttable. It is a solid wall.
- Caught Cirrus (Pidgey) Lv12 on Route 34.

## Goldenrod Pokecenter 1F (11_20)
- **Status:** Visited. Healed team.
- **Geography:** Entrance (3,7). Counter (3,2). 2F Stairs (0,7).
- **NPCs:** Nurse Joy, Gameboy Kid, Lass, Pokefan F.
- **Tile Mechanics:**
  - FLOOR: Walkable.
  - COUNTER: Impassable. Interact from adjacent tile.
  - WARP_CARPET_DOWN: Exit to Goldenrod City.
  - LADDER: To 2F.
- **Battle Cursor Memory:** The move cursor remembers the last used move. In Turn 3406, a manual move selection failed (selected Tackle) because the cursor was *already* on Rock Throw, causing the inputs to wrap to Tackle. Always check Screen Text for `▶` before navigating.

## Route 35
- **Status:** Arrived from Goldenrod Gatehouse.
- **Geography:** Path North to Route 36.
- **Trainers:**
  - Picnicker Kim (Vulpix Lv15) at (10, 26). Defeated.
  - Camper Ivan (Diglett Lv10/14, Zubat Lv10) at (5, 19). Defeated.
  - Juggler Irwin (Voltorb Lv2/6/10/14) at (5, 10). Defeated.
  - Firebreather Walt (Magmar Lv11/13) at (3, 10). Defeated.
- **Correction:** Psyduck's name is 'F', not 'Flux'.
- **Tile Mechanics:**
  - FLOOR: Walkable.
  - WALL: Impassable.
  - TALL_GRASS: Wild encounters.
## Route 35 National Park Gate
- **Status:** Entered.
- **NPCs:** Officer (Bug Catching Contest) at (2, 1).
- **Warps:** To Route 35 (South), To National Park (North).
- **Tile Mechanics:**
  - FLOOR: Walkable.
  - WALL: Impassable.
  - DOOR: Warp.
  - COUNTER: Impassable.
  - PC: Impassable.

## National Park
- **Status:** Entered from South Gate.
- **Geography:** Large park area connecting Route 35 and 36.
- **Trainers:**
  - Pokefan Beverly (Snubbull Lv14) at (17, 29). Defeated.
  - Pokefan William (Raichu Lv14) at (16, 9). Defeated.
- **Events:** Bug Catching Contest (Tues/Thurs/Sat).
- **Warps:** South exit to Gatehouse.
- **Obstacles:** Two Youngsters blocking the path North at (10, 41) and (11, 41).
- **Exits:** South Gate (WARP_CARPET_DOWN).

## PC Storage
- Briar (Nidoran♀) Lv12 [National Park]
## National Park Navigation Strategy
- **Solution:** The central fence maze blocks direct access North. The correct path is to enter the eastern section near (20, 41), then pass through the gap in the fence at (18, 39). This leads to the main northern area.
- **Items:** Received Quick Claw from Teacher at (27, 40).

## Route 36
- **Status:** Cleared. Sudowoodo defeated.
- **Trainers:** Schoolboy Alan, Psychic Mark (Defeated).
### Observed Movesets
- **Sudowoodo (Lv20):** Flail, Low Kick, Mimic (Learned Ember). (Suspected: Rock Throw).
## Route 37
- **Status:** Exploring. Heading North to Ecruteak.
- **Trainers:**
  - Psychic Greg (Drowzee Lv17) at (6, 6). Defeated.
- **Geography:** Short route connecting Route 36 and Ecruteak City.
- **Apricorns:** Suspected 'Weird Trees' (Red/Blue/Black Apricorns usually found here).
- **Observed Movesets:**
  - **Drowzee (Lv17):** Hypnosis.
- **Lesson:** Always verify specific tile mechanics (e.g. directional ledges) are explicitly coded in pathfinding tools to avoid invalid paths.
- **Tool Usage:** Always remember to set `autopress_buttons: true` when using custom tools that return button sequences.
## Burned Tower
- **Status:** Cleared. Defeated Rival Silver.
- **Geography:** Central area is walled off. Must loop around the East side (Column 16) and likely cross via Row 7 to reach Rival.
- **Goals:** Defeat Rival, Find Suicune.
### Critical Lessons
- **Action is Truth:** Never assume a tool is updated unless the `tool_code_updated` message appears. Hallucinating fixes leads to dangerous behavior.
- **Wild Escapes:** Escape probability increases with each failed attempt. Persisting in RUN is statistically better than fighting trash mobs when conserving resources.
- **Tile Mechanics:** HOLE tiles are warps/hazards. Avoid unless intentional.
- **Fake Hazards:** The hole at (10, 9) in Burned Tower is a visual fake. Trust Game State Warps list over visual tiles.
- **FAKE_HOLE (Burned Tower):** Some visual hole tiles (e.g. 10,9) do not function as warps and are walkable. Always verify hazards against the Game State Warps list.
- Used Revive on Paprika during Silver battle.
- **Tool Usage:** `sequence_press` MUST have `autopress_buttons: true` set to function.
- **Battle Menu Cursor Memory:** The Party Menu cursor seems to remember its last position even after exiting and re-entering. Always verify cursor position visually before blindly navigating.
- Battle Result: Defeated Silver. XQH sacrificed to ensure victory.
## Burned Tower B1F
- **Status:** Explored. Beasts fled. Exiting to heal.
- **Geography:** Basement level.
- **Objects:**
  - Item Ball (16, 4) (Blocked)
  - Boulder (17, 8)
- **Mechanics:**
  - **Warp Tiles:** Tiles appearing as holes (e.g. 10,8, 10,9) are safe traversable floors on this level.
- **Events:** Rival Silver defeated. Legendary Beasts fled.
- **Menu Navigation:** When using `sequence_press`, ALWAYS set `autopress_buttons: true`. Visual verification of the cursor position is mandatory before confirming selections.
- **Burned Tower B1F Discovery:** Legendary Beasts (Raikou, Entei, Suicune) fled upon interaction.
- **Tile Mechanics:** Warp at (10, 8) is traversable/landing spot (walked over it). (10, 9) is also a landing spot.
- **Obstacles:** Boulder at (17, 8) blocks access to Item (16, 4) and Warp (17, 7) from the South. Likely requires Strength or falling from upstairs.
- Defeated Sage Ping (Gastly Lv16) at (4, 13).
- Defeated Sage Jeffrey (Haunter Lv22) at (2, 7).
  - Paprika learned Flame Wheel (Lv31).
  - Path Confirmed: (6,7) is a bridge. Row 6 safe tile is (6,6).
## Route 38
- **Status:** Cleared.
- **Trainers:** Sailor Harry, Lass Dana, Beauty Olivia (Defeated).
- **Lore:** Olivia mentions Moomoo Milk. Farm likely nearby.
## Route 39
- **Status:** Arrived from Route 38 (East).
- **Geography:** Route connecting Ecruteak/Route 38 to Olivine City.
- **Landmarks:** Sign at (15, 7).
- Defeated Pokefan Ruth (Pikachu Lv17) at (14, 19).
- Defeated Pokefan Derek (Pikachu Lv17) at (10, 19).
- Farmhouse: Pokefan F mentions milk is shipped to Kanto.
- Quest: Feed Berries to sick Miltank in Barn. (Status: Paused. Requires standard 'BERRY' item. 2 fed so far. Needs more.)
## Olivine City
- **Status:** Surfing to Cianwood City via Route 40/41.
- **Landmarks:**
  - Sign at (17, 11): 'The Port Closest to Foreign Lands'.
  - Pokémon Center at (13, 21).
  - Poké Mart at (19, 17).
  - Gym at (10, 11).
  - Fishing Guru House at (13, 15). Obtained Good Rod.
  - Tim's House at (25, 11). Trade: Krabby for Voltorb.
  - Olivine Cafe at (7, 21). Contains Generous Sailor (HM Strength).
- **NPCs:** Youngster (20, 13), Sailor (16, 22).
- **Quests:**
  - **Jasmine & Lighthouse:** Rival Silver said Jasmine is at the Lighthouse. Gym is empty.
  - **HM Strength:** Fisher in Pokémon Center said a "Generous Sailor" in the "Olivine Cafe next door" teaches Strength.
  - **Good Rod:** Obtained from the Fishing Guru in the house north of the Pokémon Center.
  - **Friendship Rater:** The NPC in the Pokémon Center is a Friendship Rater.
## Olivine Lighthouse
- **Goal:** Retrieve SecretPotion from Cianwood.
- **Status:** Descending via East Pits.
- **Proven Path to Top:**
  1. Go to 5F (West Ladder).
  2. Drop into Pit at (16, 7). Lands on 4F East Balcony.
  3. Walk North to Pits at (8,3)/(9,3). Drop into them. Lands in 3F Central Room.
  4. Climb Central Ladder at 3F (9,5) -> 4F Central (9,5).
  5. Climb Central Ladder at 4F (9,7) -> 5F Central (9,7).
  6. Walk South past Sailor to find next ladder.
- **Floor Guide:**
  - **1F:** Sailor (8,2), Ladder (3,11), Lore: Lighthouse honors Pokémon that lit the sea.
  - **2F:** Gentleman Alfred, Sailor Huey, Ladder (5,3).
  - **3F:** Bird Keeper Theo (West), Gentleman Preston (East), Central Ladder (9,5) [KEY].
  - **4F:** Lass Connie, Sailor Kent, Central Ladder (9,7) [KEY].
  - **5F:**
    - West/North: Bird Keeper Denis. Ladder to 4F (3,5).
    - East: Pits to 4F East.
    - Central: Arrival from 4F Ladder. Path South to hidden area.
    - Items: TM34 (Swagger) at (2,13).
- Found Super Repel at (6, 15) on Lighthouse 5F.
## Route 40
- **Status:** Surfing South to Cianwood.
- **NPCs:**
  - Silver (14, 15) - Passive.
  - Silver (18, 30) - Sighted.
- **Geography:** Sea route connecting Olivine to Cianwood.
- **Objects:** Sign (14, 10), Rocks at (6,9), (7,8), (7,11).
- **Trainers:**
  - Swimmer Elaine (Staryu Lv21) at (5, 19). Defeated.
  - Swimmer Paula (Staryu Lv19, Shellder Lv19) at (10, 25). Defeated.
  - Swimmer Randall (Shellder Lv18, Wartortle Lv20). Defeated.
- Received call from Joey about his Rattata.
- **BUOY:** Impassable obstacle.
- **Lesson:** Navigation tools must explicitly check player state (e.g., surfing) to correctly identify traversable tiles like WATER.

## Route 41
- **Status:** Entered from Route 40 (North).
- **Geography:** Sea route with Whirl Islands.
- **Goal:** Navigate to Cianwood City.