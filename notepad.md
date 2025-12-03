# Gem's Pokémon Crystal Journey

## 📍 Current Mission: Radio Tower Expansion
**Status:** In Saffron City.
**Objective:** Obtain the Radio Expansion Card in Lavender Town.
**Next Step:** Visit Copycat (NW Saffron) to trigger doll quest, then head East to Lavender.
**Side Quest:**
- **Copycat (Saffron):** Quest Active. Retrieve Clefairy Doll from Vermilion Fan Club.
- **Rematches:** Anthony (Route 33) [Spearow Swarm], Joey (Route 30).

## Kanto Campaign
- **Objective:** Obtain Kanto Badges.
- **Next Step:** Explore Vermilion City.

## Archived Logs
- **Johto:** Champion. Rocket Disbanded.
- **S.S. Aqua:** Rescue complete.

## Global Game Mechanics
### General Mechanics
- **Physics:** Boulders cannot push other boulders. You must occupy the tile 'behind' a boulder to push it.
- **'Scoot' Mechanic:** Leaving and re-entering a map is a verified method to refresh the map state and advance puzzles (e.g., moving NPCs) after a trigger event.
- **Warp Verification:** The Game State 'Warps' list is the absolute source of truth. If a tile is not listed there, it is NOT a warp, regardless of visual cues or 'system warnings' (which may be hallucinations).

### Tile Mechanics
- **FLOOR:** Walkable.
- **WALL:** Impassable.
- **PIT / HOLE:** Traversable warp.
- **ICE:** Slippery. Slide until hitting a wall or non-ice tile.
- **LEDGE_HOP_DOWN:** One-way jump South.
- **TALL_GRASS:** Walkable (Wild Encounters).
- **WATER:** Traversable (Surf required).
- **FLOOR_UP_WALL:** Context Dependent. Verified TRAVERSABLE on Victory Road (3_91) at (13, 38). IMPASSABLE in Dragon's Den B1F, Route 10 North, and Route 9.
- **LEDGE_HOP_LEFT:** One-way jump Left. Acts as a reset on Map 3_64.
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

### Battle Mechanics
- **Switch Prompt:** Defaults to YES. Press B to decline safely.
- **Accuracy Debuffs:** Effective vs strong opponents (e.g. Smokescreen).
- **Type Effectiveness:** Fire is 0.5x effective against Water/Ground (not 0.25x).
- **Weather:** Rain Dance reduces Fire-type damage by 50%.

## Strategy Notes
- **Mechanics:** 'Scoot' refreshes map. Trust Screen Text. Mark NPCs.
- **Surfing:** Pathfinding must strictly separate Land/Water.
- **Team:** Paprika (Lead), Basalt (Backup).

## Johto History
- **Cleared:** National Park, Cianwood, Mahogany, Goldenrod, Rocket Base, Ice Path, Blackthorn.
- **Key Items:** HM06 (Whirlpool), Rising Badge, Dratini.
- **Tin Tower:** Paused. Need Rainbow Wing (Catch Raikou, Entei, Suicune).
- **Mechanics:** 'Scoot' refreshes map. Phone calls pause movement.

## Lessons Learned
- **Menu Navigation:** Blind sequence inputs in menus are unreliable due to state latency. Verify cursor state step-by-step using screen text.
- **Victory Road Navigation:** Ridge at Y=12 blocked South->North at X=9,10,11. Pit seen at (0,11) but currently unreachable from South.

## Trainer Rosters
- **Saffron Gym:**
  - **Leader Sabrina:** Defeated. Espeon (Lv 46), Mr. Mime (Lv 46, Reflect), Alakazam (Lv 48).
  - **Psychic Jared:** Mr. Mime (Lv 32), Exeggcute (Lv 35), Exeggcute (Lv 35).
  - **Medium Rebecca:** Drowzee (Lv 35), Hypno (Lv 35).
  - **Psychic Franklin:** Kadabra (Lv 37).
  - **Medium Doris:** Defeated.

### Elite Four Strategy
- Defeated.
## Recent Victories
- **Champion Lance:** Defeated.
- **Lt. Surge:** Defeated.
- **Quest Update:** Found Clefairy Doll in Vermilion Fan Club. Must trigger quest at Copycat in Saffron first to pick it up.
- **Route 6:** Path to Saffron Gatehouse is blocked by a Pokefan M at (17, 4). Nearby sign for Underground Path.
## Saffron City
- Arrived via Route 6 Gate.
- Goal: Challenge Saffron Gym. Then find Copycat (NW).
- **Syntax Reminder:** Do not use 'path' as a button input. Use 'path_plan' or directional buttons.
  - 25_14: Route 5 Saffron Gate. Officer at (0, 4).
- **Location:** North Saffron (near Magnet Train).
- Phone: Hiker Anthony reported Geodude swarm (likely Route 46).
- Cerulean: Cooltrainer F at (21, 24) has a Slowbro.
- Fisher (Saffron PC): Cerulean Cave has collapsed.
## Route 9
- **Status:** Explored.
- **Key Features:**
  - **Cut Tree:** At (5, 8), blocks main path. (Cleared).
  - **Ledges:** Multiple one-way ledges creating split paths. Gap at x=53 allows Northbound travel.
  - **Water Access:** Blocked at Rows 5-14 by wall at x=55. Accessible at (55, 4).
  - **Warps:** (0, 4) leads to Cerulean City.
- **Trainers:**
  - Youngster (11, 4) on Northern path (currently unreachable).
  - Camper Dean (Defeated) at (21, 11).
  - Lass (Sighted) at (12, 15).
  - Pokefan M (Sighted) at (36, 15).

## Quest Log: Machine Part
- **Status:** Complete!
- **Objective:** Obtain Kanto Radio Card.
- **Progress:** Returned Machine Part to Manager. Power restored. Received TM07 (Zap Cannon).
- **Next Step:** Go to Lavender Town Radio Tower to get the expansion card.

## Active Custom Tools
- **find_path:** Pathfinding with A*.
- **attempt_surf:** Automates surfing interaction.
- **scan_unseen:** Scans for reachable unseen tiles.
- **select_move:** Selects battle moves via screen text.

## Active Custom Agents

## Power Plant
- Trade: Gym Guide (5, 5) wants Dugtrio for Magneton.
## Route 10 North
- **Split Layout:** The map is divided into two isolated sections by a vertical wall at x=3 and a horizontal barrier of FLOOR_UP_WALL tiles at y=4.
- **East Section:** Accessed from Route 9 (East). Contains PokeCenter. Dead end.
- **West Section:** Contains Rock Tunnel. Must be accessed from the western side of Route 9.

# Saffron Gym
- Puzzle: Warp tiles.
- Exit: (8, 17)
- Start Room Warps: (11, 15)
## Saffron Gym Warp Log
- **Status:** Cleared. Marsh Badge obtained.
- **Leader Sabrina:** Defeated.

## Lessons Learned
- **Pathfinding:** Unseen tiles are assumed traversable. Expect reroutes in complex city layouts.