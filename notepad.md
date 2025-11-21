# Gem's Pokémon Crystal Journey

## Current Goals
- [ ] Reach Azalea Town (Primary)
- [ ] Hatch the Mystery Egg (Secondary)
- [ ] Catch Bellsprout (Tertiary) - Postponed

## Quest Log
- Defeated Rival Silver (Cherrygrove).
- Cleared Sprout Tower (Defeated Elder Li, obtained HM05 Flash).
- Paprika evolved into Quilava!
- Defeated Gym Leader Falkner (Earned Zephyr Badge, TM31).
- Received the Mystery Egg from Elm's Aide in Violet City.

## Game Mechanics
- Saving Money: Mom saves a portion of winnings.
- COUNTER: Impassable object. Interact from the front to speak with NPCs behind it.
- LADDER: Warps between floors.
- FLOOR_UP_WALL: Impassable wall from the North (looks like a ledge).

## Strategy Notes
- Team Strategy: Paprika (Quilava) is the carry. Basalt (Geodude) needs training.
- Tactics: Smokescreen vs physical attackers.
- Protocol: Mark NPCs immediately.

## Sprout Tower
- Status: Cleared. Defeated Sage Li. Obtained HM05 Flash.
- Items: Collected Potion, Escape Rope (14,1).

## Route 29 & Gate
- Connects New Bark, Cherrygrove, and Route 46.

## Route 46 (Southern Section)
- Connections: South to Route 29/46 Gate.
- Wild Pokémon: Rattata (Lv 3), Geodude (Lv 2), Spearow (Lv 2).
- Geography: Southern area separated from North by one-way ledges at Row 19. Northern area currently inaccessible from here.
- Sign at (9, 27): "MOUNTAIN RD. AHEAD".
- Traversal: TALL_GRASS is traversable.
- Discovery: Caught Geodude (Basalt) in grass at (5, 26).

## Lessons Learned
- Record new Pokémon discoveries immediately, even during battle.
- Always verify object existence before interacting.

## Cherrygrove City
- Locations: Poké Mart (23, 3), Pokémon Center (29, 3), Guide Gent's House (25, 9), Unknown House (17, 7)
- Cherrygrove PC Fisher: Confirmed PC storage is free.
- Cherrygrove Speech House: Pokefan M advised visiting Gyms and collecting Badges.

## Route 30
- Geography: Split into East and West paths.
  - East Path: Leads to Mr. Pokémon's House. Dead ends at Row 2 (Trees).
  - West Path: Leads to Violet City. Accessible via crossover at Row 30.
- Trainers:
  - Youngster Joey (Rattata Lv 4) - Defeated.
  - Youngster Mikey (Pidgey Lv 2, Rattata Lv 4) - Defeated.
  - Bug Catcher Don (Caterpie Lv 3 x2) - Defeated.
- Wild Pokémon: Caterpie, Pidgey, Weedle, Hoppip, Rattata.
- Navigation Notes:
  - Path West at (9, 7) is blocked by trees.
  - Must use the crossover at Row 30 to switch sides.

## Route 31
- Connects Route 30 to Violet City. Go North through grass to bypass wall.
- Obstacle: Cooltrainer M (32,8). Dark Cave entrance at (34, 5).

## Violet City
- Locations: PC, Gym, Academy.
- Trade: Bellsprout -> Onix.
- Sprout Tower Layout: 1F and 2F are partitioned. To switch sides on 2F, use ladders to traverse the 1F outer ring.
- Encountered Sage (Name Unknown) in 2F Left Southern Corridor.
- Pathfinding tools treat 'unseen' tiles as walls. Verify boundaries manually if pathfinding fails.
- Verified Tile Types: FLOOR (Walkable), WALL (Impassable), LADDER (Warp), CAVE (Traversable Floor), WATER (Impassable without Surf).
- Defeated Sage Edmond (Sprout Tower 2F Left, South Corridor).
- Violet Gym: Defeated Bird Keepers Abe and Rod, and Leader Falkner.
- Strategy Insight: Paprika's level advantage and Special Attack carried the gym.
- Tool Lesson: `find_path` returns coordinates, not buttons.
## Route 32
- Connects Violet City (North) to Union Cave/Azalea (South).

- Trainers Defeated: Youngster Albert (15, 22), Youngster Gordon (4, 63), Youngster at (11, 80).
- Trainers Avoided: Cooltrainer M (19, 8), Lass (10, 30), Youngster (3, 45).
- Important NPCs: Scam Fisher (7, 70) [Declined Offer].
- Items: Item Ball at (6, 53) (Bridge).
- Key Items: Old Rod (Obtained in Route 32 Pokémon Center).
## Union Cave
- Entered from Route 32 (17, 3).
- Union Cave: Hiker Daniel at (3, 6) (originally misidentified as Pokefan M). Onix Lv11 (Bind, Tackle).
- Defeated Hiker Daniel (Union Cave). Paprika reached Lv 16.
- Hiker Russell at (11, 8). Geodude Lv 4. Note: 'POKEFAN_M' sprite = Hiker.
- Defeated Hiker Russell (Union Cave, 11,8). Team: Geodude Lv4, Lv6, Lv8.
- Collected Potion at (4,17).
- B1F: Ladder at (7, 19) connects to 1F (5, 19).
- B1F: Found TM39 (Swift) at (2, 16).
- B1F: Found X Defend at (17, 23).