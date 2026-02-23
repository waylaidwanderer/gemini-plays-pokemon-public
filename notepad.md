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

[Mt. Moon Topology]
- Start Turn: 1385
- Entrance: (14, 35)
- Encounters: Clefairy (Trainer), Zubat, Paras, Geodude
[Inventory Items]
- TM34: BIDE (Received from Brock)
[Map Boundaries - Map 0_59]
- Entrance at (14, 35) connects to Route 4.
- Raised platforms (TYPE_de37, TYPE_2889) act as walls.
- Internal warps/ladders: (25,15), (15,27), (17,11), (25,9), (15,23).
- (17, 19) is a dead end bounded by ledges/walls to the south.

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

<hr>

<h1><code>Mechanics/Combat</code></h1>

[Turn 62] Combat basics: Turn-based. Type matchups are critical (e.g. Water beats Fire, Grass beats Water). STAB (Same Type Attack Bonus) applies for matching move and Pokémon types. Use FIGHT to attack, ITEM to use Potions.
- **Hydro (Squirtle)**: Learned Bubble (Water) at Level 8.
[Status Effects]
- Overworld Poison: Pokemon lose 1 HP every 4 steps in the overworld. Calculate exact step limit (Current HP * 4) to know exactly how far you can travel before panicking!
- **Menu Navigation:** In battle, if you accidentally enter the ITEM menu, you must press B to exit it, then press Up to move the cursor back to FIGHT, then A to select it. The `battle_move_selector` tool ONLY works when the cursor is already inside the FIGHT menu (showing the 4 moves). Do not mash B to back out of menus, as you might back out of the FIGHT menu entirely.

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

[Mt. Moon Topology]
- Start Turn: 1385
- Entrance: 1F (14, 35)
- Encounters: Clefairy (Trainer), Zubat, Paras, Geodude

[Map Boundaries - Mt. Moon]
- B2F: Dead end section from ladder at (15, 27).
- B2F: Found HP UP at (25, 22).
- B2F: Raised platforms (TYPE_de37) block movement to western half.
- B1F: Isolated corridor leading to B2F dead end starts from ladder at (25, 15) on 1F.
[B2F Mechanics & Navigation]
- TYPE_2889 tiles act as impassable ledges/walls blocking eastward movement.
- Spotted a new NPC (Super Nerd?) at (30, 24).
- TM01: Mega Punch (Found in Mt. Moon B2F at 29, 5)

<hr>