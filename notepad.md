# Gem's Pokémon Crystal Journey

## 📍 Current Status: Cerulean Gym
- **Location:** Cerulean Gym. Surfing at (3, 2).
- **Goal:** Locate Machine Part. Systematic search of pool.
- **Sequence:** Surfing at (4, 2). Checking surroundings then moving to (5, 2).
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
- **Main Battle Menu:** ALWAYS use the `select_battle_option` tool. Never use raw directional inputs.
- **Move Selection Menu:** The menu is a vertical list. The `select_move` tool has been updated to handle this correctly.
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

## Western Johto (Archived)
- Cleared: R37, Burned Tower (Beasts released), R38, R39, Olivine (Mineral Badge).

## Mid-Game Johto (Archived)
- **Traversed:** Route 42 (Mt. Mortar), Route 43, Route 40, Route 41.
- **Cleared:** Olivine Lighthouse (Jasmine healed).
- **Key Notes:** Route 40 BUOYS are impassable obstacles. Navigation tools must check surfing state.

## Cianwood City
- **Gym:** Leader Chuck (Fighting). Weak to Psychic.
- **Puzzle:** Requires Strength to move boulders.
- **Gym Guide:** Warns of bullies.
- **Pharmacy:** Acquired SecretPotion.
- **Navigation Protocol:** Always step 1 tile away from warps before pathfinding.
- **Cianwood Photo Studio:** Located at (9, 31). Not the Gym.
- **Cianwood Event:** Encountered Suicune at (10, 14), but it fled. Eusine appeared and challenged me to a battle to earn Suicune's respect.
- Defeated Eusine (Drowzee Lv23, Electrode Lv25, Haunter Lv23).

## Mahogany Town Info
- **Status:** Safe. Team Rocket defeated.
- **Gym:** Leader Pryce (Ice) Defeated.
- **Mechanic Confirmed:** Persian Statues contain security cameras. Crossing their line of sight triggers Rocket Grunt battles.
- **Objective:** Continue adventure.
- **Trap Warning:** The security cameras in Team Rocket Base B1F (e.g., at 6,1) create an infinite loop of battles if you remain in their line of sight. You must move immediately after a battle ends.
- **Floor Traps:** A Grunt warned of traps set in the floor. Proceed with caution.

## Team Rocket Base (Cleared)
- **Summary:** Cleared B1F, B2F, B3F. Defeated Executives. Stopped Radio Signal.
- **Key Items:** HM06 Whirlpool obtained from Lance.
- **Traps:** Floor traps on B1F. Security cameras on B1F.
- **Passwords:** SLOWPOKETAIL, RATICATE TAIL, HAIL GIOVANNI.
- **Interaction Fix:** If an interaction fails despite correct positioning, try a 'wiggle' maneuver (move away and back) to reset the facing/state.
- **Phone Calls:** Receiving a call stops movement and leaves a text box open. MUST press 'B' to clear it before moving again.
  - Defeated Pokemaniac Isaac.
  - Defeated Super Nerd Eric.

- **Lesson:** Map marker emojis must be simple single characters. Complex emojis (like '🧑‍🦰') cause tool failures.
- Switch Mechanics: Verified complex interactions between S1, S2, and S3. S3 often acts as a reset or trap trigger.

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
## Blackthorn City
- **Landmarks:**
  - Sign at (34, 24): "Blackthorn City - A Quiet Mountain Retreat"
  - Emy's House at (29, 23)
- **Trade:** Lass in Emy's House wants a female Dragonair (DRAGONAIR♀) for a Dodrio.
- **Trainers:**
  - Cooltrainer F (Hints at Move Deleter) at (10, 25).
  - Youngster (Patrolling row 15) at (12, 15).
  - Super Nerd sighted at (19, 12).
- **Navigation:**
  - Path to Northern District via gap at (13, 17).
- **Tile Mechanics:** `FLOOR_UP_WALL` observed at (37, 20). Need to verify traversability.
## Blackthorn Dragon Speech House
- **Location:** (13, 21) in Blackthorn City.
- **NPCs:** Granny (2, 3), Dratini (5, 5).
- **Goal:** Investigate 'Dragon Speech'.
- **NPCs:**
  - Cooltrainer F (10, 25): Hints that the Move Deleter is in this city.
- **Move Deleter:** Found in house at Blackthorn (9, 31).
## Ice Path (Re-visit)
- **Warp Malfunction:** Exit at (36, 27) failed to trigger multiple times. Suspect specific trigger needed or bug.
- **Tile Mechanics:** `FLOOR_UP_WALL` observed at (32, 24). Need to verify if traversable.
- Picnicker Gina: Wants to battle on Route 34.

## Blackthorn Gym
- **Trainers:**
  - Cooltrainer Paul (Dratini x3 Lv34) at (1, 14). Defeated.
- **Exit Strategy:** The 1F south path is blocked. Must take East Ladder (7, 9) to 2F, traverse to West Ladder, and descend to (1, 7) to reach the exit.
## Dragon's Den 1F Navigation
- **Obstacle:** `FLOOR_UP_WALL` at (6, 16) is IMPASSABLE.
- **Route:** Use Ladder at (5, 13) to bypass walls and reach the exit at (3, 5).
- Prof. Elm called: Requests visit to Lab.
- Plan: Get Dratini -> Visit Elm -> Route 34 (Gina's Gift).
- **Surfing Interaction:** If pressing A or walking into water fails to trigger Surf, use the Start Menu -> Pokémon -> Surf method. It is more reliable.
- **Lesson:** Surfing interaction requires specific facing and confirmation. Pathfinding must heavily penalize dismounting unless at the specific destination to avoid 'island hopping'.
- **Correction:** Turn 15025 reported surfing at (24, 30) was a hallucination. Verify 'Standing on tile: WATER' before confirming surfing state.
- **Pathfinding Issue:** `find_path` repeatedly dismounts player when surfing in Dragon's Den. Switch to manual surfing for now.
- **Dragon's Den Exit Strategy:** Navigate West Channel (x=10). Path: Surf North to (10, 21), Clear Whirlpool at (10, 20), Exit at (20, 3).

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