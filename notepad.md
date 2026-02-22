<h1><code>Main</code></h1>

[Location Encounters]
Route 22: Rattata, Nidoran F
Viridian Forest: Caterpie

[Team Milestones]
- HYDRO (Squirtle) reached Lv15, learned Water Gun (replaced Bubble).

[Tile Mechanics]
- TYPE_2889: Impassable tree/solid obstacle
- TYPE_44f6: One-way ledge (jump down only)
- TYPE_fed7: Walkable tall grass
- TYPE_3fe2: Walkable normal grass
- Map Transitions: Require specific warp tiles, gatehouse doors, or screen-edge steps. Impassable boundaries/signs do not trigger transitions.

[Lessons Learned]
- Avoid over-mashing A during map transitions and battles. It causes UI desyncs, mistaken menu inputs, and turn hallucinations. Use targeted tools instead.

[Timestamps]
- Start Turn: 339 (Entered Viridian Forest navigation task)
- Grinding Start: Turn 415
- Route 2 Arrival: Turn 869

[Viridian Forest Topology]
- Entrance: (17, 47)
- Path Forward: East corridor (x=25) bypasses the solid horizontal tree line. The actual central tree boundary is at y=29.
- Dead Ends Mapped: (16, 1), (2, 30), (2, 40).
- Strategy: Return to the east path (x>17) and head north. Look for branching paths to the west.
[Inventory Items]
- TM34: BIDE (Received from Brock)

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

<hr>

<h1><code>Mechanics/Combat</code></h1>

[Turn 62] Combat basics: Turn-based. Type matchups are critical (e.g. Water beats Fire, Grass beats Water). STAB (Same Type Attack Bonus) applies for matching move and Pokémon types. Use FIGHT to attack, ITEM to use Potions.
- **Hydro (Squirtle)**: Learned Bubble (Water) at Level 8.
[Status Effects]
- Overworld Poison: Pokemon lose 1 HP every 4 steps in the overworld. Calculate exact step limit (Current HP * 4) to know exactly how far you can travel before panicking!

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

<hr>