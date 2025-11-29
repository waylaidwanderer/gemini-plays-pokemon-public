# Gem's Pokémon Crystal Journey

## 📍 Current Status: Blackthorn City
- **Location:** Blackthorn City Pokémon Center.
- **Goal:** Defeat Gym Leader Clair.
- **Current Task:** Defeat Gym Leader Clair.
- **Status:** Inside Blackthorn Gym 1F.
- **Recent Progress:** Arrived in Blackthorn via Ice Path.
- **Notes:** Need to find Move Deleter.

## Route 44
- **Trainers:**
  - Psychic Phil (Natu Lv24, Kadabra Lv26) at (8, 9). Defeated.
  - Fisher Edgar at (19, 13). Defeated.
  - Cooltrainer Cybil (Butterfree Lv25, Bellossom) at (27, 14). Defeated.
  - Cooltrainer Allen (Charmeleon Lv27) at (37, 15). Defeated.
  - Bird Keeper Vance (Pidgeotto x2 Lv25) at (51, 6). Defeated.
- **Items:**
  - Max Repel (14, 9). Picked up.

## 🎯 Goals
- [x] Restock Poké Balls (40 Great Balls bought).
- [x] Catch a Pokémon that can Fly (Vortex caught).
- [x] Retrieve item from Gina (Route 34) - Checked, nothing yet.
- [ ] Catch Legendary Beasts (Need Rainbow Wing).

## Radio Tower Infiltration (Cleared)
- **Status:** Team Rocket disbanded. Executives defeated.
- **Key Item:** Clear Bell obtained from Director.
- **Next Step:** Exit tower and fly to Ecruteak.

## Completed Areas Summary
- **Johto West:** Cleared Ecruteak, Goldenrod, Olivine, Cianwood Gyms. Burned Tower cleared. Lighthouse cleared.
- **Mahogany Area:** Cleared Team Rocket Base. Defeated Gym Leader Pryce.

## Quest Log
- **Badges:** Zephyr, Hive, Plain, Fog, Storm, Mineral, Glacier.
- **Recent Events:**
  - Defeated Red Gyarados. Obtained Red Scale.
  - Stopped Team Rocket radio signal.
  - Defeated Pryce. Earned Glacier Badge and TM16.
  - Picnicker Gina reported Team Rocket takeover of Goldenrod Radio Tower.
  - Learned Director is on 5F with Card Key.
  - Defeated Pokemaniac Donald in Underground.
  - Defeated Super Nerd Teru.
  - Found Coin Case.
  - Defeated Pokemaniac Isaac.
  - Defeated Super Nerd Eric.

## Global Game Mechanics
### General Mechanics
- **'Scoot' Mechanic:** Leaving and re-entering a map is a verified method to refresh the map state and advance puzzles (e.g., moving NPCs) after a trigger event.
- **Warp Verification:** The Game State 'Warps' list is the absolute source of truth. If a tile is not listed there, it is NOT a warp, regardless of visual cues or 'system warnings' (which may be hallucinations).

### Tile Mechanics
- **FLOOR:** Walkable.
- **WALL:** Impassable.
- **PIT / HOLE:** Traversable warp.
- **ICE:** Slippery. Slide until hitting a wall or non-ice tile.
- **LEDGE_HOP_DOWN:** One-way jump South.
- **LEDGE_HOP_LEFT:** One-way jump Left. Acts as a reset on Map 3_64.
- **ROCK:** Breakable (Rock Smash).
- **BOULDER:** Pushable (Strength).
- **WARP_CARPET:** Walk off map to exit.

### Battle Mechanics
- **Main Battle Menu:** ALWAYS use the `select_battle_option` tool. Never use raw directional inputs.
- **Move Selection Menu:** ALWAYS use the `select_move` tool. It automatically handles cursor position and button presses.
- **Switch Prompt:** Defaults to YES. Press B to decline safely.
- **Accuracy Debuffs:** Effective vs strong opponents (e.g. Smokescreen).

## Strategy Notes
- **Puzzle Lesson:** 'Scoot' means you must leave the map area entirely to allow the game state to update (e.g. NPCs moving objects). Confirmed: Leaving Tin Tower refreshed the map and moved the Sages, advancing the puzzle.
- Team Strategy: Paprika (Typhlosion) is the carry and current lead. Basalt (Geodude) has Magnitude.
- Protocol: Mark NPCs immediately. NEVER delete markers for defeated trainers; they remain as solid obstacles. Mark as 'Defeated'.
- **Position Verification:** When movement is interrupted (e.g. by new object), immediately check actual coordinates. Do not assume movement completed.
- **Screen Text:** Trust visual evidence (Screen Text) over system notes if they conflict. Text can persist or trigger unexpectedly.
- Record new Pokémon discoveries immediately, even during battle.
- Always verify object existence before interacting.
- **NPC Interaction:** Use `stun_npc` on moving NPCs to ensure successful interaction.
- **Smokescreen Survival:** Against stronger/type-advantaged opponents, stacking accuracy debuffs is a verified survival strategy.
- **Marking Protocol:** Mark objects *immediately* upon sighting to capture their ID.
- **Sprite Deception:** NPCs may use sprites that don't match their trainer class (e.g. Hiker Benjamin looked like a Pokefan). Always verify identity via interaction or battle.
- **Security Cameras:** Confirmed: Passing Persian statues/cameras triggers 'Intruder alert!' and summons Rocket Grunts. Each statue likely has a line of sight trigger.

## National Park (Cleared)
- Connected Route 35 & 36. Bug Catching Contest (Tue/Thu/Sat).

## Phone Log
- Hiker Anthony: Reported Dunsparce Swarm in Dark Cave.
- Youngster Joey: Wants to battle on Route 30.

## PC Storage
- Briar (Nidoran♀) Lv12 [National Park]

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
### Tool Lessons
- **Robustness:** For obstacle detection, use substring matching (e.g. "TREE" in type) to handle variants like HEADBUTT_TREE.
- **Inventory Sorting:** TMs are listed numerically first, with HMs appearing at the bottom of the list (after the last TM).
- **Ice Physics:** When implementing ice sliding logic, ensure the transition from non-ice to ice is treated as the start of a slide immediately upon entry, not as a single step.
- **Item Found:** HM07 (Waterfall) at Ice Path 1F (North-East).
- **Exploration:** Fell through ice hole at (12, 12) to new area (Map 3_63 top-left).
- **Inventory:** Freed space by tossing Antidotes. Ready to pick up item at B2F (0, 2).
- Puzzle B2F Center: Dropping from B1F(11,2) lands at (11,4). Sliding DOWN escapes to perimeter (Fail). Must try sliding LEFT or RIGHT next.
### Lessons Learned
- **Tool Safety:** ALWAYS set 'autopress_buttons: true' for movement tools. Verify movement occurred before assuming success.
- Dropped from B1F (4, 7) -> Landed at B2F (4, 6). (4, 6) is solid ice. Sliding Down to test path.
### Ice Path Puzzle Update
- B2F Perimeter Loop: Confirmed that drops from (11,2), (5,12), and (4,7) lead to the outer loop.
- Solution Plan: Push boulders into pits on B1F to create stop points on B2F.
- Boulder 4 (Current: 15, 12): Push Down to (15, 13) -> Push Left into Pit (12, 13).

### Lessons Learned
- **Tool Safety:** Always double-check syntax when editing tools. A crash causes position hallucinations.
- **Boulder Mechanics:** Use `sequence_press` for pushing. Ensure Strength is active. Pushing requires moving INTO the boulder.
- Boulder 2 (Moved): Pushed to (11, 8) to clear path.
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