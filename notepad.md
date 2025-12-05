# Gem's Pokémon Crystal Journey

## 🌍 Global Status & Quests
- **Kanto Campaign:** Obtain 8 Badges.
- **Copycat (Saffron):** Quest Complete. Magnet Train Pass Obtained.
- **Rematches:** Anthony (Route 33) [Spearow Swarm], Joey (Route 30).

## 📍 Current Mission: Kanto Journey
**Status:** In Celadon Pokémon Center. 4/8 Badges.
**Objective:** Defeat Erika (Celadon Gym).
**Action Plan:**
1. Talk to NPCs in Pokémon Center.
2. Locate and Challenge Celadon Gym.

### Completed Objectives
- **Pewter Gym:** Brock Defeated (Boulder Badge Obtained).

## Pewter City
- **Status:** Explored.
- **Geography:**
  - Pokémon Center: (13, 25).
  - Gym: (16, 17).
  - Mart: (23, 17).
  - Museum: (15, 9).
  - Nidoran House: (29, 13).
- **Key NPCs:** Old Man (Silver Wing Obtained) - (28, 17).

## Route 2 (Traversed)
- **Geography:** Diglett's Cave South (12, 7). Nugget House East (15, 15).
- **Status:** Path to Pewter cleared (Cut Tree removed).

## Archived Logs
- **Johto:** Champion. Rocket Disbanded.
- **S.S. Aqua:** Rescue complete.
- **Power Plant:** Power restored.

## Global Game Mechanics
### General Mechanics
- **Physics:** Boulders cannot push other boulders. You must occupy the tile 'behind' a boulder to push it.
- **'Scoot' Mechanic:** Leaving and re-entering a map is a verified method to refresh the map state and advance puzzles (e.g., moving NPCs) after a trigger event.
- **Warp Verification:** The Game State 'Warps' list is the absolute source of truth. If a tile is not listed there, it is NOT a warp, regardless of visual cues or 'system warnings'.
- **Pokegear:** Icons: Back, Map, Phone, Radio. Blind inputs unreliable.
- **Radio:** 'A' toggles Manual/Preset. Tune to 20.0 for Poké Flute. Phone calls reset frequency.
- **Key Items:** Passive upgrades (e.g., Radio Card) may not list in inventory.
- **path:** Harness Feature. Automatically moves along the `path_plan` coordinate list. NOT a custom tool.

### Tile Mechanics
- **FLOOR:** Walkable.
- **WALL:** Impassable.
- **WINDOW:** Impassable Wall.
- **PIT / HOLE:** Traversable warp.
- **ICE:** Slippery. Slide until hitting a wall or non-ice tile.
- **LEDGE_HOP_DOWN:** One-way jump South.
- **TALL_GRASS:** Walkable (Wild Encounters).
- **WATER:** Traversable (Surf required).
- **FLOOR_UP_WALL:** Context Dependent. Verified TRAVERSABLE on Victory Road (3_91) at (13, 38). IMPASSABLE in Dragon's Den B1F, Route 10 North, Route 9, Diglett's Cave (3_84) at (12, 24), and Route 3 (18, 12).
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
- **BOOKSHELF:** Impassable Obstacle.
- **Map Markers:** Use simple emojis (e.g., ⭐) to prevent errors.

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
- **Radio Mechanics:** Phone calls reset the Radio frequency to default. Always retune to 20.0 after a call before interacting with Snorlax.
- **Menu Navigation:** Blind menu macros are unreliable due to wrapping and cursor memory. Always use `navigate_menu` or visual feedback tools.

## Trainer Rosters
- **Cerulean Gym (Misty):** Golduck (Lv42), Quagsire (Lv42), Lapras (Lv44), Starmie.
- **Saffron Gym:** Defeated.

### Elite Four Strategy
- Defeated.

## Recent Victories
- **Misty:** Defeated (Cascade Badge).
- **Champion Lance:** Defeated.
- **Lt. Surge:** Defeated.

## Lavender Town
- **Soul House:** Located South-Central. Memorial site.
- **Radio Tower:** Located North.
- **Name Rater:** Likely the house south of the mart.

## Saffron City
- Arrived via Route 6 Gate.
- Goal: Deliver Lost Item (Doll) to Copycat (NW). Gym Defeated.
- **Syntax Reminder:** The tool 'path' does not exist. Use 'find_path' for calculations or standard directional buttons for movement.
  - 25_14: Route 5 Saffron Gate. Officer at (0, 4).
- **Location:** North Saffron (near Magnet Train).
- Phone: Hiker Anthony reported Geodude swarm (likely Route 46).
- Cerulean: Cooltrainer F at (21, 24) has a Slowbro. 
- Fisher (Saffron PC): Cerulean Cave has collapsed.

## Active Custom Tools & Features
- **find_path:** Pathfinding with A*.
- **attempt_surf:** Automates surfing interaction.
- **select_move:** Selects battle moves via screen text.
- **force_press_button:** Automates repetitive inputs.
- **navigate_menu:** Robustly selects menu options by reading screen text.

## Power Plant
- Trade: Gym Guide (5, 5) wants Dugtrio for Magneton.

## Route 10 North
- **Split Layout:** The map is divided into two isolated sections by a vertical wall at x=3 and a horizontal barrier of FLOOR_UP_WALL tiles at y=4.
- **East Section:** Accessed from Route 9 (East). Contains PokeCenter. Dead end.
- **West Section:** Contains Rock Tunnel. Must be accessed from the western side of Route 9.

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

- **Pokegear Navigation:** The menu is a horizontal ROW [BACK | MAP | PHONE | RADIO]. Navigation wraps or clamps. Reliable path to Radio: Reset to BACK (Left x3), then RADIO (Right x3). Exit by selecting BACK.
- **Pokegear Navigation:** Verified as a HORIZONTAL ROW: [BACK] [MAP] [PHONE] [RADIO]. 'B' exits the Tuner/Map, and pressing 'B' in the Main Menu closes the Pokegear and returns to the Start Menu.
- **Cursor Memory:** Start Menu cursor remembers the last selection. After using PACK, it stays on PACK. POKEGEAR is one slot below PACK.
- **Pokegear Menu:** Verified that 'B' button DOES close the main menu and returns to the Overworld.
- **Phone Call:** Youngster Joey called. Discussed Rattata/Status. Reset Radio frequency.
- **Radio Mechanic:** Confirmed that receiving a phone call resets the radio frequency to default. Must retune after every call.
- **Radio Tuning:** Snorlax snoring message confirms radio must be active. Phone calls reset frequency. Retuning to 20.0 is mandatory after every interruption.
- **UI Mixed State:** Observed Pokegear menu header persisting over interaction text boxes. Requires aggressive 'B' pressing to clear both layers.
- **Menu Navigation Correction:** Start Menu cursor memory can lead to wrong selections (e.g. Party vs Pokegear). To fix, force cursor to top (Up x5) before navigating down.
- **Radio Mechanics:** Confirmed again: Phone calls ABSOLUTELY reset the radio frequency. Must retune immediately after any call.
- **Phone Call:** Hiker Anthony called (Vermilion). Interrupted radio tuning sequence. (Resolved)
- **Menu Order:** Verified Start Menu: Pokedex, Pokemon, Pack, Pokegear (4th), Status (Player), Save, Option, Exit.
- **Radio Tuning Correction:** 'Up/Down' cycles presets. To manually tune to the Poke Flute (20.0), use 'Right' to move the needle to the far end of the spectrum.
- **Pokegear Menu:** Horizontal layout [BACK | MAP | PHONE | RADIO]. Use `force_press_button` for navigation, as `navigate_menu` is vertical-only.
- Battle Strategy: Smokescreen forces Rollout misses, resetting its damage chain.

- Route 3: Upper path blocked at x=24. Jumped down ledges at x=21. Exploring lower area (Grass/Trainers).
- **Sprite Reliability:** Overworld sprites can be misleading (e.g., Firebreather using Fisher sprite). Always trust the battle intro text for accurate trainer identification.
- **Map Markers:** Use simple, standard Unicode emojis. Complex or composite emojis (e.g., ⚕️) may fail validation.

## Celadon City
- **Status:** Arrived. At Pokémon Center.
- **Key NPCs:**
  - Gentleman (PC): Friendship Rater.
  - Pharmacist (PC): Flavor text.
  - Super Nerd (PC): Eusine? (Mentioned Suicune).
  - Cooltrainer F (PC): Confirmed Erika uses Grass-types.
## Celadon Mansion
- **Status:** Exploring 2F.
- **Geography:**
  - Entrance: (16, 9) in Celadon City.
  - 1F (Manager's Suite): Visited.
  - 2F: Current Location.
- **NPCs (1F):** Granny (1, 5), Meowth (2, 6), Clefairy (3, 4), Nidoran (4, 4).
- **NPCs (3F):** Game Designer (Cooltrainer M), Programmer (Super Nerd - "Play the slot machines!").
- **Meeting Room (2F West):** Empty so far. Contains a Computer (0, 3) and Bookshelf (2, 3).
- **Celadon Mansion 2F:** Stairs at (0,0) and (1,0) are blocked by a wall. Must access from another floor.
- **Celadon Mansion 3F:** Game Freak Development Room. Contains staff and a drawing.