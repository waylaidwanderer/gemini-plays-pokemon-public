# Gem's Pokémon Crystal Journey

## Current Goals
- [ ] Obtain SquirtBottle (Flower Shop) (Primary)
- [ ] Clear Sudowoodo on Route 36 (Secondary)
- [ ] Retrieve Coin Case from Underground (Tertiary)
- [ ] Hatch Mystery & Odd Eggs (Secondary)

## Goldenrod City
- **Status:** Arrived. Entrance from Route 34 at (18, 35).

## Ilex Forest
- **Status:** Cleared. Obtained HM01 (Cut).
- **Geography:** Hidden path on West edge. Exit to Route 34 at (1, 5).

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

## Game Mechanics
- Battle Cursor: Remembers last move used. ALWAYS check cursor position before selecting!
- Accuracy Debuffs: Effective vs strong opponents.

## Strategy Notes
- Team Strategy: Paprika (Quilava) is the carry. Basalt (Geodude) needs training. XQH (Sandshrew) knows Cut for utility.
- Tactics: Smokescreen vs physical attackers/type disadvantages.
- Protocol: Mark NPCs immediately.
- Tools: `select_battle_option` (FIGHT/PKMN/PACK/RUN), `find_path`, `buy_item_quantity`, `find_interaction_point`, `scan_reachable_unseen`.
- Agents: `battle_strategist` (Battle analysis & move recommendation).
- Whitney Battle: Spam Smokescreen to neutralize Rollout/Stomp.

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

## Goldenrod Game Corner
- **Info:** Coin Case in Underground (Source: Pokefan M).
- **Mechanics:** Card Flip > Slots.

## Route 35 Gatehouse
- Located at Goldenrod (19, 1).

## Goldenrod Underground Entrance (North)
- **Status:** Entered from Goldenrod (9, 5).
- **Geography:** Small room with a ladder down.
- **NPCs:** Super Nerd.
- **Warps:** Ladder to Underground.
- **Tile Mechanics:**
  - FLOOR: Walkable.
  - WALL: Impassable.
  - WARP_CARPET_DOWN: Exit to city.
  - LADDER: Warp to Underground.
- **Navigation Lesson:** Verify building identities (e.g. signs, entering) before assuming. Directional heuristics (e.g. 'West side') can be misleading if landmarks aren't distinct.

## Goldenrod Magnet Train Station
- **Status:** Visited (Turn 3235).
- **Tile Mechanics:**
  - FLOOR: Walkable.
  - WALL: Impassable.
  - WARP_CARPET_DOWN: Exit to Goldenrod City.

## Radio Tower 1F
- **Geography:** Entrance lobby. Reception counter.
- **NPCs:**
  - Receptionist at (5, 6): 'Welcome!' loop from (3, 6). No quiz trigger.
  - Gentleman at (8, 6): Lucky Number Show (ID Mismatch).
  - Cooltrainer F at (12, 6): Radio Card Quiz.
- **Mechanics:**
  - FLOOR: Walkable.
  - WALL: Impassable.
  - COUNTER: Impassable. Interact across to speak to NPCs.
  - WARP_CARPET_DOWN: Exit to Goldenrod City.
  - PC: Impassable.

## Goldenrod Gym
- **Status:** CLEARED. Plain Badge & TM45 (Attract) Obtained.
- **Event:** Whitney cries after defeat. Must attempt to leave to trigger Lass, then speak to Whitney again to get badge.
- **Trainers:** All defeated.
- **Layout:** Flower box maze.

## Goldenrod Pokecenter 1F (11_20)
- **Status:** Visited. Healed team.
- **Geography:** Entrance (3,7). Counter (3,2). 2F Stairs (0,7).
- **NPCs:** Nurse Joy, Gameboy Kid, Lass, Pokefan F.
- **Tile Mechanics:**
  - FLOOR: Walkable.
  - COUNTER: Impassable. Interact from adjacent tile.
  - WARP_CARPET_DOWN: Exit to Goldenrod City.
  - LADDER: To 2F.
- **Battle Cursor Memory:** The move cursor remembers the last used move. In Turn 3406, `select_move(3)` failed (selected Tackle) because the cursor was *already* on Rock Throw (3), causing 'Down, Down' to wrap to Tackle (1). Always check Screen Text for `▶` before navigating.

## Critical Battle Mechanics
- **Cursor Memory:** The move cursor remembers the last used move. Always check the screen text for `▶` before navigating in the move menu. Do not assume it resets to the top.
## Goldenrod Flower Shop
- **Status:** Entered. Goal: Get SquirtBottle.
- **NPCs:** Teacher at (2, 4).
- **Quest Update:** Teacher's sister is at the wiggly tree on Route 36. Must find her to get SquirtBottle.
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

## Lessons Learned
- **Marking Protocol:** Mark objects *immediately* upon sighting to capture their ID. If a battle starts, the opportunity might be lost if you leave the map.
- **Missing Data:** Firebreather Walt on Route 35 (likely Object ID 6) was not marked as defeated before leaving the map.
## National Park
- **Status:** Entered from South Gate.
- **Geography:** Large park area connecting Route 35 and 36.
- **Events:** Bug Catching Contest (Tues/Thurs/Sat).
- **Warps:** South exit to Gatehouse.
- **Obstacles:** Two Youngsters blocking the path North at (10, 41) and (11, 41).
- **Tile Mechanics:**
  - FLOOR: Walkable.
  - WALL: Impassable.
  - WARP_CARPET_DOWN: Exits to South Gate.