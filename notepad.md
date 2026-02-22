<h1><code>Main</code></h1>

[Location Encounters]
Route 22: Rattata, Nidoran F
Viridian Forest: Caterpie

[Gym Strategy]
Pewter Gym: Rock type. Use Squirtle's Bubble.

[Tile Mechanics]
- TYPE_2889: Impassable tree/solid obstacle
- TYPE_44f6: One-way ledge (jump down only)
- TYPE_fed7: Walkable tall grass
- TYPE_3fe2: Walkable normal grass

[Timestamps]
- Start Turn: 339 (Entered Viridian Forest navigation task)
- Grinding Start: Turn 415

[Strategy & Boundaries]
- Viridian Forest Boundaries: Navigating the far right side. Reached x=26, previous assumptions about x>=26 being solid were incorrect.

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

<hr>

<h1><code>Mechanics/Combat</code></h1>

[Turn 62] Combat basics: Turn-based. Type matchups are critical (e.g. Water beats Fire, Grass beats Water). STAB (Same Type Attack Bonus) applies for matching move and Pokémon types. Use FIGHT to attack, ITEM to use Potions.
- **Hydro (Squirtle)**: Learned Bubble (Water) at Level 8.

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