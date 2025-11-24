# Gem's Pokémon Crystal Journey

## Current Goals
- [x] Deliver SecretPotion to Jasmine (Completed)
- [x] Earn the Mineral Badge (Completed)
- [ ] Travel to Mahogany Town (Primary)

## Status
- **Location:** Mt. Mortar 1F Outside (Northeast Plateau).
- **Objective:** Descend Mt. Mortar to reach Mahogany Town.
- **Team Status:** Healthy. Paprika (Lv40) leading.
- **Backlog:**
  - Cure Miltank (Needs berries).

## Completed Areas Summary
- **Johto West:** Cleared Ecruteak, Goldenrod, Olivine, Cianwood Gyms. Burned Tower cleared (Beasts released). Lighthouse cleared. Sea Routes traversed.

## Quest Log
- **Badges:** Zephyr, Hive, Plain, Fog.
- **Recent Events:**
  - Delivered SecretPotion to Jasmine. Amphy cured.
  - Acquired Shuckie from Mania.

## Global Game Mechanics
### Tile Mechanics
- **FLOOR:** Walkable. Standard movement.
- **WALL:** Impassable.
- **PIT / HOLE:** Traversable warp. Falling in warps player to the floor below. Essential for some puzzles.
- **INVISIBLE_FLOOR (Ecruteak Gym):** Traversable only on specific tiles. Stepping on the wrong tile warps player to start. Safe path must be discovered.
- **LEDGE_HOP_DOWN:** Walkable only from the tile directly above. Acts as a WALL from all other directions. Automatically jumps the player down one tile.
- **FLOOR_UP_WALL:** Visual ledge that acts as a solid WALL. Cannot be jumped over. Treat as an obstacle.
- **HEADBUTT_TREE:** Impassable. Treated as a solid obstacle.
- **TALL_GRASS / LONG_GRASS:** Walkable. Contains wild Pokémon encounters.
- **WARP_CARPET (DOWN/UP/LEFT/RIGHT):** Walk 'off' the map edge in the direction of the carpet to exit. Merely standing on the tile is insufficient.
- **DOOR / LADDER / STAIRS / CAVE:** Walk onto to warp to a new area or floor.
- **COUNTER:** Impassable. Interact with NPCs from the adjacent tile facing the counter.
- **PC / SIGNS / HOUSE_OBJECTS:** Impassable. Includes Bookshelves, TVs, Radios, Windows, etc. Interact from adjacent tile.
- **FAKE_HOLE:** Tiles appearing as holes/warps in Burned Tower B1F (e.g. 10,8) are traversable floors. Verify with Game State Warps list.
- **WATER:** Traversable using Surf. Contains wild Pokémon and Swimmers.
- **WHIRLPOOL:** Impassable obstacle. Requires HM Whirlpool to cross (Hypothesis).
- **BUOY:** Impassable obstacle. Forms barriers on sea routes. Look for gaps.
- **ROCK:** Impassable obstacle. Treated as a solid object.

### Battle Mechanics
- **Menu Navigation:** ALWAYS use `select_battle_option` for the main battle menu. Never use raw directional inputs here.
- **Move Menu Layout:** The move selection menu is a vertical list. Use UP/DOWN to navigate. LEFT/RIGHT do not work.
- **Cursor Memory:** The move cursor remembers the last used move. ALWAYS check cursor position before selecting!
- **Switch Prompt:** Defaults to YES. Press B to decline safely.
- **Accuracy Debuffs:** Effective vs strong opponents (e.g. Smokescreen).

## Strategy Notes
- Team Strategy: Paprika (Typhlosion) is the carry and current lead. Basalt (Geodude) has Magnitude.
- Protocol: Mark NPCs immediately.
- **Position Verification:** When movement is interrupted (e.g. by new object), immediately check actual coordinates. Do not assume movement completed.
- **Screen Text:** Trust visual evidence (Screen Text) over system notes if they conflict. Text can persist or trigger unexpectedly.
- Record new Pokémon discoveries immediately, even during battle.
- Always verify object existence before interacting.
- **NPC Interaction:** Use `stun_npc` on moving NPCs to ensure successful interaction.
- **Smokescreen Survival:** Against stronger/type-advantaged opponents, stacking accuracy debuffs is a verified survival strategy.
- **Marking Protocol:** Mark objects *immediately* upon sighting to capture their ID.

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
## Fly Map Mechanics
- **Navigation:** The Fly map cursor navigation appears to be list-based (cycling through towns in a specific order: New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Lake of Rage -> Blackthorn -> Mt. Silver) rather than purely spatial. Use UP/DOWN to cycle efficiently.

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
## Olivine City (Completed)
- **Status:** Cleared. Mineral Badge obtained.
- **Key Events:**
  - Jasmine cured (SecretPotion delivered).
  - Mineral Badge obtained.
  - HM04 Strength obtained.
  - Good Rod obtained.

# Route 42 & Mt. Mortar
- **Status:** Exploring Mt. Mortar 1F Outside.
- **Goal:** Traverse to Mahogany Town.
- **Geography:** Entrance at (3, 33). Inner cave entrance at (11, 21).
- **Items:** Ultra Ball found on Route 42.
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
- Encountered another 'Fake Silver' at (32, 6). It is a Swimmer.
- Defeated Swimmer Charlie (Fake Silver) at (32, 6).
- Defeated Swimmer Susie at (23, 17).
- Defeated Swimmer Kirk (Fake Silver) at (32, 31).
- Navigated East to Column 46 to bypass buoys. Heading South.
- Blocked by buoys at (48, 50) and (45, 53). Traversing West along Row 52 to find a gap.
- Encountered Swimmer Girl at (9, 50) blocking Row 52. Flanking North to bypass.
- Defeated Swimmer Wendy (Horsea Lv21 x2) at (10, 50).
- Paprika reached Lv38.
## Cianwood City
- **Gym:** Leader Chuck (Fighting). Weak to Psychic.
- **Puzzle:** Requires Strength to move boulders.
- **Gym Guide:** Warns of bullies.
- **Pharmacy:** Acquired SecretPotion.
- **Navigation Protocol:** Always step 1 tile away from warps before pathfinding.
- **Cianwood Photo Studio:** Located at (9, 31). Not the Gym.
- **Cianwood Event:** Encountered Suicune at (10, 14), but it fled. Eusine appeared and challenged me to a battle to earn Suicune's respect.
- Defeated Eusine (Drowzee Lv23, Electrode Lv25, Haunter Lv23). Paprika HP Critical (24/117).
- **Status Update:** Arrived in Olivine City via Fly. Heading to Lighthouse to deliver SecretPotion.
- **Event:** Joey called (Turn 6420). Ignoring for now.