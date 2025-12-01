# Gem's Pokémon Crystal Journey

## 📍 Current Status: Route 6
- **Location:** Route 6 (South Entrance).
- **Status:** Defeated Lt. Surge. Thunder Badge obtained.
- **Current Objective:** Find alternate route (Underground Path?) or solve Power Plant crisis.
- **Blockade:** Saffron Gatehouse (17, 4) blocked by Pokefan M. "Road closed until Power Plant problem is solved."
- **Map Notes:**
  - 12_1: Route 6. Building at (6, 1) is Saffron Gate. Underground Path blocked at (17, 4). Saffron likely closed.
  - 12_12: Route 6 Saffron Gate. Officer at (0, 4).
  - 12_3: Vermilion City. Gym (Thunder Badge), PC, Mart, Port.
- **Team:** Paprika (Lv64), Basalt (Lv17), XQH (Lv6), F (Lv8), Vortex (Lv16), Bahamut (Lv15).

## Kanto Campaign
- **Objective:** Obtain Kanto Badges.
- **Next Step:** Explore Vermilion City.

## Johto Campaign Summary (Completed)
- **Status:** Johto League Champion. All 8 Badges obtained. Team Rocket Disbanded.
- **Key Feats:** Red Gyarados, Radio Tower, Lighthouse, Dragon's Den, Elite Four Defeated.

## Quest Log
- **S.S. Aqua Quest:** Find the Gentleman's missing granddaughter.
  - **Status:** FOUND THEM! Captain (3, 25) and Twin (2, 25) are at the north end of the Captain's Cabin (15_6). Previous check missed them due to obstacles.
  - **Clue:** Sailor in Engine Room (30, 6) said she went "South".
  - **Lesson:** Always check the entire room, even if parts are blocked.

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
- **ROCK:** Breakable (Rock Smash).
- **BOULDER:** Pushable (Strength).
- **WARP_CARPET:** Walk off map to exit.
- **LADDER:** Traversable warp.
- **WARP_CARPET_DOWN:** Walk Down to warp.
- **STAIRCASE:** Traversable warp.

### Battle Mechanics
- **Main Battle Menu:** ALWAYS use the `select_battle_option` tool. Never use raw directional inputs.
- **Move Selection Menu:** The menu is a vertical list. The `select_move` tool has been updated to handle this correctly.
- **Switch Prompt:** Defaults to YES. Press B to decline safely.
- **Accuracy Debuffs:** Effective vs strong opponents (e.g. Smokescreen).
- **Type Effectiveness:** Fire is 0.5x effective against Water/Ground (not 0.25x).
- **Weather:** Rain Dance reduces Fire-type damage by 50%.

## Strategy Notes
- **Dragon's Den:** Cleared. Bahamut (Dratini) obtained. Found Dragon Fang.
- **Surfing Navigation:** When surfing, pathfinding tools must explicitly treat land tiles as obstacles (unless it's the target tile) to prevent accidental dismounting during travel.
- **Puzzle Mechanics:** 'Scoot' (leaving/re-entering map) refreshes map state/NPCs.
- **General Protocol:** Mark NPCs immediately. Keep markers for defeated trainers. Verify position after interruptions. Trust visual Screen Text.
- **Sprite Deception:** NPCs may use misleading sprites (e.g. Hiker as Pokefan).
- **Security Cameras:** Persian statues trigger alarms (Rocket Base).
- **Inventory:** In-game list order differs from Game State list.
- **Team:** Paprika (Typhlosion) lead. Basalt (Geodude) backup.

## National Park (Cleared)
- Connected Route 35 & 36. Bug Catching Contest (Tue/Thu/Sat).

## Phone Log
- Hiker Anthony: Reported Dunsparce swarm in Dark Cave.
- Youngster Joey: Wants to battle on Route 30.

## Elite Four Strategy
- **Will, Koga, Bruno:** Defeated.

- **Karen (Dark):** Fighting/Bug weakness. Paprika brute force. Watch out for Houndoom (Fire/Dark).
- **Lance (Dragon):** Rock/Ice weakness. Basalt (Rock) and Paprika (Fire) are key.
- **Protocol:** Heal to 100% between battles. Use Super Potions to save Full Restores.
- **Lesson:** ALWAYS set `autopress_buttons: true` for custom tools returning buttons.

## Fly Map Mechanics
- **Navigation:** The Fly map cursor navigation is list-based. **UP moves Forward** (New Bark -> Cherrygrove), **DOWN moves Backward**.
- **Order:** New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Lake of Rage -> Blackthorn -> Mt. Silver.

## Route 37
- **Status:** Traversed.
- **Trainers:**
  - Psychic Greg (Drowzee Lv17) at (6, 6). Defeated.
- **Geography:** Short route connecting Route 36 and Ecruteak City.
- **Apricorns:** Suspected 'Weird Trees' (Red/Blue/Black Apricorns usually found here).
- **Observed Movesets:**
  - **Drowzee (Lv17):** Hypnosis.
- **Lesson:** Always verify specific tile mechanics (e.g. directional ledges) are explicitly coded in pathfinding tools to avoid invalid paths.
- **Tool Usage:** Always remember to set `autopress_buttons: true` when using custom tools that return button sequences.

## Burned Tower (Archived)
- Cleared. Rival defeated. Beasts released.
- **Key Lessons:**
  - **Action is Truth:** Never assume a tool is updated unless the `tool_code_updated` message appears.
  - **Wild Escapes:** Escape probability increases with failed attempts.
  - **Fake Hazards:** Some visual holes (e.g. Burned Tower B1F 10,9) are safe. Verify with Game State.

## Route 38
- **Status:** Cleared.
- **Trainers:** Sailor Harry, Lass Dana, Beauty Olivia (Defeated).
  - Schoolboy Chad (Mr. Mime Lv19) at (4, 1). Defeated.
  - Bird Keeper Toby (Doduo x3) at (12, 15). Defeated.
- **Geography:** Southern path (Row 16) dead-ends at x=4.
- **Lore:** Olivia mentions Moomoo Milk. Farm likely nearby.

## Route 39
- **Status:** Arrived from Route 38 (East).
- **Geography:** Route connecting Ecruteak/Route 38 to Olivine City.
- **Landmarks:** Sign at (15, 7).
- Defeated Pokefan Ruth (Pikachu Lv17) at (14, 19).
- Defeated Pokefan Derek (Pikachu Lv17) at (10, 19).
- Farmhouse: Pokefan F mentions milk is shipped to Kanto.
- Quest: Feed Berries to sick Miltank in Barn. (Status: Paused. Requires standard 'BERRY' item. 2 fed so far. Needs more.)

## Olivine City (Completed)
- **Status:** Cleared. Mineral Badge obtained.
- **Key Events:**
  - Jasmine cured (SecretPotion delivered).
  - Mineral Badge obtained.
  - HM04 Strength obtained.
  - Good Rod obtained.

## Route 42 & Mt. Mortar (Traversed)
- **Status:** Traversed East to Mahogany.
- **Key Events:** Defeated Pokemaniac Shane, Hiker Benjamin. Paprika Lv41.
- **Geography:** Mt. Mortar entrances at (3, 33), (11, 21).
- **Items:** Ultra Ball.

## Route 43
- **Status:** Traversed.
- **Geography:** Route connecting Mahogany Town and Lake of Rage.
- **Signs:** (11, 49) - Route 43 Sign.

## Olivine Lighthouse (Cleared)
- **Summary:** Delivered SecretPotion to Jasmine. 
- **Puzzle Solution:** To reach top: 5F West Ladder -> Drop into Pit (16,7) -> Walk North to Pit (8,3) -> Climb Central Ladders.
- **Items:** TM34 (Swagger), Super Repel.

## Route 40
- **Status:** Traversed.
- **NPCs:**
  - Silver (14, 15) - Passive.
  - Silver (18, 30) - Sighted.
- **Geography:** Sea route connecting Olivine to Cianwood.
- **Objects:** Sign (14, 10), Rocks at (6,9), (7,8), (7,11).
- **Trainers:**
  - Swimmer Elaine (Staryu Lv21) at (5, 19). Defeated.
- **BUOY:** Impassable obstacle.
- **Lesson:** Navigation tools must explicitly check player state (e.g., surfing) to correctly identify traversable tiles like WATER.

## Route 41 (Cleared)
- Traversed sea route to Cianwood.
- Defeated Swimmers Charlie, Susie, Kirk, Wendy.

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
## Tool Reference
- **find_path**: Custom tool for pathfinding. Handles obstacles and surfing penalties.
- **attempt_surf**: Standardized surfing interaction sequence.
- **select_move**: Automates battle move selection.
- **sequence_press**: Executes button sequences.
- **scan_unseen**: Scans for reachable unseen tiles.

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
### Rival Silver (Victory Road Exit)
- Sneasel (Lv34)
- Feraligatr (Lv38)
- Golbat (Lv36)
- Haunter (Lv35)
- Kadabra (Lv35)
- Magneton (Lv34)
### Elite Four Strategy
- **Will:** Slowbro is a tank (Amnesia/Curse). Counter: Smokescreen (-6 Acc) + Swift. Heal aggressively.
- **General:** Keep Paprika healthy. Revive spam if needed.
- **Tool Usage:** Always set `autopress_buttons: true` for custom tools that return button sequences.
- **Menu Navigation:** Item lists are not strictly alphabetical. New items (like those bought at Indigo Plateau) may appear at the bottom. Always scroll down if an item is missing.
## Recent Victories
- **Champion Lance:** Defeated.
- **Lt. Surge:** Defeated. Strategy: Paprika (Swift/Flamethrower) swept. Light Screen ignored by Gen 2 Swift (Physical).
- **Quest Update:** Found Clefairy Doll in Vermilion Fan Club. Must trigger quest at Copycat in Saffron first to pick it up.
- **Route 6:** Path to Saffron Gatehouse is blocked by a Pokefan M at (17, 4). Nearby sign for Underground Path.