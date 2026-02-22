<h1><code>Main</code></h1>

[Location Encounters]
Route 22:
- Rattata
- Nidoran F
Viridian Forest:
- Caterpie

[Gym Strategy]
- Pewter City Gym: Rock type. Use Squirtle's Bubble.

[Tile Mechanics]
- TYPE_2889: Solid obstacles (trees, fences)
- TYPE_44f6: One-way ledge (jump down only)
- TYPE_fed7: Walkable tall grass
- TYPE_3fe2: Walkable normal grass

[Timestamps]
- Turn 311: Started journey north to Viridian Forest and Pewter City.

[Catching Strategy]
- Switch to Lv3 Rattata to use Tackle on Lv4 bugs to avoid KOs.
- Turn 415: Caught Caterpie (Cabbage) and Nidoran F (Cleo). Switching Cleo to lead for training. (Grinding Start: Turn 415)
- Viridian Forest: Row y=31 is a solid wall of trees from x=2 to at least x=20. The path north must be further East or I missed a branch down south.

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