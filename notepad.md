# Gem's Pokémon Crystal Journey

## 📍 Current Mission: Restore Power
**Status:** Event Triggered.
**Objective:** Return to Cerulean Gym to find Rocket Grunt.
**Side Quest:** Gina (Route 34) offered an item via phone. Anthony (Route 33) & Joey (Route 30) want rematches.
**Reason:** Spoke to Manager and Officer. Officer asked for cooperation, confirming the event is active.

**Cerulean Gym Search Summary:**
- Previous search negative. Retrying now that event is triggered.

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
- **FLOOR_UP_WALL:** Context Dependent. Verified TRAVERSABLE on Victory Road (3_91) at (13, 38). IMPASSABLE in Dragon's Den B1F.
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

### Elite Four Strategy
- Defeated.
## Recent Victories
- **Champion Lance:** Defeated.
- **Lt. Surge:** Defeated.
- **Quest Update:** Found Clefairy Doll in Vermilion Fan Club. Must trigger quest at Copycat in Saffron first to pick it up.
- **Route 6:** Path to Saffron Gatehouse is blocked by a Pokefan M at (17, 4). Nearby sign for Underground Path.
## Saffron City
- Arrived via Route 6 Gate.
- Goal: Explore, find Copycat, Gym.
- **Syntax Reminder:** Do not use 'path' as a button input. Use 'path_plan' or directional buttons.
  - 25_14: Route 5 Saffron Gate. Officer at (0, 4).
- Phone: Hiker Anthony reported Geodude swarm (likely Route 46).
- Cerulean: Cooltrainer F at (21, 24) has a Slowbro.
## Route 9
- **Status:** Traversing East to Power Plant.
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
- **Status:** Retrieving Machine Part.
- **Objective:** Return to Cerulean Gym.
- **Progress:** Defeated Rocket Grunt on Route 24. He confessed the part is hidden in the 'center water' of Cerulean Gym.
- **Next Step:** Return to Cerulean Gym.
- **Search Strategy:** The part is likely a HIDDEN item. Surf to the center of the pool and interact (A) with the water tiles.
- **Route 10 North:** Water channel dead-ends at y=14 (Wall). Must land on western bank (Grass) at (15, 11) to bypass.

## Active Custom Tools
- **find_path:** Pathfinding with A*.
- **attempt_surf:** Automates surfing interaction.
- **scan_unseen:** Scans for reachable unseen tiles.
- **select_move:** Selects battle moves via screen text.

## Active Custom Agents
- **clue_analyst:** Agent for puzzle solving.
## Power Plant
- Trade: Gym Guide (5, 5) wants Dugtrio for Magneton.