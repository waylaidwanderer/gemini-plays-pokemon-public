# Gem's Pokémon Crystal Journey

## 📍 Current Status: Cerulean Gym
- **Location:** Cerulean Gym. Surfing at (7, 2).
- **Goal:** Locate Machine Part. Systematic search of pool.
- **Sequence:** Sweeping East. Checking surroundings of (7, 2) then moving to (8, 2).
- **Intel:** Gym Leader Misty (Water). Weakness: Electric/Grass. Magnet Train down.

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

### Battle Mechanics
- **Switch Prompt:** Defaults to YES. Press B to decline safely.
- **Accuracy Debuffs:** Effective vs strong opponents (e.g. Smokescreen).
- **Type Effectiveness:** Fire is 0.5x effective against Water/Ground (not 0.25x).
- **Weather:** Rain Dance reduces Fire-type damage by 50%.

## Strategy Notes
- **Mechanics:** 'Scoot' refreshes map. Trust Screen Text. Mark NPCs.
- **Surfing:** Pathfinding must strictly separate Land/Water.
- **Team:** Paprika (Lead), Basalt (Backup).

## National Park (Cleared)
- Connected Route 35 & 36. Bug Catching Contest (Tue/Thu/Sat).

## Phone Log
- Hiker Anthony: Reported Dunsparce swarm in Dark Cave.
- Youngster Joey: Ready for rematch on Route 30.

## Elite Four Strategy
- **Will, Koga, Bruno:** Defeated.

- **Karen (Dark):** Fighting/Bug weakness. Paprika brute force. Watch out for Houndoom (Fire/Dark).
- **Lance (Dragon):** Rock/Ice weakness. Basalt (Rock) and Paprika (Fire) are key.
- **Protocol:** Heal to 100% between battles. Use Super Potions to save Full Restores.
- **Lesson:** ALWAYS set `autopress_buttons: true` for custom tools returning buttons.

## Fly Map Mechanics
- **Navigation:** The Fly map cursor navigation is list-based. **UP moves Forward** (New Bark -> Cherrygrove), **DOWN moves Backward**.
- **Order:** New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Lake of Rage -> Blackthorn -> Mt. Silver.

## Cianwood & Mahogany (Cleared)
- **Cianwood:** Chuck Defeated. Pharmacy has SecretPotion. Photo Studio at (9, 31).
- **Mahogany:** Pryce Defeated. Rocket Base Cleared.
- **Mechanics:** Persian Statues = Security Cameras (Battle Loop).

## Team Rocket Base (Archived)
- Cleared. HM06 obtained.
- **Lesson:** 'Wiggle' to reset facing if interaction fails. Phone calls pause movement (press B). Simple emojis only for markers.

## Goldenrod Notes (Archived)
- Cleared Radio Tower and Underground.
- Team Rocket Disbanded.

## Tin Tower (Paused)
- **Status:** Access to 2F requires Rainbow Wing.
- **Requirement:** Catch all 3 Legendary Beasts (Raikou, Entei, Suicune) to prove worthiness.
- **Next Step:** Restock balls at Mart and start the hunt.
- **Sages:** Spoken to all.
- **Mechanic Confirmed:** 'Scoot' principle (leaving and re-entering map) successfully refreshed map state and moved Sages.
### Archived Notes
- **Ice Path:** Cleared. Puzzles solved using boulder drops.
- **Tools:** `select_move` updated to handle persistent cursor.
## Blackthorn (Cleared)
- Badge & Dratini obtained. Move Deleter at (9, 31).

## Route 26 Progress
- Defeated Fisher Scott (Seaking Lv34, Qwilfish x2 Lv30).
- Received call from Picnicker Gina (Route 34): Has a gift for me (Leaf Stone/etc likely).
  - Psychic Richard (Espeon Lv36) at (13, 79). Defeated.
  - Reached House at (15, 57). Investigating.
## Lessons Learned
- **Menu Navigation:** Blind sequence inputs in menus are unreliable due to state latency. Verify cursor state step-by-step using screen text.
- **Victory Road Navigation:** Ridge at Y=12 blocked South->North at X=9,10,11. Pit seen at (0,11) but currently unreachable from South.
## Trainer Rosters
### Rival Silver (Victory Road)
- Sneasel (Lv34)
- Feraligatr (Lv38)
- Golbat (Lv36)
- Haunter (Lv35)
- Kadabra (Lv35)
- Magneton (Lv34)
### Elite Four Strategy
- **Will:** Slowbro is a tank (Amnesia/Curse). Counter: Smokescreen (-6 Acc) + Swift. Heal aggressively.
- **General:** Keep Paprika healthy. Revive spam if needed.
- **Tool Usage:** Always set `autopress_buttons: true` for custom tools returning buttons.
- **Menu Navigation:** Item lists are not strictly alphabetical. New items (like those bought at Indigo Plateau) may appear at the bottom. Always scroll down if an item is missing.
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