# Gem's Pokémon Crystal Journey

## Current Goals
- [ ] Rescue Director in Underground Warehouse (Current)
- [ ] Defeat Team Rocket

## Status
- **Location:** Goldenrod Dept Store B1F.
- **Objective:** Rescue Director (Underground Warehouse).
- **Switch State:** [ON, ON, ON] (Lockdown).
- **Action:** Take Elevator to B1F and search for Warehouse entrance.
- **Verified Mechanics:**
  - S1 ON = East Wall (16, 6) CLOSED, Middle Path (10, 6) CLOSED.
  - S1 OFF = East Wall (16, 6) OPEN.
  - S3 ON = Lockdown (Hypothesis: Opens Emergency Shutter).
- **Plan:** Turn S3 ON. Check Emergency Shutter (16, 10).

## Switch Puzzle Analysis
**Goal:** Access Emergency Switch (20,11) in South East Section.

**Current State:** [ON, ON, ON] (Lockdown Mode).

**Verified Mechanics:**
- **Switch 1 (East):** ON = Closes East Wall (16,6). OFF = Opens East Wall.
- **Switch 2 (Middle):** ON = Opens Middle Path (10,7) (unless overridden).
- **Switch 3 (West):** ON = Lockdown. Closes West (3,6), Middle (10,6), and East (16,6) walls.

**Strategy:**
- **Hypothesis:** Lockdown Mode (S3 ON) opens the Emergency Shutter (16,10).
- **Problem:** Lockdown closes all northern entrances.
- **Solution:** Approach the Emergency Shutter from the South.
- **Plan:**
  1. Exit via NE Ladder (23, 3) to Goldenrod Underground.
  2. Locate the southern entrance to the Switch Room (likely connected to the "Unexplored Door" at 22,10).

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
### Tile Mechanics
- **FLOOR:** Walkable. Standard movement.
- **WALL:** Impassable.
- **PIT / HOLE:** Traversable warp. Falling in warps player to the floor below. Essential for some puzzles.
- **INVISIBLE_FLOOR (Ecruteak Gym):** Traversable only on specific tiles. Stepping on the wrong tile warps player to start. Safe path must be discovered.
- **LEDGE_HOP_DOWN:** Walkable only from the tile directly above. Acts as a WALL from all other directions. Automatically jumps the player down one tile.
- **FLOOR_UP_WALL:** Visual ledge that acts as a solid WALL. Cannot be jumped over. Treat as an obstacle.
- **HEADBUTT_TREE:** Impassable. Treated as a solid obstacle.
- **TALL_GRASS / LONG_GRASS:** Walkable. Contains wild Pokémon encounters.
- **WARP_CARPET (DOWN/UP/LEFT/RIGHT):** Walk 'off' the map edge in the direction of the carpet to exit. Merely standing on the tile is insufficient.
- **DOOR / LADDER / STAIRS / CAVE:** Walk onto to warp to a new area or floor.
- **COUNTER:** Impassable. Interact with NPCs from the adjacent tile facing the counter.
- **PC / SIGNS / HOUSE_OBJECTS:** Impassable. Includes Bookshelves, TVs, Radios, Windows, etc. Interact from adjacent tile.
- **FAKE_HOLE:** Tiles appearing as holes/warps in Burned Tower B1F (e.g. 10,8) are traversable floors. Verify with Game State Warps list.
- **WATER:** Traversable using Surf. Contains wild Pokémon and Swimmers.
- **WHIRLPOOL:** Impassable obstacle. Requires HM Whirlpool to cross (Hypothesis).
- **BUOY:** Impassable obstacle. Forms barriers on sea routes. Look for gaps.
- **ROCK:** Impassable obstacle. Treated as a solid object.
- **SECURITY_CAMERA (Persian Statue):** Impassable WALL. Triggers infinite alarm battles if player crosses its line of sight (specific columns/rows). Must be disabled.
- **ICE:** Slippery. Stepping onto this tile forces the player to slide in the direction of movement until colliding with a WALL, OBJECT, or landing on a non-ICE tile.

### Battle Mechanics
- **Main Battle Menu:** ALWAYS use the `select_battle_option` tool. Never use raw directional inputs.
- **Move Selection Menu:** ALWAYS use the `select_move` tool. It automatically handles cursor position and button presses.
- **Switch Prompt:** Defaults to YES. Press B to decline safely.
- **Accuracy Debuffs:** Effective vs strong opponents (e.g. Smokescreen).

## Strategy Notes
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
- Hiker Anthony: Mentioned wild Geodude appearing often (Swarm?).
- Youngster Joey: Wants to battle on Route 30.

## PC Storage
- Briar (Nidoran♀) Lv12 [National Park]

## Fly Map Mechanics
- **Navigation:** The Fly map cursor navigation appears to be list-based (cycling through towns in a specific order: New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Lake of Rage -> Blackthorn -> Mt. Silver) rather than purely spatial. Use UP/DOWN to cycle efficiently.

## Route 37
- **Status:** Exploring. Heading North to Ecruteak.
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
- **Status:** Exploring North towards Lake of Rage.
- **Geography:** Route connecting Mahogany Town and Lake of Rage.
- **Signs:** (11, 49) - Route 43 Sign.

## Olivine Lighthouse (Cleared)
- **Summary:** Delivered SecretPotion to Jasmine. 
- **Puzzle Solution:** To reach top: 5F West Ladder -> Drop into Pit (16,7) -> Walk North to Pit (8,3) -> Climb Central Ladders.
- **Items:** TM34 (Swagger), Super Repel.

## Route 40
- **Status:** Surfing South to Cianwood.
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
- Verified State [ON, OFF, ON]: Top West CLOSED (Trap). Top East CLOSED. Bottom West CLOSED. (Correction: Trap State confirmed).
Verified [OFF, OFF, OFF]: Top West OPEN. Top East & Top Middle CLOSED. Bottoms UNKNOWN.
Verified [OFF, OFF, ON]: Top West OPEN. Bottom West CLOSED.
Status Update: Verified [OFF, OFF, ON] causes Lockdown (West & East Walls CLOSED). Switch 3 ON overrides S2. Returning to [OFF, OFF, OFF] to test West Wall entry.
### Puzzle Solution Plan (Trap Theory)
Target State: [ON, OFF, ON]
Logic: Closes Top East (Entrance), Opens Bottom East (Goal).
Sequence:
1. Turn S1 ON -> [ON, OFF, OFF]
2. Turn S3 ON -> [ON, ON, ON] (Linkage forces S2 ON)
3. Turn S2 OFF -> [ON, OFF, ON] (Trap State)
### Verified Puzzle Rules
1. **Linkage:** Turning Switch 3 ON automatically turns Switch 2 ON.
2. **Inverse Hypothesis:** The Bottom East Shutter (Goal) likely opens when the Top East Shutter (Entrance) closes. This requires the state [ON, OFF, ON].
- **Correction:** Warp at (21, 31) is blocked by a wall. Correct exit from 'Behind Counters' is (21, 29).
### Reflection (Turn 9823)
- **Lesson:** Game State data is the source of truth. Critique suggested a warp at (21, 29) which does not exist. Always verify.
- **Warp Anomaly:** Warp Carpets at (21, 31) and (22, 31) are blocked by WALL tiles at y=32. Standard 'walk off' mechanic fails. Hypothesis: Wall might be a trigger or these are entrances only.
- **Correction:** Switch Room NE (via Ladder) is a verified Dead End.
## Warp Verification Checklist (Goldenrod)
- [x] (5, 25): Bill's House (Verified)
- [ ] (15, 27): Marked 'Pokémon Center'
- [x] (24, 27): Dept Store (Verified)
- [ ] (29, 29): Bike Shop
- [ ] (31, 21): Unknown House (High Priority - TARGET)
- [ ] (33, 9): Unknown House (Guarded by Grunt)

**Coordinate Theory:** West Shaft exit is x=11. East Shaft is ~19 tiles east in dungeon, so exit should be ~x=30 in City.
- **Goldenrod City West:** Verified cul-de-sac. Blocked East by Rocket Grunt (16, 23) and walls. Blocked North by Game Corner. Must use Underground to reach East side.
- **Goldenrod City:** Verified (5, 25) is Bill's House (Dead End).
- **Lesson:** Warp Carpets often require walking INTO the wall below/beside them to trigger. Merely standing on them is insufficient.
- **Switch Room Strategy:** West Shaft exits to Goldenrod City (Dead End). Primary target: Door at (22, 10) in Main Underground (Map 3_53). This is the most likely entrance to the Central/East Switch Room.
- Verified Switch Room NE (23,3) is a dead end. Returning to Goldenrod City to check Unknown House at (24, 27).
**Mechanics Update:**
- **Switch 1 (ON):** Opens East Wall (16, 6-7).
- **Switch 2 (ON):** Opens West Wall (3, 6-7).
- **Switch 3:** TBD.
- **Observation:** Switch 3 ON closes East Wall (16, 6) even if Switch 1 is ON.
- **Plan:** Test `[OFF, ON, ON]`. Step 1: Turn S2 ON to ensure West Exit.
- **Observation:** In `[ON, ON, ON]`, East Wall (16, 6) CLOSED. S3 appears to override S1.
- **Current Task:** Inspecting West Wall (3, 6) to see if S3 also overrides S2.

**Deduction & Plan (Turn 9994):**
- **Logic:** S1 ON closes Shutter -> Must be OFF. S1 OFF closes East Wall -> Must use West Wall (S2 ON). S3 ON closes Connector -> Must be OFF.
- **Target Config:** `[OFF, ON, OFF]`.
1. Turn S3 OFF.
2. Turn S1 OFF.
3. Verify S2 is ON.
4. Enter via West Wall -> Connector -> Shutter.

**Logic Puzzle Solution (Agent):**
Target Configuration: `[OFF, ON, OFF]`.
- S3 OFF: Keeps Connector Open.
- S2 ON: Opens West Wall (Access).
- S1 OFF: Opens Bottom East Shutter (Goal).
**Switch Puzzle Analysis**
**Status:** Locked out by S3 ON (Lockdown). Northern paths closed.
**Dead Ends Verified:**
- SE Shaft (21, 25): Dead end. Exits to City.
- SW Shaft (5, 25): Dead end. Exits to City.
- Door at 3_53 (18, 6): Loop to Behind Counters.
**Strategy:**
- Investigate Unknown Houses in Goldenrod City ((33, 9) and (31, 21)).
- If blocked by Grunts, re-enter Underground via (9, 5) -> SE Shaft -> Main Underground.
- Return to Switch Room (North) and test [OFF, OFF, OFF] configuration.
- Hypothesis: S1 OFF (Wall Open) + S2 OFF (Middle Closed) might Open Shutter.