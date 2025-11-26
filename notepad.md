# Gem's Pokémon Crystal Journey

## Current Goals
- [ ] Rescue Director in Underground Warehouse (Current)
- [ ] Defeat Team Rocket

## Status
- **Location:** Goldenrod Underground (Behind Counters).
- **Objective:** Find Director or Key Items. Return to Switch Room if dead end.
- **Current Switch State:** [ON, OFF, ON] (S1, S2, S3).
- **Key Finding:** This state opens the path to the West Room South, but it appeared to be a dead end. Re-investigation required.

## Switch Puzzle Analysis (Goldenrod Underground)
**Goal:** Open Path South (Inner Shutter 16,10 or Bottom Middle 10,10).

**Verified States:**
1. **[OFF, OFF, ON]:** Top West OPEN. Top East, West Connector, Bottom West CLOSED.
2. **[ON, OFF, ON]:** Top West OPEN. Top East, West Connector, Bottom West CLOSED.
3. **[ON, OFF, OFF]:** Top East OPEN. Inner Shutter CLOSED. (Verified).
4. **[ON, ON, OFF]:** Top East & Top West OPEN. Inner Shutter & Bottom West CLOSED. (Verified).
5. **[ON, ON, ON]:** Top East & Top West OPEN. West Connector (6, 9) & Bottom West (3, 10) CLOSED.
6. **[OFF, ON, ON]:** Testing next. Hypothesis: Opens West Connector or Bottom West.

**Historical Notes (May need re-verification):**
- [ON, ON, OFF]: Top Middle & East Connector OPEN.
- [OFF, ON, OFF]: West Connector OPEN.
- [OFF, ON, ON]: West Connector CLOSED.

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
- Verified State [ON, OFF, ON]: Top West OPEN, West Connector CLOSED (6,9), Bottom West CLOSED (3,10). This state allows entry to West Room but no exit South or East.