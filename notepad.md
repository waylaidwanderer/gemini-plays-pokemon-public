<h1><code>Locations/Amor_City</code></h1>

# Amor City

## Amor Metro Station
- **Arrival Platform** (`latest_grid.png` & physical arrival Turn 27547):
  - Train from Sovio City arrives at the northern boarding platform (`18, 17`) in front of the green-striped train doors (`row 16`, `cols 17-23`).
  - Yellow safety line spans `row 17` (`cols 14-23`); diamond-tiled walkway narrows south through `columns 17-19` (`rows 18-21`) into the station waiting area (`row 22+`) with blue chairs on the eastern wall (`20, 20-22`).
- **Upper Ticket Concourse (`rows 22-29`)** (`latest_grid.png` Turn 27550 & physical traversal Turns 27548-27551, 27571-27572):
  - **East Turnstile Lane (Exit Only, `19, 23-24`)**: Flanked by scanner pillars (`18, 24` and `20, 24`) and station officer at `(20, 25)`. Attempting to walk north through `(19, 23-24)` from the concourse displays verbatim: *"This is where you exit, not enter!"* and steps the player south (verified Turn 27571).
  - **West Turnstile Lane (Entry / Metro Boarding, `17, 24`)**: Located between the west ticket booth (`16, 24`) and central scanner pillar (`18, 24`), guarded by the station officer at `(18, 23)` facing west. Stepping north onto `(17, 24)` triggers the prompt: *"Do you want to use the Hupest Metro Line? Yes/No"* (verified Turn 27572).
  - Ticket booths on the west (`13-16, 24-25`) and east (`21-24, 24-25`), yellow vending machines at `(16, 26)` and `(21, 26)`, and blue benches along the west (`col 12`) and east (`col 25`) walls.
  - Stepping onto `(18, 20)` on initial arrival (Turn 27548) triggers a cutscene where Asher passes through the turnstile to `(19, 24)` and Valora (`19, 25`) says: *"Ahh, here we are at last. Let's go, your dad is waiting for us down in the main lobby!"* before walking west to column 17 and south past the central brick pillar (`18-19, 28-32`) into the lower concourse (Turn 27549).
- **Lower Concourse (`rows 30-37`)** (`latest_grid.png` Turn 27552 & physical traversal Turns 27551-27553):
  - Central brick pillar (`18-19, 28-32`) with two yellow vending machines at its south face (`18-19, 32-33`), flanked by open vertical walkways at `columns 16-17` and `columns 20-21`.
  - Blue chairs at `(16, 31-33)` and `(21, 30-32)`.
  - Train timetable boards ("AMOR 16:00 / ALHIA 20:00") on the brick walls at `(12-15, 33)` and `(22-25, 33)`.
  - Two wooden staircases leading up to the Main Lobby:
    - West staircase at `(14-15, 35-36)` with vertical red mat at `(13, 35-36)` (reached via row 37 beneath the stairs); stepping `Right` from `(13, 35)` into `(14, 35)` warps to the **Amor Metro Station Main Lobby** at `(9, 3)` (verified Turn 27553).
    - East staircase at `(22-23, 35-36)` with vertical red mat at `(24, 35-36)` (`latest_grid.png` Turn 27552).

## Amor City Battle Centre / Metro Main Lobby
- **Upper Mezzanine (`rows 3-6`)** (`latest_grid.png` Turn 27555 & physical traversal Turns 27555, 27569):
  - West staircase (`7-8, 3-4`) with vertical red mat at `(9, 3-4)` connects to the Amor Metro Station Lower Concourse (`13, 35`).
  - East staircase (`12-13, 3-4`) with vertical red mat at `(11, 3-4)`.
  - Two blue escalators at `column 5` (`rows 7-9`) and `column 15` (`rows 7-9`) descend to the ground floor.
- **Ground Floor (`rows 10-21`)** (`latest_grid.png` Turns 27565-27566 & physical traversal Turns 27556-27566):
  - Central curved red reception counter (`8-12, 10-12`) with Battle Centre Assistant at `(10, 10)` and Poké Ball floor emblem at `(9-11, 13-15)`.
  - Stepping down the west escalator to `(5, 9)` (Turn 27555) triggers the Eclipse Tournament registration cutscene with Dad and Valora (Turns 27556-27561), where Asher receives the **Metro Pass** and registers for the tournament before encountering **Frio** at `(10, 14)` (Turns 27561-27564).
  - Interacting with Frio at `(10, 13)` from `(10, 14)` after registration displays verbatim: *"Maybe we shouldn't be bothering this prick..."* (verified Turn 27565).
  - Southern exit mat at `(9-11, 21)` is flanked by two lower blue escalators at `column 4` (`rows 19-22`) and `column 16` (`rows 19-22`) (`latest_grid.png` Turn 27566).
  - **Lower Arena Concourse (`rows 22-27`)**: Reached by descending the lower blue escalators at `(4, 19-22)` or `(16, 19-22)` (`latest_grid.png` Turn 27974 & physical traversal Turns 27975-27976; reached from reception by routing around the diamond pillars at `6-7, 14-18` or `13-14, 14-18` via `row 13`). Features a lower floor with a red mat at `(9-11, 27)` leading to the Eclipse Tournament arenas (per the receptionist's instructions in Turns 27971-27972).
  - **Tournament Arena Lobby (`15, 7` -> `row 17`)** (`latest_grid.png` Turns 27978, 27980):
    - Entry mat from the Lower Arena Concourse lands at `(15, 7)` (`cols 14-16, row 7`).
    - Corridor runs west along `row 6` (`cols 11-15`), south along `columns 11-12` (`rows 6-15`), and opens into a horizontal arena lobby (`cols 6-19+, rows 14-17`) with a lower blue escalator at `(6, 16-19)` on the west and a row of numbered round arena entrance mats along `row 17`:
      - **Round 1 Arena Entrance (`9-11, 17`)**: Unguarded red Poké Ball mat at `(10, 17)` prior to Round One; stepping `Down` off `(10, 17)` warps into the **Round 1 Arena** (verified Turn 27980). After Asher wins Round One, a blue-capped attendant stands at `(10, 17)` guarding the entrance (*"The round has already ended... Congrats for advancing forward!"*, verified Turn 28021).
      - **Round 2 Arena Entrance (`12-14, 17`)**: Guarded by blue-capped attendant at `(13, 17)` (*"This is where Round 2 will take place in... Not yet though."*, verified Turn 27980).
      - **Round 3 Arena Entrance (`16-18, 17`)**: Guarded by blue-capped attendant at `(17, 17)`.
    - **Post-Round-One Cutscene (`11, 9` -> `10, 9`, Turns 28021-28027)**: Stepping north onto `(11, 9)` after winning Round One triggers a cutscene with **Valora** (who also won her Round One group), the **Host** PA announcement concluding Round 1, and **Frio**, who challenges Asher to a race to **Mt. Gerhana** to find the **Eclipse Rock** before Valora joins Asher to travel to Mt. Gerhana.
  - **Round 1 Arena & Eclipse Tournament Round One (`4, 14` -> `14, 14`)** (`latest_grid.png` Turns 27983-27984 & physical completion Turns 27981-28020):
    - **Bracket & Format**: Entering `(10, 17)` displays the 8-trainer Round One bracket screen (`7, 17` map coordinate): Left side features **Asher vs. Camper Paul** and **Youngster vs. Youngster Chad**; Right side features **Roark vs. Picnicker** and **Bug Catcher Jim vs. Ruin Maniac**. No automatic healing occurs between the 3 consecutive matches.
    - **Cyber-Arena Layout**: For each match, the player materializes on a white/cyan teleporter pad at `(4, 14)`. Walking `Right 10` along `row 14` (`(4, 14) -> (14, 14)`) crosses the narrow chasm bridge (`12-13, 14-15`, where an Arena Attendant stands at `13, 15`: *"Good luck, Trainer!"*) onto the white-outlined trainer box at `(14, 14)`, which walks both trainers onto the stage (`16, 14`) and morphs the cyber-arena into a holographic rocky cavern battlefield.
    - **Match 1 (Quarterfinals — Camper Paul)**: Pre-battle quote: *"I came here to win! And I'm gonna!"*; uses 3 Pokémon—Buizel (♀, Lv11), Pidgey (♀, Lv11), and Bulbasaur (♂, Lv12); defeat quote: *"Nooooo! I lost the very first battle..."*; awards `₽576` (verified Turns 27985-27995).
    - **Match 2 (Semifinals — Youngster Chad)**: Pre-battle quote: *"I have won one battle! I'll win this one as well!"*; uses 3 Pokémon—Rattata (♂, Lv11), Timburr (♀, Lv12; Bide), and Electrike (♀, Lv12); defeat quote: *"How in the..."*; awards `₽624` (verified Turns 27996-28007).
    - **Match 3 (Round One Finals — PKMN Trainer / Leader Roark)**: Pre-battle quote: *"My name is Roark. I'm a gym leader from Sinnoh. May the stronger Trainer win!"*; uses 3 Pokémon (displayed with 4 Poké Ball icons in HUD)—Hippopotas (♂, Lv12; Sand Stream, Sand Tomb, +1 Potion), Cranidos (♂, Lv12; Mold Breaker), and Onix (♀, Lv13); defeat quote: *"... / Looks like this is the end for me. Thanks for the battle!"*; awards `₽1456` (verified Turns 28008-28019). Winning Round One returns Asher to `(10, 16)` in the Tournament Arena Lobby.
- **Exterior Plaza (`53-66, 24-29`)** (`latest_grid.png` Turn 27568 & physical interaction Turn 27568):
  - Stepping `Down` on the Battle Centre exit mat at `(10, 21)` warps outside to `(59, 25)` in Amor City (door at `59, 24`, verified Turn 27566-27567).
  - Signboard at `(56-57, 25)` interacted from `(57, 26)` reads verbatim: *"Amor Metro Station / Amor Battle Centre"* (verified Turn 27568).
  - Western street passage at `(53, 27)` is physically blocked by a construction worker who states verbatim when interacted with from `(54, 27)`: *"I'm sorry but the city is closed off due to constructions!"* (verified Turn 27568). A second construction worker sprite is visually present in the corresponding eastern street passage at `(66, 27)` (`latest_grid.png` Turn 27568; not physically interacted with).

<hr>

<h1><code>Locations/Azluf_Town</code></h1>

# Azluf Town

## Geography & Connections
- **West (`cols 0+, rows 34-35` on town map)**: Connects to Route 2 (`cols 80+, rows 58-59`) via purple brick road (`Azluf Town` banner triggers at `x=0, y=35`, verified Turn 27779).

## Story Events & Landmarks
- **Western Entrance Meeting with Professor Ivo (`3, 35` -> `12, 41` / `9, 10`)**: Stepping onto `(3, 35)` upon entering Azluf Town from Route 2 triggers a cutscene with **Professor Ivo** waiting at `(5, 34)`. She leads Asher south past the Azluf Town Pokémon Center and fountain plaza to a park bench beside a **Lake Trio (Mesprit, Uxie, Azelf) monument**, recounts her past with Jackson and the asteroid origin of The Great Eclipse, and gives Asher the **Eclipse Band** (Turn 27799) and **PokéDex** (Turn 27801) before departing (verified Turns 27779-27803).

- **Amor Battle Center Text Message (`12, 41` / `9, 10`)**: Immediately following Professor Ivo's departure, Asher received a text message from the **Amor Battle Center** announcing that the first round of the Eclipse Tournament is about to start and instructing him to return to the Battle Center in Amor City and speak with the receptionist (verified Turns 27805-27806).
- **Sinnoh Lake Guardians Monument (`13-15, 40`) & Elder (`15, 42`)**:
  - Center plaque at `(14, 40)` (interacted from `14, 41`; left tile `13, 40` is inert and `15, 41` is solid): *"Azelf / One of the Sinnoh Lake Guardians. It is told to be the bringer of willpower."* (verified Turns 27808-27810).
  - Bald elder at `(15, 42)` facing the monument: *"The 3 Sinnoh Lake Guardians... They are said to be the shapers of the human mind. Knowledge, emotions and willpower. Seeing it with my very own eyes... What a marvelous creation!"* (verified Turns 27808-27809).
- **Town Signboard (`6-7, 34`)**: Interacted from `(7, 35)`, reads verbatim: *"Azluf Town / A cozy, coastal town"* (verified Turn 27813).
- **Azluf Town Pokémon Center (`12, 33`)**: Located on the northern side of the western entrance road (`row 34`).
  - **Interior (`7-8, 8` exit mat; stepping `Down` from `7, 8` exits to `12, 34`)**: Nurse Joy at `(7, 2)` (counter at `7, 4`); PC at `(12, 1)`; pillars at `(3, 5-7)` and `(11, 5-7)` (bypassed along `row 8`); mezzanine staircase at `(2, 0)` (reached via `row 8 -> col 1 -> 2, 3 -> Up 7`).
  - **Azluf Town PokéMart Mezzanine (seamless same-map staircase transition; `7 Up` from `2, 3` reaches the counter at `5, 5`, clerk at `5, 3`)**:
    1. Poké Ball (`₽200`)
    2. Great Ball (`₽600`)
    3. Potion (`₽300`)
    4. Super Potion (`₽700`)
    5. Antidote (`₽100`)
    6. Paralyz Heal (`₽200`)
    7. Awakening (`₽250`)
    8. Repel (`₽350`) (verified Turns 28340-28343).
  - **Broken-Arm Trainer (`8, 4`)**: *"Ma'am, my arm hurts, I think I've broken it... / Nurse: I'm sorry but this is a Pokémon Center, but I can call the ambulance for you..."* (verified Turn 27818).
  - **Wandering Female Scientist (`4-5, 5-6`)**: *"I'm on a research trip, I'm just taking a small break here..."* (verified Turn 27820).
- **Claire's Organic Market (`16-19, 30-33`)**: Outdoor market stall with orange awning east of the Pokémon Center, staffed by **Claire** (`17, 32`, *"Hello, welcome to Claire's organic market!"*) and her **Bulbasaur** (`18, 32`).
  - **Inventory**:
    1. Moomoo Milk (`₽500`)
    2. EnergyPowder (`₽500`)
    3. Energy Root (`₽800`)
    4. Heal Powder (`₽450`)
    5. Revival Herb (`₽2800`)
    6. Berry Juice (`₽100`)
    7. White Herb (`₽100`)
    8. Mental Herb (`₽100`)
    9. Leaf Stone (`₽2100`) (verified Turns 27823-27825).
- **Northeast House (`25, 32`)**: Blue-roofed cottage east of the north-south avenue (`21, 9` interior exit mat).
  - **Woman in Beret (`22, 7`)**: *"Yeah I totally agree! Dynamax is so overrated! Its just Pokémon becoming big."* (verified Turn 27833).
  - **Man in Glasses (`22, 6`)**: *"Yeah I totally agree! Z moves are so overrated, they are just boosted moves!"* (verified Turn 27833).
- **Old Woman on Central Avenue (`21-22, 34-35`)**: *"There's a myth in this town, that one of Lake Guardians, Azelf, shows up here once a year. Because of this legend, the people made a statue in respect to them!"* (verified Turn 27837).
- **Northern House — Move Deleter's House (`22, 24`) & Northeast Road (`cols 21-28, rows 22-28`)**:
  - Purple brick avenue runs north along `cols 20-22` to `row 26`, where a second blue-roofed cottage stands at `(22, 24)` (`3, 9` interior exit mat), and the road branches east along `rows 26-28` to `cols 26-27` before turning north (`cols 26-27, rows 22-25`, verified Turn 27838).
  - **Move Deleter (`3, 6`)**: Male Scientist at the table: *"Hi! My herbs can delete moves! I can make Pokémon forget their moves. Would you like me to do that? Yes/No"* (verified Turn 27841).
  - **In-Game Trade — Excadrill for Golem (`7, 6`)**: Female Scientist on the right side of the room: *"I'm looking for the Pokémon Golem! Wanna trade one for my Excadrill? Yes/No"* (verified Turn 27842).
- **Southern Ledge Item Sphere (`15, 47`)**: Uncollected orange item sphere in a coastal cliff alcove south of `row 46`; enclosed by cliff walls on the north, west, and east and open only to the southern ocean water at `row 49` (**Surf-gated**, verified Turn 27887).
- **Mt. Gerhana Southern Entrance (`27, 14`)**: Reached via the northern stone stairs (`26-27, 18`) at the top of the `cols 26-27` avenue (bounded on the west at `cols 22-24` by cliffs and pine trees separating Azluf Town from the Route 2 border stairs visible at `20-21, 13-14`, verified Turns 28371-28372).
  - **Signboard (`25, 16`)**: Interacted from `(25, 17)`, reads verbatim: *"Mt. Gerhana"* (verified Turn 27845).
  - **Worker Guard (`27, 15`)**: Blocks the cave entrance prior to Round One of the Eclipse Tournament: *"I'm sorry kid, but there are some mine works going on... We will move out of the way later!"* (verified Turn 27845). After Asher wins Round One of the Eclipse Tournament and accepts Frio's challenge, the guard is gone and stepping onto `(27, 14)` enters **Mt. Gerhana** (verified Turn 28074).
- **Eastern House — Professor Oak's House (`31, 24`)**: Blue-roofed cottage at the eastern end of the `row 26` purple brick road (`37, 10` interior exit mat).
  - **Professor Oak (`40, 7`) — Special Quest #11 ("Oak's Research", Active)**: Kanto Pokémon Professor with a yellow Special Quest bubble: *"Oh, hello there! You must be a Pokémon Trainer! You also seem to have a PokéDex, may I check it? Wow, this is a well made PokéDex! It's way more complex than mine... However it's pretty empty... Oh, how rude of me, I didn't even introduce myself... My name is Oak, I'm a Pokémon professor from the Kanto Region. I research Pokémon and gather data of them... Would you help me in my research? Yes/No"* (verified Turns 27848-27849). Accepting the quest (Turn 28501) triggers the **Special Quests!** tutorial and assigns **Task 1**: *"You first task will be to show me the PokéDex with 10 Pokémon caught."* (verified Turn 28502).
- **Southeastern Coastal Ridge & Fishing Rod Giver (`37, 30`)**: Reached via stone stairs at `(34-35, 29)` south of Professor Oak's house.
  - **Fisherman (`37, 30`)**: Asks *"Tell me, kid... Do you like fishing? Yes/No"*. Answering *Yes* rewards the **Fishing Rod** (*"Take this, it might help you relax and also help you catch Pokémon! Obtained the Fishing Rod!"*, verified Turn 27854).
  - **Wild Fishing Encounters (`36, 31` facing `36, 32`)**: **Remoraid** (♂, Lv6; Water-type, verified Turn 27865).
- **Southeastern Overlook, Sailor (`28, 45`) & Azluf Town Lighthouse (`34, 46`)**:
  - **Sailor (`28, 45`)**: *"The town's lighthouse is what brings light to the coast at night so that ships can easily navigate."* (verified Turn 27879).
  - **Azluf Town Lighthouse (`34, 46`)**: Cottage attached to the coastal lighthouse tower (`53, 9` interior exit mat).
    - **Sick Spearow (`53, 5`)**: *"Spearow: Spear... / He seems sick..."* (verified Turn 27882).
    - **Old Gentleman (`52, 5`) — Quest #4 ("Medic!", Completed)**: Explains: *"My Spearow... He's really sick... He can be cured, but for that I need a special type of flower... I heard it grows on Route 2, in a closed off spot, only accessible from Mt. Gerhana. So... will you help me? Yes/No"* (verified Turns 27883-27885; accepted in Turn 28461). Delivering the **Cure Flower** (collected at Route 2 `45, 14` in Turn 28485) cures his Spearow, completes Quest #4, and rewards the **Exp. Share** into the Items Pocket (verified Turn 28495).
  - **Eastern Cliff Overlook Behind Lighthouse (`44, 46` & `44, 47`)**: Romantic couple looking out over the sea—young man at `(44, 46)` (*"It isn't as beautiful as you..."*, verified Turn 28497) and girl at `(44, 47)` (*"The sea is so beautiful isn't it?"*, verified Turn 28498).

<hr>

<h1><code>Locations/Inizio_Isle</code></h1>

# Inizio Isle - Asher's Home

## 2F Bedroom
- **Layout**: Bed at (6, 3)-(6, 5); stairs down at (10, 4); desk/terminal at (0, 4).
- **Exits**: Staircase warp at (10, 4) leads down to 1F.

## 1F Living Room
- **Layout**: Stairs up at (3, 4); wide-screen TV at (7, 3)-(9, 4); front door exit is at (10, 10) with doormat at (10, 9).
- **Verified Collisions**:
  - Bookshelf at (5, 4) is solid; bypass via row 5.

## Inizio Isle Exterior
- **House Front**: Door exit lands at (17, 17).
- **South Cove Beach**:
  - Central stairs at (17, 23)-(17, 25) lead down to sandy beach at rows 28-29.
  - Western boundary: Column 14 (water's edge with sea boulders, verified Turns 217-218).
  - Eastern boundary: Column 21 (water channel, verified Turns 219-220).
  - Southern boundary: Row 31/32 (water's edge with rocks).
  - Enclosed cove with no dock or boat; exit is strictly north via stairs.
- **Southeast Ridge**:
  - Accessible via wooden steps at (24, 18)-(26, 19).
  - Dirt platform at rows 20-25, columns 23-26. Overlook with waterfall to west.
  - Wooden bridge at (27, 23) connects Southeast Ridge directly to Eastern Coastal Lawn and Dock (verified Turn 230).
  - Eastern Coastal Lawn leads directly east to the wooden dock at rows 24-26, columns 32-35.
- **Western Trail**:
  - Column 12 corridor: (12, 18) <-> (12, 14) is clear grass.
  - (12, 13) north is blocked by chimney/trees (verified Turn 167).
  - (11, 16) has white flowers; (10, 16) is open between pines (verified Turn 169).
  - (10, 15) north is blocked by pine foliage (verified Turn 170).
  - (12, 19) south of (12, 18) is blocked by pine tree (verified Turn 173).
  - (10, 18) west of (11, 18) is blocked by cliff edge (verified Turn 175).
  - (11, 19) south of (11, 18) is blocked by cliff/foliage (verified Turn 176).

## Eastern Cliff Area & Verified Collisions
- Area above wooden steps: Small grass lawn at (27-28, 16).
- Tile (28, 15) north of (28, 16) is an impassable cliff ledge (verified Turn 137).
- Tile (27, 15) north of (27, 16) is an impassable cliff ledge (verified Turn 152).
- Tile (28, 17) south of (28, 16) is an impassable cliff corner (verified Turn 154).
- Tile (26, 16) and (26, 17) form a 1-tile wide WALKABLE corridor between pine tree (col 25) and cypress tree (col 27) (verified Turns 156, 160)!
- Corridor connects north lawn directly to row 18 at (26, 18) (white flowers).

<hr>

<h1><code>Locations/Lancio_Town</code></h1>

# Lancio Town

## Harbor / Dock

- **Dock**: Wooden pier at rows 23-26, columns 32-34.

- **Surroundings**:

  - Cobblestone/gravel path leads north from the dock into the main town.

  - Ocean to south and west.

## Points of Interest & Buildings

- **Pokémon Center**: Located east of the main north-south path at (36-39, 11-15); door at (37, 14). Interior exit mat at (7, 8). Features blue-carpeted escalator in northwest corner at (2, 0-1) leading to upper mezzanine. Resident man at (9, 4) verified post-tremor (Turn 27465, 3 boxes): "Did you know?" / "Pokémon Centers have PokéMarts built into them in this region!" / "In certain regions PokéMarts are separate buildings though...". Resident boy at (5-6, 5-6) verified post-tremor (Turn 27466, 2 boxes): "Pokémon Centers heal your tired, hurt, or fainted Pokémon." / "They make all Pokémon completely healthy.". Northeast PC kiosk at (9-10, 0-1) is enclosed behind the service counter as a decorative fixture; PC access is handled via the Sovio City terminal or HuPhone app.
  - **Upper Mezzanine & PokéMart**: Escalator warps to (5, 8). Counter staffed by clerk at (5, 3) facing south across counter at (5, 4). Verified inventory: Poké Ball ($200), Potion ($300), Antidote ($100), Paralyz Heal ($200), Repel ($350) (identical to Sovio City PokéMart).

- **Residential House (Northwest)**: Located at (25, 10). Interior entrance mat at (39, 8); resident boy at (44, 4). Gifts TM17 (Protect) after persistent dialogue, then kicks Asher outside to (25, 11). Subsequent interactions display "Get out!" and warp Asher outside to (25, 12) (verified post-tremor Turn 27471).

- **House (Northeast)**: Located at (40-42, 6-9) east of pond. Non-enterable decorative building with aquarium window at (40, 8-9); solid building foundation with no accessible doors or entrance.

- **Professor Ivo's Pokémon Laboratory**: Verified via signpost at (21, 13) ("Ivo's Pokémon Laboratory"). Large facility in the far northwest with burgundy roof, grey pillars, and red foundation trim. Verified entrance door at (17, 11-12); column 18 is a solid exterior pillar.

- **Town Plaza & Pond**: Northeast of center; contains a pond, bench.

- **Town Signpost**: 2-tile wooden billboard located at (28-29, 13) on the main avenue; reads "Lancio Town / The town of blooming" (`latest_grid.png` Turn 27459).

- **East Avenue Bottleneck (31-32, 14)**: Single-tile east-west bottleneck along row 14 bounded by solid pine trees at (30-31, 12-13) and (30-31, 15-16) and the NPC in Cap's wander box at (32-33, 13-14) (`latest_grid.png` Turn 27459, verified Turn 27475).

## Visible Field Items

- **Poké Ball Item 1 (Golden Ball at 38, 4)**: Located on northern grass strip (row 4). Verified isolated on foot: eastern corridor blocked by solid pond bank/house collision at (39, 7); western bank blocked by stationary Old Man & Woman at (32-33, 8); requires Surf.

## Professor Ivo's Pokémon Laboratory (Interior)

- **Entrance Foyer**:

  - Door lands at (12, 12) on red mat facing north.

  - Green runner rug extends along column 12 from row 12 to row 9.

  - Framed regional map on wall at (17, 8): Interacting facing Left from (18, 8) displays 'A Town Map.'

  - Western wing breakroom: table with coffee cup on red rug (cols 5-6, rows 7-8), refrigerator at (7, 5), sink at (5, 5), TV at (3, 5), bookshelf at (1, 5) (all decorative breakroom fixtures).

- Stairs at north wall: Apparent descending wooden staircase. Accessed via red capsule mat at (12, 7) (tile 11, 7 is the side railing). Stepping onto (12, 7) triggers story barrier text: "I probably shouldn't head down here..." (verified post-tremor Turn 27076).

- **East Research Wing (Comprehensive Audit)**:

  - Connected to foyer via hallway at row 10 (columns 13-16).

  - Sunlit diagonal wood flooring throughout research room.

  - Cylindrical incubator apparatus at (18-19, 5-6): Interacting facing North from (19, 6) displays 'Better not mess with that machine.'

  - Professor Ivo at (20, 6): Ambient dialogue ("Hey, Ashi, how's your new Pokémon?", verified post-tremor Turn 27080).

  - Server tower at (23, 8-9): Inert decorative fixture.

  - Wooden research desk at (21-23, 4): Inert decorative fixture.

  - Bookshelf at (24, 4): Displays "It's crammed full of Pokémon books."

  - Blue computer workstation at (24, 8-9): Inaccessible behind server tower.

## Southwest Beach & Coastline
- **Coastline / Sandy Beach**: Located southwest of Professor Ivo's Lab at columns 14-20, rows 14-18. Westernmost land at (13, 16-17), southern peninsula at (15, 18), and eastern shoreline at (19, 17) are natural shorelines bordering open ocean.
- **Terrain**: Sand patch flanked by grass to north (row 14) and east (columns 20-21). Ocean water borders south (row 18+) and west.

## Eastern Border & Route 1 Exit

- **Signboard**: Located at (44, 13) marking "Route 1 ----->".

- **Exit Path**: Cobblestone road at rows 14-15 leads directly east past column 44 into Route 1.

- **House (South / Dockside) & Column 39 Harbor Lane**: Located at (35-38, 17-20) northeast of pier (`latest_grid.png` Turn 27459). Decorative building with sliding door facade; non-enterable exterior. Column 39 across rows 15-22 east of the house forms a walkable north-south lane connecting the main avenue to the Fisherman at (38, 22) (verified Turn 27467).

## Overworld Residents & NPCs

- **Green-haired Girl**: Wanders in 2x2 box at (22-24, 14-15). Verified post-tremor (Turn 27476, 1 box): "Lancio has such pretty flowers, I wanna collect them all!".

- **NPC in Cap**: Wanders at (32-33, 13-14) on the east avenue. Verified post-tremor (Turn 27461, 2 boxes): "Living in a small town sucks... There's nothing to do." / "I wanna live in the big capital, Amor City!".

- **Old Man**: Located at (32, 8) near pond plaza. Verified post-tremor (Turn 27463, 2 boxes): "I have grown up in this place, and I never want to leave it..." / "This is home for me."

- **Old Woman**: Located at (33, 8) near pond plaza. Verified post-tremor (Turn 27463, 2 boxes): "With my husband we have been living here for over 30 years..." / "I haven't grown up here though. I used to live in Sinnoh."

- **Fisherman (Red Cap)**: Located at (38, 22) near the harbor dock. Verified post-tremor (Turn 27467, 3 boxes): "You know kid... fishing taught me one very important thing in life." / "However it goes, you must stay calm and patient, because if you" / "calm and patient, because if you do, good things might come." Does not provide Old Rod or story progression.

- **Lancio Harbor Boat Audit**: Wooden pier spans columns 32-34 across rows 23-25, ending at row 25 with row 26 being water. Harry is not present and no boat is moored; the pier terminates at open water (verified post-tremor Turn 27068).

<hr>

<h1><code>Locations/Mt_Gerhana</code></h1>

# Mt. Gerhana

## Geography & Connections
- **Southern Entrance (`6, 30` interior <- `27, 14` Azluf Town)**: Connects to Azluf Town at `(27, 14)` (unlocked after winning Round One of the Eclipse Tournament, verified Turn 28074-28076). Stepping `Down` from `(6, 30)` exits back to Azluf Town. The western side of the 1F main cavern (`cols 5-9, rows 23-29`, where a Hiker wanders around `7-9, 23-25` stating *"This mountain is said to be sorrounded by some mystical energy!"*, verified Turn 28539, and an inert small rock sits at `6, 25`) is closed off on the west by the solid outer cave wall at `col 4` (`latest_grid.png` Turn 28447, verified Turn 28448).
- **Northern Ladder (`9, 19` -> `9, 17` interior <-> `13, 9` exterior clearing)**:
  - Ascending the wooden stairs north of Roark at `(8-10, 21-22)` reaches `(9, 20)`. Climbing the vertical wall ladder rungs from `(9, 19)` up to `(9, 17)` warps out to an exterior mountain clearing of **Mt. Gerhana** at `(13, 10)` in front of the cave mouth at `(13, 9)` (verified Turns 28090-28092 & 28328-28329).
  - **Solid Wall Behind Roark (`cols 11-18, rows 18-22`)**: Directly behind Roark (`13, 23`), the cavern floor at `(14-15, 21-22)` is closed off on the north and west by solid cliff walls (`cols 11-18, rows 18-20`, verified Turn 28313), while `rows 14-15` is a north-facing cliff wall dropping down into the Northern 1F Chamber (`cols 18-25, rows 6-16`, bounded on the west at `cols 17-18` by the outer map wall, verified Turns 28331 & 28358).
  - **Exterior Mountain Pass (`13, 10` -> `13, 15` -> `6, 14` -> `5, 9` -> `2, 6`)**: Descending the mountain steps (`13, 11-15`, bounded on the south at `row 17` and east at `col 18` by solid mountain walls, verified Turn 28329-28330) and following the canyon pass west along `rows 14-15` (`cols 6-13`) and north along `cols 4-6` (`rows 7-14`) leads to a second cave entrance at `(2, 6)` with a wooden signboard at `(4, 7)` (interacted from `4, 8`) reading verbatim: *"Route 2 / A hidden path"* (verified Turns 28092-28095). Stepping into `(2, 6)` exits to the closed-off northern enclave of **Route 2** at `(38, 9)` directly behind the Pokémon Day-Care yard (verified Turn 28098).
- **Eastern Underpass Bridge (`cols 16-24, rows 23-25`) & Upper North-South Bridge (`cols 19-21, rows 20-27`)**:
  - **From the main cavern floor east of Roark (`14-15, 23-25`, with an inert small rock at `15, 26`, verified Turn 28541)**, a horizontal wooden bridge at `cols 16-24, rows 23-25` passes directly underneath the elevated north-south wooden bridge (`cols 19-21`) to reach the **1F Eastern Cavern Floor (`cols 24-33, rows 23-26`)** (verified Turn 28106).
  - **1F Eastern Cavern Floor (`cols 24-33, rows 23-26`)**: Contains a small rock at `(27, 23)` and a wandering Hiker NPC around `(26-29, 25-26)`, and is enclosed on the south (`row 27`) and east (`col 34`) by cliff walls (`latest_grid.png` Turn 28277, verified Turns 28142, 28277-28283).
  - **Northeastern Stairs (`28-30, 21-22`) & Floor Ladder (`29, 18` -> B1F `37, 15`)**: Ascending the wooden stairs at `(28-30, 21-22)` reaches an enclosed upper terrace (`cols 27-31, rows 17-20`, with an inert small rock at `31, 20`). From here, an orange item sphere is visible on an elevated northern ledge at `(24, 13)` next to wooden stairs at `(22, 13-14)` (`latest_grid.png` Turn 28115). Stepping onto `(29, 18)` and pressing `Down` descends to **Mt. Gerhana B1F** at `(37, 15)` (verified Turns 28114-28116 & 28273).

## Wild Pokémon
- **Geodude**: Encountered at Lv11 (♀, Rock/Ground) on the 1F main cavern floor at `(13, 24)` (verified Turn 28082) and at Lv11 (♀, Rock/Ground; knows Rollout) on B1F at `(37, 18)` (caught in a Poké Ball, nicknamed **Vesta**, and sent to Box 1 in Turns 28632-28641).
- **Gulpin**: Encountered at Lv10 (♂, Poison) on the upper terrace at `(29, 20)` (verified Turns 28109-28110).
- **Roggenrola**: Encountered at Lv10 (♀, Rock) on the 1F upper terrace at `(29, 20)` (verified Turns 28112-28114) and at Lv9 (♂, Rock; knows Tackle) on B1F at `(33, 23)` (caught in a Poké Ball, nicknamed **Bolide**, and sent to Box 1 in Turns 28623-28629).
- **Aron**: Encountered at Lv7 (♀, Steel/Rock) at the base of the northern ladder at `(9, 20)` (verified Turn 28327).
- **Zubat**: Encountered at Lv8 (♂, Poison/Flying) near the southern entrance at `(7, 27)` (verified Turn 28332) and at Lv7 (♂, Poison/Flying) at `(6, 28)` (caught in a Poké Ball, nicknamed **Umbra**, and sent to Box 1 in Turns 28659-28662).
- **Whismur**: Encountered at Lv10 (♂, Normal; knows Disarming Voice and Pound) near the southern entrance at `(6, 28)` (caught in a Poké Ball, nicknamed **Quasar**, and sent to Box 1 in Turns 28665-28678).

## Story Events & Landmarks
- **Southern Entrance Cutscene (`6, 29`)**: Stepping north from `(6, 30)` onto `(6, 29)` triggers a cutscene with **Valora** (`7, 29`), who wonders what the Eclipse Rock looks like (*"This is the place I think. I wonder how that rock looks... Will we even know when we find it?"* / Asher: *"I'm sure we will, it must be something very unique..."*). The camera cuts deeper into Mt. Gerhana, where **Frio** remarks *"I must be close to it... And there's no sign of that prick as well. I thought he will at least show up so that I can mess with him... Oh well."* before descending a wooden ladder into a lower pit (verified Turns 28077-28078).
- **Sinnoh Gym Leader Roark (`13, 23`) — Quest #18 ("Roark's Opal", Completed)**: Standing east of the northern stairs (`8-10, 21-22`) with a side quest bubble: *"Hmm, no, not here... Oh, hello there, Asher! Didn't expect to see you so soon after my loss again... So, what's up? / Asher: Just passing by... What about you? / Roark: Ah, you see... I am looking for a rare gem, an Opal to be specific. I love collecting rare minerals and such, but I can't find any... Oh, I know! I know it might be a lot to ask, but will you help me find an Opal? Yes/No"* (verified Turns 28084-28086). Accepting the quest (Turn 28413) gives the hint: *"Hmm, they are usually exposed to air, so they are easy to notice, but... / Hmm, maybe try on this level, or a higher one, I'll look around here!"* (verified Turn 28414), and spawns a golden **Rare Opal** sphere at **`(35, 28)`** on Mt. Gerhana 1F (collected into Key Items Pocket in Turn 28432). Delivering the Rare Opal to Roark completes Quest #18 and rewards all **11 Fossils** into the Items Pocket: **Old Amber**, **Helix Fossil**, **Dome Fossil**, **Skull Fossil**, **Armor Fossil**, **Cover Fossil**, **Plume Fossil**, **Jaw Fossil**, **Sail Fossil**, **Root Fossil**, and **Claw Fossil** (verified Turns 28443-28445).

## Mt. Gerhana B1F (`37, 15` Ladder Entry)
- **Entry Chamber (`cols 27-38, rows 13-20`)**: Reached by descending the floor ladder from 1F `(29, 18)` to B1F `(37, 15)` (`latest_grid.png` Turns 28116-28117 & 28619). Bounded on the north (`rows 13-14`), east (`col 39`), and west (`col 26, rows 15-21`, which separates the Entry Chamber and underground pond `27-29, 19-24` from the Eastern Staircase `25-26, 15-18`) by solid cave/cliff walls, with a 2x2 rock cone at `(29-30, 16-17)`, inert small rocks at `(38, 19)` and `(30, 21)`, and wooden stairs at `(33-35, 20)` descending onto a central ridge (`cols 31-35, rows 21-26`, which has a rock cone at `34, 24` and southern stairs at `33-35, 26`, verified Turn 28618).
- **Hiker Zion (`35, 23`, facing West)**:
  - **Pre-Battle Quote**: *"Ahoy, you are exploring the caves too?"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Sandshrew (♀, Lv12; Ground).
    - **Pokémon 2**: Sandile (♂, Lv12; Ground/Dark; Ability: Intimidate).
    - **Pokémon 3**: Trapinch (♂, Lv13; Ground; knows Bulldoze).
  - **Outcome**: Defeat quote: *"That was quick..."* (verified Turns 28120-28129).
- **Western Pond Ledge & Super Potion (`27, 25`)**: Descending from Hiker Zion's ridge (`33, 23 -> 33, 27 -> 30, 27`) and ascending the wooden stairs at `(29-30, 26)` leads to `(27-31, 25)` on the southern/western side of the underground pond (`28-30, 21-24`), where a **Super Potion** spray-bottle sprite rests at `(27, 25)` (collected Turn 28132); bounded on the west and south by a diagonal cliff ridge at `(26, 25)` and `(27, 26)` (`latest_grid.png` Turn 28508, verified Turn 28509).
- **Southern Corridor & Terraced Cliffs (`cols 22-33, rows 27-38`)** (`latest_grid.png` Turns 28132, 28147, 28159):
  - From the bottom of the pond stairs (`30, 27`), the cavern floor continues south past a 2x2 rock cone (`31-32, 28-29`) and a rectangular floor pit (`30-31, 33-34`) along `column 29` (`29, 31 -> 29, 38`, with an inert small rock at `31, 38`).
  - Terraced western cliffs (`cols 23-28, rows 27-37`) feature small rocks at `(26, 31)`, `(27, 32)`, and `(26, 35)`, while the southern corridor wraps west along `row 38` (`cols 22-30`) and north along `column 22` (`22, 38 -> 22, 32`) onto the southern end of the B1F north-south wooden bridge.
  - **Bug Catcher Gough (`28, 36`, facing East)**:
    - **Pre-Battle Quote**: *"What is a bug catcher like doing here? You will see!"*
    - **Team (2 Pokémon)**:
      - **Pokémon 1**: Dwebble (♂, Lv13; Bug/Rock; Ability: Sturdy; knows Sand Attack).
      - **Pokémon 2**: Dustox (♀, Lv13; Bug/Poison; knows Confusion).
    - **Outcome**: Defeat quote: *"Oh my..."*; awards `₽676` (verified Turns 28148-28158).
- **B1F North-South Wooden Bridge (`cols 20-22, rows 17-32`)** (`latest_grid.png` Turn 28161):
  - Spans north from `(20-22, 32)` to `(20-22, 17)`, connecting at the northern end (`row 16`) to both the western staircases (`cols 15-17, rows 21-26`, where a Hiker Trainer stands at `15, 22`) and the eastern staircase (`25-26, 15-18`).
  - **Collector Marsh (`20, 20`, facing East)**:
    - **Pre-Battle Quote**: *"H-hey, you like rare Pokémon? Wanna see mine?"*
    - **Team (1 Pokémon)**:
      - **Pokémon 1**: Emolga (♂, Lv14; Electric/Flying; knows Charge and Spark).
    - **Outcome**: Defeat quote: *"I thought they are unbeatable!"*; awards `₽560` (verified Turns 28161-28174).
- **Western B1F Staircases (`cols 15-17, rows 21-26`) & Coworker Garner (`15, 23` -> `16, 23`)**:
  - Two consecutive wooden staircases (`15-17, 21-22` and `15-17, 25-26`, separated by a landing at `15-17, 23-24`) descend from the upper western terrace (`cols 15-18, rows 16-20`) to the lower western floor (`cols 15-19, rows 27+`).
  - **Coworker Garner (`15, 23`, facing East)**:
    - **Pre-Battle Quote**: *"We just finished our clean up works on this level and I have nothing to do... Wanna battle?"*
    - **Team (3 Pokémon)**:
      - **Pokémon 1**: Magnemite (Lv13; Electric/Steel; Ability: Sturdy; knows Thunder Wave).
      - **Pokémon 2**: Machop (♂, Lv13; Fighting; knows Focus Energy).
      - **Pokémon 3**: Geodude (♀, Lv14; Rock/Ground; knows Rock Polish).
    - **Outcome**: Defeat quote: *"My god..."*; awards `₽560` (verified Turns 28179-28188).
- **B1F Underpass (`17, 27 -> 23, 27 -> 25, 25`) & Eastern Staircase (`25-26, 15-18 -> 25, 14`)**:
  - From the bottom of the lower western stairs (`17, 27`), the cavern floor passes underneath the north-south wooden bridge (`cols 20-22, rows 27-31`) to `(23, 27)`, wraps north/east around the boulder at `(23-24, 23-24)` via `(23, 25) -> (25, 25)`, and ascends the eastern staircase (`25-26, 18 -> 25-26, 15`) onto the northern B1F platform (`cols 22-30, rows 7-14`, verified Turns 28190-28192).
- **Northern B1F Platform (`cols 23-32, rows 7-14`) & Cave Archway (`29, 7`)**:
  - Bounded on the southwest by the deep chasm (`cols 19-24, rows 13-15`), leads north to a cave archway at `(29, 7)` (`latest_grid.png` Turn 28193), and is sealed off on the east by two 2x2 rock cones at `(31-32, 10-11)` and `(33-34, 11-12)` against a 2-tier boundary cliff wall (`35-38, 9-13`, verified via `latest_grid.png` Turn 28520 and collision testing Turns 28520-28522).
  - **Hiker Griffin (`28, 10`, rotating)**:
    - **Pre-Battle Quote**: *"I have a goal, to hike the highest mountains all over Hupest. I wanna build some confidence by battling first though... Wanna help?"*
    - **Team (4 Pokémon)**:
      - **Pokémon 1**: Geodude (♀, Lv13; Rock/Ground; Ability: Sturdy; knows Rock Polish).
      - **Pokémon 2**: Roggenrola (♂, Lv12; Rock; knows Harden).
      - **Pokémon 3**: Geodude (♂, Lv13; Rock/Ground; Ability: Sturdy; knows Magnitude).
      - **Pokémon 4**: Onix (♂, Lv13; Rock/Ground; knows Curse and Rock Tomb).
    - **Outcome**: Defeat quote: *"Ah, that's a shocker."*; awards `₽520` (verified Turns 28193-28215).
- **Northern 1F Chamber (`24, 6` Entry from B1F `29, 6`) & Moon Stone Ledge (`24, 13`)**:
  - Stepping into the B1F cave archway at `(29, 6)` warps to the northern chamber of **Mt. Gerhana 1F** at `(24, 7)` (`latest_grid.png` Turn 28358; bounded by solid outer cave walls on the north at `row 4`, west at `cols 17-18`, and east at `col 27`).
  - Walking west and south (`24, 7 -> 20, 7 -> 20, 13`) and ascending the diagonal wooden stairs at `(22, 13-14)` reaches the elevated ledge (`23-25, 9-13`), which contains a solid-collision 2x2 rectangular pit at `(24-25, 10-11)` (verified from `23, 10-11` in Turn 28526), an inert small rock at `(24, 14)` (verified Turn 28527), and an orange item sphere at `(24, 13)` yielding a **Moon Stone** (collected Turn 28223).
- **1F North-South Wooden Bridge (`cols 19-21, rows 17-27`) & Black Belt Joss (`19, 20`)**:
  - Spans south from the northern 1F chamber (`19-21, 17`) over the horizontal underpass bridge (`cols 16-24, rows 23-25`).
  - **Black Belt Joss (`19, 20`, facing East)**:
    - **Pre-Battle Quote**: *"Aren't you scared of falling down? And how about losing a battle?"*
    - **Team (2 Pokémon)**:
      - **Pokémon 1**: Makuhita (♀, Lv13; Fighting).
      - **Pokémon 2**: Pancham (♀, Lv14; Fighting; knows Work Up and Karate Chop).
    - **Outcome**: Defeat quote: *"What a strength!"*; awards `₽1008` (verified Turns 28226-28238).
- **Southern 1F Platform (`18-28, 28-35`), Hiker Frost (`22, 28`) & Cliff-Top Ledge (`24-35, 28`)**:
  - Reached at the southern end of the 1F north-south wooden bridge (`21, 28`), and bounded on the south (`rows 35-37`, with a 2x2 rock cone at `23-24, 33-34` blocking a small closed alcove at `23-24, 35-36` against a south-facing cliff wall at `row 37`, verified via `latest_grid.png` Turn 28529 and screen Turn 28530) and along `col 28, rows 29-35` by cliff walls, inert small rocks (`26, 33` and `29, 32`), and dark pits (`17-22, 34-36` and `27-28, 33-36`), while a walkable 1-tile cliff-top ledge extends east along `row 28` (`24, 28 -> 35, 28`, where the **Rare Opal** spawned at `35, 28` during Quest #18 and terminates at the solid eastern outer cave wall at `col 36`, verified via `latest_grid.png` Turn 28512).
  - **Hiker Frost (`22, 28`, facing West)**:
    - **Pre-Battle Quote**: *"Ohohoho, a Trainer? What are you doing here?"*
    - **Team (1 Pokémon)**:
      - **Pokémon 1**: Gligar (♀, Lv15; Ground/Flying; knows Payback, Harden, Sand Attack, and Quick Attack).
    - **Outcome**: Defeat quote: *"..."* (verified Turns 28243-28251).
  - **Southern Pit Ladder (`20, 33-35` -> Lower Pit Chamber `5, 28`)**: At the southern edge of the 1F platform (`20, 33-35`), a wooden ladder descends into the lower pit chamber at `(5, 28)` (verified Turns 28253-28257).
- **Lower Pit Chamber (`5, 28` Entry from 1F `20, 35`)**:
  - **Mine Workers & Blocked Passages (`14, 25` & `14, 34`)**: Enclosed on the west (`col 4`), south (`row 34`), and east (`col 17`) by solid cave walls (`latest_grid.png` Turns 28361-28362 & 28517), with inert small rocks at `(14, 28)` and `(5, 32)` (on the western ledge `cols 5-6, rows 28-34`, verified Turns 28517-28518) and a cliff edge at `(12, 33)` separating `(12, 32)` from `(13, 33)` (verified Turn 28516). Workers at `(8, 30)` (*"We are doing some work here, kid!"*), `(11, 27)` (*"We are doing some work here..."*, standing in the 1-tile gap above the cliff corner at `11, 28` to block the northern cave archway at `14, 25`), `(13, 29)` (*"We are cleaning up the path here, wait until we are done! We still have a lot of work to do though..."*), `(13, 32)` (*"We are cleaning up the path to deeper parts of the cave... We still have a lot of work to do though..."*, verified Turn 28363 & 28516), and `(15, 31)` (*"Ahh, when will we finish this?!"*) alongside a Machop at `(14, 32)` (*"Machop: Chop! Chop!"*) block both the northern exit (`14, 25`) and the boulders (`13, 33`, `14, 33`, `15, 32`, `13, 34`, `15, 34`) surrounding the floor ladder at `(14, 34)`.

<hr>

<h1><code>Locations/Route_1</code></h1>

# Route 1

## Connection & Geography
- **West**: Connects to Lancio Town via cobblestone road at (0, 45-46).
- **Northeast**: Connects to Sovio City via gateway at (53, 0).
- **Terrain**: Cobblestone road in the southwest (rows 45-46) transitions into dirt paths and tall wild grass patches (rows 44-49) heading east. A Sand Highway (columns 35-37, rows 26-38) leads north toward a roadside cottage and northeast meadow.

## Landmarks & Signposts
- **Signboard 1 (Route 1 Entrance)**: Located at (10, 47) south of central pine tree; reads "Route 1: Everything starts small."
- **Signboard 2 (Trainer Tips)**: Located at (19, 42); reads "Trainer Tips! If your Pokémon get injured you can easily heal those damages in a Pokémon Center or with Potions."
- **Signboard 3 (Trainer Warning)**: Located at (40, 26) outside the cottage; reads "Warning! Be on the lookout for Pokémon Trainers who want to fight."
- **Signboard 4 (Sovio City Approach)**: Located at (50, 10) in northeast meadow; reads "Sovio City Up ahead."
- **Central Pine Tree**: Located at (10, 44-46) dividing western and eastern grass patches.
- **Route 1 Cottage**: Located at (37, 24); interior at (4, 9). Resident boy at (6, 7) gifted a Max Repel; subsequent dialogue displays verbatim: "Now that you got your sample, go and enjoy freedom!" (verified post-tremor Turn 26692). Single room with no rear exits.

## Overworld Obstacles & Key Features
- **Cypress Bypass (Sand Highway Southern Connection)**: From the southern corridor (row 43), enter column 26 north to row 41, traverse east along the blue flower corridor across (27-29, 41) south of the cypress trees, turn north through column 29 (rows 40-39) east of the cypress trees, and step east onto the Sand Highway at (30-32, 39).
- **Cut Tree**: Located at (5, 44) between pine trees, directly north of the cobblestone road at (5, 45). Confirmed completely inert to 'A' inspection (no dialogue or interaction text); functions as a solid physical obstacle blocking northern forest access.
- **Row 20 Cottage Ledge & Northeast Meadow Routing**: One-way south-facing ledge spanning columns 39-41 at row 20. Jumpable from north to south; blocks northbound passage east of the cottage. Southbound passage from the Northeast Meadow at (47, 15) is blocked by pine tree canopy collision (verified Turn 27442), while column 50 across rows 11-18 and row 18-19 across columns 40-50 provide a completely open route to jump south over (40, 20) (verified Turns 27443-27444).
- **Northern Hedge Corridor (Row 11)**: Passable 1-tile horizontal corridor along row 11 (columns 30-34) connecting the northern red rock meadow (column 34, row 10) west into the Northwest Clearing.
- **Northwest Clearing Southern Bypass**: Passable corridor down column 27 (rows 19-22) around rock spire (26, 18-19), connecting east along row 22 (columns 28-29) and south down column 29 (rows 22-25) directly to the Sand Highway (row 26).
- **Row 43 Northern Corridor Collision**: Row 43 is blocked to the west at (11, 43) by solid pine tree canopy collision; does not connect west across column 11.
- **Row 43 Hedge Gap**: Passable gap at column 26 (rows 41-43) connecting the southern corridor (rows 44-49) north into the western corridor (empirical routing from south).
- **South Sand Highway Boundary**: Row 39 hedge line and dense pine trees (columns 31-35, rows 36-39) border the southern Sand Highway; column 36 gap at (36, 39) dead-ends at pine tree (36, 42).
- **Southern Bypass**: Open path around the central pine tree (10-11, 44-46) and Signboard 1 (10-11, 47) connecting rows 46 and 48-49 west onto the cobblestone road (rows 45-46) into Lancio Town. Note: pine tree at (5-6, 48-50) blocks stepping south from (5, 48) to (5, 49) (verified Turn 27479).
- **Decorative Red Rock (35, 7)**: Located in the northern meadow where the 'Lost Pidgey' was found. Confirmed solid decorative obstacle with zero 'A' interaction.
- **Passable Low Hedge Tiles**: Low hedge/bush tiles at (33, 11), (30, 13), and (26, 15) are confirmed fully walkable terrain on foot.
- **Row 11 Traversal & Meadow Entrance**: Row 11 does not connect westward across column 40 due to a solid pine tree at (39, 11). Access to the Northern Hedge Corridor (row 11) from the east requires entering the northern red rock meadow at (34, 10).

## Overworld NPCs & Trainers
- **NPC 1 (Camper/Straw Hat)**: Wanders around (16-18, 43-45) near Signboard 2. Verified post-tremor (Turn 27456, 3 boxes): "Haha!" / "Wild Pokémon can't attack me! I have many repels..." / "I have many repels... They keep wild Pokémon away.".
- **NPC 2 (Boy in Grass)**: Wanders near Central Pine Tree at (10-12, 48-50). Verified post-tremor (Turn 27457, 2 boxes): "I gotta be careful when I walk around in the tall grass..." / "Wild Pokémon can jump out and attack you!".
- **NPC 3 (Science Guy / Pink Vest Guy)**: Wanders in eastern clearing at (39-41, 35-37) (`latest_grid.png` Turn 27447 confirms single NPC in this clearing, consolidating former duplicate NPC 8 entry). Verified post-tremor (Turn 27453, 2 boxes): "The power of science is incredible!" / "Erm... why is it that astonishing now?".
- **NPC 4 (Youngster Mike)**: Located at (29, 20) in northwest clearing. Team: Rattata Lv5. Defeated. Post-defeat dialogue: "My Pokémon was completely destroyed by yours..." (verified post-tremor Turn 26681).
- **NPC 5 (Lass Sonia)**: Located at (27, 15) on rock spire. Team: Cherubi Lv5. Defeated. Post-defeat dialogue: "Hmm, more harmony maybe?" (verified post-tremor Turn 26680).
- **NPC 6 (Bug Catcher Duke)**: Located at (45, 12) in northeast meadow. Team: Burmy Lv6. Defeated. Post-defeat dialogue: "You really must be something to be able to counter my defense..." (verified post-tremor Turn 26646).
- **NPC 7 (Blue Cap Boy & Pidgey)**: Located at (34, 37) on Sand Highway with Pidgey at (33, 37). Owner of the lost Pidgey (Quest Completed). Verified post-tremor (Turn 27446): Boy displays "Thank you so much for finding my precious Pidgey." and Pidgey displays "Pidgey: Pi Pi!".

## Wild Encounters
- Wooper (Lv3), Starly (Lv3), Nidoran♀ (Lv3), Nidoran♂ (Lv2), Pidgey (Lv2), Mareep (Lv3), Weedle (Lv2), Bidoof (Lv2), Caterpie (Lv2), Rattata (Lv3), Pichu (Lv3), Cleffa (Lv4).

<hr>

<h1><code>Locations/Route_2</code></h1>

# Route 2

## Geography & Connections
- **North**: Connects to Sovio City (`columns 60-63, row 40`) at `columns 6-9, row 0` (verified Turn 27589).
- **East / Southeast**: Leads toward **Azluf Town**, where Professor Ivo is waiting to meet Asher (per Dad's briefing in Turn 27559).
## Wild Pokémon Encounters
- **Starly**: Encountered at Lv6 (♂) in the northern tall grass at `(12, 10)` (verified Turn 27592) and Lv4 (♂) in the southern clearing at `(64, 48)` (verified Turn 27894).
- **Gligar**: Encountered at Lv4 (♀, Ground/Flying) in the eastern corridor tall grass at `(55, 29)` (verified Turn 27898).
- **Pikipek**: Encountered at Lv3 (♂, Normal/Flying) in the eastern corridor tall grass at `(51, 27)` (verified Turn 27918).
- **Grubbin**: Encountered at Lv4 (♂, Bug) in the northern entrance clearing tall grass at `(11, 9)` (verified Turn 28037).
- **Shinx**: Encountered at Lv3 (♀, Electric) in the eastern corridor tall grass at `(53, 26)` (verified Turn 28052).
- **Budew**: Encountered at Lv5 (♂, Grass/Poison) in the eastern corridor tall grass at `(54, 26)` (verified Turn 28061).

## Landmarks & NPCs
- **Northern Entrance Clearing (`cols 6-15, rows 0-12`)** (`latest_grid.png` Turns 27590-27591):
  - Tall grass patch spans `cols 6-15, rows 6-12`.
  - Wooden signboard at `(12-13, 8)` interacted from `(12, 9)` reads verbatim: *"Route 2 / Careful on the Bridges!"* (verified Turn 27591).
  - **Patrolling Beret Girl (`13-15, 9-12`)**: *"I wonder if I can find a Mime Jr. around here... I heard they are pretty rare."* (verified Turn 27952).
- **Southern Corridor (`cols 12-25, rows 13-25`)** (`latest_grid.png` Turns 27607, 27621-27622):
  - **Lass Karina** at `(15, 17)` facing East (`"Let's have a fun Pokémon battle!"`): Uses Pikachu (♂, Lv8) and Ducklett (♀, Lv8); awards `₽512` and states post-battle: *"That was pretty amazingly fun! You have totally exhausted me..."* (verified Turns 27609-27620).
  - Clear non-grass path runs south along `column 17` (`rows 20-24`) into a horizontal dirt/flower corridor along `row 24` (`cols 12-25`).
  - **Bug Catcher Elihaj** at `(20, 24)` (`"Bugs in my net, in my bag, everywhere!"`): Uses 3 Pokémon—Caterpie (♀, Lv7), Venipede (♀, Lv8), and Scatterbug (♂, Lv7); defeat quote: *"They were squashed like a fly!"*; awards `₽364`; post-battle overworld quote: *"You aren't a big fan of insects, are you?"* (verified Turns 27622-27635).
  - **Eastern Stairs & Plateau Entrance (`cols 25-34, rows 20-25`)**: At `(27, 24)`, a wooden staircase at `(28, 23-24)` ascends east onto a sandy plateau (`cols 29+`, where a male NPC stands at `32, 21`). Stepping onto `(27, 24)` triggers a battle with **Picnicker Paul** stationed at `(27, 22)` (*"I just hatched my Pokémon in the Day-Care! Let me show you them!"*): Uses 2 Pokémon—Budew (♂, Lv8) and Swablu (♀, Lv8); defeat quote: *"My babies!"*; awards `₽320` (verified Turns 27635-27645).
- **Pokémon Day-Care Plateau (`cols 29-42, rows 17-25`)**:
  - **Grubbin Breeder** wandering at `(31-32, 20-21)`: *"I'm trying to breed the best Grubbin possible! I hatched so many eggs already..."* (verified Turns 27649-27651).
  - **Pokémon Day-Care Signboard** at `(36, 21)`: Reads *"Pokémon Day-Care"* (verified Turn 27651).
  - **Pokémon Day-Care Entrance** at `(38, 20)` (red-roofed cottage topped with giant Pokémon Eggs):
    - **Interior (`7, 11` exit mat)**: Contains Day-Care Lady at `(7, 7)`, PC terminal at `(10, 8)`, and a male Scientist at `(4, 10)` (*"I'm researching Pokémon Eggs, but no luck so far..."*, verified Turns 27685-27687).
  - **Quest NPC ("Egg Research", Quest #3)** at `(40, 21)` directly outside the Day-Care: Female scientist in glasses and lab coat with purple quest bubble. Asks: *"Oh hey! You're a Pokémon Trainer, right? I need your help... You know those rocks that make Happinies evolve? Could you find one for me?"* Accepted in Turn 27680. Gives post-accept hint: *"I heard you can catch Happinies here... They are rare, but they're said to keep those eggs with themselves from time to time. Maybe by catching one, you could get that egg easily..."* (verified Turns 27680-27683).
  - **Northern Staircase & Day-Care Yard (`cols 30-41, rows 12-18`)**: Stone staircase at `(31-33, 17-18)` ascends north from the Day-Care plateau to a small terrace (`cols 30-34, rows 13-16`; bounded on the north by a cliff at `row 12`). At `(35, 15)`, the **Day-Care Man** stands at the gap of the fenced Day-Care yard (`cols 35-41, rows 12-16`), which contains an overworld **Eevee** (`38, 13`) and **Togepi** (`39, 15`) (verified Turns 27689-27691).
  - **Rival Battle with Valora (`37, 22`)**: Stepping onto `(37, 22)` in front of the Pokémon Day-Care triggers a cutscene where **Valora** steps out beside Asher (`38, 22`), admires the Day-Care, and challenges Asher to a 4-Pokémon rival battle to stay sharp for the Eclipse Tournament (verified Turns 27652-27678):
    - **Pokémon 1**: Cleffa (♂, Lv7; Fairy-type; knows Encore, Metronome).
    - **Pokémon 2**: Ralts (♀, Lv8; Psychic/Fairy-type; knows Double Team, Growl).
    - **Pokémon 3**: Mareep (♀, Lv8; pink wool sprite; Electric-type; knows Growl, Tackle).
    - **Pokémon 4**: Popplio (♂, Lv9; Water-type starter ace; knows Water Gun).
    - **Outcome & Post-Battle**: Defeat quote: *"Oh my... I didn't have a chance."*; awards `₽1008`. Post-battle, Asher tells her *"It was a nice battle, but you gotta try harder than that."* Valora replies: *"I knoooow, I'll train more so when Round One comes, I'll be ready to advance through! I'll go ahead now, see ya in Azluf!"* and departs southeast along the pink sand path toward Azluf Town.
- **Central Ridge & Overhead Bridge Underpass (`cols 46-50, rows 24-38`)**:
  - Wooden stairs at `(46, 26)` (with railings at `46, 25` and `46, 27`) ascend east from the Day-Care path onto a rocky ridge (`cols 47-49`).
  - A second set of wooden stairs at `(50, 25)` (with railings at `50, 24` and `50, 26`) descends east from the ridge into the eastern tall grass corridor (`cols 51+`).
  - Walking south along `column 49` (`rows 25-33`) passes east of a boulder (`47-48, 28-29`) and **underneath** the northern overhead wooden bridge (`rows 30-32`) onto a southern ridge overlook (`48-49, 33-35`), which is closed off on the south by solid rock cones at `(48, 36)` and `(49, 34-35)` (`latest_grid.png` Turn 28598, verified Turn 28599; the lower ridge and staircase at `48-49, 39-45` on the southeastern shore of the Slowpoke pond are Surf-gated across the pond).
  - **Hidden Item (`48, 35` facing `48, 36`)**: Interacting with the small rock/stone at `(48, 36)` from `(48, 35)` on the southern ridge overlook yields **Revive x1** (collected Turn 27705).
- **Eastern Tall Grass Corridor (`cols 51-55, rows 24-35`)**:
  - **Black Belt Cameron** rotating at `(53, 30)` (`"Punch, kick, jab!"`): Uses 2 Pokémon—Machop (♂, Lv9) and Mankey (♀, Lv10); defeat quote: *"Ah man..."*; awards `₽720`; post-battle overworld quote: *"A martial artist beaten by a kid... Doesn't sound too cool."* (verified Turns 27707-27716).
  - **Northern Overhead Wooden Bridge & Western Underpass (`cols 36-50, rows 29-38`)**:
    - Overhead wooden bridge spans `cols 37-50, rows 30-32` (`latest_grid.png` Turns 27701, 27704).
    - **Upper Bridge Deck (`cols 37-50, rows 30-32`, entered from `51, 30-32`)**: Connects west to an elevated ledge (`35-36, 28-32`) holding a golden item sphere at `(35, 28)` yielding **Silk Scarf x1** (collected Turn 28397).
      - **Hiker Frank (`42, 30`, facing South)**:
        - **Pre-Battle Quote**: *"Don't you think these bridges are kind of unsafe? Though not more dangerous than me in a Pokémon battle!"*
        - **Team (2 Pokémon)**: Roggenrola (♀, Lv10; Rock) and Diglett (♂, Lv11; Ground; knows Sand Attack).
        - **Outcome**: Defeat quote: *"Jeez..."*; awards `₽440` (verified Turns 28390-28394).
    - **Lower Ground Underpass (`cols 40-46, rows 29-38`)**: Passing south under the bridge at `(43-45, 30-32)` leads to **Youngster Darrin** at `(43, 33)` facing East (`"Ay, nah ah bro, you can't pass here!"`; uses 2 Pokémon—Shroomish ♂ Lv9 with Stun Spore and Zigzagoon ♂ Lv9; defeat quote: *"Wow bro, for real?"*; awards `₽468`; post-battle overworld quote: *"Alright man you can pass... I allow it."*; verified Turns 27925-27935), **Fisherman Colton** at `(42, 36)` facing South (`"Where are all the fish? Well, I'll battle you instead of them I guess..."`; uses 1 Pokémon—Horsea ♂ Lv11; defeat quote: *"Noooo!"*; awards `₽396`; post-battle overworld quote: *"I should have been more patient and wait for my fish to hook..."*; verified Turns 27936-27941), and a pond at `(41-46, 37-42)` with a swimming Slowpoke at `(42, 37)`.
    - **Southwestern Grove (`cols 33-52, rows 38-59`)** (`latest_grid.png` Turns 28545, 28547, 28548 & 28549):
      - Walking west past Fisherman Colton (`42, 36`) to `col 39-40` (`40, 35 -> 40, 38 -> 39, 38 -> 39, 41 -> 40, 41`) bypasses the western shore of the Slowpoke pond and ascends a wooden staircase at `(39-41, 43)` into the Southwestern Grove (`cols 33-47, rows 44-59`).
      - **Bug Catcher Nicolas (`36, 47` -> `38, 47`, facing East)**:
        - **Pre-Battle Quote**: *"Hope you got some repels, because my bugs are too much!"*
        - **Team (2 Pokémon)**: Wurmple (♂, Lv9; Bug; knows String Shot) and Yanma (♂, Lv10; Bug/Flying; Ability: Speed Boost; knows Quick Attack and Double Team).
        - **Outcome**: Defeat quote: *"Even my Yanma?!"*; awards `₽520` (verified Turns 28550-28556; Sirius reached Lv26).
      - South of Bug Catcher Nicolas along `col 37` (`37, 46 -> 37, 56`), a horizontal gap at `(38-41, 53)` leads into a closed tall-grass pocket (`41-44, 46-52`, bounded on the east by a cliff wall at `col 45`, verified via `latest_grid.png` Turn 28559), while a one-way ledge spans `(36-38, 57)` above **Explorer Ben** at `(39, 59)`.
      - **Explorer Ben (`39, 59` -> `38, 59`, facing West)**:
        - **Pre-Battle Quote**: *"Haha, you used the shortcut too, now you must battle me!"*
        - **Team (3 Pokémon)**:
          - **Pokémon 1**: Sandshrew (♀, Lv9; Ground; knows Sand Attack).
          - **Pokémon 2**: Skorupi (♀, Lv9; Poison/Bug; knows Poison Sting).
          - **Pokémon 3**: Dwebble (♀, Lv9; Bug/Rock; knows Withdraw).
        - **Outcome**: Defeat quote: *"Why you..."*; awards `₽432` (verified Turns 28561-28576).
      - South of Explorer Ben (`37-39, 59`), a flower-lined path winds south and east around tall grass patches (`37, 59 -> 39, 60 -> 39, 63 -> 46, 63 -> 46, 61 -> 48, 61 -> 48, 58 -> 52, 58`, with inert rock cones at `43, 62` and `47, 56`, verified Turns 28578-28581).
      - **Picnicker Alice (`53, 58`, facing South)**:
        - **Pre-Battle Quote**: *"Don't you love this place? Its great for picknics."*
        - **Team (1 Pokémon)**: Pansage (♂, Lv11; Grass).
        - **Outcome**: Defeat quote: *"..."*; awards `₽440` (verified Turns 28581-28585).
      - **Northern Pocket & Hidden Green Shard (`46, 52`)**: Walking north from `(48, 58)` through the 4-tile tall-grass strip (`48, 58 -> 48, 54`) reaches a small northern pocket (`46-48, 52-54`) bounded by cliff walls (`46-48, 50-51`); interacting with the bare grass tile at **`(46, 52)`** (from `46, 53` facing Up, west of the rock cone at `47, 52`) yields a hidden **Green Shard x1** into the Items Pocket (verified Turn 28589-28590).
      - **Southeastern Exit Staircase (`62, 61-63`)**: From Picnicker Alice (`53, 58`), the clear grass path continues east (`52, 59 -> 55, 59 -> 55, 60 -> 56, 60 -> 56, 62 -> 61, 62`, past an inert rock cone at `60, 60`, verified Turn 28587) to a wooden staircase at **`(62, 61-63)`** that ascends east onto `(63, 61-63)` in the Lower Clearing of Route 2 (verified Turns 28586-28587).
  - **Southbound Wooden Bridge & Eastern Plateau (`cols 53-70, rows 31-39`)**:
    - **Southbound Wooden Bridge**: Extends south from the eastern corridor at `(53-55, 36+)` (`latest_grid.png` Turn 27718). **Hiker Jerry** stands at `(55, 42)` facing West (`"Ahh a Trainer! Would you fancy a battle?"`): Uses 3 Pokémon—Geodude (♀, Lv9; Sturdy, Rock Polish), Geodude (♂, Lv9; Sturdy, Rock Polish), and Machop (♂, Lv9; Bide); defeat quote: *"Oh no..."*; awards `₽360`; post-battle overworld quote: *"I guess I'll return to hiking and exploring the place!"* (verified Turns 27723-27740).
    - **Lower Southeastern Ledge (`cols 58-62, rows 37-39`)**: Reached via stone staircase at `(59-61, 39-42)`; contains an orange item sphere at `(60, 37)` yielding **Max Repel x1** (collected Turn 27744).
    - **Eastern Plateau (`cols 58-70, rows 31-38`)**: Reached via wooden stairs at `(58, 33-34)`. At `(64, 34-36)`, two dark rugged rocks at `(65, 35)` and `(64, 36)` sit between the cliff (`63, 35-36`) and pine tree (`66-67, 32-34`), blocking the path to the eastern pond (`70+, 36-38`).
    - **Southern Bridge Plateau & Staircases (`cols 52-63, rows 47-55`)**: The southbound wooden bridge terminates at `(53-55, 47)` on a rocky plateau (`cols 52-60, rows 48-55`). Wooden stairs at `(60, 50-51)` descend east to a middle terrace (`cols 61-62, rows 48-52`), and a second set of wooden stairs at `(63, 51-52)` descends east into the lower clearing (`cols 64+`, verified Turns 27741-27742).
    - **Lower Clearing (`cols 64-71, rows 46-56`)**: Contains **Psychic Edvin** (Youngster sprite) rotating at `(68, 52)` (`"Heya dude, do you want to battle?"`; uses 1 Pokémon—Spearow ♀, Lv11; defeat quote: *"Crap..."*; awards `₽396`; verified Turns 27753-27756) surrounded by tall grass; column 64 (`rows 46-52`) connects north around the one-way ledge (`56-62, 47`) to the underpass and southeastern staircase (verified Turn 27743). Clear path along `row 53` (`cols 70-76`) leads east below three pine trees to a stone staircase descending south at `(74-76, 55-56)` onto a pink sand path.
    - **Hiker Franklin & Cracked Cliff Wall (`57, 45`)**: Stands in front of a vertical cracked cliff wall (`57, 43-44`) north of the one-way ledge (`56-62, 47`) (`"Haha, can't climb back on that ledge huh?"`); uses 1 Pokémon—Rockruff (♀, Lv11); awards `₽440`; post-battle overworld quote: *"Just go ahead..."* (verified Turns 27745-27751).
- **Southeastern Exit & Lucas Rival Encounter (`75, 56`)**:
  - Stone staircase at `(74-76, 55-56)` descends south onto a pink sand path leading directly to the Azluf Town signboard (`78-79, 58`, interacted from `78, 59`: *"Azluf Town / ---->"*, verified Turn 27779) and purple brick road (`77-84+, 58-59`).
  - Stepping onto `(75, 56)` triggers a cutscene where **Lucas** (from Sinnoh, previously seen registering at the Amor City Battle Centre) approaches at `(75, 54)`, introduces himself (*"Anyways, the name's Lucas, I'm from Sinnoh and I came here to win!"*), and challenges Asher to a friendly 4-Pokémon battle (*"Oh, I know! How about a battle? No stakes, just to see who's the stronger as of now."*):
    - **Pokémon 1**: Starly (♂, Lv10; Normal/Flying).
    - **Pokémon 2**: Porygon (Lv11; Normal).
    - **Pokémon 3**: Eevee (♂, Lv11; Normal).
    - **Pokémon 4**: Chimchar (♂, Lv12; Fire-type Sinnoh starter ace; knows Taunt).
    - **Outcome & Post-Battle**: Defeat quote: *"Wow, you are actually experienced! Nice!"*; awards `₽1344`. Post-battle, Lucas says: *"Haha, nice, it was a great battle for sure. I really gotta train myself up if I wanna breeze through. Well, see you later in the tournament!"* and departs east along the purple brick road into Azluf Town (verified Turns 27758-27773).
- **Closed-Off Northern Enclave (`cols 35-45, rows 8-16`)** (`latest_grid.png` Turns 28098, 28100, 28379 & 28484):
  - Accessible ONLY from exterior **Mt. Gerhana** (`2, 6` cave entrance with signboard at `4, 7`: *"Route 2 / A hidden path"*), emerging at `(38, 9)` below the cave mouth at `(38, 8)`.
  - Enclosed on the south by the Pokémon Day-Care fence (`35-41, 12-16`), pine tree (`41-42, 17-18`), boulder (`43-44, 15-16`), and cliffs (`45+, 15-18`).
  - Contains an inert pale flower patch at `(39, 11)`, an inert blue flower patch at `(40, 10)`, and a sunken rocky basin at `(42-45, 11-13)` (entered via northern stone stairs at `43-44, 10` from `43-44, 9`, with a walkable low southern rim at `43-44, 14` leading onto the southern grass strip `42-45, 14-15`).
  - **Cure Flower (`45, 14`) — Quest #4 ("Medic!")**: When **Quest #4 ("Medic!")** is active, an orange item sphere spawns at **`(45, 14)`** on the southern grass strip below the sunken basin; interacting with `(45, 14)` from `(44, 14)` yields the **Cure Flower** into the Key Items Pocket (verified Turn 28485).

<hr>

<h1><code>Locations/Sovio_City</code></h1>

# Sovio City

## Geography & Connections

- **South**: Connects to Route 1 at columns 14-15, row 40-41; transitions directly to Route 1 at (53, 0) without any story barrier text.

  - **Southern Avenue Bounds**: At (15, 30), the avenue transitions from the stone curb of rows 28-29 onto an open grassy lawn flanked by pine trees. Eastward traversal into row 30 is completely blocked by solid pine trees starting at column 18. The avenue continues south along columns 14-15 between dense pine tree borders directly toward Route 1 (row 40-41).

- **East / Southeast (Route 2 Connection)**: From Central Plaza, the eastern boulevard runs east across `columns 52-65, rows 19-20` (manholes at `55, 19` and `59, 22`, street lamps at `60, 22-23` and `63, 19-21`, trash can at `63, 23`), then curves south along `columns 60-63` (`rows 20-40`) through a flower-lined grassy avenue (`rows 31-40`) that transitions directly onto **Route 2** at `(6-9, 0)` (verified Turns 27586-27589).

## Exploration & Landmarks

- **Street Lamps**: Located at (14, 27), (14, 24), (16, 23), (35, 19), (46, 17), and (35, 23).

- **Park East Border & Fountain Perimeter**: Street lamps at (43, 19) and (43, 21). Stone receptacle at (43, 20) between lamps audited facing west from (44, 20); confirmed inert with zero text or hidden items. The open east-west boulevard runs north along rows 14-15. The park features a clover-shaped pond with brown shoreline and water surrounded by grass within the stone curb. Northern stone curb at (41, 16) steps south onto grass at (41, 17). Water shoreline begins at row 18 (solid collision from 41, 17). Grass contains white flower patches (northwest) and blue flower patches (northeast).

- **Three Bikers (Non-hostile NPC gang)**: Positioned at column 13, rows 21-23, facing east on motorbikes. Bikers 1 (13, 21), 2 (13, 22), and 3 (13, 23) provide an identical 3-box sequence (verified Turns 27370-27371): Box 1: '"vroom" "vroom" / Jealous kid?', Box 2: 'We are the big guys here, the ultimate motorcycle gang!', Box 3 (Asher's internal thought): '... / what a weird gang...'.
  - **Rear Biker Lane (Column 12)**: Column 12 is a completely open, 1-tile wide paved lane behind the Bikers connecting West Avenue (row 20) continuously south to row 30 (southwest lawn). Tile (11, 20) is solid modern office building foundation wall.

- **Southwest Building**: Structure at (18-21, 26-29) with decorative wooden siding and shutters. Barrels block the shutters at (19-21, 28-29) and solid elevation curb at (18, 28-29) blocks access with zero interaction; confirmed decorative exterior.
  - **West Facade & Sidewalk Bounds**: Sidewalk at (16-17, 26-27) is walkable. Facing East into (18, 26) and (18, 27) confirms solid wall with decorative blue windows and zero interaction. Southern Avenue street lamp at (14, 24) and base at (14, 25) block westward access from (15, 25).

- **Sewer Manholes**: Located at (13, 28), (13, 19), (29, 16), (34, 15), (40, 13), (54, 19), and (54, 21). Empirically verified at (13, 28), (13, 19), (29, 16), (34, 15), and (40, 13) completely inert to 'A' interaction with zero text or warps; purely decorative road fixtures.

- **West Avenue**: Paved road at row 18 heading west from Central Plaza. Boy NPC at (23, 17) (verified Turn 27373, 2 boxes: "This is my partner, Rocky! He's the best..." / "Rocky: ...") with his partner Pokémon Rocky at (24, 17) (verified Turn 27373, Asher's internal thought: "It's just a normal rock...").

- **West Avenue Signpost & Trash Can**: Wooden signpost at (15, 18) reads "Trainer Tips! If your Pokémon gets poisoned, it will take damage during battles. However, it won't when you walk around". Trash can at (14, 19) audited facing North from (14, 20) (Turn 27371); confirmed 100% inert with zero text or items.

- **West Avenue Boundary**: Cobblestone lane along rows 16-20 terminates west at column 11 into a solid modern office building wall. The eastern facade of the office building at column 11 across rows 16-20 is a continuous solid wall with no doors or entrances. Corner tile (12, 15) is solid foundation wall of the Karate house.

- **West Avenue North Boundary**: Solid commercial building facade extends across columns 16-26 with blue windows and brown shutters beneath a large screen/billboard. Shutters at (24-25, 16) above Rocky (24, 17) and the entire western facade across columns 16-22 (row 16, inspected facing North from row 17 in Turn 27286) are confirmed solid decorative walls with zero interaction. Traversal west connects via row 17/18.
- **Inter-Building Gap**: Solid walls at (30, 14), (31, 13), and (32, 12) prevent passage between the Gumball house and the tan building.

- **Southwest Boundary**: The pine tree border at rows 29-31 terminates into a dead-end lawn at (12, 30) against the southern building wall; tile (11, 30) confirmed solid pine tree collision.

- **Central Plaza**: Located around (40-50, 10-18) containing the Pokémon Center, Metro Station entrance, and residential house.

- **Metro Plaza Signpost**: 2-tile wide wooden signpost at (50-51, 18) outside the Metro Station; solid collision at (50, 18) and (51, 18); reads "Sovio Metro Station / Route 2 ---->".

- **East Exit Story Barrier (52, 19-22)**: Prior to registering for the Eclipse Tournament at Amor City's Battle Centre, tiles (52, 19), (52, 20), (52, 21), and (52, 22) trigger the story barrier text ("I can't go yet... I have things to do!"). After registering in Amor City and returning via the Hupest Metro Line, the barrier at (52, 19-22) is permanently cleared (verified Turn 27585).

- **Building Above Metro Station (Plaza East)**: Two-story building directly above Metro portal at columns 47-51, rows 13-17 on an elevated wooden terrace accessible via row 15 curb at (47, 15). Features a teal door with entrance warp at (49, 14) (column 48 is left doorframe/knob). Leads into building interior.
  - **Interior 1F**: Entrance mat lands at (63-64, 35). Single-story residence (no 2F stairs). Granddaughter at (63, 33) ("Nana makes the best food! Weeeee!") and Nana at (62, 31) ("I'm cooking something for my dear grandkid..."). Fixtures along north wall (row 30): Stove at (63, 30) ("The stove is on... Something's boiling."), Refrigerator at (64, 30) ("Its a fridge... Seems be from the newest brand."), Television at (65, 30) ("The TV is off..."). Dining table at (65, 32).
  - **Terrace Exterior**: Terrace extends east to column 51 across rows 14-16. Modern high-rise building starts at column 52; solid wall at (52, 15) and (51, 14). Tile (51, 17) is blocked by solid signpost collision from row 16 terrace. Column 51, row 16 features a decorative sewer manhole on the terrace floor.

## Southeast Corridor & Central Park
- **Southwest Central Park Curb Boundary & Crossing**: Row 27 across columns 33-35 is a solid stone curb separating the south tan brick sidewalk from Central Park plaza, while column 36 across rows 25-29 is walkable and connects the south sidewalk north into Central Park plaza (verified Turn 27386).

- **South Sidewalk & Children's Gathering**: Paved corridor along rows 27-29 south of Central Park pond. Little Girl at (33, 28) ("Mom told me that she will evolve if she touches a Moon Stone... I must keep her away from them!"), Boy at (35, 28) ("Yeah Jigglypuff!"), and Jigglypuff at (34, 28) ("Jigglypuff: Puff Puff!") verified post-tremor (Turns 27375-27376). Street lamp at (28, 26-27) with trash can at (28, 28) (audited facing Left from 29, 28 in Turn 27376; confirmed 100% inert), plus two stacked trash cans at (22, 30-31) (audited facing Left from 23, 30-31 in Turn 27377; confirmed 100% inert).

- **Central Park Boy in Pink Shirt**: Located at (33, 22) facing east. Verbatim dialogue: "I'm supposed to meet a girl here, but she doesn't seem to show up... Was I catfished?"
- **Central Park Blonde Girl**: Wandering pedestrian along the east pond walkway (43-45, 23-26). Verbatim dialogue: "I'm supposed to meet someone here, but he doesn't seem to show up... Was I catfished?"

- **Eastern Boundary**: Row 27 terminates at column 46 into a solid building wall.

- **Central Park South Border & East Walkway**: The western curb past the pine hedges at column 42 leads into a dead-end hedge alcove at (42, 30). Columns 44-45 form a paved walkway connecting row 19 south to row 26, terminated at row 27 by a stone curb and dense bushes with a decorative sewer manhole at (42, 27). The two-story building facade at column 46 is solid wall across rows 24-29. 

- **Two-Story Commercial/Residential Building (Columns 47-51, Rows 20-31)**: Large structure south of Central Plaza. Upper story has modern grey roof and large dark windows. Lower story (rows 28-31) features brown wooden siding, blue windowpanes, and decorative wooden shutters.

  - **Upper Roof Perimeter & Collision**:
    - Covered corridor confirmed beneath the northern roof section! Spans rows 20-22 across columns 47 to 51. Entrances/exits: north at (48, 19-20) and (51, 19-20); west onto sidewalk at (46-47, 21), and west balcony peek at (47, 22). Row 23 is solid wall across all columns. Eastern boundary at (51, 22) borders Route 2 barrier at (52, 22). Exhaustively audited all 15 tiles (cols 47-51, rows 20-22) and perimeter walls in Turns 27213-27216; confirmed 100% inert with zero hidden doors, NPCs, or items.

  - **Southern Facade & Perimeter Collision**:

    - Tan brick sidewalk runs south of Central Park pond to columns 44-46 across rows 28-30.
    - Facade at (47-51, 30-31) features decorative wooden shutters flanked by blue windows; non-enterable decorative scenery.
    - Dense pine hedges border the south at row 31 (columns 41-45), and row 32 is solid tree/hedge border.

## Pokémon Center

- **Exterior Entrance**: Blue glass door at (44, 12) (column 45 is solid wall).

- **West Wall**: Solid exterior wall forms the western boundary of the Pokémon Center at column 40.

- **Interior Layout & Audit**:

  - Exit mat at (7, 8).

  - Main Nurse Joy counter straight north along column 7: Nurse Joy stands at (7, 2) behind the solid counter at (7, 3); interaction occurs facing North from (7, 4). Restores party to full health and registers official Sovio City respawn checkpoint.

  - Large decorative teal Poké Ball floor motif at columns 6-8, rows 5-6.

  - Straw-hat Camper at (5, 7): Ambient humor dialogue ('My weedle got poisoned so I will need the Pokémon Center\'s... Ironic isn\'t it?').

  - Resident Boy at (8, 6/4): Explains PC terminal ('Please feel free to use that PC in the corner. / The receptionist told me so. It's so kind of her!').

  - **Corner PC Terminal at (12, 1) & East Pillar Routing**: Fully interactive! Interacting facing Up from (12, 1) displays "Asher booted up the PC." and opens the PC menu system (Someone's PC Box 1, Asher's PC Item Storage, and Mailbox all verified empty; no Professor's PC option). Direct northward movement along column 12 is blocked by the eastern architectural pillar at (11-12, 3-6) (stopping at 12, 7); reaching (12, 1) requires stepping right to the column 13 aisle at (13, 7), walking north to (13, 1), and stepping left to (12, 1).

  - **Framed Town Map at (11, 0)**: Interacting facing Up from (11, 1) displays "A Town Map." and opens the full interactive regional Town Map interface (D-pad moves cursor to inspect towns and routes, B exits).

  - **Upper Mezzanine & PokéMart**: Reached via the blue-carpeted staircase/escalator in the northwest corner at (2, 1), which warps to an escalator at (5, 8) ascending north to the upper mezzanine floor. The ground floor pillar occupies columns 2-4 across rows 3-6; access to the escalator requires navigating around the camper (5, 7) via the southern aisle along row 8 (columns 2-6), then walking north along the column 1 corridor (rows 2-7) and stepping east into (2, 1). A PokéMart counter on the mezzanine is staffed by a clerk at (5, 3) facing south across the counter at (5, 4).

    - **Verified Shop Inventory**:

      - Poké Ball: $200

      - Potion: $300

      - Antidote: $100

      - Paralyz Heal: $200

      - Repel: $350

    - **Fixtures & Bounds**: Blue wall terminal/display at (6, 3) east of clerk (inert). Counter structure spans columns 3 to 6 across rows 3-4, completely enclosing clerk with no rear access. Escalator descends south at (5, 6-8) between red handrails. East flank: tile (7, 5) is walkable, (7, 4) solid collision. West flank: tiles (2, 3), (2, 4), (2, 5) walkable; north window wall at (2, 2) and counter side wall at (3, 3) solid collision.

## Sovio Metro Station

- **Entrance**: Blue subway portal with 'M' logo at (48, 17) in Central Plaza; entered from south at row 18.

- **Interior Layout**:

  - Main lobby floor lands at (23, 24) on vertical red mat. Stairs leading back up to Sovio City overworld at (24, 24); entered from (23, 24) stepping Right (tile 24, 25 is blocked by south railing).

  - **Train Timetable Board**: Located on north wall spanning columns 21-23 at row 23. Interacting facing Up from (21, 24), (22, 24), or (23, 24) displays verbatim: "It's a timetable showing various destinations!". Confirmed 100% decorative flavor text across all columns with zero story triggers.

  - **Turnstile Gate**: Scanner pillars at (18, 21) and (20, 21) are decorative pillars with zero interaction text. Passage at (19, 21). Prior to completing the Frio confrontation in the Southern Dark Sector (32, 38), stepping onto (19, 21) triggers 'I should find dad first!' and forces Asher 1 step Down to (19, 22). After completing the Frio confrontation, stepping through (19, 21) onto (19, 20) transitions into the reunion with Dad (18, 18) and Valora (19, 19), who lead Asher north onto the train platform to board the train to Amor City at (21, 9) (verified Turns 27535-27538).
  - **Platform Fixtures**: Platform waiting area contains a yellow vending machine on north wall (19, 18), two empty blue chairs on northwest wall, and two blue chairs at northeast wall (21-22, 18-19) facing west where a Metro attendant / police officer in blue uniform and dark peaked cap is seated in the upper chair. North of the waiting area, a second turnstile gate leads onto the upper boarding platform where the train to Amor City stops at row 9 (door at 21, 9).

- **West Wing Seating & Boundary**: Three blue chairs at column 16 (rows 22, 23, 24) face east along the solid west brick wall (Asher stands at column 17 facing west). Inspected facing west; confirmed completely inert with zero hidden items or text.

- **Sovio Sewers Secret Entrance**: Red horizontal capsule mat against south wall at (18-19, 25). Stepping Down from (18, 25) off the mat warps directly into the **Sovio Sewers**!

## Residential House (North Central)

- **Entrance**: Teal door at (39, 7) north of Pokémon Center plaza.

- **Northern Alcove & Exterior Boundary**: Paved alleyway along column 40 runs north from (40, 15) past decorative sewer manhole at (40, 13) to (40, 9) in front of house (39, 7). The entire northern alcove is completely enclosed: west flank is bordered by the solid wall of the tan building (32-37, 8-12); east flank is bordered by the solid west wall and red roof of the Pokémon Center (41-46, 9-12); north flank terminates at the foundation and walls of house (39, 7) and background structure at rows 0-6. Verified zero rear alleyways, side passages, or exits behind the Pokémon Center or residential row.

- **Interior**: Entrance mat lands at (43, 36). 

- **Layout (1F)**: Dining table with tea mug, red mat at (45, 31) before stairs to 2F at (46, 31). Resident elderly man sitting at (41, 33) dialogue: "I bought my son a Wii... Not sure why he asked for one its an old thing but whatever."

- **Layout (2F)**: Resident boy at (44, 14) dialogue: "I love the games on the Wii! I'm playing my favorite right now." TV cabinet at (44-45, 11-12) displays verbatim: "There's a game running!" / "There's a blue hedgehog... with a sword?" (Sonic and the Black Knight Easter egg). White Wii console sits on floor at (45, 13). PC desk at (46, 11-12) is an inaccessible background fixture behind the Wii and bed.

## City Signpost

- **Location**: Wooden signpost at (29-30, 18); reads 'Sovio City / The city of Union'. Trash can at (31, 17) east of signpost audited facing Right from (30, 17) (Turn 27374); confirmed 100% inert with zero text or items.

## Residential House (Central West - Gumball Family)

- **Entrance**: Teal door at (29, 14) (note: column 28 is the wall/pillar).

- **Interior 1F**: Entrance mat at (23-24, 36). Resident boy at (25, 32) dialogue: "I love this show!". Mother at (27, 33). Wide-screen TV at (25-26, 30).

- **Interior 2F**: Stairs at (26, 12). Bed with sleeping figure at (27, 15-16); verified inert scenery/no active trigger from headboard (27, 14) or side (26, 15). Generic bookshelf at (22-23, 12) reads "It's crammed full of Pokémon books.", blue PC terminal at (20, 12) is inert.

## Residential House (Northwest - Machop Family)

- **Entrance**: Teal door at (14, 15) (column 13 is the left doorframe/knob; entrance warp is at 14, 15).

- **Interior 1F**: Entrance mat at (5, 36).

  - Karate trainer at (3, 34) (spoken to facing North from 3, 35 in Turns 27358-27359) verbatim dialogue: "We are having a debate over which fighting stlye is better... / My girlfriend says kickbox is far better than karate... / Which is total nonsense!". Blonde girlfriend at (3, 33) (spoken to facing Right from 2, 33 in Turn 27361) verbatim dialogue: "We are having a debate over which fighting stlye is better... / My boyfriend says karate is far better than kickboxing...".

  - Family Machop at (6-7, 33-35); permanently displays 'Machop: Chop Chop!' followed by 'He seems a bit agressive...'.

  - Wooden staircase at (8, 31-33) with red vertical mat at (7, 32) leading to 2F.

- **Interior 2F**: Stairs down to 1F at (7-8, 12) with red mat at (8, 12). North wall fixtures: Blue cabinet at (5, 11-12) displays verbatim: "Wow! Tons of Pokémon stuff!". Green bookshelf at (3-4, 11) displays verbatim: "It's crammed full of Pokémon books.". Study desk at (1-2, 11), bed at (2-3, 13-14).

## South Central Sector

- **Building at (23-28, 24-26)**: Two-story building between Name Rater and southwest building. Decorative wooden shutters at (24-25, 26) have solid collision with no warp or text. Sidewalk terminates west at column 22 against southwest building wall with solid collision.

- **Residential House (South Central - Name Rater)**: Located at (31, 26). Interior lands at (65, 17) on red exit mat. Resident: Official Name Rater at (64, 14) behind stool (64, 15) (verified post-tremor Turn 27378: "Hello, hello! I am the official Name Rater!"). North wall fixtures (verified Turn 27381): bookshelves at (64-65, 12) ("It's crammed full of Pokémon books.") and TV at (62, 12) ("The TV is off..."). Confirmed standard nickname rating service.

## North-Central Commercial/Residential Block

- **Building at (32-37, 8-12)**: Tan building with wooden siding between Pokémon Center and west avenue. Facade shutters at (34-35, 12) are decorative exterior with solid collision and no accessible entrance.

<hr>

<h1><code>Locations/Sovio_Sewers</code></h1>

# Sovio Sewers

## Overview & Connections
- **Entrance**: Secret stairway on the south wall of Sovio Metro Station lobby at (18-19, 25).
- **Landing (1F)**: Asher arrives at (37, 22) at the base of the wooden staircase.
- **Staircase Up**: Located at (38, 22) leading back up to Sovio Metro Station; south side has solid railing blocking direct Up entry from (38, 23); must be entered from the west at (37, 22) stepping Right.
- **Terrain & Features**:
  - Stone-rimmed shallow puddle on the upper landing at columns 32-35, rows 21-23 (fully walkable without Surf).
  - Column 27 Vertical Corridor: Fully walkable vertical corridor (rows 22-26) paved with circular cobblestones that cuts through the central brick structure, connecting the lower sewer walkway (row 27-28) north to row 19 (which leads west to the Repel ledge). Tile (28, 23) is an impassable 1x1 floor pit with zero interaction. Tile (29, 22) is confirmed solid wall collision, meaning there is no direct eastward passage across row 22 into the upper landing; traversal between column 27 and the upper landing requires navigating via the lower walkway (row 28) and the column 34 staircase.
  - Impassable central brick wall at columns 33-35, rows 16-20 directly north of the shallow puddle.
  - Stone stairway leading down to the lower sewer floor at column 34, row 24 (passable descent along column 34; column 35 blocked by railing post).
  - Item Found: Repel collected at (22, 20) on walkway north of the pool. Note: (22, 20) is a dead-end ledge separated from the western platform by a void chasm at columns 20-21.
  - Elevated Gangway (Northern Corridor):
    - Horizontal stone gangway along row 5 connecting column 15 across the chasm to column 23.
    - Western terminus at (14, 4-5) bordering void chasm at column 13 and row 6.
    - Shallow puddles at (15, 4) and (25, 5).
    - Northern wall is solid brick along row 4 (columns 16-22). Recessed alcove at (23, 4) ends at solid brick wall at row 3.
    - Eastern terminus at (25, 5) dead-ends at vertical void chasm at column 26.
    - Vertical bridge crossing south across the chasm is located at column 23 (rows 6-12).
  - Southwest Corridor & Obstruction: Vertical corridor at columns 6-7 (`latest_grid.png` Turn 27492 confirms walkable alcove at 4-8, 25-28 around puddle 7-9, 26-28, brick wall at 8, 23-24, and walkable tiles at 6-7, 23-24) is blocked to the north by two diagonal rugged rocks at (6, 23) and (7, 22) (interacting facing North from 6, 24 into 6, 23 displays verbatim: "It's a rugged rock, but with some equipment, I could smash it.", verified Turn 27492). Accessing this western corridor from the northeast along row 18 is similarly blocked at (10, 18) and (9, 17) by two diagonal rugged rocks between the row 16 brick wall and row 19 void chasm. Both approaches require smashing equipment.
  - Shallow Puddles (Southwest): Located at (7-8, 26-27) south of the column 7-8 corridor, and at (17-18, 27-28) east of the southern staircase.
  - Western Terrace Wall Ladder: Located at column 15, rows 6-10. A vertical climbable circular-ring ladder on the brick wall directly connects the upper western terrace at (15, 11) to the northern elevated gangway at (15, 5). Ladder tiles contain wild cave encounters.

- **Column 30 Causeway & Northeast Wooden Staircase**: Tile (30, 12) is open stone walkway on row 13. Directly north, column 30 is a fully walkable 1-tile stone causeway across rows 6-10 connecting to the upper platform. At the top, the Northeast Wooden Staircase structure spans columns 29-30 at rows 4-5, with an east-facing opening at (30, 4) entered by stepping Left from (31, 4), leading into the Dark Sector / Basement.

## Active Missions & Enemies
- **Team Siara Presence**: All grunts permanently retreated following Marie's radio directive; sewer corridors vacated.

## Topography & Connectivity
- **Lower Eastern Walkway**: Extends east from column 34 staircase along rows 27-28 to an eastern alcove at (38-39, 27-28) with a shallow puddle at (38-39, 27) (`latest_grid.png` & verified Turn 27500; note: column 34 staircase must be entered from the south at 34, 28 due to the side railing at 35, 27). Column 37 continues south from row 28 to row 32, then turns west along row 32 across columns 36-32 bordering the southern edge of the water basin, terminating at (32, 32) against the vertical green canal water chasm at columns 30-31 (verified Turn 27500).
- **Western Terrace Layout**:
  - Terrace floor extends across columns 12 to 17 on rows 11-12.
  - South perimeter has stairs descending at column 14 (rows 12-16) and solid stone railings at row 13 (columns 11-13 and 15-17).
  - East perimeter is bounded by solid stone wall/railing at column 18.
  - West perimeter: Terrace floor verified walkable west to column 12 (rows 11-12); column 11 (rows 11-12) is a solid stone wall bordering the void chasm at columns 8-10 (verified Turn 27406).
  - Ladder ascending to Northern Gangway (row 5) is located at column 15, rows 6-10.
  - Floor tiles contain wild encounters (e.g. wild Dunsparce Lv5).
- **Lower Level Connectivity**: The lower walkway connects directly to the western wing via row 28 at (24, 28) into the western corridor (columns 20-21) and the western platform.
- **Lower Western Corridor**: From (8, 28), row 27 is an open walkway running east to column 16. A vertical corridor at columns 17-18 leads north toward Grunt 2's platform at (18, 21-22) and the western stairs. Note: Column 16 is walkable at rows 25-26, and column 17 connects rows 22-24. Column 18 vertical corridor terminates north at row 18 at a solid brick wall (18, 17) before turning west along row 18 toward the stairs at (14, 17).
- **Upper Level Connectivity**: The stone stairway at column 34 (rows 24-27) connects the lower floor to the upper landing (1F). The upper landing terminates north into solid brick walls at row 20.
- **Southern Canal Corridor**: Descends via 1-tile stone staircase at column 13 (rows 28-31; column 12 is left railing) to rows 32-36. Western alcove extends to (8, 33-35) around shallow puddle at (9-11, 34-35), bounded by brick wall at (8-11, 30-32) and void chasm at column 7 and (8-11, 36) (`latest_grid.png` Turn 27490). Eastern walkway runs along row 36 beneath the stepped brick wall (19-22, 33-35) to eastern terminus at (22, 36) (Poison Barb location), where (23, 36) is blocked by the vertical green canal water chasm (verified Turn 27490).
- **Eastern Gangway, Bridge Landing & Column 30-31 Junction**: At the south end of the column 23 bridge is a 3x3 landing (22-24, 12-14) containing a 2x2 shallow puddle at (22-23, 13-14), bounded by void chasm at columns 20-21 and row 15 (`latest_grid.png` & swept Turn 27497). From column 24 at row 13, a single-tile wide horizontal stone gangway runs east along row 13 all the way to column 36 beneath a solid brick wall (rows 10-12). Note: Row 14 at columns 24-29 and 32-35 is impassable void chasm; traversal east/west must follow row 13. At columns 30-31 (`latest_grid.png` Turn 27415) is the causeway junction: column 30 leads north to the Northeast Wooden Staircase at (30, 4), while the southern 2-tile alcove at (30-31, 14) terminates at the void chasm at row 15 (tested and verified inert Turn 27495).
- **Eastern Storage Platform**: Located at eastern dead-end along rows 12-14, columns 36-38 (`latest_grid.png` Turn 27415 confirms brick wall at 31-38, 10-11, void chasm at 32-35, 14 and rows 15-17). 3x3 stone platform. Tile (37, 14) holds a red horizontal capsule mat with a downward arrow pointing South; pressing Down or A facing South at (37, 14) into (37, 15) is impassable and displays "Its a simple storage room..." (verified Turns 26919, 27414). All remaining perimeter tiles (36, 14; 38, 14; 38, 13; 38, 12; 37, 12; 36, 12) individually movement- and interaction-tested and verified 100% inert (Turn 27494). Visual grid inspection at Western Terrace (12, 11) (`latest_grid.png` Turn 27407) also reveals brick wall at (5-7, 12-14), stone walkway at (5, 15), and green canal water at (6-7, 15) west of chasm.

## Wild Encounters
- Koffing (Lv4-7, Poison)
- Grimer (Lv5-7, Poison)
- Purrloin (Lv4-7, Dark)
- Poochyena (Lv4-7, Dark)
- Klink (Lv4-7, Steel)
- Trubbish (Lv4-7, Poison)
- Stunky (Lv4, Poison/Dark)
- Honedge (Lv5, Steel/Ghost)
- Zubat (Lv5-6, Poison/Flying)
- Stunfisk (Lv5, Ground/Electric)
- Dunsparce (Lv5-6, Normal)
- Shuppet (Lv6, Ghost)
- Gastly (Lv5-7, Ghost/Poison)
- Croagunk (Lv5, Poison/Fighting)
- Mimikyu (Lv5, Ghost/Fairy)

## Sovio Sewers - Dark Sector / Basement
- **Access**: Reached via the column 30 wall ladder and entering the Northeast Wooden Staircase at (30, 4).
- **Environment**: Dark zone with circular spotlight illumination (Flash mechanic).
- **Staircase Up**: Located at (31, 9) leading back up to the sewer upper platform.
- **Layout & Spatial Geometry**:
  - Eastern corridor (cols 21-30): Northern stone wall at row 8, corridor along row 9 with stairs up at (31, 9) and stone stairs north to upper alcove at (23, 8). Rugged rock obstacle at (22, 10). Row 8 across columns 18-20 connects the eastern corridor (at 21, 9 -> 20, 8) to the western corridor (at 17, 8).
  - Western corridor & alcove (cols 13-17): Northern stone wall is at row 7. Row 8 is a walkable corridor connecting columns 13 to 17. Western boundary terminates at solid wall at column 12 (rows 8-9). Southern boundary at row 10.
  - Red capsule mat at (14-15, 9); stepping Down from (15, 9) warps to Deep Subterranean toy room (2, 38). Tile (16, 9) has solid obstacle collision; traversal between western alcove and eastern corridor connects via row 8 (Up from 15, 9 to 15, 8, then east along row 8 to 17, 8, and down to 17, 9).
- **Staircase North**: Stone staircase at (23, 8) ascends to an upper 3x3 treasure alcove (columns 22-24, rows 3-5). Verified 100% inert perimeter walls (north row 2 across cols 22-24, west col 21, east col 25). Single-purpose treasure room.
- **Southeastern Corridor & Southern Stone Staircase (25, 11-13)**: Row 10 is walkable cobblestone floor from `(32, 10)` west to `(23, 10)`. At `(25, 11-13)`, a 1-tile stone staircase (flanked by stone railings at cols 24 and 26) descends south to a lower Dark Sector floor at `(25, 14-15)`.
  - **Lower Southern Corridor & Frio's Chamber Warp (26, 23)**: From `(25, 14-15)` (bounded east by wall at col 26), the corridor runs west along rows 14-15 to `(21, 14-15)` (rugged rock at `21, 16`), then south along columns 21-23 across rows 16-23 (rugged rocks at `23, 20` and `21, 23`), and east along rows 22-23 across columns 23-28. At `(25-26, 23)` on the southern wall is a red capsule warp mat; stepping `Down` from `(26, 23)` warps into the **Southern Subterranean Chamber** at `(32, 38)`.
  - **Southern Subterranean Chamber (32, 38)**: Isolated chamber with red exit mat at `(32, 38)` and shallow puddle at `(31-33, 35-37)`. Stepping onto `(32, 37)` triggers the mandatory story cutscene with **Frio** (disguised in a Team Siara uniform at `32, 35`), who defeats Asher with his Eclipsing Gible and departs, prompting Asher: *"Ahh crap, I should rush back to Dad and Valora!"* (verified Turns 27521-27528).
- **Item Found (Dark Sector)**: Nugget collected at (23, 4) in the upper treasure alcove.
- **Rock Smash Obstacle**: Located at (22, 10) in the southern wall of the row 9 corridor; interacting displays verbatim: "It's a rugged rock, but with some equipment, I could smash it." Confirmed field obstacle clearance requires specialized player equipment rather than traditional HM moves.
  - **Alcove Perimeter Bounds**: Tile (21, 10) directly west of the rock is walkable floor. Tile (20, 10) is a solid corner wall. Row 11 across columns 20-22 is a solid south elevation wall, confirming the rock at (22, 10) sits in a 1-tile recess.
- **Deep Subterranean Sector**: Isolated 3x3 chamber (columns 1-3, rows 36-38). Arrives at (2, 38) on red capsule mat facing North. At (2, 37), retrieved Machop's Lost Toy. Perimeter walls (rows 35-38, columns 0-4) are solid walls. Single-purpose quest room.

<hr>

<h1><code>Lore/Hupest_Region</code></h1>

# Hupest Region Lore & Story Background

## Key Entities & Figures
- **Asher**: Protagonist. Raised as heir to the Siara Mafia to conquer the world; currently living with his father after his parents divorced; resolved to forge his own destiny.
- **Mother**: Current sole leader of the Siara Mafia; obsessed with a dangerous science project to achieve world domination.
- **Father (Jackson)**: Former co-leader of Siara Mafia (addressed as Jackson by Mrs. Ivo); opposed the science project due to its catastrophic danger; took Asher away and operates from the shadows to dismantle Siara.
- **Siara Mafia**: Hegemonic criminal syndicate in Hupest controlling politics and economy.
- **The Science Project**: Research capable of world domination; central cause of the parental rift and regional threat.

- **Mrs. Ivo**: Leading Pokémon Professor of the Hupest Region. Scientist with brown hair and pink glasses, wearing a white lab coat over a pink dress. Known Asher since his childhood (affectionately calls him "Ashi") and hasn't seen him in years.
- **Harry**: Father's friend and associate who operates the boat at Inizio Isle dock; addresses Asher as "young master". Providing passage to Lancio Town.
- **Valora**: Cyan-haired girl Asher rescued from Team Siara outside Sovio City Pokémon Center. Inspired by Asher, she is traveling to Amor City to qualify for the Eclipse Tournament and become stronger.

## Starting Setting
- **Inizio Isle**: Starting location where Asher and his father reside.

## Regional History & Events
- **300-Year Anniversary**: Commemorates 300 years of human-Pokémon coexistence in Hupest.
- **Eclipse Tournament**: Major international tournament organized in Hupest for the 300-year anniversary; open to trainers worldwide. Does not require traditional Gym Badges to qualify. Registration is open for 3 days; the championship starts 15 days later.

## Major Cities & Points of Interest
- **Amor City**: Capital city of the Hupest Region.
- **Amor Sports Center**: Facility in Amor City where trainers go to register/qualify for the Eclipse Tournament.
- **Lancio Town**: Town where Mrs. Ivo's Pokémon Lab is located.

## Key Items & Technology
- **HuPhone**: Multi-purpose regional device (gifted by Dad on departure morning); stored in Key Items pocket.
  - **Apps**: Item Storage (portable PC item storage), World Map (regional map viewer), Quest Log (active objective tracker).
- **Torn Scarf**: An old, scorched scarf found with Riolu by Professor Ivo when she discovered him. Held / worn by Sirius (Riolu) as part of his custom sprite/form.

## Asher & Riolu Flashback (5 Years Ago)
- **Origin of Riolu & Torn Scarf**: 5 years ago in a forest clearing, young Asher found an injured baby Riolu. Asher gave his own scarf to Riolu to bandage his injuries. Riolu kept the scarf for 5 years until Professor Ivo rescued him. When Professor Ivo returned the scarf to Asher, it triggered Asher's memory of their fateful first meeting.

## Mother's Return & Siara Syndicate Movements
- **Mother's Return**: Dad revealed that Asher's mother has returned with her syndicate (Siara Mafia) along with something Dad feared would return (the dangerous science project).

## Sovio City Confrontation
- **Confrontation**: In Sovio City central plaza outside the Pokémon Center, Dad confronted Mother, leader of the Siara Mafia, who was flanked by two grunts.
- **The Eclipse Project Unveiled**: Mother announced the completion of 'The Eclipse Project' as a test run diversion and summoned altered Eclipse Pidgey bearing a distinct dark aura and the Eclipse insignia.
- **Asher's Intervention**: When an altered Pidgey threatened a cyan-haired civilian (Valora), Asher stepped between them to defend her.
- **Aftermath**: The Siara Mafia withdrew; Dad praised Asher's courage, cautioned him about the Eclipse threat, and instructed him to meet at the Sovio Metro Station.

## Sovio Metro Departure to Amor City
- **Train to Amor City**: Dad met Asher inside the Sovio City Metro Station. The schedule board lists trains to Amor (16:00) and Alhia (20:00).
- **Dad's Reassurance**: When Asher asked about the Eclipse Pokémon and what happened with Mother outside the Pokémon Center, Dad reassured him: "I'm on it, so don't worry so much. But I can tell you on the way. Come on! Let's go!" Dad and Asher prepared to board the train to Amor City.

## Sovio Metro Tremor & Jackson's Disappearance
- **The Tremor**: While Asher, Dad, and Valora prepared to board the train to Amor City inside the Sovio Metro Station, a sudden seismic tremor violently shook the station.
- **Dad's Investigation**: Dad immediately ran outside into Sovio City to investigate the source of the tremor.
- **Sovio Sewers & Team Siara Presence**: Asher discovered a hidden entrance behind a red mat in the Metro lobby leading down into the Sovio Sewers. Team Siara grunts guarded a storage room awaiting Commander Marie. Asher confronted the grunts until Marie broadcast a general radio retreat order, after which the grunts vacated the sewers.

## Verified Regional World Map Topology
- **Inizio Isle**: Isolated green island node in the far southwest ocean; Asher's hometown.
- **Lancio Town**: Coastal green node on the southwest tip of the mainland. Connects northeast via Route 1 to Sovio City. Location of Professor Ivo's Lab.
- **Route 1**: Coastal route connecting Lancio Town to Sovio City.
- **Sovio City**: Red rectangular urban node (subtitle: "Metro Station"). Connects southwest via Route 1 to Lancio Town, and east via Route 2.
- **Route 2**: Coastal highway extending east from Sovio City to Azluf Town.
- **Azluf Town**: Coastal green town node located southeast of Sovio City along the southern shore.
- **Route 3**: Southern coastal highway connecting Azluf Town east to Samurion City.
- **Mt. Gerhana**: Mountain landmark and waypoint located between Sovio City and Samurion City along northern mountain route.
- **Samurion City**: Major port/industrial city on the south-central coast (red node with Poké Ball symbol). Connects west to Azluf Town via Route 3 and Mt. Gerhana, and north to Amor City via Route 4.
- **Route 4**: Dual railway transit corridor connecting Samurion City north to Amor City.
- **Amor City**: Giant blue central metropolitan hub of Hupest (subtitle: "Metro Station"). Regional capital and host city of the Eclipse Tournament / Amor Sports Center.
- **Route 16**: Eastern highway connecting Amor City east to Aurin Town.
- **Aurin Town**: Green town node located east of Amor City.
- **Western Island**: Large western archipelago connected via a sea bridge from a mainland red port city; contains a northern red city and a triangle of 3 green towns.
- **Cord Island**: Southeast offshore island containing 1 red town and 1 blue coastal port (verified via World Map).
## Interactive World Map Findings (HuPhone)
- **Divampa Cave**: Verified cave/mountain landmark in the central-south mountain sector between the southern routes and Amor City.
- **Mulberry Town & Route 9**: Verified town and route nodes on the western island archipelago.
- **Solare Island**: An isolated island node in the far northwest ocean connected via dashed sea route from the western island.

## Sovio Sewers Dark Sector & Confrontation with Frio
- **Frio ("Young Master" Disguised in Siara Uniform)**: In the Southern Dark Sector subterranean chamber (`32, 38`), Asher discovered a blonde trainer named **Frio** wearing a Team Siara grunt uniform standing in a puddle (`32, 35`).
- **The Artifact & Eclipsing**: Frio declared: *"Great... I finally found this too... Now its complete! With this... I can finally do it. Hehe, she will be so happy if it actually works... As she wanted."* When Asher mentioned standing up for a friend, Frio mocked friendship as weakness (*"There are no real friends... They drag you down, never respect you, and backstab you whenever it is benefical to them."*).
- **Frio's Eclipsed Gible**: Frio overwhelmed Asher in a scripted battle flash using a Gible undergoing **"Eclipsing"**. Before departing, Frio introduced himself (*"My name is Frio... Remember that name well, because you'll never win against me!"*), hinted at his Gible's transformation (*"For now settle with me only saying 'Eclipsing'..."*), and left Asher to rush back to Dad and Valora.

## Sovio Metro Platform Reunion & Train to Amor City
- **Reunion with Dad & Valora (19, 20)**: After confronting Frio in the Southern Dark Sector, Asher passed through the Sovio Metro Station turnstile onto `(19, 20)` where Dad (`18, 18`) and Valora (`19, 19`) were waiting. Asher reported encountering the "young master" Frio, his Eclipsing Gible, and Frio's claim of completing something.
- **Boarding the Train (21, 9)**: Dad promised: *"Alright, I'll tell you everything on the way... Okay? Its time for you to know the truth. Let's go."* Dad, Valora, and Asher walked north onto the train platform and boarded the train to Amor City at `(21, 9)`.
- **Train Journey & Siara Lab Flashback**: Inside the moving train car, Dad, Asher, and Valora took seats on the right side, and Dad recounted the truth in a flashback to the Siara research laboratory:
  - **The 300-Year Eclipse Anomaly**: Around 300 years ago in Hupest, a Lunar Eclipse followed by a Solar Eclipse caused an anomaly where Pokémon shifted and transformed, becoming violent and unstable.
  - **Eclipsing, Marie & The Device**: Jackson and Asher's mother—whose name is **Marie** (leader of the Siara Mafia)—scientifically replicated this phenomenon, calling it **"Eclipsing"**, using a chemical substance to trigger the shift. However, many Pokémon could not handle the substance, became uncontrollable, and endured terrible suffering. Marie insisted on continuing the project because they were close to creating **devices that can eclipse Pokémon and turn them back** without risk.
  - **Jackson's Departure & Arrival in Amor City**: Refusing to play god or endanger young Asher with Marie's delusions, Jackson walked out of the Siara laboratory and took Asher with him to keep him safe. Realizing that Marie carried on with the project and succeeded—and that Frio's device was the culmination of her research—Dad concluded his story just as the train arrived at **Amor City** (`18, 17`).

## Amor City Battle Centre & Eclipse Tournament Registration
- **Tournament Registration (10, 13)**: Inside Amor City's Battle Centre (where famous trainers including Lyra, Lucas, Dawn, Barry, Silver, Roark, Riley, Cheryl, Marley, and Buck also registered), Asher and Valora officially registered for the **Eclipse Tournament**. The Assistant explained that participants will be contacted via their phone numbers when it is time to show up for each active round.
- **Metro Pass & Professor Ivo's Summons to Azluf Town**: Dad gave Asher the **Metro Pass** (*"With this you can use the Hupest Metro Line, and travel around easily."*) and informed him that **Professor Ivo wants to meet Asher in Azluf Town** to discuss the events in Sovio City in person. Dad advised Asher to take the Metro back to Sovio City and advance east through **Route 2** to reach Azluf Town.
- **Valora Joins & Frio's Registration (10, 14)**: Valora asked to travel with Asher to Azluf Town (*"Travelling is always better with people you are close with you know."*). As they prepared to catch the Metro, **Frio** arrived to register for the Eclipse Tournament, mocking Asher as a weakling and insulting Valora before brushing past them to the counter (`10, 13`). Asher told Valora that Frio is the "young master" and suggested they head out.

## Route 2 Pokémon Day-Care & First Rival Battle with Valora
- **Rival Battle Outside the Day-Care (`37, 22`)**: Outside the Route 2 Pokémon Day-Care, Valora challenged Asher to a friendly 4-Pokémon rival battle (Cleffa Lv7, Ralts Lv8, Mareep Lv8, Popplio Lv9) to stay sharp for Round One of the Eclipse Tournament. After Asher defeated her, Valora promised to train harder for Round One and went ahead toward Azluf Town (*"I'll go ahead now, see ya in Azluf!"*).

## Route 2 / Azluf Town Border — Encounter with Lucas from Sinnoh
- **Lucas's Challenge (`75, 56`)**: At the stone stairs leading into Azluf Town (`75, 56`), **Lucas** from the Sinnoh region recognized Asher from the Amor City Battle Centre registration and challenged him to a friendly 4-Pokémon match (Starly Lv10, Porygon Lv11, Eevee Lv11, Chimchar Lv12) to test their current strength before the Eclipse Tournament. After Asher swept his team, Lucas praised Asher's battle experience, vowed to train harder to breeze through the tournament, and headed into Azluf Town (*"Well, see you later in the tournament!"*, verified Turns 27758-27773).

## Azluf Town — Professor Ivo's Confession, The Asteroid Truth & The Eclipse Band
- **Professor Ivo's Past with Jackson & Siara**: At the Lake Trio monument bench in Azluf Town, Professor Ivo revealed that she and Jackson were close college friends (Jackson studied economics while Ivo studied Pokémon biology). After Jackson met Marie and formed Siara, he asked Ivo to help develop **Eclipsing** since she was researching nocturnal and diurnal Pokémon behavior.
- **Jackson's Phone Call (10 Years Ago)**: In a flashback to 10 years ago (when Asher was 5), Jackson called Ivo after divorcing Marie and leaving Siara to protect Asher. Jackson asked Ivo to guide Asher on his journey once he grew older and instructed her to delete all research and data on Eclipsing so it wouldn't fall into the wrong hands.
- **True Origin of The Great Eclipse (300 Years Ago)**: Ivo explained that the public story of a Lunar/Solar Eclipse causing The Great Eclipse 300 years ago is only a myth. In reality, an extinction-sized **asteroid** approached the planet 300 years ago and mysteriously exploded in the atmosphere, scattering meteorite craters and fragments across Hupest. Those meteorite fragments contain the mineral/substance that initiates Eclipsing (the same mineral Frio recovered in the Sovio Sewers Dark Sector).
- **The Eclipse Band & Eclipse Shards**: While Siara previously required large machines, time, and energy to trigger Eclipsing, Ivo discovered how to trigger it instantaneously using an accessory called the **Eclipse Band**, which channels the power of fragile, rare meteorite fragments called **Eclipse Shards** (which break upon a single use and cause a permanent, irreversible Eclipse transformation). Ivo entrusted Asher with the **Eclipse Band** (Turn 27799) to protect himself against Siara and uncover the secret of Eclipsing.
- **The Custom PokéDex**: At Jackson's request, Ivo also gave Asher a custom **PokéDex** (Turn 27801) that registers the **stats**, **abilities**, and **habitat** of caught Pokémon before departing (verified Turns 27779-27803).

- **Amor Battle Center Text Message (Round One Summons)**: Immediately after Professor Ivo departed (Turns 27805-27806), Asher received a text message on his HuPhone from the **Amor Battle Center**: *"Dear Contestant! The very first round of the Eclipse Tournament is about to start. Please, head back to the Battle Center in Amor City to participate in the round's battles. If you have any questions, be sure to ask the receptionist, in the building where you signed up. Good luck, Pokémon Trainer! - Amor Battle Center"*. Asher resolved to head back to Amor City for Round One and hoped Valora would make it in time as well.

## Eclipse Tournament Round One — Victory Over Roark & Frio's Mt. Gerhana Challenge
- **Round One Bracket & Matches (Turns 27981-28020)**: Inside the Amor City Battle Center's Round 1 Arena, Asher competed in an 8-trainer single-elimination bracket on a holographic cyber-arena stage:
  1. **Quarterfinals**: Defeated **Camper Paul** (Buizel Lv11, Pidgey Lv11, Bulbasaur Lv12).
  2. **Semifinals**: Defeated **Youngster Chad** (Rattata Lv11, Timburr Lv12, Electrike Lv12), while Sinnoh Gym Leader **Roark** defeated Bug Catcher Jim on the opposite side of the bracket.
  3. **Round One Finals**: Defeated Sinnoh Gym Leader **Roark** (Hippopotas Lv12, Cranidos Lv12, Onix Lv13) to win his Round One bracket and advance to Round Two of the Eclipse Tournament.
- **Post-Round-One Reunion with Valora & Host Announcement (Turns 28021-28023)**: In the Tournament Arena Lobby (`11, 9`), Valora ran up to Asher and shared that she also won her Round One group. Over the PA loudspeaker, the Host announced the conclusion of Round 1 and told advancing trainers to relax until notified for Round 2.
- **Frio's Race to Mt. Gerhana for the Eclipse Rock (Turns 28023-28027)**: **Frio** arrived in the corridor (`10, 11`), mocked the Round 1 competitors, and received a call instructing him to head to **Mt. Gerhana** to recover a mineral called the **Eclipse Rock**. Frio challenged Asher to a race to Mt. Gerhana: if Asher finds the Eclipse Rock first, he can keep it and uncover the answers to Eclipsing; if Frio finds it first, Frio will use the artifact to get closer to cracking the secret of Eclipsing. After Frio departed, Valora insisted on accompanying Asher so he wouldn't face Frio alone (*"Okay, got it, I'll follow like a shadow!"*) and joined Asher's party as a companion to head to Mt. Gerhana.

<hr>

<h1><code>Main</code></h1>

# Game Info
- Title: Pokémon Sors
- Developer: Vytron (2015-2021)
- Version: 1.3 (Basic Version)
- Region: Hupest Region

# Guidelines & Active Reminders
- Nicknaming: Always nickname every Pokémon creatively!
- Text Speed: FAST

<hr>

<h1><code>Mechanics/Engine</code></h1>

## Status Conditions & Overworld Poison Mechanics

- **Overworld Poison Damage**: Overworld poison damage is completely DISABLED in Pokémon Sors v1.3 (aligns with Gen 5+ / CFRU engine rules).

- **Turn-in-Place Mechanic**: There is NO turn-in-place mechanic on foot; pressing a D-Pad direction always turns and attempts a forward step unless blocked by terrain collision.

## Facilities & PokéMarts

- **PokéMarts Inside Pokémon Centers**: In the Hupest region, PokéMarts are integrated directly inside Pokémon Centers on the upper mezzanine floor! Reached via the blue carpeted stairs/escalator in the northwest corner of the center. Verified functional with clerk in Sovio City. (Note: Lancio Town Pokémon Center also features the northwest mezzanine escalator).

- **Bulk Poké Ball Purchases & Premier Ball Mechanic**: In Pokémon Sors, purchasing 10 Poké Balls does NOT grant a bonus Premier Ball.

## Quests & Mission Engine

- **Single Active Quest Limit & Cancellation**: The player can only have ONE active side quest at a time in Pokémon Sors.
  - **At the Current Quest's Provider**: Speaking to the NPC who gave the currently active quest repeats their quest hint and then prompts: *"If you find this too hard you can just say no too... / Wanna cancel the Quest? Yes/No"* (cursor defaults to **Yes**; pressing A selects Yes and cancels the quest with *"Its okay, it seems like a difficult task anyway..."*, verified at Route 2 `40, 21` in Turn 28402).
  - **At Any Other Quest Provider**: Attempting to accept a normal side quest from a different NPC while a normal quest is already active displays verbatim: *"You are already doing a Quest! Cancel the Quest in progress at the provider to start a new one."* without offering a cancellation prompt—you must return to the original quest provider to cancel an active quest (verified with Roark in Mt. Gerhana, Turn 28087).

  - **Special Quests Exception**: Quests marked with a yellow speech bubble icon (such as Quest #11 "Oak's Research") are **Special Quests**: *"These quests have a different icon from the rest. They are far more complicated than the normal quests you can take. Completing them might take longer than an ordinary quest. These quests usually have multiple tasks for multiple rewards, and their fullest completion might arc through the entire game! They can't be cancelled, however this doesn't affect other Quests! Special Quests can be in progress besides pending Quests!"* (verified Turn 28502).

## HuPhone Regional Device & Apps
- **Access**: Activated via SELECT button or through BAG Key Items pocket.
- **Main App Menu**:
  1. **Item Storage**: Launches portable PC terminal (contains Item Storage, Mailbox, Turn Off).
  2. **World Map**: Interactive regional map viewer of Hupest navigated via D-pad (+Move). Dynamically displays location hover banners (e.g. Solare Island, Divampa Cave, Mulberry Town) in the top-left corner.
     - **Dynamic Banners**: Hovering over location nodes displays town/route names and subtitles in top-left (e.g., "Sovio City / Metro Station", "Amor City / Amor Dept.", "Route 4", "Route 16").
     - **Player Location Pin**: Asher's current position is tracked by a yellow pin with a black tip.
     - **Interactivity & Fast Travel**: Node interaction with button 'A' is inert; no fast travel or town info cards exist. The World Map functions strictly as a regional topological reference.
     - **Controls**: D-pad moves cursor; START button immediately snaps cursor to bottom-right '[X]' ('Close Map'); pressing A on '[X]' or B button exits back to the HuPhone menu.
  3. **Quest Log**: Active objective tracker and completed quest list.
  4. **Back**: Closes HuPhone.
- **Portable PC Interface (Item Storage app)**:
  - **Item Storage**: Submenu with Withdraw Item, Deposit Item, Toss Item, Cancel.
  - **Mailbox**: Portable PC mailbox (no mail present). 
  - **Turn Off**: Exits portable PC interface.
- **Quest Log Scope & Structure**:
  - Tracks side quests across 5 pages (23 named quests + 2 '- Not available -' slots). Main story progression milestones are NOT tracked in the Quest Log app.
  - **Page 1 Quests**:
    1. Lost Pidgey (Completed)
    2. Lost Toy (Completed)
    3. Egg Research (Uncompleted — accepted at Route 2 `40, 21` in Turn 27680 and canceled in Turn 28402; find an Oval Stone held by wild Happiny on Route 2)
    4. Medic! (Completed in Turn 28495 — delivered Cure Flower from Route 2 `45, 14` to Old Gentleman at Azluf Town Lighthouse `52, 5`; rewarded **Exp. Share**)
    5. Squirtle Gang (Uncompleted; displays "This Quest hasn't been completed yet!")
  - **Page 2 Quests**:
    6. Lost Eevee
    7. Kaboom
    8. Valentines Gift
    9. Angry Cubone Kid
    10. Push it!
  - **Page 3 Quests**:
    11. Oak's Research (Special Quest, Active — accepted at Azluf Town `40, 7` in Turn 28501; Task 1: show Professor Oak the PokéDex with 10 Pokémon caught)
    12. Elm's Research
    13. Rowan's Research
    14. Cynthia's Research
    15. Help for Barry
  - **Page 4 Quests**:
    16. - Not available -
    17. - Not available -
    18. Roark's Opal (Completed in Turn 28444; rewarded all 11 Fossils)
    19. Pokédex!
    20. Marine Point Hunter
  - **Page 5 Quests**:
    21. Hugh's Pokémon
    22. Silver's Deal
    23. Back to the...
    24. Outcasts
    25. The Mods of Cord
  - 'Quest Status': When a quest is active, displays the currently tracked quest status and system instructions. When no quest is active, displays 'You aren't doing any Quest at the moment!'.
  - HuPhone Menu & Quest Navigation: Neither the main HuPhone app menu nor the Quest List dismiss with the B button. The player must explicitly navigate down to 'Back' or 'Exit' and press A to close them.

## Pokémon Center Respawn Mechanics

- **Whiteout / Blackout Respawn Point**: Respawn points are set only when speaking to Nurse Joy at the counter to heal. Simply entering a Pokémon Center without talking to Nurse Joy does NOT register a new checkpoint.

## Verified Inventory State & Field Move Capabilities

- **Items Pocket (Audited Turn 28654)**: Contains Poison Barb x1, Antidote x1, Revive x1, Berry Juice x4, Moomoo Milk x2, Moon Stone x1, Silk Scarf x1, Exp. Share x1, **Green Shard x1** (hidden item found at Route 2 `46, 52` in Turn 28589), plus 11 Fossils received from Roark upon completing Quest #18 ("Roark's Opal") in Turns 28443-28445: **Old Amber x1**, **Helix Fossil x1**, **Dome Fossil x1**, **Skull Fossil x1**, **Armor Fossil x1**, **Cover Fossil x1**, **Plume Fossil x1**, **Jaw Fossil x1**, **Sail Fossil x1**, **Root Fossil x1**, and **Claw Fossil x1**.
- **Repel Auto-Renewal Prompt**: When an active Repel expires on a step, the engine automatically displays: "Repel's effect wore off... Use another? Yes/No" (cursor defaults to Yes; pressing A immediately consumes and applies the next Repel without opening the Bag, verified Turn 27448).
- **Bag Structure (Audited Turn 27862)**: Features 3 main horizontal pockets from left to right: **Items** (Pocket 1), **Key Items** (Pocket 2), and **Poké Balls** (Pocket 3; does not wrap around when pressing Right).
- **Poké Balls Pocket (Audited Turn 28677)**: Contains **Poké Ball x0** (purchased 4 Poké Balls at Azluf Town PokéMart in Turn 28654, used 1 catching Umbra the Zubat in Turn 28660 and 3 catching Quasar the Whismur in Turns 28665-28676; **10 Owned species** in PokéDex: Riolu, Pidgey, Starly, Remoraid, Grubbin, Shinx, Roggenrola, Geodude, Zubat, Whismur).
- **Key Items Pocket (Audited Turn 27862)**:
  - **HuPhone** (registered to `[SELECT]`): *"A convenient smartphone that has many features to use."*
  - **TM Case**: *"A case that holds TMs and HMs. It is attached to the Bag's compartment for important items."*
  - **Metro Pass**: *"Its a card that can be used at the e-ticket reader gates to travel on the Hupest Metro Line."*
  - **Eclipse Band**: *"A special band designed to channel the power of Eclipse Shards to allow Eclipsing!"* (received from Professor Ivo in Azluf Town, Turn 27799).
  - **Fishing Rod**: *"A new, high-quality fishing rod. Use it by any body of water to fish for wild Pokémon."* (received from Fisherman at `37, 30` in Azluf Town, Turn 27854). Casting into water prints `. . .` dots and automatically resolves to either *"A Pokémon's on the hook!"* (requiring a single A/B press to start the wild battle, with no timing minigame) or *"Not even a nibble..."* (verified Turn 27865).
- **TMs & HMs Pocket**: Contains only TM17 (Protect) and TM48 (Work Up). Zero HMs in possession.

- **Empirical Constraint & Equipment Mechanic**: Interacting with cracked/rugged rocks in Sovio Sewers displays verbatim: "It's a rugged rock, but with some equipment, I could smash it." Confirmed that smashing rugged rocks is mechanic-gated by specialized equipment rather than traditional HM Rock Smash (verified at `6, 23` and `22, 10` in Sovio Sewers, Turns 27495 & 27512).

## Trainer Card Structure & Display
- **Front Layout**: Name (Asher), ID No. (54592), Money, Playtime. Features '*ROUNDS' row tracking 8 Poké Ball icons for the Eclipse Tournament.
- **Back Layout**: Displays 6 dark badge/crest silhouettes, red geometric stripes, and regional circular crest.
- **Card Controls**: Pressing A on either side initiates a 3D flip animation between Front and Back. Pressing B when settled on the Front exits back to the Start Menu.
## Start Menu Structure & Pokédex Status
- **Start Menu Entries**: Displays Pokédex, Pokémon, Bag, Asher (Trainer Card), Save, Option, Exit.
- **Empirical Pokédex Status & Special Function**: Asher received the **PokéDex** from Professor Ivo in Azluf Town in Turn 27801 (commissioned for Asher by Jackson). In addition to standard entries, the PokéDex registers the **stats**, **abilities**, and **habitat** of caught Pokémon (verified Turn 27802).
- **Pokédex Table of Contents (Audited Turn 27859)**: Tracks `Seen` and `Owned` counts across two regional dex categories (`Colen` and `Hupest`), with 54 Hupest species and 17 Colen species pre-marked as `Seen` upon receipt.
- **In-Game Real-Time Clock**: Displayed in top-left HUD box when Start Menu is open; synchronizes with host system clock.
- **TM Reusability**: Confirmed infinite use in Pokémon Sors v1.3; TM48 (Work Up) remains in the TM Case after being taught to Sirius.

## Custom Emulator SDK & Sandbox Execution Limits
- **Script Button Accumulator Limit**: The sandbox Python environment enforces a cumulative session limit on button commands executed via Python scripts/mgba. When this limit is reached, any script attempting button commands will abort with 'Maximum cumulative limit of 100 buttons per script execution exceeded'. Controller button commands should strictly use the native press_buttons tool.
- **Tool Limitation (stun_npc)**: The `stun_npc` tool fails with 'Error: Map objects data is unavailable' on this ROM/engine build. Do not invoke `stun_npc`.
## Hupest Metro Line Transit Mechanics
- **Boarding the Train**: With the **Metro Pass** in the Key Items pocket, stepping into a station's entry turnstile lane (e.g. `17, 24` in Amor Metro Station, verified Turn 27572) prompts *"Do you want to use the Hupest Metro Line? Yes/No"*. Selecting *Yes* walks the player onto the platform into the train car (`11, 8`) with the announcement *"Please mind the closing doors!"* (verified Turn 27574).
- **Train Interior Layout (`cols 1-24, rows 4-8`, verified via `latest_grid.png` Turns 27575, 27578, 27581)**:
  - **Western Car (`cols 1-6`)**: Green door mat at `(2-4, 8)` (inert while moving); elderly man at `(1, 8)` (*"The Hupest Metro Lines are very famous for foreigners..."*, Turn 27581); Italian woman at `(3, 5)` (*"Vengo da una regione lontana! E tu?"*, Turn 27581); German man at `(4, 8)` (*"Früher waren Spiele originell!..."*, Turn 27581).
  - **West Gangway (`7-8, 7`)**: Connects Western and Middle cars along row 7; glasses passenger at `(7, 6)` (*"He's texting something on a messaging app... 'Day 69 of asking for a dating sim in sors.'"*, Turn 27576).
  - **Middle Car (`cols 9-14`)**: Green door mat at `(10-12, 8)` (arrival spawn at `11, 8`); Hungarian blonde girl at `(9, 5)` (*"Kíváncsi vagyok mikor jön ki a Pokémon Sors teljes verziója..."*, Turn 27580); passenger at `(14, 6)` refreshing a game site showing a fella in a red fedora talking to a Darkrai (Turn 27578).
  - **East Gangway (`15-16, 7`) & Eastern Car (`cols 17-22`) & Far-East Gangway (`23-24, 7`)**: Green door mat at `(18-20, 8)`; Japanese passenger in Team Siara suit at `(22, 8)` (*"Watashi wa Joto kara kimashita..."*, Turn 27578); eastern end terminates at `(24, 7)` (Turn 27579).
- **Selecting a Destination Inside the Train Car (`4, 5` Seat Trigger)**: Stepping `Left` from `(5, 5)` into the purple passenger seat at `(4, 5)` sits Asher down and opens the prompt: *"Which city do you want to go to?"* with a destination list of 8 stations (`Amor`, `Sovio`, `Samurion`, `Destino`, `Galinor`, `E.S.`, `Colen`, `Dis Bay`). Selecting a station not yet unlocked displays *"You can't go to that city yet!"* (verified Turn 27582), while selecting an unlocked station such as `Sovio` announces *"The next station is... Sovio City!"* and warps to the destination station platform (`22, 17` in Sovio Metro Station, verified Turns 27583-27584).

## Battle UI & Type Effectiveness Indicators
- **Move Box Effectiveness Highlighting**: In the CFRU battle Fight menu, the selected move's box dynamically changes color to indicate type effectiveness against the active opponent (e.g. highlights **light green** when a move is super-effective, such as Steel-type Metal Claw against Fairy-type Cleffa or Psychic/Fairy-type Ralts; verified Turn 27656).

<hr>

<h1><code>Party/Altair_Starly</code></h1>

# Altair (Starly) - Teammate

## Profile
- **Species**: Starly (Normal/Flying)
- **Nickname**: Altair
- **Gender**: Male (♂)
- **Level**: Lv6
- **Ability**: Keen Eye (Prevents loss of accuracy; verified Turn 27904)
- **Caught**: Route 2 at `(12, 10)` in standard Poké Ball (Turns 27592-27605)
- **HP**: 20/20 HP (verified via Party menu in Turn 27627)
- **Moves**:
  - Slot 1: Growl (Normal, Status, 40 PP)
  - Slot 2: Tackle (Normal, Physical)
  - Slot 3: Quick Attack (Normal, Physical, Priority +1) (verified Turn 27904)

<hr>

<h1><code>Party/Cetus_Remoraid</code></h1>

# Cetus (Remoraid) - Teammate

## Profile
- **Species**: Remoraid (National Dex No. 223, Water-type)
- **Nickname**: Cetus (named after the Sea Monster constellation)
- **Gender**: Male (♂)
- **Level**: Lv6
- **Caught**: Azluf Town (`36, 31` fishing into `36, 32`) in standard Poké Ball (Turns 27865-27873)
- **HP**: 21/21 HP (healed to full; verified via Party menu in Turns 27901 & 28200)

<hr>

<h1><code>Party/Pulsar_Grubbin</code></h1>

# Pulsar (Grubbin) - Teammate

## Profile
- **Species**: Grubbin (Bug-type; evolves into Charjabug -> Vikavolt, Bug/Electric)
- **Nickname**: Pulsar (named after a magnetized neutron star emitting beams of electromagnetic radiation)
- **Gender**: Male (♂)
- **Level**: Lv4
- **Caught**: Route 2 at `(11, 9)` in standard Poké Ball (Turns 28037-28041)
- **Moves**:
  - Knows Vice Grip (Normal, Physical; observed in wild battle Turn 28039)
- **HP**: 18/18 HP (verified via Party menu in Turn 28200)

<hr>

<h1><code>Party/Sirius_Riolu</code></h1>

# Sirius (Riolu) - Starter Pokémon

## Profile
- **Species**: Riolu (Regional Dex No. 161, Fighting-type)
- **Nickname**: Sirius (Officially renamed from default Riolu via Sovio Name Rater)
- **Gender**: Male (♂)
- **Level**: Lv26
- **Nature**: Relaxed (+Def, -Speed)
- **Ability**: Quick Feet (Boosts Speed by 50% if suffering from a major status condition)
- **Stats (IV Grades)**: HP 67 (C), Attack 47 (C+), Defense 48 (A-), Sp. Atk 32 (C-), Sp. Def 37 (E), Speed 35 (C-)
- **Current Condition**: 34/67 HP, Paralyzed (activates Quick Feet +50% Speed boost; verified after battling Explorer Ben in Turn 28576)
- **EXP**: Lv26 (reached during battle against Bug Catcher Nicolas on Route 2, Turn 28555)
- **Moves**:
  - Slot 1: Metal Claw (Steel, Physical, 50 power, 95% acc, 35 PP; 10% chance to raise Attack +1)
  - Slot 2: Force Palm (Fighting, Physical, 60 power, 100% acc, STAB, 10 PP; 30% chance to Paralyze; learned at Lv20 replacing Quick Attack)
  - Slot 3: Work Up (Normal, Status, 20 PP; raises Attack and Sp. Atk by +1 stage; taught via TM48)
  - Slot 4: Mach Punch (Fighting, Physical, Priority +1, STAB, 30 PP)
  - *Declined / Replaced*: Counter (Physical Fighting, offered Lv12; declined), Quick Attack (Normal Priority +1, replaced at Lv20 by Force Palm), Nasty Plot (Status Dark, +2 Sp. Atk, offered Lv24; declined)
- **OT / ID**: Asher / 54592
- **Met**: Lancio Town at Lv5
- **Appearance**: Custom sprite wearing a red/black scarf
- **Held Item**: Black Belt (boosts Fighting-type moves by 20%)

<hr>

<h1><code>Party/Vega_Shinx</code></h1>

# Vega (Shinx) - Teammate

## Profile
- **Species**: Shinx (Electric-type; evolves into Luxio -> Luxray)
- **Nickname**: Vega (named after Alpha Lyrae, the bright blue-white star of the Summer Triangle alongside Altair)
- **Gender**: Female (♀)
- **Level**: Lv3
- **Ability**: Intimidate (Cuts the foe's Attack stat upon entering battle; verified Turn 28053)
- **Caught**: Route 2 at `(53, 26)` in standard Poké Ball (Turns 28052-28059)
- **HP**: 16/16 HP (verified via Party menu in Turn 28200)

<hr>

<h1><code>Party/Zephyr_Pidgey</code></h1>

# Zephyr (Pidgey) - Teammate

## Profile
- **Species**: Pidgey (Regional Dex No. 016, Normal/Flying)
- **Nickname**: Zephyr
- **Gender**: Male (♂)
- **Level**: Lv2
- **Caught**: Route 1 in standard Poké Ball
- **Nature**: Mild (+Sp. Atk, -Def)
- **OT / ID**: Asher / 54592
- **Met**: Route 1 at Lv2
- **Item**: None
- **Ability**: Keen Eye (Prevents loss of accuracy)
- **Stats (IV Grades)**: HP 13 (D+), Attack 7 (C), Defense 5 (C-), Sp. Atk 6 (C+), Sp. Def 6 (D-), Speed 7 (A)
- **Moves**:
  - Slot 1: Tackle (Normal, Physical, 35 PP)
  - Slot 2: Protect (Normal, Status, 10 PP; taught via TM17)

<hr>