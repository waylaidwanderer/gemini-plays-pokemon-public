# Gem's Pokémon Crystal Journey

## 📍 Current Mission: Wake Snorlax
**Status:** In Vermilion City (Pokegear Menu).
**Objective:** Wake Snorlax.
**Next Step:** Enter Radio Tuner. Force Retune (Tune away then back to 20.0) to fix audio state. Exit and interact with Snorlax.
**Context:** EXPN Card obtained. Lost Item (Clefairy Doll) obtained.
**Side Quest:**
- **Copycat (Saffron):** Quest Active. Have Doll. Return to Copycat after Snorlax.
- **Rematches:** Anthony (Route 33) [Spearow Swarm], Joey (Route 30).

## Kanto Campaign
- **Objective:** Obtain Kanto Badges.
- **Next Step:** Explore Vermilion City.

## Archived Logs
- **Johto:** Champion. Rocket Disbanded.
- **S.S. Aqua:** Rescue complete.
- **Power Plant:** Power restored.
- **Radio Tower:** EXPN Card obtained.

## Global Game Mechanics
### General Mechanics
- **Physics:** Boulders cannot push other boulders. You must occupy the tile 'behind' a boulder to push it.
- **'Scoot' Mechanic:** Leaving and re-entering a map is a verified method to refresh the map state and advance puzzles (e.g., moving NPCs) after a trigger event.
- **Warp Verification:** The Game State 'Warps' list is the absolute source of truth. If a tile is not listed there, it is NOT a warp, regardless of visual cues or 'system warnings' (which may be hallucinations).
- **Phone Calls:** Receiving a phone call resets the Radio audio, requiring the player to retune the channel.
- **Radio Mechanics:** 'A' toggles between Manual Tuning and Preset Selection. 'Right/Left' tunes or scans.

### Tile Mechanics
- **FLOOR:** Walkable.
- **WALL:** Impassable.
- **WINDOW:** Impassable Wall.
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
- **Menu Navigation:** Blind sequence inputs in menus are unreliable. Verify cursor state step-by-step using screen text.
  - **Pokegear Layout:** Icons are arranged in a horizontal row: Back, Map, Phone, Radio. NOT a 2x2 grid.
  - **Menu Hierarchy:** Start -> Pokegear -> Radio (4th Icon) -> Tuner.

## Johto History
- **Cleared:** National Park, Cianwood, Mahogany, Goldenrod, Rocket Base, Ice Path, Blackthorn.
- **Key Items:** HM06 (Whirlpool), Rising Badge, Dratini.
- **Tin Tower:** Paused. Need Rainbow Wing (Catch Raikou, Entei, Suicune).
- **Mechanics:** 'Scoot' refreshes map. Phone calls pause movement.

## Lessons Learned
- **Item Verification:** Always verify possession of Key Items in the Game State list before attempting puzzles. Memory/Logs can be wrong.
- **Menu Navigation:** Blind sequence inputs in menus are unreliable. Verify cursor state step-by-step using screen text.
- **Tool Usage:** `find_path` outputs a coordinate list for `path_plan`. Do NOT use `autopress_buttons: true` with it.
- **Tool Definition:** Defined `tune_radio` to strictly handle radio tuning without side effects (unlike `force_press_button` which adds 'A' presses).

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
- **Lavender Radio Tower:** Obtained EXPN Card.

## Lavender Town
- **Soul House:** Located South-Central. Memorial site.
- **Radio Tower:** Located North.
- **Name Rater:** Likely the house south of the mart.

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

## Quest Log: Snorlax Blockade
- **Status:** Active.
- **Objective:** Wake Snorlax.
- **Progress:** Obtained EXPN Card.
- **Next Step:** Tune to Poke Flute Channel.

## Active Custom Tools
- **find_path:** Pathfinding with A*.
- **attempt_surf:** Automates surfing interaction.

- **select_move:** Selects battle moves via screen text.
- **force_press_button:** Automates repetitive inputs. Configured with 'Double A' bypass (A, sleep, A, sleep) to ignore harness text checks like 'TUNING'.
- **tune_radio:** Presses a direction button multiple times to tune the radio. Bypasses text checks.
- **Menu Verification:** Radio Hierarchy: Start -> Pokegear -> Radio (4th) -> Tuner. Poke Flute is at 20.0 (Far Right).

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

## Route 8
- **Status:** Exploring East towards Lavender.
- **Obstacles:**
  - Biker Gang blocking x=10 (Rows 8-10). Bypass: North (Row 6).
  - Cut Tree at (21, 12).
- **Points of Interest:**
  - Locked Door at (10, 5).
  - Underground Path Sign at (11, 7).