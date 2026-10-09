<h1><code>Locations/Amor_City</code></h1>

# Amor City

## Amor Metro Station
- **Arrival Platform** (`latest_grid.png` & physical arrival Turn 27547):
  - Train from Sovio City arrives at the northern boarding platform (`18, 17`) on initial story arrival, whereas subsequent Hupest Metro Line trips to `Amor` spawn the player directly at `(20, 26)` in the Upper Ticket Concourse (verified Turn 31408).
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
  - East staircase (`12-13, 3-4`) with vertical red mat at `(11, 3-4)`: stepping `Right` from the top mat tile `(11, 3)` onto `(12, 3)` warps to `(24, 35)` in the Amor Metro Station Lower Concourse (whereas `(12-13, 4)` are walkable stair tiles, verified Turn 29660). Ground floor features Ace Trainer Male at `(6, 12)` and Ace Trainer Female at `(14, 13)`, while the Tournament Arena Lobby features Round 1-4 guards at `(10, 17)`, `(13, 17)`, `(17, 17)`, `(20, 17)` and Round 5-8 guards at `(10, 26)`, `(13, 26)`, `(17, 26)`, `(20, 26)` (verified Turns 29639-29655). In Amor City Exterior, stepping onto `(66, 28)` or `(66, 29)` triggers the Eastern Construction Worker at `(66, 27)` (*"I'm sorry but the city is closed off due to constructions!"*, verified Turns 29635-29636).
  - Two blue escalators at `column 5` (`rows 7-9`) and `column 15` (`rows 7-9`) descend to the ground floor.
- **Ground Floor (`rows 10-21`)** (`latest_grid.png` Turns 27565-27566 & physical traversal Turns 27556-27566):
  - Central curved red reception counter (`8-12, 10-12`) with Battle Centre Assistant at `(10, 10)` (repeats standard tournament overview post-Round 1, verified Turn 28829) and Poké Ball floor emblem at `(9-11, 13-15)`.
  - Stepping down the west escalator to `(5, 9)` (Turn 27555) triggers the Eclipse Tournament registration cutscene with Dad and Valora (Turns 27556-27561), where Asher receives the **Metro Pass** and registers for the tournament before encountering **Frio** at `(10, 14)` (Turns 27561-27564).
  - Interacting with Frio at `(10, 13)` from `(10, 14)` after registration displays verbatim: *"Maybe we shouldn't be bothering this prick..."* (verified Turn 27565).
  - Southern exit mat at `(9-11, 21)` is flanked by two lower blue escalators at `column 4` (`rows 19-22`) and `column 16` (`rows 19-22`) (`latest_grid.png` Turn 27566).
  - **Lower Arena Concourse (`rows 22-27`)**: Reached by descending the lower blue escalators at `(4, 19-22)` or `(16, 19-22)` (`latest_grid.png` Turn 27974 & physical traversal Turns 27975-27976; reached from reception by routing around the diamond pillars at `6-7, 14-18` or `13-14, 14-18` via `row 13`; note that `4, 26-27` and `16, 26-27` are solid diagonal wall corners, requiring the player to step north to `row 25` before aligning with `col 4` or `col 16` to ascend the escalators, verified via `latest_grid.png` Turns 28835-28836). Features a lower floor with a red mat at `(9-11, 27)` leading to the Eclipse Tournament arenas (per the receptionist's instructions in Turns 27971-27972).
  - **Tournament Arena Lobby (`15, 7` -> `row 17`)** (`latest_grid.png` Turns 27978, 27980):
    - Entry mat from the Lower Arena Concourse lands at `(15, 7)` (`cols 14-16, row 7`).
    - Corridor runs west along `row 6` (`cols 11-15`), south along `columns 11-12` (`rows 6-15`), and opens into a horizontal arena lobby (`cols 6-19+, rows 14-17`) with a lower blue escalator at `(6, 16-19)` on the west and a row of numbered round arena entrance mats along `row 17`:
      - **Round 1 Arena Entrance (`9-11, 17`)**: Unguarded red Poké Ball mat at `(10, 17)` prior to Round One; stepping `Down` off `(10, 17)` warps into the **Round 1 Arena** (verified Turn 27980). After Asher wins Round One, a blue-capped attendant stands at `(10, 17)` guarding the entrance (*"The round has already ended... Congrats for advancing forward!"*, verified Turn 28021).
      - **Round 2 Arena Entrance (`12-14, 17`)**: Guarded by blue-capped attendant at `(13, 17)` (*"This is where Round 2 will take place in... Not yet though."*, verified Turn 27980).
      - **Round 3 Arena Entrance (`16-18, 17`)**: Guarded by blue-capped attendant at `(17, 17)`.
      - **Lower Arena Ring (`cols 6-19, rows 20-25`, reached via escalator at `6, 16-19`)**: Contains 4 additional numbered round arena entrances along `row 25` (`Rounds 5-8`), all guarded by blue-capped attendants (verified Turn 28832).
    - **Post-Round-One Cutscene (`11, 9` -> `10, 9`, Turns 28021-28027)**: Stepping north onto `(11, 9)` after winning Round One triggers a cutscene with **Valora** (who also won her Round One group), the **Host** PA announcement concluding Round 1, and **Frio**, who challenges Asher to a race to **Mt. Gerhana** to find the **Eclipse Rock** before Valora joins Asher to travel to Mt. Gerhana.
  - **Round 1 Arena & Eclipse Tournament Round One (`4, 14` -> `14, 14`)** (`latest_grid.png` Turns 27983-27984 & physical completion Turns 27981-28020):
    - **Bracket & Format**: Entering `(10, 17)` displays the 8-trainer Round One bracket screen (`7, 17` map coordinate): Left side features **Asher vs. Camper Paul** and **Youngster vs. Youngster Chad**; Right side features **Roark vs. Picnicker** and **Bug Catcher Jim vs. Ruin Maniac**. No automatic healing occurs between the 3 consecutive matches.
    - **Cyber-Arena Layout**: For each match, the player materializes on a white/cyan teleporter pad at `(4, 14)`. Walking `Right 10` along `row 14` (`(4, 14) -> (14, 14)`) crosses the narrow chasm bridge (`12-13, 14-15`, where an Arena Attendant stands at `13, 15`: *"Good luck, Trainer!"*) onto the white-outlined trainer box at `(14, 14)`, which walks both trainers onto the stage (`16, 14`) and morphs the cyber-arena into a holographic rocky cavern battlefield.
    - **Match 1 (Quarterfinals — Camper Paul)**: Pre-battle quote: *"I came here to win! And I'm gonna!"*; uses 3 Pokémon—Buizel (♀, Lv11), Pidgey (♀, Lv11), and Bulbasaur (♂, Lv12); defeat quote: *"Nooooo! I lost the very first battle..."*; awards `₽576` (verified Turns 27985-27995).
    - **Match 2 (Semifinals — Youngster Chad)**: Pre-battle quote: *"I have won one battle! I'll win this one as well!"*; uses 3 Pokémon—Rattata (♂, Lv11), Timburr (♀, Lv12; Bide), and Electrike (♀, Lv12); defeat quote: *"How in the..."*; awards `₽624` (verified Turns 27996-28007).
    - **Match 3 (Round One Finals — PKMN Trainer / Leader Roark)**: Pre-battle quote: *"My name is Roark. I'm a gym leader from Sinnoh. May the stronger Trainer win!"*; uses 3 Pokémon (displayed with 4 Poké Ball icons in HUD)—Hippopotas (♂, Lv12; Sand Stream, Sand Tomb, +1 Potion), Cranidos (♂, Lv12; Mold Breaker), and Onix (♀, Lv13); defeat quote: *"... / Looks like this is the end for me. Thanks for the battle!"*; awards `₽1456` (verified Turns 28008-28019). Winning Round One returns Asher to `(10, 16)` in the Tournament Arena Lobby.
- **Exterior Plaza (`53-66, 24-29`) & Western Boulevard (`cols 7-52, rows 27-35`)** (`latest_grid.png` Turns 27568, 31900-31909):
  - **Route 4 Gatehouse (`1, 7` <-> `15, 7`)**: Connects Route 4 North `(30, 16)` to Western Amor City at `(7, 33)` (verified Turns 31898-31900).
  - **Western Signboard (`11-12, 33`)**: Interacted from `(12, 34)`, reads verbatim: *"Amor City / The center of Hupest"* (verified Turn 31901).
  - **Western Amor City Pokémon Center (`23, 27`, exits to `23, 28`)**: Reached via `(16, 34 -> 17, 32 -> 23, 32 -> 23, 27)`; Nurse Joy at `(7, 2)` (counter at `7, 4`; healed and registered checkpoint in Turn 31904).
  - **PiTaxi Operator & Pidgeot (`26, 27` & `27, 27`)**: Standing east of the Pokémon Center: *"The PiTaxi is not in service until the constructions finish..."* (verified Turn 31908).
  - **Main Avenue Connection (`rows 29-30`)**: Upon arriving via Route 4 for Round 2, the `(53, 27)` construction roadblock is cleared, connecting `(26, 29)` directly east along `row 29` to the **Amor City Battle Centre** (`59, 24`, verified Turn 31910).
  - Stepping `Down` on the Battle Centre exit mat at `(10, 21)` warps outside to `(59, 25)` in Amor City (door at `59, 24`, verified Turn 27566-27567).
  - Signboard at `(56-57, 25)` interacted from `(57, 26)` reads verbatim: *"Amor Metro Station / Amor Battle Centre"* (verified Turn 27568).
  - Eastern street passage at `(66, 27)` is blocked by a construction worker (*"I'm sorry but the city is closed off due to constructions!"*, verified Turns 29635-29636).

## Round 2 Arena & Eclipse Tournament Round Two (`13, 17` -> `4, 14` -> `14, 14`)
- **Bracket & Format (Entered Turn 31914 at `13, 17` -> `7, 17` Bracket Screen)**:
  - **Left Bracket**: **Asher vs. Picnicker Raginald** (Match 1) and **Ace Trainer Male vs. Ruin Maniac/Camper** (Match 2; won by Ruin Maniac/Camper).
  - **Right Bracket**: **Cheryl (from Sinnoh) vs. Ace Trainer Female** (Match 3; won by Cheryl) and **Worker vs. Black Belt** (Match 4; won by Worker).
- **Match 1 (Quarterfinals — Picnicker Raginald)**:
  - **Pre-Battle Quote**: *"Yeah yeah! / I advanced through the first round, I'll advance through this one too!"*
  - **Team (3 Pokémon)**: Swadloon (♀, Lv19; Bug/Grass; knows GrassWhistle and String Shot), Lombre (♂, Lv19; Water/Grass; knows Fake Out), and Ivysaur (♂, Lv20; Grass/Poison).
  - **Outcome**: Defeat quote: *"How could this be?"*; awards `₽800` (verified Turns 31918-31930).
- **Match 2 (Semifinals — Lass Stacy)**:
  - **Pre-Battle Quote**: *"Teehee! / What a cute opponent I have here!"*
  - **Team (3 Pokémon)**: Flaaffy (♀, Lv20; Electric), Palpitoad (♂, Lv20; Water/Ground), and Purugly (♀, Lv20; Normal).
  - **Outcome**: Defeat quote: *"Argh!"*; awards `₽1,280` (verified Turns 31932-31937).
- **Match 3 (Round Two Finals — PKMN Trainer Cheryl)**:
  - **Pre-Battle Quote**: *"Hello, Trainer! / My name is Cheryl. / I came from the Sinnoh Region, I hope my journey wasn't a waste. / Let's enjoy our fight"*
  - **Team (4 Pokémon)**: Drifloon (♂, Lv20; Ghost/Flying; Ability: Aftermath), Wailmer (♂, Lv20; Water), Wormadam (♀, Lv20; Plant Cloak, Bug/Grass; knows Protect), and Chansey (♀, Lv21; Normal).
  - **Outcome**: Defeat quote: *"My my... / I guess this is the end for me..."*; awards `₽1,260` and crowns Asher winner of his Round 2 group (verified Turns 31940-31953).
## Post-Round-2 Street Layout & Route to Northern Amor City (Verified Turns 31958-31965)
- **Eastern Avenue Extension (`cols 60-74, rows 27-30`)**: After winning Round 2, the construction worker at `(66, 27)` is gone, opening the main avenue east to `column 74`, where three construction workers at `(75, 28)`, `(75, 29)`, and `(75, 30)` block further eastbound progress (*"I'm sorry, there are still construction going on in the city!"*, verified Turn 31960).
- **Central Northbound Street (`cols 42-44, rows 12-28`) & Northern Westbound Street (`cols 18-44, rows 12-13`)**:
  - From the main avenue (`43, 29`), an open northbound street runs along `columns 42-44` (`rows 12-28`) to a northern junction at `(43, 12-13)`.
  - Two construction workers at `(45, 12-13)` block the eastbound branch, while the westbound street along `rows 12-13` (`cols 18-44`) is open and leads to the northwestern vertical avenue along `column 18` (with a streetlamp at `17, 10-12`, verified Turn 31965).
- **Northwestern Route 6 Signboard (`14-15, 7`) & Route 6 Gatehouse (`7, 7` <-> `14, 7`)**:
  - Following `column 18` north from `(18, 13)` to `(18, 7)` reaches the northwestern gatehouse street (`cols 7-18, rows 7-8`).
  - Wooden signboard at `(14-15, 7)` (interacted from `15, 8`) reads verbatim: *"Route 6 / <-------"* (verified Turn 31969).
  - Stepping `Left` along `row 7` (`(9, 7) -> (8, 7) -> (7, 7)`) enters the **Route 6 Gatehouse** at `(14, 7)` (verified Turn 31971).

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
- **Azluf Town Pokémon Center (`12, 33`)**: Located on the northern side of the western entrance road (`row 34`). An overhead walkable path along the top of the streetlamp (`15, 32-33`) and Pokémon Center roof (`10-15, 29`) leads to a 1-tile grass recess at `(13, 27-28)` bounded by a solid cliff wall at `(12, 27-28)` and `(13, 26)` and pine tree at `(14, 27-28)` (`latest_grid.png` Turns 31355-31356).
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
- **Mt. Gerhana Southern Entrance (`27, 14`)**: Reached via the northern stone stairs (`26-27, 18`) at the top of the `cols 26-27` avenue (bounded on the west at `cols 22-24` by cliffs and pine trees separating the lower Azluf Town avenue from the elevated northwest mountain ridge stairs at `19-21, 13-14`, which are accessed by emerging from the Mt. Gerhana Lower Pit Chamber archway `14, 25` to `10, 21`, verified Turns 31461-31465).
  - **Verified Collision-Free Route Between Azluf Pokémon Center (`12, 34`) & Mt. Gerhana (`27, 14`)**: `(12, 34) <-> (12, 35) <-> (16, 35) <-> (16, 34) <-> (21, 34) <-> (21, 28) <-> (23, 28) <-> (23, 27) <-> (27, 27) <-> (27, 14)` (37 steps total, bypassing the streetlamps at `15, 34` and `24, 26`, verified Turns 30763, 30794 & 30806).
  - **Signboard (`25, 16`)**: Interacted from `(25, 17)`, reads verbatim: *"Mt. Gerhana"* (verified Turn 27845).
  - **Worker Guard (`27, 15`)**: Blocks the cave entrance prior to Round One of the Eclipse Tournament: *"I'm sorry kid, but there are some mine works going on... We will move out of the way later!"* (verified Turn 27845). After Asher wins Round One of the Eclipse Tournament and accepts Frio's challenge, the guard is gone and stepping onto `(27, 14)` enters **Mt. Gerhana** (verified Turn 28074).
- **Eastern House — Professor Oak's House (`31, 24`)**: Blue-roofed cottage at the eastern end of the `row 26` purple brick road (`37, 10` interior exit mat).
  - **Professor Oak (`40, 7`) — Special Quest #11 ("Oak's Research", Active)**: Kanto Pokémon Professor with a yellow Special Quest bubble: *"Oh, hello there! You must be a Pokémon Trainer! You also seem to have a PokéDex, may I check it? Wow, this is a well made PokéDex! It's way more complex than mine... However it's pretty empty... Oh, how rude of me, I didn't even introduce myself... My name is Oak, I'm a Pokémon professor from the Kanto Region. I research Pokémon and gather data of them... Would you help me in my research? Yes/No"* (verified Turns 27848-27849).
    - **Task 1 (10 Pokémon Caught — Completed Turn 28681)**: Showing Professor Oak the PokéDex with 10 Owned species rewards a gift **Bulbasaur** (sent to Box 1, bringing Owned species to 11; verified Turns 28681-28682).
    - **Task 2 (25 Pokémon Caught — Completed Turn 29958)**: Showing Professor Oak the PokéDex with 25+ Hupest Owned species rewards a gift **Charmander** (sent to Box 1, verified via PokéDex Turn 29993).
    - **Task 3 (45/50 Pokémon Caught — Completed Turn 31043)**: Showing Professor Oak the PokéDex with 50 Hupest Owned species rewards a gift **Squirtle** (bringing Owned species to **51 Hupest / 20 Colen**, verified Turns 31043-31045). Subsequent interaction displays: *"Thank you, this will be enough, but come back later, I might have some more tasks for you!"* (verified Turn 31045).
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

<h1><code>Locations/Destino_City</code></h1>

# Destino City

## Geography & Connections
- **East (`59, 20` <-> `60, 20` Warp <-> Route 6 `0-1, 9`)**: Arriving west from Route 6 (`0, 9`) warps to the eastern paved square at `(59, 20)` in **Destino City**, while stepping east from `(59, 20)` onto `(60, 20)` warps back to Route 6 (`1, 9`; verified Turns 32183-32184). The eastern street runs west from `(59, 20)` via `(58, 20 -> 58, 22-23 -> 52, 22-23)` below a fire hydrant at `(55, 21)`.
## Facilities & Points of Interest
- **Destino City Pokémon Center (`41, 18`, exits to `41, 19`)**:
  - Located at the western end of the eastern stone street (`cols 41-59, rows 19-22`), with a wooden signpost at `(47, 19)` (interacted from `47, 20`, reading verbatim: *"Destino Metro Station / Up ahead"*, verified Turn 32194) and a wandering pigtail girl around `(47-48, 20-22)`.
  - **Interior (`7, 8` exit mat)**: Nurse Joy at `(7, 2)` (counter at `7, 4`; healed party and registered respawn checkpoint in Turn 32187); glasses man at `(6, 4)` (*"Health care is top notch for Pokémon... I wonder if it will ever be this good for humans."*, Turn 32188); wandering woman with dark bun around `(9-10, 6-7)`; PC terminal at `(12, 1)`; PokéMart mezzanine staircase at `(2, 0)` (connected seamlessly on the same map to `5, 7`, clerk at `5, 3` selling Poké Ball `₽200`, Great Ball `₽600`, Potion `₽300`, Super Potion `₽700`, Antidote `₽100`, Paralyz Heal `₽200`, Awakening `₽250`, Burn Heal `₽250`, Repel `₽350`, and Super Repel `₽500`, verified Turns 32191-32192).
- **Destino Metro Station Archway & Guard (`45, 14`)**:
  - North of the Pokémon Center (`cols 44-46, rows 13-18`), a green-uniformed worker at `(45, 14)` guards the northern archway leading to the Destino Metro Station: *"I'm sorry but the metro station is under renovation. Come back later"* (verified Turn 32194).
- **Town Signboard (`37-38, 19`)**:
  - Located immediately west of the Pokémon Center (interacted from `38, 20`); reads verbatim: *"Destino City / The industrial mine city"* (verified Turn 32194).
- **Western Street Roadblock (`34, 19-21`)**:
  - Stepping west onto `col 34` (`34, 20`) prior to investigating the Destino Mine displays verbatim: *"We should check what's the deal with the Destino Mine!"* and steps the player east to `(35, 20)` (verified Turn 32195).
- **Southern Avenue & Diagonal Staircase toward Destino Mine (`cols 32-46, rows 22-30`)**:
  - Directly south of the Destino City Pokémon Center (`41, 18`), the tan curb along `row 22` (`cols 36-44`) is passable and leads south into the upper dirt plaza (`cols 36-46, rows 23-29`), where a female resident in a pink shirt patrols around `(40-41, 22-24)` (*"The city is huge... I need to find a Burger Kingler..."*, verified Turn 32197).
  - At the western edge of the upper dirt plaza (`36, 23`), stepping onto `(36, 23)` warps down the diagonal stone staircase to `(30, 26)` on the lower plaza (where a wandering Sailor patrols `29-30, 28-30` and a residential house sits at `25, 30`), leading east along `rows 29-31` to the main **Destino Mine** entrance at **`(39, 28)`** (flanked by a miner at `40, 30` saying *"We miners work hard everyday to dig up resources."* and a wooden signpost at `41, 30` reading verbatim: *"Destino Mine"*, verified Turns 32198-32201).

<hr>

<h1><code>Locations/Destino_Mine</code></h1>

# Destino Mine

## Geography & Connections
- **Main Entrance (`47, 7-8` <-> Destino City `39, 28`)**: Connects at `(47, 7)` to the southern mining plaza of **Destino City** (`39, 28`; verified Turn 32202).
- **Route 6 Stone Tower Chamber (`11, 46-47` <-> Route 6 `44, 18`)**: Separate small chamber entered from Route 6 (`44, 18` after completing Quest #7 "Kaboom"), containing an ancient stone tower at `(10-12, 53-55)` (*"It's a stone tower... / It appears to have been built many years ago"*, verified Turn 32175).
## Wild Pokémon
- **Numel**: Encountered at Lv18 (♀, Fire/Ground) on 1F at `(46, 14)` (caught in a Great Ball, nicknamed **Etna**, and transferred to Box 2 as 59th Owned species in Turns 32210-32214).
- **Diglett**: Encountered at Lv18 (♀, Ground) on 1F at `(47, 14)` (caught in a Great Ball, nicknamed **Gaia**, as 60th Owned species in Turns 32217-32221).
- **Klink**: Encountered at Lv17 (Steel) on 1F at `(50, 45)` (already owned; verified Turn 32230).
- **Trapinch**: Encountered at Lv14 (♀, Ground) on 1F at `(42, 49)` (caught in a Poké Ball, nicknamed **Dune**, and transferred to Box 2 as 61st Owned species in Turns 32245-32248).
## Main Entrance Cavern (`cols 40-54, rows 4-14`)
- **Valora Cutscene (`47, 9`, Turns 32203-32204)**: Stepping south onto `(47, 9)` from the entrance (`47, 8`) triggers Asher and Valora to deduce that Team Siara must have gone deeper into the mine.
- **Landmarks & NPCs**:
  - **Large Boulder (`49-50, 8-9`)**: Flanking the east side of the entrance archway.
  - **Overhead Blue Pipe & Red Support Girders (`col 44`, `43, 9-12`, `45, 10-12`)**: The western alcove (`cols 40-42`) is reached by routing along `row 8` (`45, 9 -> 45, 8 -> 42, 8`) above the top cap of the western girder (`43, 9`).
  - **Side Quest Explorer (`42, 12`) — Quest #6 ("Lost Eevee", Active)**: Standing in the western alcove above small rocks (`42, 13`, `41, 14`, & `45, 14`, all verified inert Turns 32208-32215), a stalagmite (`40, 11`, inert), and a golden item sphere at **`(40, 13)`** that yields **Red Shard x1** (collected Turn 32208). Asks the player to help find his missing partner Eevee, **Evy**, on the **second level** of Destino Mine while he searches the first level (accepted Turn 32207).
  - **Miners (`47-49, 10-12` & `52, 13`)**: A wandering miner patrols near the entrance tracks, and a second miner stands beside an orange mining machine (`50-52, 11-12`) at `(52, 13)` (*"These machines help us with all the mining work. / Technology really makes this industry strive!"*, verified Turn 32216).
  - **Southern Tunnel Doorway (`50, 16` -> `50, 17` <-> Main 1F Chamber `50, 42`)**: Stepping south from `(50, 14)` -> `(50, 15)` -> `(50, 16)` displays a downward exit arrow (`▼`) at `(50, 17)`; pressing `Down` from `(50, 16)` warps into the **Main 1F Chamber** of Destino Mine at **`(50, 42)`** below the northern archway (`50, 41`, verified Turns 32225-32227; note that `49, 15 -> 49, 16` is solid wall).
## Main 1F Chamber (`cols 35-55, rows 40-55`)
- **Northern Archway (`50, 41` -> `50, 42` <-> Entrance Cavern `50, 16`)**: Connects back to the southern tunnel doorway of the Main Entrance Cavern (`50, 16`; verified Turn 32227).
- **Coworker Eddie (`45, 46`, facing South)**:
  - **Pre-Battle Quote**: *"These mining equipment here are really heavy... / Not as heavy as my Pokémon though!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Aron (♀, Lv24; Steel/Rock; Ability: Sturdy; knows Protect and Roar).
    - **Pokémon 2**: Onix (♀, Lv24; Rock/Ground).
  - **Outcome**: Defeat quote: *"B-but my Pokémon"*; awards `₽960` (verified Turns 32232-32242).
- **Western Section (`cols 35-44, rows 41-49`)**:
  - **Overhead Blue Pipe (`col 44`)**: Passable horizontally across `rows 46-49`, solid along `rows 40-45`.
  - **Machop (`43, 44`), Orange Mining Machine (`40-42, 44-45`), & Crystal Alcove (`42, 40`)**: Machop stands at `(43, 44)` beside the machine (`"Machop: Chop! Chop!"`, verified Turn 32243). North of the machine across a cliff wall (`40-42, 41-43`), a small purple/teal Eclite crystal shard sits at `(42, 40)` next to a stalagmite at `(41, 40)` (observed via `latest_grid.png` Turn 32315).
  - **Small Rocks (`40, 49`, `35, 49`, `25, 49`, & `22, 49`)**: All four verified inert in Turns 32249, 32261, 32272, & 32273.
  - **Minecart Tracks (`rows 47-48`), Coworker Marvin (`38, 48` -> `39, 48`), & Northbound Staircase (`35-36, 44-45`)**:
    - Tracks run west below the northbound staircase at `(35-36, 44-45)`.
    - **Coworker Marvin (`38, 48` -> `39, 48`, rotating)**:
      - **Pre-Battle Quote**: *"These hats are to protect us during work... and battles!"*
      - **Team (3 Pokémon)**:
        - **Pokémon 1**: Graveler (♂, Lv24; Rock/Ground).
        - **Pokémon 2**: Boldore (♂, Lv24; Rock).
        - **Pokémon 3**: Larvitar (♂, Lv24; Rock/Ground).
      - **Outcome**: Defeat quote: *"Noooo!"*; awards `₽960` (verified Turns 32252-32259).
    - **Coworker Ifan (`32, 46`, facing South)**:
      - **Pre-Battle Quote**: *"My diamond pickaxe can mine anything!"*
      - **Team (1 Pokémon)**:
        - **Pokémon 1**: Steelix (♂, Lv26; Steel/Ground; knows Iron Defense).
      - **Outcome**: Defeat quote: *"Oh no."* ; awards `₽1,040` (verified Turns 32262-32267).
    - **Coworker Rudy (`20, 45` -> `22, 45`, facing East)**:
      - **Pre-Battle Quote**: *"So we back in the mine, got our pickaxe swinging from side to side!"*
      - **Team (4 Pokémon)**:
        - **Pokémon 1**: Rhyhorn (♂, Lv23; Ground/Rock).
        - **Pokémon 2**: Gurdurr (♂, Lv25; Fighting).
        - **Pokémon 3**: Palpitoad (♀, Lv24; Water/Ground).
        - **Pokémon 4**: Bronzor (Lv24; Steel/Psychic).
      - **Outcome**: Defeat quote: *"Oh man"*; awards `₽1,000` (verified Turns 32274-32285).
- **Northwestern Corridor & Team Siara Rockfall (`cols 18-32, rows 30-41`)**:
  - **Team Siara Rockfall Cutscene (`24, 40`, Turns 32287-32292)**: Stepping onto `(24, 40)` triggers a cutscene where four Team Siara Grunts start their operation and drop a rockfall across `(24-29, 33-35)` to block outsiders, accidentally stranding two grunts on the south side (`23, 35` and `23, 36`, facing East) while the other two grunts depart across the overhead wooden bridge (`26-27, 30-31`). Completing this cutscene also clears the two Machop (`27, 39-40`) that previously blocked the eastern staircase (`26, 39-41`).
  - **Stranded Team Siara Grunts (`23, 36-37` -> `25, 35-36`) & Frio's Rockfall Clearance (`26-27, 33-34`, Turns 32293-32308)**:
    - Initially, the two stranded grunts at `(23, 36-37)` whisper and blame each other for stopping at a bakery for sweets and getting locked on the wrong side of the rockfall.
    - Stepping onto `(26, 36)` triggers **Frio** to arrive (`25, 35`) and clear the central rocks (`26-27, 33-34`). The two stranded grunts immediately challenge Asher (`26, 35`) and Valora (`26, 36`) while Frio heads north under the bridge (`26, 30`):
      - **Siara Grunt (`25, 35`)**:
        - **Team (3 Pokémon)**: Mightyena (♀, Lv24; Dark; Ability: Intimidate), Toxicroak (♀, Lv25; Poison/Fighting), Haunter (♀, Lv24; Ghost/Poison).
        - **Outcome**: Defeat quote: *"These kids... aaargh!"*; awards `₽2,600`. Both defeated grunts flee north to warn their group, and Valora rejoins Asher at `(26, 35)` (verified Turns 32308-32309).
  - **Visible Landmarks Around `(26, 35)`**:
    - **Western Cliff Ledge Floor Ladder (`19, 36`)**: Visible on the raised western cliff ledge (`cols 17-20, rows 35-38`).
    - **Eastern Ledge Item Sphere (`32, 35`)**: Reached by ascending the double northbound staircases at `(36, 45)` and `(36, 40)` to `(36, 37)` (where small rocks at `36, 36` and `37, 37` are inert) and walking behind the top row of the 2x2 boulder (`34, 37 -> 34, 35 -> 33, 35`); yields **TM37 (Sandstorm)** (verified Turns 32313-32318).
  - **Northern Bridge Passage (`27, 34` -> `27, 24`), Upper Bridge Ledges (`cols 20-34, rows 24-31`), & Wall Ladder (`27, 24` <-> 2F `44, 10`)**:
    - Passing north under the overhead wooden bridge (`cols 26-28, rows 29-33`, where `26, 32-33` and `28, 32-33` are solid support pillars and `col 27` is the open center lane) leads to a northern alcove containing small rocks at `(26, 27)` and `(28, 25)` (both verified inert in Turn 32320; `(28, 35)` south of the bridge is also inert, verified Turn 32311), a stalagmite at `(26, 24)`, and a **wall ladder** at **`(27, 24)`** (`Up` onto `27, 24` displays `▲` at `27, 23`; pressing `Up` warps to the **Second Level (2F)** at **`(44, 10)`** facing North. Note: pressing `Down` while standing directly on `(44, 10)` warps back to `(27, 24)`—step `Right` to `(45, 10)` or `Left` to `(43, 10)` to dismount the ladder, verified Turns 32321-32324).
    - The overhead wooden bridge (`cols 26-28, rows 29-31`) connects a western upper ledge (`cols 20-25, rows 24-31`, containing an orange mining machine at `20-21, 27-28` and a stalagmite at `23, 29`) to an eastern upper ledge (`cols 29-34, rows 24-31`, containing a small rock at `30, 29` and a cave archway at `34, 28`, observed via `latest_grid.png` Turn 32320).
## Second Level (2F) (`44, 10`+)
- **Northern Ladder Entrance (`44, 10` <-> 1F `27, 24`)**: Arrives at `(44, 10)` facing North; small rock at `(46, 11)` is inert (verified Turn 32324).
- **Overhead Wooden Bridge (`cols 35-48, rows 14-16`)**: A **Team Siara Grunt** stands on top of the bridge at `(41, 14)` facing South, while the ground passage passes underneath along `col 43` (`43, 13 -> 43, 17`, verified Turn 32326).
- **Siara Grunt 1 (`43, 18`, facing West)**:
  - **Pre-Battle Quote**: *"What the?! / Didn't we block off the path?"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Arbok (♂, Lv24; Poison; Ability: Intimidate).
    - **Pokémon 2**: Seviper (♀, Lv25; Poison; knows Glare).
  - **Outcome**: Defeat quote: *"You are strong!"*; awards `₽2,500` (verified Turn 32333).
- **Siara Grunt 2 (`41, 21`, female grunt facing East)**:
  - **Pre-Battle Quote**: *"So you are telling me those idiots didn't just lock themselves out, but lost to some kids too?"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Weezing (♂, Lv24; Poison; knows Self-Destruct).
    - **Pokémon 2**: Zangoose (♀, Lv25; Normal).
  - **Outcome**: Defeat quote: *"Arghhh!"*; awards `₽2,600` (verified Turns 32334-32342).
- **Siara Grunt 3 (`47, 24` -> `47, 23`, rotating)**:
  - **Pre-Battle Quote**: *"We were driven here to secure the area for a unit retracting material from the mine..."*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Murkrow (♀, Lv24; Dark/Flying; knows Night Shade).
    - **Pokémon 2**: Absol (♂, Lv25; Dark; knows Swords Dance).
  - **Outcome**: Defeat quote: *"..."*; awards `₽2,600` (verified Turns 32344-32350).
- **Upper Eastern Ledge (`cols 48-55, rows 14-27`)**:
  - Reached via the double eastbound staircases at `(46, 22-24)` and `(48, 21-23)`; small rocks at `(49, 25)` and `(54, 18)` (across the overhead blue pipe at `cols 51-52`) are both verified inert (Turns 32351-32352). Connects north along `col 49` (`49, 21 -> 49, 15`) onto the overhead wooden bridge (`cols 35-48, rows 14-16`).
- **Siara Grunt 4 (`41, 14`, on overhead wooden bridge facing South)**:
  - **Pre-Battle Quote**: *"I'm honestly only doing all this because of the payment... / I got kids to raise you know, so I gotta do, what I gotta do!"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Swoobat (♀, Lv26; Psychic/Flying).
  - **Outcome**: Awards `₽2,704` (verified Turns 32364-32365).
- **Siara Grunt 5 (`26, 19`, female grunt on western upper passage)**:
  - **Pre-Battle Quote**: *"I hate trespassers... / Sorry, kiddo!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Bronzor (Lv24; Steel/Psychic).
    - **Pokémon 2**: Krokorok (♀, Lv25; Ground/Dark; Ability: Intimidate).
    - **Pokémon 3**: Durant (♂, Lv25; Bug/Steel).
  - **Outcome**: Defeat quote: *"This is awkwards."*; awards `₽2,600` (verified Turns 32370-32378).
  - **Raised Plateau Item Sphere (`29, 21`)**: Reached via the wooden staircase at `(25, 22-23)` (`24, 23 -> 25, 22 -> 29, 22`); yields **Fire Stone x1** (collected Turn 32381).

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

- Stairs at north wall: Apparent descending wooden staircase. Accessed via red capsule mat at (12, 7) (tile 11, 7 is the side railing). Prior to the Upper Mt. Gerhana Eclite Crystal awakening, stepping onto (12, 7) triggers story barrier text: "I probably shouldn't head down here..." (verified Turn 31497). After speaking with Professor Ivo at (20, 6) in Turn 31498 following the Mt. Gerhana collapse, she leads Asher down (12, 7) into her **Basement Laboratory** (`16, 17` stairs up; **Eclicizer** machine at `11, 12-14`).

- **East Research Wing (Comprehensive Audit)**:

  - Connected to foyer via hallway at row 10 (columns 13-16).

  - Sunlit diagonal wood flooring throughout research room.

  - Cylindrical incubator apparatus at (18-19, 5-6): Interacting facing North from (19, 6) displays 'Better not mess with that machine.'

  - Professor Ivo at (20, 6): Ambient dialogue ("Hey, Ashi, how's your new Pokémon?", verified post-tremor Turn 27080). After receiving the PokéDex in Azluf Town, speaking to her triggers a PokéDex progress check ("Ivo: Hey, Ashi, how's your PokéDex coming along?" -> "Ivo: Wow, you've registered 10 different species! Here, take this for your efforts!"), rewarding **Full Restore x1** at 10 Owned species (verified Turn 29012), **Max Revive x1** at 25 Owned species (verified Turn 30121), and **Destiny Knot x1** at 50 Owned species (verified Turn 31109) before repeating "Ivo: If you catch enough Pokémon I might give you some rewards...".

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
- **Post-Basement Lab HuPhone Trigger (`21, 14`, Turn 31508)**: Stepping onto `(21, 14)` south of the Lab signpost after receiving the Eclipsed Pidgey triggers Valora's text message inviting Asher to meet her in **Samurion City** via **Mt. Gerhana**, and automatically warps Asher to Route 2 `(77, 59)` at the western border of Azluf Town.

<hr>

<h1><code>Locations/Mt_Gerhana</code></h1>

# Mt. Gerhana

## Geography & Connections
- **Southern Entrance (`6, 30` interior <- `27, 14` Azluf Town)**: Connects to Azluf Town at `(27, 14)` (unlocked after winning Round One of the Eclipse Tournament, verified Turn 28074-28076). Stepping `Down` from `(6, 30)` exits back to Azluf Town. The western side of the 1F main cavern (`cols 5-9, rows 23-29`, where a Hiker wanders around `7-9, 23-25` stating *"This mountain is said to be sorrounded by some mystical energy!"*, verified Turn 28539, and an inert small rock sits at `6, 25`) is closed off on the west by the solid outer cave wall at `col 4` (`latest_grid.png` Turn 28447, verified Turn 28448).
- **Northern Ladder (`9, 19` -> `9, 17` interior <-> `13, 9` exterior clearing)** (`latest_grid.png` Turn 28782):
  - Ascending the wooden stairs north of Roark at `(8-10, 21-22)` reaches `(9, 20)` (bounded on the west at `cols 2-7` and east at `cols 11-16` by multi-tier cliff walls, with a 1x1 rock cone at `12, 17`, a 2x2 boulder at `11-12, 22-23`, and a dark pit at `16, 21-22` north of the underpass bridge, verified Turn 28782). Climbing the vertical wall ladder rungs from `(9, 19)` up to `(9, 17)` warps out to an exterior mountain clearing of **Mt. Gerhana** at `(13, 10)` in front of the cave mouth at `(13, 9)` (verified Turns 28090-28092 & 28328-28329).
  - **Solid Wall Behind Roark (`cols 11-18, rows 18-22`)**: Directly behind Roark (`13, 23`), the cavern floor at `(14-15, 21-22)` is closed off on the north and west by solid cliff walls (`cols 11-18, rows 18-20`, verified Turn 28313), while `rows 14-15` is a north-facing cliff wall dropping down into the Northern 1F Chamber (`cols 18-25, rows 6-16`, bounded on the west at `cols 17-18` by the outer map wall, verified Turns 28331 & 28358).
  - **Exterior Mountain Pass (`13, 10` -> `13, 15` -> `6, 14` -> `5, 9` -> `2, 6`)**: Verified via `latest_grid.png` (Turns 28703-28705) that the entire exterior pass (`cols 0-20, rows 5-19`) is enclosed by multi-tier canyon walls with a 2x2 outdoor boulder at `(7-8, 10-11)` (which has solid collision on all 4 tiles including its top row `7-8, 10`, verified Turn 31346). Descending the mountain steps (`13, 11-15`, bounded on the south at `row 16` and east at `col 18` by solid mountain walls, verified Turn 28329-28330) and following the canyon pass west along `rows 14-15` (`cols 5-14`) and north along `cols 3-6` (`rows 7-14`) leads only to the cave entrance at `(2, 6)` with a wooden signboard at `(4, 7)` (interacted from `4, 8`) reading verbatim: *"Route 2 / A hidden path"* (verified Turns 28092-28095). Stepping into `(2, 6)` exits to the closed-off northern enclave of **Route 2** at `(38, 9)` directly behind the Pokémon Day-Care yard (verified Turn 28098).
- **Eastern Underpass Bridge (`cols 16-24, rows 23-25`) & Upper North-South Bridge (`cols 19-21, rows 20-27`)**:
  - **All multi-column bridges and staircases across 1F and B1F** (`rows 23-25` of the 1F Underpass Bridge, `cols 28-30` of the 1F Northeastern Stairs, `cols 19-21` of the 1F North-South Bridge, `cols 33-35` of the B1F Central Ridge Staircases at `rows 20 & 26`, `cols 20-22` of the B1F North-South Bridge, and `cols 15-17` of the B1F Western Staircases) have been physically swept with zero coordinate triggers (verified Turns 31317-31330 & 31370-31378).
  - **From the main cavern floor east of Roark (`14-15, 23-25`, with an inert small rock at `15, 26`, verified Turn 28541)**, a horizontal wooden bridge at `cols 16-24, rows 23-25` passes directly underneath the elevated north-south wooden bridge (`cols 19-21`) to reach the **1F Eastern Cavern Floor (`cols 24-33, rows 23-26`)** (verified Turn 28106).
  - **1F Eastern Cavern Floor (`cols 24-33, rows 23-26`)**: Contains a small rock at `(27, 23)` and a wandering Hiker NPC around `(26-29, 25-26)`, and is enclosed on the south (`row 27`) and east (`col 34`) by cliff walls (`latest_grid.png` Turn 28277, verified Turns 28142, 28277-28283).
  - **Northeastern Stairs (`28-30, 21-22`) & Floor Ladder (`29, 18` -> B1F `37, 15`)**: Ascending the wooden stairs at `(28-30, 21-22)` reaches an enclosed upper terrace (`cols 27-31, rows 17-20`, with an inert small rock at `31, 20`). From here, an orange item sphere is visible on an elevated northern ledge at `(24, 13)` next to wooden stairs at `(22, 13-14)` (`latest_grid.png` Turn 28115). Stepping onto `(29, 18)` and pressing `Down` descends to **Mt. Gerhana B1F** at `(37, 15)` (verified Turns 28114-28116 & 28273; upon returning from B1F `37, 15` to 1F `29, 18`, pressing `Down` directly on `29, 18` immediately re-descends to B1F, whereas stepping `Left` to `28, 18` or `Right` to `30, 18` first exits onto the 1F terrace, verified Turns 28779-28780).

## Wild Pokémon
- **Geodude**: Encountered at Lv11 (♀, Rock/Ground) on the 1F main cavern floor at `(13, 24)` (verified Turn 28082) and at Lv11 (♀, Rock/Ground; knows Rollout) on B1F at `(37, 18)` (caught in a Poké Ball, nicknamed **Vesta**, and sent to Box 1 in Turns 28632-28641).
- **Gulpin**: Encountered at Lv10 (♂, Poison) on the upper terrace at `(29, 20)` (verified Turns 28109-28110).
- **Roggenrola**: Encountered at Lv10 (♀, Rock) on the 1F upper terrace at `(29, 20)` (verified Turns 28112-28114) and at Lv9 (♂, Rock; knows Tackle) on B1F at `(33, 23)` (caught in a Poké Ball, nicknamed **Bolide**, and sent to Box 1 in Turns 28623-28629).
- **Aron**: Encountered at Lv7 (♀, Steel/Rock) at the base of the northern ladder at `(9, 20)` (verified Turn 28327).
- **Zubat**: Encountered at Lv8 (♂, Poison/Flying) near the southern entrance at `(7, 27)` (verified Turn 28332) and at Lv7 (♂, Poison/Flying) at `(6, 28)` (caught in a Poké Ball, nicknamed **Umbra**, and sent to Box 1 in Turns 28659-28662).
- **Whismur**: Encountered at Lv10 (♂, Normal; knows Disarming Voice and Pound) near the southern entrance at `(6, 28)` (caught in a Poké Ball, nicknamed **Quasar**, and sent to Box 1 in Turns 28665-28678).
- **Pawniard**: Encountered at Lv8 (♀, Dark/Steel) on B1F at `(31, 27)` and `(29, 32)` (verified Turns 28726 & 28728).
- **Phanpy**: Encountered at Lv10 (♀, Ground) on B1F at `(26, 28)` and `(25, 23)` (verified Turns 28727 & 28732).
- **Paras**: Encountered at Lv10 (♀, Bug/Grass) on B1F at `(16, 16)` (verified Turn 28730).
- **Drilbur**: Encountered at Lv10 (♀, Ground) on B1F at `(16, 27)` and at Lv11 (♂, Ground) at `(25, 21)` (verified Turns 28731 & 28738).
- **Diglett**: Encountered at Lv11 (♀, Ground; Ability: Arena Trap) on B1F at `(25, 12)` (verified Turns 28733-28735).
- **Tympole**: Encountered at Lv8 (♂, Water) on B1F at `(28, 8)` (verified Turn 28737).
- **Woobat**: Encountered at Lv9 (♂, Psychic/Flying) on B1F at `(16, 17)` (verified Turn 28757).
- **Shellos**: Encountered at Lv10 (♀, West Sea Pink form, Water) on 1F at `(14, 24)` (verified Turn 28781).
- **Mawile**: Encountered at Lv8 (♀, Steel/Fairy) on B1F at `(29, 32)` (verified Turn 29152).
- **Makuhita**: Encountered and caught on 1F at `(11, 24)` (Turn 30006).
- **Mienfoo**: Encountered at Lv6–8 (Fighting) on 1F at `(6, 26-28)` (verified Turns 30538 & 30569).
- **Onix**: Encountered at Lv8 (Rock/Ground) on 1F at `(6, 27)` (verified Turn 30766).
- **Carbink**: Encountered at Lv8 (Rock/Fairy) on the 1F Northeastern Terrace at `(27, 18)` (verified Turn 31342).
- **Dwebble**: Encountered at Lv13 (♂, Bug/Rock) in the Closed Segment Eclite Cavern at `(32, 28)` (verified Turn 31607).
- **Nincada**: Encountered at Lv10 (♀, Bug/Ground) in the Closed Segment Eclite Cavern at `(9, 18)` (verified Turn 31633).

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
  - From the bottom of the pond stairs (`30, 27`), the cavern floor continues south past a 2x2 rock cone (`31-32, 28-29`) and a solid-collision rectangular floor pit (`30-31, 33-35`, verified from `29, 33-35` and `30, 36` via `latest_grid.png` in Turn 28720) along `column 29` (`29, 31 -> 29, 38`, with an inert small rock at `31, 38`).
  - Terraced western cliffs (`cols 23-28, rows 27-37`) feature small rocks at `(26, 31)`, `(27, 32)`, and `(26, 35)`, while the southern corridor wraps west along `row 38` (`cols 20-30`, bounded on the west at `cols 14-19, rows 32-38` by a deep chasm and on the south by a solid-collision rectangular floor pit at `22-24, 39-40`, verified via `latest_grid.png` Turn 28752) and north along `cols 20-22` (`38 -> 32`) onto the southern end of the B1F north-south wooden bridge.
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
- **Western B1F Staircases (`cols 15-17, rows 21-26`), Upper Western Terrace (`cols 15-18, rows 15-20`) & Coworker Garner (`15, 23`)** (`latest_grid.png` Turns 28710-28711):
  - Bounded on the west (`cols 11-14`) by a 3-tier cliff wall and black void and on the north (`row 14`) by an upper cliff wall. Two consecutive wooden staircases (`15-17, 21-22` and `15-17, 25-26`, separated by a landing at `15-17, 23-24`) descend from the Upper Western Terrace (`cols 15-18, rows 15-20`) to the Lower Western Floor (`cols 15-19, rows 27-30`, bounded on the south at `rows 30-31` by a 2-tier cliff wall).
  - **Coworker Garner (`15, 23`, facing East)**:
    - **Pre-Battle Quote**: *"We just finished our clean up works on this level and I have nothing to do... Wanna battle?"*
    - **Team (3 Pokémon)**:
      - **Pokémon 1**: Magnemite (Lv13; Electric/Steel; Ability: Sturdy; knows Thunder Wave).
      - **Pokémon 2**: Machop (♂, Lv13; Fighting; knows Focus Energy).
      - **Pokémon 3**: Geodude (♀, Lv14; Rock/Ground; knows Rock Polish).
    - **Outcome**: Defeat quote: *"My god..."*; awards `₽560` (verified Turns 28179-28188).
- **B1F Underpass (`17, 27 -> 23, 27 -> 25, 25`) & Eastern Staircase (`25-26, 15-18 -> 26, 12`)** (`latest_grid.png` Turns 28711-28712 & 31173-31174; `cols 20-22, rows 21-31` under the bridge have a 0% wild encounter rate and connect north via `20, 27 -> 20, 23 -> 21, 23 -> 21, 21 -> 23, 21` around the north side of the boulder):
  - From the bottom of the lower western stairs (`16-17, 27`), the cavern floor passes underneath the north-south wooden bridge (`cols 20-22, rows 27-31`) to `(23, 27)`, wraps north/east around the 2x2 boulder at `(23-24, 23-24)` via `(23, 25) -> (25, 25)`, and ascends the eastern staircase (`25-26, 18 -> 25-26, 15`) onto the northern B1F platform (`25-26, 14 -> 26, 12`, verified Turns 28190-28192 & 28712).
- **Northern B1F Platform (`cols 23-32, rows 7-14`) & Cave Archway (`29, 7`)**:
  - Bounded on the southwest by the deep chasm (`cols 19-24, rows 13-15`), leads north to a cave archway at `(29, 7)` (`latest_grid.png` Turn 28193), and is sealed off on the east by two 2x2 rock cones at `(31-32, 10-11)` and `(33-34, 11-12)` against a 2-tier boundary cliff wall (`35-38, 9-13`; while the top row of 2x2 cave rock cones such as `31-32, 10` on B1F and `23-24, 33` on 1F has passable `0x00` collision, `32, 10` is blocked on the east at `33, 10` by the solid cliff wall corner and on the south at `31-32, 11` by the rock cone base, verified Turns 28520-28522, 31321 & 31328).
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
  - **Mine Workers & Blocked Passages (`14, 25` & `14, 34`)**: Enclosed on the west (`col 3`), south (`row 34`, with a solid cliff lip at `9-11, 33` above the dark pit `9-11, 34`, verified Turn 31149), and east (`col 16-17`, where `16, 29-30` is a 1-tile wall recess bounded by solid wall at `17, 29-30`, verified Turn 31148) by solid cave walls (`latest_grid.png` Turns 28361-28362, 28517, 28743 & 28939), with inert rock cones at `(9-10, 25-26)`, `(4-5, 30-31)`, `(4-5, 32-33)`, and `(14-15, 28-29)`, an inert small rock at `(6, 32)` on the southwest ledge (`cols 4-7, rows 31-33`), and wooden stairs at `(11, 31-32)` descending from the western upper floor (`cols 5-10, rows 27-33`) to the eastern lower floor (`cols 12-16, rows 29-34`). Although a Worker stands at `(11, 27)`, the upper cliff lip along `row 28` (`(10, 28) -> (11, 28) -> (12, 28) -> (12, 27) -> (14, 27) -> (14, 25)`) is 100% passable, allowing the player to walk directly around the south side of the Worker at `(11, 27)` onto the northern archway ledge (`cols 12-15, rows 25-28`) and enter the northern cave archway at `(14, 25)` (verified Turn 31459). Workers at `(8, 30)` (*"We are doing some work here, kid!"*), `(11, 27)` (*"We are doing some work here, kid!"*), `(13, 29)` (*"We are cleaning up the path to deeper parts of the cave... / We still have a lot of work to do though..."*), `(13, 32)` (*"We are cleaning up the path to deeper parts of the cave... / We still have a lot of work to do though..."*), and `(15, 31)` (*"Ahh, when will we finish this?!"*) alongside a Machop at `(14, 32)` (*"Machop: Chop! Chop!"*) block both the northern exit (`14, 25`) and the boulders/rugged rocks (`13, 33`, `14, 33`, `15, 32`, `13, 34`, `15, 34`) surrounding the floor ladder at `(14, 34)` (all individually verified with no open textboxes in Turn 28938).
- **Northwest Mountain Ridge Exterior (`10, 21` Exit from Lower Pit Chamber `14, 25`)**:
  - Stepping into the northern cave archway at `(14, 25)` in the Lower Pit Chamber exits outside onto the elevated northwest canyon ridge of the **Azluf Town** map at `(10, 21)` below the cave mouth `(10, 20)` (`latest_grid.png` Turns 31461-31468).
  - **Path to Upper Junction (`20, 8`)**: From `(10, 21)`, follow `(10, 21) -> (10, 22) -> (14, 22) -> (14, 17) -> (15, 17) -> (15, 16) -> (17, 16) -> (17, 15) -> (20, 15)` (stepping across the passable top tile `18, 15` of the 1x2 red rock spire at `18, 15-16`), and ascend the wooden staircase at `(19-21, 13-14)` to `(20, 12) -> (20, 8)`.
  - **Upper Junction (`20, 8`) Branches**:
    - **Eastern Branch to Upper Cave Entrance (`29, 5`)**: Extends east along `row 8` across `(22, 8)` and the passable top canopy tile of the cypress tree at `(23, 8)` into `(24-30, 6-8)`, leading directly to a northern cave entrance at **`(29, 5)`** (entered from `29, 6` stepping `Up`, verified Turns 31476-31477).
    - **Western Canyon Trail to Route 2 Eastern Canyon (`79, 44` -> `71, 39`)**: Descends the wooden staircase at `(16, 6-7)` via `(20, 8) -> (17, 8) -> (17, 7) -> (15, 7) -> (14, 7) -> (14, 8) -> (13, 8) -> (13, 10) -> (12, 10) -> (12, 12) -> (10, 12) -> (10, 14) -> (5, 14) -> (5, 20) -> (0, 20)`, where stepping `Left` from `(0, 20)` transitions onto the elevated eastern canyon of **Route 2** at `(79, 44)` and leads to the southern bank (`71, 39-42`) of the Route 2 eastern pond (`70-74, 36-40`, verified Turns 31465-31473).
- **Upper Mt. Gerhana Cave Entrance Cutscene (`29, 5`) & Upper Cave Chamber (`7, 12`)**:
  - **Pre-Entry Cutscene with Valora (`29, 5`, Turns 31477-31479)**: Stepping into `(29, 5)` triggers a cutscene where Valora steps out at `(29, 6)`. Sensing danger (*"Hey... I have a bad feeling... Maybe you should wait for me out here."*), Asher convinces Valora to wait outside (*"Be really careful, Asher. Don't do anything stupid..."*) and enters the cave at `(29, 5)`, arriving at **`(7, 12)`** inside the **Upper Cave Chamber of Mt. Gerhana** (exit archway at `7, 11`, with an eastbound wooden bridge spanning `cols 11+, rows 14-16`).
  - **Eclite Crystal Platform (`cols 25-28, rows 14-19`) & Confrontation with Frio (`24, 15` -> `27, 16`, Turns 31482-31487)**:
    - Crossing the western wooden bridge (`cols 11-24, rows 14-16`, with small rocks at `23, 16` and `24, 14`) and stepping onto `(24, 15)` triggers the confrontation with **Frio** (`27, 16`) in front of the giant purple **Eclite** crystal monolith (`26-28, 12-14`).
    - Frio explains that the crystal and Eclipse Shards are made of **Eclite**, and that Eclipsing is a hereditary power carried in the user's bloodline which Eclite and the Eclipse Band merely channel.
    - When a wild **Aggron** touches the crystal and transforms into a violent **Eclipsed Aggron** (`27, 14`), Asher's inner bloodline power and **Eclipse Band** resonate with the Eclite to calm and revert the Aggron. Stunned, Frio remarks *"You seem way more unique than I actually anticipated. Very well... We will meet again, Asher"* and departs east across the eastern wooden bridge (`cols 29+, rows 16-18`).
    - **Mandatory Post-Frio Eclite Crystal Interaction (`27, 15` facing `27, 14`, Turns 31488-31489)**: After Frio departs east across the bridge, stepping to `(27, 15)` and pressing `A` facing `Up` into the Eclite Crystal (`27, 14`) triggers the mandatory follow-up cutscene where Asher reflects on resonating with the Eclite, feels heavy and exhausted from the bloodline power drain, and collapses on the cave floor, waking up in his bedroom on **Inizio Isle** (`6, 4`) alongside Dad (`7, 4`) and Valora (`5, 5`).
  - **Team Siara Eclite Theft Cutscene & Gauntlet (`18, 15` -> `25, 15`, Turns 31525-31532)**: Returning across the western bridge after Valora's text message in Lancio Town triggers a cutscene at `(18, 15)` where four **Team Siara Grunts** have mined and taken the giant Eclite crystal to deliver to Team Siara HQ for Marie. Recognizing Asher from the Sovio Sewers, the grunts challenge Asher at `(25, 15)`:
    - **Siara Grunt 3 (`26, 15`)**: Uses 2 Pokémon—Duskull (♂, Lv14; Ghost) and Shuppet (♀, Lv14; Ghost); defeat quote: *"Noooo"*; awards `₽1456` and retreats east across the bridge (verified Turns 31527-31531).
    - **Siara Grunt 1 (`27, 14` -> `26, 15`)**: Pre-battle quote: *"Come on, he can't be that strong!"*; uses 1 Pokémon—Mareanie (♂, Lv15; Poison/Water); defeat quote: *"How could this no one pummel me?!"*; awards `₽1560` and retreats east across the bridge (verified Turns 31532-31534).
    - **Siara Grunts (Grunt 2 & Grunt 4 at `26, 15-16`)**: Pre-battle quote: *"Grunt 2 & 4: We will be the ones to take care of you!"*; uses 4 Pokémon—Nidoran♀ (Lv13; Poison), Nidoran♂ (Lv14; Poison), Murkrow (♂, Lv14; Dark/Flying), and Misdreavus (♀, Lv15; Ghost); defeat quote: *"He... / ...defeated both of us!"*; awards `₽1560` (verified Turns 31535-31543; Sirius reached Lv34 and learned Aura Sphere).
    - **Post-Gauntlet Retreat**: After Grunt 2 & Grunt 4 are defeated (*"The eclite is close to the HQ so at least we won time."*), they flee east across the bridge, and Asher deduces they are heading toward **Samurion City** (verified Turn 31543).
  - **Eastern Chasm Bridge (`cols 31-46, rows 16-18`), Eastern Landing (`cols 47-55, rows 16-21`), TM39 Rock Tomb (`43, 9`) & Eastern Exit Archway (`53, 8`)**:
    - Crossing the eastern wooden bridge (`cols 31-46, rows 16-18`) reaches the eastern landing (`cols 47-55, rows 16-21`) and a northbound wooden staircase at `(49-51, 12-15)` leading up to the upper eastern ledge (`cols 43-54, rows 8-11`, verified Turns 31544-31547).
    - **TM39 (Rock Tomb) (`43, 9`)**: Golden item sphere on the western side of the upper eastern ledge (`43, 9`, interacted from `44, 9`; collected Turn 31547).
    - **Eastern Exit Archway (`53, 8` -> Samurion City `39, 65`)**: Located on the northeastern side of the upper eastern ledge (`53, 8`, entered from `53, 9` stepping `Up`); exits directly into **Samurion City** at `(39, 65)` below the cave mouth at `(39, 64)` (verified Turns 31547-31549).

## Closed Segments of Mt. Gerhana (`18, 39` Samurion Western Terrace Entrance)
- **Entry Chamber (`31, 12` Exit Mat <-> Samurion City `18, 39`)**: Stepping into the newly opened northern cave entrance at `(18, 39)` on the Samurion City Western Terrace arrives at `(31, 12)` (`latest_grid.png` Turns 31580-31581). Walking west across the chamber (`31, 12 -> 31, 10 -> 22, 10 -> 22, 12 -> 23, 12`) reaches a floor ladder at **`(23, 12)`** (verified Turns 31581-31582).
- **Eclite Cavern (`30, 10` Ladder Arrival <- Entry Chamber `23, 12`)**:
  - **Team Siara Briefing Cutscene (Turns 31583-31585)**: Descending from `(23, 12)` to `(30, 10)` triggers a cutscene showing the red-haired female Team Siara officer (*"???"*) briefing **Frio** and a grunt on finding the largest Eclite piece in the cavern while grunts collect smaller fragments and guard against intruders; Frio wonders whether Asher will try to stop them from uncovering the truth about their shared ancestors before following the officer south across a wooden bridge.
  - **Northern Corridor (`cols 27-35, rows 10-29`)**: Features purple Eclite crystals embedded in the upper cliff wall (`28-29, 8`) and leads south along `column 30` (`30, 10 -> 30, 19`) past an underground water channel (`25-30, rows 19-28`) to two patrolling **Team Siara Grunts**:
    - **Siara Grunt (`30, 20`, facing East)**: Pre-battle quote: *"H-huh? Isn't this area supposed to be closed from intruders?"*; uses 2 Pokémon—Remoraid (♀, Lv15; Water) and Wartortle (♂, Lv16; Water); defeat quote: *"He really means business!"*; awards `₽1664` (verified Turns 31589-31595).
    - **Siara Grunt (`31, 28` -> `31, 26`, rotating)**: Pre-battle quote: *"What the? Am I seeing things because of spinning around so much?"*; uses 3 Pokémon—Sandshrew (♀, Lv14; Ground), Phantump (♀, Lv15; Ghost/Grass), and Stunky (♂, Lv15; Poison/Dark); defeat quote: *"Noooo, it was real!"* (verified Turns 31597-31604).
  - **Bridge Underpass (`cols 21-23, rows 27-30`) & Western Floor (`cols 7-20, rows 19-32`)**:
    - **Siara Grunt (`20, 25` -> `20, 27`, facing South)**: Guarding the purple Eclite crystal embedded in the cliff wall at `(20, 24)`; pre-battle quote: *"Ahahaha, no no no! This bridge marks your final steps."*; uses 1 Pokémon—Combusken (♂, Lv16; Fire/Fighting); defeat quote: *"I was saying yours, not mine!"* (verified Turns 31609-31611).
    - **Siara Grunt (`16, 27`, rotating)**: Pre-battle quote: *"She didn't stop you? My, my..."*; uses 2 Pokémon—Yamask (♂, Lv15; Ghost) and Gulpin (♂, Lv16; Poison); defeat quote: *"Hooow?"* (verified Turns 31612-31616).
    - **Siara Grunt (`10, 22`, rotating)**: Pre-battle quote: *"This might disappoint you, but I can't let you go more forward!"*; uses 3 Pokémon—Croagunk (♂, Lv15; Poison/Fighting), Drifloon (♂, Lv16; Ghost/Flying; Ability: Aftermath), and Stunky (♂, Lv15; Poison/Dark); defeat quote: *"..."* (verified Turns 31622-31628).
    - **Siara Grunt (`10, 13` -> `10, 15`, facing South)**: Pre-battle quote: *"Don't try to stop us, we can't disappoint Miss Marie!"*; uses 2 Pokémon—Diglett (♀, Lv16; Ground) and Trapinch (♂, Lv16; Ground); defeat quote: *"My god..."* (verified Turns 31635-31640).
  - **Northwestern Eclite Chamber (`cols 7-18, rows 6-14`) & Water Stone (`16, 14`)**:
    - Contains an underground water pool at `(8-10, 9-12)`, a purple Eclite crystal embedded in the northern wall at `(10-11, 6-7)` guarded by two **Team Siara Grunts** at `(10, 8)` and `(14, 8)`, and an eastbound wooden staircase at `(17, 9-11)` ascending onto the central ridge (`cols 18-24`), which connects via a southbound staircase (`19-22, 12`) and lower westbound staircase (`18, 13-15`) to a golden item sphere at **`(16, 14)`** yielding a **Water Stone** (collected Turn 31654; `latest_grid.png` Turns 31635, 31643, 31645 & 31653-31654).
    - **Siara Grunt (`14, 8` -> `14, 9`, facing South)**: Pre-battle quote: *"What the?! What happened to everyone? Weren't there guards all over the place?"*; uses 1 Pokémon—Rotom (Lv17; Electric/Ghost; knows Double Team and Thunder Wave); defeat quote: *"I see..."* (verified Turns 31645-31652).
  - **Central Ridge (`cols 19-24, rows 9-19`), Central Wooden Bridge (`cols 21-23, rows 20-37`) & Southern Bridge Exit (`cols 20-24, rows 38-44`)**:
    - Ascending the eastbound diagonal staircase at `(17, 9-11)` reaches `(19, 9)` beside a purple Eclite crystal at `(20-21, 8-9)` and a northbound wooden staircase at `(22-24, 7-8)` (`latest_grid.png` Turn 31653).
    - Descending the southbound staircase at `(19-22, 12)` reaches the lower central ridge (`cols 19-24, rows 13-19`), which connects south onto the encounter-free **Central Wooden Bridge (`cols 21-23, rows 20-37`)** (`latest_grid.png` Turns 31654, 31657 & 31659).
    - At the southern end of the bridge (`22, 38`), two **Team Siara Grunts** flank the narrow canyon passage at **`(21, 39)`** (facing East) and **`(23, 39)`** (facing West); direct interaction is inert, while stepping onto **`(22, 39)`** triggers a dual confrontation:
      - **Siara Grunts (`21, 39` & `23, 39`, triggered at `22, 39`)**: Pre-battle quotes: *"Grunt 1: You aren't going to pass through here, kiddo! / Grunt 2: Yeah we are turning ya back!"*; uses 4 Pokémon—Elekid (♂, Lv14; Electric), Makuhita (♂, Lv15; Fighting; knows Fake Out), Magby (♂, Lv14; Fire; knows SmokeScreen), and Meditite (♂, Lv15; Fighting/Psychic; knows Detect); defeat quotes: *"Grunt 1: Noooooo! / Grunt 2: How could this happen, it was 2 versus one?"*; awards `₽1560` (verified Turns 31660-31674).
    - **Southern Floor Ladder (`22, 45` -> Deep Eclite Chamber `14, 22`)**: Located 6 tiles south of `(22, 39)` along `column 22` (`latest_grid.png` Turn 31675); stepping onto `(22, 45)` descends into the **Deep Eclite Chamber** at `(14, 22)` (`latest_grid.png` Turn 31676), which immediately triggers a confrontation cutscene where Asher walks up to `(14, 13)` before **Marie ("Mom")**, **Frio**, **Siara Admin Flo** (*"???"*), and three grunts standing in front of a massive prime **Eclite Crystal** (verified Turns 31675-31686):
      - After Asher exposes Marie's plan to weaponize Eclipsing, Marie admits she adopted Frio after her divorce from Jackson, prompting Frio to defect from Team Siara and depart.
      - **Dad (Jackson)**, **Valora**, and **Professor Ivo** arrive to back up Asher and hold off the grunts while **Siara Admin Flo** (`14, 12`) battles Asher (party is automatically healed to full HP/PP and cured of status conditions prior to the battle):
        - **Siara Admin Flo (`14, 12`)**: Pre-battle quote: *"My name is Flo, Miss Marie trusts me the most. So I'll live up to that and take you out!"*; uses 4 Pokémon (plus Super Potion)—Larvesta (♂, Lv16; Bug/Fire), Salandit (♂, Lv16; Poison/Fire; knows Dragon Rage), Trubbish (♂, Lv17; Poison; Ability: Aftermath), and Grovyle (♂, Lv18; Grass; knows Quick Attack); defeat quote: *"Gosh darn it! How could this kid... How dare he!"*; awards `₽2160` (verified Turns 31687-31698).
      - After Flo's defeat, Marie orders Team Siara to retreat (*"Don't worry... I don't need that kid to succeed. My plan... my plan is just about to begin, for now we retreat."*), leaving Asher (`14, 13`), Dad (`14, 15`), Valora (`12, 15`), and Professor Ivo (`15, 16`) before the prime Eclite Crystal (verified Turn 31698).
      - **Post-Battle Cutscene & Auto-Warp to Samurion City (`14, 13` -> `18, 40`, Turns 31699-31704)**: Following Team Siara's retreat, Dad, Valora, Professor Ivo, and Asher discuss Frio's tearful departure, Marie's upcoming plan, and Round 2 of the Eclipse Tournament in Amor City. Asher resolves to head to Amor City via the Samurion City Metro Station, automatically warping outside the western cave entrance in **Samurion City** at `(18, 40)`.

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
- **Yamper**: Encountered at Lv4 (Electric) in the eastern corridor tall grass at `(54, 31)` (verified Turn 28877).

## Landmarks & NPCs
- **Northern Entrance Clearing (`cols 6-15, rows 0-12`)** (`latest_grid.png` Turns 27590-27591):
  - Tall grass patch spans `cols 6-15, rows 6-12`.
  - Wooden signboard at `(12-13, 8)` interacted from `(12, 9)` reads verbatim: *"Route 2 / Careful on the Bridges!"* (verified Turn 27591).
  - **Patrolling Beret Girl (`13-15, 9-12`)**: *"I wonder if I can find a Mime Jr. around here... I heard they are pretty rare."* (verified Turn 27952).
- **Southern Corridor (`cols 12-25, rows 13-25`)** (`latest_grid.png` Turns 27607, 27621-27622 & 31390; includes an enclosed 3x2 grass pocket behind the pine tree canopies at `21-23, 15-16` bounded by solid cliffs at `21, 13-14` and `24, 14-16`, verified Turn 31390):
  - **Lass Karina** at `(15, 17)` facing East (`"Let's have a fun Pokémon battle!"`): Uses Pikachu (♂, Lv8) and Ducklett (♀, Lv8); awards `₽512` and states post-battle: *"That was pretty amazingly fun! You have totally exhausted me..."* (verified Turns 27609-27620).
  - Clear non-grass path runs south along `column 17` (`rows 20-24`) into a horizontal dirt/flower corridor along `row 24` (`cols 12-25`, where the western end at `12, 24` is an enclosed dead end bounded by solid trees at `cols 5-11`, verified Turns 31217-31218).
  - **Bug Catcher Elihaj** at `(20, 24)` (`"Bugs in my net, in my bag, everywhere!"`): Uses 3 Pokémon—Caterpie (♀, Lv7), Venipede (♀, Lv8), and Scatterbug (♂, Lv7); defeat quote: *"They were squashed like a fly!"*; awards `₽364`; post-battle overworld quote: *"You aren't a big fan of insects, are you?"* (verified Turns 27622-27635).
  - **Eastern Stairs & Plateau Entrance (`cols 25-34, rows 20-25`)**: At `(27, 24)`, a wooden staircase at `(28, 23-24)` ascends east onto a sandy plateau (`cols 29+`, where a male NPC stands at `32, 21`). Stepping onto `(27, 24)` triggers a battle with **Picnicker Paul** stationed at `(27, 22)` (*"I just hatched my Pokémon in the Day-Care! Let me show you them!"*): Uses 2 Pokémon—Budew (♂, Lv8) and Swablu (♀, Lv8); defeat quote: *"My babies!"*; awards `₽320` (verified Turns 27635-27645).
- **Pokémon Day-Care Plateau (`cols 29-42, rows 17-25`)**:
  - **Grubbin Breeder** wandering at `(31-32, 20-21)`: *"I'm trying to breed the best Grubbin possible! I hatched so many eggs already..."* (verified Turns 27649-27651).
  - **Pokémon Day-Care Signboard** at `(36, 21)`: Reads *"Pokémon Day-Care"* (verified Turn 27651).
  - **Pokémon Day-Care Entrance** at `(38, 20)` (red-roofed cottage topped with giant Pokémon Eggs):
    - **Interior (`7, 11` exit mat)**: Contains Day-Care Lady at `(7, 7)`, PC terminal at `(10, 8)`, and a male Scientist at `(4, 10)` (*"I'm researching Pokémon Eggs, but no luck so far..."*, verified Turns 27685-27687).
  - **Quest NPC ("Egg Research", Quest #3 — Completed)** at `(40, 21)` directly outside the Day-Care: Female scientist in glasses and lab coat with purple quest bubble. Asks: *"Oh hey! You're a Pokémon Trainer, right? I need your help... You know those rocks that make Happinies evolve? Could you find one for me?"* Gives post-accept hint: *"I heard you can catch Happinies here... They are rare, but they're said to keep those eggs with themselves from time to time. Maybe by catching one, you could get that egg easily..."* (verified Turns 27680-27683; wild Happiny ♀ Lv5 encountered and caught at `52-53, 26` in Turn 29315 alongside wild Shroomish, Bellsprout, Cherubi, and Phanpy). Taking the **Oval Stone** held by the caught Happiny into the Bag (via Someone's PC `Move Items` at `10, 8` inside the Day-Care) and speaking to the scientist at `(40, 21)` completes Quest #3, rewards a **Pokémon Egg** (transferred to Box 1 if the party is full), and causes the scientist to depart (verified Turns 29327-29330).
  - **Northern Staircase & Day-Care Yard (`cols 30-41, rows 12-18`)**: Stone staircase at `(31-33, 17-18)` ascends north from the Day-Care plateau to a small terrace (`cols 30-34, rows 13-16`; bounded on the north by a cliff at `row 12`). At `(35, 15)`, the **Day-Care Man** stands at the gap of the fenced Day-Care yard (`cols 35-41, rows 12-16`), which contains an overworld **Eevee** (`38, 13`) and **Togepi** (`39, 15`) (verified Turns 27689-27691).
  - **Rival Battle with Valora (`37, 22`)**: Stepping onto `(37, 22)` in front of the Pokémon Day-Care triggers a cutscene where **Valora** steps out beside Asher (`38, 22`), admires the Day-Care, and challenges Asher to a 4-Pokémon rival battle to stay sharp for the Eclipse Tournament (verified Turns 27652-27678):
    - **Pokémon 1**: Cleffa (♂, Lv7; Fairy-type; knows Encore, Metronome).
    - **Pokémon 2**: Ralts (♀, Lv8; Psychic/Fairy-type; knows Double Team, Growl).
    - **Pokémon 3**: Mareep (♀, Lv8; pink wool sprite; Electric-type; knows Growl, Tackle).
    - **Pokémon 4**: Popplio (♂, Lv9; Water-type starter ace; knows Water Gun).
    - **Outcome & Post-Battle**: Defeat quote: *"Oh my... I didn't have a chance."*; awards `₽1008`. Post-battle, Asher tells her *"It was a nice battle, but you gotta try harder than that."* Valora replies: *"I knoooow, I'll train more so when Round One comes, I'll be ready to advance through! I'll go ahead now, see ya in Azluf!"* and departs southeast along the pink sand path toward Azluf Town.
- **Central Ridge & Overhead Bridge Underpass (`cols 46-50, rows 24-38`)**:
  - Wooden stairs at `(46, 26)` (with railings at `46, 25` and `46, 27`) ascend east from the Day-Care path onto a rocky ridge (`cols 47-49`, bounded on the north by a solid cliff wall at `48-49, 22` and inert rock cones at `47, 22-23` and `49, 23`, verified Turns 31291-31292).
  - A second set of wooden stairs at `(50, 26)` (with railings at `50, 25` and `50, 27`) descends east from the ridge into the eastern tall grass corridor (`cols 51+`).
  - Walking south along `column 49` (`rows 25-33`) passes east of a boulder (`47-48, 28-29`) and **underneath** the northern overhead wooden bridge (`rows 30-32`) onto a southern ridge overlook (`48-49, 33-35`), which is closed off on the south by solid rock cones at `(48, 36)` and `(49, 34-35)` (`latest_grid.png` Turn 28598, verified Turn 28599; the lower ridge `48-52, 36-40`, stone staircase `50-52, 41-42`, and southeastern Slowpoke pond shore `48-50, 43-47` are reached from the east by walking along `row 46` underneath the Southbound Wooden Bridge `cols 53-55` west of Hiker Franklin at `57, 45`; verified via `latest_grid.png` Turns 28808-28811, with inert rock cones at `50, 37` and `48, 36` and a one-way ledge at `47-52, 47`).
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
      - South of Explorer Ben (`37-39, 59`), a flower-lined path winds south and east around tall grass patches (`37, 59 -> 39, 60 -> 39, 63 -> 46, 63 -> 46, 61 -> 48, 61 -> 48, 58 -> 52, 58`, with inert rock cones at `43, 62` and `47, 56`, verified Turns 28578-28581), while walking west from `(37, 59)` via `(37, 60 -> 26, 60 -> 26, 58)` leads into a closed western tall-grass pocket (`cols 21-25, rows 55-58`) where interacting with the small rock at **`(22, 57)`** yields a hidden **Max Ether x1** (collected Turn 30459).
      - **Picnicker Alice (`53, 58`, facing South)**:
        - **Pre-Battle Quote**: *"Don't you love this place? Its great for picknics."*
        - **Team (1 Pokémon)**: Pansage (♂, Lv11; Grass).
        - **Outcome**: Defeat quote: *"..."*; awards `₽440` (verified Turns 28581-28585).
      - **Northern Pocket & Hidden Green Shard (`46, 52`)**: Walking north from `(48, 58)` through the 4-tile tall-grass strip (`48, 58 -> 48, 54`) reaches a small northern pocket (`46-48, 52-54`) bounded by cliff walls (`46-48, 50-51`); interacting with the bare grass tile at **`(46, 52)`** (from `46, 53` facing Up, west of the rock cone at `47, 52`) yields a hidden **Green Shard x1** into the Items Pocket (verified Turn 28589-28590).
      - **Southeastern Exit Staircase (`62, 61-63`)**: From Picnicker Alice (`53, 58`), the clear grass path continues east (`52, 59 -> 55, 59 -> 55, 60 -> 56, 60 -> 56, 62 -> 61, 62`, past an inert rock cone at `60, 60`, verified Turn 28587) to a wooden staircase at **`(62, 61-63)`** that ascends east onto `(63, 61-63)` in the Lower Clearing of Route 2 (verified Turns 28586-28587).
  - **Southbound Wooden Bridge & Eastern Plateau (`cols 53-70, rows 31-39`)**:
    - **Southbound Wooden Bridge**: Extends south from the eastern corridor at `(53-55, 36+)` (`latest_grid.png` Turn 27718). **Hiker Jerry** stands at `(55, 42)` facing West (`"Ahh a Trainer! Would you fancy a battle?"`): Uses 3 Pokémon—Geodude (♀, Lv9; Sturdy, Rock Polish), Geodude (♂, Lv9; Sturdy, Rock Polish), and Machop (♂, Lv9; Bide); defeat quote: *"Oh no..."*; awards `₽360`; post-battle overworld quote: *"I guess I'll return to hiking and exploring the place!"* (verified Turns 27723-27740).
    - **Lower Southeastern Ledge (`cols 58-62, rows 37-39`)**: Reached via stone staircase at `(59-61, 39-42)`; contains an orange item sphere at `(60, 37)` yielding **Max Repel x1** (collected Turn 27744).
    - **Eastern Plateau (`cols 58-70, rows 31-38`)**: Reached via wooden stairs at `(58, 33-34)`. At `(64, 34-36)`, two dark rugged rocks at `(65, 35)` and `(64, 36)` sit between the cliff (`63, 35-36`) and pine tree (`66-67, 32-34`), blocking the path to an enclosed golden item sphere at `(71, 35)` and small eastern pond (`70-73, 36-39`, verified via `latest_grid.png` and screen Turns 31367-31368).
    - **Southern Bridge Plateau & Staircases (`cols 52-63, rows 47-55`)**: The southbound wooden bridge terminates at `(53-55, 47)` on a rocky plateau (`cols 52-60, rows 48-55`, with a 1x2 rock spire at `54, 49-50` whose top tile `54, 49` is passable and base `54, 50` is solid). Wooden stairs at `(60, 50)` (railing at `60, 51`) descend east to a middle terrace (`cols 61-62, rows 48-52`), and a second set of wooden stairs at `(63, 51)` (railing at `63, 52`) descends east into the lower clearing (`cols 64+`, verified Turns 27741-27742 & 31425).
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
  - Enclosed on the west by the solid 2x2 outdoor boulder at `(36-37, 10-11)` and cliff wall at `(35, 9-10)` (verified solid across all 4 boulder tiles in Turn 31347), and on the south by the Pokémon Day-Care fence (`35-41, 12-16`), pine tree (`41-42, 17-18`), boulder (`43-44, 15-16`), and cliffs (`45+, 15-18`).
  - Contains an inert pale flower patch at `(39, 11)`, an inert blue flower patch at `(40, 10)`, and a sunken rocky basin at `(42-45, 11-13)` (entered via northern stone stairs at `43-44, 10` from `43-44, 9`, with a walkable low southern rim at `43-44, 14` leading onto the southern grass strip `42-45, 14-15`).
  - **Cure Flower (`45, 14`) — Quest #4 ("Medic!")**: When **Quest #4 ("Medic!")** is active, an orange item sphere spawns at **`(45, 14)`** on the southern grass strip below the sunken basin; interacting with `(45, 14)` from `(44, 14)` yields the **Cure Flower** into the Key Items Pocket (verified Turn 28485).

<hr>

<h1><code>Locations/Route_4</code></h1>

# Route 4

## Geography & Connections
- **Two-Segment Vertical Map Structure**:
  - **Route 4 South/Central (`rows 0-60`)**: Connects at the south (`cols 49-51, row 60`) via the northern pagoda gate staircase to **Samurion City** (`cols 25-27, row 0`; verified Turn 31718), and transitions seamlessly at the north (`cols 24-29, row 0`) onto **Route 4 North** (`cols 24-29, row 49`; verified Turn 31874).
  - **Route 4 North (`rows 0-50`)**: Extends north from `(27, 49)` to the **Amor City Gatehouse** at `(30, 16)` and provides the northern overland connection to the eastern purple-sand road (`cols 44-46, rows 0-17` on Route 4 South/Central) leading down to the lost Squirtle's family at `(45, 17)`.
## Wild Pokémon
- **Ducklett**: Encountered at Lv13 (♂, Water/Flying) in the southern tall grass at `(44, 53)` (verified Turn 31722).
- **Patrat**: Encountered at Lv11 (♀, Normal) in the southern tall grass at `(44, 50)` (caught in a Great Ball, nicknamed **Vomor**, and transferred to Box 2 as 53rd Owned species in Turns 31763-31768).
- **Cascoon**: Encountered at Lv12 (♀, Bug) in the tall grass at `(43, 45)` (caught in a Great Ball, nicknamed **Nyx**, and transferred to Box 2 as 54th Owned species in Turns 31770-31778).
- **Litleo**: Encountered at Lv13 (♀, Fire/Normal) in the northern tall grass at `(26, 10)` (verified Turn 31847).
## Trainers & Landmarks
- **Route 4 Signboards**:
  - **Southern Riverbank Signboard (`43-44, 35`)**: Interacted from `(44, 36)`, reads verbatim: *"Route 4 / Road to Amor"* (verified Turn 31784).
  - **Northern Bridge Signboard (`17-18, 22`)**: Interacted from `(18, 23)`, reads verbatim: *"North: Amor City / South: Samurion City"* (verified Turn 31815).
  - **Route 4 North Trainer Tips Signpost (`25, 40`)**: Interacted from `(25, 41)`, reads verbatim: *"Trainer Tips! / Sometimes one area can be sliced up to different segments based on their Pokémon inhabitant variety."* (verified Turn 31878).
  - **Amor City Gatehouse Signboard (`26-27, 15` on Route 4 North)**: Interacted from `(27, 16)`, reads verbatim: *"Amor City / ----->"* (verified Turn 31897).
- **Southwestern Riverside Alcove (`10-14, 38-39`) & Ultra Ball (`14, 39`)**: Golden item sphere at `(14, 39)` yields **Ultra Ball x1** (collected Turn 31797); the riverbank path behind the pine tree tops (`row 38`) terminates at the water edge at `(10, 38)` (verified Turn 31797).
- **Eastern Northern-Riverbank Alcove (`34-39, 20-21`) & Oval Stone (`39, 20`)**: Reached behind the tall grass patch (`31-33, 21`); golden item sphere at `(39, 20)` yields **Oval Stone x1** (collected Turn 31853). Separated from the Squirtle Gang clearing (`cols 42-53, rows 12-19`) by solid pine trees (`36-41, 16-19`).
- **Squirtle Gang Clearing (`cols 42-53, rows 12-19` on Route 4 South/Central) — Quest #5 ("Squirtle Gang", Completed)**:
  - **Verified Route**: Transition north from Route 4 South/Central `(27, 0)` onto Route 4 North `(27, 49)`, follow the flower-lined dirt trail northeast via `(30, 41 -> 30, 35 -> 33, 35 -> 36, 32 -> 40, 28 -> 44, 29)`, and walk south along the eastern corridor (`cols 44-46, rows 29-49`) across the map seam onto Route 4 South/Central `(45, 0 -> 45, 11 -> 46, 13)` through the wooden fence gap at `(45, 11)`.
  - **Event & Reward**: Stepping onto `(46, 13)` reunites the lost Squirtle with four family Squirtles (`44, 14`, `48, 14`, `47, 16`, `45, 17`), who leap into the river together. The quest provider arrives at `(45, 13)` and rewards the **Itemfinder** into the Key Items Pocket, completing Quest #5 (verified Turns 31887-31891). A golden item sphere in the southeastern corner of the clearing at `(53, 17)` yields **TM03** into the TM Case (collected Turn 31892).
- **Small Rocks (`42, 44`, `36, 38`, `32, 35`, `25, 36`, `26, 23`, & `32, 18` on Route 4 South/Central; `30, 34`, `45, 41`, & `47, 48` on Route 4 North)**: Inert (verified Turns 31769, 31785, 31786, 31792, 31822, 31861, & 31879-31886).
- **Black Belt Hamid (`28, 16`, rotating)**:
  - **Pre-Battle Quote**: *"The sound of the river is so relaxing and perfect for training!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Makuhita (♂, Lv17; Fighting).
    - **Pokémon 2**: Sawk (♂, Lv18; Fighting; Ability: Sturdy; knows Counter).
    - **Pokémon 3**: Stufful (♂, Lv18; Normal/Fighting).
  - **Outcome**: Defeat quote: *"Darn..."* (verified Turns 31824-31833).
- **Bug Catcher Montel (`27, 9`, rotating)**:
  - **Pre-Battle Quote**: *"Bug spray ain't gonna protect you from my Pokémon!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Whirlipede (♀, Lv18; Bug/Poison).
    - **Pokémon 2**: Heracross (♂, Lv18; Bug/Fighting; knows Endure).
  - **Outcome**: Defeat quote: *"B-but how?"*; awards `₽936` (verified Turns 31836-31842).
- **Bug Catcher Joel (`43, 50`, rotating)**:
  - **Pre-Battle Quote**: *"Many bugs love water, so I am here to catch some besides the river!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Venonat (♂, Lv16; Bug/Poison).
    - **Pokémon 2**: Beedrill (♀, Lv17; Bug/Poison).
    - **Pokémon 3**: Butterfree (♀, Lv16; Bug/Flying).
  - **Outcome**: Defeat quote: *"Oh nooo!"* (verified Turns 31724-31748).
- **Picnicker Imaan (`42, 42`, facing East)**:
  - **Pre-Battle Quote**: *"Oh boy, time for a battle!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Staravia (♂, Lv17; Normal/Flying; Ability: Intimidate).
    - **Pokémon 2**: Prinplup (♂, Lv17; Water).
  - **Outcome**: Defeat quote: *"Oh my..."* (verified Turns 31779-31783).
- **Lass Sherry (`30, 37`, rotating)**:
  - **Pre-Battle Quote**: *"Ahh the water is sooo beautiful! A perfect background for the sweet victory!"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Corsola (♀, Lv18; Water/Rock).
  - **Outcome**: Defeat quote: *"I meant my victory"*; awards `₽1152` (verified Turns 31789-31792).
- **Wooden River Bridge (`cols 18-20, rows 26-36`), Western Pier (`cols 16-17, rows 31-33`) & Eastern Pier (`cols 21-22, rows 29-30`)**:
  - Spans north across the Route 4 river from `(18-20, 36)` to `(18-20, 26+)`.
  - **Tuber & Big Brother (`16, 32` & `16, 31`)**: Friendly NPCs on the western pier: *"Can I jump in the water, big bro? / Yes, but be careful and stay close!"* (verified Turn 31811).
  - **Fisherman (`22, 28`)**: Friendly NPC on the eastern pier: *"Ahh fishing... / One of the fun and chill activities..."* (verified Turn 31813).
  - **PKMN Trainer Lyra (`19, 34` Bridge Trigger)**: Stepping north onto `(19, 34)` triggers **Lyra** from the Johto region to walk up onto `(19, 35)`, recognize Asher from the Amor City Battle Centre, and challenge him to a friendly 4-Pokémon battle (*"Hehe, I won't hold back!"*, verified Turns 31799-31803):
    - **Pokémon 1**: Marill (♂, Lv16; Water/Fairy).
    - **Pokémon 2**: Vulpix (♀, Lv17; Fire).
    - **Pokémon 3**: Nidorina (♀, Lv17; Poison).
    - **Pokémon 4**: Bayleef (♂, Lv18; Grass).
    - **Outcome**: Defeat quote: *"Oh my... let's hope I'm not gonna need to fight you this round"*; awards `₽2016` (`₽6,182` cash total), heals Asher's party to full HP/PP (*"Wow, that was... intense. Thanks for the quick battle! Here, let me heal your Pokémon. We should both get going now, see ya at the tournament!"*), and departs north across the bridge (verified Turns 31803-31810).
- **Northern Riverbank (`cols 11-39, rows 19-26`)**:
  - Small rock at `(16, 25)` is inert and blocks direct southern access from `(16, 24)` onto the western riverbank strip `(10-13, 26)` (verified Turns 31816-31817 & 31850).
  - **Picnicker Katrina (`24, 20`, facing South)**:
    - **Pre-Battle Quote**: *"Hehe, you can't pass here!"*
    - **Team (2 Pokémon)**:
      - **Pokémon 1**: Roselia (♂, Lv17; Grass/Poison).
      - **Pokémon 2**: Grotle (♂, Lv18; Grass).
    - **Outcome**: Defeat quote: *"..."*; awards `₽720` (`₽6,902` cash total; verified Turns 31818-31822).

<hr>

<h1><code>Locations/Route_6</code></h1>

# Route 6

## Geography & Connections
- **Two-Segment Structure**:
  - **Route 6 Eastern Approach (`cols 0-16, rows 17-19`)**: Connects at the east (`16, 18` <-> Route 6 Gatehouse `1, 7` <-> Amor City `7, 7`, verified Turns 31971-31973) and transitions seamlessly at the west (`0, 17-18`) onto **Route 6 Main** (`69, 37-38`, verified Turn 31975).
  - **Route 6 Main (`69, 37`+)**: Wooden signboard at `(68-69, 36)` (interacted from `69, 37`) reads verbatim: *"Route 6 / The mines just beneath..."* (verified Turn 31976).
## Wild Pokémon
- **Timburr**: Encountered at Lv17 (♀, Fighting) in the upper mining plateau tall grass at `(43, 21)` (caught in a Great Ball, nicknamed **Xyla**, and transferred to Box 2 as 55th Owned species in Turns 32018-32021).
- **Growlithe**: Encountered at Lv16 (♂, Fire; Ability: Intimidate) in the upper mining plateau tall grass at `(38, 23)` (caught in a Great Ball, nicknamed **Pyro**, and transferred to Box 2 as 56th Owned species in Turns 32025-32033).
- **Bunnelby**: Encountered at Lv15 (♀, Normal) in the lower central tall grass at `(38, 28)` (caught in a Poké Ball, nicknamed **Lepus**, and transferred to Box 2 as 57th Owned species in Turns 32056-32059).
- **Swadloon**: Encountered at Lv16 (♀, Bug/Grass) in the lower central tall grass at `(34, 29)` (caught in a Poké Ball, nicknamed **Sylva**, and transferred to Box 2 as 58th Owned species in Turns 32062-32068).
- **Ledyba**: Encountered at Lv20 (♀, Bug/Flying) in the lower central tall grass at `(35, 29)` (verified Turn 32178).
## Landmarks, NPCs & Rival Encounter
- **Eastern Tall Grass Patches (`60-63, 33-36` & `62-66, 27-29`)**: Flanking the eastern dirt road (`cols 56-66, rows 30-37`). A wandering Bug Catcher patrols `(63-65, 28-29)`, and a 1-tile grass pocket at `(65, 26)` terminates at solid pine trees (`64-65, 25`, verified Turn 31980).
- **PKMN Trainer Valora (`58, 30` Cutscene Trigger — Second Rival Battle)**:
  - Stepping west onto `(58, 30)` triggers **Valora** (`57, 30`) to greet Asher, talk about enjoying the Eclipse Tournament while worrying about Team Siara's plan, and challenge Asher to a friendly 5-Pokémon rival battle to see how much they have grown (verified Turns 31981-31996):
    - **Pokémon 1**: Clefairy (♀, Lv21; Fairy).
    - **Pokémon 2**: Kirlia (♀, Lv21; Psychic/Fairy).
    - **Pokémon 3**: Brionne (♂, Lv23; Water).
    - **Pokémon 4**: Flaaffy (♂, Lv22; Electric).
    - **Pokémon 5**: Roselia (♂, Lv21; Grass/Poison).
    - **Outcome**: Defeat quote: *"A loss again... ahhh!"*; awards `₽1,380`.
- **Police Officer (`49, 30`) & Northern Mountain Staircase (`cols 46-48, rows 26-27`)**:
  - Stepping onto `(49, 31)` triggers the cutscene with the **Police Officer** (`49, 30`) and **Valora**, after which Valora joins Asher (`54, 31`) to pursue the lost Team Siara Grunt up the northern staircase (`cols 46-48, rows 26-27`, verified Turns 32003-32007).
- **Upper Mining Plateau (`cols 40-52, rows 18-25`)**:
  - **Mine Warning Signpost (`46, 19`)**: Interacted from `(46, 20)`, reads verbatim: *"Warning! / Collapse of mine is possible!"* (verified Turn 32012).
  - **Route 6 Mine Entrance (`44, 18-19`) & Coworker (`43, 19`) — Quest #7 ("Kaboom", Completed)**: Initially blocked by three rubble piles (`43, 18`, `44, 18`, `45, 19`). Speaking to the Coworker at `(43, 19)` initiates **Quest #7 ("Kaboom")** to find the **Dynamite** he dropped in a patch of sand (accepted Turn 32015). Delivering the Dynamite from `(27, 34)` to the Coworker at `(43, 19)` blasts open the mine entrance at `(44, 18-19)` (*"Fire in the hole!"*) and rewards a **Rocky Helmet** into the Items Pocket, completing Quest #7 and placing the player at `(44, 21)` (verified Turn 32170).
    - **Destino Mine — Route 6 Stone Tower Chamber (`11, 47` -> `11, 54`)**: Stepping north onto `(44, 18)` enters a small subterranean chamber of **Destino Mine** (`cols 8-14, rows 46-56`, exit archway at `11, 46`). Two rock cones at `(9, 47)` and `(13, 47)` are inert, and the southern end of the chamber contains an ancient stone tower structure (`10-12, 53-55`) where interacting with `(11, 53)` from `(11, 52)` reads verbatim: *"It's a stone tower... / It appears to have been built many years ago"* (verified Turns 32172-32175).
  - **Coworker Dario (`37, 22`, facing South)**:
    - **Pre-Battle Quote**: *"I should be working, but I like winning battles against by passing trainer much more!"*
    - **Team (2 Pokémon)**:
      - **Pokémon 1**: Bronzor (Lv21; Steel/Psychic).
      - **Pokémon 2**: Graveler (♀, Lv21; Rock/Ground).
    - **Outcome**: Defeat quote: *"Noooo"*; awards `₽840` (verified Turns 32035-32043).
  - **Southbound Wooden Staircase (`cols 34-36, rows 24-25`) & TinyMushroom (`41, 28`)**: Descends south from `(34-36, 23)` onto the lower central sand landing (`34-36, 26-27`, verified Turn 32023). A golden item sphere at `(41, 28)` behind the pine tree top (interacted from `40, 28`) yields **TinyMushroom x1** (collected Turn 32053).
- **Central & Western Sand Patches & Staircases**:
  - **Northwestern Wooden Staircase (`28-29, 22-23`)**: Ascends north from `(28-29, 24)` toward an upper northwestern sand patch around `(31, 19-21)` (spotted Turns 32023 & 32044).
  - **Wandering Police Officer (`31-33, 28-29`)**: Patrols the lower central clearing below Psychic Hugo (`33, 26`, verified Turn 32070).
  - **Southwestern Sand Patch & Visible Dynamite (`cols 26-28, rows 33-35`)**: Visible in the bottom-left corner from `(33, 29)` with an object sticking out of the center of the sand patch (spotted Turn 32070).
- **Psychic Hugo (`33, 26`, facing South)**:
  - **Pre-Battle Quote**: *"Watch out my PokéBall is floating to you!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Musharna (♂, Lv23; Psychic; inflicts Sleep).
    - **Pokémon 2**: Kadabra (♂, Lv23; Psychic; knows Night Shade and Barrier).
  - **Outcome**: Awards `₽828` (verified Turns 32045-32052).
- **Upper Northern Plateau (`cols 21-41, rows 6-20`)**:
  - **Northbound Wooden Staircase (`cols 27-29, rows 16-17`)**: Ascends north from the rocky mountain ridge crossroads (`28, 20`) to `(28, 15)` (verified Turn 32079).
  - **Trainer Tips Signpost (`35, 16`)**: Interacted from `(35, 17)`, reads verbatim: *"Trainer Tips! / Hidden items might be hiding on the ground unvisible to the eye."* (verified Turn 32081).
  - **Small Rock Cones (`41, 15`, `38, 12`, `32, 19`, `24, 7`, & `20, 14`)**: All verified inert (Turns 32081, 32099, 32164, & 32180).
  - **Hiker Travis (`15, 17`, facing East) & Western Bridge/Terrace Topology**:
    - **Pre-Battle Quote**: *"I heard some criminals were sighted here... / I'm gonna knock each and every one out!"*
    - **Team (1 Pokémon)**:
      - **Pokémon 1**: Gurdurr (♂, Lv25; Fighting).
    - **Outcome**: Awards `₽1,000` (verified Turns 32100-32103).
    - **Elevated Wooden Bridge (`cols 16-18, rows 20-28`) & Southern Cliff Terrace (`cols 9-23, rows 29-36`)**: South of Hiker Travis (`15, 17`), an elevated wooden bridge with solid lateral side-rails spans `rows 20-28` over the intermediate terrace (`cols 10-22, rows 20-26`) and lands on the southern cliff terrace at `(16, 29)` (verified Turns 32104-32106). From the southern cliff terrace, two westbound staircases at `(10, 32-34)` and `(8, 33-35)` descend to `(7, 35)`, connecting north along `col 7` and `row 27` (`cols 7-12`) onto the western intermediate terrace (`cols 7-22, rows 21-27`) and underneath the elevated wooden bridge (`16-18, 24-26`) to the lost Team Siara Grunt at `(21, 24)` (verified Turns 32136-32139). Stepping onto the western sand patch at `(12, 21)` below the northbound staircase (`10-12, 18-19`) displays *"We must deal with that grunt, quick!"* and steps the player `Down 1` to `(12, 22)` until the grunt is defeated (verified Turn 32139). Two eastbound staircases at `(22, 32-34)` and `(24, 33-35)` descend from the southern cliff terrace to the southwestern sand patch (`26-28, 33-35`, verified Turns 32107-32109).
    - **Southwestern Sand Patch & Dynamite (`27, 34`)**: Reached from the southern cliff terrace (`16, 29`) via the two eastbound staircases at `(22, 32)` and `(24, 34)`; the golden item sphere in the center of the sand patch (`27, 34`) yields the **Dynamite** (into the Key Items Pocket) for **Quest #7 ("Kaboom")** (*"This must be the dynamite, that coworker was looking for..."*, collected Turn 32110) and immediately triggers a scripted ambush by a wild **Gible** (♀, Lv20; Dragon/Ground; knows Sandstorm, Sand Tomb, Take Down, and Dragon Rage; verified Turns 32112-32132). Small rock cones at `(14, 31)`, `(15, 34)`, `(18, 33)`, `(23, 36)`, and `(9, 36)` are inert (verified Turns 32108-32109 & 32137).
  - **Youngster Scott (`39, 9`, facing South)**:
    - **Pre-Battle Quote**: *"If you think you can run without a Pokémon Battle, you are very wrong!"*
    - **Team (2 Pokémon)**:
      - **Pokémon 1**: Raticate (♂, Lv23; Normal).
      - **Pokémon 2**: Luxio (♂, Lv24; Electric; Ability: Intimidate; knows Charge).
    - **Outcome**: Defeat quote: *"Oh boy..."*; awards `₽1,248` (verified Turns 32083-32087).
  - **Camper Peter (`26, 5`, facing South)**:
    - **Pre-Battle Quote**: *"Police Officers have raided the place... I wonder why."*
    - **Team (3 Pokémon)**:
      - **Pokémon 1**: Skiploom (♀, Lv23; Grass/Flying).
      - **Pokémon 2**: Spinda (♂, Lv24; Normal).
      - **Pokémon 3**: Floette (♀, Lv24; Fairy; knows Copycat).
    - **Outcome**: Defeat quote: *"Ah whatever..."*; awards `₽1,152` (verified Turns 32089-32097).
  - **Western Item Spheres & Lost Team Siara Grunt**:
    - **Upper Northwestern Item Sphere (`23, 13`)**: Reached via `(26, 6 -> 25, 8 -> 23, 8 -> 23, 12)`; yields **King's Rock x1** (collected Turn 32098).
    - **Middle Western Item Sphere (`23, 21`)**: Reached on the lower grass terrace via `(27, 21 -> 27, 24 -> 25, 24 -> 25, 22 -> 23, 22)` behind the pine tree top; yields **Thunder Stone x1** (collected Turn 32168).
    - **Lost Team Siara Grunt (`21, 24`, facing South)**: Cornered from `(21, 25)` (`-> 20, 24`, Turns 32140-32144); reveals that Team Siara headed to the nearby mining settlement of **Destino City**, and then stops Asher and Valora at `(19, 24)` to battle:
      - **Pokémon 1**: Carvanha (♂, Lv23; Water/Dark; knows Aqua Jet).
      - **Pokémon 2**: Swoobat (♀, Lv24; Psychic/Flying; knows Imprison).
      - **Pokémon 3**: Golbat (♂, Lv24; Poison/Flying; knows Air Cutter).
      - **Pokémon 4**: Purugly (♂, Lv24; Normal).
      - **Outcome**: Defeated in Turns 32145-32154, clearing the patrolling Police Officers from Route 6, unlocking the northwestern sand patch (`12, 21`) and northbound staircase (`10-12, 18-19`), and automatically warping Asher and Valora to `(11, 21)` (verified Turn 32156).
  - **Northwestern Staircase Terrace (`cols 4-12, rows 13-20`) & Upper Destino Road (`cols 0-8, rows 7-12`)**:
    - **Small Rock (`8, 19`)**: Interacted from `(8, 18)`, yields a hidden **Super Repel x1** (collected Turn 32157).
    - **Rock Cones (`8, 15` & `12, 16`)**: Inert (verified Turn 32158).
    - **Upper Northwestern Staircase (`4-6, 13-14`)**: Ascends north from the sand patch (`4-6, 15`) to `(5, 12)` (terminating on the east at trees `cols 9-12, rows 8-12` and leading northwest onto a stone-paved road at `cols 0-1, rows 8-9` that transitions west onto `(-1, 8-9)` into **Destino City**, verified via `latest_grid.png` Turn 32161).

<hr>

<h1><code>Locations/Samurion_City</code></h1>

# Samurion City

## Geography & Connections
- **North (`cols 25-27, row 0`)**: Connects via the northern pagoda gate bridge and staircase (`26, 6 -> 26, 0`) to **Route 4** (`50, 60`; verified Turn 31718).
- **Southwest Mountain Cave (`39, 64` -> Upper Mt. Gerhana Cave `53, 8`)**: Stepping out of the eastern exit archway (`53, 8`) in the Upper Cave Chamber of Mt. Gerhana emerges at `(39, 65)` in **Samurion City** below the cave mouth at `(39, 64)` (verified Turn 31549).
## Southern Pagoda Outskirts (`cols 17-43, rows 65-79`)
- **Southwest Mountain Ridge & Staircase (`39, 65` -> `37, 74` -> `33, 75`)**: From the Upper Mt. Gerhana exit (`39, 65`), a mountain ridge path runs south along `cols 38-40` (`rows 65-75`) to a westbound wooden staircase at `(37, 73-75)` descending into the Southern Pagoda Plaza (`cols 21-35, rows 71-75`, verified Turns 31549-31551).
- **Southern Pagoda Plaza Crossroads (`28-29, 74-75`)**:
  - **East (`cols 30-35, rows 74-75`)**: Connects to the Mt. Gerhana exit staircase (`37, 74`).
  - **West (`cols 21-27, rows 74-75`)**: Leads to a westbound wooden staircase at `(19, 73-75)` ascending onto a western mountain terrace (`cols 17-18, rows 71-78`).
  - **South (`cols 27-29, rows 76-79`)**: Pink sand avenue extending south (with a lower mountain staircase visible at `32, 77` connecting east to `cols 40-43`).
  - **North (`cols 27-29, rows 65-73`)**: Passes underneath an overhead pagoda bridge (`cols 26-30, row 68-69`, where a uniformed officer stands at `27, 68`) between two red pagoda towers (`20-25, 65-72` and `31-36, 65-72`) and ascends a grand wooden staircase (`cols 27-29, rows 66-58`) into the main city (verified Turns 31556-31558).

## Southern Residential Block & Pokémon Center Plaza (`cols 21-36, rows 46-59`)
- **Southern Residential Houses**: Four traditional shoji-door residences flank the central avenue (`cols 27-29`) at `(25, 58)`, `(31, 58)`, `(25, 54)`, and `(31, 54)` (`latest_grid.png` Turn 31559).
  - **Male Resident (`27, 53`)**: *"Are you from somewhere foreign? Because it looks like it. / Samurion is well known for its unique culture after all!"* (verified Turn 31559).
  - **Female Resident (`27, 52`)**: *"Isn't the architecture so beautiful?"* (verified Turn 31559).
- **Samurion City Pokémon Center (`23, 47`) & Town Signboard (`26, 48`)**: Located on the western side of the central avenue northwest of `(28, 50)`, with a wooden signboard at `(26, 48)` (interacted from `26, 49`, reading verbatim: *"Samurion City / The city of Culture"*, verified Turn 31574). Opposite on the eastern side of the avenue sits the **Samurion Dojo (`31, 47`)**, flanked by a wooden dojo signboard (`33-34, 48`) and straw-hat NPC (`36, 48`).
  - **Interior (`7, 8` exit mat -> exits to `23, 48`)**: Nurse Joy at `(7, 2)` (counter at `7, 4`; healed and registered respawn checkpoint in Turn 31570); PC terminal at `(12, 1)` (reached via `row 8 -> col 13 -> 13, 1 -> 12, 1` around the eastern pillar at `11-12, 3-7`); Town Map at `(11, 0)`; wandering Bald Elder around `(5-7, 4-7)`; PokéMart mezzanine staircase in northwest corner (`2, 0`, reached via `row 8 -> col 1 -> 2, 3 -> Up 7` to `5, 5`, clerk at `5, 3`, selling Poké Ball `₽200`, Great Ball `₽600`, Potion `₽300`, Super Potion `₽700`, Antidote `₽100`, Paralyz Heal `₽200`, Awakening `₽250`, Repel `₽350`, verified Turn 31754).
- **Valora Reunion & Samurion Dojo Cutscene (`28, 50` -> `31, 47` -> `6, 5`, Turns 31560-31564)**:
  - Stepping onto `(28, 50)` triggers **Valora** (`28, 49`) to greet Asher and report that she saw **Frio** enter the **Samurion Dojo** (`31, 47`).
  - Asher and Valora automatically enter the Samurion Dojo (`31, 47`) and walk through the foyer into the main hall (`6, 5`), where **Frio** (`5, 4`) is seated beside his sensei, the **Dojo Master** (`7, 4`, flanked by two seated masters at `2, 7` and `10, 9` and four Black Belts at `4, 7`, `4, 9`, `8, 7`, `8, 9`).
  - The Dojo Master identifies Asher as *"the other Eclipser"*, and Frio announces that **Team Siara** has arrived to retrieve more Eclite by making their way into the **closed segments of Mt. Gerhana**. After Frio departs, Asher resolves to call Dad and Professor Ivo and stop Team Siara in Mt. Gerhana, returning outside to `(31, 48)`.
- **Post-Dojo Cutscene & Newly Opened Western Cave Entrance (`30, 48` -> `18, 39`, Turns 31565-31579)**:
  - Stepping onto `(30, 48)` triggers Asher's call to Dad and Ivo and reveals a red-haired female Team Siara commander (*"???"*) and grunt smashing open the 5 rugged rocks blocking a northern **Mt. Gerhana** cave entrance at **`(18, 39)`** on the Western Terrace above the Samurion City Pokémon Center (with a wooden signboard at `20, 40` interacted from `20, 41` reading verbatim: *"Mt. Gerhana"*, verified Turn 31576).
  - **Verified Collision-Free Route Between Samurion Pokémon Center (`23, 48`) & Western Mt. Gerhana Cave (`18, 39`)**: `(23, 48) <-> (23, 49) <-> (28, 49) <-> (28, 40) <-> (26, 40 staircase shifts diagonally to row 39) <-> (21, 39) <-> (21, 41 passable top tip of rock spire) <-> (18, 41) <-> (18, 40) <-> (18, 39)` (verified Turns 31573-31579).

## Northern Boulevard & Plaza (`cols 21-36, rows 15-35`)
- **Frio Cutscene & Round 2 Summons (`28, 26`, Turns 31706-31712)**: Stepping north onto `(28, 26)` alongside the western pink flower garden (`cols 21-26, rows 26-34`) triggers **Frio** to emerge from `(26, 27)` in casual purple attire, recount the 300-year history of the five Samurion Pokémon Tamers who became the first **Eclipsers**, and receive the **Amor Battle Center** text message announcing Round 2 of the Eclipse Tournament and the temporary shutdown of the Hupest Metro Line for maintenance. Frio tells Asher to travel north on foot through **Route 4** to reach Amor City before departing north.
- **Trainer & Lost Squirtle (`33, 25` & `34, 25`) — Quest #5 ("Squirtle Gang", Completed)**: Standing outside the house (`31, 24`) west of the Samurion Metro Station entrance (`37, 24`). Explains: *"Aw poor little guy... Ah hey! You're a Pokémon Trainer, right? You see... this Squirtle has lost its family and I found him all alone on Route 4. Can you help me? No, this poor Squirtle reuniting with it's family? Yes/No"* (verified Turns 31714-31715). Accepting the quest causes the Squirtle (`34, 25`) to accompany Asher and gives the hint: *"I found him by the river in a more closed off, hidden area... I hope you can help him out!"* (accepted Turn 31715; completed at Route 4 `46, 13` in Turn 31891, rewarding the **Itemfinder**).

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

- **Column 30 Causeway & Northeast Wooden Staircase**: Tile (30, 12) is open stone walkway on row 13. Directly north, column 30 is a walkable 1-tile stone causeway across rows 6-12 connecting to the upper platform (`30, 6` is blocked on the north by the doorway wall at `30, 5` and crate at `29, 5`). From `(30, 6)`, step `Right 1` to `(31, 6)`, `Up 2` to `(31, 4)`, and `Left 1` into the east-facing doorway at `(30, 4)` to enter the Dark Sector / Basement at `(31, 9)` (verified Turn 29067).

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
- **Staircase Up**: Located at (31, 9) leading back up to the sewer upper platform (`31, 4`); features a bottom handrail blocking `Up` from `(31, 10)`, so it must be entered by stepping `Right` from `(30, 9)` into `(31, 9)` (verified Turn 29086).
- **Layout & Spatial Geometry**:
  - Eastern corridor (cols 21-30): Northern stone wall at row 8, corridor along row 9 with stairs up at (31, 9) and stone stairs north to upper alcove at (23, 8). Rugged rock obstacle at (22, 10). Row 8 across columns 18-20 connects the eastern corridor (at 21, 9 -> 20, 8) to the western corridor (at 17, 8).
  - Western corridor & alcove (cols 13-17): Northern stone wall is at row 7. Row 8 is a walkable corridor connecting columns 13 to 17. Western boundary terminates at solid wall at column 12 (rows 8-9). Southern boundary at row 10.
  - Red capsule mat at (14-15, 9); stepping Down from (15, 9) warps to Deep Subterranean toy room (2, 38). Row 9 (`14, 9 <-> 23, 9`) is a straight open horizontal corridor connecting the western alcove directly to the eastern corridor (verified Turn 31250).
- **Staircase North**: Stone staircase at (23, 8) ascends to an upper 3x3 treasure alcove (columns 22-24, rows 3-5). Verified 100% inert perimeter walls (north row 2 across cols 22-24, west col 21, east col 25). Single-purpose treasure room.
- **Southeastern Corridor & Southern Stone Staircase (25, 11-13)**: Row 10 is walkable cobblestone floor from `(32, 10)` west to `(23, 10)`. At `(25, 11-13)`, a 1-tile stone staircase (flanked by stone railings at cols 24 and 26) descends south to a lower Dark Sector floor at `(25, 14-15)`.
  - **Lower Southern Corridor & Frio's Chamber Warp (26, 23)**: From `(25, 14-15)` (bounded east by wall at col 26), the corridor runs west along rows 14-15 to `(21, 14-15)` (rugged rock at `21, 16`), then south along columns 21-23 across rows 16-23 (rugged rocks at `23, 20` and `21, 23`), and east along rows 22-23 across columns 23-28 (where `cols 27-28, rows 21-23` form a 2x3 dead-end corner enclosed by solid walls at `row 20`, `col 29`, and `row 24`, verified Turns 31244-31251). At `(26-27, 23)` on the southern wall is a red capsule warp mat; stepping `Down` from `(26, 23)` or `(27, 23)` warps into the **Southern Subterranean Chamber** at `(32, 38)`.
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

## Upper Mt. Gerhana — The Eclite Crystal, Eclipsed Aggron & Asher's Bloodline Awakening
- **Valora Waits Outside (`29, 5`, Turns 31478-31479)**: At the upper cave entrance of Mt. Gerhana (`29, 5`), Asher sensed danger (*"Hey... I have a bad feeling... Maybe you should wait for me out here."*) and convinced Valora to stay outside at `(29, 6)` so she wouldn't be dragged into unnecessary danger (*"Be really careful, Asher. Don't do anything stupid..."*).
- **Frio & The Giant Eclite Crystal (`24, 15` -> `27, 16`, Turns 31482-31484)**: Inside the Upper Cave Chamber, Asher crossed the western chasm bridge to find **Frio** standing before a massive purple monolith (`26-28, 12-14`). Frio revealed:
  - **Eclite**: The giant crystal—as well as smaller fragments known as **Eclipse Shards**—is composed of a mineral called **Eclite**, which initiates the Eclipsing process.
  - **The Bloodline Requirement**: Frio laughed at the idea that anyone could use Eclipsing with just Eclite and an accessory: *"Eclipsing is a power that lays inside the user. These just channel the said power. This power is in the user's veins, in their bloodline. Simply... If you aren't worthy of the power, if you aren't chosen for it, you cannot use it... If you don't have it in you, you can't tap into its potential."*
- **The Eclipsed Aggron & Asher's Awakening (Turns 31484-31487)**:
  - A violent tremor shook the cavern and dimmed the light as a wild **Aggron** emerged from the Eclite crystal (`27, 14`) and transformed into a rampaging **Eclipsed Aggron** from direct contact with the Eclite.
  - While Frio urged Asher to run because neither of them could handle such a powerful Eclipse form yet, Asher felt a familiar inner power awaken (*"I have a weird feeling... It feels familiar, yet so new..."*). Surrounded by a crimson aura, **Asher's Eclipse Band resonated with the Eclite**, calming the Eclipsed Aggron and reverting it to normal before it returned into the crystal.
  - Shocked (*"H-how did you do that? (No... he isn't supposed to...)"*), Frio realized Asher possesses the bloodline power of Eclipsing (*"Very interesting... You seem way more unique than I actually anticipated. Very well... We will meet again, Asher"*) and departed east across the chasm bridge (`cols 29+, rows 16-18`).
- **Eclite Exhaustion Collapse & Inizio Isle Bedroom Reunion (`27, 15` -> `6, 4`, Turns 31488-31493)**:
  - Interacting with the Eclite Crystal (`27, 14`) after Frio's departure causes Asher to reflect on being worthy of the Eclipsing power before collapsing from severe exhaustion (*"Agh, why do I feel so tired! My body feels heavy... I feel... really... exhausted..."*).
  - Asher wakes up in his bed on **Inizio Isle** (`6, 4`) with **Dad** (`7, 4`) and **Valora** (`5, 5`). Valora explains that after feeling the tremor outside the upper cave, she ran inside, found Asher unconscious, and called Dad from Asher's HuPhone to bring him home immediately.
  - After Asher recounts everything Frio revealed about **Eclite**, the Eclipsed Aggron, and how Asher reverted it, Asher urges Dad to visit **Professor Ivo's Laboratory** in Lancio Town (*"Dad! We should head to Ivo's place! ... I need to tell her every information Frio provided."*). Realizing Ivo already told Asher about her past, Dad agrees (*"So she told him about her past... I guess I have no choice. You should rest a bit first, gain some energy and then we will pay her visit, okay?"*) and heads downstairs.
  - Before Valora leaves the room, Asher stops her to thank her for worrying about him, and Valora makes him pinky-promise not to put himself in such reckless danger again.

## Lancio Town — Professor Ivo's Basement Laboratory, The Eclicizer & Gift Eclipsed Pidgey
- **True vs. Artificial Eclipsing (Turns 31498-31501)**: After resting for 12 hours on Inizio Isle and sailing to the Lancio Town dock (`33, 25`), Asher met Professor Ivo in her East Research Wing (`20, 6`), and she led him down the previously blocked foyer stairs (`12, 7`) into her **Basement Laboratory** (`11, 16`) where Dad (`11, 17`) and Valora (`11, 15`) were waiting. When Dad asked how Siara used Eclipsing despite the bloodline requirement, Ivo explained that Siara's method is **Artificial Eclipsing** (*"a mere copy of what this power originally is"*), whereas **true Eclipsing** requires a worthy bloodline wielder (currently only Asher and Frio are known).
- **The Eclicizer (`11, 12-14`, Turns 31501-31502)**: Professor Ivo unveiled a machine she built called the **Eclicizer**, which has two functions:
  1. Restores powerless **Clear Shards** (clear Eclite crystals that look like normal crystals) into active **Eclite Shards**.
  2. Combines small, weak **Eclite Pieces** into a single fully powered **Eclite Shard**.
- **Controlled Eclipsing Experiment & Gift Eclipsed Pidgey (Turns 31502-31504)**: Using an **Eclite Shard** provided by Ivo, Asher Eclipsed a **Pidgey** on command and stayed conscious afterward, showing his body is slowly adapting to the energy drain. Ivo gifted the **Eclipsed Pidgey** to Asher (Turn 31504) to help him train (automatically sent to PC Box 1 because all 6 party slots were full, bringing Owned Pokédex species to `52` and cash to `₽4632`, verified Turn 31553).
- **Professor Ivo's Private Request (Turn 31505)**: After Dad and Valora stepped outside to wait, Ivo privately asked Asher to train himself, become a strong Trainer, and master Eclipsing to counter whatever Team Siara is planning, suggesting he can also gather Eclite from the giant Eclite crystal in **Mt. Gerhana**.
- **Valora's HuPhone Message & Fast-Travel to Azluf Town Border (`21, 14` -> Route 2 `77, 59`, Turn 31508)**:
  - Stepping onto `(21, 14)` outside Professor Ivo's Laboratory in Lancio Town triggers a text message from **Valora**: *"Hey! Your dad had to go take care of some business, so he left, and I set off to Samurion City. Let's meet up there!"*
  - Recalling that **Samurion City** connects to Azluf Town through **Mt. Gerhana**, Asher decides to check on the **Eclite** crystal in Mt. Gerhana on the way there, and the game automatically fast-travels Asher to **`(77, 59)`** at the eastern end of Route 2 outside Azluf Town.

## Upper Mt. Gerhana — Team Siara Steals the Eclite Crystal
- **Theft of the Eclite Crystal (`18, 15` -> `25, 15`, Turns 31525-31543)**: Upon returning to the Upper Cave Chamber of Mt. Gerhana on the way to Samurion City, Asher found four **Team Siara Grunts** standing where the giant purple Eclite crystal had been (`26-29, 14-18`), having mined and taken the entire crystal to deliver it to **Team Siara HQ** on **Marie**'s ("milady") orders. Recognizing Asher from the Sovio Sewers, Grunt 3 (`26, 15`), Grunt 1 (`27, 14`), and Grunts 2 & 4 (`26, 15-16`) battled Asher in a 3-battle gauntlet before retreating east across the chasm bridge.

## Samurion City — Reunion with Valora, The Samurion Dojo & The Eclipsers
- **Reunion with Valora Outside the Pokémon Center (`28, 50`, Turns 31560-31562)**: After Asher defeated the four Team Siara Grunts in Upper Mt. Gerhana and emerged into Samurion City (`39, 65`), he met **Valora** at `(28, 50)`. Asher told her that Team Siara grunts stole the Eclite crystal from Mt. Gerhana, and Valora revealed that she saw **Frio** enter the **Samurion Dojo** (`31, 47`).
- **The Samurion Dojo, The Dojo Master & "Eclipsers" (`31, 47` -> `6, 5`, Turns 31562-31564)**:
  - Inside the Samurion Dojo, Asher and Valora found **Frio** (`5, 4`) seated beside the **Dojo Master** (`7, 4`), whom Frio addressed as *"sensei"*.
  - When Frio introduced Asher (*"He's the kid I was talking about."*), the Dojo Master remarked: *"The other Eclipser? So there's another..."*—revealing that people who possess the hereditary bloodline power to channel Eclite are called **Eclipsers**.
  - **Team Siara Opens the Closed Segments of Mt. Gerhana**: Suddenly sensing Team Siara's arrival, Frio announced: *"Who else but Siara? We will retrieve more Eclite. And for that we gotta make our way into the closed segments of Mt. Gerhana. I'm off now, thank you sensei for your time."* and departed toward Mt. Gerhana.
  - Determined to stop Team Siara from seizing more Eclite in the deeper segments of Mt. Gerhana, Asher told Valora: *"I'm gonna call Dad and Ivo. We gotta go and stop Siara, now!"* before stepping outside the Samurion Dojo to `(31, 48)`.
- **Team Siara Smashes Open the Western Samurion Cave Entrance to Mt. Gerhana (`30, 48`, Turns 31565-31566)**:
  - Stepping west onto `(30, 48)` outside the Samurion Dojo triggers a cutscene where Asher calls Dad and Professor Ivo.
  - Meanwhile, immediately west of the Samurion City Pokémon Center, a red-haired female Team Siara officer (*"???"* / *"madam"*) and a grunt smash away five rugged rocks blocking a northern cave entrance into the closed segments of **Mt. Gerhana** (*"Alright, time to smash the last pieces our roadblock... Yes, now we can start the operation... Call all units!"*).
  - Asher tells Valora to wait in Samurion City until Dad and Professor Ivo arrive while he goes ahead into the newly opened cave to see how big the situation is (*"Uhh, alright, but be very careful, okay?"*).

## Closed Segments of Mt. Gerhana — Team Siara Briefing & Frio's Shared Ancestry Hint
- **Team Siara's Eclite Operation (`23, 12` -> `30, 10`, Turns 31582-31585)**: Upon descending the floor ladder at `(23, 12)` inside the newly opened Samurion cave entrance of Mt. Gerhana, a cutscene shows the red-haired female Team Siara officer (*"???"*) briefing **Frio** and a grunt:
  - `???`: *"Let's go over this once again... Our job is to find the largest Eclite piece that is said to be located around here."*
  - When Frio asks about the smaller fragments and warns that Asher will show up, the grunt says they will collect the smaller fragments and guard the area from intruders, while the officer remarks: *"Don't worry about the kid, Frio... He won't even reach us."*
  - **Shared Eclipser Ancestry**: Before following the officer south across the wooden bridge, Frio thinks to himself: *"I wonder... Will you come and stop us, Asher? Will you really try to stop us from uncovering the truth about your... no, our ancestors?"*—revealing that Frio and Asher share Eclipser ancestors.

## Deep Eclite Chamber of Mt. Gerhana — Frio's Adoption Revelation, Defection & Showdown with Siara Admin Flo
- **Marie ("Mom") & The Prime Eclite Crystal (`22, 45` -> `14, 22` -> `14, 13`, Turns 31675-31678)**: Descending the southern floor ladder at `(22, 45)` into the Deep Eclite Chamber (`14, 22`) triggers a confrontation at `(14, 13)` before **Marie ("Mom")**, **Frio**, the red-haired Team Siara officer, and three grunts standing in front of a massive prime **Eclite Crystal**.
- **Frio's Adoption & Defection from Team Siara (Turns 31678-31685)**:
  - When Asher addresses Marie as *"Mother"*, Frio is stunned and calls Marie *"Mom"*, unaware of Asher's existence.
  - Asher exposes Marie's past: that she was married to Asher's father (Jackson), worked on Eclipsing with him, and drove Jackson to leave Siara with Asher when she insisted on weaponizing Eclipsing.
  - Confronted by Frio (*"...Am I... adopted, by chance?"*), Marie admits that Frio's biological parents died when he was a baby and that she adopted him after her divorce from Jackson.
  - Realizing that Marie lied to him about preserving Eclipser heritage to protect people and Pokémon and only adopted and used him as a tool to weaponize Eclipsing, Frio renounces Marie (*"...You are not my Mother! You just used me for your selfish desires, you lunatic! ... As an Eclipser my duty isn't to dominate people. As an Eclipser I'm supposed to do what's right for the people."*) and defects from Team Siara (*"I'm done with Siara. Good luck progressing without me!"*).
- **Arrival of Dad, Valora & Professor Ivo & Boss Battle with Siara Admin Flo (Turns 31685-31698)**:
  - After Frio departs, Marie's most trusted red-haired commander introduces herself as **Siara Admin Flo** and steps up (`14, 12`) to eliminate Asher.
  - Just in time, **Dad (Jackson)**, **Valora**, and **Professor Ivo** arrive behind Asher to hold off the Team Siara grunts while Asher battles and defeats **Siara Admin Flo** (who uses Larvesta Lv16, Salandit Lv16, Trubbish Lv17, and Grovyle Lv18).
  - **Team Siara's Retreat**: Following Flo's defeat, Marie orders a retreat, telling Flo: *"Don't worry... I don't need that kid to succeed. My plan... my plan is just about to begin, for now we retreat."* before vanishing with Flo and the grunts, leaving Asher, Dad, Valora, and Professor Ivo before the prime Eclite Crystal (`14, 13`).
- **Post-Battle Discussion & Departure for Amor City (`14, 13` -> Samurion City `18, 40`, Turns 31699-31704)**:
  - After Team Siara's retreat, Valora shared that she, Dad, and Professor Ivo bumped into Frio leaving the cave in tears.
  - Professor Ivo noted that Marie mentioned a plan about to begin and no longer needing Frio, while Asher resolved to get answers from Frio about Eclipsing.
  - Dad reminded Asher and Valora that Round 2 of the Eclipse Tournament is starting soon in Amor City, and Asher suggested taking the Samurion City Metro Station back to Amor City (*"Alright, let's head to Amor City! I heard this city has a Metro station."*), automatically warping outside the western Mt. Gerhana cave entrance in **Samurion City** at `(18, 40)`.

## Samurion City Boulevard — Frio's History of the Five Eclipser Tamers & Route 4 to Amor City
- **Frio's New Attire & Search for His Parents (`28, 26`, Turns 31706-31708)**: Emerging from the Samurion City flower garden (`26, 27`) in casual purple clothes after ditching his Team Siara uniform, Frio tells Asher that he is still competing in the Eclipse Tournament and intends to find out who his biological parents really were through their connection to the Eclipsers.
- **The Five Tamers of Samurion & Origin of the Eclipsers (Turns 31708-31710)**:
  - Frio recounts how the chaos of The Great Eclipse 300 years ago was stopped: when the meteorite exploded and scattered **Eclite** across Hupest, **Samurion City** was the only safe zone for people and Pokémon due to its walls.
  - Five brave **Pokémon Tamers** from Samurion City stood up to fight the Eclipsed Pokémon, discovered the source of the phenomenon (Eclite), and became the first **Eclipsers**—able to channel Eclite naturally to control and revert Eclipsed Pokémon.
  - After resolving the chaos, the five warriors swore to protect the innocent and passed their bloodline power and knowledge down through generations so there would always be people to protect it from evil hands, making Asher and Frio descendants of those nameless heroes.
- **Amor Battle Center Round 2 Summons & Metro Maintenance (Turns 31710-31712)**:
  - Both Asher and Frio simultaneously receive a text message on their HuPhones from the **Amor Battle Center**: *"Dear Contestant! The second round of the Eclipse Tournament is going to start in a few hours. We are sending this message way before the event because due to maintence, the metro lines aren't functioning. We want to assure everyone is notified in time so that they won't be late! Good luck, Pokémon Trainer! - Amor Battle Center"*.
  - Frio informs Asher that **Amor City** can be reached easily on foot from Samurion City by passing north through **Route 4**. When Asher offers to help Frio find his parents, Frio remarks that while Asher is no longer the antagonist in his life, they are still rivals rather than friends before heading north toward Route 4.
## Route 4 River Bridge — Friendly Match with Lyra from Johto
- **Lyra's Challenge (`19, 34`, Turns 31799-31810)**: On the wooden bridge spanning the Route 4 river, **Lyra** from the Johto region recognized Asher from the Amor City Battle Centre registration and challenged him to a friendly 4-Pokémon match (Marill Lv16, Vulpix Lv17, Nidorina Lv17, Bayleef Lv18). After Asher swept her team, Lyra healed his party (*"Wow, that was... intense. Thanks for the quick battle! Here, let me heal your Pokémon."*) and headed north toward Amor City (*"We should both get going now, see ya at the tournament!"*).
## Eclipse Tournament Round Two — Victory Over Cheryl & Valora's Route 6 Summons
- **Round Two Bracket & Matches (Turns 31914-31953)**: Inside the Amor City Battle Centre's Round 2 Arena (`13, 17`), Asher competed in an 8-trainer single-elimination bracket on the holographic cyber-arena stage:
  1. **Quarterfinals**: Defeated **Picnicker Raginald** (Swadloon Lv19, Lombre Lv19, Ivysaur Lv20).
  2. **Semifinals**: Defeated **Lass Stacy** (Flaaffy Lv20, Palpitoad Lv20, Purugly Lv20), while Sinnoh's **Cheryl** defeated Worker Josh on the opposite side of the bracket.
  3. **Round Two Finals**: Defeated **PKMN Trainer Cheryl** from the Sinnoh Region (Drifloon Lv20, Wailmer Lv20, Plant Cloak Wormadam Lv20, Chansey Lv21) to win his Round Two group and advance to Round Three of the Eclipse Tournament.
- **Valora's HuPhone Text Message (`9, 26`, Turns 31955-31956)**: Upon returning to the Lower Arena Concourse (`9, 26`), Asher received a text message on his HuPhone from **Valora**: *"I heard your Round took a bit longer than for everyone else, so I decided to train a bit on Route 6 in the meantime. I passed so I'm still going strong! Let's meet up at Route 6!"*.
## Route 6 — Rival Match with Valora & The Escaping Team Siara Grunt
- **Second Rival Battle with Valora (`58, 30`, Turns 31981-31996)**: On Route 6, Valora told Asher she was also enjoying the Eclipse Tournament despite worrying about Team Siara's plan, and challenged him to a 5-Pokémon rival battle (Clefairy Lv21, Kirlia Lv21, Brionne Lv23, Flaaffy Lv22, Roselia Lv21) to test their growth.
- **Police Officer & Team Siara Grunt Cutscene (`49, 30-31`, Turns 31996-32007)**:
  - Immediately after the battle with Valora, a **Police Officer** (`49, 30`) further west on Route 6 shouted *"Freeze!"* at a **Team Siara Grunt** who had lagged behind the rest of a Team Siara group. When the officer demanded to know where the gang went and tried to arrest him, the grunt shouted *"L-look! A donut truck!"* to distract the officer and bolted north up the mountain staircase (`cols 46-48, rows 26-27`).
  - Stepping onto `(49, 31)` triggers Asher and Valora to question the Police Officer, who explains that thugs in dark uniforms and masks have banded together and are causing trouble in the area. Stepping back to `(54, 31)`, Asher and Valora resolve to track down and catch the lost Team Siara grunt to get information out of him, and Valora joins Asher to head up the northern staircase.
- **Interrogation of the Lost Team Siara Grunt & Destino City Lead (`20, 24`, Turns 32140-32143)**:
  - On the western intermediate terrace of Route 6 (`20, 24`), Asher and Valora cornered the lost Team Siara Grunt (`21, 24`), who panicked and admitted that Marie had warned Team Siara about Asher.
  - Begging to be spared as a straggler who got left behind, the grunt revealed that he overheard his companions talking about *"mines and the city laying nearby"*.
  - Valora recalled that the nearby city, **Destino City**, is a mining settlement, and concluded that Team Siara must have headed to **Destino City**. As Asher and Valora turned to leave (`19, 24`), the grunt tried to stop them with a 4-Pokémon team (Carvanha Lv23, Swoobat Lv24, Golbat Lv24, Purugly Lv24), which Asher swept with Sirius (Turns 32144-32154).
## Destino City & Destino Mine Investigation
- **Arrival in Destino City & Entrance to Destino Mine (`59, 20` -> `39, 28` -> `47, 9`, Turns 32183-32204)**:
  - Arriving in **Destino City** ("The industrial mine city") from Route 6 (`59, 20`), Asher found the Destino Metro Station (`45, 14`) closed for renovation and the western city street (`34, 20`) gated until investigating the **Destino Mine**.
  - Descending the diagonal stone staircase (`36, 23` -> `30, 26`) to the southern mining plaza and entering the main **Destino Mine** (`39, 28` -> `47, 9`), Asher and Valora noted there was no visible trace of Team Siara at the entrance. Asher reasoned that the Route 6 grunt wouldn't have fought to stop them if he had given a false location, and Valora suggested heading deeper into the mine to find Team Siara's operation.
- **Team Siara Rockfall Cutscene (`24, 40`, Turns 32287-32292)**:
  - Upon reaching `(24, 40)` on the western side of Destino Mine 1F, Asher and Valora spotted four **Team Siara Grunts** ahead (`26, 35`, `27, 36`, `27, 31`, and `26, 30`).
  - Declaring *"Alright, let's start the operation!"*, the two northern grunts ascended onto the overhead wooden bridge and triggered a rockfall (`24-29, 33-35`) to seal the northern ground passage against *"that blondie"* (Frio) and *"the hair dyed kid"* (Asher).
  - However, the two southern grunts realized they had accidentally stood on the wrong side of the rockfall and locked themselves out of their own operation. Calling them morons, the two grunts on the upper bridge went ahead to get help while leaving the two stranded grunts at `(23, 35-36)`—simultaneously clearing the two Machop that had been blocking the eastern staircase at `(26, 39-41)`.
- **Frio's Arrival & Clearing the Rockfall (`26, 36` -> `26, 35`, Turns 32295-32308)**:
  - Examining the rockfall at `(26, 36)` prompted **Frio** to arrive from the south (`25, 35`), explaining that after passing Round 2 of the Eclipse Tournament he heard Team Siara was planning something in Destino City.
  - Frio smashed open the center of the rockfall (`26-27, 33-34`) under the wooden bridge, causing the two stranded Team Siara Grunts to rush over (`25, 35-36`). Calling Valora *"Smurfette"*, Frio left the two grunts to Asher and Valora while he went ahead north under the wooden bridge (`26, 30`). Asher defeated his grunt (`25, 35`; Mightyena Lv24, Toxicroak Lv25, Haunter Lv24) while Valora handled the second grunt (`25, 36`).

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
    3. Egg Research (Completed in Turn 29330 — caught a wild Happiny holding an Oval Stone at Route 2 `52-53, 26`, moved the Oval Stone to the Bag via the Day-Care PC `10, 8`, and delivered it to the scientist at Route 2 `40, 21`; rewarded a **Pokémon Egg** sent to Box 1; **7 Poké Balls** remaining and **12 Owned species** in PokéDex)
    4. Medic! (Completed in Turn 28495 — delivered Cure Flower from Route 2 `45, 14` to Old Gentleman at Azluf Town Lighthouse `52, 5`; rewarded **Exp. Share**)
    5. Squirtle Gang (Completed in Turn 31891 — reunited the lost Squirtle from Samurion City `33, 25` with its family at `(46, 13)` on Route 4 South/Central via the eastern southbound branch `cols 44-46` of Route 4 North; rewarded **Itemfinder**)
  - **Page 2 Quests**:
    6. Lost Eevee (Active — accepted from Explorer at Destino Mine 1F `42, 12` in Turn 32207; find his missing partner Eevee "Evy" on the second level of Destino Mine)
    7. Kaboom (Completed in Turn 32170 — found the lost Dynamite in the southwestern sand patch at Route 6 `27, 34`, defeated the ambushing Lv20 Gible, and delivered the Dynamite to the Coworker at Route 6 `43, 19` to blast open the collapsed Route 6 mine entrance at `44, 18-19`; rewarded **Rocky Helmet**)
    8. Valentines Gift
    9. Angry Cubone Kid
    10. Push it!
  - **Page 3 Quests**:
    11. Oak's Research (Special Quest — accepted at Azluf Town `40, 7` in Turn 28501; Task 1 [10 Pokémon caught] completed in Turn 28681, rewarding **Bulbasaur**; Task 2 [25 Pokémon caught] completed in Turn 29958, rewarding **Charmander**; Task 3 [45/50 Pokémon caught] completed in Turn 31043, rewarding **Squirtle** and bringing Owned species to **51 Hupest / 20 Colen**; Professor Oak now states *"Thank you, this will be enough, but come back later, I might have some more tasks for you!"* and `Quest Status` reports *"You aren't doing any Quest currently..."*, while `Page 3 -> 11. Oak's Research` still displays *"This Quest hasn't been completed yet."*, verified Turns 31045-31051)
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

- **Items Pocket (Audited Turn 32271)**: Contains **Destiny Knot x1** (received from Professor Ivo in Lancio Town at 50 Owned species in Turn 31109), **Water Stone x1** (collected at `(16, 14)` in the Closed Segment of Mt. Gerhana in Turn 31654), **Thunder Stone x1** (collected at Route 6 `23, 21` in Turn 32168), **Rocky Helmet x1** (rewarded at Route 6 `43, 19` for completing Quest #7 "Kaboom" in Turn 32170), **Repel x0**, **Super Repel x8** (purchased 10 at Destino City PokéMart in Turn 32192, used 1 at Destino Mine `27, 48` in Turn 32271 and 1 at `37, 15` in Turn 32367), **Super Potion x5** (used 2 at Destino Mine 2F in Turns 32390 & 32394), **Oval Stone x1** (collected at Route 4 `39, 20` in Turn 31853), **TinyMushroom x1** (collected at Route 6 `41, 28` in Turn 32053), **King's Rock x1** (collected at Route 6 `23, 13` in Turn 32098), **Red Shard x1** (collected at Destino Mine `40, 13` in Turn 32208), and **Fire Stone x1** (collected at Destino Mine 2F `29, 21` in Turn 32381).
- **Key Items Pocket (Audited Turn 32170)**: Contains **HuPhone**, **TM Case**, **Metro Pass**, **Eclipse Band**, **Fishing Rod**, **Rare Opal** (retained in Key Items after completing Quest #18), and **Itemfinder** (rewarded at Route 4 `46, 13` for completing Quest #5 in Turn 31891; **Dynamite** was delivered to the Coworker at Route 6 `43, 19` in Turn 32170).
- **Repel Auto-Renewal Prompt**: When an active Repel expires on a step, the engine automatically displays: "Repel's effect wore off... Use another? Yes/No" (cursor defaults to Yes; pressing A immediately consumes and applies the next Repel without opening the Bag, verified Turn 27448).
- **Bag Structure (Audited Turn 27862)**: Features 3 main horizontal pockets from left to right: **Items** (Pocket 1), **Key Items** (Pocket 2), and **Poké Balls** (Pocket 3; does not wrap around when pressing Right).
- **Poké Balls Pocket (Audited Turn 32247)**: Contains **Poké Ball x9** and **Great Ball x8** (caught Lv18 Numel at `46, 14` in Turn 32212, nicknamed **Etna**, Lv18 Diglett at `47, 14` in Turn 32219, nicknamed **Gaia**, and Lv14 Trapinch at `42, 49` in Turn 32246, nicknamed **Dune**, bringing Owned species to **61** in PokéDex; **Red Shard x1** also added to Items Pocket at `40, 13` in Turn 32208).
- **Key Items Pocket (Audited Turn 27862)**:
  - **HuPhone** (registered to `[SELECT]`): *"A convenient smartphone that has many features to use."*
  - **TM Case**: *"A case that holds TMs and HMs. It is attached to the Bag's compartment for important items."*
  - **Metro Pass**: *"Its a card that can be used at the e-ticket reader gates to travel on the Hupest Metro Line."*
  - **Eclipse Band**: *"A special band designed to channel the power of Eclipse Shards to allow Eclipsing!"* (received from Professor Ivo in Azluf Town, Turn 27799).
  - **Fishing Rod**: *"A new, high-quality fishing rod. Use it by any body of water to fish for wild Pokémon."* (received from Fisherman at `37, 30` in Azluf Town, Turn 27854). Casting into water prints `. . .` dots and automatically resolves to either *"A Pokémon's on the hook!"* (requiring a single A/B press to start the wild battle, with no timing minigame) or *"Not even a nibble..."* (verified Turn 27865).
- **TMs & HMs Pocket**: Contains TM03 (collected at Route 4 `53, 17` in Turn 31892), TM17 (Protect), TM37 (Sandstorm, collected in Destino Mine 1F at `32, 35` in Turn 32317), TM39 (Rock Tomb, collected in Upper Mt. Gerhana at `43, 9` in Turn 31547), and TM48 (Work Up). Zero HMs in possession.

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
- **Selecting a Destination Inside the Train Car (`4, 5` Seat Trigger)**: Stepping `Left` from `(5, 5)` into the purple passenger seat at `(4, 5)` sits Asher down and opens the prompt: *"Which city do you want to go to?"* with a destination list of 8 stations (`Amor`, `Sovio`, `Samurion`, `Destino`, `Galinor`, `E.S.`, `Colen`, `Dis Bay`). Selecting a station not yet unlocked displays *"You can't go to that city yet!"* (verified for `Samurion` both pre-Round 1 in Turn 27582 and post-Round 1 in Turn 28824), while selecting an unlocked station such as `Sovio` announces *"The next station is... Sovio City!"* and warps to the destination station platform (`22, 17` in Sovio Metro Station, verified Turns 27583-27584).

## Battle UI & Type Effectiveness Indicators
- **Move Box Effectiveness Highlighting**: In the CFRU battle Fight menu, the selected move's box dynamically changes color to indicate type effectiveness against the active opponent (e.g. highlights **light green** when a move is super-effective, such as Steel-type Metal Claw against Fairy-type Cleffa or Psychic/Fairy-type Ralts; verified Turn 27656).

## Eclipsing & The Eclicizer Machine
- **True Eclipsing Requirements**: Requires a worthy bloodline wielder (such as Asher or Frio), the **Eclipse Band**, and a powered **Eclite Shard** (which breaks upon a single use and permanently transforms the target Pokémon into its Eclipsed form).
- **The Eclicizer (Professor Ivo's Basement Lab in Lancio Town)**:
  1. Restores powerless **Clear Shards** into active **Eclite Shards**.
  2. Combines smaller **Eclite Pieces** into a single fully powered **Eclite Shard**.
  - Professor Ivo noted that Eclite Pieces / Clear Shards can also be obtained from the giant Eclite crystal in Upper Mt. Gerhana (`27, 14`).

## UI & Transition Timing Mechanics (Verified Turns 31758-31768)
- **Nicknaming Screen Layout & PC Transfer Dismissal (`A` Required)**:
  - **7x4 Keyboard Grid `(col, row)`**:
    - **Row 0**: `(0,0)=A/a`, `(1,0)=B/b`, `(2,0)=C/c`, `(3,0)=D/d`, `(4,0)=E/e`, `(5,0)=F/f`, `(6,0)=.`
    - **Row 1**: `(0,1)=G/g`, `(1,1)=H/h`, `(2,1)=I/i`, `(3,1)=J/j`, `(4,1)=K/k`, `(5,1)=L/l`, `(6,1)=,`
    - **Row 2**: `(0,2)=M/m`, `(1,2)=N/n`, `(2,2)=O/o`, `(3,2)=P/p`, `(4,2)=Q/q`, `(5,2)=R/r`, `(6,2)=S/s`
    - **Row 3**: `(0,3)=T/t`, `(1,3)=U/u`, `(2,3)=V/v`, `(3,3)=W/w`, `(4,3)=X/x`, `(5,3)=Y/y`, `(6,3)=Z/z`
  - **Page Flip & Two-Part PC Box Transfer**: Pressing `Select` to toggle uppercase/lowercase requires `sleep 800` before subsequent D-Pad inputs. After pressing `Start` -> `A` to confirm a nickname when the party is full, two sequential messages appear (`"<Name> was transferred to Someone's PC.▼"` followed by `"It was placed in Box 'Box2.'"`), both of which ignore `B` presses and require pressing **`A`** twice (`A, sleep 1800, A, sleep 2500`) to return to the overworld (verified Turn 32248).
- **Battle Bag Fade-In Delay (`2500ms`) & Cursor Memory**: Pressing `A` on `Bag` during battle requires a `sleep 2500` pause for the Bag UI fade-in animation to complete before D-Pad inputs register. Subsequent Bag openings within the same battle remember both the last opened pocket (e.g. `Poké Balls`) and the last highlighted row (verified Turns 31763-31776).
- **Samurion City Pokémon Center Exit Routing**: Stepping `Down` off `(7, 8)` inside the Samurion City Pokémon Center requires `sleep 2500` for the door warp to settle at `(23, 48)`, followed by `Right 2` to `(25, 48)` -> `Down 1` to `(25, 49)` -> `Right 3` to `(28, 49)` to bypass the Pokémon Center window (`24, 47`) and southern house roof peak (`24, 50`) (verified Turns 31757-31760).

<hr>

<h1><code>Party/Altair_Starly</code></h1>

# Altair (Staravia) - Teammate

## Profile
- **Species**: Staravia (Normal/Flying; evolved from Starly at Lv14 in Turn 30644)
- **Nickname**: Altair
- **Gender**: Male (♂)
- **Level**: Lv14 (stored in Box 1)
- **Ability**: Intimidate (evolved from Keen Eye Starly)
- **Caught**: Route 2 at `(12, 10)` in standard Poké Ball (Turns 27592-27605)
- **HP**: 40/40 HP
- **Moves**:
  - Slot 1: Wing Attack (Flying, Physical, 60 power, 100% acc, 35 PP, STAB; learned at Lv9)
  - Slot 2: Tackle (Normal, Physical)
  - Slot 3: Quick Attack (Normal, Physical, Priority +1)
  - Slot 4: Double Team (Normal, Status; learned at Lv13)

<hr>

<h1><code>Party/Cetus_Remoraid</code></h1>

# Cetus (Remoraid) - Teammate

## Profile
- **Species**: Remoraid (National Dex No. 223, Water-type)
- **Nickname**: Cetus (named after the Sea Monster constellation)
- **Gender**: Male (♂)
- **Level**: Lv6
- **Caught**: Azluf Town (`36, 31` fishing into `36, 32`) in standard Poké Ball (Turns 27865-27873)
- **HP**: 21/21 HP (healed to full by Nurse Joy in Turn 28688)
- **Moves**:
  - Slot 1: Water Gun (Water, Special, 40 power, 100% acc, STAB; verified Turn 28673)

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

# Sirius (Lucario) - Starter Pokémon

## Profile
- **Species**: Lucario (Fighting/Steel; evolved from Riolu via high friendship + daytime level-up at Lv30 in Mt. Gerhana 1F, verified Turn 30857)
- **Nickname**: Sirius (Officially renamed from default Riolu via Sovio Name Rater)
- **Gender**: Male (♂)
- **Level**: Lv44
- **Nature**: Relaxed (+Def, -Speed)
- **Ability**: Steadfast (evolved from Quick Feet Riolu; verified Turn 31668)
- **Stats (IV Grades)**: HP (C, 131), Attack (C+, 122), Defense (A-, 117), Sp. Atk (C-, 113), Sp. Def (E, 78), Speed (C-, 80)
- **Current Condition**: 64/131 HP, Paralyzed (Healed at Destino City Pokémon Center in Turn 32187; leveled up to Lv44 in Turn 32339; paralyzed by Siara Grunt's Seviper in Turn 32331; 64/131 HP after defeating Siara Grunt 4's Swoobat in Turn 32364)
- **EXP**: Lv44 (evolved into Lucario at Lv30 during Mt. Gerhana training; declined Fire Punch at Lv32; learned Aura Sphere at Lv34; learned Bulldoze at Lv36; declined Swords Dance at Lv40; declined Low Sweep at Lv44; reached Lv44 defeating Siara Grunt 2's Zangoose in Destino Mine 2F in Turn 32339)
- **Moves**:
  - Slot 1: Metal Claw (Steel, Physical, 50 power, 95% acc, STAB, 35 PP; 10% chance to raise Attack +1; does not trigger cave wild Pokémon's Sturdiness damage-reduction popup)
  - Slot 2: Bulldoze (Ground, Physical, 60 power, 100% acc, 20 PP; lowers target's Speed -1; learned at Lv36 replacing Force Palm in Turn 31742)
  - Slot 3: Aura Sphere (Fighting, Special, 80 power, never misses, STAB, 20 PP; learned at Lv34 replacing Work Up)
  - Slot 4: Mach Punch (Fighting, Physical, Priority +1, STAB, 30 PP)
  - *Declined / Replaced*: Counter (Physical Fighting, offered Lv12; declined), Quick Attack (Normal Priority +1, replaced at Lv20 by Force Palm), Nasty Plot (Status Dark, +2 Sp. Atk, offered Lv24; declined), Screech (Status Normal, -2 Def, offered Lv28; declined)
- **OT / ID**: Asher / 54592
- **Met**: Lancio Town at Lv5
- **Appearance**: Custom sprite wearing a red/black scarf
- **Held Item**: Black Belt (boosts Fighting-type moves by 20%)

<hr>

<h1><code>Party/Vega_Shinx</code></h1>

# Vega (Luxio) - Teammate

## Profile
- **Species**: Luxio (Electric-type; evolved from Shinx at Lv15 in Turn 30885)
- **Nickname**: Vega (named after Alpha Lyrae, the bright blue-white star of the Summer Triangle alongside Altair)
- **Gender**: Female (♀)
- **Level**: Lv15
- **Ability**: Intimidate (Cuts the foe's Attack stat upon entering battle; verified Turn 28053)
- **Caught**: Route 2 at `(53, 26)` in standard Poké Ball (Turns 28052-28059)
- **HP**: 46/46 HP (Healed at Destino City Pokémon Center in Turn 32187)
- **Moves**:
  - Slot 1: Spark (Electric, Physical, STAB; learned at Lv12)
  - Slot 2: Leer (Normal, Status; learned at Lv5)
  - Slot 3: Charge (Electric, Status; learned at Lv9)
  - Slot 4: Baby-Doll Eyes (Fairy, Status, Priority +1, lowers target's Attack -1; verified Turn 32118)

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