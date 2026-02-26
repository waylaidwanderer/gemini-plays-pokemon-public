<h1><code>Main</code></h1>

[Location Encounters]
(Moved to Archive/LocationEncounters)

[Lessons Learned]
- Avoid over-mashing A during map transitions and battles. It causes UI desyncs, mistaken menu inputs, and turn hallucinations. Use targeted tools instead.
- Always carry Antidotes when exploring caves to prevent retreating from Poison damage.

[Timestamps]
- Start Turn: 339 (Entered Viridian Forest navigation task)
- Grinding Start: Turn 415
- Route 2 Arrival: Turn 869
- Mt. Moon Start: Turn 1385
- Cerulean City Arrival: Turn 2126
- Turn 3135: Severe spatial hallucination occurred because I ignored objective Y-coordinate data (Y=27) indicating I was at the south edge of the map, and instead trusted a flawed visual assumption. Lesson: ALWAYS trust (X, Y) coordinate math over feelings of being lost.
- Turn 3239 Reflection: Long pathing macros (walk_waypoints) are highly brittle in NPC-populated areas. Navigate step-by-step and verify 'TYPE_' collision data instead of trusting visual assumptions about fences/roofs.
- Route 24 Grinding Start: Turn 3516 (Resumed Turn 3638, Mon Feb 23 2026)
- Route 6 / Vermilion Grinding Start: Turn 4321
- S.S. Anne Boarding: Turn 4431 (Tue Feb 24 2026)
- Rival Gary Battle Start (S.S. Anne): Turn 4855

[Trades]
- Route 5 Gate (Underground Path entrance): NPC wants to trade a Nidoran F for a Nidoran M.
- Vermilion City (House next to Mart): NPC wants Spearow for Farfetch'd.

[Vermilion City]
- Fan Club: (9, 13) - Talk to Chairman for Bike Voucher.

[Plan]
- Cut the tree blocking the Vermilion Gym and challenge Lt. Surge. (Lead with Pebbles or Cleo for Electric immunity!)
- Return to Cerulean City (walk back through Route 5 Underground Path after acquiring HM01 and ship departs) to exchange Bike Voucher for Bicycle.

[Navigation Rules]
- Ledges (e.g. TYPE_44f6) enforce one-way movement. Route 5 requires looping back to the top to access the right-side lanes.
- Building identities must be verified by entering them, not by visual assumption. Saffron Gate and Underground Path are visually similar.
- Do NOT blindly trust assumed long-distance coordinate math (e.g. 'walk straight south from X'). Walk step-by-step and trace impassable tiles (water, trees) to find correct paths.
- When mapping, use exact coordinates and do not jump to conclusions about blocked paths until physically bumping into them. Use map markers to explicitly mark entrances!

[Battle Tactics]
- Switch out immediately if hit by multiple accuracy-dropping moves (like Sand-Attack) to avoid wasting turns mashing attacks that miss.
- Map markers for defeated trainers (e.g. ☠️) should ONLY be placed AFTER returning to the overworld, never during a battle, as fainting could invalidate the marker.
- Always consider enemy speed and damage rolls.

[Turn 4850 Reflection]
- STRICT RULE: If an item is not explicitly listed in the Game State Information sprite list, it DOES NOT EXIST. I wasted turns trying to pick up stools. Stop interacting with furniture.
- Fixed `swap_pokemon_party` custom tool to handle Gen 1 cursor memory.

[Rival Gary - S.S. Anne]
- Pidgeotto Lv 19
- Raticate

[Boss Prep Checklist]
- Check party HP and status conditions.
- Heal at Pokemon Center BEFORE entering known hostile or boss areas.
- Verify optimal lead Pokemon.

[S.S. Anne Navigation]
- NEVER use dead reckoning. ALWAYS read the Game State Player Position before making any navigational assumptions or using walk_to_coordinate.
[Turn 5214 Reflection: Path to S.S. Anne]
- The path to the docks is NOT near the Gym. It is on the FAR EAST side of town.
- From Pokemon Center, walk East to X=30.
- Walk South down X=30 to Y=26.
- Walk West along Y=26 to X=18.
- Walk South onto the bridge at X=18.
- NEVER ask custom agents for exact map coordinates or pathfinding instructions, as they will hallucinate them. Always manually trace collision bounds.

<hr>

<h1><code>Quests/Main</code></h1>

[Turn 201] Active Quest: Complete the Pokedex & Become Champion.
Execution Plan:
1. Head north to Viridian City and beyond.
2. Explore new routes (Route 22, Route 2) to catch new Pokemon.
3. Navigate Viridian Forest to reach Pewter City for the first Gym Badge.
[Bill's Quest]
- Status: Complete. Turned Bill back into a human using the Cell Separation System.
- Reward: S.S. Ticket (Cruise ship S.S. Anne in Vermilion City).
- Next Steps: Defeat Misty at Cerulean Gym, then find the path south to Vermilion City.

<hr>

<h1><code>Mechanics/TileCollisions</code></h1>

[Turn 79] Walkable: TYPE_3fe2 (paths/doors/grass/floor). Impassable: TYPE_2889 (buildings/fences/signs/walls).
- **TYPE_3fe2**: Walkable (Grass/Ground)
- **TYPE_2889**: Impassable (Building Wall/Sign)
- **TYPE_fed7**: Tall Grass (Wild Encounters)
- **TYPE_44f6**: Ledge (Jumpable 1-way)
[Known Tile IDs]
- TYPE_2889: Impassable tree/solid obstacle
- TYPE_44f6: One-way ledge (jump down only)
- TYPE_fed7: Walkable tall grass
- TYPE_3fe2: Walkable normal grass

[General Collision Rules]
- Map Transitions: Require specific warp tiles, gatehouse doors, or screen-edge steps.
- Impassable boundaries or signs do NOT trigger map transitions.
- TYPE_2889: Impassable tree/solid obstacle
- TYPE_44f6: One-way ledge (jump down only)
- TYPE_fed7: Walkable tall grass
- TYPE_3fe2: Walkable normal grass
- Map Transitions: Require specific warp tiles, gatehouse doors, or screen-edge steps. Impassable boundaries/signs do not trigger transitions.
[Tile Mechanics]
- TYPE_2889: Impassable tree/solid obstacle
- TYPE_44f6: One-way ledge (jump down only)
- TYPE_fed7: Walkable tall grass
- TYPE_3fe2: Walkable normal grass
- Map Transitions: Require specific warp tiles, gatehouse doors, or screen-edge steps. Impassable boundaries/signs do not trigger transitions.
[Tile Collisions]
- TYPE_2889: Impassable tree/solid obstacle
- TYPE_44f6: One-way ledge (jump down only)
- TYPE_fed7: Walkable tall grass
- TYPE_3fe2: Walkable normal grass/ground (Cave entrance tiles)
[Tile Mechanics]
- TYPE_2889: Impassable tree/solid obstacle/cave wall
- TYPE_44f6: One-way ledge (jump down only)
- TYPE_fed7: Walkable tall grass
- TYPE_3fe2: Walkable normal grass
- Map Transitions: Require specific warp tiles, gatehouse doors, or screen-edge steps. Impassable boundaries/signs do not trigger transitions.
- TYPE_de37: Impassable raised cave platform/wall
- Raised platforms (TYPE_2889 and TYPE_de37) are impassable tiles that act as walls, blocking movement. They cannot be walked over.
- TYPE_2889: Impassable ledge/wall. Blocks movement.
- TYPE_3fe2: Raised platform floor. Often inaccessible from lower floors without stairs.
- TYPE_3fe2: Regular passable ground/bridge (NOT tall grass, no encounters here).
- TYPE_44f6: Cut Tree (Impassable without HM01 Cut)

<hr>

<h1><code>Mechanics/Combat</code></h1>

[Turn 62] Combat basics: Turn-based. Type matchups are critical (e.g. Water beats Fire, Grass beats Water). STAB (Same Type Attack Bonus) applies for matching move and Pokémon types. Use FIGHT to attack, ITEM to use Potions.
- **Hydro (Squirtle)**: Learned Bubble (Water) at Level 8.
[Status Effects]
- Overworld Poison: Pokemon lose 1 HP every 4 steps in the overworld. Calculate exact step limit (Current HP * 4) to know exactly how far you can travel before panicking!
- **Menu Navigation:** In battle, if you accidentally enter the ITEM menu, you must press B to exit it, then press Up to move the cursor back to FIGHT, then A to select it. The `battle_move_selector` tool ONLY works when the cursor is already inside the FIGHT menu (showing the 4 moves). Do not mash B to back out of menus, as you might back out of the FIGHT menu entirely.
[Route 25 Enemies]
- Youngster's Lv 17 Slowpoke: Confusion deals 6-12 damage to Lv 25 Wartortle.
- Gym Leaders (e.g., Misty) actively use stat-boosting items like X Defend during battle. Plan for longer fights or bring counter-stat moves (like Tail Whip) if relying on physical damage.
- Risk Assessment: Always consider enemy speed and damage rolls. If your Pokemon is slower and can be KO'd by a high roll or crit (like Pidgey's Gust dealing 10+ damage to a 15 HP Nidoran), switch to a healthier/resistant Pokemon to secure split EXP rather than risking a faint.
- Gust is a Normal-type move in Generation 1, not Flying-type.

<hr>

<h1><code>Locations/ViridianCity_Mart</code></h1>

[Turn 241] Viridian City Poke Mart Inventory:
- Poke Ball (¥200)
- Antidote (¥100)
- Parlyz Heal (¥200)
- Burn Heal (¥250)

<hr>

<h1><code>Mechanics/Battle_Gen1</code></h1>

- "But, it failed!" refers to the move just executed by the current Pokemon (e.g., an enemy's stat-dropping move failing because the stat can't go lower, or Gen 1 AI quirks). It does NOT mean the player's previous attack missed.
[Mechanics/Combat]
- Gen 1 battle menus WRAP AROUND (pressing Down at move 4 goes to move 1).
- Cursor position is remembered per Pokemon. Must accurately track current_move_index.
- The battle cursor RESETS to index 1 in two cases:
  1. At the start of a NEW BATTLE.
  2. After a Pokemon LEVELS UP.
- It is REMEMBERED between enemy Pokemon within the SAME battle (if no level up occurred).
[Cursor Memory]
- In Gen 1, menu cursor positions are remembered! The Item menu remembers the last used item position globally. The Fight menu remembers the last used move per-Pokemon. The Party menu remembers the last selected Pokemon. ALWAYS check the visual cursor position before using navigation tools, as assuming it resets to index 1 will cause wrong selections.
- Wrap/Bind Mechanic: In Gen 1, trapping moves like Wrap completely immobilize the target. The move selection phase is skipped entirely and you cannot attack until the effect ends. Do not try to use battle menus during Wrap.

<hr>

<h1><code>Locations/PewterCity</code></h1>

[Points of Interest]
- Pokemon Center: (13, 25)
- Pewter Gym: (16, 17)
- Poke Mart: (23, 17)
[Poke Mart Inventory]
- Poke Ball: ¥200
- Potion: ¥300
- Escape Rope: ¥550
- Antidote: ¥100
[Pewter Gym Trainers]
- Jr. Trainer (at entrance): Lv 11 Diglett, Lv 11 Sandshrew
[Navigation Notes]
- Gym door (16, 17) MUST be approached from below (y=18).
- South path to Gym is blocked by trees at y=21. East path blocked by signs at x=18.
- From PC (13,25) to Gym: Up to y=18, Right to x=16, Up to door.
- From East (Mart) to Gym: Up to y=13, Left over Gym to x=14, Down to y=18, Right to door.

<hr>

<h1><code>Locations/Route3</code></h1>

# Route 3
- Located east of Pewter City, leading towards Mt. Moon.
- Features one-way ledges and patches of tall grass.
- Many trainers spotted in the area.
[Trainer Teams]
- Bug Catcher (10,6): Caterpie (Lv10), Weedle (Lv10), Caterpie (Lv10)
- Lass (15,9): Pidgey (Lv9), Pidgey (Lv9)
[Trainers]
- Bug Catcher (19, 5): Weedle (Lv 9), Kakuna (Lv 9), Metapod (Lv 9)
- Lass (near 19, 4): Rattata (Lv 10), Nidoran♂ (Lv 10)
- Bug Catcher (24, 6): Caterpie (Lv 11), Metapod (Lv 11)
- Lass (33, 9): Jigglypuff (Lv 14)
[Terrain]
- Ledges (TYPE_44f6) can only be jumped over going Down. They block Upward movement.
- Rock walls (TYPE_2889) form maze-like barriers requiring weaving up and down.

<hr>

<h1><code>Archive/ViridianForest</code></h1>

[Viridian Forest Topology]
- Entrance: (17, 47)
- Path Forward: East corridor (x=25) bypasses the solid horizontal tree line. The actual central tree boundary is at y=29.
- Dead Ends Mapped: (16, 1), (2, 30), (2, 40).
- Strategy: Return to the east path (x>17) and head north. Look for branching paths to the west.

<hr>

<h1><code>Mechanics/StatusEffects</code></h1>

[Overworld Effects]
- Poison: Pokémon loses 1 HP approximately every 4 steps taken in the overworld. Can be fatal. Cure immediately at a Center or with an Antidote.
- Poison Contingency: Do not panic. Check HP. Damage is 1 HP per 4 steps. Calculate steps to Center. Use Potion only if HP will drop below 0 before reaching the Center.

<hr>

<h1><code>Archive/LocationEncounters</code></h1>

[Location Encounters]
Route 22: Rattata, Nidoran F
Viridian Forest: Caterpie
Route 3: Spearow, Pidgey

<hr>

<h1><code>Mechanics/NPCBehavior</code></h1>

[Wandering NPCs]
- Wandering NPCs can step on and block warp tiles (like doors). If this happens, you must step back to give them space to wander off the tile before you can enter.
[Trainer Displacement]
- Trainers walk up to 1 tile towards you when they spot you.
- This can be exploited to move them out of blocking positions (e.g., to reach an item).

<hr>

<h1><code>Notes/ShoppingList</code></h1>

[High Priority]
- Buy Antidotes ASAP at the next Poke Mart. Poison damage is brutal in caves.

<hr>

<h1><code>Locations/MtMoon</code></h1>

[Mt. Moon Topology & Connections]
- Start Turn: 1385
- 1F Entrance: (14, 35) connects to Route 3.
- Ladder A: 1F (25, 15) <-> B1F (25, 15) [Leads to isolated corridor]
- Ladder B: B1F (15, 27) <-> B2F (15, 27) [Leads to B2F Dead End, HP UP, TR Grunt]
- Ladder C: 1F (5, 5) <-> B1F (5, 5) [Main path continuation]
- Ladder D: B1F (21, 17) <-> B2F (21, 17) [Main section of B2F, Super Nerd, TM01]
- Ladder E: B1F (23, 3) <-> B2F (5, 7) [Path to Exit]

[Map Boundaries & Notes]
- Encounters: Clefairy, Zubat, Paras, Geodude
- B2F: Raised platforms (TYPE_de37) block movement to western half.
- B2F: TYPE_2889 tiles act as impassable ledges/walls.
- B2F: Unreachable item ball spotted at (29, 11) on northern raised platform.
- **B2F HAZARD (The Southern Loop):** The massive southern corridor connects the far East (x=36, y=24) to the far West (x=8, y=17). It is a massive time-sink. DO NOT enter.
- 1F: Western corridor from Moon Stone (2,2) leads south.

[Route to B2F Northern Section]
1. Reach western side via the loop OR find the path from the eastern side.
2. From (8, 17) on the west side, head straight NORTH to explore the top-left quadrant of B2F.

<hr>

<h1><code>Mechanics/TrainerCompositions</code></h1>

[Trainer Compositions]
- Bug Catcher: Caterpie, Weedle, Metapod, Kakuna.
- Youngster: Rattata, Zubat, Ekans, Sandshrew.
- Lass: Pidgey, Nidoran (F/M), Clefairy, Jigglypuff.
- Super Nerd: Grimer, Voltorb, Koffing, Magnemite.
- Team Rocket Grunt: Rattata, Zubat, Sandshrew, Ekans, Machop.
[Rival Gary - Cerulean City]
- Pidgeotto (Lv 18)
- Abra (Lv 15)
- Rattata (Lv 15)
- Bulbasaur (Lv 17)

<hr>

<h1><code>Locations/CeruleanCity</code></h1>

# Cerulean City
- Arrived Turn 2126
- West: Route 4 (one-way ledges prevent returning to Mt. Moon)
- North: Route 24 (Bridge is around X=20)
- South: Route 5 (Direct path blocked by Cut Tree at 19, 28)

[Points of Interest]
- Pokemon Center: (19, 17)
- Poke Mart: (25, 25)
- Bike Shop: (13, 25)
- Gym: (30, 19)
- Trade House: (13, 15)
- Badge Info House: (9, 11)
- Robbed House (Front Door): (27, 11)
- Robbed House (Hole in back): (27, 9)

[Path to Route 5 (Bypassing Cut Tree & Ledges)]
- Objective Started: Turn 3048
1. From the Pokemon Center, bypass the one-way ledges by heading west, then north, then east across the top of the city.
2. Enter the Robbed House front door at (27, 11).
3. Inside, take the warp at (3, 0) to exit through the hole in the wall.
4. In the backyard, navigate the gaps to the main south path and enter Route 5.

[Layout Hazards]
- (13, 25) is Bike Shop. Avoid walking into the door accidentally.
- (23, 17) and (22, 17) have Cut Trees blocking horizontal movement.
- (19, 28) has a Cut Tree blocking the south exit.

[Navigation Notes]
- Route 24 Bridge is straight NORTH from (20, 17) (just right of the Pokemon Center).
- Route 5 is accessed by walking through the Robbed House (27, 11) to bypass the south Cut tree.

<hr>

<h1><code>Archive/MtMoon</code></h1>

[Mt. Moon Topology]
- Entrance: (14, 35)
- Encounters: Clefairy (Trainer), Zubat, Paras, Geodude
[Map Boundaries - Map 0_59]
- Entrance at (14, 35) connects to Route 4.
- Raised platforms (TYPE_de37, TYPE_2889) act as walls.
- Internal warps/ladders: (25,15), (15,27), (17,11), (25,9), (15,23).
- (17, 19) is a dead end bounded by ledges/walls to the south.

<hr>

<h1><code>Strategy/TeamBuilding</code></h1>

[Strategy]
- The level gap is massive. I need to either switch-train the lower level Pokemon against weaker enemies or catch new, higher-level Pokemon on Route 24/25.
- Goal: Catch a Grass or Electric type for coverage. (Caught Bellsprout!)
- If HYDRO gets too low on HP, I need to use Potions or head back to the Cerulean City Pokemon Center.
[PC Box]
- AUDREY (Bellsprout): Lv 12. Need to swap someone out to train her.
[Timestamps]
- Route 25 Trainer Maze & Switch Training Start: Turn 2461

<hr>

<h1><code>Locations/Route25</code></h1>

# Route 25
- Start Turn: 2655
- Item spotted at (22, 2). Can be accessed by luring the trainer at (24, 4) downwards.

<hr>

<h1><code>Mechanics/PC_System</code></h1>

[PC Navigation]
- To swap a Pokemon when party is full (6/6):
  1. Access PC -> Bill's PC
  2. DEPOSIT PKMN -> Select Pokemon to store -> Yes
  3. WITHDRAW PKMN -> Select Pokemon to take -> Yes
- PC menus are sensitive. Do NOT button mash. Use single A presses and verify screen state.

<hr>

<h1><code>Mechanics/Movement</code></h1>

[Movement Rules]
- Turning vs Stepping: If you change direction from a standstill, your character will "turn in place" first. This consumes an input/turn without changing your (x, y) coordinates. Account for this in long movement sequences!
- Ledges & Obstacles: Gym statues have 2-tile bases. Ledges (like the water barriers in Cerulean Gym) act as one-way drops or solid walls depending on the side. 
- ALWAYS use short, 1-3 step movements to test unfamiliar collisions before committing to long tool sequences.
[Gen 1 Movement Mechanics]
- 1st directional press turns the character in place.
- 2nd consecutive press in the same direction moves the character to the next tile.
- Custom tools MUST include a short sleep (e.g., 'sleep 150') between these presses to ensure the emulator registers them as distinct inputs, otherwise the character will just spin in place forever without triggering encounters.

<hr>

<h1><code>Mechanics/General</code></h1>

[Mechanics/LevelUp]
- Mashing B cancels move learning.
- Cascade Badge: Pokémon up to Lv 30 obey. Enables CUT outside of battle.
- TM11 (Misty): Bubblebeam.
- Nidoran F evolves into Nidorina at Level 16.

<hr>

<h1><code>Locations/Route24</code></h1>

[Encounters]
- Route 24: Caterpie, Metapod, Abra, Bellsprout.
WARNING: Bellsprout's Vine Whip is 4x effective against Geodude. Train Cleo here instead.

<hr>

<h1><code>Locations/Route5</code></h1>

# Route 5
- Located South of Cerulean City.
- Saffron City Gate: Center lane (x=10). BLOCKED by thirsty guards. (Roof starts at y=23).
- Underground Path: Far-right lane. Door is at (17, 27).
- To reach Underground Path: Exit Cerulean City at x=28 (behind Robbed House). This puts you in Route 5 at x=18. Walk straight south to the Underground Path building. A 1-way ledge at Cerulean (28, 33) prevents going back up, proving this is the correct path. Do not trust previous hallucinated notes about x=39.

<hr>

<h1><code>Mechanics/UI</code></h1>

- Item Menu: The in-game Item menu order is chronological/manual, NOT alphabetical. Do not rely on Game State inventory order for navigation.
- Cursor Memory: The PKMN switch menu and FIGHT menu remember the last selected index per session/battle. ALWAYS visually verify the starting cursor position and pass it to custom tools (current_index) to prevent wrong selections.
- Gen 1 Menu Mechanics: The party menu and start menu both feature cursor memory (opening on the last selected item) and cursor wrapping (pressing Up at the top goes to the bottom). This breaks blind navigation macros, so always do menu navigation step-by-step or use state-aware tools.
- Cursor Memory: In Gen 1, the cursor position in menus (like the Party screen) is often remembered between opens. Always verify the blinking cursor position before mashing A or using a tool, especially when returning from a sub-menu, as it might wrap or stay where it was.
- [Turn 6149 Reflection] The party menu cursor remembers its last position even when accessed from the ITEM menu. Always verify cursor position before using an item!

<hr>

<h1><code>Locations/SS_Anne</code></h1>

# S.S. Anne
- Hallway (Map 0_95): The horizontal walking path is Y=6 and Y=7. Y=8 contains alternating doors and impassable walls.
- Navigation Rule: To avoid bumping into walls, always walk horizontally on Y=6 or Y=7. Turn Down only when you are directly above the door you want to enter (Y=8).
- Coordinate mapping: Map 0_95 is the hallway, and Map 0_102 contains the individual cabin interiors.
- Map 0_100: Reached via stairs at (3, 16) on Map 0_95. This is a large open room (crew quarters/engine room) with pink/white checkerboard floors, not a hallway. Contains several Sailors.
- Trash cans checked: The two on the left side of the room are empty. The 'odd ball' might be in a different room like the kitchen.
[Cabin Clearance Checklist]
- Cabin 1: Cleared
- Cabin 2: Cleared
- Cabin 3: Cleared
- Cabin 4: Cleared
- Cabin 5: Cleared
- Cabin 6: Cleared
[Healing Plan]
- Cleo (Nidoqueen) is 23/58 HP. Hydro is 22/81 PAR. Use Potions/Antidotes as needed, or return to Vermilion Center if Cleo drops below 10 HP.
- Warp Link: Vermilion City (18, 31) connects to S.S. Anne Docks Map 0_94 (14, 0).
[Map IDs]
- Map 0_95: 1F (Entrance)
- Map 0_98: B1F (Basement)
- Map 0_96: Deck Connector
- Map 0_97: Deck (Outside)
[Gary Rematch Objective]
- Status: Completed! (Turn 5541)
- Gary's Team: Pidgeotto Lv19, Raticate Lv16, Kadabra Lv18, Ivysaur Lv20
- Next Step: Find the Captain to get HM01 (Cut) in his cabin (up the stairs past Gary).

<hr>

<h1><code>Archive/SS_Anne</code></h1>

# S.S. Anne
- Hallway (Map 0_95): The horizontal walking path is Y=6 and Y=7. Y=8 contains alternating doors and impassable walls.
- Navigation Rule: To avoid bumping into walls, always walk horizontally on Y=6 or Y=7. Turn Down only when you are directly above the door you want to enter (Y=8).
- Coordinate mapping: Map 0_95 is the hallway, and Map 0_102 contains the individual cabin interiors.
- Map 0_100: Reached via stairs at (3, 16) on Map 0_95. This is a large open room (crew quarters/engine room) with pink/white checkerboard floors, not a hallway. Contains several Sailors.
- Trash cans checked: The two on the left side of the room are empty. The 'odd ball' might be in a different room like the kitchen.
[Cabin Clearance Checklist]
- Cabin 1: Cleared
- Cabin 2: Cleared
- Cabin 3: Cleared
- Cabin 4: Cleared
- Cabin 5: Cleared
- Cabin 6: Cleared
[Healing Plan]
- Cleo (Nidoqueen) is 23/58 HP. Hydro is 22/81 PAR. Use Potions/Antidotes as needed, or return to Vermilion Center if Cleo drops below 10 HP.
- Warp Link: Vermilion City (18, 31) connects to S.S. Anne Docks Map 0_94 (14, 0).
[Map IDs]
- Map 0_95: 1F (Entrance)
- Map 0_98: B1F (Basement)
- Map 0_96: Deck Connector
- Map 0_97: Deck (Outside)
[Gary Rematch Objective]
- Status: Completed! (Turn 5541)
- Gary's Team: Pidgeotto Lv19, Raticate Lv16, Kadabra Lv18, Ivysaur Lv20
- Next Step: Find the Captain to get HM01 (Cut) in his cabin (up the stairs past Gary).

<hr>

<h1><code>Locations/VermilionGym</code></h1>

# Vermilion Gym
- Type: Electric
- Weaknesses: Ground (Immune to Electric)
- Gym Leader: Lt. Surge
- Team Plan: Lead with Cleo (Nidoqueen) or Pebbles (Geodude).

# Vermilion Gym Puzzle
- Start Turn: 5821
- Timestamp: Thursday, February 26, 2026 at 10:55 AM PST
- Mechanic: First switch is randomly hidden. Second switch is in an adjacent can.
- CRITICAL: Failing the second guess RESETS the puzzle AND randomizes the first switch's location again!
- I accidentally reset the puzzle by bumping into cans and mashing A. Starting over carefully.

# Navigation
- Safe horizontal paths: Y=6, Y=8, Y=10, Y=12
- Safe vertical paths: X=0, X=2, X=4, X=6, X=8, X=10

# Trash Can Grid (15 cans)
Row 1 (Y=7): (1,7)[ ] (3,7)[ ] (5,7)[ ] (7,7)[ ] (9,7)[ ]
Row 2 (Y=9): (1,9)[ ] (3,9)[ ] (5,9)[ ] (7,9)[ ] (9,9)[ ]
Row 3 (Y=11): (1,11)[X] (3,11)[X] (5,11)[S1] (7,11)[ ] (9,11)[ ]

<hr>

<h1><code>Mechanics/Input_Delays</code></h1>

# Text Box Input Delay
- Gen 1 text box delays have been eating my first D-pad input after a text box closes, causing me to turn in place instead of walking. This leads to checking the same objects multiple times.
- Solution: Move to target tile -> End Turn (verify position) -> Turn & Press A -> End Turn -> Mash B to close text -> End Turn -> Repeat. Alternatively, use sleep commands in macros (e.g. sleep 500) between closing a text box and moving.

<hr>