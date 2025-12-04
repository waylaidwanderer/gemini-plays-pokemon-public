# Gem's Pokémon Crystal Journey

## 📍 Current Mission: Wake Snorlax
**Status:** In Vermilion City.
**Objective:** Wake Snorlax using the Poke Flute Radio Channel.
**Next Step:** Retune radio to 20.0 (Poke Flute) and interact with Snorlax again. (Previous attempt failed, likely due to phone call reset).
**Context:** Confirmed with Lavender Radio Tower Gentleman that I have the Kanto Radio expansion (passive upgrade). I possess the LOST ITEM (Doll) for Copycat.
**Side Quest:**
- **Copycat (Saffron):** Quest Active. Have Doll.
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
- **Warp Verification:** The Game State 'Warps' list is the absolute source of truth. If a tile is not listed there, it is NOT a warp, regardless of visual cues or 'system warnings'.
- **Pokegear:** Icons: Back, Map, Phone, Radio. Blind inputs unreliable.
- **Radio:** 'A' toggles Manual/Preset. Tune to 20.0 for Poké Flute. Phone calls reset frequency.
- **Key Items:** Passive upgrades (e.g., Radio Card) may not list in inventory.

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
- **Surfing:** Pathfinding must strictly separate Land/Water.
- **Team:** Paprika (Lead), Basalt (Backup).

## Johto History
- **Cleared:** National Park, Cianwood, Mahogany, Goldenrod, Rocket Base, Ice Path, Blackthorn.
- **Key Items:** HM06 (Whirlpool), Rising Badge, Dratini.
- **Tin Tower:** Paused. Need Rainbow Wing (Catch Raikou, Entei, Suicune).

## Lessons Learned
- **Item Verification:** Passive upgrades (e.g., Radio Card) often don't appear in the inventory; trust NPC dialogue.
- **Tool Usage:** `find_path` outputs a coordinate list for `path_plan`. Do NOT use `autopress_buttons: true` with it.
- **Tool Definition:** Defined `tune_radio` to strictly handle radio tuning without side effects.

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
- **Next Step:** Execute macro to retune Radio to 20.0 and wake Snorlax.

## Active Custom Tools
- **find_path:** Pathfinding with A*.
- **attempt_surf:** Automates surfing interaction.

- **select_move:** Selects battle moves via screen text.
- **force_press_button:** Automates repetitive inputs. Configured with 'Double A' bypass (A, sleep, A, sleep) to ignore harness text checks like 'TUNING'.
- **press_sequence:** Executes a list of button presses. Useful for complex menu navigation or macros.
- **Menu Verification:** Radio Hierarchy: Start -> Pokegear -> Radio (4th) -> Tuner. Poke Flute is at 20.0 (Far Right).
- **Radio Mechanics:** Phone calls reset the frequency. ALWAYS retune to 20.0 after a call. Verify needle position before interacting.

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
- **UI Desync:** If text boxes and menus overlap, use a sequence of 'B' presses to fully exit to the Overworld before re-opening menus. Do not trust mixed states.
- **Tool Usage:** Multiple tool calls in one turn overwrite each other's button outputs. Use `run_code` or a custom tool to chain multiple distinct button actions.
- **Tool Limitations:** `run_code` cannot use `autopress_buttons: true`. To execute complex button sequences, define a custom tool.
- **Phone Calls:** Receiving a phone call resets the Radio audio, requiring the player to retune the channel.
- **Radio Mechanics:** Phone calls reset the Radio frequency. You must retune to the specific channel (e.g., Poké Flute at 20.0) after a call.
- **Phone Calls:** Receiving a phone call resets the Radio audio, requiring the player to retune the channel.
- **Phone Call:** Hiker Anthony called (Vermilion). Reported 'didn't see any' (likely Dunsparce), implying NO swarm active.
- **Phone Call:** Picnicker Gina (Route 34) called. Shared battle story about a Snubbull.
- **Interaction Loops:** If an interaction text box (e.g., 'Snorlax is snoring') appears while trying to access a menu, the menu inputs will likely fail or re-trigger the interaction. Aggressively clear with 'B' before retrying.
- **Phone Call:** Youngster Joey called. Discussed Pidgey. Reset Radio frequency.
- **Pokegear Navigation:** The menu is a horizontal ROW [BACK | MAP | PHONE | RADIO]. Navigation wraps or clamps. Reliable path to Radio: Reset to BACK (Left x3), then RADIO (Right x3). Exit by selecting BACK.
- **Pokegear Navigation:** Verified as a HORIZONTAL ROW: [BACK] [MAP] [PHONE] [RADIO]. 'B' exits functions (Map/Tuner) but NOT the Main Menu; must select 'BACK' to exit.
- **Cursor Memory:** Start Menu cursor remembers the last selection. After using PACK, it stays on PACK. POKEGEAR is one slot below PACK.
- **Pokegear Menu:** 'B' button does NOT close the main menu. Must navigate to and select [BACK].