# Gem's Pokémon Crystal Journey

## 📍 Search Plan: Cerulean Gym Pool
**Status:** Surfing at (6, 2).
**Objective:** Search Northern Row Eastbound.

**Priority:**
1. Check (5, 1), (5, 3), (6, 2).
2. Move East to (6, 2).
3. Continue checking East.

**Completed:**
- Col 5-9: Done.
- Col 1: Done.
- Row 2: (5, 2) Checked.

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
- **WARP_CARPET:** Walk off map to exit.
- **LADDER:** Traversable warp.
- **WARP_CARPET_DOWN:** Walk Down to warp.
- **STAIRCASE:** Traversable warp.
- **COUNTER:** Impassable. Allows interaction with Entity on other side.
- **WATER/LAND Interaction:** Moving from Water to Land triggers 'Want to get off?'. Cancel with B to face Land. Moving from Land to Water triggers 'Want to Surf?'. Both prompts override hidden item checks.

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
- **System Correction:** 'path' is a button command, not a tool. Ensure `buttons_to_press` uses `['path']` (not `['path (tool)']`) and `tools_to_call` uses `find_path`.
  - 25_14: Route 5 Saffron Gate. Officer at (0, 4).
- Phone: Hiker Anthony reported Geodude swarm (likely Route 46).
- Cerulean: Cooltrainer F at (21, 24) has a Slowbro.
## Route 9
- **Status:** Entered from Cerulean (South Path).
- **Geography:** Split path separated by ledges. Currently on Southern path.
- **Trainers:**
  - Youngster (11, 4) sighted on Northern path (unreachable from current position).
  - Lass (12, 15) sighted on Southern path.
## Route 9
- **Status:** Exploring East towards Power Plant.
- **Trainers:**
  - Camper Dean (Defeated) at (21, 11).
  - Lass (Sighted) at (12, 15).
  - Pokefan M (Sighted) at (36, 15).
- **Mechanics Lesson:** Do NOT use `autopress_buttons: true` for built-in tools like `select_battle_option`.
- **Obstacles:** Path East on Row 14 blocked at x=42. Investigating Row 16 `FLOOR_UP_WALL`.
- **Tool Usage Lesson:** Do NOT use `autopress_buttons: true` for tools that do not return a JSON array of button strings (like `find_path`) or built-in tools (like `select_battle_option`).
## Quest Hypothesis
- **Rocket Grunt Sequence:** Power Plant (Trigger) -> Cerulean Gym (Encounter) -> Route 24 (Battle).
- **Current State:** Gym Empty. Police confirmed theft.
- **Next Step:** If Grunt not on Bridge, go to Power Plant via Route 9 (East of Cerulean).
- **Pathfinding Update:** Fixed `find_path` to treat LEDGE_HOP tiles as strictly one-way. They can only be entered from the 'hop' direction (e.g., Down for LEDGE_HOP_DOWN).
- LEDGE_HOP_RIGHT: One-way jump Right.
- **LEDGE_HOP_RIGHT:** One-way jump Right.
- **Tool Safety:** `find_path` returns coordinates (use `path` button). `sequence_press` returns buttons (requires `autopress_buttons: true`). Always verify output formats.
- **Machine Part Search:** Resetting search due to position errors. Currently entering water at (1, 5) to re-verify top-left corner (1, 2)/(2, 2).
- **Interaction Mechanics:** The 'Want to Surf?' prompt overrides item pickup interactions. To check a water tile for a hidden item, you must face it from another water tile. To check a land edge from the water, surf to it and face the land.
**Column 4 (Center):**
- [x] (3, 6) Water - Checked
- [x] (3, 4) Floor - Checked
- [x] (4, 3) Floor - Checked
- [ ] (4, 5) Water - Check from Water
- [ ] (4, 4) Floor - Check from (5, 4)
- [ ] (5, 4) Floor - Checking Now