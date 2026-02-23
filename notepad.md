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

[Route 24 & Route 25]
- Start Turn: 2300
- Plan: Navigate east to Bill's House. Defeat trainers along the way. Monitor HP carefully.
[Mechanics/LevelUp]
- Mashing B cancels move learning.
[Visual Cues]
- Pokemon Centers have a 'POKé' sign.
- Poke Marts have a 'MART' sign.

<hr>

<h1><code>Quests/Main</code></h1>

[Turn 201] Active Quest: Complete the Pokedex & Become Champion.
Execution Plan:
1. Head north to Viridian City and beyond.
2. Explore new routes (Route 22, Route 2) to catch new Pokemon.
3. Navigate Viridian Forest to reach Pewter City for the first Gym Badge.

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
- Connected to Route 4 (West, one-way ledges prevent returning to Mt. Moon)
- Trade House: (13, 15)
- Pokemon Center: (19, 17)
- Robbed House: (9, 11)
- Poke Mart: (25, 25)
[City Layout & Traversal]
- Route 24 connection is at x=20, y=0 (NOT x=10).
- To reach Route 24 from the Pokemon Center (19, 17), walk right to x=20, then straight NORTH.
- The Cut Tree at (23, 17) only blocks the easternmost path, not the path to Route 24.
- Do NOT go through the Robbed House to go north; that area is a dead end blocked by trees at y=6.

<hr>

<h1><code>Quests/CeruleanGym</code></h1>

# Cerulean Gym (Misty)
- Start Turn: 2188
- Type: Water
- Weaknesses: Grass, Electric
- Current Team: Wartortle (Lv 23), NidoranF, Caterpie, Rattata, Spearow, Pidgey.
- Contingency Plan (if Wartortle faints): Send in Pidgey/Spearow to use Sand-Attack/Growl to debuff the enemy, then use Potions to heal Wartortle back up.
- Strategy:
  1. Explore Route 24/25 to catch a Grass or Electric type.
  2. If no advantageous types are found, rely on Wartortle's Normal-type moves.
  3. Keep the team fully healed before challenging.

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