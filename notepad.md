<h1><code>Main</code></h1>

[Lessons Learned]
- Avoid over-mashing A during map transitions and battles. It causes UI desyncs, mistaken menu inputs, and turn hallucinations. Use targeted tools instead.
- Always carry Antidotes when exploring caves to prevent retreating from Poison damage.
- Map markers for defeated trainers (e.g. ☠️) should ONLY be placed AFTER returning to the overworld, never during a battle.
- If an item is not explicitly listed in the Game State Information sprite list, it DOES NOT EXIST.
- NEVER use dead reckoning. ALWAYS verify the Game State Player Position against the visual sprite position in the screenshot, as the Game State can sometimes be stale after a battle!
- EXHAUSTIVE EXPLORATION: NEVER declare an area a dead end until you have physically bumped into the absolute furthest boundaries of the space. Walk the entire perimeter! Stopping short leads to massive routing failures.
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
- Ultimate Secret Key Plan Execution Start: Turn 46422

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
- [PokeMart Mechanics] Gen 1 Mart inventories do NOT scale with badges. They are fixed to their location. Celadon Dept Store 2F is fixed to Super Potions and Great Balls. Must visit late-game cities (Saffron, Fuchsia, Cinnabar) for Hyper Potions, Ultra Balls, and Full Heals.
[Run Status]
- Post-game exploration active.

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
- [Turn 37262] Defeated Giovanni in Silph Co. 11F and received the Master Ball from the President. Silph Co. liberation complete!
[Zapdos Quest]
- Status: Located water access on Route 10. Requires using Cut on the bush at (4, 9).
- Next Steps: Cut the bush, Surf south to the Power Plant, and navigate the facility to catch Zapdos.

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
- [Turn 54320] Collision Error: The Indigo Plateau lobby (Map 0_9) has invisible collision barriers! Walking East from the center hallway (X=10) is blocked at X=11. The visual tile `TYPE_3fe2` at (11, 11) acts as a solid wall. I must find a different path to the PC.
- [Route 24] `TYPE_2889` is a solid mountain wall. `TYPE_4e8c` appears to be water. Always verify `TYPE_` IDs instead of relying on visual patterns like 'checkered' which can be mountains.

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
- Viridian Mart: Sells Poke Ball, Antidote, Parlyz Heal, Burn Heal. (Basic early game items).

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
- Route 24 Bridge is at X=20.
- From Pokemon Center (19, 17) to Bridge: Walk WEST to X=8, go NORTH to Y=12, walk EAST to X=20, then NORTH onto the bridge.
- Route 5 is accessed by walking through the Robbed House (27, 11) to bypass the south Cut tree.

# Post-Game Unknown Dungeon Access
- From Cerulean City Pokemon Center (19, 17), walk West to X=8, North to Y=12, East to X=20, and North onto the Route 24 bridge.
- Enter Route 24 (Map 0_35). Walk North on the bridge to the grass at Y=15, then walk West to (7, 15).
- Stand at (7, 15), face South towards the blue water at (7, 16), and Surf.
- Surf South down the water channel at X=7, crossing back into Cerulean City (Map 0_3) at X=17.
- Navigate the water channel in Cerulean City: Surf South from (17, 0) to (17, 4), then West to (6, 4).
- From (6, 4), Surf South down the water channel to the Unknown Dungeon entrance.

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
- The main story is complete! We are now exploring the post-game, specifically the Unknown Dungeon.
- Hydro (Blastoise) is our main powerhouse at Lv70.
- Dugtrio is kept for Dig to escape dungeons quickly.
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
- PC Box 2 is currently active (7/20). Box 1 is FULL (20/20).

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
- Turning vs Stepping: The game harness AUTOMATICALLY handles turning to face the correct direction before walking. You ONLY need to press a direction once to turn AND step. Do not manually add extra presses for turning, even in custom tools like move_sequence.
- Ledges & Obstacles: Gym statues have 2-tile bases. Ledges (like the water barriers in Cerulean Gym) act as one-way drops or solid walls depending on the side. 
- ALWAYS use short, 1-3 step movements to test unfamiliar collisions before committing to long tool sequences.
[Gen 1 Movement Mechanics]
- HARNESS AUTOMATION: The harness automatically handles turning. Pressing a direction ALWAYS results in a step (or a bump if blocked). DO NOT add extra presses just to turn!
- Bumping: To face a solid object (like a Cut bush), simply press the direction towards it. You will bump it and end up facing it.
- [Gen 1 Ledge Mechanics] Ledges can face South OR East/West! Turn 33137 PROVED that an East-facing ledge (TYPE_44f6) at (23, 28) in Fuchsia City CAN be jumped by walking Right into it. Previous assumption that only South-facing ledges work is false.
- HM FIELD MOVES: You MUST face the target tile (e.g., Cut bush, Water) BEFORE opening the Start Menu. The game checks your facing direction at the exact moment you select the move in the menu. Being adjacent is not enough.
- [Cycling Road] Route 17 has an automatic downward slope that forces the player South. Travel NORTH is IMPOSSIBLE with this harness due to the 500ms input delay allowing gravity to trigger. Must use Eastern routes to travel North.
- VISUAL CUES TRUMP TYPE LABELS: Always inspect the actual pixel art of a tile. A tile labeled `TYPE_3fe2` (floor) might visually contain the bottom half of a potted plant, a dark line indicating a one-way ledge, or the top of a desk (different color). If it looks like an obstacle, treat it as one, even if the label says otherwise. Don't blindly trust `TYPE_` labels without visual confirmation.
- [Gen 1 Field Moves] The STRENGTH effect is DEACTIVATED after every wild Pokemon encounter or trainer battle! You must re-open the party menu and use Strength again to continue pushing boulders.
- [Boulder Pushing] Pushing a boulder consumes your step! You do NOT automatically step into the tile the boulder vacated. To push a boulder multiple times in a row, you must alternate: Push (bump), Step (into vacated tile), Push (bump), etc.

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
[Gen 1 Mechanics]
- STRENGTH DEACTIVATION: The effect of Strength (allowing you to push boulders) is completely deactivated if you enter a battle (wild or trainer). You MUST open the Party menu and use STRENGTH again after every battle to continue pushing boulders!
- [Vitamins] If a stat booster (HP UP, IRON, CARBOS, CALCIUM, PROTEIN) says "It won't have any effect.", it means the Pokemon's Stat Exp (EVs) for that stat are already maxed out (or above the vitamin cap of 25600). Pokemon that have been used extensively in battle (like a starter) will likely hit this cap and cannot use vitamins.

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
- Gen 1 Menu Mechanics: The start menu features cursor wrapping, but the party menu DOES NOT. Both feature cursor memory. Always do menu navigation step-by-step or use state-aware tools.
- Cursor Memory: In Gen 1, the cursor position in menus (like the Party screen) is often remembered between opens. Always verify the blinking cursor position before mashing A or using a tool, especially when returning from a sub-menu, as it might wrap or stay where it was.
- [Turn 6149 Reflection] The party menu cursor remembers its last position even when accessed from the ITEM menu. Always verify cursor position before using an item!
- [Turn 6151 Reflection] CRITICAL: The Game State inventory list is ALPHABETIZED and does NOT match the in-game bag's chronological order. Never use Game State indices for item tools. Manual counting/scrolling is required!

# Menu Navigation
- Gen 1 Menus (Items, Pokemon, PC) have cursor memory! The cursor stays where you last left it. Always visually verify the cursor position or track it carefully before using tools that navigate menus blind.
- The Party Menu DOES wrap vertically when pressing Down (Bottom -> Top). It retains cursor memory, so always verify current_index.
- Inventory Mechanics: To free an inventory slot occupied by a stacked item (like Poke Balls), the ENTIRE stack must be tossed or used. Tossing just one from a stack of multiple does not free the slot.
- WARNING: Pressing START in the item menu does NOT close the menu. It selects the item below the cursor and can trigger accidental item usage. ALWAYS use B to exit menus.
- Gen 1 Item Bag Wrap-around: Pressing Up at the top item wraps to CANCEL, then pressing Up again wraps to the bottom item. Mashing Up will endlessly loop the menu, not reset the cursor to the top!
- Gen 1 UI Quirks: The OVERWORLD ITEM menu WRAPS when navigating past the top/bottom. However, the BATTLE ITEM menu DOES NOT wrap! Keep this in mind when navigating items in battle.
- Menus with introductory text (like Vending Machines) can eat inputs if the text is still rendering or waiting for input to clear. Always use sleep commands (e.g., 'sleep 500') or wait visually before sending menu navigation inputs.
- Overworld signs/interactables can have multiple pages of text. If a text box isn't closing with 'B', check for a down arrow indicating more text and advance it with 'A' to prevent movement soft-locks.
- [Party Sub-Menu] Pokemon with Field Moves (Cut, Surf, Fly, etc.) have the field move at the top of their sub-menu. This pushes STATS to the 2nd slot and SWITCH to the 3rd slot. Standard Pokemon have STATS 1st and SWITCH 2nd. Custom tools like swap_pokemon will fail if they assume a fixed position for SWITCH.
- [Party Menu Cursor Memory] The cursor position is remembered across completely different access methods! If you use an item on Pokemon #2 via the ITEM menu, the next time you open Start->POKEMON, the cursor will STILL be on Pokemon #2. Never assume it resets to index 1.
- Fly Map Navigation [EMPIRICALLY PROVEN Turn 55061-55078]: The Fly map is a 1D list. Left/Right do nothing. 'Up' moves FORWARD. 'Down' moves BACKWARD. The list WRAPS.
  The cursor DEFAULTS to Pallet Town (index 1) upon opening, regardless of your current location. (Observed Turn 55060).
  The exact order (Up / Forward) is: Pallet Town -> Viridian City -> Pewter City -> Cerulean City -> Lavender Town -> Vermilion City -> Celadon City -> Fuchsia City -> Cinnabar Island -> Indigo Plateau -> Saffron City -> (wraps to Pallet).
  Note: Unlocking new fly locations SHIFTS the indices! Always visually verify the destination before pressing A.
- KO Switch Cursor Memory: When you select YES to "Will [PLAYER] change POKEMON?" after defeating an enemy, the cursor in the party menu STARTS on the currently active Pokemon, NOT index 1!
- `execute_battle_turn` has been fixed to use explicit `main_cursor` state instead of blind Up/Left resets.
- PC Deposit Menu Wrap: Pressing 'Up' at the very top of the deposit list (index 1) DOES NOT wrap to the bottom. It stays at index 1. Verified Turn 37675.
- MAIN BATTLE MENU CURSOR MEMORY: The main battle menu (FIGHT/PKMN/ITEM/RUN) retains cursor memory between turns! If you use an item, the cursor starts on ITEM next turn. You must explicitly reset it or account for it in macros.
- [Turn 54211] WILD ENCOUNTER CURSOR RESETS: Running from a wild encounter completely RESETS both the Start Menu cursor (back to index 1: POKéDEX) and the Party Menu cursor (back to index 1: Lead Pokemon). Never assume cursor memory persists after a wild battle!
- PC Withdraw Cursor Reset: After withdrawing an item from the PC, the cursor DOES NOT retain its position. It resets completely to index 1 (the top of the list).
- [PC Menu Reset]: Backing out of Bill's PC and re-entering Gem's PC completely resets the main PC menu cursor to index 1 ("WITHDRAW ITEM").
- [Item Menu Cursor Reset]: Using a TM and completing the teaching process completely resets the Start Menu's ITEM bag cursor to index 1 (the top).
- [Item Menu Cursor Memory] The Party Menu cursor retains its position even between repeated TM uses! If you teach a TM to Pokemon #2, the next time you use a TM from the bag, the Party Menu cursor will start on Pokemon #2.
- [Trainer Battle Cursor Reset]: Defeating a trainer completely resets the overworld Start Menu cursor back to index 1 (POKéDEX). Confirmed after Bruno (Turn 54761).
- [Start Menu Cursor Memory]: Using an HM like Fly from the Party menu retains the Start Menu cursor on POKéMON for the next time you open it. It DOES NOT reset to index 1!
- [Field Move UI Flow]: After using SURF from the Party Menu, the text "GEM got on [PKMN]!" appears. You must press A or B to clear this text. Afterward, you are returned to the START MENU, not the overworld! You must press B again to exit the Start Menu before you can move.
- [HM Field Move Tool Use] The `use_field_move` tool is inherently fragile because Gen 1 menus have cursor memory and wrap-around. I MUST visually verify the cursor is on POKEMON in the Start menu, AND visually verify the cursor in the Party menu, before calling the tool. Blind macros without visual confirmation are a recipe for disaster.
- [Cursor Blinking Hazard] If the selection arrow (→) is NOT explicitly visible in the text dump for a menu (like the Party Menu), it means the arrow was blinking off when the screenshot was taken. DO NOT assume it has reset to index 1! It is likely still at its previous memory location. Wait a turn or trust your exact tracking of cursor memory. I assumed it was on Hydro (index 1) because I didn't see an arrow, but it was actually still on Audrey (index 4) from my previous Cut usage!
- [Party Menu Text Extraction] The text extraction for the Party Menu interleaves the HP text on a new line. The selection arrow `→` is unreliable and can appear on different lines depending on OCR. Always rely on the physical screen image: look for the black triangle `▶` at the VERY LEFT EDGE of the screen (X=0). Index 1 = Y=4, Index 2 = Y=5/6, Index 3 = Y=6/7, Index 4 = Y=7/8. Do NOT look at X=4!
- [Field Move Failure UI] If a field move fails (e.g., "No SURFing on HYDRO here!"), pressing 'A' to clear the message returns you to the Party Menu, NOT the overworld. You must press 'B' repeatedly to exit the menus entirely before attempting to move again. I got trapped in the Party Menu because I assumed it would close automatically!

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
[Dig/Teleport Mechanics]
- Dig and Escape Ropes return you to the last Pokemon Center where you ACTUALLY HEALED your Pokemon. Simply entering and exiting a Pokemon Center does NOT set the warp point. You must speak to Nurse Joy and complete the healing dialogue. (Proved Turn 55685 when Dig warped me from Unknown Dungeon back to Pallet Town because I skipped healing in Cerulean City).

<hr>

<h1><code>Locations/Route9</code></h1>

# Route 9 (Map 0_20)
- Route 9 and Route 10 North share the same Map ID (0_20). X=0 is the Cerulean City border. X=59+ connects to Route 10 proper.
- Cerulean City connects to Route 9 at (0, 8) and (0, 9).
- To navigate Route 9, you MUST Cut the bush at (5, 8) to access the eastern sections.
- Previous notes claiming the Cut bush leads to a dead end were hallucinations. Explore the area east of the bush carefully to find the path forward.
- The water channel leading to the Power Plant is located at the far East end of the route (near X=59).
- [Route 9 Choke Point] At X=14, there is a solid rock wall from Y=7 to Y=11. To continue East from the Cut bush (Y=8), you must walk Right to X=12, Down to Y=10, and jump the South-facing ledge at Y=11 to land in the Y=12 lane. The Y=12 lane bypasses the X=14 wall.
- [Route 9 Navigation] From the Y=12 lane, the path East is blocked at X=24 by another rock wall extending South (Y=12 to Y=16). To bypass this, walk North to Y=11 and continue East. Route 9 is a zigzag of rock walls forcing alternating North/South lane changes.
- [Route 9 Navigation] From (38, 12), the path East is blocked at X=42 by a solid rock wall (from Y=8 to Y=13). To continue, I can either jump the ledge at Y=13 to use the lower lane (Y=14/15), or head North at X=41 to find the Northern path. Since my notes say the water is only accessible via the Northern path (Y=2 to Y=5), I will head North at X=41.
- [Route 9 Navigation] At X=41, heading North from Y=12 leads into the line of sight of a Hiker trainer at (41, 7) facing South. Prepare for battle when taking this path!
- [Route 9 Navigation] At X=41, heading North from Y=12 leads to a gap in the ledges at (39, 5). Passing through this gap to Y=4 allows you to bypass the rock wall at X=46 (which blocks Y=5 to Y=12). The Northern path continues East! My previous dead-end assumption was a hallucination from incomplete exploration.
- [Route 9 Navigation] The lower lane (Y=14/15) ending at X=54 is a DEAD END containing only a grass patch. The ledges above it at (52, 13) and (53, 13) are South-facing, indicating the path from the North drops down here. To continue East to the water, I MUST take the Northern path at X=41 (past the Hiker). My previous assumption that X=41 North was a dead end was wrong! I must backtrack West.
- [Route 9 Lower Lane] Backtracking West along the lower lane (Y=14). The North edge is mostly a continuous cliff/ledge at Y=13, preventing access to the upper lanes. I need to find the specific gap or stairs that allow me to transition back to the Northern path.
- [Route 9 Navigation] Found a gap in the South-facing ledge at (29, 13). This gap allows transitioning from the lower Y=14 lane back up to the middle Y=12 lane. Route 9 requires using these specific gaps to navigate between the horizontal lanes.
- [Route 9 Navigation] Continuing East along the Northern path (Y=2 to Y=4), you reach a South-facing ledge at X=50/51, Y=5. Jumping down this ledge lands you at Y=6. From here, walk South to Y=8 to find a gap in the rock walls allowing passage East. Be aware of a Hiker at (48, 8) facing East.

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

# Route 10 (Map 0_21)
- Map 0_21 represents the ENTIRETY of Route 10, both North and South of Rock Tunnel!
- It connects Route 9 at the top (X=59 on Map 0_20 transitions to Map 0_21) and Lavender Town at the bottom.
- Rock Tunnel is located in the middle of this route.
- The water channel leading to the Power Plant is located at the top-left (West side) of this map, accessible just after transitioning from Route 9.
- To reach the water from the Route 9 transition, walk South through the gap in the trees at X=2/3, Y=4.
- Surf South down this water channel to reach the Power Plant!
- South of Rock Tunnel: Defeated Hiker around (3, 62) and Pokemaniac at (11, 64). Leads to Lavender Town.
- [Water Channel] From the North access at (2, 5), Surf South all the way to Y=46. The channel then turns East.
- [Water Channel] At (3, 47) there is a 1-tile dead end pocket. The main Eastward channel is at Y=46. From (3, 46), Surf East!
- [Water Channel] Surfing East along Y=46, the channel turns North at (17, 46).
- [Water Channel] Surfing North along X=17, you pass by the Rock Tunnel Pokemon Center, which is located on land to the West around (11, 19).
- [Water Channel] Addressing Overwatch: The channel physically forces me North here (bounded by land on both East and West). It appears to loop around the Rock Tunnel landmass. I am following the only available water path, trusting it leads to the Power Plant.
- [Water Channel] The channel forms a complete loop around the Rock Tunnel landmass! I started at (2, 5), went South, East, North, and West, arriving back at the top of the loop near (2, 2).
- [Power Plant Search] Since the Power Plant was not on the inner loop, it must be accessible via a branch or shore on the OUTSIDE of the loop. I need to carefully check the East side of the East channel (X=17) and the South side of the South channel (Y=46). I will surf back East and South to re-examine the outer boundaries.
- [Power Plant Search] Scanning the East boundary (X=18/19) of the Eastern water channel (X=17) moving South.
- [Power Plant] FOUND IT! The Power Plant is located on a landmass accessed by surfing South along the East channel, then West along the South channel to a shore at (9, 45). The building is located in the NW corner of this landmass.
- [Power Plant Path] Landed at (9, 45). Walked North to (9, 44) and was spotted by a Pokemaniac at (10, 44) facing Left.

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
## Silph Co 7F
- Pidgeot Lv 37
- Gyarados Lv 38 (Moves: Bite, Leer)
- Growlithe Lv 35
- Alakazam Lv 35
- Venusaur Lv 40
## Route 22 (Late Game)
- Encountered at Turn 49371
- Pidgeot Lv 47
- Rhyhorn Lv 45
- Gyarados Lv 45
- Growlithe Lv 47
- Alakazam Lv 50
- Venusaur Lv 53

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
- Depositing TMs into PC to free up space for Pokemon Mansion.
- Need to navigate from BILL's PC back to GEM's PC.
- Deposited TM03 (Turn 37618)
- Deposited TM36 (Turn 37650)
- Deposited TM46 (Turn 37656)
- Deposited PIXEL and withdrew OMEGA (Mewtwo) from Box 2 to Party.

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

[Points of Interest]
- Pokemon Center: (9, 29)
- Silph Co: (18, 21) - CLEARED
- Fighting Dojo: (26, 3) - CLEARED
- Saffron Gym (Sabrina): (34, 3) - NEXT TARGET

[Notes]
- Guard gates are now open after giving the thirsty guard a drink.
- Team Rocket has been cleared from the city.

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
- Trainer Position Reset Hypothesis: FAILED. Defeated trainers that step towards the player to initiate battle (like the 5F Grunt at 28, 4) DO NOT unblock the 1-tile pathway even after leaving the floor and returning via elevator. Their sprite permanently blocks the path.
- Card Key Usage: CONFIRMED! You do NOT use the Card Key from the item menu! Simply face an electronic door and press 'A' to open it. It will say "Bingo! The CARD KEY opened the door!"
- Text Box Mechanics: Pressing 'B' on a text box with a down arrow (▼) simply advances to the next line of text, it DOES NOT close the text box. This means any movement inputs sent immediately after 'B' will be eaten if there are more lines of text to render! Always ensure the text is fully complete before appending movement to a sequence.
- [Gen 1 Battle Mechanic] Wild Vulpix used ROAR. The text said "HYDRO ran away scared!" and the battle ended immediately. Roar forces the player to run away in wild battles!
- [50-Turn Reflection] Text Box Input Eating: The "Got away safely!" text after running from a wild battle remains on screen and will eat subsequent directional overworld inputs until cleared with 'A' or 'B' (or wait). Always clear it before moving.
- Battle Intro Input Eating: Do not use menu navigation tools (like run_battle or execute_battle_turn) on the turn a wild encounter starts (when 'Wild [PKMN] appeared!' is on screen). The button presses will be consumed as text advances, and you will be left at the main battle menu on the next turn.
[Turn 41952 Dig Reflection]
- Dig successfully warped me to Saffron City (Map 0_10) Pokemon Center! I then accidentally tried to use Dig again in the Saffron overworld, which caused Oak's warning message. Now I am using Fly to get back to Cinnabar Island.
- [Statue Interaction]: Statues in the Pokemon Mansion must be interacted with from the FRONT (standing below them and facing UP). Interacting from the side (facing Left/Right) does nothing and acts like a normal wall.
- [Turn 46985] EMPIRICAL PROOF OVERRIDES OVERWATCH: The overwatch agent in Turn 46979 claimed the doors at (9, 7) were open in State B because the "red barriers" were gone. This was visually and physically FALSE. I bumped into (9, 7) four times from (10, 7) in Turn 46985 and did not move. Tile (9, 7) is a yellow/orange striped tile (`TYPE_a83b`), which is the visual representation of CLOSED VERTICAL electronic doors. The doors at X=9 are absolutely CLOSED in State B. I must toggle the switch at (18, 3) back to State A to open them.
- [Turn 50564] Anomaly: Strength was activated on Turn 50559, but pressing A on the boulder on Turn 50563 said "This requires STRENGTH to move!". Strength somehow deactivated or failed to register. Possibility 1: The failed Surf attempt on Turn 50558 messed up the state. Possibility 2: Spamming B to exit the menu somehow cancelled the field move activation. I will re-activate it manually.
- [Turn 50574] Anomaly Resolved: Spamming B to exit the Party menu immediately after activating Strength cancels the activation! I must exit the menus slowly or use 'A' to back out where possible to ensure the flag is set.
- [Turn 50620] Start menu cursor was on EXIT, not POKéMON. Cursor memory persists. Navigating UP 5 times to reach POKéMON.
- [Turn 50697] Party menu cursor reset to index 1 (HYDRO) after changing floors via stairs to reset the boulder.
- [Gen 1 Battle Mechanic] After using an item in battle, the main battle menu cursor remains on the ITEM option. You must account for this cursor memory or manually reset it before using execute_battle_turn, otherwise it will just open the ITEM menu again!
- [Gen 1 Battle Mechanic] 2-Turn Move Sleep Lock: If a Pokemon is put to Sleep while charging a two-turn move (like Skull Bash), the player is completely LOCKED OUT of the battle menu. The game automatically attempts to execute the move every turn, resulting in 'is fast asleep!' until the Pokemon wakes up. Items like the Poke Flute cannot be used during this time!
- [Turn 51025] Battle Mechanic: The switch prompt "Will [PLAYER] change POKEMON?" can eat inputs if 'B' is pressed while the text is still scrolling out. Wait for the YES/NO box to fully appear before pressing 'B'.
- [Gen 1 Battle Mechanic] 2-Turn Move Confusion Cancel: PROVEN. If a Pokemon is confused and hurts itself while charging a two-turn move (like Skull Bash), the move is instantly cancelled and the player regains control of the battle menu on the following turn. (Correction: I hallucinated the "But, it failed!" message. I just selected Skull Bash again and Hydro hurt himself a second time).
- Switch Intro Input Eating: Just like wild encounters, the "Go! [PKMN]!" text when sending out a new Pokemon will eat inputs if you try to use execute_battle_turn immediately. The 'A' press will be consumed to advance the text, and subsequent directional inputs will navigate the main battle menu incorrectly (e.g., ending up in the ITEM menu). Always clear the intro text first!
- Step 1: Pallet Town -> Down -> Saffron City.
- Step 2: Saffron City -> Down -> Indigo Plateau.
- Step 3: Indigo Plateau -> Down -> Cinnabar Island.
- Step 4: Cinnabar Island -> Down -> Fuchsia City.
- Step 5: Fuchsia City -> Down -> Celadon City.
- Step 6: Celadon City -> Down -> Vermilion City.
- Step 7: Vermilion City -> Down -> Lavender Town.
- Step 8: Lavender Town -> Down -> Cerulean City.
- Step 9: Cerulean City -> Down -> Pewter City.
- Step 10: Pewter City -> Down -> Viridian City.
- [Turn 55645 Overwatch Rebuttal] The Overwatch agent claimed I empirically confirmed a rock wall at (9, 4). This is FALSE. In Turn 55614, my sequence from (9, 3) was `DDLLLLLLLLLUUR`. I visited 4 tiles. The exact trace is: Down to (9, 4), Down to (9, 5), Left (bump 8, 5), ..., Up to (9, 4), Up to (9, 3), Right (bump 10, 3). The 4 tiles visited were (9,3), (9,4), and (9,5). (9,4) and (9,5) are empirically passable. The wall I bumped into was (8, 5).
- [Overwatch Rebuttal Turn 55772] The Overwatch agent suggested making `use_field_move` robust by mashing 'Up' 6 times to guarantee index 1. However, as documented in my Mechanics/UI notes, the Gen 1 Party Menu WRAPS. Mashing 'Up' will endlessly cycle through the party and does NOT reset the cursor to index 1. The only safe way to use the Party Menu is to visually verify the blinking cursor's position before navigation. I will strictly rely on visual confirmation from now on.
- [Menu Desync Error]: If you misread the starting cursor position and use a navigation tool, the resulting sequence will likely select the wrong option (e.g., trying to FLY instead of SURF). Always completely back out to the overworld with B-spam when this happens to guarantee a clean state.
- [Map Topology Resolved] Map 0_20 encompasses BOTH Route 9 (X=0 to ~59) and Route 10 (X=60+). Cerulean City (39, 16) connects directly to Route 9 at (0, 8). My assumption of a 'massive glitch' was a hallucination caused by not realizing Route 9 and 10 share the same Map ID.
- [Cut Bush Mechanics] Stationary Cut bushes DO NOT appear in the Game State Info sprite list or NPC Movement Tracker (which only tracks moving objects). They must be identified visually by their tile graphic (e.g., TYPE_2889) and tested empirically by using the Cut field move. Do not rely on the sprite list to determine if a tree is cuttable.
- [Cursor Visibility Check] In Turn 57876, the Party Menu cursor was invisible (blinking off) when the screenshot was taken. Instead of guessing its position based on memory (which has failed me multiple times), I am intentionally NOT pressing any buttons this turn. I will only update this notepad. Since the emulator runs continuously, the next turn's screenshot should capture the cursor in its "on" state, allowing me to visually verify it safely.
- [Cursor Blinking Wait] Intentionally skipping button presses on Turn 57910 to wait for the Party Menu cursor to blink 'on' in the text log. Precision is more important than speed.

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

<h1><code>Locations/SilphCo_1F_to_6F</code></h1>

# Silph Co. (Saffron City) - Lower Floors

[Navigation]
- 1F (Map 0_181): Elevator doors are at (20, 0). Exit to Saffron at (10, 18).
- 1F Navigation: There are desks blocking the path East at Y=17 starting at X=12. Must walk at Y=16 or higher to go East.
- 1F Navigation: Path North through the center (X=14 to X=17) is blocked by a zigzag of potted plants (Y=10) and couches/glass walls (Y=8, Y=9). Must bypass these partitions by walking around the left side (X=11) or right side.
- 1F Navigation: Path North at X=9 is blocked by monitors at Y=6 and Y=7. Must use X=8 or further West to bypass the partitions and head North.
- Elevator Interior (Map 0_236): This 4x4 room is the inside of the elevator. The control panel is at (3, 0). Stand at (3, 1) and press A facing Up to select a floor. Exit the elevator by moving DOWN onto the red tiles from (1, 2) or (2, 2). Pressing Down at X=0 does not work.
- Elevator Menu: The floor selection menu DOES NOT wrap! Pressing Up at 1F does nothing. To reach 11F from 1F, you must press Down 10 times.
- Electronic Doors: Red barriers block paths throughout the building. They require the Card Key to open. We need to find it ASAP to explore fully.

[Floors 2F-6F]
- 2F (Map 0_207): Elevator at (20, 0). Stairs DOWN to 1F at (24, 0). Stairs UP to 3F at (26, 0). Hallways extend East and West from the elevator.
- 2F Navigation: West hallway from the elevator is a dead end at X=12. A solid wall at X=11 blocks the path West. A Scientist is visible behind the wall at (10, 1). There is a warp pad at (13, 3).
- 2F Navigation: The warp from 3F (27, 3) lands at (3, 3) in a small room on the West side of the building. There is an electronic door blocking the path East at (4, 4) and (5, 4) (OPENED). A Silph Employee at (10, 2) gives TM36 (Selfdestruct).
- 2F Navigation: East hallway from the elevator leads to stairs at X=24 and X=26. South of the stairs is a woman at (25, 7). She mentions "I work for SILPH. What can I do?".
- 2F Navigation: Reached via warp pad from 6F (23, 3). The warp lands at (9, 15) in a small isolated room. A Scientist is at (5, 14). A woman is at (4, 13). No items or further progress here; it's a dead end.
- 3F (Map 0_208): Elevator at (20, 0). Stairs DOWN to 2F at (26, 0). Stairs UP to 4F at (24, 0). Electronic door at (20, 4) blocks the path South. Path West is open.
- 3F Navigation: West hallway ends in a room with a warp pad at (3, 3) and a solid wall at X=0. No path South; it's a dead end connecting to 5F. 3F requires the Card Key to progress. Item ball at (8, 5) is accessible by opening the electronic door at (9, 8)/(9, 9).
- 3F Navigation: East hallway from the stairs has a warp pad at (27, 3). The path South is blocked by desks at Y=4.
- 3F Navigation: The central area is blocked by an electronic door at (20, 4) and (17, 8). Opening (20, 4) gives access to a Grunt at (20, 7) and a path South. The path South connects to the East side of 3F via a gap at (21, 8)/(21, 9). The East area has a warp pad at (23, 11) bounded by a wall at Y=13. The warp at (23, 11) connects to a Southern hallway at (27, 15). This Southern hallway (Y=15/16) runs West all the way to a warp pad at (3, 15). Opening (17, 8) gives access to a room with a warp pad at (11, 11).
- Warp Connection: 3F warp at (11, 11) connects to 7F warp at (5, 3).
- 4F (Map 0_209): Stairs UP to 5F at (26, 0). Stairs DOWN to 3F at (24, 0). Grunt at (12, 14).
- 4F Navigation: Warp at (11, 7) lands in a partitioned area. Scientist at (14, 6). Electronic doors at (12, 8) and (13, 8) block South. Second warp pad located at (17, 3).
- 4F Navigation: The area isolated by the warp pad at (17, 11) is bounded by an electronic door at (5, 12) and walls. The warp pad itself is blocked from the South by desks at Y=12; access it via X=13. It's a dead end without the Card Key.
- 4F Navigation: East of the stairs, the path South at X=26 is blocked by a Grunt at (26, 7). Bypassing via X=23 leads to an empty loop (X=26/28, Y=8 to Y=16). A solid wall at Y=4 blocks access to the room to the North.
- 4F Navigation: West corridor (Y=13/14) from X=15 leads West past X=13. The item ball at (3, 9) (Full Heal) is accessed by opening doors at (4, 12)/(5, 12). Inside this locked room are two more item balls at (4, 7) (Max Revive) and (5, 8) (Escape Rope).
- 4F Navigation: West of the elevator, a path leads South down an open hallway at X=19 all the way to Y=13. There are NO doors at (18, 10)/(19, 10). The path North from (19, 5) goes to Y=3 and wraps East back to the stairs. The locked area West of X=18 (containing a warp pad and electronic doors) must be accessed from the South via X=13.
- 5F (Map 0_210): Elevator at (20, 0). Desks block the south path immediately out of the elevator at Y=4. West hallway leads to a Silph Employee at (8, 3) (Master Ball dialogue). Bypass him via X=9.
- 5F: Warp pad at (11, 5). Warp pad at (9, 15). Warp pad at (3, 15).
- 5F Navigation: The path South at X=14 leads to a dead-end room with a warp pad at (11, 5). To explore the rest of the floor, use the path South at X=22 (East of the elevator).
- 5F Navigation: To reach the East/Central area from the elevator, walk down X=22/23 to Y=5, East to X=26, then South. A Pokemon Report is on the desk at (25, 10). To reach the central room, continue South down X=26 to Y=14, then head West.
- 5F Navigation: Item ball at (21, 16) is the CARD KEY! It is accessible via a hidden 1-tile wide hallway running East at Y=16 from the bottom of the West corridor (starts at X=9, Y=16).
- 5F Navigation: Wall at X=27 blocks access to X=28 from the central room. Wall at Y=15 blocks access to the item ball at (21, 16) from the central room.
- 5F Navigation: The central room is bounded by an electronic door at (15, 10) (OPENED) on the West and desks at Y=15 on the South. A Silph Employee is inside at (18, 10). A Pokemon Report clipboard is on the desk at (22, 12). The item at (21, 16) is unreachable from here.
- 5F Navigation: East of the elevator at X=24 is a path South. It contains a warp pad at (27, 3), a Grunt at (28, 4), and a clipboard at (24, 6). The Grunt blocks the path South at X=28.
- 5F Navigation: The Grunt at (28, 4) is defeated but physically blocks the 1-tile wide hallway. Therefore, the path South at X=28 is permanently inaccessible.
- 5F Stairs: Stairs UP to 6F at (24, 0). Stairs DOWN to 4F at (26, 0).
- 5F Navigation: West corridor leads South to a true dead end at Y=16. Silph Employee at (8, 16) (Master Ball dialogue). Electronic door at (7, 12). Warp pad at (9, 15).
- 6F (Map 0_211): Elevator at (18, 0). Stairs DOWN to 5F at (14, 0). Stairs UP to 7F at (16, 0). Electronic doors at (10, 4) and (11, 4). Grunt at (17, 3). Trainer at (10, 6).
- 6F Navigation: The path West from the stairs leads to an open hallway going South at X=7 and X=6. X=8 is a wall blocking the path East at Y=4 to Y=6. There are electronic doors at (2, 1) and (3, 1). There is a warp pad at (3, 3).
- 6F Navigation: Warp at (3, 3) lands in a partitioned area on the West side of 6F. This area is completely empty and a dead end.
- 6F Navigation: Following the hallway South leads to a Scientist at (7, 8). The path continues South to an intersection at (6, 12). An Item Ball to the West at (3, 12) is blocked by an electronic door at X=5.
- 6F Navigation: East of the intersection at (6, 15) is a hallway leading East. A Grunt is at (14, 15).
- 6F Navigation: The hallway continues East from (14, 15). A solid wall at Y=14 blocks the path North. A Grunt is visible behind the wall at (18, 13). The hallway continues East past X=23.
- 6F Navigation: The hallway continues East from (14, 15) to a dead end at X=25. The only path forward is North at X=24.
- 6F Navigation: The path North at X=24 leads to a warp pad at (23, 3). A room is visible to the West with two NPCs at (20, 6) and (21, 6), blocked by a wall at X=23.

[Warp Connections 1F-6F]
- Warp Connection: 5F warp at (11, 5) connects to 3F warp at (3, 3).
- Warp Connection: 4F warp at (17, 3) connects to 6F warp at (3, 3).
- Warp Connection: 6F warp at (23, 3) connects to 2F (Map 0_207) warp at (9, 15).
- Warp Connection: 3F warp at (27, 3) connects to 2F warp at (3, 3).
- Warp Connection: 3F warp at (23, 11) connects to 3F warp at (27, 15) (Intra-floor).
- Warp Connection: 3F warp at (3, 15) connects to 5F warp at (3, 15). 5F (3, 15) is a room containing TM09 (Take Down) at (2, 13), separated from the main 5F hallway by an electronic door at (7, 12)/(7, 13).

<hr>

<h1><code>Locations/SilphCo_7F_to_11F</code></h1>

# Silph Co. (Saffron City) - Upper Floors

[Floors 7F-11F]
- 7F Main (Map 0_212): Elevator at (18, 0). Stairs DOWN to 6F at (22, 0). Electronic doors block the path South at (20, 4) and (21, 4). Grunt at (20, 2). The path East of the stairs is a dead end. 7F Main is fully explored without a Card Key.
- 7F (Map 0_212): Warp at (21, 15) lands in a partitioned area. A Grunt is at (19, 14) and electronic doors at (20, 12) and (21, 12) block the path North. Desks at Y=12 block access to the item ball at (24, 11) from the South. Dead end without Card Key.
- 7F Navigation: Warp at (5, 3) from 3F (11, 11) lands in an isolated room on the West side. Defeated Rival Gary here. Silph Employee at (1, 3) gives Lapras (Lv 15).
- 8F Main Navigation: Elevator at (18, 0). Grunt at (19, 2). Path goes West to X=15, then South.
- 8F Main Navigation: Path East of elevator loops around (17, 5) to (24, 12) and connects South to the East hallway. No Card Key here.
- 8F Main Navigation: Hallway at X=15 goes South to Y=15. Grunt at (12, 15). Need to explore West of this Grunt.
- 8F Navigation: Warp at (3, 15) lands in an area bounded by a wall at Y=13. Another warp pad is visible at (3, 11) but blocked by this wall. Path continues East.
- 8F Navigation: Path from (3, 15) goes East, turning North at X=11, East at Y=14, and North again at X=21, continuing up to Y=7 where it opens up.
- 8F Navigation: Path North at X=21 leads to a room with potted plants. A South-facing ledge at (17, 8) forces a one-way drop into a 1x4 dead-end hallway from (17, 9) to (17, 12).
- 8F Navigation: Warp pad at (11, 9) connects to 8F warp at (3, 11). Path goes West to X=1, North to Y=2, and East to an NPC at (4, 2), bypassing the electronic doors at (4, 10).
- 8F Navigation: Finished mapping 8F. It is entirely a large connected loop with no Card Key. The paths are 100% mapped. Returning to 5F.
- 9F Main Navigation: Elevator at (18, 0). Path West leads to a South corridor at X=13. It ends at Y=13, with an electronic door blocking West at (11, 12). The tiles at (12, 9) and (12, 11) are just potted plants, NOT warp pads! 9F is fully explored without a Card Key.
- 9F (Map 0_233): Warp at (17, 15) lands in a partitioned area. A solid wall at X=14 blocks access to a Team Rocket Grunt at (13, 16) (one of the 4 Rocket Brothers!). A Grunt is accessible to the East at (21, 13).
- 9F Navigation: Path East is at Y=15. Grunt at (21, 14). Electronic doors at (18, 10) opened! The path North of the doors leads West to a dead end at X=15, and North to X=20 where it hits a wall at Y=4. West of (20, 5) are electronic doors at (18, 4) and (19, 4) which connect BACK to the elevator starting area. Opened (18, 4)!
- 9F Navigation: Path West from the elevator goes South down X=13. Grunt at (13, 13) (Rocket Brother) is defeated. Electronic door at (11, 12) is OPENED! The path leads West.
- 9F Navigation: Path North at X=24 leads West to a dead-end room with objects at (18, 4) and (19, 4) that require a Card Key.
- 10F (Map 0_234): Elevator doors at (12, 0). Scientist at (10, 2).
- 10F Navigation: From elevator, path goes South via X=11. Path West at Y=5 is a dead end (wall at X=7). Electronic doors at (10, 8) and (11, 8) block South (OPENED). Opening them gives access to the entire South-East area. Warp pad located at (13, 7).
- 10F Navigation: The South-East area (also accessible via warp at 13, 15) contains a wandering Silph employee, a warp pad at (9, 11), and a warp pad at (13, 15). Item ball visible at (5, 11) on the West side of a solid wall at X=7, which blocks access to the West side of 10F.
- 11F (Map 0_235): Elevator at (13, 0). Path from elevator goes East and West. A solid wall at X=13 separates the South area. NPC spotted at (10, 5) on the West side. I will explore the East side first.
- 11F Navigation: Path East from the elevator leads South down a corridor (X=14/15) bounded by a solid wall at X=13 and X=16. It ends in a complete dead end at Y=16. No Card Key here. Bounded by a Grunt at (15, 7).
- 11F Navigation: Path West from the elevator goes along Y=1/Y=2 to a dead end at X=4. A wall at Y=3 blocks access to the South where a Grunt is at (10,5) and a Boss at (7,5).
- 11F Navigation: The West strip (X=0 to X=3) is accessed via warp from 7F. Traveling South down X=3 leads past a Grunt at (3, 13) to an opening at Y=14. The path goes East to X=6, then North through electronic doors at (4, 13)/(5, 13) to enter the main Boss room.

[Warp Connections Upper/Cross]
- Warp Connection: 10F warp at (13, 7) connects to 4F warp at (17, 11).
- Warp Connection: 5F warp at (9, 15) connects to 9F warp at (17, 15).
- Warp Connection: 5F warp at (27, 3) connects to 7F warp at (21, 15).
- Warp Connection: 4F warp at (3, 15) connects to 10F warp at (13, 15).
- Warp Connection: 10F warp at (9, 11) connects to 4F warp at (11, 7).
- Warp Chain Analysis: The warp chain starting at 4F (3, 15) -> 10F (13, 15) -> 4F (11, 7) -> 6F (3, 3) is a complete dead end with no Card Key. Backtracking out.
- Warp Connection: 2F warp at (13, 3) connects to 8F (Map 0_213) warp at (3, 15).
- 9F Navigation: West of the electronic door at (11, 12) is a room with beds. A healing Nurse is located here at (3, 14)!
- [Reflection Turn 37172] The warp pad at 7F (5, 7) connects to 11F (3, 2). This warp is MANDATORY. It places the player on the West strip (X=0 to X=3) of 11F, which bypasses the solid wall at Y=3. This wall previously blocked access to Giovanni's room from the main 11F elevator area. I must now travel South down this strip to find an entrance into the main room.
- 11F Navigation: The Silph Co. President is located at (7, 5) in the boardroom. The large boardroom table covers X=6 to X=9, Y=6 to Y=8. Approach him from the left side (via X=5, Y=5).

<hr>

<h1><code>Bosses/TeamRocket</code></h1>

# Giovanni (Silph Co. 11F)
- Nidorino Lv 37
- Kangaskhan Lv 35
- Rhyhorn Lv 37
- Nidoqueen Lv 41

<hr>

<h1><code>Locations/SaffronGym</code></h1>

# Saffron City Gym (Map 0_178)

[Warp Pairs]
1. Entrance (11, 15) <-> BR Bottom-Right (19, 17)
2. BR Bottom-Left (15, 17) <-> BL Top-Right (5, 15)
3. BL Top-Left (1, 15) <-> TR Bottom-Right (19, 5)
4. TR Top-Left (15, 3) <-> MR Top-Left (15, 9)
5. MR Bottom-Left (15, 11) <-> TC Top-Left (9, 3)
6. TC Top-Right (11, 3) <-> TL Top-Right (5, 3)
7. TL Top-Left (1, 3) <-> TR Bottom-Left (15, 5)
8. MR Top-Right (19, 9) <-> BR Top-Right (19, 15)
9. BR Top-Left (15, 15) <-> TR Top-Right (19, 3)
10. BL Bottom-Left (1, 17) <-> TC Bottom-Right (11, 5)
11. TC Bottom-Left (9, 5) <-> ML Top-Right (5, 9)
12. ML Top-Left (1, 9) <-> MR Bottom-Right (19, 11)
13. ML Bottom-Left (1, 11) <-> TL Bottom-Right (5, 5)
14. TL Bottom-Left (1, 5) <-> MC Center (11, 11) [SABRINA'S ROOM]

[Unexplored Warps]
- BL (Bottom-Left): Bottom-Right (5, 17)
- ML (Middle-Left): Bottom-Right (5, 11)

[Notes]
- Sabrina is in the MC (Middle-Center) room. (DEFEATED)
- The trainer at (10, 1) in the TC (Top-Center) room is a regular Channeler.

<hr>

<h1><code>Bosses/Sabrina</code></h1>

# Gym Leader Sabrina (Saffron City)
- Kadabra Lv 38
- Mr. Mime Lv 37
- Venomoth Lv 38
- Alakazam Lv 43

<hr>

<h1><code>Locations/Route21</code></h1>

# Route 21

[Navigation]
- Traveling South from Pallet Town via Surf.
- Starting at (7, 0).
- Encounters: Wild Tentacool (Surf).
- Swimmer spotted around (6, 25).
- Swimmer at (12, 30) facing Left.
- Swimmer at (10, 31) facing Up.
- Swimmer spotted at (5, 71).
- Route 21 ends around Y=89 at a wooden dock. Cinnabar Island is directly South.
- Read sign at (13, 3): "CINNABAR GYM'S HOT-HEADED LEO!"
- Read sign at (12, 3): "CINNABAR ISLAND, The Fiery Town of Burning Desire"
- Read sign at (9, 5): "CINNABAR ISLAND POKEMON LAB"

<hr>

<h1><code>Locations/CinnabarIsland</code></h1>

# Cinnabar Island

[Navigation]
- Arrived from Route 21 (North).

[Points of Interest]
- Sign at (9, 5): "CINNABAR ISLAND, The Fiery Town of Burning Desire"
- Building at (6, 9) is the Pokemon Lab.
- Building at (11, 11) is the Pokemon Center.
- Building at (15, 11) is the Poke Mart.
- Inside Pokemon Lab (3rd room / rightmost): The scientist who revives fossils paces around X=4 to X=6 at Y=2. Revived Helix Fossil into Omanyte (HELIX).
- Building at (6, 3) is the Pokemon Mansion.
- Building at (18, 3) is the Cinnabar Gym. It is currently locked, and requires the Secret Key.
- The path to the Mansion entrance at (6, 3) from the East side of the island is via a 1-tile wide gap at Y=4 (X=9, 4).
[Island Layout Revelation]
- The Lab (X=4 to X=9), Pokemon Center (X=10 to X=13), and Poke Mart (X=14 to X=17) form a massive, continuous solid barrier across the island from Y=7 to Y=11.
- You CANNOT walk North on the West side of the Lab because X=3 is Water.
- You CANNOT walk North between the buildings.
- The ONLY path North to the Gym and Mansion from the southern area (where you exit the Lab or Center) is via the far East corridor at X=18!
- Route: Walk East to X=18, walk North to Y=4, then walk West to reach the Mansion.
- WARNING: Stepping onto the tile at (18, 4) automatically triggers a text box ("The door is locked...") from the Cinnabar Gym door without needing to press A. This will interrupt movement macros.
- [Turn 48839] Successfully unlocked and entered Cinnabar Gym (Map 0_166) using the Secret Key! The door opens automatically when you walk into it (18, 3) from the outside, just like electronic doors with the Card Key.

<hr>

<h1><code>Locations/PokemonMansion</code></h1>

# Pokemon Mansion

[Navigation]
- Located at (6, 3) on Cinnabar Island.
- 1F Exit is at (5, 27).
- 1F Map ID is 0_165. 2F Map ID is 0_214. 3F Map ID: 0_215. B1F Map ID: 0_216.

[Encounters]
- Vulpix
- Ponyta
- Grimer
- Muk
- Koffing
- Magmar

[1F Points of Interest]
- 1F Central Hallway runs North from the entrance along X=5.
- Green pillars line X=3 and X=8, with 1-tile gaps.
- A solid horizontal wall at Y=9 blocks the Central Hallway and West Wing.
- East wing is separated by a vertical wall at X=13 (from Y=7 South). Another solid wall at X=9 runs from Y=3 to Y=7. To cross between the Central and East wings, you MUST use the Northern hallway at Y=2.
- The horizontal wall at Y=9 does NOT extend all the way to the East Wing wall. There is a gap at X=12! You can walk South down X=12 to bypass the Y=9 wall, then head West along Y=11 (passing through a gap in the green pillars at 8, 11) to reach the main stairs at (5, 10).
- The main staircase on 1F is only 1 tile wide at (5, 10). It leads to 2F (5, 10). On 2F, there is a wider 3-tile staircase at Y=10. The left tile (5, 10) goes down to 1F. The middle/right tiles (6, 10) and (7, 10) go UP to the isolated 3F room!
- CRITICAL: The stairs at 1F (7, 10) ONLY lead to the isolated 3F room with the Burglar and Diary. This room is a VERIFIED DEAD END (no pit!). You must use the stairs at 2F (6, 1) to reach the main 3F area and the pit.
- The 1F statue at (2, 10)/(2, 11) is JUST A NORMAL STATUE. However, there IS a switch on a statue at 1F (2, 5)!
- 2F Central South doors at (7, 22)/(7, 23) are OPEN IN STATE B! Grants access to the SW room containing beds and a diary at (3, 21). THERE ARE NO STAIRS HERE. My previous notes were a massive hallucination.
- Closed electronic doors located at (16, 7)/(17, 7) blocking the path South. To bypass them, use the far-East hallway at X=23!
- The glowing-eye statue at (15, 10)/(15, 11) is a red herring; it does not have a hidden switch.
- The Northeast area (accessed via X=18) contains a diary at (18, 2) and CONNECTS to the East Wing via a gap at Y=3. Walk East to X=26 or X=27 to bypass the tables at Y=4, then South to explore the East Wing.
- South-East corridor (X=18 to X=21, Y=12 to Y=15) is a dead end. The East Wing corridor (accessed via the doors at 24, 13) continues South of Y=18.
- 1F South-East doors are located at (26, 27) and (27, 27). These are closed in State A.
- Found a regular statue at (27, 18) in the East Wing. It is NOT a switch. There is NO way to toggle states from within the 1F East Wing.
- SW corridor (X=1/X=2) runs from Y=27 North to Y=10. It is a dead end containing a Burglar at (1, 14), and connects to the Central Hallway via a gap at (3, 11).

[2F Points of Interest]
- Arrived from 1F via stairs at (5, 10).
- You CAN walk North-East from the stairs area to the Northern hallway. The path from (10, 13) is North to (10, 9), East to (12, 9), North to (12, 6), then East to (16, 6).
- VERIFIED: The Northern hallway is clear. There is NO solid wall at Y=9 blocking X=10 to X=12. The electronic doors are further East at (18, 8)/(19, 8).
- The path from 2F Central to 2F East is via the Northern hallway: Walk North from (10, 13) to (10, 9), East to (12, 9), North to (12, 6), then East to (16, 6).
- This path requires the Mansion to be in STATE B (Northern doors open)!
- VERIFIED: The tiles at (7, 12) to (7, 15) are solid walls (TYPE_2889). The crossing between West and Central is specifically at Y=11.
- A path leads West to the Northwest corner at Y=4/Y=5. The statue here is just a regular statue, NOT a switch.
- Found stairs at (6, 1). VERIFIED: They CAN be ascended if approached directly from the bottom at (6, 2). They lead to 3F (6, 1).
- Found stairs at (16, 14)/(17, 14) on 3F (the pit). There are NO stairs at (16, 7) on 2F; it is an open corridor heading South.
- The tiles at (4, 1) and (5, 1) are clear floor, allowing access from the far West side to the Northern Hallway at Y=2.
- The wall at X=9 on 2F consists of green pillars, separating the West and Central areas.
- In the East wing of 2F, there is a solid vertical wall at X=11 extending from at least Y=17 to Y=25.
- In the Northeast area, the brown blocks at (24, 8)/(25, 8) are just a table/solid obstacle, NOT stairs!
- The 2F East Wing North (accessed via the 1-tile gap at 22, 3) is a dead end! It contains Calcium at (28, 5). The path South is completely blocked by a solid line of tables at Y=8 (from X=21 to X=28).
- The stairs at 2F (25, 14) remain a mystery, inaccessible from known 1F/2F paths (see Verified Dead Ends).

[3F Points of Interest]
- Burglar trainer spotted at (4, 11).
- Diary located at (6, 12). "Feb. 6. MEW gave birth. We named the newborn MEWTWO."
- Found Max Potion at (1, 16).
- Wide open gap/drop-off visible on the right side at X=12.
- Spotted an item ball at (9, 4).
- Spotted a glowing-eye switch statue at (10, 4)/(10, 5).
- The southern half of 3F is ACCESSIBLE from the switch via a gap at X=13/X=14! Walk East from the switch to (13, 5), then South to bypass the wall at Y=8.
- There are electronic doors at Y=5 (X=15 to X=17). (Northern doors)
- The path North at X=18 is blocked by a solid barrier at Y=9.
- On 3F, eastern section (past the doors at X=15): Path continues south of a wall at X=22. Found an item ball at (25, 5).
- 3F Pit: The top edge of the pit at (12, 13) to (15, 13) is a solid wall. You must jump down from the right side at (16, 14) or (17, 14).
- Southern doors at (15, 10)/(15, 11) block access to the pit in State A.
- Found stairs down to B1F at (21, 23). Currently blocked by a vertical wall at X=16.
- VERIFIED DEAD END: The ENTIRE 3F West Wing and South-West area is a dead end. The Central South area (X=11 to X=14) is blocked from going further West by a solid wall at X=11. The path South to the pit at Y=14 is blocked by rubble at Y=13. There is no Second Pit in the West/South-West.

[B1F Points of Interest]
- Arrived from 1F via stairs at (23, 22). These stairs lead back up to the enclosed area on 1F (accessed via 3F pit).
- The Northwest section of B1F (containing the switch at 7, 15) is completely isolated by solid walls at X=9 and Y=8, and a table at Y=17. All hypotheses regarding 3F pits, 3F hidden stairs, 2F hidden stairs, and 1F NW stairs have been proven FALSE via exhaustive exploration. The only remaining unexplored vertical transition is the main 3F pit drop on the right side (X=16/17), which drops to the 1F enclosed area. I must re-evaluate how manipulating door states from B1F (via the switch at 18, 25) might change the layout of B1F itself to allow access to the NW section.
- Found TM14 (Blizzard) at (19, 25).
- Diary located at (16, 20): "Sept. 1. MEWTWO is far too powerful..."
- Found a glowing-eye switch statue at (18, 24)/(18, 25).
- Horizontal electronic doors are located at (16, 16) and (17, 16). These are OPEN in State B and CLOSED in State A. The tiles at (14, 16)/(15, 16) and (18, 16)/(19, 16) are solid brown walls, NOT doors.
- There are VERTICAL electronic doors at X=13 (Y=22 and Y=23). I empirically verified these are CLOSED in State B. I need to test if they open in State A.
- Found another switch statue at (7, 14)/(7, 15) in the western area.
- The path West from the enclosed 1F stairs area is at Y=14. X=20 is a solid wall from Y=15 downwards.
- The far East corridor (X=26 to X=28) is accessed from the X=24 corridor by crossing at Y=18, where the separating wall at X=25 ends.
- Horizontal electronic doors at (26, 17) and (27, 17) block access to the far East room of B1F. These are OPEN in State A and CLOSED in State B.
- The NW area (North of Y=17, West of X=9) might be accessible through the electronic doors at X=9! In State B, the red barriers disappear. I must systematically test walking West through EVERY Y-coordinate in the X=9 corridor (Y=4 to Y=8) to find the passable door tile, avoiding the solid doorframes.

[Global Door States]
- State A: 
  - 1F East doors (24, 13) OPEN.
  - 2F East doors (24, 13) OPEN.
  - 2F Northern doors (18, 8)/(19, 8) CLOSED.
  - 2F South-East doors (26, 27) CLOSED.
  - 3F Northern doors (15, 4) OPEN.
  - 3F Southern doors (15, 10) CLOSED.
  - B1F Central doors (20, 17) CLOSED.
- State B: 
  - 1F East doors (24, 13) CLOSED.
  - 2F East doors (24, 13) CLOSED.
  - 2F Northern doors (18, 8)/(19, 8) OPEN.
  - 2F South-East doors (26, 27) OPEN. (Hypothesis: Alternates with State A)
  - 3F Northern doors (15, 4) CLOSED.
  - 3F Southern doors (15, 10) OPEN.
  - B1F Central doors (20, 17) OPEN.
  - 1F Central doors (16, 7)/(17, 7) OPEN.
- 2F Central doors located at (20, 17) and (21, 17). In State A, these are CLOSED. They block the path South to Y=18.
- Rubble at Y=8 blocks X=8 to X=11 on 2F West. Path South is at X=7 or X=6.
- Rubble at Y=16 blocks X=5 to X=7. The path South is only open from X=1 to X=4.
- Solid wall at Y=18 blocks X=1 to X=7. The West Wing North of Y=18 is a VERIFIED DEAD END!
- To open the 1F East doors at (24, 13), the Mansion MUST be in STATE A.
- There is NO switch on 2F! My previous notes about a 2F switch were hallucinations. The doors must be toggled from 3F (10, 4) or B1F.
- 2F West Wing: The path North from the main stairs at (5, 10) is BLOCKED by a solid wall at Y=9. You MUST cross to the Central area via the gap at (8, 11), go North via X=10 to Y=4/Y=5, then cross BACK to the West Wing via the gap in the green pillars at (9, 4)/(9, 5) to reach the stairs at (6, 1).
- 2F North-West GAP is at (9, 4)/(9, 5). There are NO electronic doors here! It is always open regardless of state. My previous trap warning was a hallucination. You can freely walk between the 2F Central area and the 2F NW stairs at (6, 1).
- The 2F West Wing and East Wing can also be connected by crossing the X=9 pillar gap at Y=11.
- VERIFIED: The Northern hallway at Y=2 is OPEN across X=9. You can cross between the East/Central Wing and West Wing here.
[Verified Dead Ends]
- The B1F South-West area (South of Y=22, West of X=13) is a complete dead end loop. It connects the gap at (10, 17) to the electronic doors at (13, 22) and contains no items or switches.
- The B1F West Room (X=1 to 7, Y=14 to 27) is entirely blocked off from the switch area at (7, 15) by solid tables. The long SW corridor (X=1 to 3) is a dead end. The Secret Key is NOT accessed via the 3F pit at (16, 14).
- The 2F Central doors at (20, 17) lead to a dead-end 4x3 room.
- The stairs at 1F (6, 10)/(7, 10) lead to an isolated 3F room containing only a Burglar and a Diary. It is a dead end. The room is walled off on the East side by a solid wall at X=11 (Y=8 to Y=15), preventing access to the 3F pit.
- VERIFIED: The X=12 gap on 1F is OPEN at Y=7. You can bypass the Y=9 wall by walking South down X=12, then West.
- The 2F area South of the Northern doors at (18, 8) is a CONFIRMED DEAD END. It ends at Y=15, blocked by walls and rubble at X=22.
- 1F East Wing South is a completely empty dead end down to Y=27. There are NO stairs to 2F here.
- 1F Central Doors at (16, 7) lead to a dead-end hallway from Y=8 to Y=13. It is blocked at Y=13 by a solid wall. It DOES NOT connect to the 3F pit landing area (which is at 16, 14).
- 3F East side (X=16, 17) is blocked from going South by a solid horizontal wall of rubble at Y=9. The pit is South of Y=11. So you CANNOT reach the pit from the East side via the doors at (15, 4). This path is a dead end.
- 3F West Wing (West of X=9) is ACCESSIBLE. I previously hallucinated it was blocked. I must thoroughly search this area (especially South of Y=10).
- Diary located at 1F (18, 2): "Diary: July 5. Guyana, South America. A new POKEMON was discovered deep in the jungle."
- Burglar trainer at (16, 22), facing Right. His line of sight covers Y=22.
- B1F NE Area: The switch statue is at (20, 3) and must be interacted with from (20, 4). There is a long horizontal table at Y=5 blocking access from Y=6. You must go around the table on the East side (around X=25/X=26) to reach the Y=4 hallway.
- Enclosed 1F Area Navigation: To reach the B1F stairs at (21, 23) after dropping from the 3F pit, walk West to X=13, then South. The path East is blocked by walls and bushes at X=14/X=18.
[TRUE SECRET KEY ROUTE]
1. Arrive at B1F (23, 22) in State B. Central Doors (16, 16) are OPEN.
2. Walk West to (16, 14), then South through OPEN Central doors to Central Switch at (18, 25).
3. Toggle Central Switch to State A.
4. Central Doors CLOSE. Far East doors (26, 17) OPEN. Vertical doors at (13, 22) OPEN.
5. Walk West through the OPEN vertical doors at (13, 22) into the SW Loop.
6. Follow the SW Loop to emerge at the gap at (10, 17). We are now North of the closed Central Doors!
7. Walk North to Y=14, then East to X=24.
8. Walk South to Y=18, then East to X=26 (Far East corridor).
9. Walk North through the OPEN Far East doors at (26, 17) into the NE Area!
10. Walk to the NE Switch at (20, 3) and toggle it to State B.
11. The X=9 doors are now OPEN. Pass through them to reach the Secret Key!
- [Turn 48778] VERIFIED: In State B, the vertical doors at X=9 are OPEN at Y=6 and Y=7! The red barriers disappear, allowing access to the NW area!
- [Turn 48784] FOUND THE SECRET KEY! It was the item ball at B1F (5, 13) in the newly opened NW area.

<hr>

<h1><code>Locations/CinnabarGym</code></h1>

# Cinnabar Gym
[Navigation]
- Map ID: 0_166
- Entrance at (16, 17)

[Layout]
- Gym Guide at (16, 13) facing Down.
- Quiz Machine at (17, 13).
- Burglar trainer at (17, 8) facing Right.
- Electronic doors blocking path North at (18, 6) and (19, 6).
- Quiz Machine for this room is likely at (15, 7).
- Defeating a room's trainer automatically opens the adjacent electronic doors. (Verified at 18, 6 after defeating Burglar).
- Super Nerd trainer at (17, 2) facing Down.
- Electronic doors blocking path West at (15, 2) and (16, 2).
- Defeating the Super Nerd at (17, 2) opened the doors, allowing access to the western path via (15, 1) and (15, 3).
- Gap at (14, 1) allows crossing the wall at X=14.
- Super Nerd/Burglar trainer at (11, 4) facing Right.
- Super Nerd/Burglar trainer at (11, 8) facing Up.
- Defeating the Super Nerd at (11, 4) did NOT open doors at (10, 6)/(11, 6) as they are solid walls.
- The path West is blocked by a solid wall at X=8. Must explore South.
- Defeated trainer at (11, 8). Quiz Machine 3 is at (9, 7). Exploring South.
- Fourth section accessed via doors at (12, 12)/(13, 12).
- Defeated Super Nerd trainer at (11, 14) facing Down. (Can talk from behind).
- Electronic doors blocking the path North are located at (4, 12) and (5, 12).
- Defeated Trainer at (3, 14) facing Down. (Can talk from side).
- Quiz Machine 5 is at (1, 12)/(1, 13).
- Quiz Machine 4 is at (9, 12)/(9, 13).
- Solid wall at X=14 blocks line of sight to the Super Nerd at (16, 13).
- Fifth section accessed via doors at (4, 12)/(5, 12).
- Defeated Super Nerd trainer at (3, 8) facing Down.
- Quiz Machine 6 is at (1, 6)/(1, 7).
- Electronic doors blocking the path North are at (4, 6) and (5, 6).
- Defeated Gym Leader Blaine at (3, 3).
- Obtained Volcano Badge and TM38 (Fire Blast).
- All trainers and Gym Leader defeated!

<hr>

<h1><code>Locations/ViridianCity</code></h1>

# Viridian City
- Poke Mart is at (29, 19).
- Pokemon Center is at (23, 25).
- Gym is in the Northeast corner. Accessible by walking North past the old man at (17, 9), then heading East.
- Path North from the East side of the city is blocked by buildings/ledges. Must walk West along Y=16 to reach the main North-South road on the West side of the city (around X=20).
- [Turn 49043] At Viridian Gym. The NPC at (30, 8) said "VIRIDIAN GYM'S LEADER returned!". He is currently blocking the path to the door at (32, 7). Talking to him again to see if he moves.
- [Turn 49057] The NPC at (30, 8) permanently blocks the western path to the Gym door. The correct route is to walk East past the Gym on the North side to X=34, walk South past the fence to Y=8, and then walk West to the Gym door at (32, 7).

<hr>

<h1><code>Locations/ViridianGym</code></h1>

# Viridian Gym
[Navigation]
- Map ID: 0_45
- Entrance: (16, 17)

[Layout & Mechanics]
- Gym Guide at (16, 14) says trainers here use Ground-type Pokemon.
- Spin tiles (spinners) are present in this gym. Spotted at X=13, Y=16/17 (TYPE_55d0).
- Statues block direct North path at X=15 and X=18.
[Spinner Paths]
- (19, 11) [Up] -> shoots North, stops at yellow tile (19, 2).
- (19, 2) is a yellow stop tile in an enclosed corridor (X=18 to 19, Y=2 to 6).
- (19, 1) is a Left-pointing spinner.
- From (19, 2) stop tile, stepping Up hits (19, 1) [Left spinner].
- From (19, 2) stop tile, stepping Left hits (18, 2) [Down spinner].
- (19, 2) stop tile -> [Up] -> hits (19, 1) Left spinner. Pushes Left all the way to (11, 1) Down spinner.
- Black Belt `SPRITE_427f` at (11, 10) facing Up (Defeated).
- Cooltrainer `SPRITE_e4ed` at (12, 8) facing Down (Defeated).
- Tamer `SPRITE_9238` at (10, 7) facing Down.
- Cooltrainer `SPRITE_e4ed` at (13, 5) facing Down.
- [Turn 49071 Reflection] Stopped on Down spinner at (11, 1). Likely because the Black Belt at (10, 1) (facing Right) spotted me and interrupted the spin.
- [Turn 49088] Defeated Blackbelt at (10, 1). The tile at (11, 1) is a Down spinner, and (11, 2) is a yellow stop tile. Stepping Down to continue.
- (11, 2) is a Right spinner (`TYPE_64a2`).
- Stepping Down from (11, 1) onto (11, 2) should push me Right along Y=2.
- (11, 2) Right spinner pushes all the way to (17, 2) yellow stop tile.
- No trainer at (17, 1). The stop at (17, 2) was just a stop tile.
- From (12, 1), the path Left hits the Down spinner at (11, 1), which loops back to the Right spinner at (11, 2) and pushes back to (17, 2).
- The correct path seems to be taking the Down spinner at (18, 2).
- Walking back to (17, 2) and stepping Right onto (18, 2).
- (18, 2) is a Down spinner (`TYPE_55cd`). Stepping onto it now.
- (18, 2) Down spinner pushes all the way South to the (18, 11) yellow stop tile.
- From (18, 11), the path South goes to Y=12, then West to another stop tile at (16, 12).
- Item Ball at (16, 9) contained a Revive.
- (16, 10) is a Down spinner, blocking the path North to the Cooltrainer at (16, 9).
- The path from (16, 12) continues West to (14, 12), North to (14, 9), then West to (12, 9) towards the Cooltrainer at (12, 7).
- CRITICAL VISUAL CUE: The black blocks with blue/white checkerboard bases are solid walls (`TYPE_2889`). They are NOT "Left Spinners". The Gym is a maze of these solid walls.
- X=8 is a DEAD END at Y=5. The wall at (8, 4) blocks it.
- To reach the Northern corridor (Y=5), navigate from (11, 7) East to (15, 7), then North to (15, 5).
- Cooltrainer `SPRITE_e4ed` at (14, 5) facing Right (Defeated).
- Solid wall at X=7 (Y=5 to Y=6). The path West from (10, 2) goes along Y=2, then South down X=7 to Y=4, then West to (6, 4).
- Cooltrainer `SPRITE_e4ed` is at (6, 5) facing Down. Can be approached from behind at (6, 4).

<hr>

<h1><code>Bosses/Giovanni_Gym</code></h1>

# Giovanni (Viridian Gym)
- Rhyhorn Lv 45
- Dugtrio Lv 42
- Nidoqueen Lv 44
- Nidoking Lv ??? (Next)
- Nidoking Lv 45
- Rhydon Lv 50
- DEFEATED! Earned Earth Badge and TM27 (Fissure).

<hr>

<h1><code>Locations/Route22</code></h1>

# Route 22
- Connects Viridian City (East) to the Pokemon League Front Gate (West).
- The path West is a maze. The lower path at Y=14 is blocked by a wall at X=26. The upper path is blocked by a wall at X=29. You must climb back up from the lower path via the gap at X=31, and navigate North through the tall grass!
- [Turn 49545 PROOF] The upper path is a 100% VERIFIED DEAD END. I physically bumped into the building at X=16, X=17, X=18. It is solid.
- To reach the Reception Gate, you MUST jump down the ledge at Y=7 near X=17 to access the lower path, travel West to Y=12.
- I must now physically test the 'white doors' at X=7/X=8, and if they fail, I must physically explore the far West area (X=1 to X=5) to find the true path North.
- [Turn 49554 Reflection] I bumped into the 'door' at (7, 11) and it is solid. More importantly, my claim from Turn 49526 that 'X=1 is a solid wall' was made from X=5. This is a classic visual hallucination. I must ride all the way West past X=5 to physically test the boundary!
- [Turn 49659 Discovery] TRIPLE HALLUCINATION CORRECTED: The water is actually located at X=22, Y=6 on the UPPER PATH! I can clearly see it on my screen. If the lower path Y=9 scan fails, I MUST return to X=22 and use Surf.
- [Turn 49558 CRITICAL REALIZATION] FAILED. The statues at X=14/15 extend all the way to the ledge at Y=7. The tiles at (14, 6) and (15, 6) are TYPE_2889 (solid). There is no gap. The upper path is 100% a dead end. I must jump the ledge to the lower path and navigate South around the grey blocks to reach the water at X=3.
[Turn 49592 Hallucination Correction]
- I completely hallucinated entering the Pokemon League Reception Gate at (18, 4). Map ID 0_33 is Route 22. I bumped into a solid wall at (18, 4) and then wandered East back to the start of the route, thinking I was inside a building!
- The true path forward is to the WEST, which requires Surf. I must return to the western section of Route 22 and find the water crossing at X=14.
[Turn 49607 Route 22 Reset]
- I have confirmed the very bottom path (Y=14, Y=15) is a one-way drop returning East.
- Since the lower path (Y=12) ended in a dead end at X=1 and forced me to jump down to Y=13, the TRUE path to the Reception Gate MUST be somewhere I missed on the upper or middle routes.
- I will return to the Viridian City entrance and systematically remap the route, ignoring my previous assumptions.
[Turn 49628 Hypothesis Update]
- The upper path is 100% blocked by a solid building and statues at X=14/X=15 from Y=1 down to Y=8. There is NO path North of the statues.
- The lower path at Y=12 bypasses these statues.
- I previously thought the lower path was a dead end because of a ledge at Y=9. However, I likely missed a gap in that ledge while mashing Left!
- I will jump down to the lower path, walk West, and meticulously scan the North side (Y=9) for a gap to reach the Reception Gate at (8, 5).
[Turn 49681 Lower Path Puzzle Solved]
- The lower path is NOT a dead end! I missed a crucial hidden gap.
- The building/statues at Y=11 block the path North, but there is a gap at (5, 11).
- Walking North through (5, 11) to (5, 10), then East along Y=10, leads behind the facade.
- At (11, 10), there is a GAP in the South-facing ledge at (11, 9)!
- This allows me to climb up to Y=8 and bypass the entire blockade.
[Turn 49643 Reflection]
- Error Analysis: My biggest failure in the last 50 turns was severe spatial hallucination. I assumed tiles were water/walls without physically bumping them, and I misremembered the location of the Reception Gate.
- Correction: I am now strictly adhering to the "Exhaustive Exploration" rule from my Main notepad. I will physically test the northern boundary of the Upper Path (Y=1 to Y=3) to conclusively prove or disprove my hypothesis.
[Turn 49658 Upper Path Dead End Confirmed]
- Bumping Left at (16, 4) and (16, 5) confirms X=15 is a solid wall of statues/columns from Y=4 down to Y=9.
- The Upper Path is a 100% verified dead end at X=16. It is physically impossible to go further West on the Upper Path.
- The ONLY way forward is the Lower Path. I must jump down the ledge at Y=7 and meticulously scan the North boundary (Y=9) of the lower path for a gap or stairs going Up to the Reception Gate.
[Turn 49674 Route 22 Water]
- I successfully reached the water at (22, 6) on the Upper Path.
- The path West on the Upper Path was indeed blocked at X=16, but the water extends South from X=22.
- I will Surf South to continue towards the Reception Gate.
[Turn 49678 Pond Realization]
- The water at X=22 is just a 4x4 decorative pond. It does NOT block the path West.
- I walked West to (17, 10) and discovered the statues at X=14/X=15 actually extend all the way down to Y=11!
- The ONLY way to bypass them is to walk West along the very bottom path at Y=12.
- I will walk West on Y=12, then immediately scan the North boundary (Y=11, Y=10, Y=9) for any gaps that lead up to the Reception Gate.
[Turn 49682 True Path Documented]
- The puzzle of Route 22 is finally solved!
- TRUE PATH TO RECEPTION GATE:
  1. Jump down the ledge near X=17 to the Lower Path (Y=12).
  2. Walk West along Y=12 to X=5.
  3. Walk North through the hidden gap at (5, 11) into the "facade" area behind the statues.
  4. Walk East along Y=10 to (11, 10).
  5. Walk North through the hidden gap in the ledge at (11, 9).
  6. Walk West to X=8, then North to enter the Reception Gate at (8, 5)!
[Turn 49689 Reception Gate]
- Arrived at Reception Gate (Map 0_193).
- Walking North to Y=2 automatically triggers the Boulderbadge check. The guard says "Go right ahead!"
- I will continue North through the door.
[Turn 49690 Reception Gate Progress]
- Passed the Boulderbadge check at (4, 2)! The guard stepped aside.
- Moving North to the next map/section.
- Navigation Note: The path West through Route 22 is located on the upper section around Y=5. The lower section at Y=12 is blocked by rock walls at X=29.
- The upper path at Y=5 dead-ends at X=15 due to trees. Jumping down the ledge at (16, 7) to use the lower path to bypass them.

<hr>

<h1><code>Locations/Route23</code></h1>

# Route 23
- Map ID: 0_34
- This route consists of sequential Badge Checks to reach Victory Road.
- Badge Check 1: Boulderbadge (Passed in Reception Gate 0_193)
- Badge Check 2: Cascadebadge at (7, 135).
- The water at Y=129 is blocked by a ledge at Y=131. Do NOT Surf here.
- Instead, take the dirt paths North at X=4 or X=9 to bypass the water.
- Badge Check 3: Thunderbadge at (9, 119). Passed.
- The water at Y=115 is bypassed by walking East to X=10 and then North.
- Badge Check 4: Rainbowbadge at (10, 105). Passed.
- At (11, 104), used Surf to cross the water North.
- Badge Check 5: Soulbadge at (11, 96). Passed.
- Badge Check 6: Marshbadge at Y=85. Guard at (8, 85).
- The water is blocked by a ledge at Y=83. Surf West to X=7 to bypass it and continue North.
- The water path ends at Y=72. Make landfall at X=8, Y=71.
- Continuing North from Y=68 through the grass to find the 7th Badge Check.
- At Y=65, the path North is blocked by rocks at X=8 and X=9. Move East to X=10 to bypass.
- Badge Check 7: Volcano Badge at (10, 56). Passed.
- At Y=56, the path North is along X=12. Move East to X=12 to bypass the rocks at X=10/X=11.
- At Y=44, the path North is blocked by a South-facing ledge at Y=43. This is NOT water. The path continues North on the West side at X=7. Backtrack South to Y=48, then West to X=7 to bypass the rocks.
- Badge Check 8: Earth Badge at (4, 35). Passed.

<hr>

<h1><code>Locations/VictoryRoad_1F</code></h1>

# Victory Road 1F
- Map ID: 0_108
- Entrance from Route 23 is at (8, 17).
- Puzzle 1: Boulder started at (5, 15). Switch is at (17, 13).
- TRUE SOLUTION FOUND:
  1. Use Strength.
  2. Walk to (5, 14) and push boulder DOWN to (5, 16).
  3. Walk to (4, 16) and push boulder RIGHT to (9, 16).
  4. Walk to (9, 17) and push boulder UP to (9, 14).
  5. Walk to (8, 14) via (8, 15). Push boulder RIGHT to (16, 14).
  6. Walk to (16, 15) via (15, 15). Push boulder UP to (16, 12).
  7. Walk to (15, 12) via (14, 14) -> (14, 12). Push boulder RIGHT to (17, 12).
  8. Walk to (17, 11) via (16, 11). Push boulder DOWN to switch at (17, 13).
- Current Status: PUZZLE SOLVED! (Turn 52850). The wall blocking 1F (1, 1) should be open. I am currently at (8, 14). Navigating to stairs at (5, 13) to access the Raised Platform, then to (7, 7) to drop to the Central Lower Level, then to (1, 1).
- Goal: Walk WEST along the Raised Platform to the stairs at (7, 7), drop DOWN to the Lower Level at (7, 8), and find the path to the NW stairs at (1,1).
- TOPOGRAPHY DISCOVERY (Turn 52082): The East Lower Level (accessed via 15,7) is a dead end, blocked West by a rock wall at X=14. The East Raised Platform connects (15,7) to (7,7). We MUST drop down at (7,7) to access the Central Lower Level.
- TRUE PATH TO 2F: The Central Lower Level MUST connect (7,8) to (1,1) because I walked this path earlier! My note claiming it was blocked was a hallucination.
- STAIRS CONNECTION: The stairs at 1F (1, 1) connect to 2F (27, 7). They are located on the LOWER LEVEL in the NW corner. The switch puzzle at (17,13) likely removed a wall blocking these stairs.
- **Central Boulder Puzzle**:
  - The boulder's original position is (2, 10). It blocks the 1-tile chokepoint on X=2.
  - TOPOGRAPHY TRAP: If you approach this boulder from the North (via the stairs at 1,1), you CANNOT get above it to push it Down! The path is blocked by a rock at (2,8) and an invisible wall/obstacle at (3,9).
  - Therefore, the NW Lower Level (where the 1,1 stairs are) is an ISOLATED POCKET. You MUST push this boulder UP from the South side to open the path to the 2F stairs.
- [Turn 52883 1F Topography] The boulder at (2, 10) is a DECOY. It blocks the path and cannot be bypassed from the South. We must find another way to access the Northern Lower Level.
- [Turn 52910 Breakthrough] Successfully accessed the NW Lower Level (and the 1,1 stairs) by bypassing the (2,10) decoy boulder! The correct path is: Stairs at (5, 13) UP to Raised Platform -> Walk North/East -> Drop DOWN 1-way ledge at (7, 7) to Lower Level at (7, 8) -> Walk West to (3, 8) -> Walk North to the stairs.

<hr>

<h1><code>Locations/VictoryRoad_2F</code></h1>

# Victory Road 2F
- Map ID: 0_194
- Elevation Facts (CRITICAL):
  - LOWER LEVEL is TYPE_3fe2. Contains Boulder at (5, 5), Item Ball at (9, 11), Item Ball at (18, 9), Moltres at (11, 5).
  - RAISED PLATFORM is TYPE_2770. Contains Blackbelt at (12, 9), Juggler at (21, 13), Target Hole at (23, 14), Stairs to 3F at (25, 14).
- Entrance from 1F is at (0, 8) on LOWER level.
- Puzzle 1 (Lower Level): Switch at (1, 16).
- Puzzle 1 Solution (Switch at 1,16):
  - The boulder at (5,5) is a DECOY.
  - TRUE SOLUTION: The correct boulder is found at (4, 14). Push West to (3, 14), push Down to (3, 16), push West to (1, 16).
  - TOPOGRAPHY TRAP: Do NOT push the boulder West to (2, 14)! Tile (2, 15) is a rock, preventing you from pushing it down the X=2 column.
  - REWARD: Solves the X=8 rock wall barrier on the RAISED PLATFORM, connecting the West and East halves.
- To reach 3F, we must find another staircase on the Raised Platform. (Visually confirmed 17,5 is Lower Level with NO stairs).
- How to reach the Raised Platform:
  1. From 2F entrance at (0, 8), walk North to (0, 7), East to (3, 7), then South to (3, 8). (Direct East from 0,8 is blocked by a rock at 1,8).
  2. Walk South through the gap at (3, 8) to reach the South side of the West Lower Level.
  3. Walk East to (5, 11).
  4. Take the stairs UP at (5, 10) to reach the Raised Platform!
- Topography Facts:
  - Stairs at (5, 10) connect Raised (5, 9) to Lower (5, 11).
  - NO STAIRS at (7, 8). It is a cliff edge.
  - West Lower Level (X < 8) is separated from East Lower Level by a solid rock wall at X=8.
  - East Raised Platform: 
    - The Juggler is at (21, 13). The Hole is at (23, 14). It completely blocks access to the stairs at (25, 14).
    - The path South of (15, 8) goes down X=14 to Y=12, then East to the Juggler. This entire section is a dead end until the hole is filled.
  - West Raised Platform (West of X=8): Connected to East Raised Platform! The switch at (1, 16) removed the rock wall at X=8 on the Raised Platform.
  - CONCLUSION: The switch at (1,16) ONLY opened the Raised Platform path at X=8. The Lower Level rock wall at X=8 (from Y=11 to Y=15) remains CLOSED. This confirms we must travel via the Raised Platform to cross to the East side.
- [Turn 52367] Discovered stairs DOWN at 2F (15, 15) on the Raised Platform! Taking them to reach the East Lower Level.
- [Turn 52397 2F Topography Correction] Massive hallucination! The path West along Y=11 from (28, 11) DOES NOT dead-end at X=24. Tile (24, 11) is open! It connects to X=23, which is a straight corridor North to the stairs at (23, 7)! The East Lower Level path is the correct way to 3F!
- PUZZLE 2 (Lower Level South): A switch exists at (9, 16). The hole at 3F (23,15) is the CORRECT path! The boulder drops to 2F (23,16), which is open on the East, West, and South sides. You can walk around it via Y=17 to push it West to the switch. My previous note about it dropping into a solid wall was a complete hallucination!
- EXIT WARP: The exit to Indigo Plateau is triggered by walking RIGHT from 2F (29, 7). It warps you to 0_34 (14, 32).

<hr>

<h1><code>Locations/VictoryRoad_3F</code></h1>

# Victory Road 3F
- Map ID: 0_198
- Reached via 2F stairs at (23, 7), arriving at 3F (23, 7).
- PUZZLE 1 SOLVED: The Switch at (3,5) permanently removes the solid obstacle at (7,10) on the Raised Platform, granting access to the Far West stairs at (1,9). (Verified Turn 53124)
- [CRITICAL MECHANICS] Boulders on switches DO NOT RESET when leaving the floor or using Dig! The rock walls they open ALSO DO NOT RESET. The switch at (3,5) is permanently solved and (7,10) is OPEN.
- [TRAP TILE WARNING] Tile (4, 3) in the Northern Corridor is an inescapable 1x1 pit trap bounded by a 1-way ledge to the North and solid walls on all other sides. Stepping Down from (4, 2) permanently traps the player. Use Dig or Escape Rope to exit.
- [BOULDER TRAP] Never push a boulder against the top wall (Y=0)! You cannot get above it (Y=-1) to push it Down, permanently sticking it. If this happens, you must leave the floor via stairs to reset.
- Boulder 1 must be pushed along Y=1 or Y=2 so you can walk to Y=0 to push it South when needed.
- FAR WEST LOWER LEVEL: Accessed via stairs at (1,9) from Raised Platform. Contains a Cooltrainer at (6,14). There is NO BOULDER here.
- SOUTH CORRIDOR: A path along Y=15/Y=16 connects the Far West to the East side.
- EAST LOWER LEVEL (SOUTH): Contains Boulder 3 at (22,15) and a Hole at (23,15). The Hole at (23,15) is a trap/exit that drops to 2F (23,16) Lower Level. DO NOT push Boulder 3 into this hole! We must find a path North to Boulder 2 at (24,10).
- THERE IS NO HOLE AT (9, 15). I completely hallucinated it because of the switch at 2F (9, 16). The boulder at (6, 14) must go somewhere else.
- TRUE EXIT PATH OF VICTORY ROAD (VERIFIED):
  1. Solve switch at 3F (3,5) to open wall at (7,10).
  2. Walk West to (1,9) and DROP DOWN the 1-way ledge to the Lower Level.
  3. Walk South to Y=15, then East through the South Corridor to Boulder 3 at (22,15).
  4. Push Boulder 3 into the Hole at (23,15). Jump in after it.
  5. On 2F, push the dropped boulder to the switch at (9,16).
  6. This opens the barrier at 2F (23,14), allowing access to the stairs at 2F (25,14).
  7. Take 2F (25,14) stairs UP to 3F (27,15).
  8. Walk North to the final stairs at 3F (26,8), which lead to the exit!

<hr>

<h1><code>Scratchpad/VictoryRoad_3F</code></h1>

# Victory Road 3F Empirical Map
- Map ID: 0_198
- Stairs down to 2F at (23, 7) (Lower Level).
- Lower Level path West from stairs dead-ends at X=12 (Y=6, Y=7).
- Stairs to Raised Platform at (17, 5).
- RAISED PLATFORM (TYPE_2770): Contains Cooltrainer at (16, 3). Path extends North to Y=2, East to X=18 (wall at X=19), and West to X=9 (wall at X=8). At X=9, path turns South to Y=10, then West to a hole at (7, 10).
- HOLE at (7, 10): Acts as a solid obstacle to the player. Cannot walk into it. Need to drop a boulder in it from somewhere? Wait, (7, 10) might be where a boulder drops *to*, or drops *from*.
- LOWER LEVEL EAST: Visible East of the X=19 wall. The wall at X=19 has a gap at Y=6 and Y=7 connecting to the West. Contains Boulder 1 at (22, 1), Item Ball at (26, 5), Boulder 2 at (24, 10), Boulder 3 at (22, 15), and HOLE at (23, 15). Path South from (20, 11) is blocked. Path East from (23, 5) is blocked by rock wall at X=24..25. NE Corner (Item Ball & Trainer at 28,5) must be accessed by routing North via Y=2.
- TOPOGRAPHY: X=21 is a solid wall from Y=9 to Y=12. Y=9 is a solid wall from X=21 to X=24. This completely blocks access to Boulder 2 (24, 10) and Boulder 3 (22, 15) from the North and West. We MUST find a way to access them from the South!
- LOWER LEVEL CENTRAL: Path from East side at (19, 9) goes South to (19, 10), then West along Y=10 and Y=11, connecting to the North side of the Western Boulder at (13, 12). This confirms there is no path South from here.
- LOWER LEVEL WEST: Path West at Y=11 connects North to Y=7 via X=12. Path South at X=13 is blocked by Boulder at (13, 12). Pushing it DOWN from the North traps it at (13, 13)! It MUST be approached from the South and pushed UP. Southern area likely accessed via Raised Platform stairs at (7, 10).
- Defeated Cooltrainer♂ at (28, 5).
- LOWER LEVEL EAST: Max Revive collected at (26, 5). Second stairs DOWN at (26, 8) (blocked from North by rock wall at Y=6).
- Raised Platform (7, 10): Tile TYPE_de37 is a solid obstacle when approached from the Right. Cannot walk onto it. Abandoning this route. Will re-explore Lower Level East around Boulder 2 (24, 10) to find a path South.
- HYPOTHESIS REJECTED: The Boulder at (13, 12) is in a 1-tile wide hallway. Tiles (12, 12) and (14, 12) are solid rock walls (TYPE_2889). It is physically impossible to push it Left or Right. It MUST be pushed UP from the South.
- NEW PLAN: The Southern area must be accessed via the Raised Platform. I am going back to the stairs at (17, 5) to explore the far West side of the Raised Platform (West of X=9 at Y=2..Y=4).
- LOWER LEVEL NORTH CORRIDOR: Discovered on Turn 51253. There is a 1-tile wide corridor along Y=1 that connects the East side (X>19) to the West. It runs North of the Raised Platform. Exploring it now.
- LOWER LEVEL WEST (NORTH OF RAISED PLATFORM): Reached via the Northern Corridor (Y=1). This area contains a Switch (`TYPE_eb90`) at (3, 5) and an Item Ball at (7, 7). The area is bounded by the Raised Platform to the South at Y=7. The Switch at (3, 5) likely needs a boulder. Boulder 1 at (22, 3) is the only candidate, meaning it must be pushed all the way across the Northern Corridor!
[Boulder 1 Puzzle Routing]
Current: Boulder at (2, 5). Switch at (3, 5). Must reactivate Strength after every wild battle!
Strategy: Reactivate Strength. Walk to (1, 5) and push Right to (3, 5).
- RAISED PLATFORM WEST: Path from (7, 10) continues West and North to (5, 8). At (5, 8), the path goes West to X=1. There appears to be a staircase DOWN at (1, 9).
- LOWER LEVEL FAR WEST: Accessed via stairs at (1, 9) from the Raised Platform. This area goes South along X=1 to Y=15, and opens Eastward. There is a boulder at (6, 14).
- LOWER LEVEL SOUTH CORRIDOR: Discovered Turn 51442. There is a path along Y=15/Y=16 connecting the Far West (X=6) to the East! This allows access to the southern area containing Boulder 3 (22, 15) and the target hole (23, 15).
- [Turn 51444] Reached Boulder 3 at (22, 15) via the South Corridor! The target hole is directly East of it at (23, 15). Preparing to push it in.
- [Turn 51445] Pushed Boulder 3 at (22, 15) into the hole at (23, 15)! It disappeared. (Note: Strength was still active despite wild encounters, meaning my previous hypothesis that *all* wild encounters deactivate it might be wrong. Perhaps running from them preserves it? Regardless, the boulder is in!). Jumping in after it!
- [Turn 51446] REVELATION: The hole at 3F (23, 15) drops to 2F (23, 16), which is on the LOWER LEVEL. The target hole for 2F is at (23, 14) on the RAISED PLATFORM. Furthermore, the boulder is stuck at 2F (23, 16) surrounded by rocks, and I landed at (22, 16). Therefore, the hole at 3F (23, 15) is a TRAP/EXIT! It does not solve the 2F Raised Platform puzzle. Exploring the path West from 2F (22, 16) now.
- [Turn 52458] Boulder 1 successfully pushed onto the switch at (3,5) AGAIN! Puzzle solved. The path at (7, 10) is open.
- [Turn 52525] Topography Correction: The Northern Corridor has a 1-way ledge at Y=2 (facing South). This means you CANNOT walk North from (4,3) to (4,2). Furthermore, (3,3) is a rock wall. The area at (4,3) and (4,4) is a ledge trap! You must loop around via X=2: (4,3) -> (4,4) -> (2,4) -> (2,1) -> (3,1) -> (3,2) -> (4,2).
- [Turn 52527 WARNING: TRAP TILE] Tile (4, 3) is a 1x1 inescapable pit trap! It is bounded by a 1-way ledge to the North (4, 2) and solid walls on all other sides (Left, Right, and Down). Stepping Down from (4, 2) permanently traps the player here! MUST use Dig or Escape Rope to exit the dungeon!
- [Turn 53197] Topography Update: The East pocket (containing the 23,7 stairs) is completely separated from Boulder 2 (24,10) by a solid rock wall at Y=9 (X=21..24). Boulder 2 must be reached from the South! The stairs at 2F (25,14) likely emerge South of Boulder 2.
- NEW PUZZLE HYPOTHESIS: Boulder 3 at (22,15) is a decoy for the trap hole. The true puzzle solution for the 2F (9,16) switch is to use the boulder at 3F (6,14) in the Far West!
- [Turn 53216] EPIPHANY! The hole at 3F (9, 15) perfectly aligns with the switch at 2F (9, 16) due to the map's +1 Y drop offset! The boulder at 3F (6, 14) must be pushed into this hole.
- [Turn 53431] CRITICAL REMINDER: The wall at (7, 10) is CLOSED! Leaving the floor reset the rock wall, even though the boulder is still on the switch at (3, 5). I MUST travel to (3, 5), push the boulder OFF the switch, and push it back ON to re-open the wall.
- Strategy: From (8, 10), walk East to the stairs at (17, 5), drop to the Lower Level, walk North to the Y=1 corridor, and walk West to (3, 5).
- [Turn 53434] Raised Platform navigation: The Raised Platform from X=10 goes North to Y=2, then East to the stairs at (17, 5). I cannot go West from X=10 because of the rock wall at X=8.
- [Turn 53500] Routing Boulder 1: Boulder is at (7,1). The wall at X=5 is solid at Y=0 and Y=1 (`TYPE_2889`). The ONLY gap is at (5,2). Sequence planned: push LEFT to (6,1), walk to (6,0), push DOWN to (6,2), walk to (7,2), push LEFT through the gap to (5,2) and then (4,2).
- [Turn 53503] Pushing Boulder 1 from (2,2) to (2,5), then navigating to (1,5) and pushing it Right to the switch at (3,5).
- [Turn 53669] Navigating South Corridor East. The path at Y=15 is blocked by a rock at (12, 15). The corridor dips down to Y=16 via (11, 16) to continue East.
- [Turn 53761] Route from Boulder 3 Drop to 2F Switch:
  1. From (23, 13), I am blocked from walking North to the (23, 7) stairs by the solid rock wall at Y=9.
  2. I must take the long way around: Walk West through South Corridor -> Stairs at (1, 9) UP to Raised Platform -> Walk East to stairs at (17, 5) DOWN to Lower Level -> Walk North to Y=1 -> Walk East to X=23 -> Walk South to stairs at (23, 7) DOWN to 2F.
  3. Once on 2F, walk South to the dropped boulder and push it West to the switch at 2F (9, 16).
- [Turn 54005] Boulder 1 Puzzle Route (From 22,3 to Northern Corridor):
  1. From (22,4), walk Right to (23,4), Up to (23,3). Push boulder LEFT to (21,3).
  2. Walk Down to (22,4), Left to (21,4). Push boulder UP to (21,2).
  3. Walk Up to (21,3). Push boulder UP to (21,1).
  4. Walk Right to (22,2), Up to (22,1). Push boulder LEFT through the Y=1 gap!
  Executing in small chunks.

<hr>

<h1><code>Scratchpad/VictoryRoad_2F_East</code></h1>

- [Turn 51448 Analysis] The stairs at 2F (21, 15) lead up to the Raised Platform! This gives us access to the Raised Platform on the East side of 2F, very close to the target hole at (23, 14). I am going to explore this Raised Platform area to see if there is another switch or if the dropped boulder at (23, 16) has a purpose.
- [Turn 51453 Analysis] The Raised Platform at 2F East (where I am currently at 20, 12) connects directly West to the main Raised Platform area where the Blackbelt is. The stairs at (21, 15) down to the Lower Level lead to a dead-end pocket at Y=16, which is why the boulder from 3F (23, 15) gets trapped there. The hole at 3F (23, 15) is definitely a trap. I must find a way back to 3F to locate the correct hole at 3F (23, 14). I am navigating West on the 2F Raised Platform to find stairs down to the main 2F Lower Level so I can return to the 3F stairs at (23, 7).
- [Turn 51454 Analysis] The stairs at (15, 15) connect the Raised Platform down to the East Lower Level! Taking these stairs will put me on the Lower Level path that leads straight back East to the 3F stairs at (23, 7).
- [Turn 51458] Successfully navigated East to (19, 16) on the 2F Lower Level. The trap boulder is visible at (23, 16). The Juggler on the Raised Platform is visible at (21, 13). From the current view, it appears the path North to the stairs at (23, 7) might be accessible by walking East to X=24, then North. I will continue East to verify if the boulder at (23, 16) blocks the path.
- [Turn 51467 Navigation] Reached the stairs UP at 2F (15, 15). Taking them to return to the Raised Platform. From there, I will head West back to the main area, then find a path North to the Lower Level so I can return to the 3F stairs at (23, 7).
- [Turn 51816] Exploring 2F Raised Platform further East. Path is blocked by rocks at X=15 (Y=8 to 11), so routing South to Y=12 to continue East.
- [Turn 51818] Realized my route was flawed. The 2F Raised Platform East path is blocked by the hole at (23, 14). There are no stairs to 3F at (17, 5) on 2F; that note referred to 3F! To reach 3F, I must access the stairs at 2F (23, 7) on the North-East Lower Level. To get there, I need to backtrack to the West Lower Level (via stairs at 5,10) and walk North from (0, 8). Backtracking now.

<hr>

<h1><code>Mechanics/PuzzleMechanics</code></h1>

- [Turn 54211] BOULDER RESET RULES:
  1. Boulders resting on the floor or on switches WILL RESET to their original starting positions if you leave the floor (e.g. taking stairs). The rock walls opened by switches will also reset to closed!
  2. Boulders pushed into HOLES DO NOT RESET when leaving the floor. They permanently remain on the lower floor where they landed.
- STAIRS TRIGGER MECHANICS: 1x1 warp stairs (like 1F (1,1) or 2F (0,8)) require standing ON the tile and pressing the direction the stairs lead (Up or Down). Just walking onto the tile does not trigger the warp. Interestingly, the stairs at 2F (23, 7) leading UP to 3F require pressing DOWN to trigger!

<hr>

<h1><code>Locations/IndigoPlateau</code></h1>

# Indigo Plateau (0_34)
- The Pokemon League building is a massive structure to the North.
- There is a maze of statues in front of the building.
- A solid wall of statues runs along X=11 from Y=14 down to Y=20.
- The path crosses from East to West via Y=21.
- [Turn 54299] The West side of the maze (X <= 9) is a DEAD END. X=4 is blocked by statues and raised terrain at Y=16. The correct path must be on the East side, navigating North via the wide open paths at X=12, X=13, or X=14.
- [Turn 54299] Confirmed X=14 dead-ends at Y=10. The true path North through the statue maze is at X=13.
- [Turn 54304] The TRUE entrance to the Indigo Plateau building is located at (9, 0) and (10, 0). It is reached by navigating the maze via X=10.
- [Turn 54331] The entrance at (10, 0) outside on Map 0_34 leads to Map 0_9. Map 0_9 is a connecting hallway that warps to Map 0_174, which is the TRUE Indigo Plateau Lobby containing the PC and Mart.
- [Turn 54472] Mart Clerk FOUND: The Mart clerk is on the far left side of the lobby! The NPC is at (0, 5) behind the counter. Stand at (2, 5) and interact LEFT with the cash register at (1, 5) to open the shop.

<hr>

<h1><code>Quests/OaksAides</code></h1>

# Professor Oak's Aides
- Route 2 Gatehouse 2F: HM05 Flash (Requires 10 Pokemon) - OBTAINED
- Route 11 Gatehouse 2F: Itemfinder (Requires 30 Pokemon) - DEFERRED (Exploring Unknown Dungeon first)
- Route 15 Gatehouse 2F: Exp. All (Requires 50 Pokemon) - PENDING (Currently have 37)

<hr>

<h1><code>Locations/UnknownDungeon_2F</code></h1>

# Unknown Dungeon 2F (Map 0_226)
- Ladder DOWN to 1F at (8, 1). Drops to 1F (9, 1). (Note: Previously believed this was an infinite loop trap due to a hallucinated slide tile. Re-evaluating the 2F layout now).
- Ladder DOWN to 1F at (1, 3). Topologically isolated from the (7,1) ladder region.
- CENTRAL TOPOLOGY: The maze accessed from 1F (18, 9) -> 2F (19, 7) is a massive DEAD END. I have exhaustively mapped every branch. The West branch ends at a pocket around (3, 3) where the only path goes North to (3, 1) and East to the ladder DOWN at (8, 1). This drops you into the INFINITE LOOP TRAP described above. The East branch loops back to the West branch. DO NOT RETURN TO THIS MAZE.
- Ladder DOWN to 1F at (29, 1) arrives from 1F (27, 1) (via East water channel). This entire branch is an isolated DEAD END. It leads South via a zigzag path. The only item is a PP UP at (29, 9), accessed from the South via a loop: from (26, 13), path goes Down to (26, 14), East to (29, 14), North to (29, 12), West to (28, 12), North to (28, 9), then East to the item at (29, 9). The path South of (26, 14) is blocked by rock walls at Y=15.
- Ladder DOWN to 1F at (19, 7) (arrives from 1F 18,9). Dead end to the South at Y=8. Path heads North/West.
- Ladder DOWN to 1F at (3, 11).
- The NW quadrant from (10, 16) is a massive dead-end maze.
- Area East of (11, 5) is a dead end at X=16.
- The path from (19, 7) leads to a maze. The West branch winds through (17, 1) and continues West to (13, 1). From (13, 1) it goes South to (13, 5), forming a loop via (16, 5). The only path forward is West from (13, 5) to (9, 5) and North to (9, 3). The East branch from (19, 7) winds North and East to (24, 2). From (24, 2), the North path via (24, 0) and (21, 0) connects to the West branch at (17, 1). The South path from (24, 2) goes to (24, 4) and East to (27, 4), which is EMPIRICALLY CONFIRMED to be a complete dead end (Turn 56059). The entire East branch is just a loop back to the West branch.
- Ladder DOWN to 1F at (22, 6) (arrives from 1F 23,7). Leads to a completely empty dead-end pocket. The path goes South to (23, 11), where it splits. The East branch goes South to a dead end at (24, 15). The West branch goes to (14, 11), zigzags South to (15, 15), and ends East at (19, 15). The entire pocket is EMPIRICALLY CONFIRMED to be a 100% dead end.
- Ladder UP from 1F (3, 11) arrives at 2F (3, 11).
- Path from 2F (3, 11): North to (3, 9), East to (12, 9). From (12, 9), the East branch goes to (13, 9) -> (13, 8) -> (15, 8) -> (15, 9) -> East to a DEAD END at (21, 9). The South branch from (12, 9) goes down X=12...
- From (12, 9), the South branch goes straight down X=12 to (12, 15), then East to (13, 15), then South to (13, 16)...
- At (13, 17), the path splits. East goes along Y=17 to a DEAD END at (19, 17) (bounded by X=19, Y=16, Y=18). West goes to (11, 17). Exploring West.
- From (11, 17), the path goes Up to (11, 16), Left to (10, 16). At (10, 16), there is a path North and a path West.
- From (10, 16), the North path zigzags NW to a dead end at (4, 15) (bounded by X=3, Y=14, Y=16). The West path from (10, 16) goes to (6, 16), then Down to (6, 17), then West along Y=17...
- From (6, 17), the path continues West to (1, 17), then zigzags North: Up to (1, 15), Right to (2, 15), Up to (2, 13), Left to (1, 13)...
- From (1, 13), the path goes Up to (1, 12), Left to (0, 12), Up along X=0 to (0, 9), Right to (1, 9), Up to (1, 7), East along Y=7 to (6, 7), North to (6, 5), West along Y=5 to (0, 5), North to (0, 3), and East to the ladder DOWN to 1F at (1, 3).

<hr>

<h1><code>Locations/UnknownDungeon_1F_Clean</code></h1>

# Unknown Dungeon 1F (Map 0_228)
- Entrance from Cerulean is at (24, 17).
- Ladders UP to 2F (0_226):
  - (23, 7): Leads to an isolated pocket on 2F.
  - (7, 1): Arrives at 2F (9, 1). Connects to 2F Central Maze.
  - (18, 9): Arrives from 2F (19, 7).
  - (15, 3): Exit-only drop from 2F.
  - (27, 1): Arrives at 2F (29, 1).
- Ladders DOWN to B1F (0_227):
  - (0, 6): Arrives at B1F (3, 6). (ITEM DETOUR: Leads to Max Revive and Ultra Ball. NOT THE PATH TO MEWTWO).
- Topography:
  - The 1F landmass is divided into a Lower Level (Entrance) and an Elevated Level.
  - The Elevated Level is split into East and West halves by a solid rock wall at X=19, 20.
  - East Elevated Platform: Reached from entrance via stairs at (21, 11). Contains ladder at (23, 7).
  - West Elevated Platform: Reached from West Moat via stairs at (11, 13). Contains ladder at (18, 9).
  - SW Lower Path: From stairs at (17, 15), the path goes West along Y=16/17 all the way to X=2, then North and East to the ladder UP at (3, 11).
  - POTENTIAL ROUTE: The ladder at 1F (3, 11) leads to 2F (3, 11), which forces a long linear zigzag path to a ladder DOWN at 2F (1, 3). This drops to 1F (1, 3), which leads directly to the ladder DOWN at 1F (0, 6). The ladder at 1F (0, 6) drops into B1F (3, 6).
- Isolated Pockets:
  - Northern Corridor: Accessed by surfing from the main water to shore at (15, 3). This corridor runs from X=5 to X=16 at Y=0, Y=1, and Y=2. It contains a ladder UP at (7, 1) leading to the 2F Central Maze dead end. The entire corridor is bounded by rock walls to the South (Y=3), East (X=17), and West (X=4). It does NOT connect to the rest of the 1F landmass. (FULLY EXPLORED).
[Water Topography]
- The 1F water is a single continuous moat!
- Starts at shore (25, 9) facing South. Water is at Y=10. Goes East along Y=10 to X=28, then North to Y=5, then West along Y=5 to (15, 5).
- At (15, 5), it connects to the West Water, which goes North to shore (15, 3), and West to X=8.
- From X=8/9, it goes South to Y=14/15, East to X=11, where it meets Central Platform stairs at (11, 13) and a dead-end shore at (7, 13).
- Shores found: (25, 9) [Entrance access], (23, 3) [Ladder 27,1 access], (15, 3) [Ladder 7,1 trap access], (11, 13) [Central Platform access], (19, 3) [1-tile dead end island].
[Central Platform Mapping]
- Accessed via water from the West (stairs at 11,13).
- [Central Platform] The platform is bounded by X=19 on the East (solid rock wall from Y=8 to Y=16).
- [Central Platform Path] From stairs at (11, 13), walk North to (11, 9), then East along Y=9 to reach the ladder at (18, 9).
- The Central Platform ends at Y=8. The area North of Y=8 (from X=11 to X=15) is the water moat (Y=7). The platform is completely bounded. The Northern edge (Y=8) was bump-tested and is a solid cliff; no hidden shores.
[Entrance Area Navigation]
- To reach the main water from the entrance: From (21, 12), take stairs UP at (21, 11), walk North to (22, 8), East to (25, 8), and stairs DOWN at (25, 9).
- [East Water Channel] Surf East from (25, 9) enters a water channel at X=28/29 that heads North. The South path is blocked by rock walls at Y=12.
[Entrance Platform Borders]
- The SW corner at (20, 15) is a dead end. The path West is blocked by a rock wall at X=19, and South is blocked by Y=16. The entrance path is a strict 1-tile wide corridor from (24, 17) wrapping around to stairs at (21, 11).
[West Moat]
- Surfed West from (15, 5) to X=8/9, then South to Y=15.
- West boundary (X=7) is empirically proven to be solid rock from Y=7 to Y=16.
- [Water Boundary] The water channel at Y=5 has a solid rocky border on its South edge preventing landing directly at X=23. I must navigate East to X=28, South to Y=10, and West to land at the known shore at (25, 9), then walk to the ladder at (23, 7).
[NW Pocket]
- Accessed from 2F via ladder at 1F (1, 3). The path winds East and South to (1, 7). West of (1, 7) is a ladder DOWN to B1F at (0, 6).
- The ladder at 1F (0, 6) leads to B1F (3, 6). The "water" on B1F is walkable cave floor. This path leads to an item detour (Max Revive, Ultra Ball), but also has an unexplored plateau at (13, 14).

<hr>

<h1><code>Locations/UnknownDungeon_B1F</code></h1>

# Unknown Dungeon B1F (Map 0_227)
- Ladder from 1F (0, 6) arrives at B1F (3, 6).
- Topography: B1F features lower cave floors (TYPE_2770, which visually resembles water) and elevated plateaus (TYPE_3fe2).
- The ladder at B1F (3, 6) drops onto the LOWER floor.
- Stairs at (13, 3) go UP from the lower floor (13, 2) to the elevated plateau (13, 4).
- The South edge of the East plateau (from X=12 to X=17 at Y=5) is a solid cliff. There are no jumpable ledges here to reach the lower floor. The plateau continues West.
- Stairs at (19, 3) go DOWN from the East end of the entrance plateau to the lower floor.
- Item ball at (18, 1) on the lower floor contained a MAX REVIVE. Accessible via stairs at (19, 3).
- The East plateau connects Westward. The path at Y=4 is blocked by rock walls at X=14/15, but Y=5 is open. Path continues West along Y=5.
- Item Ball: SPRITE_bbb7 at (16, 9) on the lower floor was an ULTRA BALL.
- Plateau Path West: From stairs at (13, 3), the plateau winds SW to (6, 7). From (6, 7) it goes South to (6, 8), West to (3, 8), South to (3, 9), West to (1, 9), South to (1, 10), West to (0, 10), South to (0, 12). From (0, 12) it zigzags SE to stairs at (9, 13), which go DOWN to the North (9, 12) onto the lower floor.
- Lower Floor Path East: From the stairs at (9, 13), the lower floor continues North to (9, 8), East to (13, 8), and South to (13, 12). A gap in the rock walls at Y=12 allows passage East to an Ultra Ball at (16, 9), and South to stairs UP at (13, 13).
- CONCLUSION: The route accessed from the ladder at B1F (3, 6) is NOT fully explored! I found stairs UP at (13, 13) leading to a new plateau, but abandoned it prematurely. I must return here and thoroughly bump-test the plateau at (13, 14) before drawing any conclusions about Mewtwo's location.
- [Flooded Section]: The stairs at (13, 13) do NOT go up to a plateau. They go DOWN into actual water (`TYPE_4e8c`) at (13, 14).
- Surfing East from (13, 14) -> South to Y=16 -> East to X=19 -> North lands at a shore (19, 10).
- The land path from (19, 10) goes East and North to stairs at (27, 7), which lead back DOWN into another water section starting at (27, 8).
- Final path to Mewtwo: From (23, 15), Surf South to (23, 16), East to (26, 16), and North to land at the stairs at (26, 15). Walk North to (26, 14), East to (27, 14), and interact with Mewtwo at (27, 13).
- Mewtwo is located on the central island at (27, 13).

<hr>

<h1><code>Locations/PowerPlant</code></h1>

# Power Plant (Map 0_83)
- Entrance is at Route 10 (6, 39).
- Player starts inside at (4, 35).
- Goal: Navigate the facility and catch Zapdos.
[Layout]
- Entrance room at (4, 35). Path goes North to (4, 26).
- Room at Y=25. Carbos found at (7, 25).
- From (7, 25), path goes South to Y=27, then West.
- Path also goes West from (4, 25) to (2, 25), then North to (2, 20), then East to an open area at Y=15-17.
- Open area at Y=15-17 has paths going East (via gap at 8,15/16).
- The path going South from the open area (down X=5/6) just connects back to the Y=20 horizontal path I already took.
- Main path goes East through (8, 15/16) to an open area up to X=13.
- Solid horizontal wall at Y=12 extends from X=1 past X=17, completely blocking North.
- Path is forced South through a 1-tile gap at (13, 18) down to (13, 20).
- From (13, 20), path goes South to (13, 21).
- From (13, 21), path West along Y=21 leads to the item ball at (9, 20), which is a trap (Lv 40 Voltorb).
- From (13, 21), path East continues deeper into the facility along Y=21/22.
- At X=16/17, the path splits around machinery at (18-20, 21). North path goes East along Y=20. South path goes East along Y=22.
- BOTH the North (Y=20) and South (Y=22) paths lead to the open vertical hallway at X=34/35.
- At X=34/35, the path North is blocked by rocks at Y=15. This is a DEAD END.
- The gap at (36, 14) is Floor, but it connects to a horizontal hallway at Y=14.
- Since Y=15 is a solid wall from X=30 to X=36, the Y=14 hallway MUST be accessed from further West.
- Item ball spotted at (25, 18), above the machinery at Y=21. Accessible from the North path (Y=20).
- Item ball spotted at (21, 25). Accessible from a southern path, likely East from the start area.
- Testing the pocket at (9-11, 13-14) to confirm it is a dead end. Confirmed! The Y=12 wall is solid here, and Y=14 is blocked to the East by walls at (13-15, 14).
- Correction: The North path (Y=20) starts at X=16, not X=13. Y=20 at X=14/15 is blocked by machinery.
- Confirmed: The North wall of the Y=20 path is solid machinery from X=16 to X=33. There is no path North from here.
- Spotted Floor tiles at Y=24/25/26. This means there is a vast Southern area!
- Confirmed: The South wall of the Y=22 path is solid machinery from X=36 all the way West. There is no path South from here.
- Conclusion: The entire East section (X=14 to X=36, Y=20 to Y=22) is a massive dead-end loop.
- Re-verified entrance hallway: East wall (X=8) is SOLID ROCK from Y=24 down to Y=35. There is NO path East from the starting room.
- DISCOVERY: The path West from (13, 21) does not just lead to the trap at (9, 20). It continues SOUTH from (10, 21) to weave through the machinery and reach the Southern area at Y=24+!
- Path from (10, 23) weaves East and South through the machinery: R to (11, 23), D to (11, 24), R to (13, 24), D to (13, 26), R to (14, 26), D to (14, 27).
- From (13, 24), path continues South down X=13/14. I am currently walking South to see where it leads.

<hr>