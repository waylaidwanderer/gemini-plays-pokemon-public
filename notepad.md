# Gem's Pokémon Crystal Journey

## Current Goals
- [ ] Heal at Azalea Pokémon Center (Immediate)
- [ ] Enter Ilex Forest (Primary)
- [ ] Hatch the Mystery Egg (Secondary)

## Quest Log
- **Badges:** Zephyr (Violet), Hive (Azalea).
- **Events:**
  - Defeated Rival Silver (Cherrygrove).
  - Cleared Sprout Tower (Flash) & Slowpoke Well.
  - Defeated Leader Bugsy.
  - Paprika evolved into Quilava.
  - Received Mystery Egg.

## Game Mechanics
- Saving Money: Mom saves a portion of winnings.
- COUNTER: Impassable object. Interact from the front to speak with NPCs behind it.
- LADDER: Warps between floors.
- FLOOR_UP_WALL: Context-dependent. Acts as a ramp (climbable South->North) and ridge (walkable horizontally) in Union Cave.

## Strategy Notes
- Team Strategy: Paprika (Quilava) is the carry. Basalt (Geodude) needs training.
- Tactics: Smokescreen vs physical attackers.
- Protocol: Mark NPCs immediately.

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
- **NPC Interaction:** Use `stun_npc` on moving NPCs to ensure successful interaction.

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

## Route 32 & Union Cave (Cleared)
- **Route 32:** Connects Violet to Cave. Old Rod obtained.
- **Union Cave:** Cleared. FLOOR_UP_WALL acts as ramp (S->N) and ridge (E-W).

## Route 33
- Geography: Short route connecting Union Cave and Azalea Town.
- Trainers: Hiker Anthony (Geodude Lv11) - Defeated. Swapped phone numbers.

## Azalea Town & Slowpoke Well
- Status: Battling in Azalea Gym.
- Mission: Defeat Leader Bugsy.
- Note: Cleared Slowpoke Well. Received Lure Ball from Kurt.
- Locations: Kurt's House (9, 5), Slowpoke Well (31, 7), Pokémon Center (15, 9), Poké Mart (21, 5), Azalea Gym (10, 15).

### Azalea Gym (Cleared)
- Status: Defeated Leader Bugsy. Earned Hive Badge & TM49 (Fury Cutter).
- Strategy: Paprika (Quilava) dominated with Ember.

### Slowpoke Well B1F
- **Progress:**
  - Defeated Grunt (Entrance), Grunt (F) (13, 4), Grunt (6, 6).
  - Retrieved Super Potion (10, 3).
  - Spotted Grunt (5, 2), Slowpoke (6, 2), Boulder (3, 2).
- **Interactions:**
  - Slowpoke (7, 4): Has Mail. "Be good and look after the house. Love, Dad".
- **Navigation & Hypotheses:**
  - **Path to East:** Accessible via gap at (8, 6).
  - **FLOOR_UP_WALL (Row 2):** Verified climbable ramps (South->North). Can be traversed horizontally and jumped down from (North->South).