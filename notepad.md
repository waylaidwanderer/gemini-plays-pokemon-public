<h1><code>Main</code></h1>

[Turn 207 Reflection]
- Progress: Successfully delivered Oak's Parcel, obtained the Pokedex, and am currently acquiring the Town Map.
- Tool Ideas: 1. catch_routine (bag nav) 2. heal_spam (pokemon center nav) 3. buy_item (mart nav) 4. type_matchup_agent (combat logic) 5. route_planner (map nav). For now, my `move_sequence` tool handles repetitive menu mashing perfectly.
- Goal Clarity: High. Short-term is getting the map, long-term is Pewter City Gym.
- Error Analysis: My earlier auto-walk script error was swiftly fixed by ensuring proper JSON output. No unverified assumptions currently blocking me.

<hr>

<h1><code>Quests/Main</code></h1>

[Turn 201] Active Quest: Complete the Pokedex & Become Champion.
Execution Plan:
1. Visit Gary's sister (Daisy) in the house next to mine in Pallet Town to get a Town Map.
2. Head north to Viridian City and beyond.
3. Explore new routes (Route 22, Route 2) to catch new Pokemon.
4. Navigate Viridian Forest to reach Pewter City for the first Gym Badge.

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

<hr>