# Gem's Pokémon Crystal Journey

## Current Goals
- [ ] Earn Plain Badge (Primary)
- [x] Obtain Bicycle
- [ ] Obtain Radio Card (Secondary) - High Priority
- [ ] Hatch Mystery & Odd Eggs (Secondary) - HAVE BOTH EGGS
- [ ] Explore Goldenrod City (Tertiary)
- [x] Heal at Pokémon Center
- [x] Locate Dept Store
- [x] Locate Bike Shop (Southeast)
- [ ] Find Goldenrod Gym
- [ ] Locate Game Corner

## Goldenrod City
- **Status:** Arrived.
- **Geography:** Large city. Entrance from Route 34 at (18, 35).

## Ilex Forest
- **Status:** Farfetch'd returned. Obtained HM01 (Cut). Tree at (8,25) cut.
- **Geography:**
  - Hidden path on West edge (Col 0) leads North.
  - Path East of center (Row 10) leads to a Northbound corridor at Col 22.
  - Northern path ends at (14, 0).
  - Path south of Youngster (12, 1) connects central area.
  - Exit to Route 34 Gatehouse at (1, 5).
- **Tile Mechanics:**
  - FLOOR: Walkable.
  - HEADBUTT_TREE: Impassable.
  - CUT_TREE: Impassable (requires Cut).
  - WATER: Impassable (requires Surf).
  - LEDGE_HOP_*: One-way jumps.
  - WARP_CARPET_*: Map transition.

## Quest Log
- **Badges:** Zephyr (Violet), Hive (Azalea).
- **Events:**
  - Defeated Rival Silver (Azalea Town).
  - Cleared Sprout Tower (Flash) & Slowpoke Well.
  - Defeated Leader Bugsy.
  - Paprika evolved into Quilava.
  - Received Mystery Egg.
  - Found Revive at (20, 32).
  - Solved Farfetch'd puzzle in Ilex Forest.

## Game Mechanics
- Saving Money: Mom saves a portion of winnings.
- COUNTER: Impassable object. Interact from the front to speak with NPCs behind it.
- LADDER: Warps between floors.
- FLOOR_UP_WALL: Context-dependent. Acts as a ramp (climbable South->North) and ridge (walkable horizontally) in Union Cave.
- Accuracy Debuffs: Verified effective survival tactic against strong opponents (e.g. Silver's Croconaw).

## Strategy Notes
- Team Strategy: Paprika (Quilava) is the carry. Basalt (Geodude) needs training. XQH (Sandshrew) knows Cut for utility.
- Tactics: Smokescreen vs physical attackers/type disadvantages.
- Protocol: Mark NPCs immediately.

## Lessons Learned
- **Position Verification:** When movement is interrupted (e.g. by new object), immediately check actual coordinates. Do not assume movement completed.
- Record new Pokémon discoveries immediately, even during battle.
- Always verify object existence before interacting.
- **NPC Interaction:** Use `stun_npc` on moving NPCs to ensure successful interaction.
- **Smokescreen Survival:** Against stronger/type-advantaged opponents, stacking accuracy debuffs is a verified survival strategy.

## Archived Logs (Azalea & Route 33)
- **Route 33:** Cleared. Hiker Anthony (Phone reg).
- **Azalea Town:** Cleared Well & Gym. Rival Defeated.
- **Caught:** Flux (Psyduck) in Ilex.
## Route 34 Gatehouse
- Connecting Ilex Forest and Route 34.
- NPCs: Teacher, Lass, and a Butterfree sprite.
- Received TM12 (Sweet Scent) from Teacher in Route 34 Gatehouse.
- Lore: Ilex Forest Shrine honors a grass-type protector (implied Celebi).

## Route 34
- **Geography:** South end connects to Ilex Forest Gate.
- **Status:** Defeated Picnicker Gina, Youngster Ian, & Camper Todd. Paprika Lv23. Exploring north.
- **Quest:** Gina called (Turn 2936) offering an item on Route 34.
- **Berry Mechanics:** Berry trees regenerate new berries every day. Note which trees bear which berries.
- **Items:** Item ball at (7, 30) blocked by fake tree at (8, 24). Likely requires Surf.
## Day Care Center
- Entered main building. Gramps (Day Care Man) and Granny are inside.
- **Tile Mechanics:**
  - FLOOR: Walkable.
  - WARP_CARPET_LEFT: Exits to Route 34 (West).
  - WARP_CARPET_DOWN: Exits to Route 34 (Front).
- **Tool Usage Lesson:** Do NOT use 'autopress_buttons' with 'find_path'. It returns a coordinate list, not button strings.
- **Day Care Mechanics:** The side exit (WARP_CARPET_RIGHT) leads to the Day Care Yard/West Route 34.
- **Fake Tree at (8, 24):** The tree-like object at (8, 24) in the Day Care Yard is NOT cuttable. It is a solid wall.
- Caught Cirrus (Pidgey) Lv12 on Route 34.
## Goldenrod Dept Store
- **Status:** Entered 1F.
- **Geography:** Entrance at South. Stairs/Elevator likely at North.
- **NPCs:** Receptionist (1F), Pokefan F, Bug Catcher, Gentleman.
- **Tile Mechanics:**
  - WARP_CARPET_DOWN: Exit to city.
## Goldenrod Bike Shop
- **Status:** Entered. Goal: Obtain Bicycle.
- **NPCs:** Clerk at (7, 2).
## Goldenrod City Mechanics
- **FLOOR:** Standard walkable terrain.
- **WALL:** Buildings, fences, and obstacles (Impassable).
- **DOOR:** Warps to building interiors.
- **WARP_CARPET:** Map connection points.
## Goldenrod Game Corner
- **Status:** Exploring.
- **Tile Mechanics:** Counters and Machines are impassable.
- **Info:** Coin Case tossed in the Underground (Source: Pokefan M).
- **Mechanics:** Card Flip has better odds than slots but lower payout.
- **NPCs:**
  - Pharmacist (8, 7): Lucky Slot Tip.
  - Cooltrainer M (14, 8): Card Flip addict.
  - Pokefan F (17, 6): Card Flip odds tip.
  - Pokefan M (17, 10): To do.
  - Receptionists: (16, 2) & (18, 2).
  - Gentleman (5, 10).
  - Pokefan M (11, 10): Coin Case tip source.
- **Tool Constraint:** `notepad_edit` 'overwrite' fails if >20% change. Use 'replace' or 'append' instead.