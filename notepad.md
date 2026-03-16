<h1><code>Main</code></h1>

[Lessons Learned]
- Avoid over-mashing A during map transitions and battles. It causes UI desyncs, mistaken menu inputs, and turn hallucinations. Use targeted tools instead.
- Always carry Antidotes when exploring caves to prevent retreating from Poison damage.
- Map markers for defeated trainers (e.g. ☠️) should ONLY be placed AFTER returning to the overworld, never during a battle.
- If an item is not explicitly listed in the Game State Information sprite list, it DOES NOT EXIST.
- NEVER use dead reckoning. ALWAYS read the Game State Player Position before making any navigational assumptions.
- Gen 1 PC menus (DEPOSIT, WITHDRAW, etc.) retain cursor memory.
- Gen 1 Battle menus retain cursor memory! Reset the main menu cursor to FIGHT by pressing Up and Left before navigating.
- Gen 1 Move menu cursor memory is ALWAYS retained between turns in the same battle, even when the opponent sends out a new Pokemon! It only resets at the start of a completely new encounter.
- The Game State Info inventory list is alphabetized, but the in-game bag is NOT. Do not rely on Game State indices to find items.
- The overworld Start Menu ALSO retains cursor memory! Always check where the cursor is before blindly executing navigation sequences.
- When menu state desyncs or cursor memory causes an error, ALWAYS back out entirely to the overworld (spam B) and start fresh. Do not try to "fix" it mid-menu blindly.

[Timestamps]
- Route 6 / Vermilion Grinding Start: Turn 4321
- Route 11 Exploration Start: Turn 6409
- S.S. Anne Boarding: Turn 4431 (Tue Feb 24 2026)
- Rock Tunnel Exploration Start: Turn 7476
- Journey to Celadon City Start: Turn 9075
- Silph Scope Retrieval (Backtracking): Turn 11929
- Safari Zone True Path Run Start: Turn 31428

[HMs]
- HM01 (Cut): Taught to Audrey (Bellsprout).
- HM02 (Fly): Taught to Gye (Doduo).
- HM03 (Surf): Obtained! (Safari Zone Secret House prize).
- HM05 (Flash): Obtained! Tested party + Diglett, Dugtrio, Meowth, Voltorb - none can learn it. Abandoned finding a Flash user; navigating via grid is faster.

[Exploration Notes]
- NEVER assume a path is blocked based on visual patterns (like fences). ALWAYS physically test every tile along the suspected barrier by bumping into it to confirm if there is a hidden gap.
- Encountered Lv 30 Snorlax on Route 12. Failed to catch due to running out of Poke Balls. Defeating it to clear the path. Must stock up before the next static encounter!
- Custom tools cannot read the screen mid-execution (no while loops for visual feedback).
- Skull Bash is a 2-turn move (Turn 1: lowers head, Turn 2: attacks).
- Always visually confirm the item name under the cursor before pressing A in the item menu, as the bag is not alphabetized and indices change.
- The building at (22, 13) in Fuchsia City is NOT the Pokemon Center. It's a house with books.
- I must exclusively use short (1-3 step) movement sequences when navigating tight corridors with ledges and fences.
- WARNING: Cut bushes respawn if you walk too far away from them (off-screen reload)! Always re-verify if the path is actually open.

[Fuchsia City Layout]
- Moved to Locations/FuchsiaCity.

[Gen 1 Mechanics]
- Cursor memory differences: Party menu from Start->POKéMON ALWAYS RETAINS cursor memory, even if you close the Start menu completely and return to the overworld! Start->ITEM->USE resets it. PC and Battle menus retain it. Move menu retains it when switching manually, but resets on faint/new battle. PokeMart SELL menu RESETS to the top after every sale!
- The Party Menu and Move Menu WRAP. Mashing 'Up' does not guarantee index 1.
- HALLUCINATION CHECK: In the Safari Zone, TYPE_3fe2 is regular grass/path. TYPE_fed7 is PASSABLE TALL GRASS (Proven Turn 28643 by walking through it). TYPE_2889 is a solid bush. Do not assume visual "trees" are solid without physically bumping into them! Always verify turning vs stepping when a move sequence fails.
- MACRO DANGER: Do not use alternating directional macros (like L-D-L-D) near ledges when searching for gaps. It can cause accidental ledge jumps, leading to false assumptions about solid walls. Always use step-by-step inputs for precise exploration.
- In the overworld, the harness automatically handles turning in place before walking. You ONLY need to press a direction once to turn and take a step. DO NOT add extra presses for turning.
- The Start Menu WRAPS! Mashing 'Up' does not guarantee index 1.
- run_battle tool works perfectly in the Safari Zone because the 2x2 menu layout maps identically to the standard battle menu.
- NEVER assume a building's purpose based on interior floor tiles (e.g., checkered floors). Different buildings can share tilesets. Always rely on Game State Info (like the presence of a PC or Nurse Joy) to identify it.
- NEVER delete a verified, working path from notes just because you suspect a shortcut exists. Only update navigation notes AFTER empirically proving the new route works. Hallucinating gaps in solid walls (like Y=22 in Fuchsia) wastes dozens of turns.
- HALLUCINATION CHECK: If my current visual perception (e.g., seeing an Item Ball in a building) contradicts a previously written note (e.g., "This building is a trap Rest House"), I MUST trust my eyes and investigate the anomaly, rather than blindly following the note and ignoring the item. Notes can be poisoned by past false assumptions!
- Turn Hallucinations: When mashing A or B through dialogue (like the Safari Zone entrance), the exact number of turns taken can vary based on text rendering speed and auto-advances. Always double-check the current turn number in the Game State before declaring the current turn.
- HALLUCINATION CHECK: Always verify Cut bushes exist as SPRITES in the Game State before trying to cut them. Standard tree walls look identical on the grid but will yield "There isn't anything to CUT!".
- DIRT TRENCH NORTH: The dirt trench (TYPE_2770) extends North to Y=6. The green grass at Y=5 is separated by a ledge, preventing Northward movement.
- TOOL DESIGN NOTE: A custom tool for using HM field moves cannot reliably start from the Overworld because the Start Menu retains cursor memory (it doesn't reset to POKéMON). Therefore, `use_hm_field` MUST start from the Party Menu where the `current_index` can be visually verified by the player.
- SAFARI ZONE MAP TRANSITIONS: Transitions between Safari Zone areas do NOT always preserve coordinates. For example, moving West from Area 1 Center (0, 11) deposits you at Area 4 West (29, 23) - a +12 tile Y-shift! Never assume strict spatial continuity between Safari Zone sub-maps.

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
[Route 16 Planning]
- HM02 Fly is located on Route 16, which is West of Celadon City.
- Status: Snorlax caught! The path is now clear.
- Next Steps: Explore the area beyond the Snorlax spot to find HM02 Fly. After getting Fly, head to Saffron City.

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
- TYPE_5519: Cut Tree (Can be removed by using HM01 Cut from the Pokémon menu while facing it).
- CRITICAL: Cut bushes are ALWAYS `TYPE_5519`. Regular trees like `TYPE_2889` or `TYPE_1c8e` cannot be cut!
[Tile Identification]
- Safari Zone: TYPE_4e8c is a solid Plateau Edge (impassable from below). It is green but NOT tall grass. Passable tall grass is TYPE_fed7.

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
- Night Shade deals fixed damage equal to the user's level.

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
- Wrap Mechanic: Wrap is a multi-turn trapping move in Generation 1. The attack continues automatically for several turns without needing new inputs. When the main battle menu (FIGHT/PKMN/ITEM/RUN) reappears, it signifies the trapping effect has concluded.
- `execute_battle_turn` tool selects FIGHT and a move index. It CANNOT switch Pokemon. To switch, use `switch_pokemon_in_battle` or manual menu navigation.

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
- Pokemon Tower 3F: Caught Gastly (Lv 20)

<hr>

<h1><code>Mechanics/NPCBehavior</code></h1>

[Wandering NPCs]
- Wandering NPCs can step on and block warp tiles (like doors). If this happens, you must step back to give them space to wander off the tile before you can enter.
[Trainer Displacement]
- Trainers walk up to 1 tile towards you when they spot you.
- This can be exploited to move them out of blocking positions (e.g., to reach an item).
- Trainers have a line of sight. Stepping into it from a distance makes them walk toward you to start a battle. This is crucial for pulling them out of 1-tile choke points they are blocking so you can pass behind them after!

<hr>

<h1><code>Notes/ShoppingList</code></h1>

[High Priority]
- Buy Antidotes ASAP at the next Poke Mart. Poison damage is brutal in caves.
- To earn money for the Safari Zone, I will sell a single Ultra Ball at the PokeMart instead of a Rare Candy or TM. An Ultra Ball sells for 600 Poke Dollars, which is enough to cover the 500 Poke Dollar entry fee.
- Strategy: Sell BULK items (e.g., 5-10 Ultra Balls) to build a cash buffer for the Safari Zone, avoiding repeated trips to the PokeMart.

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
- The level gap is massive. I need to either switch-train the lower level Pokemon against weaker enemies or catch new, higher-level Pokemon.
- Audrey has fully evolved into Victreebel! She is currently our lead Pokemon.
[Party]
- HYDRO (Blastoise)
- DUGTRIO
- AUDREY (Bellsprout)
- CLEO (Nidoqueen)
- BAMBAM (Machop)
- PIXEL (Jolteon)
[Timestamps]
- Dugtrio has DIG! Use this instead of Escape Ropes to exit dungeons quickly.
[Items]
- Lemonade (from Celadon Dept Store Roof) is an extremely cost-effective healing item (80 HP for 350 Poke Dollars). Stock up when possible!
[Eevee]
- Obtained Eevee from Celadon Mansion Roof (0_132).
- Evolved into Jolteon (PIXEL) using Thunder Stone from Celadon Dept Store 4F!

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
- HARNESS AUTOMATION: The harness automatically handles turning. Pressing a direction ALWAYS results in a step (or a bump if blocked). DO NOT add extra presses just to turn!
- Bumping: To face a solid object (like a Cut bush), simply press the direction towards it. You will bump it and end up facing it.
- [Gen 1 Ledge Mechanics] Ledges can face South OR East/West! Turn 33137 PROVED that an East-facing ledge (TYPE_44f6) at (23, 28) in Fuchsia City CAN be jumped by walking Right into it. Previous assumption that only South-facing ledges work is false.
- HM FIELD MOVES: You MUST face the target tile (e.g., Cut bush, Water) BEFORE opening the Start Menu. The game checks your facing direction at the exact moment you select the move in the menu. Being adjacent is not enough.
- [Cycling Road] Route 17 has an automatic downward slope that forces the player South. Travel NORTH is IMPOSSIBLE with this harness due to the 500ms input delay allowing gravity to trigger. Must use Eastern routes to travel North.
- VISUAL CUES TRUMP TYPE LABELS: Always inspect the actual pixel art of a tile. A tile labeled `TYPE_3fe2` (floor) might visually contain the bottom half of a potted plant, a dark line indicating a one-way ledge, or the top of a desk (different color). If it looks like an obstacle, treat it as one, even if the label says otherwise. Don't blindly trust `TYPE_` labels without visual confirmation.

<hr>

<h1><code>Mechanics/General</code></h1>

[Mechanics/LevelUp]
- Mashing B cancels move learning.
- Cascade Badge: Pokémon up to Lv 30 obey. Enables CUT outside of battle.
- TM11 (Misty): Bubblebeam.
- Nidoran F evolves into Nidorina at Level 16.

[Elevators]
- To use an elevator, step onto the 2x2 red pad.
- The control panel is located on the top-left wall inside the elevator car.
- Face the control panel (usually by stepping up if you just entered) and press 'A' to open the floor selection menu.
- Silph Scope automatically identifies Ghost-type Pokemon in battle. No need to manually use it from the bag.
- Poison in the overworld damages 1 HP every 4 steps. Keep this in mind for survival calculations!

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
- [Turn 6151 Reflection] CRITICAL: The Game State inventory list is ALPHABETIZED and does NOT match the in-game bag's chronological order. Never use Game State indices for item tools. Manual counting/scrolling is required!

# Menu Navigation
- Gen 1 Menus (Items, Pokemon, PC) have cursor memory! The cursor stays where you last left it. Always visually verify the cursor position or track it carefully before using tools that navigate menus blind.
- The Party Menu wraps around (pressing Up at the top goes to the bottom) and retains cursor memory. You cannot reset the cursor by mashing Up. Always track or visually confirm current_index before using tools.
- Inventory Mechanics: To free an inventory slot occupied by a stacked item (like Poke Balls), the ENTIRE stack must be tossed or used. Tossing just one from a stack of multiple does not free the slot.
- WARNING: Pressing START in the item menu does NOT close the menu. It selects the item below the cursor and can trigger accidental item usage. ALWAYS use B to exit menus.
- Gen 1 Item Bag Wrap-around: Pressing Up at the top item wraps to CANCEL, then pressing Up again wraps to the bottom item. Mashing Up will endlessly loop the menu, not reset the cursor to the top!
- Gen 1 UI Quirks: The OVERWORLD ITEM menu WRAPS when navigating past the top/bottom. However, the BATTLE ITEM menu DOES NOT wrap! Keep this in mind when navigating items in battle.
- Menus with introductory text (like Vending Machines) can eat inputs if the text is still rendering or waiting for input to clear. Always use sleep commands (e.g., 'sleep 500') or wait visually before sending menu navigation inputs.
- Overworld signs/interactables can have multiple pages of text. If a text box isn't closing with 'B', check for a down arrow indicating more text and advance it with 'A' to prevent movement soft-locks.
- [Party Sub-Menu] Pokemon with Field Moves (Cut, Surf, Fly, etc.) have the field move at the top of their sub-menu. This pushes STATS to the 2nd slot and SWITCH to the 3rd slot. Standard Pokemon have STATS 1st and SWITCH 2nd. Custom tools like swap_pokemon will fail if they assume a fixed position for SWITCH.
- [Party Menu Cursor Memory] The cursor position is remembered across completely different access methods! If you use an item on Pokemon #2 via the ITEM menu, the next time you open Start->POKEMON, the cursor will STILL be on Pokemon #2. Never assume it resets to index 1.
- Fly Map Navigation [PROVEN]: The Fly map is a 1D list (Pallet -> Viridian -> Pewter -> Cerulean -> Lavender -> Vermilion -> Celadon -> Fuchsia -> Saffron). Left/Right do nothing. 'Up' moves FORWARD to the next city. 'Down' moves BACKWARD. The list WRAPS! (e.g. Down from Pallet wraps to Saffron).
- KO Switch Cursor Memory: When you select YES to "Will [PLAYER] change POKEMON?" after defeating an enemy, the cursor in the party menu STARTS on the currently active Pokemon, NOT index 1!
- CRITICAL TOOL FLAW: `execute_battle_turn`'s `start_on_main` feature attempts to reset the cursor to FIGHT by pressing `Up, Left`. However, the Gen 1 main battle menu WRAPS. If the cursor is already on FIGHT, `Up, Left` will wrap it to ITEM! Do not use `start_on_main: true` if the cursor is already on FIGHT, or you will accidentally open the ITEM menu.

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
- Puzzle solved! The motorized doors are now open. The first switch was at (5, 11) and the second was at (5, 9). I can proceed to Lt. Surge! (Deleting grid to save space)

# Lt. Surge Battle
- Voltorb Lv 21 (Tackle, Screech, Sonicboom)
- Pikachu Lv 18 (Quick Attack, Growl)
- Raichu Lv 24 (Thundershock, Growl, X Speed)
- Defeated Lt. Surge! Received Thunderbadge (Speed + Fly) and TM24 (Thunderbolt).

<hr>

<h1><code>Mechanics/Input_Delays</code></h1>

# Text Box Input Delay
- Gen 1 text box delays have been eating my first D-pad input after a text box closes, causing me to turn in place instead of walking. This leads to checking the same objects multiple times.
- Solution: Move to target tile -> End Turn (verify position) -> Turn & Press A -> End Turn -> Mash B to close text -> End Turn -> Repeat. Alternatively, use sleep commands in macros (e.g. sleep 500) between closing a text box and moving.

<hr>

<h1><code>Locations/DiglettsCave</code></h1>

# Diglett's Cave
- Encounters: Diglett, Dugtrio
- Catching Strategy: Cleo (Lv 20 Nidoqueen) is too strong. Switch to Audrey (Lv 16 Bellsprout) and use Wrap, or use Pebbles (Lv 12 Geodude) to weaken them. 
- Dugtrio Contingency: If a high-level Dugtrio appears, immediately switch to Audrey to resist Ground moves. Use Wrap to chip its health. 
- Gen 1 Mechanic: Wrap is a multi-turn trapping move. The attack continues automatically for several turns. When the main battle menu reappears, it means the trap has concluded.

<hr>

<h1><code>Mechanics/Navigation</code></h1>

# Navigation Mechanics
- ALWAYS read the TYPE_ annotations on the screen grid instead of blindly guessing why movement failed. Ledges and fences require visual confirmation.
- Ledges (e.g. TYPE_44f6) enforce one-way movement. Route 5 requires looping back to the top to access the right-side lanes.
- Building identities must be verified by entering them, not by visual assumption. Saffron Gate and Underground Path are visually similar.
- Do NOT blindly trust assumed long-distance coordinate math (e.g. 'walk straight south from X'). Walk step-by-step and trace impassable tiles (water, trees) to find correct paths.
- When mapping, use exact coordinates and do not jump to conclusions about blocked paths until physically bumping into them. Use map markers to explicitly mark entrances!
- Protocol: When taking a ladder or door, immediately stop, verify the new Map ID, and step OFF the warp tile before using automation tools.

<hr>

<h1><code>Locations/Route9</code></h1>

[Route 9 Layout]
- Ledge at Y=13 drops South.
- Lane at Y=14, Y=15 is bounded by X=10 and X=23. Gap UP at X=19.
- X=9 is a solid wall from Y=10 to Y=17. Cannot go West.
- Middle lane (Y=8 to Y=12) goes East by squeezing through at Y=12, bypassing the rock wall at X=30.
- Northern path (Y=2 to Y=5) goes East past X=39 gap.

<hr>

<h1><code>Locations/RockTunnel</code></h1>

# Rock Tunnel Master Route (Forward)
Entrance is at Route 10 (8, 16). Map 1F = 0_82, B1F = 0_232.
1. Enter 1F at (15, 3). Go East to 1F (37, 3) ladder. Down to B1F (33, 25).
2. B1F (33, 25) -> navigate West and North to B1F (27, 3) ladder. Up to 1F (5, 3).
3. 1F (5, 3) -> West to X=4, South to Y=21, East to X=21, North to Y=17, West to X=17, North to 1F (17, 11) ladder. Down to B1F (23, 11).
4. B1F (23, 11) -> South to Y=13, West to X=14, South to Y=14, West to X=5, North to Y=4, West to X=3, North to B1F (3, 3) ladder. Up to 1F (37, 17).
5. 1F (37, 17) -> South to Y=20, West to X=36, South to Exit at (36, 33) (Lavender Town).

[Tile Dictionary]
- TYPE_3fe2: Walkable Floor
- TYPE_2889: Impassable Rock Wall
- TYPE_2770: Impassable Rock Wall

<hr>

<h1><code>Locations/RockTunnel_B1F</code></h1>

# Rock Tunnel B1F (Map 0_232) Tracking
- Strategy: B1F is ONE GIANT interconnected map. Don't get tricked into thinking sections are separated.
- Ladders to 1F:
  1. (33, 25) - Connects to 1F (37, 3) [Near Entrance]
  2. (27, 3) - Connects to 1F (5, 3)
  3. (23, 11) - Connects to 1F (17, 11)
  4. (3, 3) - Connects to 1F (37, 16)

<hr>

<h1><code>Notes/InventoryOrder</code></h1>

# Inventory Order
1. TM08
2. HM01
3. OLD ROD
4. TM24
5. HM05
6. BICYCLE
7. TM30
8. SUPER POTION
9. REVIVE
10. MOON STONE
11. NUGGET
12. LIFT KEY
13. SILPH SCOPE
14. ESCAPE ROPE
15. ELIXER
16. HP UP
17. X ACCURACY
18. RARE CANDY
19. POKé FLUTE
20. SUPER ROD

<hr>

<h1><code>Locations/Route10_South</code></h1>

# Route 10 South (Map 0_21)
- Exited Rock Tunnel at the north end of this map.
- Defeated Hiker around (3, 62).
- Defeated Pokemaniac at (11, 64).
- Heading further South to reach Lavender Town.

<hr>

<h1><code>Locations/LavenderTown</code></h1>

# Lavender Town

Points of Interest:
- Pokemon Center: Exterior 0_4 (3, 5)
- Mr. Fuji's Volunteer Pokemon House: Exterior 0_4 (5, 5) (Mr. Fuji is missing)
- Name Rater's House: Exterior 0_4 (7, 11)
- PokeMart: Exterior 0_4 (15, 13), Interior 0_150
  - Sells: Great Ball, Super Potion, Revive, Escape Rope, Super Repel, Antidote
- Pokemon Tower: Exterior 0_4 (14, 5), Interior 1F 0_142
- Pokemon Tower 2F: 0_143
[Pokemon Tower]
- 5F has a purified healing zone at (10, 8) that fully restores the party!

<hr>

<h1><code>Mechanics/TypeMatchups</code></h1>

# Type Matchups

[Ghost]
- Immune to: Normal, Fighting

<hr>

<h1><code>Bosses/RivalGary</code></h1>

# Rival Gary Encounters

## Pokemon Tower 2F
- Pidgeotto Lv 25
- Gyarados Lv 23 (Moves: Bite, Hydro Pump)
- Growlithe Lv 22
- Kadabra Lv 20
- Ivysaur Lv ???

<hr>

<h1><code>Locations/Route8</code></h1>

# Route 8

[Layout & Navigation]
- Saffron City Gate: Located at the west end of the main paved road.
- Underground Path (to Route 7 / Celadon): Located on the upper path at (13, 3).
- To bypass the Saffron Gate, use the Underground Path at (13, 3).
- There is also a Cut tree at (29, 12) granting access to a narrow southern path with trainers.
- Follow this southern path westward to find more trainers (like a Gambler at x=13, y=8) and continue searching for the real Underground Path entrance.

[Trainers Defeated]
- Super Nerd at (42, 6)
- Lass at (48, 12)
- Gambler at (46, 13)
[Route 8]
- Saffron City Gate at (8, 11) is blocked by thirsty guards.

<hr>

<h1><code>Locations/CeladonCity</code></h1>

# Celadon City

[Points of Interest]
- Pokemon Center: East side of the city (arriving from Route 7).
- Map 0_129 is 2F of Celadon Mansion. It is NOT the back alley.
- Map 0_130 is the Game Freak HQ (Celadon Mansion 3F), accessible via the back entrance. It is NOT Route 16.
- Moving UP at 0_129 (6, 1) warps to 0_130 (Game Freak HQ). It is NOT stairs.
- Celadon Mansion Main Entrance: (24, 9). Contains Manager and Game Freak developers.
- Celadon Dept Store 1F: (10, 13) in Celadon City.
- Game Corner (Map 0_135): Entrance at (28, 19). Contains Team Rocket members. Look for a hidden switch to access their hideout.
- Game Corner (0_135): NPC at (17, 13) offers free coins, requires Coin Case.
- Game Corner (0_135): Hidden switch behind the poster at (9, 4), previously guarded by a Rocket Grunt.

[Navigation & Hidden Paths]
- The alley at X=5 on the West side of Celadon City is a dead end.
- The path North at X=14 (East of Dept Store) is completely blocked.
- The top path (Y=1/Y=2) behind the buildings is accessed via a hidden gap in the trees at X=32 and X=33 (Y=3). These tiles appear as solid trees but are walkable. This connects back to the main city streets on the East side at X=44. This is the ONLY way to reach the back entrance of Celadon Mansion.
- Gym Entrance Route (Southwest): Drop down the ledge at (7, 18) -> Walk East and go South on X=22 -> Follow the path East along Y=31 -> Cut the bush at (35, 32) -> Walk West along the bottom perimeter (Y=34) -> Go North through the gap at X=5 -> The Gym entrance is at (12, 27).
- The West exit to Route 16 from Celadon City is located at Y=18. The main road at Y=10-14 is blocked by trees on the far West edge.

<hr>

<h1><code>Notes/PC_Storage</code></h1>

# PC Storage Log

[Items Deposited]
- HELIX FOSSIL (Deposited Turn 9518)
- S.S. TICKET (Deposited Turn 9526)
- TM11 (Deposited Turn 9529)

<hr>

<h1><code>Locations/CeladonDeptStore</code></h1>

# Celadon Department Store
- Needs exploration.

[Floors]
1F: Elevator at (16, 1). Stairs Up at (12, 1). Exit is at (2, 7) and (3, 7).
2F: Stairs Down at (12, 1), Stairs Up at (16, 1)
3F: Stairs Down at (16, 1), Stairs Up at (12, 1)
4F: Stairs Down at (12, 1), Stairs Up at (16, 1)
5F: Stairs Down at (16, 1), Stairs Up at (12, 1)
Roof:
- Roof (6F): Only one set of stairs located at (15, 2) leading back down to 5F. Vending machines are at (12, 1).
- 2F Right Cashier: Sells TMs (TM32, TM33, TM02, TM07...)
- 2F Left Cashier: Sells standard items (Great Ball, Super Potion, Revive, Super Repel, etc.)
- 3F: Video Game Shop. No item cashiers observed here.
- 4F: Left counter is just display stands. Cashier must be elsewhere.
- 4F: The cashiers are located at the bottom of the room behind the counter at Y=6. The left cashier is at (5, 7).
- 4F Left Cashier (5, 7): Sells Poke Doll (1000), Fire Stone (2100), Thunder Stone (2100), Water Stone (2100), Leaf Stone (2100).
- 4F: Confirmed only ONE cashier on this floor at (5, 7). The NPC on the right is just a shopper.
- 5F Right Cashier (6, 4): Sells Stat Boosters (HP Up, Protein, Iron, Carbos, Calcium).
- 5F Left Cashier (5, 4): Sells Battle Items (X Accuracy, Guard Spec, Dire Hit, X Attack, etc.).
- Roof (6F, Map 0_126): Vending machines. Need to buy one of each drink for the little girl to get TMs. (Fresh Water = TM13)
- Soda Pop = TM48 (Rock Slide)
- Lemonade = TM49 (Tri Attack)

<hr>

<h1><code>Locations/CeladonMansion</code></h1>

# Celadon Mansion
- Physically divided into 'Front' and 'Back' sections by an impassable wall.
- Cannot cross between Front and Back from inside.
- Front Entrance: South side.
- Back Entrance: North side (alleyway), Map 0_6 (25, 2).

[Floors]
1F (Map 0_128): Elevator at (7, 1). Exit at bottom.
- 1F (Map 0_128): The room is divided by a wall. The stairs to 2F are on the right side at (7, 1). There is no obvious back exit on the ground floor.
- 1F Back: Entrance from 0_6 (25, 2) drops you at (4, 1). To go back outside, press UP at (4, 1). To go to 2F, step onto the stairs at (2, 1).
2F (Map 0_129): Elevator at (7, 1). Stairs at (2, 1) and (4, 1).
- 2F Left Side: Physically blocked by a solid row of desks/plants from (0, 3) to (4, 3). Cannot reach the back stairs at (2, 1) or (4, 1) from the front entrance.
3F (Map 0_130): Game Freak HQ. Back stairs down at (4, 1), up at (2, 1).
4F (Map 0_131): Split map! Right side is 4F interior (from front elevator). Left side is the ROOF (from back stairs). Back stairs down at (2, 1). There is a small room on the roof. The entrance to this room is at (2, 7).
5F (Map 0_132): The room on the roof (contains Eevee).

<hr>

<h1><code>Locations/RocketHideout</code></h1>

# Rocket Hideout - Verified Route to Silph Scope
[Start: Turn 12425]
[STATUS: COMPLETE]

## Master Route
1. **Enter Hideout:** Take secret stairs at Game Corner (17, 4) down to B1F.
2. **B1F to B2F:** Walk right and down to the stairs at (23, 2), descend to B2F.
3. **B2F Spinner Maze:** Enter maze at (17, 11).
   - (2, 9) Stop: Walk R, D, D, R to (4, 11) spinner -> (8, 11) Stop.
   - (8, 11) Stop: Walk R, R, D, D, D, R to (11, 14) spinner -> (15, 18) Stop.
   - (15, 18) Stop: Walk L, L to (13, 18) spinner -> (11, 20) Stop.
   - (11, 20) Stop: Walk R, R, R, D, D, L to (13, 22) spinner -> (9, 24) Stop.
   - (9, 24) Stop: Walk R, D to (10, 25) spinner -> (14, 25) Stop.
4. **B2F Elevator:** From (14, 25) Stop, walk right to X=24, then up to the Elevator pad at (24, 19). Press 'Up' to enter the doors at (24, 18).
5. **To B4F:** Inside the Elevator (Map 0_203), face the panel at the top left and press 'A' to use the Lift Key and travel to B4F.
6. **Giovanni & Silph Scope:** Defeat Giovanni at (25, 3) and pick up the Silph Scope item ball.

<hr>

<h1><code>Locations/RocketHideout_B1F</code></h1>

# Rocket Hideout B1F
[Start: Turn 10026]

## Verified Routes & Mechanics
- **Elevator Doors:** There are NO accessible elevator doors on the main section of B1F. 
- **B1F South:** Accessed via B2F maze. Bounded by a solid wall at X=23. Verified as a complete dead-end trap with no items or hidden warps. Use Dig to escape.
- The elevator must be accessed from B2F at (24, 19).

<hr>

<h1><code>Locations/RocketHideout_B2F</code></h1>

# Rocket Hideout B2F
[Start: Turn 10168]

## Spinner Maze
- Entrance at right side.
- Top path: (17, 11) L -> (14, 11) U -> (14, 9) L -> (4, 9) L. Player ends up at (2, 9).
- Items visible: (1, 11), (6, 12).
- Middle path: (4, 15) R -> (8, 15) U -> (8, 12) U -> stops at (8, 11).
- From (8, 11), going L leads to item at (6, 12).
### Tile Dictionary
- UP: TYPE_cf9b
- DOWN: TYPE_55cd
- LEFT: TYPE_55d0
- RIGHT: TYPE_64a2
- STOP: TYPE_55d4
- WALK: TYPE_3fe2
- Bottom path: From (8, 11) stop tile, go R to (10, 11), U to (10, 10) Up spinner. Leads to (2, 9) stop tile, which is near an elevator.
- Found Item at (16, 8). Reached via navigating the right-side paths after the initial top/middle exploration.
- From (8, 11) stop tile, going R, R, D, D, D, R hits (11, 14) Down spinner. Leads to (15, 18) stop tile.
- From (15, 18) stop tile, L L hits (13, 18) L spinner -> (11, 18) D spinner -> (11, 20) stop tile.
- From (11, 20) stop tile, L U hits (10, 19) U spinner -> (10, 17) R spinner -> (12, 17) R spinner -> (14, 17) U spinner -> (14, 15) stop tile.
- From (14, 15) stop tile, R R D hits (16, 16) U spinner -> (16, 14) U spinner -> (16, 13) stop tile.
- From (16, 13) stop tile, going U U L hits (16, 11) U spinner -> (16, 9) L spinner -> (14, 9) L spinner -> (2, 9) stop tile.
- Wait, I ended up at (14, 12) somehow.
- From (9, 16) stop tile: R R hits (11, 16) R spinner. R D hits (10, 17) R spinner. U R hits (10, 15) U spinner. U L U hits (8, 14) which is walkable.
- The stairs at (27, 8) go back UP to B1F (at 23, 2). Not down to B3F!
- From (2, 9) stop area: (4, 11) R spinner -> (8, 11) stop tile. (5, 14) R spinner -> (9, 16) stop tile.
- The grey panels at (2, 9) and (3, 9) are just the graphics for the stop tiles! No elevator here.
- The entire left corridor from (2, 9) to (4, 15) is a dead end. All three right-facing spinners return to the maze at (8, 11) or (9, 16).
- From (16, 13) stop tile, going R R U U L hits (17, 11) L spinner -> (2, 9) stop tile.
- From (11, 20) stop tile, going R R R D D L hits (13, 22) L spinner -> (9, 24) stop tile.
- From (9, 24) stop tile: 
  - Option A: L U hits (8, 23) U spinner.
  - Option B: R D hits (10, 25) R spinner.
- From (14, 25) stop tile, I can walk freely in the corridor to the right (X=14..19, Y=21..25).
- From (8, 23) U spinner, path leads to (2, 19) stop tile. Item found at (3, 21).
- From (2, 19) area, can walk down to (4, 22) U spinner.
- From (6,20) stop tile, going D L L L leads to item at (3,21).
- From (6,20) stop tile, going U L hits (4,19) L spinner -> (2,19) stop tile.
- Found stairs at (21, 8) leading to B3F (Map 0_201)!
## TRUE ELEVATOR PATH (Step-by-Step)
1. From B2F (27, 8) stairs, walk to (17, 11) Top Spinner -> Ends at (2, 9) Stop.
2. From (2, 9) Stop: Walk R D D R to (4, 11) spinner -> Ends at (8, 11) Stop.
3. From (8, 11) Stop: Walk R R D D D R to (11, 14) spinner -> Ends at (15, 18) Stop.
4. From (15, 18) Stop: Walk L L to (13, 18) spinner -> Ends at (11, 20) Stop.
5. From (11, 20) Stop: Walk R R R D D L to (13, 22) spinner -> Ends at (9, 24) Stop.
6. From (9, 24) Stop: Walk R D to (10, 25) spinner -> Ends at (14, 25) Stop.
7. From (14, 25) Stop: Walk right and up to (21, 22) stairs -> Takes you to B1F South.
[B2F Maze Path to Elevator]
- Path: (17, 11) spinner -> (2, 9) stop -> (4, 11) spinner -> (8, 11) stop -> (11, 14) spinner -> (15, 18) stop -> (13, 18) spinner -> (11, 20) stop -> (13, 22) spinner -> (9, 24) stop -> (10, 25) spinner -> (14, 25) stop.
- Then walk to the warp at (21, 22) which leads back to B1F South.

<hr>

<h1><code>Locations/RocketHideout_B3F</code></h1>

# Rocket Hideout B3F
[Start: Turn 10494]
- Arrived via stairs. Grunt defeated at (26, 8).

## Spinner Maze Paths (Machine Readable)
START:(20,11)|DIR:L|END:(17,11)
START:(17,11)|DIR:D|END:(17,16)
START:(17,16)|DIR:R|END:(18,15)
START:(18,15)|DIR:R|END:(20,15)
START:(18,15)|DIR:L|END:(16,11)
START:(17,16)|DIR:L|END:(16,11)
START:(16,11)|DIR:R|END:(20,11)
START:(16,11)|DIR:L|END:(10,11)
START:(10,11)|DIR:D|END:(14,13)
START:(10,11)|DIR:L|END:(9,17)
START:(14,13)|DIR:L|END:(9,17)
START:(9,17)|DIR:R|END:(15,22)
START:(10,19)|DIR:R|END:(18,15)
- [Turn 11115] Right side of maze is a trap loop. The real path is reached via the left side.
## True Path to B4F Stairs:
1. Walk through plant gap at (13,10). At (13,11) walk L to (12,11) L-spinner -> (10,11) STOP.
2. Walk D to (10,13) R-spinner -> (14,13) STOP.
3. Walk L to (11,13), D to (11,16) L-spinner -> (9,17) STOP.
4. Walk R to R-spinner -> (15,22) STOP. From here, walk L L D D D R R R R R R U U U U U U U to reach the B4F stairs at (19, 18).

<hr>

<h1><code>Locations/RocketHideout_B4F</code></h1>

# Rocket Hideout B4F
[Start: Turn 10637]

## Layout & Mechanics (VERIFIED)
- B4F is COMPLETELY SEPARATED into a Left Side and a Right Side by impassable walls.
- Left Side: Accessed via manual stairs from B3F (19, 10). Contains the Lift Key Grunt at (11, 2).
- Right Side: Accessed ONLY via the Elevator at (24, 11) / (25, 11). Contains Giovanni at (25, 3) and the Silph Scope.

## Objective
- MUST use the elevator from B2F (24, 18) to reach the Right Side, defeat Giovanni, and retrieve the Silph Scope. Do not trust past hallucinations stating otherwise.

<hr>

<h1><code>Locations/SaffronCity</code></h1>

# Saffron City
- Huge central hub city.
- The center is completely blocked off by the massive Silph Co. building and fences.
- To cross the city (e.g., West Gate to East Gate), you must navigate around the perimeter. The northern path is clear and connects the west and east sides.
- West Gate: Leads to Route 7 (Celadon City).
- East Gate: Leads to Route 8 (Lavender Town).
- North Gate: Leads to Route 5 (Cerulean City).
- South Gate: Leads to Route 6 (Vermilion City).
- Fighting Dojo and Saffron Gym are in the northeast corner.
- Poke Mart is in the northeast.
- Pokemon Center is in the southwest.
- Decorative Doors: The buildings along the southern border (Y=29) have doors, but they are solid walls (TYPE_2889) and cannot be entered. Do not try to enter them.
- Mr. Psychic's House: Located at (29, 29). He gives you TM29 (Psychic) for free!
- Fighting Dojo (Map 0_177): Located in the Northeast corner next to the actual Saffron Gym. Contains Blackbelt trainers using Fighting-type Pokemon.

# Fighting Dojo (Map 0_177)
- Located at (26, 3) in Saffron City.

[Points of Interest]
- Saffron Gym: Located at (34, 3). Currently blocked by a Team Rocket Grunt.
- Silph Co. Main Entrance: Located at (18, 21). The Team Rocket guard is asleep, allowing access!

<hr>

<h1><code>Archive/LocationNotes</code></h1>

[Trades]
- Route 5 Gate: NPC wants to trade a Nidoran F for a Nidoran M.
- Vermilion City: NPC wants Spearow for Farfetch'd.
- Route 2 House: NPC wants Abra for Mr. Mime.

[Vermilion City]
- Fan Club: (9, 13) - Talk to Chairman for Bike Voucher.

[Route 10]
- Found a Pokemon Center right next to Rock Tunnel entrance! This is a great place to heal and grind if needed.

<hr>

<h1><code>Locations/Route13</code></h1>

# Route 13
- Navigating a maze of fences. Watch out for dead ends and hidden gaps.
- Lots of Beauty, Bird Keeper, and Jr. Trainer♀ trainers.
- Mechanic note: Whirlwind has no effect in Trainer battles in Gen 1!
- TRUE MAZE PATH (West to East):
  1. Start on the Y=6 lane. Walk East to X=14. (Y=6 is blocked at X=16).
  2. At X=14, walk North through the gap to the Y=4 lane.
  3. Walk East on Y=4 to X=24/25. (Y=4 is blocked at X=26).
  4. At X=24/25, walk South through the gap back to the Y=6 lane.
  5. Walk West on Y=6 to X=17.
  6. At X=17, walk South through the gap to the Y=8 lane.
  7. Walk East on Y=8 to X=26.
  8. At X=26, walk South through the gap to the Y=10 lane.
  9. Walk East on Y=10 to exit the maze!

<hr>

<h1><code>Locations/Route14</code></h1>

# Route 14 (Map 0_25)
- This is the vertical route that connects Route 13 (East) to Route 15 (South/West).
- The East side connects to Route 13 at Y=8.
- The path West from the Route 13 connection (at Y=8) is a corridor bounded by trees.
- Need to find a way to the West side of Route 14 to access Route 15.
- (14, 12): ☠️ Defeated Bird Keeper
- (15, 6): ☠️ Defeated Bird Keeper

<hr>

<h1><code>Locations/Route15</code></h1>

# Route 15
- Horizontal route connecting Fuchsia City (West) to Route 14 (East).
- Divided into an upper path and a lower path by a one-way ledge.
- The West end connects to the Fuchsia City Gatehouse at (7, 8) on the lower path.
- Trainers: Lots of Bikers, Bird Keepers, Jr. Trainers.

<hr>

<h1><code>Locations/FuchsiaCity</code></h1>

# Fuchsia City
- Fishing Guru's Brother (Good Rod): (27, 27)
- Main city accessed via Cut tree at (26, 13).
- PokeMart: (5, 13) - Sells: Ultra Ball, Great Ball, Super Potion, Revive, Full Heal, Repel. (Clerk is on the LEFT side at 0,5. Stand at 2,5 and face Left to buy/sell).
- Pokemon Center: (19, 27) (Map 0_154. PC is at 13, 3 inside)
- House (Map 0_153): (11, 27)
- House (Map 0_154): (19, 27)
- Safari Zone Warden's House: (27, 27). The Warden is inside! (Has a boulder blocking an item inside).
- Fishing Guru's Brother: (31, 27). (Sign outside says 'FISHING GURU'S OLDER BROTHER').

[City Layout & Navigation Rules]
- Ledges are strictly ONE-WAY. You can only jump DOWN (South) or RIGHT (East) over them depending on their facing.
- Moving between North and South halves: The city is divided by a wall of buildings and fences at Y=27/Y=25.
- TOP TO BOTTOM: The West side is BLOCKED at Y=15 by a solid wall of bushes! To go South from the top half, you MUST walk East to X=18 and head South through the Cut bush at (18, 19). Then walk South to Y=21 and walk ALL THE WAY WEST to X=1 to bypass the zoo enclosures. Walk South along X=1 to Y=32, then walk East to X=8. The path East is blocked by trees at X=10. Walk North through the gap at (8, 31) to Y=28, then walk East along the sidewalk to the Pokemon Center at (19, 27).
- BOTTOM TO TOP: You CANNOT go North up the West side (X=1) due to ledges. You MUST go to the East side. From the Pokemon Center, walk East to X=22 and jump RIGHT over the East-facing ledge at X=23. Once on the East side, walk North to Y=20, then walk West to X=18, then North to Cut the bush at (18, 19).
- Safari Zone Path: From the Cut bush at (18, 19), walk North. To go to Safari Zone, go to X=22, walk North to Cut bush at (22, 7). Cut it. Walk West along Y=6 to X=18, North to enter at (18, 4). (Note: There is NO cut bush at 16,11. That was a hallucination).
- WARNING: The top path of Route 15 (Y=4) is a DEAD END. Do not use it expecting to return to Fuchsia City's top half.
- Transition: Fuchsia City (0_7) West exit at Y=18 connects to Route 18 (0_29) East side at Y=9.

<hr>

<h1><code>Locations/SafariZone</code></h1>

# Safari Zone
WARNING: EXECUTE ROUTES IN 3-5 STEP CHUNKS ONLY. Long macros cause accidental ledge jumps and desyncs.
- Limit: 500 steps.

[Map Connections (TWO-WAY LOOP!)]
- Area 1 Center (0_220) <-> Area 2 East (0_217) [via East Exit at 29,10 <-> 0,22]
- Area 1 Center (0_220) <-> Area 3 North (0_218) [via North Exit at 15,0 <-> South Exit at 20,35]
- Area 2 East (0_217) <-> Area 3 North (0_218) [via Northwest Exit at 0,4 <-> Southeast Exit at 39,30/31]
- Area 3 North (0_218) <-> Area 4 West (0_219) [via Southwest Exit at 8..15, 35 <-> Northeast Exit at 26, 0]

[AREA 4 WEST EXPLORATION ROUTE - THE TRUE PATH]
1. The entrance from Area 3 North's Southwest Exit (drops at 26, 0 in Area 4 West) is a DEAD END ROUTE. It only leads to the East Grass, Dirt Trench (ends at X=5), the North Pocket (ends at Y=6), and the South Grass Trap (loops back to Area 1).
2. HYPOTHESIS: The TRUE entrance to the functional part of Area 4 West (where the Secret House is) must be located on the WEST edge of Area 3 North, North of Y=23.
3. STRATEGY: Navigate to Area 3 North, cross the upper lake (North of Y=9), and explore the far West edge of Area 3 North to find this entrance.

[KNOWN TRAPS & DEAD ENDS]
- Area 4 West Trap Ledges: Jumping ledges at (14, 17) or (24, 17) traps you in the southern path, forcing an exit to Area 1 Center.
- Area 1 Center West Pocket: Exiting Area 4 West via (29, 22) drops you here. Walk West at (0, 11) to re-enter Area 4 West.
- Area 4 West Y=4 Path: DOES NOT EXIST. Hallucinated. X=24 is a solid tree wall.

[CURRENT STRATEGY: VERIFY AREA 1 CENTER WEST]
- [Turn 31894] Overwatch flagged a critical hallucination: I never physically tested the tiles at Y=15/16 on the West side of Area 1 Center (X=0 to X=5) for a gap North.
- [Turn 31908] EMPIRICAL PROOF OBTAINED:
  - Walked along Y=17 from X=6 to X=2, systematically pressing UP. Bumped into solid bushes (TYPE_2889) at (5, 16), (4, 16), (3, 16), and (2, 16).
  - Attempted to walk West from (2, 17). Blocked by a large solid tree occupying (0, 16)-(1, 16) and (0, 17)-(1, 17).
  - CONCLUSION: There is absolutely no gap North on the West side of Area 1 Center. The wall is 100% solid.

[FINAL PROVEN LAYOUT FACTS]
- TRUE PATH TO SECRET HOUSE: In Area 3 North, cross the Northern edge (Y=1..3) from X=28 to X=1. Walk South down the 1-tile wide path at X=1. Enter the gap at (2, 35). This places you at (20, 0) in Area 4 West. Walk West along Y=4 to reach the Secret House at (3, 3) and the Gold Teeth at (19, 7).
- AREA 1/2 CHOKEPOINTS: Area 1 West is fully blocked. Area 2 requires using the South Dirt Plateau (stairs at 20,21 to 12,21) to bridge over the tree walls.

<hr>

<h1><code>Scratchpad/Reflections</code></h1>

[Active Reflections]
- Goal: Explore 8F main area to find the Card Key.
- Strategy: Defeat the Grunt at (19, 2), then systematically map the paths radiating from the elevator.

[Turn 36392 50-Turn Reflection]
- Notepad Hygiene: `Locations/SilphCo` is being updated meticulously with every new path and dead end discovered.
- Error Analysis: Misidentified potted plants as warp pads due to similar pixel patterns at a glance. Lesson: Always physically approach anomalous tiles to verify their nature before committing them to permanent notes.

<hr>

<h1><code>Scratchpad/Mechanics</code></h1>

[Unverified Hypotheses]
- Status Move Accuracy Message: In Gen 1, when a status move (like Stun Spore or Sleep Powder) misses due to accuracy, the game displays "It didn't affect [PKMN]!" instead of "The attack missed!". I observed this when an enemy Oddish's Stun Spore failed against my Dugtrio (Ground-type) with the "didn't affect" message. This disproves my previous theory about Grass-type immunity to Grass status moves; it was just a 75% accuracy miss!
- [Gen 1 Status Immunity] A Pokemon can only have ONE major status condition at a time. If a Pokemon is Paralyzed, it is IMMUNE to being put to Sleep, Frozen, Burned, or Poisoned. This makes a Paralyzed Pokemon an excellent safe lead for switch-training against enemies that spam Sleep Powder/Stun Spore (like the trainers in Celadon Gym).
- Wrap-lock: In Gen 1, if the Wrap user is faster, the target cannot attack at all during Wrap. If the target is paralyzed, their speed is reduced, making them susceptible to indefinite Wrap-locks from normally slower Wrap users. Switching to a faster Pokemon is required to break the lock.
- Text Box Input Eating: If you use a macro (like execute_battle_turn) while a text box is still printing or waiting to be cleared, ALL directional inputs and A/B presses will simply act as text-advances. The menu navigation will fail, and you will be left at the root menu when the text finally clears. For Wrap-locks, it's better to just spam 'A' so it advances the text and automatically selects the first move.
- Switch Prompt Cancel: Mashing 'B' to clear text after defeating an enemy will automatically select 'NO' on the "Will [PLAYER] change POKEMON?" prompt. Use step-by-step inputs instead of safe_mash_b if you intend to switch-train the next Pokemon!
- Evolution Cancel: NEVER mash 'B' or use safe_mash_b when exiting a battle if a Pokemon just reached its evolution level! Pressing 'B' during the evolution animation will cancel it. Use 'A' instead to advance text safely.
- Overworld Item Menu Wrap: Pressing Up at the very top of the Item menu (index 1) DOES NOT wrap around to the bottom. It stays at the top. Blind upward wrap-around navigation will fail here!
- PC Deposit Cursor Reset: Turn 34518 to 34528 proved that when depositing an item, the cursor RESETS to index 1 (the top of the current visible list) after the deposit confirmation. It does NOT retain the previous index like the Withdraw or overworld Item menus.
- PC Menu Input Eating: If inputs are sent while the "What do you want to deposit?" text is still rendering (e.g., just after a previous deposit confirmation), directional inputs will be eaten! This causes tools like `deposit_item_pc` to fail and deposit the top item (index 1) instead of the target. ALWAYS ensure the menu is fully loaded and the cursor is visible before sending navigation sequences.
- Fly Map Input Eating: The Fly map has a rendering/animation delay when opened. D-pad inputs sent immediately after pressing 'A' to select Fly can be eaten. The destinations are ordered in a list (Pallet, Viridian, Pewter, Cerulean, Lavender, Vermilion, Celadon, Fuchsia). Press Down/Up to navigate this list.
- Silph Elevator: Appears operational without a keycard! The elevator interior is a separate map (0_236). Select a floor at the panel (3,0), then walk South to exit onto the new floor.
- Electronic Doors: Red barriers block paths. Require Card Key.
- [Gen 1 Battle Mechanic] The game says "The trainer blocked the BALL!" when you try to use a Poke Ball in a trainer battle. I accidentally selected Ultra Ball instead of Fresh Water!
- [Gen 1 Battle Mechanic] I used Fresh Water (index 3) via the ITEM menu. The next time I pressed 'A' on the main battle menu, it opened the ITEM menu again instead of FIGHT. This proves that the MAIN BATTLE MENU also retains cursor memory between turns! It does not default back to FIGHT.
- [Gen 1 Battle Mechanic] Turn 35634: I visually confirmed the text "But, it failed!" on screen when Cubone used a move (likely Bone Club) against Gye. My original observation was correct! In Gen 1, Ground-type moves failing against Flying-types display the "failed" message, not the "doesn't affect" message. My previous correction was a hallucination caused by missing OCR frames.
- [Gen 1 Battle Mechanic] Turn 35615: Cubone used Leer on the turn I switched to Gye. The attack missed or failed (or I missed the text). Need to re-verify if switching breaks stat-lowering moves, but I must be careful not to assume text that isn't logged.
- [Gen 1 Battle Mechanic] Turn 35643: Cubone's Growl "failed!" against Gye. This is likely because Gye's Attack stat has already been lowered 6 times (the maximum number of stat stages in Gen 1). Good to know the game explicitly tells you when a stat can't go any lower!

<hr>

<h1><code>Locations/CeladonGym</code></h1>

# Celadon Gym (Map 0_134)
- Type: Grass
- Leader: Erika
- Entrance/Exit: (4, 17)

[Layout & Trainers]
- Left Path (X=3/X=4): Lass at (3, 11) [Defeated]. Team: Bellsprout Lv 23, Weepinbell Lv 23.
- Right Path (X=7/X=8): Beauty at (7, 10) [Defeated]. Team: Oddish Lv 21, Bellsprout Lv 21, Oddish Lv 21, Bellsprout Lv 21.
- Middle Path (X=5): Blocked by a Cut bush at (5, 7). Trainer located at (5, 5).

[Strategy]
- Enemy trainers primarily use Grass/Poison types (Oddish, Bellsprout lines).
- They frequently use status powders (Sleep Powder, Stun Spore, Poisonpowder).
- Leading with a Paralyzed Pokemon (like Audrey) grants immunity to Sleep and Poison, making it a safe lead for switch-training.
- Status Shield Maintenance: DO NOT heal at the Pokemon Center while clearing Celadon Gym! Healing at the Center cures Paralysis, which we need to keep as our immunity shield against Sleep/Poison. Instead, use Lemonades and Fresh Water to restore HP between battles while preserving the Paralyzed status.
[More Trainers]
- (1, 5) Beauty - NPC only.
- (3, 3) Beauty - NPC only.
- (4, 3) Erika (Defeated).
- (6, 4) Lass (Defeated).
- (9, 5) Lass - NPC only.
- Celadon Gym is completely CLEARED!

<hr>

<h1><code>Locations/Route16</code></h1>

# Route 16
- Connects Celadon City (East) to Cycling Road/Route 17 (South).
- Snorlax blocks the main intersection at (26, 10). Defeated/Caught Turn 34645.
- Upper Path: Accessible via Cut bush at (34, 9).
- Secret House (Map 0_188): Located at the far West end of the upper path (past the gatehouse). Contains the NPC who gives HM02 (Fly).

<hr>

<h1><code>Locations/SilphCo</code></h1>

# Silph Co. (Saffron City)

[Navigation]
- 1F (Map 0_181): Elevator doors are at (20, 0). Exit to Saffron at (10, 18).
- Elevator Interior (Map 0_236): This 4x4 room is the inside of the elevator. The control panel is at (3, 0). Stand at (3, 1) and press A facing Up to select a floor. Exit the elevator by moving DOWN onto the red tiles from (1, 2) or (2, 2). Pressing Down at X=0 does not work.
- Electronic Doors: Red barriers block paths throughout the building. They require the Card Key to open. We need to find it ASAP to explore fully.

[Floors]
- 5F (Map 0_210): Elevator at (20, 0). Electronic doors block the south path immediately out of the elevator. West hallway leads to a Silph Employee at (8, 3) (Master Ball dialogue). Bypass him via X=9.
- 5F: Warp pad at (11, 5).
- 5F Navigation: The path South at X=14 leads to a dead-end room with a warp pad at (11, 5). To explore the rest of the floor, use the path South at X=22 (East of the elevator).
- 5F Navigation: South path at X=22 leads to a large central room. There is a clipboard on the desk at (26, 10) with a Pokemon Report.
- 5F Navigation: Item ball at (21, 16) is behind a wall at Y=15. Grunt at (18, 10).
- 5F Navigation: Wall at X=27 blocks access to X=28 from the central room. Wall at Y=15 blocks access to the item ball at (21, 16) from the central room.
- 5F Navigation: The central room is bounded by an electronic door at (15, 10) on the West and desks at Y=15 on the South. The item at (21, 16) is unreachable from here.
- 5F Navigation: East of the elevator at X=24 is a path South. It contains a warp pad at (27, 3), a Grunt at (28, 3), and a clipboard at (24, 6). The Grunt blocks the path South at X=28.
- 5F Stairs: Stairs UP to 6F at (24, 0). Stairs DOWN to 4F at (26, 0).
- 4F (Map 0_209): Stairs UP to 5F at (26, 0). Stairs DOWN to 3F at (24, 0). Grunt at (12, 14).
- Warp Connection: 10F warp at (13, 7) connects to 4F warp at (17, 11).
- Warp Connection: 5F warp at (11, 5) connects to 3F warp at (3, 3).
- 5F Navigation: West corridor leads South to a true dead end at Y=16. Grunt is at (8, 16). Electronic door at X=7. Warp pad at (9, 15).
- Warp Connection: 5F warp at (9, 15) connects to 9F warp at (17, 15).
- 9F (Map 0_233): Warp at (17, 15) lands in a partitioned area. A solid wall at X=14 blocks access to a healing Nurse at (13, 16). A Grunt is accessible to the East at (21, 13).
- 9F Navigation: Path East is at Y=15. Grunt at (21, 14). Electronic doors at (18, 10) block North.
- 9F Navigation: Path continues North at X=24.
- 9F Navigation: Path North at X=24 leads West to a dead-end room with objects at (18, 4) and (19, 4) that require a Card Key.
- Warp Connection: 5F warp at (27, 3) connects to 7F warp at (21, 15).
- 7F (Map 0_212): Warp at (21, 15) lands in a partitioned area. A Grunt is at (19, 14) and electronic doors at (20, 12) and (21, 12) block the path North. Desks at Y=12 block access to the item ball at (24, 11) from the South. Dead end without Card Key.
- 6F (Map 0_211): Elevator at (18, 0). Stairs DOWN to 5F at (14, 0). Stairs UP to 7F at (16, 0). Electronic doors at (10, 4) and (11, 4). Grunt at (17, 3). Trainer at (10, 6).
- 6F Navigation: The path West from the stairs leads to an open hallway going South at X=7 and X=6. X=8 is a wall blocking the path East at Y=4 to Y=6. There are electronic doors at (2, 1) and (3, 1). There is a warp pad at (3, 3).
- Warp Connection: 4F warp at (17, 3) connects to 6F warp at (3, 3).
- 6F Navigation: Warp at (3, 3) lands in a partitioned area on the West side of 6F. This area is completely empty and a dead end.
- 6F Navigation: Following the hallway South leads to a Scientist at (7, 8). The path continues South to an intersection at (6, 12). An Item Ball to the West at (3, 12) is blocked by an electronic door at X=5.
- 6F Navigation: East of the intersection at (6, 15) is a hallway leading East. A Grunt is at (14, 15).
- 6F Navigation: The hallway continues East from (14, 15). A solid wall at Y=14 blocks the path North. A Grunt is visible behind the wall at (18, 13). The hallway continues East past X=23.
- 6F Navigation: The hallway continues East from (14, 15) to a dead end at X=25. The only path forward is North at X=24.
- 6F Navigation: The path North at X=24 leads to a warp pad at (23, 3). A room is visible to the West with two NPCs at (20, 6) and (21, 6), blocked by a wall at X=23.
- Warp Connection: 6F warp at (23, 3) connects to 2F (Map 0_207) warp at (9, 15).
- 2F (Map 0_207): Reached via warp pad from 6F (23, 3). The warp lands at (9, 15) in a small isolated room. A Scientist is at (5, 14). A woman is at (4, 13). No items or further progress here; it's a dead end.
- 7F Main (Map 0_212): Elevator at (18, 0). Stairs DOWN to 6F at (22, 0). Electronic doors block the path South at (20, 4) and (21, 4). Grunt at (20, 2).
- 1F Navigation: There are desks blocking the path East at Y=17 starting at X=12. Must walk at Y=16 or higher to go East.
- 1F Navigation: Path North through the center (X=14 to X=17) is blocked by a zigzag of potted plants (Y=10) and couches/glass walls (Y=8, Y=9). Must bypass these partitions by walking around the left side (X=11) or right side.
- 1F Navigation: Path North at X=9 is blocked by monitors at Y=6 and Y=7. Must use X=8 or further West to bypass the partitions and head North.
- 10F (Map 0_234): Elevator doors at (12, 0). Scientist at (10, 2).
- 10F Navigation: From elevator, path goes South via X=11. Path West at Y=5 is a dead end (wall at X=7). Electronic doors at (10, 8) and (11, 8) block South. Warp pad located at (13, 7).
- Warp Connection: 4F warp at (3, 15) connects to 10F warp at (13, 15).
- 10F Navigation: Warp at (13, 15) lands in an isolated area on the East side of a wall at X=7. A scared Silph employee wanders here. Item ball visible at (5, 11) on the West side of the wall. There is a second warp pad at (9, 11).
- Warp Connection: 10F warp at (9, 11) connects to 4F warp at (11, 7).
- 4F Navigation: Warp at (11, 7) lands in a partitioned area. Scientist at (14, 6). Electronic doors at (12, 8) and (13, 8) block South. Second warp pad located at (17, 3).
- Warp Chain Analysis: The warp chain starting at 4F (3, 15) -> 10F (13, 15) -> 4F (11, 7) -> 6F (3, 3) is a complete dead end with no Card Key. Backtracking out.
- 4F Navigation: The area isolated by the warp pad at (17, 11) is bounded by an electronic door at (5, 12) and walls. The warp pad itself is blocked from the South by desks at Y=12; access it via X=13. It's a dead end without the Card Key.
- 3F (Map 0_208): Elevator at (20, 0). Stairs DOWN to 2F at (26, 0). Stairs UP to 4F at (24, 0). Electronic door at (20, 4) blocks the path South. Path West is open.
- 3F Navigation: West hallway ends in a room with a warp pad at (3, 3) and a solid wall at X=0. No path South; it's a dead end connecting to 5F. 3F requires the Card Key to progress. Item ball at (8, 5) is unreachable from here.
- 3F Navigation: East hallway from the stairs has a warp pad at (27, 3). The path South is blocked by desks at Y=4.
- 2F (Map 0_207): Elevator at (20, 0). Stairs DOWN to 1F at (24, 0). Stairs UP to 3F at (26, 0). Hallways extend East and West from the elevator.
- 2F Navigation: West hallway from the elevator is blocked by a solid wall at X=11 (Scientist visible behind it at 10,1). The only feature is a warp pad at (13, 3).
- Warp Connection: 2F warp at (13, 3) connects to 8F (Map 0_213) warp at (3, 15).
- 8F Navigation: Warp at (3, 15) lands in an area bounded by a wall at Y=13. Another warp pad is visible at (3, 11) but blocked by this wall. Path continues East.
- 8F Navigation: Path from (3, 15) goes East, turning North at X=11, East at Y=14, and North again at X=21, continuing up to Y=7 where it opens up.
- 8F Navigation: Path North at X=21 leads to a room with potted plants. A South-facing ledge at (17, 8) forces a one-way drop into a 1x4 dead-end hallway from (17, 9) to (17, 12).
- Warp Connection: 3F warp at (27, 3) connects to 2F warp at (3, 3).
- 2F Navigation: The warp from 3F (27, 3) lands at (3, 3) in a small room on the West side of the building. There is an electronic door blocking the path East at (4, 4) and (5, 4). There is an Item Ball visible behind a wall to the East at (8, 4). This room is a dead end without the Card Key.
- 2F Navigation: East hallway from the elevator leads to stairs at X=24 and X=26. South of the stairs is a woman at (25, 7). She mentions "I work for SILPH. What can I do?".
- 4F Navigation: East of the stairs, the path South at X=26 is blocked by a Grunt at (26, 7). Bypassing via X=23 leads to an empty loop (X=26/28, Y=8 to Y=16). Electronic doors at (26, 4) to (28, 4) block access to a room.
- 4F Navigation: West corridor (Y=13/14) from X=15 leads to a dead end at X=3. The item ball at (3, 9) is inaccessible from here due to a wall at Y=12.
- 8F Main Navigation: Elevator at (18, 0). Grunt at (19, 2). Path goes West to X=15, then South.
- 8F Main Navigation: Path East of elevator loops around (17, 5) to (24, 12) and connects South to the East hallway. No Card Key here.
- 8F Main Navigation: Hallway at X=15 goes South to Y=15. Grunt at (12, 15). Need to explore West of this Grunt.
- 8F Navigation: Warp pad at (11, 9) connects to 8F warp at (3, 11). Path goes West to X=1, North to Y=2, and East to an NPC at (4, 2), bypassing the electronic doors at (4, 10).
- 8F Navigation: Finished mapping 8F. It is entirely a large connected loop with no Card Key. The paths are 100% mapped. Returning to 5F.

<hr>