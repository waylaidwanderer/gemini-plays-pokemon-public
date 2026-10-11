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
  - **Lower Arena Concourse (`rows 22-27`)**: Reached by descending the lower blue escalators at `(4, 19-22)` or `(16, 19-22)` (`latest_grid.png` Turn 27974 & physical traversal Turns 27975-27976; reached from reception by routing around the diamond pillars at `6-7, 14-18` or `13-14, 14-18` via `col 5` or `col 15`; note that `4, 26-27` and `16, 26-27` are solid outer diagonal wall corners and `6, 24 / 7, 25 / 8, 26` form an inner diagonal wall border, so the cleanest route from the west escalator `4, 19-22` to the central exit mat `10, 27` is `Down` to `4, 24` -> `Right 1` to `5, 24` -> `Down 2` to `5, 26` -> `Right 5` to `10, 26` -> `Down 2` off `10, 27`, verified Turns 32505-32506). Features a lower floor with a red mat at `(9-11, 27)` leading to the Eclipse Tournament arenas (per the receptionist's instructions in Turns 27971-27972).
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
## Round 3 Arena & Eclipse Tournament Round Three (`17, 17` -> `4, 14` -> `14, 14`)
- **Round 3 Arena Entrance (`17, 17`)**: Unguarded after receiving the Round 3 HuPhone summons in Destino City (Turn 32489); stepping `Down` through `(17, 17)` warps to the 8-trainer Round 3 Bracket Screen (`7, 17`, verified Turn 32507).
- **Match 1 (Quarterfinals — Juggler Tony)**:
  - **Pre-Battle Quote**: *"Interesting.. / May I take this win?"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Togetic (♂, Lv25; Fairy/Flying).
    - **Pokémon 2**: Ninjask (♀, Lv25; Bug/Flying; Ability: Speed Boost; knows Agility, Sand Attack, and Fury Cutter).
    - **Pokémon 3**: Luxio (♀, Lv26; Electric; knows Spark and Thunder Fang).
  - **Outcome**: Defeat quote: *"Losing at this point... / How embarrassing"*; awards `₽1,040` (verified Turns 32510-32525).
- **Match 2 (Semifinals — Black Belt Lee)**:
  - **Pre-Battle Quote**: *"Hello... / May the stronger Trainer win!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Heracross (♀, Lv25; Bug/Fighting; knows Counter).
    - **Pokémon 2**: Hitmonlee (♂, Lv25; Fighting; knows Protect).
    - **Pokémon 3**: Dewott (♂, Lv26; Water).
  - **Outcome**: Defeat quote: *"Argh!"*; awards `₽1,872` (verified Turns 32528-32540).
- **Match 3 (Round Three Finals — PKMN Trainer Aaron)**:
  - **Pre-Battle Quote**: *"Hmm, so you are gonna be my final opponent... / My name is Aaron. / I came from the Sinnoh region, and my goal is to become the greatest Trainer specializing Bug Pokémon! / Let this battle be my glow up."*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Dustox (♂, Lv25; Bug/Poison).
    - **Pokémon 2**: Yanmega (♀, Lv25; Bug/Flying; knows Double Team).
    - **Pokémon 3**: Vespiquen (♀, Lv26; Bug/Flying; Ability: Pressure).
    - **Pokémon 4**: Scizor (♂, Lv25; Bug/Steel).
  - **Outcome**: Defeat quote: *"I guess you really were my final opponent... / Not just in this round but in the whole tournament... how shocking."*; awards `₽2,912` and crowns Asher winner of his Round 3 group (verified Turns 32542-32553).
- **Post-Round-3 Cutscene Trigger (`11, 11` in Tournament Arena Lobby, Turns 32554-32556)**: Stepping north onto `(11, 11)` after winning Round 3 triggers Professor Ivo's HuPhone text message inviting Asher to meet her in **Jarro Town** via **Route 12** (reached through the most northerly tunnel in Amor City).
## Amor City Northern Sector (`18, 0` South <-> `18, 39` North) & Route 12 Gatehouse (`6, 12`)
- **Seamless Map Transition (`18, 0` <-> `18, 39`)**: Walking north along `column 18` past the Route 6 turnoff (`18, 7`) in Amor City South transitions seamlessly at `(18, 0)` onto `(18, 39)` in **Amor City North** (verified Turns 32623-32624).
- **Northern Amor City Pokémon Center (`23, 31`)**: Located on the east side of `column 18` in Amor City North, south of a four-way street intersection at `(18, 26-27)` (observed Turn 32625).
- **Route 12 Signboard (`11-12, 12`) & Route 12 Gatehouse (`7, 12` -> `6, 12`)**:
  - At the northern end of `column 18` (`18, 12-13`), a westbound street runs along `rows 12-13` (`cols 7-18`).
  - Wooden signboard at `(11-12, 12)` (interacted from `11, 13`) reads verbatim: *"Route 12 / <-------"* (verified Turn 32628).
  - Stepping `Left` from `(7, 12)` onto `(6, 12)` enters the **Route 12 Gatehouse** (the most northerly tunnel in Amor City; verified Turn 32629).
## Round 4 Arena & Eclipse Tournament Round Four (`20, 17` -> `4, 14` -> `14, 14`)
- **Round 4 Arena Entrance (`20, 17`)**: Unguarded after receiving the Round 4 HuPhone summons in Jarro Town (`36, 29`, Turn 32949); stepping `Down` through `(20, 17)` warps to the 8-trainer Round 4 Bracket Screen (`7, 17`, verified Turn 32957).
- **Round 4 Bracket**:
  - **Left Side**: **Asher** vs. **Scientist/Collector** (Match 1) and **Ace Trainer Male** vs. **Hiker** (Match 2).
  - **Right Side**: **Silver (from Johto)** vs. **Worker** (Match 3) and **Picnicker** vs. **Black Belt** (Match 4).
- **Match 1 (Quarterfinals — Super Nerd Eugene)**:
  - **Pre-Battle Quote**: *"Hehe a kid will be easy to defeat! / Bring it on"*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Haunter (♂, Lv27; Ghost/Poison; Ability: Levitate).
    - **Pokémon 2**: Diggersby (♂, Lv28; Normal/Ground).
    - **Pokémon 3**: Banette (♀, Lv27; Ghost; Ability: Cursed Body).
    - **Pokémon 4**: Vigoroth (♀, Lv28; Normal).
  - **Outcome**: Defeat quote: *"Losing to a kid... / What an awkward way to end this"*; awards `₽1,008` (verified Turns 32960-32967).
- **Match 2 (Semifinals — Hiker Tom)**:
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Carnivine (♀, Lv28; Grass; Ability: Levitate).
    - **Pokémon 2**: Cryogonal (Lv29; Ice).
    - **Pokémon 3**: Quilladin (♂, Lv28; Grass).
  - **Outcome**: Defeat quote: *"What the? / Wasn't I focusing enough?"*; awards `₽1,160`, while Johto's **Silver** defeated the Picnicker on the opposite side of the bracket (verified Turns 32971-32974).
- **Match 3 (Round Four Finals — PKMN Trainer Silver)**:
  - **Pre-Battle Quote**: *"So you are my final opponent this round... / My name is Silver, I came from the Johto Region... / You don't look like much, I bet my Pokémon will pummel you!"*
  - **Team (4 Pokémon, +2 Hyper Potions)**:
    - **Pokémon 1**: Weavile (♂, Lv29; Dark/Ice).
    - **Pokémon 2**: Crobat (♀, Lv29; Poison/Flying).
    - **Pokémon 3**: Magnezone (Lv30; Electric/Steel; Ability: Sturdy; knows Iron Defense).
    - **Pokémon 4**: Feraligatr (♂, Lv31; Water).
  - **Outcome**: Defeat quote: *"What the?! / Arghhh! / Now that I look at you, you do remind me of someone I really don't like... / Looks like my Pokémon were worthless... they were weak!"*; awards `₽3,472` and crowns Asher winner of his Round 4 group (verified Turns 32977-32987).
- **Post-Round-4 Cutscene Trigger (`14, 6` in Tournament Arena Lobby, Turn 32989)**: Stepping onto `(14, 6)` after winning Round 4 triggers Dad's HuPhone text message asking Asher to meet him in front of the Amor City Battle Centre (`59, 25`) so he can pick Asher up for Professor Ivo's emergency meeting.
## Round 5 Arena & Eclipse Tournament Round Five (`10, 26` -> `4, 14` -> `14, 14`)
- **Round 5 Arena Entrance (`10, 26` in Lower Arena Ring)**: Unguarded after receiving the Round 5 HuPhone summons in Professor Ivo's Basement Lab (Turn 33425); stepping `Down` through `(10, 26)` warps to the 8-trainer Round 5 Bracket Screen (`7, 17`, verified Turn 33429).
- **Round 5 Bracket**:
  - **Left Side**: **Asher** vs. **Cooltrainer Summer** (Match 1) and **Worker** vs. **Camper** (Match 2).
  - **Right Side**: **Barry (from Sinnoh)** vs. **Camper** (Match 3) and **Black Belt** vs. **Lass** (Match 4).
- **Match 1 (Quarterfinals — Cooltrainer Summer)**:
  - **Pre-Battle Quote**: *"May the stronger Trainer win, even though that's obviously me."*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Florges (♀, Lv32; Fairy; OHKO'd by Sirius's `Meteor Mash` for `1384 EXP`).
    - **Pokémon 2**: Cacturne (♂, Lv32; Grass/Dark; OHKO'd by Sirius's `Mach Punch` for `1213 EXP`).
    - **Pokémon 3**: Venusaur (♀, Lv32; Grass/Poison; OHKO'd by Sirius's `Meteor Mash` for `1425 EXP`, leveling Sirius to Lv57).
  - **Outcome**: Defeat quote: *"This is... no, impossible!"* (verified Turns 33431-33434).
- **Match 2 (Semifinals — Fisherman Otis)**:
  - **Pre-Battle Quote**: *"This fishing rod has been through a lot... / Let me show you what we caught together over the years!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Octillery (♂, Lv32; Water; OHKO'd by Sirius's `Aura Sphere` for `1123 EXP`).
    - **Pokémon 2**: Gyarados (♂, Lv32; Water/Flying; Ability: Intimidate; knows Leer; 2HKO'd by Sirius's `Aura Sphere` for `1467 EXP`).
    - **Pokémon 3**: Sharpedo (♂, Lv33; Water/Dark; OHKO'd by Sirius's non-contact `Aura Sphere` for `1237 EXP`).
  - **Outcome**: Defeat quote: *"We... we failed buddy."*; awards `₽1,188`, while Sinnoh's **Barry** defeated Black Belt Adam on the opposite side of the bracket (verified Turns 33436-33439).
- **Match 3 (Round Five Finals — PKMN Trainer Barry)**:
  - **Pre-Battle Quote**: *"Hey hey hey! / You look awfully familiar... / Ah yes! You must be that guy from the Galtino Bridge! / You are quite famous among us, competitors... / Ah, anyway! My name is Barry! I came from sinnoh, you probably know one of my friends though. / She was the one you saved back there. Dark hair, beanie, familiar? / Ah, I'm just stalling our battle! Let's get to it already!"*
  - **Team (4 Pokémon, +2 Hyper Potions)**:
    - **Pokémon 1**: Staraptor (♂, Lv32; Normal/Flying; Ability: Intimidate; Held Item: Rocky Helmet; OHKO'd by Sirius's `Meteor Mash` for `1179 EXP`).
    - **Pokémon 2**: Hitmontop (♂, Lv33; Fighting; Ability: Intimidate; OHKO'd by Sirius's `Aura Sphere` for `975 EXP`).
    - **Pokémon 3**: Empoleon (♂, Lv34; Water/Steel; custom Ability: Sturdiness [reduces super-effective damage]; knows Scald; defeated by Sirius's `Aura Sphere` for `1530 EXP`).
    - **Pokémon 4**: Roserade (♀, Lv33; Grass/Poison; OHKO'd by Sirius's `Meteor Mash` for `1441 EXP`).
  - **Outcome**: Defeat quote: *"'Thud' Oh man... / Even though my Dad is a Frontier Brain... I still failed"*; awards `₽3,808` and crowns Asher winner of his Round 5 group (verified Turns 33443-33455).
- **Post-Round-5 Cutscene with Dawn & Valora (`11, 10` in Tournament Arena Lobby -> `9, 18` in Ivo's Basement Lab, Turns 33457-33461)**:
  - Stepping onto `(11, 10)` in the Tournament Arena Lobby after winning Round 5 triggers **Dawn** to greet Asher (`"So, how's Mr. Famous doing?"`), invite him out for a drink or food to celebrate (which Asher declines because he has business to take care of and needs to pick someone up), and exchange phone numbers with him before departing.
  - Riding up the escalator at `(6, 17)`, **Valora** spots Dawn leaving and feels a pang of jealousy (*"Yet... why is she being so close to him? I have known him way longer"*). Though she also passed Round 5, Valora avoids meeting Asher's eyes and urges him to return to Professor Ivo's laboratory immediately, automatically fast-traveling them to **`(9, 18)`** in Professor Ivo's Basement Lab in Lancio Town.
## Post-Round-5 Eastern Amor City & Amor City Northeast (`cols 75-92` & `64, 24` Amor Dept.)
- **Cleared Construction Barrier (`75, 28-30`, Verified Turn 33465)**: After winning Round 5 of the Eclipse Tournament, the three construction workers at `(75, 28-30)` in Amor City South are gone, opening the main avenue east to `columns 85-86`.
- **Eastern Northbound Avenue (`cols 85-86`, Verified Turns 33467-33475, 33520, 33560-33580)**:
  - Runs north from `(85, 29)` to `(86, 0)` (with a streetlamp at `85, 21` and an overhead skybridge spanning `rows 16-20`).
  - **Route 16 Gatehouse (`87, 24` -> `88, 24` <-> `1, 7`, Verified Turn 33579)**: Located on the east side of `column 86` at `rows 23-24` beneath a diagonal blue glass canopy and warm tan interior doorway light; stepping `Right` from `(87, 24)` onto `(88, 24)` warps into the **Route 16 Gatehouse** at `(1, 7)`!
  - **Decorative Building Facade (`80, 12`, Verified Turn 33473)**: Located west of `(86, 12-15)` with a wandering female Scientist at `(83-84, 12-15)`; the door at `(80, 12)` does not open.
  - **Interior Cross-Avenues (`rows 12-15`, `col 51-52`, `col 73`, Verified Turns 33559-33566)**: `rows 12-15` connects `(18, 12-13)` east to `(86, 12-15)`. `column 73` connects `(73, 13)` south to `(73, 29)`, while `column 51-52` connects `(51, 13)` north across `(51, 0)` South <-> `(51, 43)` North to `(51, 26)` in Amor City North.
- **Amor City Northeast (`86, 0` South <-> `86, 43` North, Verified Turns 33475-33563 & 34592-34596)**:
  - Walking north across `(86, 0)` in Amor City South transitions seamlessly onto `(86, 43)` in Amor City Northeast (`column 86` runs north to `(86, 10)`, where three construction workers at `(85-87, 23)` block the northern road prior to Round 8 with the dialogue: *"I'm sorry but this area is still under renovations... / We will open it soon"*, verified Turns 33529 & 33562, and clear after Asher wins Round 8, while `rows 26-27` turn west across the city to `(18, 26)`).
  - **Route 14 Gatehouse (`88-89, 10` <-> `1, 7`, Verified Turn 34596)**: Located at the northern end of `column 86` in Amor City Northeast; stepping `Right` from `(88, 10)` through `(89, 10)` warps into the **Route 14 Gatehouse** at `(1, 7)`.
  - **Amor Department Store ("Amor Mall!", `64, 24` -> `8, 17`, Verified Turns 33477-33519)**:
    - Reached by walking west from `(86, 26)` along `rows 26-27` to `(64, 26)` and north into the green-arched entrance at `(64, 24)`, which warps into **Amor Dept. 1F** at `(8, 17)`. (The orange-roofed Pokémon Center south of the plaza at `64, 31` is enclosed by solid streetlamps at `61, 30-31` and `67, 30-31` and is unreachable on foot).
    - **Elevator (`8, 2` on 1F; `14, 2` on 2F/4F/5F; `6, 2` on 3F)**: Connects `1F` through `5F` (menu order from top to bottom: `5F`, `4F`, `3F`, `2F`, `1F`). Entering the elevator warps to `(18, 4)` and automatically triggers the attendant to walk to `(18, 6)` and ask `"Greetings, sir! / Which floor can I take you today?▼"` (~2.5s after warp); pressing `A` opens the floor list with the cursor at `5F`. Selecting a floor (`Alright, let's go!▼` -> ~2.5s elevator ride -> `Thank you for choosing the Amor Department Store!▼` -> `Have a nice day!▼`) automatically steps the player out of the elevator onto the destination floor.
    - **1F (Lobby)**: Receptionist at `(8, 12)` (`"Hello, welcome to the Amor Department Store! Have fun shopping"`), shopper boy at `(3, 14)` / `(4, 15)`, elderly gentleman at `(8, 4)` / `(9, 4)`, elevator at `(8, 2)`, and eastern stairwell mats at `(14, 7-8)` and `(14, 10-11)` leading to the 1F stairwell (`30, 7-8` -> stairs up to 2F at `26, 7`).
    - **2F (Standard PokéMart Supplies, Clerk at `8, 5` facing `Up`)**: Sells `Poké Ball` (`₽200`), `Great Ball` (`₽600`), `Nest Ball` (`₽1000`), `Timer Ball` (`₽1000`), `Ultra Ball` (`₽1200`), `Potion` (`₽300`), `Super Potion` (`₽700`), `Hyper Potion` (`₽1200`), `Revive` (`₽1500`), `Antidote` (`₽100`), `Paralyz Heal` (`₽200`), `Awakening` (`₽250`), `Burn Heal` (`₽250`), `Ice Heal` (`₽250`), `Repel` (`₽350`), `Super Repel` (`₽500`), and `Max Repel` (`₽700`). After Round 8, Unova's **Hugh** appears at `(11, 7)` (interacted from `11, 6` facing `Down`) offering **Special Quest #21 ("Hugh's Pokémon")**—promising to give Asher three rare Pokémon from Unova if shown a PokéDex with **150 species** registered (accepted Turn 34675).
    - **3F (Evolution Stones & Trade/Hold Evolution Items, Clerk at `11, 6` facing `Up`)**: Sells `Leaf Stone` (`₽2100`), `Water Stone` (`₽2100`), `ThunderStone` (`₽2100`), `Fire Stone` (`₽2100`), `Shiny Stone` (`₽2100`), `Dusk Stone` (`₽2100`), `Sun Stone` (`₽2100`), `Moon Stone` (`₽2100`), `Oval Stone` (`₽2000`), `Protector` (`₽2000`), `Electirizer` (`₽2000`), `Magmarizer` (`₽2000`), `Dubious Disc` (`₽2000`), `Up-Grade` (`₽2100`), `Reaper Cloth` (`₽2000`), `Razor Claw` (`₽5000`), `Razor Fang` (`₽5000`), `Prism Scale` (`₽2000`), `WhippedDream` (`₽2000`), `Sachet` (`₽2000`), and `Link Cable` (`₽2100`).
    - **4F (Battle Items, Vitamins, Incenses & EV Power Items)**:
      - **Left Clerk (`6, 5` facing `Up`)**: Sells `Guard Spec.` (`₽700`), `Dire Hit` (`₽650`), `X Attack` (`₽500`), `X Defend` (`₽550`), `X Speed` (`₽350`), `X Accuracy` (`₽950`), `X Special` (`₽350`), `Poké Doll` (`₽1000`), `HP Up` (`₽9800`), `Protein` (`₽9800`), `Iron` (`₽9800`), `Carbos` (`₽9800`), `Calcium` (`₽9800`), and `Zinc` (`₽9800`).
      - **Right Clerk (`14, 5` facing `Up`)**: Sells `Sea Incense` (`₽9600`), `Lax Incense` (`₽9600`), `Power Weight` (`₽1500`), `Power Bracer` (`₽1500`), `Power Belt` (`₽1500`), `Power Anklet` (`₽1500`), `Power Lens` (`₽1500`), and `Power Band` (`₽1500`).
    - **5F (Amor Lotto, Clerk at `10, 5` facing `Up`)**: Runs the **Amor Lotto** for `₽4,500` per ticket (`"Hello, would you like to participate in the Amor Lotto? It costs 4500 dollars and you can win awesome prizes!"`). No staircase leads higher than 5F.
## Round 6 Arena & Eclipse Tournament Round Six (`13, 26` -> `4, 14` -> `14, 14`)
- **Round 6 Arena Entrance (`13, 26` in Lower Arena Ring)**: Unguarded after receiving the Round 6 HuPhone summons in Aur Factory (Turn 33863); stepping `Down` through `(13, 26)` warps to the 8-trainer Round 6 Bracket Screen (`7, 17`, verified Turn 33867).
- **Round 6 Bracket**:
  - **Left Side**: **Asher** vs. **Albert** (Match 1) and **Gentleman** vs. **Sailor** (Match 2).
  - **Right Side**: **Riley (from Sinnoh)** vs. **Ace Trainer Male** (Match 3) and **Ruin Maniac** vs. **Ace Trainer Female** (Match 4).
- **Match 1 (Quarterfinals — Scientist Albert)**:
  - **Pre-Battle Quote**: *"This will serve as a great way to research strong Pokémon!"*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Ditto (Lv35; Normal; OHKO'd by Sirius's `Mach Punch` for `457 EXP`).
    - **Pokémon 2**: Manectric (♂, Lv35; Electric; OHKO'd by Sirius's `Bulldoze` for `1260 EXP`, leveling Sirius to Lv62).
    - **Pokémon 3**: Porygon-Z (Lv36; Normal; OHKO'd by Sirius's `Mach Punch` for `1426 EXP`).
    - **Pokémon 4**: Cryogonal (Lv35; Ice; OHKO'd by Sirius's `Mach Punch` for `1350 EXP`).
  - **Outcome**: Defeated in Turns 33872-33879 (`"Very, very impressive..."`; awards `₽1,728`).
- **Match 2 (Semifinals — Sailor Kyle)**:
  - **Pre-Battle Quote**: *"Let me show you what I learned as being part of the marine!"*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Pelipper (♀, Lv35; Water/Flying; knows Shock Wave; 2HKO'd by Sirius's `Aura Sphere` for `1230 EXP`).
    - **Pokémon 2**: Machamp (♂, Lv36; Fighting; OHKO'd by Sirius's `Aura Sphere` for `1488 EXP`).
    - **Pokémon 3**: Whiscash (♀, Lv35; Water/Ground; OHKO'd by Sirius's `Aura Sphere` for `1185 EXP`).
    - **Pokémon 4**: Poliwrath (♀, Lv36; Water/Fighting; OHKO'd by Sirius's `Aura Sphere` for `1426 EXP`).
  - **Outcome**: Defeated in Turns 33884-33889 (*"All those years... / To lose to a kid?!"*; awards `₽2,016`).
- **Match 3 (Round Six Finals — PKMN Trainer Riley)**:
  - **Pre-Battle Quote**: *"Hello Trainer... / You are... oh! You are Asher! I heard quite a lot about you. / You must be a powerful trainer to create such a reputation for yourself without trying... / I'm also a Pokémon Trainer, only for fun... / My name is Riley! / Your team... hmm... / I sense your strong aura... / Please, show me what you can do!"*
  - **Team (5 Pokémon)**:
    - **Pokémon 1**: Absol (♀, Lv35; Dark; OHKO'd by Sirius's `Mach Punch`).
    - **Pokémon 2**: Lucario (♂, Lv37; Fighting/Steel; OHKO'd by Sirius's `Aura Sphere` for `1458 EXP`).
    - **Pokémon 3**: Metang (Lv35; Steel/Psychic; knows Stealth Rock; defeated by Sirius's `Aura Sphere` + `Bulldoze` for `1147 EXP`, leveling Sirius to Lv63).
    - **Pokémon 4**: Blaziken (♂, Lv36; Fire/Fighting; OHKO'd by Sirius's `Bulldoze`).
    - **Pokémon 5**: Gyarados (♂, Lv36; Water/Flying; knows Dragon Dance; 2HKO'd by Sirius's `Aura Sphere` for `1650 EXP`).
  - **Outcome**: Defeated in Turns 33891-33904 (*"Know your enemy... / Just as much as you know yourself. / That's the key to victory, but it seems like you already gained a good grasp on that concept... / Thank you for the battle!"*; awards `₽4,144`), crowning Asher winner of his Round 6 group and advancing him to Round 7 of the Eclipse Tournament.
- **Post-Round-6 Cutscene Trigger (`12, 25` in Lower Arena Ring, Turn 33906)**: Stepping onto `(12, 25)` after winning Round 6 triggers Dad's HuPhone text message instructing Asher to meet him, Professor Ivo, and Valora in **Maple Town**.
## Round 7 Arena & Eclipse Tournament Round Seven (`17, 26` -> `4, 14` -> `14, 14`)
- **Round 7 Arena Entrance (`17, 26` in Lower Arena Ring)**: Unguarded after receiving the Round 7 HuPhone summons in Mulberry Town (Turn 34178); stepping `Down` through `(17, 26)` warps to the 8-trainer Round 7 Bracket Screen (`7, 17`, verified Turn 34269).
- **Round 7 Bracket**:
  - **Left Side**: **Asher** vs. **Jonathan** (Match 1) and **Camper** vs. **Black Belt** (Match 2).
  - **Right Side**: **Hugh (from Unova)** vs. **Ace Trainer Male** (Match 3) and **Scientist** vs. **Worker** (Match 4).
- **Match 1 (Quarterfinals — Gentleman Jonathan)**:
  - **Pre-Battle Quote**: *"Greetings... / You can go first, I'm a gentleman"*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Arcanine (♂, Lv37; Fire; Ability: Intimidate; OHKO'd by Sirius's `Aura Sphere` for `1687 EXP`, leveling Sirius to Lv67).
    - **Pokémon 2**: Alomomola (♂, Lv38; Water; OHKO'd by Sirius's `Aura Sphere`).
    - **Pokémon 3**: Lumineon (♂, Lv37; Water; OHKO'd by Sirius's `Aura Sphere` for `1276 EXP`).
    - **Pokémon 4**: Manectric (♂, Lv38; Electric; OHKO'd by Sirius's `Aura Sphere` for `1368 EXP`).
  - **Outcome**: Defeated in Turns 34274-34284; awards `₽2,736`.
- **Match 2 (Semifinals — Battle Girl Sachi)**:
  - **Pre-Battle Quote**: *"I made it far enough, I'm not gonna lose! / Full front assault!"*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Medicham (♂, Lv37; Fighting/Psychic; OHKO'd by Sirius's `Aura Sphere` for `1212 EXP`).
    - **Pokémon 2**: Hariyama (♂, Lv37; Fighting; OHKO'd by Sirius's `Aura Sphere` for `1458 EXP`).
    - **Pokémon 3**: Blaziken (♂, Lv38; Fire/Fighting; OHKO'd by Sirius's `Aura Sphere` for `1701 EXP`).
    - **Pokémon 4**: Emboar (♂, Lv38; Fire/Fighting; OHKO'd by Sirius's `Aura Sphere` for `1693 EXP`).
  - **Outcome**: Defeated in Turns 34288-34295 (*"I... I lost?"*; awards `₽2,736`), while Unova's **Hugh** defeated Scientist Jesse on the opposite side of the bracket.
- **Match 3 (Round Seven Finals — PKMN Trainer Hugh)**:
  - **Pre-Battle Quote**: *"Hi! You must be Asher! / Man, battling with you feels so surreal... / My name is Hugh! / I came all the way from the Unova Region, and I'm not gonna lose! / My sister is definitely watching the broadcast so I can't"*
  - **Team (5 Pokémon)**:
    - **Pokémon 1**: Unfezant (♂, Lv37; Normal/Flying; OHKO'd by Sirius's `Aura Sphere` for `1363 EXP`).
    - **Pokémon 2**: Bouffalant (♀, Lv38; Normal; OHKO'd by Sirius's `Aura Sphere` for `1399 EXP`).
    - **Pokémon 3**: Simisage (♂, Lv37; Grass; OHKO'd by Sirius's `Aura Sphere` for `1378 EXP`).
    - **Pokémon 4**: Eelektross (♀, Lv38; Electric; Ability: Levitate; survived `Aura Sphere` in red HP and used `Volt Switch` into Samurott; later KO'd by Sirius's `Aura Sphere` for `1563 EXP`).
    - **Pokémon 5**: Samurott (♂, Lv39; Water; OHKO'd by Sirius's `Aura Sphere` for `1737 EXP`, leveling Sirius to Lv68).
  - **Outcome**: Defeated in Turns 34299-34307 (*"I... lost. / I couldn't achieve victory for my partners, nor my little sister... / Well, whatever. I'm just happy to know you are a Trainer others can count on every time."*; awards `₽4,368`), crowning Asher winner of his Round 7 group and advancing him to Round 8 of the Eclipse Tournament.
- **Post-Round-7 Confrontation with Frio & Professor Ivo's Urgent Summons (`16, 25` -> `19, 13` in Tournament Arena Lobby -> Maple Town `43, 15`, Turns 34308-34312)**:
  - Stepping onto `(16, 25)` after winning Round 7 warps Asher to `(19, 13)` in the upper Tournament Arena Lobby facing **Frio** (`19, 12`).
  - Keeping his promise from Mulberry Town, Frio reveals that the underwater Location 3 signal is an old, abandoned **undersea laboratory of Team Siara** located below sea level close to **Maple Town**.
  - When Asher asks Frio to join forces against Team Siara since Frio hates them more than anything, Frio refuses to get involved with Marie, Team Siara's experiments, or that undersea lab ever again (`"No! I'm not getting involved... I'm done with them! With that woman, with their experiments, with that damn Lab! I'm off now..."`) and departs.
  - Immediately afterward, Asher receives an urgent HuPhone text message from **Professor Ivo**: *"Asher! Quick pick up Valora and come here quick! We are on a small isle from Maple to the south, this is urgent!"*. Asher finds Valora and fast-travels directly to **`(43, 15)`** at the southern shoreline stairs of **Maple Town**.
## Round 8 Arena & Eclipse Tournament Round Eight (`20, 26` -> `4, 14` -> `14, 14`)
- **Round 8 Arena Entrance (`20, 26` in Lower Arena Ring)**: Unguarded after receiving the Round 8 HuPhone summons on the Small Offshore Isle (`36, 42`, Turn 34507); stepping `Down` through `(20, 26)` warps to the 8-trainer Round 8 Bracket Screen (`7, 17`, verified Turn 34548).
- **Round 8 Bracket**:
  - **Left Side**: **Asher** vs. **Cooltrainer Quentin** (Match 1) and **Scientist** vs. **Cooltrainer Lola** (Match 2; won by Lola).
  - **Right Side**: **Gladion (from Alola)** vs. **Hiker** (Match 3; won by Gladion) and **Expert Bert** vs. **Gentleman** (Match 4; won by Bert).
- **Match 1 (Quarterfinals — Cooltrainer Quentin)**:
  - **Pre-Battle Quote**: *"Ohohoho, the last round! I'm gonna make it to the finals! / I wanna have a movie made of my spectacular carrier!"*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Luxray (♂, Lv39; Electric; OHKO'd by Sirius's `Aura Sphere` for `1620 EXP`).
    - **Pokémon 2**: Toxicroak (♂, Lv39; Poison/Fighting; OHKO'd by Sirius's `Bulldoze` for `1437 EXP`).
    - **Pokémon 3**: Talonflame (♀, Lv40; Fire/Flying; knows Nature Power; 2HKO'd by Sirius's `Aura Sphere` for `1500 EXP`).
    - **Pokémon 4**: Cacturne (♀, Lv40; Grass/Dark; OHKO'd by Sirius's `Mach Punch` for `1516 EXP`).
  - **Outcome**: Defeated in Turns 34551-34558 (*"Nooo!"*; awards `₽2,400`).
- **Match 2 (Semifinals — Cooltrainer Lola)**:
  - **Pre-Battle Quote**: *"Finally... / A worthy opponent"*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Gastrodon (♂, Lv39; Water/Ground; OHKO'd by Sirius's `Aura Sphere`).
    - **Pokémon 2**: Delphox (♀, Lv40; Fire/Psychic; OHKO'd by Sirius's `Bulldoze` for `1791 EXP`).
    - **Pokémon 3**: Ampharos (♂, Lv39; Electric; OHKO'd by Sirius's `Bulldoze` for `1620 EXP`).
    - **Pokémon 4**: Lilligant (♀, Lv40; Grass; OHKO'd by Sirius's `Aura Sphere` for `1440 EXP`).
  - **Outcome**: Defeated in Turns 34559-34566 (*"Impossible... / H-how?!"*; awards `₽2,400`), while Alola's **Gladion** defeated Expert Bert on the opposite side of the bracket.
- **Match 3 (Round Eight Finals — PKMN Trainer Gladion)**:
  - **Pre-Battle Quote**: *"What does a Pokémon Trainer really need to be successful? / I guess everyone might have their own answer. / But for me... I want the strongest rival for myself! / My name is Gladion! / I came from the Alola Region to participate and make my partner stronger than anyone. / All I have to do is avoid making any more mistakes... / After all, I have Silvally with me."*
  - **Team (5 Pokémon)**:
    - **Pokémon 1**: Crobat (♀, Lv40; Poison/Flying; OHKO'd by Sirius's `Meteor Mash` [+1 Attack boost] for `1747 EXP`).
    - **Pokémon 2**: Zoroark (♂, Lv40; Dark; OHKO'd by Sirius's `Aura Sphere` for `1533 EXP`, leveling Sirius to Lv70).
    - **Pokémon 3**: Lucario (♂, Lv40; Fighting/Steel; OHKO'd by Sirius's `Aura Sphere` for `1576 EXP`).
    - **Pokémon 4**: Charizard (♂, Lv41; Fire/Flying; Held Item: Sitrus Berry; knows Fire Blast; 2HKO'd by Sirius's `Aura Sphere` for `1836 EXP`).
    - **Pokémon 5**: Silvally (Lv42; Normal; OHKO'd by Sirius's `Aura Sphere` for `1980 EXP`).
  - **Outcome**: Defeated in Turns 34568-34577 (*"Looks like after I made it all all this way... I still lost... / Hmph... It's not like me to slip up like that. / I've got to keep fighting stronger opponents. / Maybe one day we can fight again, Asher"*; awards `₽4,704`), crowning Asher winner of his Round 8 group and qualifying him for the Eclipse Tournament Finals.
- **Post-Round-8 Finals Announcement & Cutscene (`19, 25` in Lower Arena Ring, Turns 34579-34582)**:
  - Stepping onto `(19, 25)` after winning Round 8 triggers a PA announcement from the Host declaring that the final qualifying round of the Eclipse Tournament has officially ended and instructing all finalists and spectators to head to **Eclipse Square** (accessible on foot via **Route 14** from northeastern Amor City).
  - In the upper Tournament Arena Lobby (`14, 15`), **Barry** congratulates **Lucas** and **Dawn** on making it to the Finals alongside Asher (calling Asher *"a beast"* after losing to him in Round 5), while **Frio** listens silently nearby (`"..."`) before Lucas, Dawn, and Barry set off toward Route 14 and Eclipse Square.

<hr>

<h1><code>Locations/Aurin_Town</code></h1>

# Aurin Town & Route 16 Eastern Bay Approaches

## Route 16 Eastern Bay (`cols 0-60, rows 8-34`, Verified Turns 33648-33721)
- **Seamless Western Connection**: Connects at `(6, 25)` <-> `(89, 25)` on Route 16 West.
- **Seamless Eastern Connection to Aurin Town (`60, 18` <-> `1, 18`, Turn 33721)**: Signboard at `(57-58, 17)` reads verbatim: *"Aurin Town / ------->"*. Walking east past `column 60` transitions seamlessly onto `(1, 18)` in **Aurin Town**.
- **Sandbars**: Located at `(7-10, 24-27)` and `(16-17, 30)`.
- **Wild Surf Encounters**: Wild **Barboach** (caught Lv22 ♂ at `7, 22` in Turn 33653, nicknamed **Richter**) and **Horsea** (caught Lv20 ♂ at `25, 22` in Turn 33664, nicknamed **Triton**).
- **Southern Peninsula (`cols 21-31, rows 22-34`)**:
  - Shoreline landing along `column 22` (`rows 26-30`) with a wandering Bug Catcher at `(22-26, 28-30)` (*"Ugh it always rains in this area! It's so hard to find bugs!"*, verified Turn 33669).
  - Northern cove inlet at `(27, 23)` leads ashore to `(27, 24-25)` in front of an item ball at `(27, 26)` containing **Net Ball x1** (collected Turn 33661).
  - Uncollected purple spray-bottle item sprite observed at `(26, 34)` on the southern tip of the peninsula beyond the tree line (`rows 31-33`, observed Turn 33669).
- **Eastern Peninsula Landing & Wooden Bridge (`cols 32-44, rows 23-32`)**:
  - Shoreline landing at `(32, 23)` -> `(32, 24)` leads past tall grass (`28-34, 27-30`) to a wooden bridge at `(37-41, 27-29)`.
  - **Wild Tall Grass Encounters**: Wild **Volbeat** (caught Lv24 ♂ at `46, 24` in Turn 33694, nicknamed **Lumen**).
  - **Cooltrainer Alan (`39, 27`, facing `Down` on the wooden bridge)**:
    - **Pre-Battle Quote**: *"You crossed the water, right? / You must be a skilled Trainer!"*
    - **Team (3 Pokémon)**: Manectric (♂, Lv34; Electric), Gastrodon (♂, Lv35; Water/Ground; `1245 EXP`), and Feraligatr (♀, Lv34; Water; knows Scary Face; `1530 EXP`).
    - **Outcome**: Defeated in Turns 33676-33687 (*"Maybe too skilled"*; awards `₽2,100`).
- **Hiker Jovan (`43, 18` -> `43, 19`, facing `Down` beside the wooden cliff staircase at `40-42, 14-18`)**:
  - **Pre-Battle Quote**: *"I lost my precious job a long time ago... / The best I can do now is fighting Trainers passing by..."*
  - **Team (3 Pokémon)**: Camerupt (♀, Lv34; Fire/Ground; `1275 EXP`), Excadrill (♂, Lv34; Ground/Steel; `1296 EXP`), and Nidoking (♂, Lv35; Poison/Ground; `1462 EXP`).
  - **Outcome**: Defeated in Turns 33698-33706.
- **Upper Cliffside & Collapsed Bridge Eastern Span (`cols 17-48, rows 8-18`, Verified Turns 33706-33714)**:
  - **Wooden Cliff Staircase (`40-42, 14-18`)**: Connects the lower meadow (`40-42, 19`) to the upper cliffside (`40-42, 14`).
  - **Rugged Rock (`47, 12`)**: Blocks the narrow eastern cliff passage at `(47, 12)`.
  - **Eastern Bridge Span (`18-37, 11-13`)**: Extends west from `(38, 12)` across the bay to the western cliff island (`cols 8-17`).
  - **Black Belt Julio (`24, 13`, facing `Up` on the wooden bridge)**:
    - **Pre-Battle Quote**: *"Darn... the bridge has collapsed! / Be really careful!"*
    - **Team (2 Pokémon)**: Primeape (♂, Lv35; Fighting; `1117 EXP`) and Medicham (♀, Lv35; Fighting/Psychic; `1147 EXP`).
    - **Outcome**: Defeated in Turns 33710-33714 (`"..."`).
  - **Western Cliff Island & Broken Bridge End (`cols 8-17, rows 8-16`, Verified Turns 33715-33716)**:
    - Reached from `(16, 12)` by weaving behind the top tree canopies along `row 12` (`16, 12 -> 12, 12`) and `row 13` (`12, 13 -> 9, 13 -> 9, 12`).
    - **TM18 (Rain Dance, `8, 12`)**: Gold item ball on the broken western bridge end at `(8, 12)` (collected Turn 33716).
## Aurin Town Proper (`cols 1+, rows 1-24`, Entered Turn 33721)
- **Weathered Concrete House (`8, 17`)**: Dilapidated concrete house with broken windows and vines covering the door at `(8, 17)` (cannot be entered).
- **Arrival Cutscene with Dad & Aur Factory Lead (`9, 19`, Turns 33722-33726)**: Stepping onto `(9, 19)` triggers a cutscene with **Dad (Jackson)** (`10, 19`) and a local man (`11, 19`), who reveals that Pokémon in the ruins of **Aur Factory** (up the northern stairs at `13-15, 13-16`, where a wooden sign at `12, 17` reads verbatim: *"Aur Factory / Up Ahead"*, verified Turn 33746) have been behaving violently and abnormally. Dad recognizes **Aur Factory** from years ago and joins Asher to investigate it.
- **Aurin Town Pokémon Center (`19, 17`, exits to `19, 18`)**: Nurse Joy at `(7, 2)` (counter at `7, 4`; healed and registered checkpoint in Turn 33728); PokéMart mezzanine escalator at northwest corner (`3, 2`).
- **Town Signboard (`22-23, 18`)**: Interacted from `(22, 19)`, reads verbatim: *"Aurin Town / Look out for your belongings!"* (verified Turn 33731).
- **Biker Gang House (`25, 17`)**: Blocked by two Bikers sitting at `(25, 18)` and `(26, 18)` (*"Get lost kid, this is our gang's domain!"*, verified Turn 33731).
- **Southern Aurin Town & Fossil Resurrection Lab (`28, 25` -> `32, 32`, Verified Turns 33734-33740)**:
  - **Shady Delinquent (`27, 20`)**: *"Watch your steps kid, some parts of the ground might collapse under your feet."* (verified Turn 33734).
  - **Southern Staircase (`27-29, 27-30`)**: Descends to a lower plaza with a wandering Hiker (`33-34, 33-34`), a 2x2 dark ground pit (`29-30, 34-35`), and an unblocked concrete house doorway at `(32, 32)`.
  - **Fossil Resurrection Lab (`32, 32` -> `55, 10`)**:
    - **Explorer (`59, 7`)**: *"Hello there, Trainer! Tell me, do you like fossils? Ancient life? Now you can enjoy both! With this great machine, you can revive ancient Pokémon from fossils! Just use the computer there"* (verified Turn 33740).
    - **Fossil Revival Computer (`56, 4`, interacted from `56, 5` facing `Up`)**: Blue computer terminal connected to the green bio-tank (`58-59, 4-5`); prompts *"Would you like to revive a fossil? Yes/No"* (verified Turn 33742).
- **Aur Factory Gatehouse (`14, 3-5` -> `14, 0` <-> `14, 39` in Aur Factory, Verified Turns 33751-33754)**:
  - **Parasol Lady (`13, 5`)**: *"Pokémon are acting so weird in the old factory's area!"* (verified Turn 33752).
  - Walking north through the open gatehouse doorway (`14, 4 -> 14, 0`) transitions seamlessly onto `(14, 39)` in **Aur Factory**.

<hr>

<h1><code>Locations/Aur_Factory</code></h1>

# Aur Factory

## Southern Entrance & Exterior Grounds (`14, 39` <-> `14, 0` in Aurin Town)
- **Seamless Entrance (`14, 39`)**: Entering through the open gatehouse at `(14, 0)` in northern Aurin Town transitions seamlessly onto `(14, 39)` in **Aur Factory**.
- **Stone Archway (`16, 35-36`) & Rugged Rocks (`14, 34` and `22, 32`)**: Passing north through the stone archway at `(16, 35-36)` leads to an overgrown path with a rugged rock blocking the western tree gap at `(14, 34)` and tall grass patches spanning `(19-23, 32-34)` and `(29-30, 30-32)`.
- **Pit Ladder Cutscene with Dad (`22, 33` -> `25, 32`, Turns 33758-33759)**:
  - Stepping onto `(22, 33)` triggers a cutscene where Asher remarks that the path looks like a dead end, and **Dad (Jackson)** inspects the dark ground pit (`25-26, 29-31`) from `(26, 28)`, discovers a ladder inside the pit (*"Yes! There's a ladder! We can get down and back easily with this. Let's keep going!"*), and descends into `(26, 29)`.
## Aur Factory 1F (`26, 29` Ladder Entrance)
- **Entry Room (`cols 19-27, rows 26-33`)**: Reached by stepping `Down` from `(26, 28)` into `(26, 29)` on the Aur Factory exterior map (climbs down the wall ladder to `26, 29` -> `24, 30` on Aur Factory 1F; verified Turns 33761-33764). Features indoor tall grass patches at `(19-21, 28-33)` and a passage leading north along `columns 19-21`.
- **Gangster Russel (`25, 23`, facing `Down` beside the indoor floor pit at `27-28, 23-24`)**:
  - **Pre-Battle Quote**: *"Hello there, kid, sorry but this is a dangerous place for you!"*
  - **Team (2 Pokémon)**: Toxicroak (♂, Lv35; Poison/Fighting; `1290 EXP`) and Cacturne (♂, Lv35; Grass/Dark; `1327 EXP`).
  - **Outcome**: Defeated in Turns 33767-33772 (`"..."`).
- **Rebar Pit Beams (`27-28, 24`)**: While `(27-28, 23)` and `(27-28, 25)` of the indoor floor pit are impassable, the horizontal metal rebar beam across `row 24` (`27-28, 24`) is walkable and connects `(26, 24)` directly to `(29, 24)` (verified Turn 33776).
- **Eastern Rebar Pit (`34-36, 23-24`) & Central Staircase (`30-32, 19-22`)**: East of the first rebar pit (`27-28, 24`) lies an indoor tall grass patch (`30-33, 23-25`), a second rebar-bridged floor pit at `(34-36, 23-24)` (leading to a capsule item sprite at `38, 24`), and a wide staircase at `(30-32, 19-22)` ascending to the upper platform (`rows 14-21`).
- **Upper Platform Landmarks (`cols 22-38, rows 14-21`)**: Features a wandering **Explorer** at `(22-24, 18-20)` (*"These ruins... Can you imagine hundreds of people working here everyday?"*, verified Turn 33786), **Ultra Ball x1** at `(22, 21)` (collected Turn 33788), **TM08 (Payback)** in the enclosed western pocket at `(17, 17)` (reached by descending the exterior ground pit ladder at `19, 20 -> 19, 21` onto `14, 17` on Aur Factory 1F; collected Turn 33815), a rugged rock at `(37, 17)`, and **Gangster Cony** at `(29, 17)` facing `Down` (*"Hey hey! What is a defenseless kid doing here?"*; uses Skuntank ♀ Lv35 [`1260 EXP`] and Absol ♂ Lv35 [`1305 EXP`]; defeated in Turns 33779-33785, `"What the?!"`).
- **Northern Corridor & Gangster Hans (`26, 11`, facing `Right`)**:
  - **Pre-Battle Quote**: *"Hey there, kid! / How much is in your wallet?"*
  - **Team (2 Pokémon)**: Machamp (♂, Lv35; Fighting; `1447 EXP`) and Cloyster (♂, Lv35; Water/Ice; `1522 EXP`).
  - **Outcome**: Defeated in Turns 33792-33795 (*"Clearly more than how much I'll ever have!"*). Rugged rocks sit at `(26, 9)` and `(33, 8)` beside a blue barrel at `(32, 8)`.
- **Northern Exit Ladder (`36, 7` in Aur Factory 1F <-> `38, 10 -> 38, 11` on Aur Factory Exterior)**: Stepping onto `(36, 7)` and pressing `Up` climbs the wall ladder to `(38, 10)` on the northern exterior grounds of **Aur Factory**.
- **Collector Daniel (`33, 15`, facing `Right` on the northern exterior grounds)**:
  - **Pre-Battle Quote**: *"I'm here looking for new Pokémon I could sell!"*
  - **Team (2 Pokémon)**: Sigilyph (♂, Lv35; Psychic/Flying; `1290 EXP`) and Grumpig (♀, Lv35; Psychic; `1230 EXP`).
  - **Outcome**: Defeated in Turns 33800-33805.
- **Ether (`29, 12`)**: Collected from purple spray-bottle sprite at `(29, 12)` via the fence gap at `column 27` (`rows 12-15`; verified Turn 33806).
- **Criminal Harry (`24, 15`, facing `Down` in the tall grass on the northern exterior grounds)**:
  - **Pre-Battle Quote**: *"Why is a kid wandering out here? / Don't you know this is a messy place?"*
  - **Team (1 Pokémon)**: Seismitoad (♀, Lv36; Water/Ground).
  - **Outcome**: Defeated in Turns 33808-33811 (*"Ah... / You are well aware, I see..."*).
- **Black Belt Jack (`15, 17`, facing `Right` in front of the northwestern ground pit at `11-12, 15-17`)**:
  - **Pre-Battle Quote**: *"Tch, what is this? / Now anyone can just venture around?"*
  - **Team (3 Pokémon)**: Crabominable (♀, Lv35; Fighting/Ice; `1252 EXP`), Cloyster (♂, Lv35; Water/Ice), and Weavile (♂, Lv35; Dark/Ice; `1342 EXP`).
  - **Outcome**: Defeated in Turns 33818-33822 (`"Oh."`; awards `₽2,520`).
## Aur Factory Western / Lower Section (`12, 14 -> 12, 15` Exterior Pit Ladder -> `10, 36`)
- **The Gang Leader's Deal (`10, 36`, Turns 33824-33826)**:
  - Descending the northwestern exterior ground pit ladder (`12, 14 -> 12, 15`) onto `(10, 36)` triggers a cutscene where **Dad (Jackson)** is negotiating with the local gang leader (`Man`, a Black Belt at `12, 35`) and two Gangsters.
  - Recognizing Asher's name and reputation as a skilled Pokémon Trainer, the gang leader offers a deal: gather **3 Scrap Metals** from the more dangerous locations around the factory ruins, and he will grant Dad and Asher a free pass through his territory.
- **Lower & Upper Staircases (`16-18, 31-33` & `16-18, 22-25`)**:
  - From `(10, 36)`, walking east along `row 36` bypasses the gang leader (`12, 35`) and reaches the lower staircase (`16-18, 31-33`).
  - **Furnace Alcove (`cols 19-24, rows 26-29`)**: Reached via the 1-tile gap at `(19, 30 -> 19, 29)`; contains an old furnace (`21-22, 26-27`, `"I wonder what these were used for back in the day..."`) and an indoor rugged rock at `(24, 29)`.
  - Routing along `column 15` (`15, 30 -> 15, 26 -> 17, 26`) reaches the upper staircase (`16-18, 22-25`) to the northern terrace (`rows 18-23`).
- **Northern Terrace (`cols 2-24, rows 18-26`, Verified Turns 33832-33839)**:
  - **Narrow Stone Pillar (`8, 24 -> 8, 25`)**: Connects `(8, 23)` south to `(8, 25)` directly in front of the Gold Item Ball at `(8, 26)` containing **Scrap Metal** (#1 of 3, collected into Key Items Pocket in Turn 33835).
  - **Western Stone Beam (`3-4, 21`)**: Walkable grey stone beam across `row 21` connecting `(5, 21)` west across the pit to `(2, 21)` below the Gold Item Ball at `(2, 19)` containing **Scrap Metal** (#2 of 3, collected into Key Items Pocket in Turn 33841; `(3-4, 19-20)` are solid pit collision).
  - **Eastern Rebar Beam (`21-22, 21`)**: Connects `(20, 21)` east across the pit to `(23, 21)`, leading to the third Gold Item Ball at `(28, 22)` containing **Scrap Metal** (#3 of 3, collected into Key Items Pocket in Turn 33843) and an eastern staircase at `(25-27, 16-19)`.
  - **Fenced Alcove (`12-14, 24-25`) & Overhead Bridge (`12-14, 18-23`)**: `(12-14, 18-23)` is a two-elevation overhead bridge: the upper terrace (`rows 20-22`) crosses east-west on Elevation 2, while `columns 12-14` (`rows 14-25`) form a lower underpass on Elevation 1 connecting `(12-14, 14)` (reached via the northern loop `25-27, 16-19 -> 26, 8 -> 17, 8 -> 17, 14 -> 15, 14`) south underneath the bridge to `(12-14, 24-25)`, where **Luxury Ball x1** sits at `(13, 25)` (collected Turn 33848; verified Turn 33853).
  - **Northern Doorway (`13, 9`)**: Guarded by a Gangster at `(13, 10)` at the north end of the `(12-14, 10-14)` corridor until the 3 Scrap Metals are delivered to the gang leader at `(12, 35)` (*"Oh! You got 3, as I asked you to... Wow, I'm impressed. / Asher gave the Scrap Metal to the shady guy. / I don't know why you two are investigating around here, but I hope you will find whatever you two are looking for..."*, verified Turn 33855).
- **Inner Pedestal Chamber (`13, 9` -> `16, 9` -> Amor City South `88, 24`, Turns 33857-33865)**: Stepping into the northern doorway at `(13, 9)` triggers the cutscene showing **Siara Admin Flo** escaping by helicopter with the second gem from the pedestal (`16, 8`), the mysterious boy (`???`) vanishing upon Asher and Dad's arrival, and the **Amor Battle Center** HuPhone summons for **Round Six of the Eclipse Tournament**, which automatically fast-travels Asher to **`(88, 24)`** outside the Route 16 Gatehouse in **Amor City South**.

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
  - **Interior (`7, 8` exit mat)**: Nurse Joy at `(7, 2)` (counter at `7, 4`; healed party and registered respawn checkpoint in Turn 32187; blacking out to a Pokémon Center resets the Start Menu cursor to `Pokédex`, verified Turn 33409); glasses man at `(6, 4)` (*"Health care is top notch for Pokémon... I wonder if it will ever be this good for humans."*, Turn 32188); wandering woman with dark bun around `(9-10, 6-7)`; PC terminal at `(12, 1)`; PokéMart mezzanine staircase at `(2, 0)` (connected seamlessly on the same map to `5, 7`, clerk at `5, 3` selling Poké Ball `₽200`, Great Ball `₽600`, Ultra Ball `₽1200`, Potion `₽300`, Super Potion `₽700`, Hyper Potion `₽1200`, Revive `₽1500`, Antidote `₽100`, Paralyz Heal `₽200`, Awakening `₽250`, Burn Heal `₽250`, Full Heal `₽600`, Escape Rope `₽550`, Repel `₽350`, Super Repel `₽500`, and Max Repel `₽700`, verified Turns 32191-32192 & 33400-33401).
- **Destino Metro Station (`45, 13` <-> Station Interior `23, 24`)**:
  - North of the Pokémon Center (`cols 44-46, rows 13-18`), a green-uniformed worker at `(45, 14)` initially guarded the northern archway leading to the Destino Metro Station (*"I'm sorry but the metro station is under renovation. Come back later"*, verified Turn 32194) until clearing Destino Mine and receiving the Round 3 summons at `(37, 31)` (Turns 32488-32491).
  - Stepping north onto `(45, 13)` after the guard vacates enters the **Destino Metro Station** at **`(23, 24)`** (verified Turn 32497).
  - **Interior Layout**: Walk `Left 4` to `(19, 24)`, `Up 7` through the concourse archway (`19, 21`) to `(19, 17)`, `Right 1` to `(20, 17)`, and `Up 1` onto the turnstile lane at **`(20, 16)`** (between the two officers at `19, 15` and `21, 15`) to trigger the Hupest Metro Line boarding prompt (verified Turns 32498-32501).
- **Town Signboard (`37-38, 19`)**:
  - Located immediately west of the Pokémon Center (interacted from `38, 20`); reads verbatim: *"Destino City / The industrial mine city"* (verified Turn 32194).
- **Western Street Roadblock (`34, 19-21` / `33, 20`)**:
  - Stepping west onto `col 34` (`34, 20`) prior to investigating the Destino Mine displays verbatim: *"We should check what's the deal with the Destino Mine!"* and steps the player east to `(35, 20)` (verified Turn 32195). After clearing Destino Mine and receiving the Round 3 summons, stepping onto `(34, 20)` displays verbatim: *"Round three starts soon... / I should head to Amor City now!"* and steps the player east to `(35, 20)` (verified Turn 32497). After winning Round 3, `(34, 20)` is passable, while stepping onto `(33, 20)` displays verbatim: *"I have other things to do! / I don't have a reason to go this way."* and steps the player east to `(34, 20)` (verified Turn 32565). After winning Round 4 and attending Professor Ivo's emergency meeting in Lancio Town, `(33, 20)` is permanently cleared (verified Turn 32999).
- **Southern Avenue & Diagonal Staircase toward Destino Mine (`cols 32-46, rows 22-30`)**:
  - Directly south of the Destino City Pokémon Center (`41, 18`), the tan curb along `row 22` (`cols 36-44`) is passable and leads south into the upper dirt plaza (`cols 36-46, rows 23-29`), where a female resident in a pink shirt patrols around `(40-41, 22-24)` (*"The city is huge... I need to find a Burger Kingler..."*, verified Turn 32197).
  - At the western edge of the upper dirt plaza (`36, 23`), stepping `Left` from `(36, 23)` onto `(35, 23)` warps down the diagonal stone staircase to `(30, 26)` on the lower plaza (where a wandering Sailor patrols `29-30, 28-30`), leading east along `rows 29-31` to the main **Destino Mine** entrance at **`(39, 28)`** (flanked by a miner at `40, 30` saying *"We miners work hard everyday to dig up resources."* and a wooden signpost at `41, 30` reading verbatim: *"Destino Mine"*, verified Turns 32198-32201).
  - **Lower Plaza Residential House (`25, 30` <-> Interior `5, 51`)**: Reached via the `row 31` sidewalk (`28, 31 -> 25, 31 -> 25, 30`); interior features a woman at `(6, 48)` (*"Hehe... / Bird is the word! / Everyone knows bird is the word"*) and decorative non-enterable stairs at `(1-2, 47)` (verified Turns 32569-32570).
- **Western Destino City (`cols 0-35, rows 18-21`)**:
  - **Professor Elm's Apartment (`33, 18` <-> `5, 9`)**: **Professor Elm** from the Johto region is seated at `(6, 6)` (interacted from `5, 6`) and provides **Special Quest #12 ("Elm's Research")**. Task 1 (`60 species caught`) rewards a **Pokémon Egg** (Turn 33007), Task 2 (`80 species caught`) rewards a second **Pokémon Egg** (Turn 34586), and Task 3 requires **100 species caught**.
  - **Western Apartment (`23, 18` <-> `5, 23`)**: Empty 1F interior with decorative stairs (verified Turn 33004).
  - **Gentleman (`25, 21`)**: *"Back in my day this city used to be even richer! / Then all this fancy technology came and coal became less important!"* (verified Turn 33002).
  - **Route 11 Signboard (`15-16, 19`)**: Interacted from `(17, 19)`, reads verbatim: *"Route 11 / <-------"* (verified Turn 33010).
  - **Far-Western Apartment (`12, 18` <-> `5, 37`)**: Contains a blonde girl at `(7, 34)` (*"Grandma's bolognese is the best in the entire world"*) and her grandmother at `(6, 33)` (*"You know... / The key for good pasta is salting the water before doing anything"*; verified Turn 33011).
  - **Rear Cobblestone Alleyway (`18, 18` -> `20, 14`)**: Diagonal alleyway between the apartment blocks terminates in a decorative dead-end corner at `(20, 14)` (verified Turn 33015).
  - **West Exit to Route 11 (`0, 19-20` <-> Route 11)**: The main western cobblestone street (`rows 19-20`) transitions seamlessly west at `col 0` onto **Route 11**.

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
- **Northern Archway (`50, 41` -> `50, 42` <-> Entrance Cavern `50, 16`)**: Connects back to the southern tunnel doorway of the Main Entrance Cavern (`50, 16`; verified Turn 32227). The eastern side of the chamber (`cols 46-56, rows 40-50`) contains two orange mining machines (`46-48, 43-44` and `52-54, 47-48`) and terminates at the eastern rock wall (`cols 55-56`, verified Turns 32485-32486).
- **Coworker Eddie (`45, 46`, facing South)**:
  - **Pre-Battle Quote**: *"These mining equipment here are really heavy... / Not as heavy as my Pokémon though!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Aron (♀, Lv24; Steel/Rock; Ability: Sturdy; knows Protect and Roar).
    - **Pokémon 2**: Onix (♀, Lv24; Rock/Ground).
  - **Outcome**: Defeat quote: *"B-but my Pokémon"*; awards `₽960` (verified Turns 32232-32242).
- **Western Section (`cols 35-44, rows 41-49`)**:
  - **Overhead Blue Pipe (`col 44`)**: Passable horizontally across `rows 46-49`, solid along `rows 40-45`.
  - **Machop (`43, 44`), Orange Mining Machine (`40-42, 44-45`), & Iron Alcove (`42, 40`)**: Machop stands at `(43, 44)` beside the machine (`"Machop: Chop! Chop!"`, verified Turn 32243). The top-left shovel tip of the orange mining machine at `(40, 44)` has walkable collision (`39, 44 -> 40, 44 -> 40, 42 -> 41, 42 -> 41, 41 -> 42, 41`), allowing access to the bottle sprite at **`(42, 40)`**, which yields **Iron x1** (verified Turn 32582).
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
  - Reached via the double eastbound staircases at `(46, 22-24)` and `(48, 21-23)`; a potion bottle sprite at `(47, 20)` above the middle landing (`47, 22 -> 47, 21`) yields **Hyper Potion x1** (collected Turn 32445). Small rocks at `(49, 25)` and `(54, 18)` (across the overhead blue pipe at `cols 51-52`) are both verified inert (Turns 32351-32352). Connects north along `col 49` (`49, 21 -> 49, 15`) onto the overhead wooden bridge (`cols 35-48, rows 14-16`).
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
- **Siara Grunt 6 (`21, 26`, facing East)**:
  - **Pre-Battle Quote**: *"These machines are actually really handy, I gotta give them that! / Not as handy as my Pokémon though when it comes to destroying kids!"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Mantine (♀, Lv26; Water/Flying; knows Water Pulse).
  - **Outcome**: Defeat quote: *"Noooo!"*; awards `₽2,704` (verified Turn 32402). Post-battle quote: *"This is all wrong... How dare you..."*. Small rocks at `(25, 27)`, `(22, 29)`, and `(20, 26)` are verified inert (Turn 32403).
- **Siara Executive (`27, 30` -> `27, 31`, facing South)**:
  - **Pre-Battle Quote**: *"The heck?! / Weren't there a bunch of grunts guarding the area? / Why does it always end like this..."*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Scyther (♀, Lv25; Bug/Flying; knows Agility).
    - **Pokémon 2**: Wobbuffet (♂, Lv25; Psychic; Ability: Shadow Tag; knows Mirror Coat, Counter, Destiny Bond, and Safeguard).
    - **Pokémon 3**: Umbreon (♂, Lv26; Dark; knows Feint Attack).
  - **Outcome**: Defeat quote: *"Noooo!"*; awards `₽2,704` (verified Turns 32426-32427). Small rocks at `(30, 29)` and `(35, 31)` are inert (verified Turns 32427-32428).
- **Southern Wall Ladder (`31, 29` <-> 1F `19, 36`), Explored Southeastern 2F Corridor, & Far-Eastern Ledge**:
  - The wall ladder at `(31, 29)` warps up to `(19, 36)` on the raised western cliff ledge of Destino Mine 1F (verified Turns 32429-32430), where small rocks at `(16, 34)` and `(17, 33)` are inert (verified Turn 32433) and a miner stands at `(19, 29)` beside a broken mining machine (`20-21, 27-28`, verified Turn 32434).
  - Crossing the 1F overhead wooden bridge (`cols 26-28, row 30`) from `(19, 30)` to `(30, 30)` reaches the 1F upper eastern ledge (small rocks at `30, 29` and `35, 32` both inert, verified Turns 32435 & 32439) and the upper cave archway at **`(35, 28)`**, which enters the **Deep Triple-Staircase Chamber** of Destino Mine at **`(9, 7)`** (exit at `9, 6`, verified Turns 32436-32438).
  - On 2F, a continuous rock ridge along `cols 34-36` separates `(31, 29)` from the southeastern minecart track corridor (`cols 37-47, rows 24-32`, south of Siara Grunt 2 at `41, 21` and Siara Grunt 3 at `47, 23`), where the minecart tracks terminate at `(42, 28)`, the western boulder pocket terminates at `(37, 22)` and `(37, 28)`, and the far-eastern ledge east of the blue pipe (`cols 51-52`) terminates at `(54, 23)` with no sign of Evy on the 2F map (verified Turns 32444-32449).
## Deep Triple-Staircase Chamber (`9, 7` -> `9, 17`) & Inner Den (`12, 19`+)
- **Triple-Staircase Passage (`9, 7` -> `9, 17`)**: Entered from the 1F upper eastern cave archway (`35, 28` <-> `9, 6`). Stepping onto the second landing at `(9, 13)` triggers a tremor from the southern den (`"It came from that den! / Frio must be in there already... Let's go!"`, verified Turn 32456). Stepping south off `(9, 17)` (`▼` at `9, 18`) enters the **Inner Den** at **`(12, 19)`** (verified Turn 32461).
- **Inner Den (`12, 19` <-> Triple-Staircase Chamber `9, 17`)**:
  - Stepping north onto `(12, 18)` triggers the confrontation with **Frio** (`14, 14`) and four **Team Siara Grunts** digging up fossils to resurrect and Eclipse ancient Pokémon for Marie (Turns 32462-32472).
  - After Frio defeats all four grunts, Asher calms and reverts the **Eclipsed Tyranitar** released by the retreating grunts, Frio pulls Valora away from a falling rock at `(14, 16)` before departing, and Asher collects the **Clear Shard** at `(14, 16)` before automatically exiting to `(9, 17)` in the Triple-Staircase Chamber (verified Turns 32466-32472).
  - **Quest #6 ("Lost Eevee") Audit (`1F`, `2F`, & `Inner Den`)**: Re-entering the Inner Den (`12, 19`) and auditing all accessible tiles of 1F, 2F (`cols 19-54, rows 9-32`), and the Inner Den after the Team Siara fossil cutscene confirms that Team Siara has vacated and no Eevee sprite is present in the currently accessible mine chambers (verified Turns 32580-32609); Quest #6 was paused with the Explorer at `(42, 12)` in Turn 32613 (`"If you have something else to do, you can leave, don't worry about me. / Wanna leave? Yes"`) to keep the single active quest slot open for Route 12 and Jarro Town.

<hr>

<h1><code>Locations/Galinor_City</code></h1>

# Galinor City (Bugiaret Island)

## Geography & Connections
- **East (`69, 48-49` <-> Route 11 Main `0, 20-21`)**: Seamless map border connecting the western approach of **Galtino Bridge (Route 11)** onto the eastern trail of **Galinor City** at `(69, 48-49)` (verified Turn 33037).
- **West (`0, 59-60` <-> Route 9 `71, 19-20`)**: Seamless western boulevard border connecting **Route 9** into **Galinor City** at `(0, 59-60)` (verified Turn 34252).
- **Town Signboard (`52-53, 46`)**: Interacted from `(53, 47)`, reads verbatim: *"Galinor City / The luxury resort city"* (verified Turn 33039).
- **Eastern Arrival Cutscene (`47, 47`, Turn 33041)**: Stepping west onto `(47, 47)` triggers a cutscene with **Valora** and a HuPhone text message from **Dad** instructing Asher and Valora to find **Harry** waiting for them at the **Cargo Loading Bay**.
- **Cargo Container Yard (`cols 43-59, rows 35-45`)**:
  - **Police Officer (`46, 41-43`, patrolling)**: Patrols the central cobblestone avenue (`cols 46-48`).
  - **Quest #10 Provider ("Push it!", `54, 41`)**: Sailor with a side-quest icon standing among the green shipping containers at `(54, 41)` (verified Turn 33043).
- **Galinor Cargo Loading Bay (`48, 32` Signboard & `cols 46-48, rows 15-31` Bridge)**:
  - **Signboard (`48, 32`)**: Interacted from `(48, 33)`, reads verbatim: *"Galinor Cargo Loading Bay"* (verified Turn 33044).
  - **Wooden Bridge (`cols 46-48, rows 15-31`)**: Connects north from `(47, 32)` across the channel onto the northern headland (`47, 12`), where a dirt path runs west along `rows 11-12`.
  - **Northern Headland Sailor (`32, 11`) & Dive Ball (`35, 6`)**: Sailor at `(32, 11)` stands beside a round boulder (`31, 9`) and shipping containers (*"Whew... lifting this was a real workout... / Haha, you should see the surprised look on your face! / Nah, we lift these containers with the help of Pokémon and equipment from the cargo ships."*, verified Turn 33048). Walking north up the 1-tile gap at `column 35` (`35, 11 -> 35, 7`) to the item ball at **`(35, 6)`** yields **Dive Ball x1** (verified Turn 33048).
  - **Western Pier (`cols 17-22, rows 14-21`)**: Accessed via the ramp at `(21, 14)` beside the Sailor at `(21, 12)`. Behind the green shipping container (`cols 18-20, rows 16-19`), a stone sprite at **`(18, 20)`** yields **Water Stone x1** (interacted from `19, 20`; verified Turn 33054).
  - **Middle Pier (`cols 26-31, rows 14-21`)**: Accessed via the ramp at `row 14` (`cols 27-30`); **Harry** waits at `(28, 19)` in front of his ship (`28, 20`). Speaking to Harry from `(28, 18)` triggers the cutscene with Valora, Dad, and Professor Ivo and sails to **Solare Island** (`36, 51`, Turns 33057-33060).
## Southern Boulevard & Galinor Metro Station (`32, 59`)
- **Galinor Metro Station (`32, 58`, exits to `32, 59`)**: Unlocked on the Hupest Metro Line destination menu (`4: Galinor`) after winning Round Six of the Eclipse Tournament (verified Turn 33919). Entering from `(32, 59 -> 32, 58)` spawns at `(22, 24)` inside the station; walking `Left 5` to `(17, 24)` and `Up 4` straight up `column 17` (`17, 24 -> 17, 20`) steps directly into the Hupest Metro Line boarding turnstile at **`(17, 20)`** between the west ticket booth and central scanner pillar (whereas `19, 20` is the exit-only lane; verified Turns 34261-34263 & 34542-34544).
- **Galinor City Pokémon Center (`28, 58`, exits to `28, 59`)**: Located immediately west of the Galinor Metro Station on the southern boulevard.
- **Western Boulevard Signboard (`24-25, 59`)**: Interacted from `(25, 60)`, reads verbatim: *"Galinor Metro Station / ---> / Route 9 / <---"* (verified Turn 33924).
- **Southwestern Avenue (`cols 18-19, rows 60-75`) & Route 13 Border (`14-15, 86` <-> Route 13 `14-15, 0`)**: Following `column 18` south to `(18, 75)` and `column 14` south from `(14, 75)` transitions seamlessly at `(14, 86)` onto **Route 13** `(14, 0)` (verified Turn 33927).

<hr>

<h1><code>Locations/Hupest_Sea</code></h1>

# Hupest Sea (South of Maple Town — Location 3)

## Geography & Connections
- **North (`27, 0` <-> Maple Town `42, 40`)**: Seamless northern sea border connecting the southeastern sea channel of **Maple Town** (`43, 18` -> `42, 39`) onto **Hupest Sea** at `(27, 0)` (verified Turn 34316).
## Landmarks, Trainers & Points of Interest
- **Northern Rock Clusters (`28-30, 4-5` & `27-29, 6-7`)**: Brown ocean rock formations just south of the Maple Town channel border (`27, 0`), with a clear vertical sea lane along `column 26` (verified Turn 34317).
- **Northern Swimmers**:
  - **Male Swimmer (`21, 8`)**: Stationed west of the northern rock cluster (observed Turn 34317).
  - **Female Swimmer (`31-32, 7`)**: Swims horizontally east of the northern rock cluster (observed Turn 34317).
- **Central Sandbar (`cols 19-28, rows 12-16`)**:
  - **Single Tall Grass Tile (`21, 13`)**: Located near the northwest curve of the sandbar.
  - **Fisherman 1 (`26, 14`)**: Faces north at the eastern notch of the sandbar (cannot be spoken to directly from the water tile `26, 13` without dismounting onto land, verified Turn 34319).
  - **Fisherman 2 (`20, 15`)**: Faces south near the western edge of the sandbar (observed Turn 34319).
  - **Small Rock (`27, 15`)**: Located on the southeastern tip of the sandbar.
- **Eastern Grassy Sandbar (`34, 15-17`)**: Features a red item ball at `(34, 16)` inside a small patch of grass (observed Turn 34321).
- **Mid-Sea Rock Gap (`cols 26-28, rows 23-27`)**:
  - **Swimmer♂ Avery (`26, 23`)**:
    - **Pre-Battle Quote**: *"Swift! Swift faster!"*
    - **Team (3 Pokémon)**: Seadra (♀, Lv39; Water; `1294 EXP`), Floatzel (♀, Lv39; Water; Ability: Drizzle; `1444 EXP`), Jellicent (♂, Lv39; Water/Ghost; `1404 EXP`).
    - **Outcome**: Defeated in Turns 34328-34334 (*"One more lap"*; awards `₽468`).

## Wild Pokémon Encounters (Surfing)
- **Wailmer** (♂, Lv31; Water; caught in 2nd Ultra Ball at `27, 23` in Turn 34326, nicknamed **Baleen**, transferred to Box 3; brings PokéDex Owned count to **79**).
- **Small Offshore Isle (Location 3 — `cols 24-38, rows 32-48`)**:
  - **Western Landing (`25-26, 40-43`) & Hidden Canopy Path (`30, 44-45 -> 31, 45`)**: From `(26, 42)`, walking `Right 4` to `(30, 42)`, `Down 3` through the overlapping tree canopies at `(30, 44)` and `(30, 45)`, and `Right 1` to `(31, 45)` leads directly onto the southeastern terrace (verified Turn 34371).
  - **Northeastern Clearing (`32-37, 34-36`)**: Reached by surfing around the northern coast (`row 31-32`) and dismounting at `(37, 34)`; contains **TM27 (Return)** in a gold item ball at `(32, 36)` above a south-facing cliff (`32-40, 37-39`, collected Turn 34362).
  - **Southeastern Terrace & Cave Entrance**:
    - **Professor Ivo (`36, 46`)**: Waiting on the southeastern grass terrace below the cliff staircase (`33, 44-45`).
    - **Dad / Jackson (`36, 42`)**: Standing on the upper plateau in front of the **cave entrance (`36, 40`)** leading down to the abandoned undersea Team Siara laboratory.
- **Tentacruel** (♀, Lv27; Water/Poison; caught in Ultra Ball at `27, 31` in Turn 34356, nicknamed **Medusa**, transferred to Box 3; brings PokéDex Owned count to **80**, fulfilling Task 2 of Special Quest #12 `"Elm's Research"`).
- **Small Offshore Isle Reunion & Newly Opened Cave Entrance (`32, 46` -> `33, 46`, Turns 34372-34373)**:
  - Stepping onto `(32, 46)` triggers the reunion with **Professor Ivo** (`36, 46`), **Valora** (`32, 47`), and **Dad (Jackson)** (`36, 42`).
  - When Asher relays Frio's revelation about an abandoned undersea Team Siara laboratory, Professor Ivo shows them a newly opened hole/cave entrance (`36, 40`) that wasn't there during her earlier research with Valora, realizing Team Siara has most likely already broken into the old laboratory below.
  - Professor Ivo, Valora, and Dad enter the cave (`36, 40`), leaving Asher at `(33, 46)` (`Right 3, Up 6` climbs the stairs at `35-36, 44-45` into the cave entrance `36, 40`).
## Location 3 Cave Passage (Undersea Lab Approach)
- **Entrance (`13, 11` <-> Small Offshore Isle `36, 40`)**: Stepping `Down` off `(13, 11)` exits back to `(36, 40)` on the Small Offshore Isle (verified Turn 34375).
- **Three Consecutive Descending Wooden Staircases (`20, 9 -> 26, 12`)**:
  - **Staircase 1**: `(20, 9) -> Right 2 -> (22, 10)` (verified Turn 34378).
  - **Staircase 2**: `(22, 10) -> Right 2 -> (24, 11)` (verified Turn 34379).
  - **Staircase 3**: `(24, 11) -> Right 2 -> (26, 12)` (verified Turn 34379).
- **Orange Mining Machine & Northern Archway (`27-30, 6-12`)**:
  - An abandoned Team Siara orange mining machine sits at `(28-30, 11-12)`.
  - Walking `Up 2` from `(27, 12)` to `(27, 10)` and `Right 1` to `(28, 10)`, then `Up 2` onto `(28, 8)` under the wooden support archway warps to `(5, 15)` in the Undersea Laboratory Stairwell (verified Turn 34381).
## Undersea Laboratory Stairwell (`5, 15` -> `5, 4`)
- **Entrance (`5, 15` <-> Location 3 Cave Passage `28, 8`)**: Stepping `Down` off `(5, 15)` exits back to the cave passage (verified Turn 34382).
- **Elevator Doorway Cutscene (`5, 7` -> `5, 4`, Turns 34382-34384)**:
  - Stepping north onto `(5, 7)` triggers a cutscene with **Professor Ivo** (`5, 4`), **Dad (Jackson)** (`3, 5`), and **Valora** (`6, 6`).
  - Professor Ivo notes that despite the lab being at least 10 years old, the electricity is still running. Dad repairs the jammed elevator panel at `(4, 4)`, and Ivo, Dad, and Valora enter the elevator doorway at `(5, 4)`.
  - Stepping `Up` into `(5, 4)` enters the **Abandoned Undersea Laboratory Elevator** (`6, 15`), which automatically prompts: *"Choose the floor you would like to enter!"* (`5F`, `4F`, `3F`, `2F`, `1F`).

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

<h1><code>Locations/Jarro_Town</code></h1>

# Jarro Town

## Geography & Connections
- **Southern Entrance (`10-12, 39` <-> Route 12 Main `10-12, 0`)**: Seamless transition at the southern lantern-lined path (`cols 10-12, row 39`) from the northern gateway arch of **Route 12 Main** (`10-12, 0`, verified Turn 32903).

## Landmarks, Facilities & Key Events
- **Jarro Town Pokémon Center (`14, 28`)**: Located along the southern entrance avenue (`col 11 -> row 29 -> 14, 28`).
  - **Nurse Joy (`7, 2`, counter at `7, 4`)**: Healed party and registered checkpoint in Turn 32914.
  - **Patron (`8, 6`)**: *"You can't become a good Trainer with just one strong Pokémon. / But raising many Pokémon evenly is no easy task, either."* (verified Turn 32915).
  - **Encounter with Sinnoh Champion Cynthia & The Odd Keystone (`14, 29` -> `14, 30`, Turns 32905-32912)**: Stepping onto `(14, 29)` outside the Pokémon Center door triggers a cutscene where **Cynthia**, Champion of the Sinnoh Region, exits the Pokémon Center (`14, 29`). She explains that she was invited as a special guest to watch the **Eclipse Tournament**, came to Jarro Town because of the **Ancient Hupestian Ruins**, and noticed Asher's battles as having greater potential than even the other standout competitors (Frio and Valora). Before departing south toward Route 12, Cynthia gifts Asher the **Odd Keystone** (stored in the Items Pocket; fits the ancient stone tower in the secret Route 6 section of Destino Mine 1F).
- **Town Signboard (`17-18, 29`)**: Interacted from `(16, 29)` or `(17-18, 30)`, reads verbatim: *"Jarro Town / Highest of Hupest"* (verified Turn 32916).
- **Southern Entrance Woman NPC (`16, 31`)**: Standing beside the lamppost southeast of the Pokémon Center (*"Jarro is such a quiet little town!"*, verified Turn 32917).
- **Old Gentleman & Zangoose (`20, 29` & `21, 29`)**: Standing outside the West Cabin (`22, 28` door) east of the Pokémon Center (*"I used to be a Pokémon Trainer in my youngest days... / With my partner Zangoose we defeated every opponent!"*; Zangoose: *"Zan Zan!"*, verified Turns 32917-32918).
- **West Cabin (`22, 28` <-> `6, 51`)**:
  - **Seated Father (`6, 48`)**: *"Going to a store from here is such a pain."* (verified Turn 32920).
  - **Little Blonde Girl (`3, 50`)**: *"Oh my... / The almighty fridge has no milk... / Dad! We need to get some milk!"* (verified Turn 32920).
- **Central Stone Staircase (`24-26, 24-26`)**: Leads north between the West Cabin (`22, 28`) and East Cabin (`29, 28`) toward the upper level of Jarro Town.
- **Hiker Outside East Cabin (`27, 29` <-> `28, 30`, wandering)**: *"Fresh air, nature everywhere... / The perfect place to live!"* (verified Turn 32921). Wanders in the area south of the East Cabin (`26-28, 29-30`); when he stands at `(27, 29)`, he temporarily blocks the narrow 1-tile bottleneck between the East Cabin wall (`27, 28`) and the lamppost (`27, 30-32`) until he steps aside to `(28, 30)` (verified Turn 32931).
- **Middle Terrace (`rows 14-23`, reached via Central Stone Staircase `24-26, 24-26`)**:
  - **Quest #9 Provider ("Angry Cubone Kid", `22, 15`)**: Boy in a brown cap standing in front of a fenced snow pen containing a **Cubone** (`23, 13`).
  - **Northwest Cabin (`18, 15` <-> `6, 37`)**: Empty interior (likely belongs to the boy outside at `22, 15`; verified Turn 32929).
  - **Police Officer (`15, 17`, facing East)**: *"Being a police officer in such a quiet little town is such an easy and calm job..."* (verified Turn 32930).
  - **Upper Ridge & Northeast Cabin (`29-30, 18-19` Staircase)**: A rugged rock at `(31, 14)` blocks access to the Northeast Cabin until rock-smashing equipment is obtained (verified Turn 32931).
- **East Cabin (`29, 28` <-> `6, 23`)**: Contains a **Meowth** (`5, 20-21`; *"Meowth: Meooooow"*) and a wandering **Old Woman** (`8-9, 20-22`; verified Turns 32933-32935).
- **Ecly Festival Lantern Path (`cols 33-38, rows 21-31`)**:
  - **Ecly Festival Signboard (`33, 29`)**: Interacted from `(32, 29)`, reads verbatim: *"Ecly Festival / Held every year here in Jarro Town / Be sure to bring your friends!"* (verified Turn 32937).
  - **Festival Girl (`33-34, 31`, wandering)**: *"The Ecly Festival... / I love that festival so much! / I feel all young nostalgic..."* (verified Turn 32938).
  - **Explorer (`35, 25`)**: Standing under the festival lanterns south of the ruins entrance (*"The Ancient Hupestian Ruins..."*, verified Turn 32939).
  - **Ancient Hupestian Ruins Signboard (`34, 21`) & Entrance (`36, 20-21`)**: Signboard at `(34, 21)` (interacted from `34, 22`) reads verbatim: *"Ancient Hupestian Ruins"* (verified Turns 32939-32940). Inside (`15, 13`), Professor Ivo translated the three-part **Eklissi Prophecy** inscribed beneath the three wall murals before returning to her laboratory in Lancio Town (verified Turns 32941-32946). Stepping south onto `(36, 29)` afterward triggers the Round 4 HuPhone summons from the Amor Battle Center and fast-travels the player to `(25, 109)` on Route 12 Main (verified Turns 32948-32949).

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

<h1><code>Locations/Maple_Town</code></h1>

# Maple Town (Bugiaret Island)

## Geography & Connections
- **North (`28-30, 0` <-> Route 13 `48-50, 49`)**: Seamless northern border connecting the southern dirt road of **Route 13** onto the main northern road of **Maple Town** at `(28-30, 0)` (verified Turn 34046).
- **West (`0, 16-17` <-> Route 8 `59, 20-21`)**: Seamless western border road leading onto **Route 8** (verified Turn 34089); marked by the wooden signboard at `(1-2, 16)` (interacted from `2, 17`), which reads verbatim: *"Route 8 / <------"* (verified Turn 34074).
- **Maple Town Pokémon Center (`34, 10`, exits to `34, 10-11`)**: Located on the east side of the northern entrance road (`cols 32-36, rows 6-10`); a short wooden fence at `(31-32, 9-10)` sits to the left of the building, so the entrance door at `(34, 10)` is reached via `row 11` (`30, 11 -> 34, 11 -> 34, 10`, verified Turn 34056).
  - **Ground Floor**: Nurse Joy at `(7, 2)` (counter at `7, 4`; healed and registered checkpoint in Turn 34056); trainer at `(8, 5)` (*"Pokémon can still learn techniques after canceling evolution. Evolution can wait until new moves have been learned."*, verified Turn 34058); mezzanine stairs at `(2, 1)` -> `Up 4` to `(5, 6)`.
  - **Mezzanine PokéMart (`5, 5`)**: Sells standard PokéMart supplies including **Ultra Balls** (`₽1200`; purchased 30 in Turn 34063).
- **Maple Town Signboard (`38-39, 10`)**: Interacted from `(38, 11)`, reads verbatim: *"Maple Town / The village of agriculture!"* (verified Turn 34067).
- **Northeastern Garden Stalls (`cols 41-47, rows 6-13`, accessed via `41, 10-11`)**:
  - **Pokémon Move Maniac / Move Reminder (`44, 8`)**: Female Farmer who teaches forgotten level-up moves in exchange for **two TinyMushrooms** or **one Big Mushroom** (*"I'm the Pokémon Move Maniac. I know every single move that Pokémon learn growing up. I'm also a mushroom maniac. Bring me two Tinymushrooms, or one Big Mushroom."*, verified Turn 34067).
  - **Move Deleter (`44, 6`)**: Male Farmer behind the Move Maniac whose herbs make Pokémon forget moves (*"Hi! My herbs can delete moves! I can make Pokémon forget their moves."*, verified Turn 34068).
- **Maple Farm Signpost (`20, 15`)**: Interacted from `(20, 16)` beside the broken fence twigs (`21, 14-15`), reads verbatim: *"Maple Farm"* (verified Turn 34071).
- **Southern Maple Town Courtyard (`cols 12-27, rows 18-27`) & Shoreline (`rows 28-30`)**:
  - **Eastern House (`25, 23`, interior exit mat at `21-22, 10`)**: Contains a male Farmer at `(19-20, 5)`, a female Farmer at `(23, 5)`, a wandering Meowth/Persian (`16-19, 5-6`), and a decorative northern wall staircase graphic (`18, 2-3`; verified non-warping in Turn 34086).
  - **Western House (`15, 23`, interior exit mat at `6, 10`)**: Reached from the central avenue via the log fence gap at `(18, 24)` -> `(17, 24)` -> walkable wheat top-tips `(17, 25) -> (15, 25)` -> `(15, 24) -> (15, 23)` (bypassing the solid wheat stalk at `16, 22-24`). Contains a wandering female Farmer at `(5-6, 4-5)` with a Meowth (`1, 7`) and an Eevee (`3, 6`; verified Turns 34083-34084).
  - **Southeastern Road (`cols 20-26, rows 25-26`)**: Branches east from `(20, 25-26)` south of the Eastern House and terminates at trees (`27-30, 17-27`).
  - **Southern Shoreline Cliff Staircase (`15-17, 29`) & Fence Gap (`31-32, 27`)**: Observed south of the `row 27` fence overlooking the southern coast (Turn 34085).
- **Townsfolk & NPCs**:
  - **Female Farmer (`16-17, 18`)**: *"Maple Town provides a huge portion of Hupest's food supplies"* (verified Turn 34071).
  - **Male Farmer (`9-10, 15-16`)**: *"Only the best of quality here, when it comes to the crops."* (verified Turn 34073).

## Story Events
- **Reunion with Dad, Professor Ivo & Valora & Frio's Eavesdropping (`29, 7`, Turns 34046-34049)**: Stepping south onto `(29, 7)` triggers the reunion cutscene with Valora (`28, 7`), Dad (`28, 9`), and Professor Ivo. When Professor Ivo explains that the third energy signal is underwater and they need specific clues to locate it, Valora and Asher spot **Frio** eavesdropping at `(28, 12)`. Frio recognizes the underwater location (*"Underwater location? No... They can't be talking about that damn place..."*), realizes he made eye contact with them, and walks west into Maple Town along `row 12`.
- **Southeastern Shoreline Staircase (`43, 15` -> `43, 18` Water Border)**: Unlocked after winning Round 7 when Professor Ivo texts Asher to come to the small isle south of Maple Town (`Turns 34312-34315`). Stepping `Down 2` from `(43, 15)` to `(43, 17)` reaches the shoreline border at `(43, 18)`, where FastSwift launches south into the sea channel (`cols 42-46`). When returning from Hupest Sea to `(43, 17)`, `row 14` (`43, 14 -> 45, 14 -> 37, 14`, across the walkable top edge of the twigs and wooden fence) leads cleanly out to `(37, 11)` and the Maple Town Pokémon Center at `(34, 10)` (verified Turns 34520-34521).

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

<h1><code>Locations/Mulberry_Town</code></h1>

# Mulberry Town (Bugiaret Island)

## Geography & Connections
- **East (`21, 10-11` <-> Route 8 `0, 8-9`)**: Seamless eastern border connecting the western road of **Route 8** into **Mulberry Town** at `(21, 10-11)` (verified Turn 34168).
- **North (`4-5, 0` <-> Route 9 `6-7, 39`)**: Seamless northern sandy trail connecting **Mulberry Town** north onto **Route 9** at `(6-7, 39)` (verified Turn 34196).
- **Mulberry Town Pokémon Center (`15, 9`, exits to `15, 10`)**: Located on the north side of the eastern entrance road (`cols 13-17, rows 5-9`). Nurse Joy at `(7, 2)` (counter at `7, 4`; healed party and registered active respawn checkpoint in Turn 34169).
- **Mulberry Town Signboard (`6-7, 10`)**: Interacted from `(7, 11)`, reads verbatim: *"Mulberry Town / The twin of Maple"* (verified Turn 34173).
- **Farmer (`10-12, 11-14`, patrolling central avenue)**: *"Ahh Mulberry Town... / Such a quiet town. / Almost as if it was the beginning of something.."* (verified Turn 34196).
## Story Events
- **Frio's Wager & Round Seven Summons (`11, 18` -> `11, 17`, Turns 34175-34179)**: Stepping onto `(11, 18)` in the southern plaza triggers a cutscene with **Valora** (`12, 18`) and **Frio** (who exits the Western House at `8, 17`). Hearing about Team Siara, the stolen gems, and the underwater Location 3 signal fills Frio with terror. When the **Amor Battle Center** texts all three trainers to announce **Round Seven of the Eclipse Tournament**, Frio promises to tell Asher and Valora what he knows about the underwater location if Asher wins Round 7, and advises taking **Route 9** north to **Galinor City** to catch the Metro back to Amor City.
- **Western House (`8, 17`, exits to `8, 18`; Signpost at `9, 18`)**:
  - **Signpost (`9, 18`)**: Interacted from `(9, 19)` outside the house Frio exited (`8, 17`), reads verbatim: *"For sale! / Call 515-808-2362 for details."* (verified Turn 34181).
  - **1F (`6, 8` Exit Mat & `6, 2` Upstairs Mat)**: Unoccupied house; walking `Left 1` from `(6, 8)` to `(5, 8)`, `Up 6` to `(5, 2)`, and `Right 2` across the red mat `(6, 2)` onto the stairs `(7, 2)` warps to **2F** at `(22, 3)` (verified Turn 34182).
  - **2F (`22, 3` Arrival Mat & Eclite Shard at `19, 6`)**: Contains a golden item ball on the bedroom rug at **`(19, 6)`** yielding a fully powered **Eclite Shard x1** (interacted from `19, 7`; verified Turn 34184), confirming the house's connection to Frio's Eclipser family heritage.
- **Eastern House (`16, 17`, exits to `16, 18`; interior exit mat at `36, 8`)**:
  - **In-Game Trade Resident (`35, 5`)**: Male NPC seated at the table who offers to trade his **Rhydon** for a **Lairon** (*"Hello, there! Do you happen to have a Lairon? / Would you agree to a trade for my Rhydon?"*, verified Turns 34189-34190).
- **Townswoman (`14, 19-20`, wandering in southern plaza)**: Recounts the tragedy of Frio's biological parents who lived in the Western House (`8, 17`): *"That boy... Apparently he was the son of the couple who lived next to us. One day, they disappeared, along with their kid. I heard he was adopted, but his parents were never seen again... Rumors say the family was attacked by weird Pokémon, and they saved their child instead of themselves. 'sniff' Such a terrible, yet wholesome story"* (verified Turns 34191-34193).

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

<h1><code>Locations/Route_11</code></h1>

# Route 11

## Geography & Connections
- **Route 11 Eastern Approach (`0-11, 18-20`)**:
  - **East (`11, 19-20` <-> Destino City `0, 19-20`)**: Seamless map border connecting the western cobblestone street of **Destino City** (`0, 19-20`) onto **Route 11 Eastern Approach** at `(11, 19-20)` (verified Turn 33016).
  - **Signboard (`3-4, 18`)**: Interacted from `(5, 18)`, reads verbatim: *"Route 11 / The trail to Bugiaret Island"* (verified Turn 33018).
  - **West (`0, 19-20` <-> Route 11 Main `76, 21-22`)**: Seamless map border connecting the 12-column eastern approach onto **Route 11 Main** at `(76, 21-22)` (verified Turn 33018).
- **Route 11 Main & Galtino Bridge (`cols 0-76`)**:
  - **Galtino Bridge Signboard (`66-67, 19`)**: Interacted from `(66, 20)`, reads verbatim: *"Galtino Bridge / <------"* (verified Turn 33021).
  - **Southern Coastal Cliff & Beach Ledge (`cols 59-67, rows 22-32`)**:
    - Side-facing wooden staircase at `(61, 28-30)` (approached along `row 29`: `62, 29 <-> 60, 29`) leads down to the western beach ledge where a purple bottle sprite at **`(60, 27)`** yields **Carbos x1** (interacted from `60, 28`; verified Turn 33024).
  - **Galtino Bridge Cutscene & Boss Eclipsed Pidgeot (`53, 20` -> `46, 20`, Turns 33028-33034)**:
    - Stepping onto `(53, 20)` triggers a cutscene where **Dawn** (from Sinnoh) confronts three **Team Siara Grunts** blocking the bridge, who release a boss **Lv34 Eclipsed Pidgeot** (`859 EXP`; resists Fighting-type moves) as a diversion before fleeing west.
  - **Galtino Bridge Midpoint Signboard (`35-36, 18`)**: Interacted from `(34, 18)`, reads verbatim: *"Galtino Bridge / Galinor City        Destino City / <-------                 ------->"* (verified Turn 33036), beside a green-haired boy at `(29, 20)` (*"Wow, you must be a strong trainer!"*, Turn 33035), a woman at `(32, 20)`, and a straw-hat boy around `(26, 18-21)`.
  - **West (`0, 20-21` <-> Galinor City `69, 48-49`)**: Crossing the western arch of Galtino Bridge (`9, 21-22`) and walking west across `col 0` seamlessly transitions into **Galinor City** at `(69, 48-49)` (verified Turn 33037).

<hr>

<h1><code>Locations/Route_12</code></h1>

# Route 12

## Geography & Connections
- **Two-Segment Structure**:
  - **Route 12 Eastern Approach (`28, 6` <-> `9, 0`)**: Connects at the east (`28, 6 <-> 29, 6` <-> Route 12 Gatehouse `1, 7 <-> 14, 7` <-> Amor City North `7, 12`, verified Turn 32629), features a wooden signboard at `(12-13, 5)` (interacted from `13, 6`, reading verbatim: *"Route 12 / <-------"*, verified Turn 32631), and transitions seamlessly at the north (`9, 0`) onto **Route 12 Main** (`33, 118`, verified Turn 32631).
  - **Route 12 Main (`33, 118` <-> `10-12, 0`)**: Main mountain route corridor climbing from `(33, 118)` at the south to the **Jarro Town** wooden gateway arch (`10-12, 0-3`) at the north.
    - **Southern Signboard (`28-29, 109`)**: Interacted from `(28, 110)`, reads verbatim: *"Route 12 / Border of the Cest Mountain System"*, beside a northbound wooden staircase at `(25-26, 108)` (verified Turn 32633).
    - **Northern Signboard (`14-15, 3`)**: Interacted from `(14, 4)`, reads verbatim: *"North: Jarro Town / South: Amor City"* (verified Turn 32902).
## Wild Pokémon
- **Teddiursa**: Encountered at Lv17 (♂, Normal) in the tall grass at `(18, 97)` on Route 12 Main (caught in a Poké Ball, nicknamed **Ursa**, and transferred to Box 2 as 62nd Owned species in Turns 32652-32654).
- **Staravia**: Encountered at Lv17 (♂, Normal/Flying) at `(29, 85)` and Lv19 (♀) at `(18, 54)` in the tall grass on Route 12 Main (verified Turns 32700 & 32802).
- **Spearow**: Encountered at Lv17 (♀, Normal/Flying) at `(22, 44)` and Lv18 (♀) at `(29, 14)` in the tall grass on Route 12 Main (verified Turns 32834 & 32884).
## Trainers, Landmarks & Items (Route 12 Main)
- **Side-Quest Provider NPC (`16, 75` — Quest #8 "Valentines Gift")**: Chubby boy in blue overalls standing on the upper cliff plateau at `(16, 75)` (reached via the overhead bridge `35, 69 -> 18, 69` and western path `13, 70-73 -> 14, 73 -> 15, 74-75`). Accepting his quest (*"I made a bonquet of different flowers for the girl I like, but on my way to Amor City to visit her, wind made my flowers fly away... I think there is six missing... I'll look for three, I will leave the other three to you!"*, Turn 32745) tasks the player with finding 3 missing flowers (`Flower 1`, `Flower 2`, `Flower 3`, which use standard red/white Poké Ball item sprites):
  - **Flower 3 (`18, 47`)**: Standard Poké Ball sprite tucked in the tree nook south of the `(16, 43-45)` side-facing staircase (collected from `18, 46` into Key Items Pocket in Turn 32835).
- **Link Cable (`23, 10` — Yellow/Orange Capsule Sprite)**: Tucked behind the rock cones `(21, 10)`, `(22, 10)`, and `(22, 11)` (collected from `24, 10` into Items Pocket in Turn 32884 via `row 10` behind the passable tree canopy at `27-28, 10`).
- **Wandering Gentleman NPC (`13, 14` -> `14, 13`)**: Non-hostile hat-wearing NPC at the top of the `(12-14, 17-18)` staircase (*"At this altitude there aren't many people living around... However, there is this one town nearby... Jarro Town I think."*, verified Turn 32872).
- **Northern Southbound Shortcut Staircase (`11-13, 7-8`) & One-Way Ledge (`10-14, 10`)**: Located north of `(10, 11)`; bypassed by heading east along `row 11-12` (`cols 10-22`) and around the pine trees via `row 17` and `col 29` (verified Turns 32874-32877).
- **Trainer Tips Signboard (`24, 43`)**: Located in the tall grass at `(24, 43)` (interacted from `24, 44`, reads verbatim: *"Trainer Tips! / You can jump down from small ledges in order to take shortcuts!"*, verified Turn 32833).
- **Burn Heal (`33, 46` — Spray Bottle Sprite)**: Located on the eastern nook of the middle-upper cliff terrace (`33, 46`, collected from `32, 46` in Turn 32830).
- **X Special (`19, 19` — Capsule Sprite)**: Tucked to the right of the `(18, 19)` rock cone; reached by walking behind the passable top canopy of the pine tree at `(19, 20)` from `(18, 20)` and pressing `A` facing `Up` (collected in Turn 32870).
- **Upper Rugged Rocks (`22, 20` & `23, 19`)**: Block the small eastern cliff nook at `(23, 20)` until rock-smashing equipment is obtained (observed Turn 32870).
- **Southbound Shortcut Staircase (`32-34, 88-89`) & One-Way Ledge (`32-34, 91`)**: Located on the southeastern edge of the middle terrace; leads south over a one-way ledge at `(32-34, 91)` back down to Bird Keeper Jett's terrace (verified Turn 32703).
- **Rock Cones (`24, 104`, `34, 98`, `39, 98`, `20, 92`, `37, 68`, `16, 66`, `35, 62`, `11, 56`, `16, 54`, `36, 23`, `18, 19`, `22, 11`, & `37, 4`)**: Twelve are inert (Turns 32634, 32641, 32663, 32712, 32740, 32773, 32774, 32827, 32869, 32876, & 32900), while the rock cone at **`(35, 62)`** contains a hidden **Revive** (collected from `34, 62` in Turn 32758).
- **Upper Eastern Ascent & Western Connecting Staircases (`rows 21-51`)**:
  - **Northbound Eastern Corridor (`cols 34-36, rows 41-52`)**: Bypasses the `(25-27, 51)` one-way ledge east of Nurse Joy (`28, 52`) via `col 35` (`rows 42-50`) and `col 36` (`rows 39-43`), guarded by Lass Wanda (`37, 48`) and Cooltrainer Joely (`41, 41`).
  - **Upper Eastern Staircases (`39-41, 35-36` & `39-41, 29`)**: Climb to the upper eastern terrace (`rows 24-28`), where a southbound shortcut staircase (`31-33, 21-22`) and one-way ledge (`31-33, 24`) sit west of the inert rock cone at `(36, 23)`.
  - **Western Connecting Staircase (`26-28, 37`) & Side-Facing Ridge Staircase (`16, 43-45`)**: Reached by walking south from `(29, 25)` along `col 28` (`rows 26-36`); descends to the middle-upper terrace (containing the Burn Heal at `33, 46`, Trainer Tips sign at `24, 43`, southbound shortcut staircase `25-27, 48-49` above ledge `25-27, 51`, and `Flower 3` at `18, 47`) and climbs west via `(16, 44)` onto the western ridge (`cols 6-18, rows 27-46`).
- **Patrolling Girl NPC (`12-14, 57-59`)**: Non-hostile hiker girl catching her breath north of the staircase `(12-14, 62)` (*"Huff huff... I'm so exhausted! This mountain is huge!"*, verified Turn 32771).
- **Overhead Wooden Bridge (`18-35, 68-70`) & Under-Bridge Item Ball (`33, 71` — Ultra Ball)**: Reached via the eastern staircases at `(39-41, 81)` and `(39-41, 72-75)`; crosses over the lower path (`19-33, 71-73`) where the item ball at `(33, 71)` contains an **Ultra Ball** (collected from `(32, 71)` via `row 71` in Turn 32754).
- **Rugged Rock (`20, 76`) & Item Ball (`21, 76`)**: Located on a middle cliff ledge reached via the east-facing staircase at `(18, 75-76)`; the rugged rock at `(20, 76)` blocks access to the item ball at `(21, 76)` until rock-smashing equipment is obtained (observed Turn 32667).
- **Hiker Calum (`29, 104`, facing South)**:
  - **Pre-Battle Quote**: *"I'm going for a hike but I need some motivation... / Can my win here be that?"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Rhyhorn (♀, Lv26; Ground/Rock).
    - **Pokémon 2**: Omanyte (♀, Lv26; Rock/Water).
    - **Pokémon 3**: Quagsire (♂, Lv26; Water/Ground).
  - **Outcome**: Defeated in Turns 32634-32639; awards `₽1,040`.
- **Bird Keeper Jett (`29, 94` -> `31, 94`, facing East)**:
  - **Pre-Battle Quote**: *"Hehe, hey there? / Wanna lose?"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Togetic (♂, Lv26; Fairy/Flying).
    - **Pokémon 2**: Skarmory (♀, Lv26; Steel/Flying; knows Air Cutter).
  - **Outcome**: Defeat quote: *"Nooooo!"*; awards `₽624` (verified Turns 32642-32645).
- **Hiker Carlton (`22, 99`, facing South)**:
  - **Pre-Battle Quote**: *"These cliffs... / They are very steep, perfect for me!"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Nidoking (♂, Lv27; Poison/Ground).
  - **Outcome**: Defeat quote: *"Oh no, I slipped"*; awards `₽1,080` (verified Turns 32648-32650).
- **Cooltrainer Albert (`16, 92`, facing East)**:
  - **Pre-Battle Quote**: *"Yooo, wanna get higher on the mountain? Too bad!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Loudred (♀, Lv26; Normal).
    - **Pokémon 2**: Sandslash (♀, Lv26; Ground; knows Sand Tomb).
    - **Pokémon 3**: Granbull (♀, Lv27; Fairy).
  - **Outcome**: Defeated in Turns 32656-32661; awards `₽1,620` (Sirius at 75/139 HP).
- **Picnicker Sanna (`22, 78`, facing South)**:
  - **Pre-Battle Quote**: *"A Pokémon Trainer? / That means a battle!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Tranquill (♂, Lv27; Normal/Flying; knows Detect).
    - **Pokémon 2**: Jellicent (♂, Lv27; Water/Ghost; knows Water Pulse).
  - **Outcome**: Defeat quote: *"Why?!"*; awards `₽1,080` (verified Turns 32669-32683; Sirius leveled up to Lv48 and learned Meteor Mash replacing Metal Claw).
- **Black Belt Dane (`30, 81` -> `28, 81`, rotating)**:
  - **Pre-Battle Quote**: *"Serious Puuunch!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Toxicroak (♂, Lv27; Poison/Fighting).
    - **Pokémon 2**: Hawlucha (♂, Lv27; Fighting/Flying).
  - **Outcome**: Defeat quote: *"Huh"*; awards `₽1,944` (verified Turns 32685-32690).
- **Picnicker Pierce (`24, 86`, rotating)**:
  - **Pre-Battle Quote**: *"The forests here are such perfect places for picnicking! / And winning battles!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Staravia (♀, Lv27; Normal/Flying).
    - **Pokémon 2**: Floatzel (♀, Lv27; Water; Ability: Drizzle).
  - **Outcome**: Defeat quote: *"My Pokémon"*; awards `₽1,080` (verified Turns 32692-32697).
- **Hiker Arda (`39, 78`, facing East)**:
  - **Pre-Battle Quote**: *"Doesn't it get a bit colder as you climb higher?"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Torkoal (♂, Lv27; Fire; Ability: Drought).
    - **Pokémon 2**: Klang (Lv27; Steel).
  - **Outcome**: Defeat quote: *"Oh my."*; awards `₽1,080` (verified Turns 32706-32710).
- **Collector Rob (`31, 68`, facing South on overhead wooden bridge)**:
  - **Pre-Battle Quote**: *"Hehe, yo, wanna see my rare Pokémon?"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Bouffalant (♂, Lv28; Normal).
  - **Outcome**: Defeated in Turns 32714-32718; awards `₽1,120`.
- **Hiker Abid (`21, 68`, facing South on overhead wooden bridge)**:
  - **Pre-Battle Quote**: *"Haha be careful not to fall while we battle!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Lairon (♂, Lv27; Steel/Rock; Ability: Sturdy; knows Protect, Roar, and Take Down).
    - **Pokémon 2**: Dugtrio (♂, Lv27; Ground).
  - **Outcome**: Defeat quote: *"I'm the one who's gonna fall!"*; awards `₽1,080` (verified Turns 32721-32738; Sirius leveled up to Lv49).
- **Explorer Johnathan (`22, 60` -> `22, 61`, rotating)**:
  - **Pre-Battle Quote**: *"My explorer spirit needs a fiery battle!"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Bronzong (Lv28; Steel/Psychic; knows Iron Defense).
  - **Outcome**: Defeat quote: *"..."*; awards `₽1,344` (verified Turns 32761-32765).
- **Bug Catcher Humza (`23, 55`, rotating)**:
  - **Pre-Battle Quote**: *"I'm here to catch the greatest bug Pokémon!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Scyther (♀, Lv27; Bug/Flying).
    - **Pokémon 2**: Whirlipede (♂, Lv27; Bug/Poison; knows Protect).
    - **Pokémon 3**: Forretress (♂, Lv27; Bug/Steel).
  - **Outcome**: Defeat quote: *"Nooo!"*; awards `₽1,404` (verified Turns 32780-32788).
- **Nurse Joy (`28, 52`, facing South — Repeatable Party Healer)**:
  - **Pre-Battle Quote**: *"Oh what is a a poor little boy doing out here?"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Blissey (♀, Lv28; Normal; awards 1,530 EXP).
  - **Outcome & Healing Service**: Defeat quote: *"My my... I really underestimated you..."*; awards `₽112`. Speaking to her after battle prompts *"The battles up here must exhaust you a lot... Do you want me to heal your Pokémon? Yes/No"*, fully healing the party on demand (verified Turns 32793-32798).
- **Lass Wanda (`37, 48` -> `36, 48`, rotating)**:
  - **Pre-Battle Quote**: *"Hihi, what a cute opponent!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Roselia (♀, Lv27; Grass/Poison).
    - **Pokémon 2**: Politoed (♀, Lv28; Water; Ability: Drizzle).
  - **Outcome**: Defeat quote: *"And how strong"*; awards `₽1,792` (verified Turns 32804-32811; Sirius leveled up to Lv50).
- **Cooltrainer Joely (`41, 41` -> `38, 41`, facing West)**:
  - **Pre-Battle Quote**: *"You there! / You look like a strong opponent! / We battle, now!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Lycanroc (♂, Lv27; Rock).
    - **Pokémon 2**: Arcanine (♂, Lv28; Fire).
    - **Pokémon 3**: Tropius (♂, Lv28; Grass/Flying).
  - **Outcome**: Defeat quote: *"Looks like I wasn't wrong..."* (verified Turns 32813-32824).
- **Picnicker Casper (`10, 38` -> `13, 38`, rotating)**:
  - **Pre-Battle Quote**: *"My dude! / Wanna battle?"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Ninetales (♀, Lv28; Fire).
    - **Pokémon 2**: Houndoom (♂, Lv28; Dark/Fire).
  - **Outcome**: Defeat quote: *"Nooo!"*; awards `₽1,120` (verified Turns 32837-32843).
- **Bug Catcher Ioan (`15, 31`, facing South)**:
  - **Pre-Battle Quote**: *"My net is big enough to catch you!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Trapinch (♀, Lv28; Ground).
    - **Pokémon 2**: Venomoth (♂, Lv28; Bug/Poison).
  - **Outcome**: Defeat quote: *"Nooo it got tore apart!"*; awards `₽1,456` (verified Turns 32844-32849).
- **Cooltrainer Troy (`10, 28` -> `9, 28`, rotating)**:
  - **Pre-Battle Quote**: *"You must be a Trainer! / Wanna battle?"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Kadabra (♂, Lv28; Psychic).
    - **Pokémon 2**: Hariyama (♂, Lv28; Fighting).
    - **Pokémon 3**: Gastrodon (♀, Lv28; Water/Ground).
  - **Outcome**: Defeat quote: *"..."*; awards `₽1,680` (verified Turns 32852-32859; Sirius leveled up to Lv51).
- **Hiker Ayman (`15, 19` -> `14, 19`, rotating)**:
  - **Pre-Battle Quote**: *"Ahoy, you fancy a battle?"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Minior (Lv28; Meteor Form, Rock/Flying).
    - **Pokémon 2**: Graveler (♂, Lv28; Rock/Ground; Ability: Sturdy; knows Bide).
    - **Pokémon 3**: Sableye (♀, Lv29; Dark/Ghost; knows Fake Out).
  - **Outcome**: Defeated in Turns 32861-32869.
- **Explorer Gwion (`28, 16`, facing South)**:
  - **Pre-Battle Quote**: *"Hello, fellow explorer, since you got up here, let me reward you!"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Amoonguss (♀, Lv29; Grass/Poison).
  - **Outcome**: Defeat quote: *"..."*; awards `₽1,392` (verified Turns 32877-32882).
- **Picnicker Gracie (`34, 13` -> `34, 11`, rotating)**:
  - **Pre-Battle Quote**: *"Let me show you my strong Pokémon!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Lombre (♂, Lv28; Water/Grass).
    - **Pokémon 2**: Swadloon (♀, Lv28; Bug/Grass; knows GrassWhistle, String Shot, and Razor Leaf).
    - **Pokémon 3**: Leafeon (♀, Lv29; Grass).
  - **Outcome**: Defeat quote: *"Nooooo!"*; awards `₽1,160` (verified Turns 32885-32899; Sirius leveled up to Lv52 and declined Dragon Pulse).
- **Northern Landmarks Around `(26, 53)` (Observed Turn 32789)**:
  - **Southbound Shortcut Staircase (`30-32, 58`) & One-Way Ledge (`30-32, 60`)**: Leads south from `(30-32, 57)` over a one-way ledge at `(30-32, 60)` back down to Explorer Johnathan's terrace (`row 61`).
  - **Upper Northbound Staircase (`25-27, 48-49`) & One-Way Ledge (`25-27, 51`)**: Located north of `(26, 52)` above a southbound one-way ledge at `(25-27, 51)`.

<hr>

<h1><code>Locations/Route_13</code></h1>

# Route 13 (Bugiaret Island)

## Geography & Connections
- **North (`14-15, 0` <-> Galinor City `14-15, 86`)**: Seamless northern border connecting the southern sandy trail of **Galinor City** onto **Route 13** at `(14-15, 0)` (verified Turn 33927).
- **South (`48-50, 49` <-> Maple Town `28-30, 0`)**: Seamless southern border connecting the fenced southern dirt road of the Route 13 wheat fields (`49, 49`) directly into **Maple Town** at `(29, 0)` (verified Turn 34046).
- **Northern Signboard (`19-20, 11`)**: Interacted from `(19, 12)`, reads verbatim: *"Route 13 / The route of agriculture"* (verified Turn 33937).
## Wild Pokémon Encounters
- **Tall Grass (`11-17, 10-16` & `17-29, 39-47`)**:
  - **Ponyta** (♂, Lv27; Fire; caught in 1 Ultra Ball at `12, 12` in Turn 33933, transferred to Box 2, bringing Owned species to **70**).
  - **Yanma** (♀, Lv25; Bug/Flying; Ability: Speed Boost; knows Supersonic and Sonic Boom; caught at `20, 43` in Turn 33982, nicknamed **Anis**, transferred to Box 2, bringing Owned species to **71**).
  - **Vespiquen** (♀, Lv26; Bug/Flying; Ability: Pressure; knows Pursuit and Fury Swipes; chipped to ~34% HP with 2x Mach Punch and caught in 1 Ultra Ball at `19, 41` in Turn 34007, nicknamed **Regina**, transferred to Box 2, bringing Owned species to **72**).
  - **Tangela** (♀, Lv30; Grass; knows Mega Drain, Stun Spore, Growth, and Amnesia; chipped to ~25% HP with 2x Bulldoze and caught in an Ultra Ball at `44, 38` in Turn 34033, nicknamed **Liana**, transferred to Box 2, bringing Owned species to **73**).
## Trainers & NPCs
- **Picnicker (`14-15, 14-16`, wandering in tall grass)**: Friendly NPC wandering in the northern grass patch.
- **Gentleman Rick (`30, 21`, facing `Right` across `31-33, 21`)**:
  - **Pre-Battle Quote**: *"The fields give such a conservative vibe... / You wanna see how that is?"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Ninetales (♀, Lv36; Fire; Ability: Drought; OHKO'd by Sirius's `Bulldoze` for `1372 EXP`).
    - **Pokémon 2**: Simisear (♂, Lv36; Fire; OHKO'd by Sirius's `Bulldoze` for `1341 EXP`).
  - **Outcome**: Defeated in Turns 33941-33946.
## Story Events
- **Reconciliation with Valora in the Wheat Field (`32, 26` -> `39, 32`, Turns 33947-33952)**: Stepping onto `(32, 26)` triggers a cutscene where Asher meets **Valora** (`32, 28`), follows her into the golden wheat field (`39, 31-32`), apologizes and hugs her following Dad's advice, and promises never to leave her behind before they head toward **Maple Town** together.
- **Farmer Adelle (`30, 31`, facing `Down` at `30, 32`)**:
  - **Pre-Battle Quote**: *"I took my Pokémon out for a walk, wanna see them?"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Miltank (♀, Lv36; Normal; OHKO'd by Sirius's `Aura Sphere` for `1542 EXP`).
    - **Pokémon 2**: Rapidash (♀, Lv36; Fire; OHKO'd by Sirius's `Bulldoze` for `1480 EXP`).
    - **Pokémon 3**: Persian (♀, Lv36; Normal; OHKO'd by Sirius's `Mach Punch`).
  - **Outcome**: Defeated in Turns 33954-33961.
- **Farmer Omar (`29, 35`, rotating between `Right` and `Left`)**:
  - **Pre-Battle Quote**: *"I'm out here working... / Wanna battle on my break?"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Staraptor (♂, Lv36; Normal/Flying; OHKO'd by Sirius's `Aura Sphere` for `1326 EXP`).
    - **Pokémon 2**: Tauros (♂, Lv37; Normal; OHKO'd by Sirius's `Aura Sphere` for `1672 EXP`, leveling Sirius to Lv64).
  - **Outcome**: Defeated in Turns 33962-33966.
- **Farmer Lan (`32, 40`, rotating in the wheat field)**:
  - **Pre-Battle Quote**: *"Wheat... wheat everywhere..."*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Mothim (♂, Lv36; Bug/Flying; OHKO'd by Sirius's `Meteor Mash` for `1141 EXP`).
    - **Pokémon 2**: Mudsdale (♂, Lv37; Ground; OHKO'd by Sirius's `Aura Sphere` for `1387 EXP`).
    - **Pokémon 3**: Rapidash (♀, Lv36; Fire; OHKO'd by Sirius's `Bulldoze` for `1480 EXP`).
  - **Outcome**: Defeated in Turns 33970-33974 (*"Darn..."*).
- **Black Belt Sive (`16, 35`, facing `Right` across `17-18, 35` on the western cliff plateau)**:
  - **Pre-Battle Quote**: *"Falco Punch!"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Passimian (Lv36; Fighting; OHKO'd by Sirius's `Aura Sphere` in Turn 33989).
    - **Pokémon 2**: Hariyama (♂, Lv36; Fighting; OHKO'd by Sirius's `Aura Sphere` for `1419 EXP` in Turn 33991).
    - **Pokémon 3**: Sawk (♂, Lv36; Fighting; Ability: Sturdy; knows Bulk Up; defeated by Sirius's `Aura Sphere` + `Mach Punch` in Turns 33992-33993).
  - **Outcome**: Defeated in Turns 33988-33993 (*"Oh come on."*).
- **Hiker Rey (`19, 26`, facing `Down` in tall grass on the western cliff plateau)**:
  - **Pre-Battle Quote**: *"Ahoy, on a refreshing walk on the cliffs?"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Golem (Lv36; Rock/Ground; Ability: Sturdy; knows Self-Destruct; fainted in Turn 33996).
    - **Pokémon 2**: Gigalith (♀, Lv37; Rock; Ability: Sand Stream; OHKO'd by Sirius's `Aura Sphere` for `1402 EXP` in Turn 33999).
  - **Outcome**: Defeated in Turns 33995-34000 (*"Oh, I almost slipped"*).
- **Farmer Megan (`47, 43`, facing `Left` in the eastern wheat field)**:
  - **Pre-Battle Quote**: *"Heyy, wanna fight in the crops?"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Meganium (♂, Lv38; Grass; OHKO'd by Sirius's `Meteor Mash` for `1693 EXP` in Turn 34018, leveling Sirius to Lv65).
  - **Outcome**: Defeated in Turns 34015-34019.
## Items
- **Stick x1 (`25, 35`)**: Collected from the golden item ball at `(25, 35)` in the western wheat field (interacted from `26, 35`; verified Turn 33966).
- **Hyper Potion x1 (`8, 30`)**: Collected from the purple spray-bottle sprite at `(8, 30)` in the western green canyon nook below the `(10, 26-28)` staircase (interacted from `8, 29`; verified Turn 34001).
- **Revival Herb x1 (`48, 37`)**: Collected from the spray-bottle/herb sprite at `(48, 37)` in the northeastern wheat field (interacted from `47, 37`; verified Turn 34035).
- **Leaf Stone x1 (`50, 38`)**: Collected from the golden item ball at `(50, 38)` on the passable top edge of the northeastern haystack (`51-52, 38`), reached via the `column 55` aisle (`55, 43 -> 55, 40 -> 53, 40 -> 53, 38 -> 51, 38`; verified Turn 34044).
- **Western Cliff Ridge Item (`15, 43`)**: Item ball on the southern ledge of the western cliff ridge, gated by the rugged rock at `(15, 39)` (`latest_grid.png` Turns 33976 & 33987).
## Spatial & Terrain Mechanics
- **Wheat Field Crop Row Collision**: In the Route 13 wheat fields, the lower/middle stalks of the vertical wheat rows (`29-32, 33-36` and `25-27, 28-34`) have solid wall collision, while the top-tip rows (`row 32` at `28-32, 32`, `row 35` at `25-28, 35`, and `row 39` at `30-35, 39`) and green grass aisles (`column 28` and `columns 33-36`) are walkable (verified Turns 33961-33975).
- **Western Fence Gates & Cliff Staircase**:
  - Two openings in the western wheat-field fence at `(21-22, 39-40)` and `(21-22, 43)` lead west to `columns 19-20`.
  - Heading south along `column 19` dead-ends at trees at `(19, 49)` with a continuous impassable fence along `column 20` (`20, 44-53`; verified Turns 33984-33986).
  - Heading north along `column 19` from `(19, 43)` reaches the wooden cliff staircase at `(17-19, 36-38)`, which climbs onto the western cliff plateau (`cols 12-19, rows 31-38`; verified Turns 33986-33988).
- **Northbound Wheat-Field Return Route (`50, 49` -> `33, 30`, Verified Turns 34530-34534)**: From the southern Maple Town border (`50, 49`), walk `Left 1, Up 6` to `(49, 43)`, `Left 14` along the grass aisle `row 43` to `(35, 43)`, `Up 4` to `(35, 39)`, `Left 6` along the passable top-tip `row 39` to `(29, 39)`, `Up 1, Left 1, Up 6` up `column 28` to `(28, 32)`, `Right 5` along the passable top-tip `row 32` to `(33, 32)`, and `Up 2` to `(33, 30)` at the northern dirt road.

<hr>

<h1><code>Locations/Route_14</code></h1>

# Route 14

## Overview & Connections
- **Western Gatehouse (`8, 12` -> `9, 12` <-> Route 14 Gatehouse `15, 7` <-> `1, 7` <-> Amor City Northeast `88-89, 10`)**: Unlocked after winning Round Eight of the Eclipse Tournament in the Amor City Battle Centre (verified Turns 34593-34598).
- **Eastern Connection**: Leads toward **Hupestian Ruins / Mt. Nit** and **Eclipse Square** (host venue of the Eclipse Tournament Finals).
## Western Forest Clearing & River Bridge (`cols 9-30, rows 6-16`)
- **Western Signboard (`22-23, 10`)**: Interacted from `(22, 11)`, reads verbatim: *"Route 14 / The trail to Victory"* (verified Turn 34599).
- **Wooden River Bridge — Reunion with Valora (`26, 11`, Turns 34600-34601)**: Stepping onto `(26, 11)` on the wooden river bridge (`cols 26-32, rows 10-12`) prompts **Valora** (`29, 11`) to turn and greet Asher (`27, 11`), sharing that she also cleared Round Eight to reach the Finals and that Professor Ivo told her they can head to **Eclipse Square** since Team Siara is low on activity. Asher insists on accompanying her for the long journey (`"I checked the map and it's a huge journey, so I wouldn't even let you go alone!"`), and a flustered Valora (`"Hehe... Is that so? Alrighty then! Let's go!"`) joins Asher at `(26, 11)`.
## Eastern Riverbank & Tall Grass Clearing (`cols 31-40, rows 4-15`)
- **River Staircase (`32, 6-8`)**: Side-facing 3-tile wooden staircase connecting the eastern riverbank (`33, 7`) down to the straight shoreline border tile at `(31, 7)`.
- **Cooltrainer Dale (`36, 7`, Rotating)**:
  - **Pre-Battle Quote**: *"Hey hey hey! / On the way to the Eclipse Square?"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Electrode (Lv40; Electric; knows Shock Wave; OHKO'd by Sirius's `Aura Sphere` for `1285 EXP`).
    - **Pokémon 2**: Hippowdon (♂, Lv40; Ground; Ability: Sand Stream; OHKO'd by Sirius's `Aura Sphere` for `1576 EXP`).
    - **Pokémon 3**: Lunatone (Lv40; Rock/Psychic; OHKO'd by Sirius's `Aura Sphere` for `1285 EXP`).
  - **Outcome**: Defeated in Turns 34604-34609 (awards `₽2,400`).
- **Eastern Clearing Boundary (`cols 32-39, rows 5-13`)**: Enclosed by solid tree lines on the north (`row 4`), east (`col 40`), and south (`rows 13-15`, verified Turn 34706); the Female Cooltrainer at `(33, 27)` is reached by routing around the western/southern side of the river.
- **Wild Grass Encounters**:
  - **Amoonguss** (Lv32, ♂; Grass/Poison; knows Sweet Scent; caught at `38, 8` in Ultra Ball in Turn 34691 and nicknamed "Morel", bringing Owned PokéDex species to 82).
  - **Unfezant** (Lv32, ♂; Normal/Flying; knows Air Cutter; caught at `37, 8` in Ultra Ball in Turn 34704 and nicknamed "Plume", bringing Owned PokéDex species to 84).
  - **Skarmory** (Lv33, ♂; Steel/Flying; caught at `36, 12` in Ultra Ball in Turn 34711 and nicknamed "Aegis", bringing Owned PokéDex species to 85).
## Route 14 River (`cols 27-31, rows 4-18`)
- **Upstream Rock Barrier (`27, 6`, `28, 5`, `29, 4`)**: Launching the FastSwift boat from `(32, 7)` onto `(31, 7)` and surfing north to `(30, 5)` reveals a diagonal line of river rocks at `(27, 6)`, `(28, 5)`, and `(29, 4)` and curved shoreline at `(30, 4)` that completely block upstream passage beyond `row 5` (verified Turns 34611-34612).
- **Downstream Passage Under the Wooden Bridge (`column 29`, `rows 5-28`)**: Surfing south along `column 29` passes directly underneath the overhead wooden river bridge (`rows 10-12`) into the downstream section, which terminates at a solid cliff wall along `row 29` (`cols 25-29`) with no southern landing (verified Turns 34612-34613 & 34640).
- **Swimmer♀ Abigail (`29, 17`, Rotating)**:
  - **Pre-Battle Quote**: *"Isn't the water current too strong?"*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Alomomola (♀, Lv40; Water; OHKO'd by Sirius's `Aura Sphere` for `1413 EXP`).
    - **Pokémon 2**: Quagsire (♀, Lv40; Water/Ground; OHKO'd by Sirius's `Aura Sphere` for `1173 EXP`).
    - **Pokémon 3**: Lumineon (♂, Lv40; Water; OHKO'd by Sirius's `Aura Sphere` for `1380 EXP`).
    - **Pokémon 4**: Pyukumuku (♂, Lv40; Water; Ability: Unaware; OHKO'd by Sirius's `Aura Sphere` for `1233 EXP`).
  - **Outcome**: Defeated in Turns 34634-34638 (*"Hmm... doesn't seem like it"*; awards `₽480`).
- **Swimmer♂ Luis (`26, 26` -> `27, 26`, Facing Right)**:
  - **Pre-Battle Quote**: *"Yooo! / Wanna have an aquatic fight?"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Sharpedo (♀, Lv40; Water/Dark; OHKO'd by Sirius's `Aura Sphere` for `1500 EXP`, leveling Sirius to Lv71).
    - **Pokémon 2**: Gyarados (♀, Lv40; Water/Flying; knows Scary Face; 2HKO'd by Sirius's `Aura Sphere` for `1833 EXP`).
    - **Pokémon 3**: Muk (♂, Lv40; Poison; OHKO'd by Sirius's `Bulldoze` for `1345 EXP`).
  - **Outcome**: Defeated in Turns 34640-34647 (*"Wow!"*).
- **Wild Surfing Encounters**:
  - **Bruxish** (Lv30, ♀; Water/Psychic; knows Psywave, Aqua Jet, Crunch; caught at `29, 13` in Luxury Ball in Turn 34631 and nicknamed "Dazzle", bringing Owned PokéDex species to 81).
  - **Sharpedo** (Lv30-33, ♀/♂; Water/Dark; Ability: Speed Boost; knows Scary Face, Swagger, Ice Fang, Screech; caught Lv33 ♂ at `29, 8` in Ultra Ball in Turn 34699 and nicknamed "Mako", bringing Owned PokéDex species to 83).

<hr>

<h1><code>Locations/Route_16</code></h1>

# Route 16

## Western Entrance & Gatehouse (`8, 20` <-> `15, 7` in Route 16 Gatehouse <-> `88, 24` in Amor City South)
- **Amor City Gatehouse Connection**: Stepping `Right` from `(87, 24)` onto `(88, 24)` in Amor City South warps into the **Route 16 Gatehouse** at `(1, 7)`. Walking `Right 14` across the gatehouse exits at `(15, 7)` onto **Route 16** at `(9, 20)` (verified Turns 33579-33580).
- **Western Signboard (`12-13, 18`)**: Interacted from `(12, 19)`, reads verbatim: *"Amor City - Green District / <-----"* (verified Turn 33581).
## Railway Underpass & Western Meadow (`cols 9-25, rows 10-24`)
- **Gentleman Thomas (`18, 17`, facing `Left`)**:
  - **Pre-Battle Quote**: *"Under the railway in the shade... / Such a perfect place to battle."*
  - **Team (2 Pokémon)**: Arcanine (♂, Lv33; Fire; Ability: Intimidate; `1506 EXP`) and Serperior (♂, Lv33; Grass; `1470 EXP`).
  - **Outcome**: Defeated in Turns 33583-33587 (`"Noooo!"`).
- **Cooltrainer Brad (`21, 10`, facing `Left`)**:
  - **Pre-Battle Quote**: *"Hey! You there! / Wanna battle?"*
  - **Team (3 Pokémon)**: Sawk (♂, Lv33; Fighting; `1152 EXP`), Krokorok (♀, Lv33; Ground/Dark; Ability: Intimidate; `868 EXP`), and Conkeldurr (♂, Lv34; Fighting; `1405 EXP`).
  - **Outcome**: Defeated in Turns 33588-33593 (`"..."`).
- **Cooltrainer Jane (`32, 8` -> `30, 8`, facing `Left`)**:
  - **Pre-Battle Quote**: *"Agh, I'm gonna go home..."*
  - **Team (4 Pokémon)**: Seadra (♂, Lv33; Water; `1095 EXP`), Alomomola (♀, Lv34; Water; `1201 EXP`), Floatzel (♀, Lv33; Water; `1179 EXP`), and Araquanid (♀, Lv34; Water/Bug; `1158 EXP`).
  - **Outcome**: Defeated in Turns 33595-33603 (*"I like to come out here to take a break from the concrete jungle of Amor. / And sometimes to battle."*).
- **Lass Emy (`40, 19`, facing `Left`)**:
  - **Pre-Battle Quote**: *"Ooooh, a Pokémon Trainer! / Let's fight!"*
  - **Team (2 Pokémon)**: Victreebel (♀, Lv34; Grass/Poison; knows Sweet Scent; `1390 EXP`) and Vileplume (♂, Lv34; Grass/Poison; `1339 EXP`).
  - **Outcome**: Defeated in Turns 33605-33609 (`"Nooo!"`).
- **Youngster Micky (`51, 21`, facing `Down` in front of the Metro Underground Tunnel Entrance at `cols 52+, rows 17-20`)**:
  - **Pre-Battle Quote**: *"You are going down, just like Metros go underground here!"*
  - **Team (4 Pokémon)**: Tauros (♂, Lv34; Normal; Ability: Intimidate; `1536 EXP`), Vigoroth (♂, Lv34; Normal; `918 EXP`), Porygon2 (Lv34; Normal; Ability: Download; `1311 EXP`), and Toucannon (♂, Lv34; Normal/Flying; `1326 EXP`).
  - **Outcome**: Defeated in Turns 33611-33618 (*"I... I said you.."*; awards `₽1,768`).
## Eastern Bridge Signboard (`65-66, 22`)
- **Bridge Signboard (`65-66, 22`)**: Interacted from `(65, 23)`, reads verbatim: *"Route 16 / Use the bridge for your own responsibility!"* (verified Turn 33623).
- **Wandering Traveler (`66-67, 23-24`)**: Non-hostile wandering overworld NPC near the signboard.
## Eastern Cliffside & Collapsed Bridge (`cols 71-80, rows 8-24`)
- **Wooden Staircase (`72-74, 17-20`)**: Connects the lower meadow (`72-74, 21`) to the upper cliffside (`72-74, 16`).
- **Dad & FastSwift Service App Cutscene (`76, 12`, Turns 33627-33630)**: Stepping onto the narrow wooden plank at `(76, 12)` triggers a cutscene where Asher sees the bridge to **Aurin Town** has collapsed from a storm, and **Dad (Jackson)** joins him (`76, 13`) and gives Asher the **FastSwift** service app on his HuPhone (*"When facing a body of water, press the 'A Button' to surf."*).
- **Eastern Bay & Sandbar (`cols 77-89, rows 18-29`, Turns 33642-33648)**:
  - Pressing `A` at `(76, 22)` facing the shoreline edge `(77, 22)` immediately mounts the FastSwift inflatable boat onto `(77, 22)`.
  - A small sandbar with a rock at `(86, 22)` spans `(85-89, 21-24)`.
  - **Wild Surf Encounters**: Wild **Wishiwashi** (Solo Form; encountered at `86, 25` in Turn 33645).
  - **Seamless Transition to Eastern Map (`89, 25` <-> `6, 25`, Turn 33648)**: Surfing east past `column 89` transitions seamlessly onto `(6, 25)` of the rainy eastern bay / Aurin Town approaches map.

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

<h1><code>Locations/Route_8</code></h1>

# Route 8 (Bugiaret Island)

## Geography & Connections
- **East (`59, 20-21` <-> Maple Town `0, 16-17`)**: Seamless eastern border connecting the western road of **Maple Town** onto **Route 8** at `(59, 20-21)` (verified Turn 34089).
- **West (`0, 8-9` <-> Mulberry Town `21, 10-11`)**: Seamless western border road leading into **Mulberry Town** (`21, 10-11`, verified Turn 34168), marked by the wooden signboard at `(1-2, 8)` (interacted from `1, 9`), which reads verbatim: *"Mulberry Town / <-----"* (verified Turn 34167).
- **Eastern Signboard (`52-53, 20`)**: Interacted from `(53, 21)`, reads verbatim: *"Route 8 / The path to Mulberry"* (verified Turn 34090).
- **Eastern Plateau & Ledge Bypass (`cols 31-39, rows 15-27`)**:
  - A one-way east-facing ledge at `(36, 24-27)` blocks direct westbound ground travel along `rows 24-27`.
  - **Eastern Plateau Staircase (`37-39, 20-23`)**: Climbs onto the central plateau (`cols 32-39, rows 18-19`), which descends west via the **Western Plateau Staircase (`31-33, 20-23`)**.
  - **Upper Ridge Staircase (`33-35, 16-17`)**: Climbs from the central plateau (`33-35, 18`) onto the upper rocky ridge (`cols 32-42, rows 15-16`), where an item ball at **`(42, 15)`** yields **Ultra Ball x1** (interacted from `41, 15`; verified Turn 34101).
- **Central Valley & Western Bridge (`cols 21-30, rows 17-28`)**:
  - **Northern Cliff Staircase (`24-26, 17-19`)**: Located north of `(24-26, 20)` with a trainer standing near `(25, 19)` (observed Turn 34103).
  - **Overhead Wooden Bridge (`20-22, 16-25`), One-Way Ledge (`24, 22-23`) & Star Piece (`23, 23`)**: A golden item ball yielding **Star Piece x1** sits at **`(23, 23)`** below solid twigs at `(23, 22)`, enclosed on the east by a 2-tile one-way east-facing ledge (`24, 22-23`) and on the south by solid cliff lip collision at `(23-24, 24)` (verified Turns 34113-34114, 34139-34142). Reached by walking under the overhead wooden bridge along `row 22` (`15, 22 -> 18, 22 [one-way right-facing ledge] -> 19-22, 22`), stepping `Down` to **`(22, 23)`** underneath the bridge, and pressing `A` facing `Right` toward `(23, 23)` (verified Turns 34139-34142).
- **Western Double Staircase (`11, 26-29` & `9, 27-30`) & Western Corridor (`cols 3-15, rows 18-32`)**:
  - **Double Side-Facing Staircase (`11, 26-29` -> `10, 28` -> `9, 27-30`)**: Climbs west from `(13, 27)` onto the narrow ridge `(10, 27-29)` and descends west via `(9, 28)` onto `(8, 29)` (verified Turns 34130-34131).
  - **Western Green Grass Corridor (`col 8, rows 22-32`)**: Connects `(8, 29)` north to `(8, 22-23)`, where an eastbound lane (`8-11, 23` -> `10-18, 22`) curves around the cliff ridge to the bridge underpass (`19-22, 22 -> 22, 23`), while a northbound path passes an elderly Gentleman/Farmer trainer at `(7, 18)` (`latest_grid.png` Turn 34132).

## Wild Pokémon Encounters
- **Tall Grass (`40-50, 22-28`, `25-32, 21-28`, `14-24, 26-30` & `3-15, 18-32`)**:
  - **Floette** (♀, Lv27, Red Flower; Fairy; knows Wish and Magical Leaf; caught at full HP in 3 Ultra Balls at `25, 23` in Turn 34119, nicknamed **Camellia**, transferred to Box 2, bringing Owned species to **74**).
  - **Gloom** (♀, Lv28; Grass/Poison; knows Razor Leaf; caught at full HP in 3 Ultra Balls at `12, 22` in Turn 34136, nicknamed **Dahlia** and transferred to Box 2 in Turn 34138, bringing Owned species to **75**).
  - **Audino** (♂, Lv26; Normal; caught at full HP in 1 Ultra Ball at `13, 27` in Turn 34148, nicknamed **Lyric** and transferred to Box 2 in Turn 34149, bringing Owned species to **76**).

## Trainers & NPCs
- **Wandering Farmer (`47-48, 22-24`)**: Friendly NPC wandering above the eastern tall grass patch (`40-50, 22-28`).
- **Hiker Miguel (`36, 18`, facing `Down` on the central plateau)**:
  - **Pre-Battle Quote**: *"Greetings, fellow hiker!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Sudowoodo (♂, Lv37; Rock; Ability: Sturdy; knows Rock Tomb; defeated by Sirius's `Aura Sphere` + `Mach Punch` for `1069 EXP`).
    - **Pokémon 2**: Lairon (♂, Lv37; Steel/Rock; Ability: Sturdy; knows Metal Sound; defeated by Sirius's 2x `Mach Punch` for `1204 EXP`).
  - **Outcome**: Defeated in Turns 34095-34101 (*"Oh nooo!"*; awards `₽1,480`).
- **Battle Girl Kelsey (`28, 22`, rotating in tall grass west of the plateau)**:
  - **Pre-Battle Quote**: *"Drop kick!"*
  - **Team (4 Pokémon)**:
    - **Pokémon 1**: Hakamo-o (♀, Lv35; Dragon/Fighting; OHKO'd by Sirius's `Meteor Mash` for `1102 EXP`).
    - **Pokémon 2**: Poliwrath (♀, Lv35; Water/Fighting; OHKO'd by Sirius's `Aura Sphere` for `1387 EXP`).
    - **Pokémon 3**: Medicham (♀, Lv36; Fighting/Psychic; OHKO'd by Sirius's `Meteor Mash` for `1179 EXP`).
    - **Pokémon 4**: Infernape (♂, Lv36; Fire/Fighting; OHKO'd by Sirius's `Bulldoze` for `1611 EXP`).
  - **Outcome**: Defeated in Turns 34103-34112 (*"Retreat attack"*; awards `₽2,592`).
- **Collector Winston (`22, 19`, rotating on the overhead wooden bridge `20-22, 16-25`)**:
  - **Pre-Battle Quote**: *"Hehe I just bought this Pokémon, they are pretty rare!"*
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Heatmor (♂, Lv38; Fire; OHKO'd by Sirius's `Bulldoze` for `1375 EXP`).
  - **Outcome**: Defeated in Turns 34122-34125 (*"All that money to waste."*; awards `₽1,520`).
- **Hiker Aiden (`15, 27`, facing `Up`/`Right` in tall grass west of the bridge)**:
  - **Pre-Battle Quote**: *"As the altitude raises, so does my excitement for a fight!"*
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Solrock (Lv37; Rock/Psychic; Ability: Levitate; OHKO'd by Sirius's `Aura Sphere` for `1188 EXP`).
    - **Pokémon 2**: Lunatone (Lv37; Rock/Psychic; Ability: Levitate; OHKO'd by Sirius's `Aura Sphere` for `1188 EXP`).
  - **Outcome**: Defeated in Turns 34126-34129 (*"Falling right off.."*; awards `₽1,480`).
- **Gentleman Leslie (`7, 18`, facing `Down` in the western corridor)**:
  - **Pre-Battle Quote**: *"Hello, young man... / Would you fancy a battle?"*
  - **Team (3 Pokémon)**:
    - **Pokémon 1**: Pidgeot (♂, Lv37; Normal/Flying; OHKO'd by Sirius's `Meteor Mash` for `1363 EXP`).
    - **Pokémon 2**: Talonflame (♂, Lv37; Fire/Flying; knows Nature Power [turns into Stun Spore on grass]; 2HKO'd by Sirius's `Aura Sphere` for `1387 EXP`, leveling Sirius to Lv66).
    - **Pokémon 3**: Decidueye (♂, Lv37; Grass/Ghost; knows Foresight; OHKO'd by Sirius's `Meteor Mash`).
  - **Outcome**: Defeated in Turns 34152-34163.

<hr>

<h1><code>Locations/Route_9</code></h1>

# Route 9 (Bugiaret Island)

## Geography & Connections
- **South (`6-7, 39` <-> Mulberry Town `4-5, 0`)**: Seamless southern border connecting the northern sandy trail of **Mulberry Town** onto **Route 9** at `(6-7, 39)` (verified Turn 34196).
- **East (`71, 19-20` <-> Galinor City `0, 59-60`)**: Seamless eastern border connecting **Route 9** into **Galinor City** at `(0, 59-60)` (verified Turn 34252), marked by the wooden signboard at `(63-64, 18)` (interacted from `64, 19`), which reads verbatim: *"Galinor City / ----->"* (verified Turn 34250).
- **Southwestern Tall Grass & Staircase (`cols 1-8, rows 27-36`)**:
  - **Patrolling Black Belt (`3, 27-30`)**: Patrols north and south through the western tall grass.
  - **Side-Facing Wooden Staircase (`8, 31-34`)**: Climbs east from `(7, 32)` onto the eastern rocky plateau at `(9, 31-32)` (verified Turn 34198).
- **Eastern Rocky Plateau (`cols 9-29, rows 18-35`)**:
  - **Northwestern Descending Staircase (`16-17, 24`) & Max Potion (`13, 25`)**: A 2-tile wide wooden staircase at `(16-17, 24)` descends from the plateau (`16-17, 25`) into an enclosed lower green grass nook (`cols 13-17, rows 18-25`, closed off by trees on the north), giving access to a spray-bottle sprite at **`(13, 25)`** yielding **Max Potion x1** (interacted from `14, 25`; verified Turns 34208, 34215), while the main plateau path continues north and east via `(19, 26 -> 20, 24 -> 20, 22 -> 21, 20 -> 24, 20 -> 27, 20 -> 27, 19)`.
  - **Northeastern Descending Staircase (`27-28, 18`)**: Descends north from `(27-28, 19)` on the rocky plateau onto the northern green grass corridor (`27-28, 17`, verified Turn 34224).
- **Northern Green Grass Corridor (`cols 26-40+, rows 12-17`)**:
  - **Northern Signboard (`32-33, 14`)**: Interacted from `(32, 15)`, reads verbatim: *"Route 9 / Mulberry Hills"* (verified Turn 34230).

## Trainers & NPCs
- **Hiker Miguel (`17, 29`, facing `Down` in tall grass)**:
  - **Pre-Battle Quote**: *"You and me on the summit battle now!"* (triggered at `17, 30` in Turn 34200).
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Nidoking (♂, Lv38; Poison/Ground; OHKO'd by Sirius's `Bulldoze` for `1587 EXP`).
    - **Pokémon 2**: Dugtrio (♂, Lv38; Ground; knows Mud Bomb; OHKO'd by Sirius's `Mach Punch` for `1245 EXP`).
  - **Outcome**: Defeated in Turns 34201-34206.
- **Trainer at `(26, 26)` (facing `Left` across tall grass on the rocky plateau)**: Observed Turn 34220.
- **Hiker Wily (`26, 19`, facing `Right` in front of the northeastern staircase `27-28, 18`)**:
  - **Pre-Battle Quote**: *"Just another wimpy hiker... / Let me show you how real hiking is done!"* (triggered at `27, 19` in Turn 34224).
  - **Team (1 Pokémon)**:
    - **Pokémon 1**: Aggron (♀, Lv40; Steel/Rock; Ability: Sturdy; knows Metal Sound; 2HKO'd by Sirius's `Mach Punch` for `1756 EXP`).
  - **Outcome**: Defeated in Turns 34225-34228.
- **Cooltrainer Sofia (`38, 14`, facing `Down` in tall grass east of the northern signboard)**:
  - **Pre-Battle Quote**: *"Hey hey! / How about a quick power demonstration?"* (triggered at `38, 15` in Turn 34232).
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Mimikyu (♂, Lv38; Ghost/Fairy; Ability: Sturdy; knows Shadow Claw; 2HKO'd by Sirius's `Meteor Mash` + `Bulldoze` for `1359 EXP`).
    - **Pokémon 2**: Clefable (♀, Lv38; Fairy; OHKO'd by Sirius's `Meteor Mash` for `1050 EXP`).
  - **Outcome**: Defeated in Turns 34233-34238 (*"Asher got ₽2,280 for winning!"*).
- **Cooltrainer Albert (`51, 18`, rotating; walked left to `49, 18` when triggered at `48, 18`)**:
  - **Pre-Battle Quote**: *"Good grief... / Another Trainer?!"* (triggered at `48, 18` in Turn 34240).
  - **Team (2 Pokémon)**:
    - **Pokémon 1**: Skarmory (♂, Lv38; Steel/Flying; Ability: Sturdy; knows Agility; 2HKO'd by Sirius's `Aura Sphere` + `Mach Punch` for `1368 EXP`).
    - **Pokémon 2**: Probopass (♂, Lv38; Rock/Steel; OHKO'd by Sirius's `Mach Punch` for `1497 EXP`).
  - **Outcome**: Defeated in Turns 34241-34248.
## Wild Pokémon Encounters
- **Tall Grass (`cols 1-8, rows 27-36` & `cols 13-18, rows 19-32`)**:
  - **Linoone** (♀, Lv28; Normal; knows Fury Swipes; caught at full HP in 2 Ultra Balls at `15, 22` in Turn 34212, nicknamed **Vector** and transferred to Box 3 in Turn 34213, bringing Owned species to **77**).
  - **Vigoroth** (♂, Lv27; Normal; caught at full HP in 1 Ultra Ball at `16, 22` in Turn 34217, nicknamed **Tempo** and transferred to Box 3 in Turn 34218, bringing Owned species to **78**).

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

<h1><code>Locations/Siara_Lab</code></h1>

# Abandoned Undersea Team Siara Laboratory (Location 3)

## Elevator Mechanics (`6, 15`)
- **Floor Selector (`5F, 4F, 3F, 2F, 1F`)**: Stepping into any elevator doorway (`5, 4` on `1F`, `36, 5` on `2F`) warps to `(6, 15)` inside the elevator and automatically opens the 5-floor menu (cursor defaults to `5F`).
  - Selecting a valid unlocked floor plays a ~5500ms elevator ride animation and **automatically warps Asher out of the elevator** onto the destination floor (verified Turns 34386-34388).
  - **Floor Access**:
    - `1F`: Entrance Stairwell (`5, 5`; connects south at `5, 15` to the Location 3 Cave Passage `28, 8`).
    - `2F`: Unlocked initially; warps to `(36, 6)` (verified Turn 34388).
    - `5F`: Displays *"UNAUTHORIZED PERSONEL / EC CARD IS REQUIRED"* until the **EC Card** is obtained (verified Turn 34385).

## Floor 2F (`36, 6` Elevator Exit)
- **Elevator Lobby (`33-38, 5-10`)**:
  - **Elevator Doorway (`36, 5`)**: Enters the elevator (`6, 15`).
  - **Locked Northern Security Door (`30-31, 6`)**: Unlocked using **Code Red (`0203`)** obtained from the B2F Southern Area console at `(36, 16)` (automatically steps Asher inside to `30, 5`; contains an **Eclite Shard** at `30, 4`, collected Turn 34431).
  - **Professor Ivo's HuPhone Briefing (`37, 6`, Turns 34389-34391)**:
    - Stepping onto `(37, 6)` triggers a HuPhone call from **Professor Ivo**, who explains that while the elevator is running on a backup generator, everything else in the facility is offline because the **main generator** is not running.
    - Because the security doors cannot be opened without power, Asher must **find the generator room and turn the main generator back on**.
    - Ivo also warns Asher that the abandoned laboratory is crawling with **Eclipsed Pokémon**.
  - **Purple Wall Plaque (`38, 5`)**: Reads *"B2F / Lobby"* (confirming `1F–5F` on the elevator panel correspond to subterranean undersea levels `B1F–B5F`, verified Turn 34391).
  - **Wild Eclipsed Pokémon Encounters**:
    - Floor tiles inside the Abandoned Undersea Laboratory can trigger wild **Eclipsed Pokémon** encounters (such as **Eclipsed Pikachu**♀ Lv40, which knows `Eclipse Zap`) even while a Repel / Super Repel is active (verified Turn 34393).
    - Wild Eclipsed Pokémon can be fled from normally via `Run` (*"Got away safely!"*, verified Turn 34396) or targeted with Poké Balls (verified Turn 34395).
  - **Western Corridor (`23-33, 8-9`)**:
    - **Purple Wall Plaque (`27, 7`)**: Reads *"Doors are password protected! / If you forgot the code for a door, find the computer displaying it."* (verified Turn 34398).
    - **Bookshelves (`23-26, 7-8`)**: Located along the northern wall.
    - **Purple Door Mat (`25, 9` <-> Western Stairwell Room `6, 7`)**: Stepping `Down` off `(25, 9)` warps into the **B2F Western Stairwell & Computer Room** at `(6, 7)` (doorway exit at `6, 6`; features a descending staircase with a red mat at the southwest corner and a computer/server station along the northern wall, verified Turn 34400).
  - **Southern Corridor (`34-35, 10-13+`)**: Extends south past the yellow crates at `(36, 12-13)`.
## B2F Western Stairwell & Computer Room (`6, 7` from B2F Lobby `25, 9`)
- **Doorway Exit (`6, 6`)**: Warps back to B2F Lobby at `(25, 9)`.
- **Northern Wall (`cols 8-13, rows 8-9`)**: Bookshelves at `(8-9, 8-9)` and `(13+, 8-9)`, blue computer desk at `(10-11, 8-9)`, and server tower at `(12, 8-9)`.
- **Cracked Floor Shadow (`5-7, 8-10`)**: 3x3 circular shadow centered on `(6, 9)` between the northern doorway (`6, 7`) and the southern floor (`row 10+`); `(7, 9)` has solid collision (verified Turn 34403).
- **Descending Staircase (`2-3, 10-11`)**: Accessed via the red mat at `(4, 11)`.
  - **Northern Computer Terminal (`10-11, 8-9`)**: Decorative wall terminal (`row 10` is completely walkable from `5, 10` to `10, 10`; verified Turn 34405).
  - **Blue Control Console (`13, 12`)**: Located on the eastern table below `(13, 11)`; displays *"Code Blue / Location: B3F Code: 0405"* and grants **Code Blue** (verified Turn 34454; triggers wild Lv40 **Eclipsed Quagsire** on floor tiles, verified Turn 34452).
  - **Staircase Warp (`3, 11` <-> B3F `12, 11`)**: Stepping onto `(3, 11)` from the red mat `(4, 11)` descends to **B3F** at `(12, 11)` (verified Turn 34406).

## Floor B3F (Western Stairwell Entry at `12, 11`)
- **Ascending Staircase (`13-14, 11`)**: Accessed via the red mat at `(12, 11)`; returns to the B2F Western Stairwell & Computer Room (`4, 11`).
- **Western Security Door (`3-4, 9-10`) & Descending Staircase (`2, 5`)**:
  - Approaching from the south along `row 11` (`12, 11 -> 4, 11`), step onto the walkable bottom half `(4, 10)` facing `(4, 9)` and press `A` to unlock the door with **Code Blue (`0405`)**, which automatically steps Asher through to `(4, 8)` (verified Turn 34454).
  - **Descending Staircase (`2, 5` via Red Mat `3, 5-6`)**: Descends from the B3F northwest corridor to the **B4F Western Corridor**.
- **Northern Elevator & Floor Plaque (`9, 5` & `11, 5`)**:
  - **Elevator Doorway (`9, 5`)**: Connects to the facility elevator (`6, 15`).
  - **Purple Wall Plaque (`11, 5`)**: Reads *"B3F / Machine Room"* (verified Turn 34409).
- **Southern Corridor (`cols 8-10, rows 11-19`)**:
  - Floor hole at `(10, 15)` (`col 9` is completely clear from `9, 6` to `9, 19`).
  - **Purple Door Mat (`9, 19` <-> B3F Machine Room `29, 4`)**: Stepping `Down` off `(9, 19)` enters the **B3F Machine Room** at `(29, 4)` (verified Turn 34411).
- **Eastern Branch (`cols 11-17, rows 15-19`)**:
  - **Purple Wall Plaque (`12, 17`)**: Reads *"V Generator Room V"* (verified Turn 34422).
  - **Ascending Staircase (`17, 18` via Red Mat `16, 18-19`)**: Ascends to the **B2F Southern Area** at `(30, 16)` (verified Turn 34423).

## B2F Southern Area (`30, 16` from B3F Eastern Staircase `17, 18` & B2F Lobby `34-35, 10-13`)
- **Descending Staircase (`28-29, 16-17` via Red Mat `30, 16-17`)**: Descends to the B3F Eastern Branch at `(16, 18)`.
- **Objects & Consoles**:
  - **Marie's Diary (`34, 18`)**: Dated *"2011. April 5th"*: *"This is it! I have finally set up the entire Laboratory. Here I'll fully develop out Eclipsing, so that Jackson will believe that it's safe. Can you believe he left with our 5 year old son?! I can't mess this up. If I prove this is completely safe we can be a family again..."* (verified Turns 34426-34429).
  - **Blue Control Console (`36, 16`)**: Displays *"Code Red / Location: B2F Code: 0203"* and grants **Code Red** to unlock the B2F northern security door (`30-31, 6`) (verified Turn 34429).
  - **Item (`38, 16`)**: **Full Restore** located in the eastern alcove behind the yellow crates at `(37, 15-16)` and `(38, 17-18)` (collected Turn 34429).

## B3F Machine Room (`29, 4` from B3F Corridor `9, 19`)
- **Doorway Exit (`29, 3`)**: Warps back to the B3F Corridor at `(9, 19)`.
- **Wild Eclipsed Pokémon**: Floor tiles trigger Lv40 wild Eclipsed Pokémon such as **Eclipsed Solrock** (verified Turn 34413).
- **Main Generator Switch (`29, 12`)**:
  - Reached via the western passage (`28, 4 -> 28, 7 -> 27, 7 -> 27, 13 -> 29, 13`).
  - Interacting with `(29, 12)` from `(29, 13)` flips the switch from red/blue to solid blue and restores main power to the facility (verified Turn 34415).
  - Immediately triggers a HuPhone call from **Professor Ivo**, who confirms power is restored, reports that the third energy signal is on the lowest floor (**B5F**, which requires an **Ec Card**), and warns Asher that something is approaching—triggering a scripted ambush by a wild **Lv40 Eclipsed Golem** at `(29, 13)` (OHKO'd by Sirius's `Aura Sphere` for `1011 EXP`, verified Turns 34415-34420).
- **Item**: **Ultra Ball** at `(32, 14)` in the southeast corner (collected Turn 34420).
## Floor B4F (`23, 6` Elevator Exit)
- **Elevator & Floor Plaque (`23, 5` & `25, 5`)**:
  - **Elevator Doorway (`23, 5`)**: Connects to the facility elevator (`6, 15`; exiting steps to `23, 7`).
  - **Purple Wall Plaque (`25, 5`)**: Reads *"B4F / Community Room"* (verified Turn 34435).
- **B4F Community Room (`cols 20-36, rows 6-18`)**:
  - **Wild Eclipsed Pokémon**: Floor tiles trigger Lv40 wild Eclipsed Pokémon such as **Eclipsed Gengar** (verified Turn 34440).
  - **Locked Security Door (`21-22, 17-18`)**: Password-protected security door in the southwest corridor. **2-Tile-Tall Security Door Mechanic**: For all 2-tile-tall vertical security doors (`30-31, 5-6` on B2F, `3-4, 9-10` on B3F, `21-22, 17-18` and `14-15, 15-16` on B4F), the top row (`row 17`) is a walkable overlap tile while the bottom row (`row 18`) is the solid interactive door tile; when approaching from the north, step onto the top half (`21, 17`) facing `Down` toward `(21, 18)` and press `A` to unlock it with **Code Green: `1115`** (verified Turn 34447).
  - **Marie's 2013 Diary (`30, 15`)**: Dated *"2013. September 1st"*: *"I adopted the little boy from two years ago and named him Frio. / I have also made a groundbreaking discovery because of him! / The gem he always kept with himself seemed to calm Eclipsed Pokémon down... / Normally they are really violent, but the gem caused them to be controlable. / The test subjects still can't be kept outside of tubes but we found out the reason. / The process is tied to a material called 'Eclite'. / We tried using chemicals similar to the components of Eclite. / However due to Eclite's unique origin, it's not possible with Earth elements... / We need Eclite to continue on... A lot of it!"* (verified Turns 34437-34438).
  - **Blue Control Console (`30, 17`)**: Displays *"Code Green / Location: B4F Code: 1115"* and grants **Code Green** (verified Turn 34442).
  - **Marie's 2014 Diary (`31, 17`)**: Dated *"2014. October 31st"*: *"I found out more of the origin of Eclipsing... / Apparently Frio is part of an Eclipser family... / A bloodline of people having the abillity to use Eclite as a way to channel their spirit and Eclipse Pokémon without technology. / I must train him here now! / I managed to make a test subject which doesn't require life sustaining equipment... / I can start training Frio's Eclipser power to get the full potential of the Eclite!"* (verified Turns 34442-34443).
  - **Item (`36, 15`)**: **Revive** located in the eastern alcove below `(36, 14)` (collected Turn 34443).
- **B4F Western Corridor & Storage Room (`13, 9` from B3F Staircase `2, 4`)**:
  - **Ascending Staircase (`11-12, 9-10` via Red Mat `13, 9-10`)**: Returns to B3F at `(3, 4)`.
  - **Locked Security Door (`14-15, 15-16`)**: Unlocked from `(15, 15)` facing `Down` toward `(15, 16)` using **Code Green (`1115`)**, stepping Asher into the room at `(15, 17)` (verified Turn 34457; triggers wild Lv40 **Eclipsed Excadrill** on floor tiles, verified Turn 34459).
  - **Blue Control Console (`17, 17`)**: Located above `(17, 18)`; displays *"Code Yellow / Location: B4F Code: 0420"* and grants **Code Yellow** (verified Turn 34458).
  - **Key Item (`11, 18`)**: **Ec Card** sitting on the broken table (interacted with from `12, 18` facing `Left` via `col 12` around the floor-hole ring at `13-15, 17-19`; collected Turn 34460).
  - **Marie's 2015–2016 Diary (`13, 20`)**: Dated *"2015. June 6th"* and *"2016. April 5th"*: *"2015. June 6th / I managed to make a quick and cheap way of Eclipsing Pokémon! / I also created a special band for Frio that he can use to Eclipse Pokémon, helping his training. / ... / ... / 2016. April 5th / This is bad! This is bad! / Eclipse Pokémon have gone berserk all over the Laboratory! / We can't control all of them... / We need to leave immediately and seal this lab away!"* (verified Turn 34461).
  - **Purple Wall Plaque (`9, 16`)**: Reads *"Number of failed experiments: 405 / Number of successful experiments: 1"* (verified Turn 34463).
- **B4F Ailing Room (`cols 16-38, rows 19-28`, behind Code Yellow Door `21-22, 17-18`)**:
  - Unlocked via the left panel `(21, 18)` (from `21, 17` facing `Down` or from `21, 19` facing `Up`) using **Code Yellow (`0420`)** (verified Turns 34466 & 34472).
  - **Purple Wall Plaque (`28, 25`)**: Reads *"Ailing room"* (verified Turn 34470).
  - **Item (`37, 28`)**: **TM10 (Dark Pulse)** located at the far eastern end of the Ailing Room (collected Turn 34472).
## Floor B5F (`8, 18` Elevator Exit; Requires Ec Card)
- **Elevator Doorway (`8, 18`)**: Connects to the facility elevator (`6, 15`).
- **Breached Security Door (`7-9, 10-11`)**: Smashed open down the center (`col 8`); purple wall plaque at `(6, 10-11)` is blank.
- **B5F Inner Chamber (`cols 5-11, rows 3-8`)**:
  - **Third Gem Pedestal (`8, 3`)**: Stone formation holding the third gem.
  - **Confrontation with Colen Champion Micah (`8, 6` -> `8, 5`, Turns 34477-34494)**:
    - Mistaking Asher and Jackson for Team Siara members after seeing them at Aur Factory, **Micah** (Champion of the Colen Region; uses `Staraptor♀ Lv40`, `Aggron♂ Lv41`, `Samurott♂ Lv41`, and `Sceptile♂ Lv42` holding Rocky Helmet) battled Asher at `(8, 7)` before learning that Asher, Jackson, Professor Ivo, and Valora are fighting against Team Siara.
    - Micah retrieved the **Third Gem** from the stone pedestal (`8, 3`) and entrusted it to **Professor Ivo**, who hurried back to her laboratory in Lancio Town to secure it before Micah departed to his team's base.
  - **Table (`10-11, 3`)**: Decorative blue console (`10, 3`) and notes (`11, 3`) (verified Turns 34495-34496).

<hr>

<h1><code>Locations/Solare_Island</code></h1>

# Solare Island

## Geography & Connections
- **Southern Dock (`cols 35-37, rows 49-53`)**:
  - **Harry (`36, 52`)**: Guards the boat at the southern tip of the dock after sailing from the **Galinor Cargo Loading Bay** (`28, 19`). Speaking to Harry allows returning to the mainland (Galinor City) at any time (verified Turn 33061).
  - **Shoreline & Southern Staircase (`36, 45-48`)**: Grassy landing north of the dock with a stone staircase at `(35-37, 45)` leading north toward the Solare Island forest.
- **Southern Ruin Terrace (`cols 31-39, rows 38-44`)**:
  - **Dad (`34, 43`)**: *"Everything alright, son?"* (verified Turn 33063).
  - **Professor Ivo (`37, 42`)**: *"We got to find the source of the signal, fast!"* (verified Turn 33065).
  - **Ancient Stone Plate (`36, 41`)**: Interacted from `(36, 42)`, reads verbatim: *"It looks like an ancient stone plate... / There's some text carved in! / 'Thou... see this pla... when the ti... comes' / It's barely readable, and the rest is completely messed up..."* (verified Turns 33064-33065).
  - **Eastern Ledge Item (`42, 42`) & Northeastern Forest Connection (`39, 29`)**: Purple potion bottle sprite visible on the lower eastern terrace (`cols 40-43, rows 41-44`), connected via the cliffside trail (`cols 37-38, rows 32-38`) from a northeastern forest exit at `(39, 29)`. Bounded on the west by solid pine trees (`cols 35-36, rows 33-38`), a stone ruin wall (`cols 34-39, rows 38-43`, where only `34-35, 38` on the top lip is reachable from `33, 38`), a brown rock cone (`38, 44`), and the ocean cliff (`38, 45-47`), confirming that `(39, 29) -> (42, 42)` is a one-way exterior item alcove exited from inside the Eastern Forest (verified Turns 33067 & 33280-33284).
  - **Northern Staircase (`32-33, 37`)**: Stone staircase leading north into the Solare Island forest.
  - **Forest Entrance Archway (`32-33, 31` <-> Solare Island Forest `57-58, 32`)**: Stepping north into `(33, 31)` warps into the **Solare Island Forest** at `(58, 32)` (verified Turn 33067).
- **Solare Island Forest**:
  - **Southern Entrance Clearing (`cols 44-62, rows 24-32`)**:
    - **Ancient Stone Plate #2 (`57, 25`)**: Interacted from `(57, 26)`, reads verbatim: *"It looks like an ancient stone plate... / There's some text carved in! / = 'Whoeve... ste... shall beware. Th... gem ... the key...' / It's barely readable, and the rest is completely messed up..."* (verified Turn 33070).
    - **Hupestian Wall Symbol & Hole (`55, 24`)**: Carved into the stone ruin wall 2 tiles west of Ancient Stone Plate #2 (`55, 24`, interacted from `55, 25`); reads verbatim: *"There's a symbol in the wall... / There's also a hole. / It looks exactly like the one in the Hupestian Ruins!"* (verified Turns 33258 & 33276). Testing `Rare Opal`, `Eclipse Band`, `Red Shard`, `Clear Shard`, and `Odd Keystone` from the Bag at `(55, 25)` (and at the identical symbol at `33, 29`) displays *"Ivo: Asher! This isn't the time to use that!"*, and scanning with the `Itemfinder` at `(55, 25)` reports *"Nope! There's no response."* (verified Turns 33290-33291, 33335-33336, & 33341). The grass tile at `(53, 24)` to the left of the wall is blocked on the north by the autumn tree at `(52-53, 21-23)` (verified via Turn 33340 `latest_grid.png`).
    - **Eastern Tree Border (`cols 60-62, rows 25-31`)**: The clearing terminates on the north and east at the solid pine tree border (`cols 60-66, rows 22-31`, verified at `62, 26` and `60, 25` in Turns 33258 & 33284).
    - **Tall-Grass Alcove (`cols 46-47, rows 26-29`)**: Dead-end tall-grass alcove between the orange autumn trees at `(46-47, 26-29)`, terminating at the tree trunk at `(46-47, 25)` (verified Turn 33220).
  - **Western Barrier Shrine (`cols 31-39, rows 24-32`)**:
    - **Team Siara Grunts (`34, 31` & `36, 32`)**: Separated from their squad after touching a crystal that activated the ancient defense barrier (`col 33, rows 29-31`).
    - **Ancient Stone Plate #3 (`38, 30`)**: Read during the cutscene at `(38, 31)` (Turn 33073): *"'Onl... the one... worthy... ca.. clear the pa... to... truth. Le...crystal be... guidance...'"*.
    - **Shrine Courtyard & Blue Barrier Crystal (`35, 25`)**: Reached via the stone staircase at `(35-36, 28-29)` (where the wooden stair railings at `34, 28-29` and `36, 28-29` are also walkable; bounded on the west by a wall enclosure containing a decorative yellow lantern sphere on a vine at `32, 27` above a second **Hupestian Wall Symbol & Hole** at `33, 29` reading *"There's a symbol in the wall... / There's also a hole. / It looks exactly like the one in the Hupestian Ruins!"*, verified Turns 33332-33333; the northern interior wall of Shrine #1 is solid at `row 24`, verified at `36, 25` in Turn 33239). Interacting with the large blue crystal at `(35, 25)` from `(35, 26)` prompts *"The crystal is shining in light blue as the bright sky... / Will you touch it? Yes/No"*; selecting **Yes** deactivates the glowing blue barrier at `col 33, rows 29-31` (verified Turn 33077; subsequent interactions only display the 1-line description with no prompt, verified Turn 33274).
    - **Siara Grunt Battle (`35, 30`, Turns 33079-33085)**: Stepping down to `(35, 30)` after deactivating the blue barrier triggers the two Team Siara Grunts (`34, 31` & `36, 32`) to confront Asher and Valora. Valora battles one grunt while Asher defeats the other (Carnivine Lv30, Luxray Lv30, Honchkrow Lv30; `₽3120`), after which both grunts flee west to rejoin their squad.
  - **Western Forest Clearing Beyond Barrier #1 (`cols 20-30, rows 21-31`)**:
    - **Siara Grunt (`24, 26`)**: Faces south in the tall grass (`"*How did you get in?! / Didn't those morons accidentally lock us in?*"*, Turn 33088; Granbull Lv30, Floatzel Lv30 [Drizzle], Herdier Lv31; `₽3224`, defeated Turns 33088-33095).
    - **Max Repel (`24, 30`) & Eclite Piece (`32, 27`)**: Gold item ball sprite sitting on the grass tile at `(24, 30)` (interacted from `25, 30`; yields **Max Repel x1**, verified Turn 33343). A second gold item ball sprite sits at **`(32, 27)`** inside the western enclosure of Shrine #1 (above the Hupestian Wall Symbol & Hole at `33, 29`), reached from `(26, 22)` by stepping `Down` onto `(26, 23)` and walking `Right 6` along the walkable upper brick row of the horizontal stone wall (`26, 23 -> 32, 23`) and `Down 3` to `(32, 26)`, yielding **Eclite Piece x1** (verified Turn 33345). From `(32, 23)`, `row 23` continues east behind Shrine #1 to `(38-39, 22-23)` into the Eastern Sector of Solare Island Forest.
    - **Wild Encounters**: **Spewpa** (Lv23; caught at `26, 30` in Turn 33109 after chipping to ~48% yellow HP with two `0.5x` resisted `Mach Punches` against `+6` Defense from `Harden`), **Shelmet** (Lv22; caught at `25, 25` in Turn 33117 after chipping ~26% HP and inflicting Paralysis with Lv16 Vega's `Spark`), **Ferroseed** (Lv25; caught at `9, 12` in Turn 33155 after paralyzing with Lv15 Flaaffy's `Thunder Wave`), **Unown** (Lv23 Unown-U; caught at `16, 17` in Turn 33166 in a standard Poké Ball after paralyzing with `Thunder Wave` and chipping ~23% HP with `ThunderShock`), **Sigilyph** (Lv20; encountered at `28, 17` in Turn 33171, where two `0.25x` double-resisted `Mach Punches` from Lv54 Sirius chipped ~44% HP each to leave it at ~12% red HP), **Joltik** (Lv24; encountered at `25, 25` in Turn 33254), **Wormadam** (Lv24 Trash Cloak; encountered at `46, 29` in Turn 33256), **Phantump** (Lv25; encountered at `16, 16` in Turn 33264), **Yamask** (Lv22; encountered at `45, 30` in Turn 33276), **Karrablast** (Lv23; encountered at `52, 13` in Turn 33366).
    - **S-Curve Stone Ruin Corridor (`cols 16-25, rows 24-28`)**: Connects `(25, 25)` west via `(21, 25) -> (21, 28) -> (17, 28) -> (16, 25)` between the vertical stone walls at `col 22 (rows 26-28)` and `cols 18-19 (rows 24-27)` (verified Turn 33119).
    - **Western Clearing & Ruin Walls (`cols 9-18, rows 19-30`)**: From `(16, 25)`, clear grass leads north via `(16, 22-23)` toward the northern terrace (`rows 19-22`), while the corridor along `row 19` (`15, 19 -> 10, 19`) and `col 10` (`10, 19 -> 10, 24`) west of the square ruin block (`cols 11-14, rows 20-23`) is bounded on the west by solid forest trees (`cols 6-9, rows 15-24`; verified Turns 33121 & 33301).
    - **Ambushing Female Siara Grunt (`18, 23` -> `17, 23`)**: Crouches behind the stone ruin wall at `(18, 23)` (with her purple beret peeking above the wall at `18, 22`) and ambushes the player at `(16, 23)` (`"*Ha! These walls are perfect to hide and then ambush!*"`, Turn 33122; Starmie Lv30, Wobbuffet Lv31 [Shadow Tag, Destiny Bond], Gardevoir Lv31; `₽3224`, defeated Turns 33122-33139).
  - **Northwest Forest Ruins (`cols 6-23, rows 7-19`)**:
    - **Path North from `(16, 22)` to `(16, 14)`**: Clear short grass leads via `(16, 21) -> (15, 21) -> (15, 19) -> (16, 19)`, followed by `Up 5` along `col 16` (`rows 16-18` tall grass, `rows 14-15` short grass) past the stone ruin wall at `cols 17-23, rows 15-16` (verified Turns 33141-33142).
    - **Eastern Short-Grass Alcove (`row 14, cols 16-23`)**: Clear short-grass dead-end alcove extending east along `row 14` between the autumn trees (`rows 11-13`) and the stone ruin wall (`rows 15-16`), terminating at the vertical stone wall at `col 24 (rows 12-16)` (verified Turn 33162).
    - **Northwest Stone Wall (`cols 10-15, rows 8-11`) & Rock Cone (`12, 12`)**: From `(16, 14)`, `Up 2, Left 3` reaches `(13, 12)` beside a rock cone at `(12, 12)` and above a thin wall (`cols 13-15, row 13`). Stepping `Down 1, Left 2, Up 1, Left 2` via `(13, 13) -> (11, 13) -> (11, 12) -> (9, 12)` reaches the western passage along `col 9 (rows 8-12)`, which is bounded on the east by a solid vertical stone wall at `col 10 (rows 8-10)` and leads north to a tan dirt trail at `(6-9, 7-9)` (verified Turns 33144-33145 & 33262).
    - **Northwest Clearing & Team Siara Squad (`cols 4-9, rows 3-9`)**: At the top of `col 9` (`9, 8`), a tan dirt clearing (`cols 5-8, rows 6-9`, bounded on the east and north by solid trees at `cols 8-16, rows 1-8`) is occupied by **five Team Siara Grunts** (`6, 6` facing south, `4, 5` facing east, `5, 5` facing north, `7, 5` facing west, and `6, 4` facing south) blocking a northern forest archway (`5-6, 3-4`). Interacting with any of the grunts (`6, 6`, `5, 5`, `4, 5`, `7, 5`) displays verbatim: *"We are blocking this suspiciously placed area! / You definitely won't need to come back here later!"* even after all solitary grunts in the forest are defeated (verified Turns 33160 & 33304-33305).
  - **North-Central & Eastern Ruin Corridors (`cols 24-35, rows 8-21`)**:
    - **Crossing at `(22, 18) -> (25, 18)`**: From `(16, 17)`, walking `Right 6` to `(22, 17)`, `Down 1` to `(22, 18)`, and `Right 3` to `(25, 18)` passes underneath the rock cone at `(23, 17)` onto the flower corridor (`cols 24-27, rows 12-17`) east of the vertical stone wall (`col 24, rows 12-16`; verified Turn 33169).
    - **Northern Dead-End Alcove (`col 28, rows 8-12`)**: Walking north along `col 26` (`26, 17 -> 26, 12`), east to `(28, 12)`, and north along `col 28` terminates at a solid tree line at `(28, 8)` (`28, 7` blocked by pine tree) and is bounded on the west at `(28, 9)` by solid forest trees (`cols 21-27, rows 6-11`), while stepping east from `(28, 9)` onto the top-left wall corner at `(29, 9)` is blocked on the east by the solid tree root at `(30, 9)` and on the south by the vertical stone wall along `col 29 (rows 10-16)` (verified Turns 33189-33192, 33265, & 33297).
    - **Spinner Siara Grunt (`24, 19`) & Middle Terrace (`rows 19-20, cols 21-30`)**: A stationary random-turning Team Siara Grunt stands at `(24, 19)` (`"You! / This area is under our investigation, leave now!"`; Sandslash♀ Lv31, Golem♂ Lv31 [Rock Head, Sucker Punch], Bronzong Lv30; `₽3224`, defeated Turns 33194-33200), while `col 25` (`25, 17-20`) and `col 29-30` (`29-30, 17-20`) connect south from `(28, 17)` onto `row 20`, which is bounded on the east at `col 31 (rows 18-24)` by a solid vertical stone wall (verified Turns 33243 & 33299).
    - **Stationary Siara Grunt (`30, 14`) & Blue Barrier #2 (`col 34, rows 13-16`)**: Passing under the stone wall at `(27-28, 15-16)` along `row 17` (`25, 17 -> 30, 17`) leads to a stationary Team Siara Grunt at `(30, 14)` facing south over tall grass (`30, 15-19`) inside an enclosed courtyard (`cols 30-33, rows 11-16`), with a second glowing blue energy barrier on its eastern wall at `col 34, rows 13-16` (`"This is just great... / Do I really need to take care of you?"`; Quagsire♂ Lv31, Stunfisk♂ Lv32; `₽3328`, defeated Turns 33228-33231 after stepping to `30, 15`). Below `(33, 16)`, `row 17` (`33, 17`) is impassable due to the stone wall and trees (verified Turn 33269).
    - **Courtyard Upper Alcove (`cols 30-35, rows 11-13`), Rugged Rock (`35, 12`), & Blue Crystal #2 (`37, 11-12`)**: Walking north behind the defeated grunt at `(30, 15)` via `(31, 16) -> (31, 14) -> (30, 14) -> (30, 11)` reveals that the top wall-lip tiles at `(31, 11)` and `(33, 13)` are walkable (verified Turns 33233-33235). Stepping across `(33, 13) -> (33, 12) -> (34, 12) -> (34, 11) -> (35, 11)` (around the solid brown rock at `34, 13`) leads to a **rugged rock** at **`(35, 12)`** (*"It's a rugged rock, but with some equipment, I could smash it."*, verified Turn 33236). Across the vertical stone wall (`col 36, rows 12-14`), a second large glowing blue crystal sits at **`(37, 11-12)`** with open grass below it (`37, 13-16`) extending east along `rows 15-16` (`cols 35-40+`; verified via Turn 33268 `latest_grid.png`).
  - **Southwest Ruin Quadrant (`cols 2-16, rows 21-32`)**:
    - **Path from `(16, 21)` to `(9, 30)`**: Walking south from `(16, 21)` to `(16, 25)`, west along `row 25` to `(12, 25)` (where the stone ruin wall juts out to `col 11, rows 25-26`), south to `(12, 27)`, west onto the flower patch at `(9, 27)`, and south to `(9, 30)` reaches the southwest corridor (`rows 29-31, cols 4-15`; verified Turns 33203-33206).
    - **Female Siara Grunt (`8, 30`)**: Stands at `(8, 30)` facing east along `row 30` (`"These weird barriers are all around the area... / Wait, why am I telling you this?"`; Passimian♂ Lv33; `₽3432`, defeated Turns 33206-33213).
    - **Ether (`15, 30`)**: Purple bottle sprite at the eastern end of `row 30` (`15, 30`, interacted from `14, 30`), yielding **Ether x1** (verified Turn 33213).
    - **Blue Barrier #3 (`col 3, rows 29-31`) & Locked Blue Crystal (`2, 31`)**: A third glowing blue energy barrier at `col 3, rows 29-31` (with a solid vertical stone wall below it at `col 3, rows 32-34` and solid wall/trees at `col 3, row 28`, reachable along the upper wall lip `7, 28 -> 4, 28 -> 4, 29` or lower grass `4, 31`) blocks access to a large glowing light-blue crystal at `(2, 31)` in the southwest corner (`cols 1-2, rows 30-31`; verified Turns 33205-33253).
    - **Southwest Forest Archway (`5-6, 36` <-> Solare Island Western Terrace `12-13, 36`)**: Located directly south of `(4, 31)` at `(5-6, 34-36)`. Stepping `Down` at `(5, 36)` warps out to the **Western Exterior Terrace of Solare Island** at `(12, 36)` above a southbound stone staircase at `(12-13, 40-41)` (verified Turns 33246-33248).
- **Western Exterior Terrace & Shoreline (`cols 4-18, rows 35-49`)**:
  - **Big Pearl (`17, 47`)**: Descending the stone staircases at `(12-13, 40-41)` and `(11-12, 44-45)` to the southwestern shoreline point (`16, 47`) and interacting with the gold ball sprite at **`(17, 47)`** yields **Big Pearl x1** (verified Turn 33249).
  - **Western Loop Path (`12, 43` -> `8, 43` -> `8, 41` -> `8, 40`)**: From `(12, 43)` between the two staircases, a grass path weaves west between the pine trees via `(8, 43) -> (8, 41) -> (8, 40)`, where it terminates at a solid cliff wall and pine trees (`cols 6-8, rows 35-40`; verified Turn 33250).
  - **Horizontal Stone Ruin Wall Collision & Encounter-Free Short-Grass Highway (Verified Turns 33314-33328)**:
    - Horizontal stone ruin walls consist of a walkable top-lip row, a **walkable upper brick row** (entered from above, where Asher walks behind the wall with only the top of his head visible), and a solid lower brick row (verified at `11-15, 28` and `4, 29`).
    - **Blue Crystal #3 (`2, 31-32`)**: Completely enclosed by trees (`col 1`), stone walls (`2-3, 29-30` and `2, 34`), and `col 3` (`3, 30-31` Blue Barrier #3 and `3, 32-35` solid post/trees; verified via Turn 33313 `latest_grid.png` and tested row-by-row in Turns 33319-33321). Testing `Eclipse Band` from the Key Items pocket while facing Blue Barrier #3 at `(4, 31)` displays *"Ivo: Asher! This isn't the time to use that!"* (verified Turn 33309).
    - **Semicircular Wall Indentation (`24-26, 23`)**: Observed on the horizontal stone ruin wall (`cols 19-28, rows 23-24`) on Turn 33322's `latest_grid.png` (captured from `21, 25`), directly south of the short-grass tiles at `(24-26, 21-22)`.
    - **Blue Crystal #2 (`38, 11-12`) & Eastern Siara Grunt (`41, 17`)**: Located on the eastern side of `Blue Barrier #2` (`col 34, rows 14-16`) and the rugged rock (`35, 12`), with `(35, 10)` and `(36, 11)` verified solid from `(35, 11)` (Turn 33325 `latest_grid.png`).
    - **100% Short-Grass Highway (`(9, 28) <-> (30, 20)`)**: Connects the Southwest Quadrant `(9, 28)` and Central S-Curve `(23, 25)` to the Northeast Courtyard border `(30, 20)` with zero tall-grass tiles via `(9, 28) -> (11, 27) -> (17, 27) -> (17, 21) -> (15, 21) -> (15, 19) -> (23, 19) -> (23, 18) -> (25, 18) -> (25, 19) -> (26, 19) -> (26, 21) -> (25, 21)` (bypassing the defeated spinner grunt standing at `25, 20`; verified Turns 33323-33328 & 33350).
    - **Blue Crystal #4 (`41, 18-19`), Blue Barrier #5 (`col 45, rows 14-16`), & The 4-Crystal Deactivation Chain (Verified Turns 33347-33360)**:
      1. **Blue Crystal #1 (`35, 25`)** -> Deactivates **Blue Barrier #1 (`col 33, rows 29-31`)** (Turn 33077).
      2. **Blue Crystal #4 (`41, 18-19`)** -> Reached from `(38, 22)` behind Shrine #1 via `(39, 22) -> (39, 21) -> (40, 21) -> (41, 21) -> (41, 20)` across the passable top canopy of the autumn tree at `40-41, 21-23`; touching `(41, 19)` deactivates **Blue Barrier #3 (`col 3, rows 30-31`)** in the southwest corner (verified Turns 33348-33353).
      3. **Blue Crystal #3 (`2, 31-32`) & Hupestian Wall Symbol #3 (`3, 30`)** -> With Blue Barrier #3 gone, stepping onto `(2, 31)` ( revealing a third Hupestian Wall Symbol & Hole on the wall at `3, 30`) and facing `Down` to touch `(2, 32)` displays *"The weird barrier somwhere far away is gone!"* and deactivates **Blue Barrier #2 (`col 34, rows 15-16`)** in the northeast courtyard (verified Turns 33353-33355).
      4. **Blue Crystal #2 (`38, 11-12`) & Hupestian Wall Symbol #4 (`44, 13`)** -> Passing east through `(34, 15)` to `(38, 13)` and touching `(38, 12)` pans the camera east and deactivates **Blue Barrier #5 (`col 45, rows 14-16`)** (located below a fourth Hupestian Wall Symbol & Hole at `44, 13`; verified Turns 33356-33357).
    - **Eastern Sector Team Siara Grunt (`41, 17`)**: Stands behind the horizontal stone wall at `(41, 17)` and challenges the player at `(41, 15)` (*"I feel all nauseous... / I wonder what makes me dizzy..."*; Swalot♂ Lv31, Toxicroak♀ Lv31, Weezing♂ Lv31; `₽3224`, defeated Turns 33358-33365).
  - **Northeast Clearing (`cols 45-55, rows 8-16`)**:
    - **Ancient Stone Plate #4 (`52, 11`)**: Interacted from `(52, 12)`, reads verbatim: *"It looks like an ancient stone plate... / There's some text carved in! / 'Ones... got this fa... may st... in' / It's barely readable, and the rest is completely messed up..."* (verified Turn 33370).
    - **Northeast Forest Archway (`48-50, 8`)**: Located directly north of the sand patch (`48-50, 11-13`); bounded on the west by the pine tree at `(46-47, 7-9)` and on the east by the stone ruin wall (`51-53, 9-10`) and trees (`54-59, 8-16`; verified via Turn 33371 `latest_grid.png`).
- **Solare Island Inner Shrine (`14, 28` -> `14, 17`)**:
  - **Connection**: Stepping north into the Northeast Forest Archway at `(49, 8)` in Solare Island Forest warps to `(14, 28)` in the Solare Island Inner Shrine and automatically walks Asher up to `(14, 26)` (verified Turn 33372).
  - **The Enigmatic Gem & Marie's Ambush (`14, 14` -> `14, 17`, Turns 33373-33375)**:
    - Dad (Jackson) and Professor Ivo join Asher and Valora at `(14, 26)` as Ivo's energy detector spikes toward the upper shrine altar (`14, 14`), where a glowing enigmatic gem rests.
    - **Marie ("Mom")** arrives up the shrine stairs (`14, 19`) with two Team Siara Grunts (`13, 20` & `15, 20`) and reveals that because only a true Eclipser could lower the island's crystal barriers (and Frio refused to be lured in after defecting), Team Siara intentionally let Asher solve the barrier puzzle and lead them to the shrine.
    - **Harry's Betrayal as Siara Admin Harry**: When Marie remarks that *"the four of us will be enough"*, **Harry** walks up the stairs in his Team Siara uniform (`14, 19`), punches Jackson aside (`14, 18 -> 13, 18`), and reveals that his "double agent" story at the Galinor Cargo Loading Bay was a lie—he is still loyal to Marie as **Siara Admin Harry** (*"Mom: Lesson number one about life, Ashi. Never trust anyone!"*).
  - **Boss Battle — Siara Admin Harry (`14, 17`, Turns 33375-33391)**:
    - **Team (4 Pokémon)**:
      1. **Lapras♂ Lv32** (Water/Ice; OHKO'd by Sirius's `Aura Sphere` for `1501 EXP` in Turn 33376).
      2. **Shiftry♀ Lv33** (Grass/Dark; OHKO'd by Sirius's `Mach Punch` for `1279 EXP` in Turn 33378).
      3. **Zoroark♂ Lv32** (Dark; OHKO'd by Sirius's `Mach Punch` for `1440 EXP` in Turn 33380, leveling Sirius to Lv56).
      4. **Eclipsed Vikavolt♂ Lv33** (holds `Leftovers`, uses `Discharge` and the priority signature move **`Eclipse Zap`**, features a purple Eclipse HP bar phase, is **weak to Electric-type moves** [`2x` super-effective from Vega's `Spark`, verified Turn 33390], and **double-resists Fighting-type moves** [`0.25x` from `Aura Sphere`, dealing ~14% HP, verified Turn 33416]; OHKO'd from 94% HP by Lv56 Sirius's `+1 Attack` STAB `Meteor Mash` for `1378 EXP` in Turn 33417, defeating Siara Admin Harry for `₽3960`!).
  - **Helicopter Escape & Post-Battle Cutscene (`14, 16-18`, Turns 33418-33421)**:
    - Upon defeat, **Siara Admin Harry** remarked: *"Seeing Marie's own son fight for his Dad... What an honor I must say"*.
    - **Marie ("Mom")** ordered the grunts to get to business, and a helicopter hovered above the Inner Shrine and dropped a ladder. The grunts took the mysterious gem from the altar (`14, 14`, revealing a fifth **Hupestian Wall Symbol & Hole** on the altar wall behind the pedestal) and escaped with Marie and Harry.
    - As **Dad (Jackson)** regained consciousness and wondered how Harry could betray him, **Professor Ivo** noted that *"Harry isn't someone who would betray a friend just like that... I'm sure he had his reasons to do what he ended up doing..."*. Checking the empty pedestal (`14, 15`), Ivo confirmed the energy readings vanished with the gem and called the authorities to send a boat to take them back to her laboratory in Lancio Town.
  - **Mysterious Trainer (`???`) Epilogue (`14, 15`, Turns 33421-33423)**:
    - Immediately after Asher's group departed Solare Island, a mysterious trainer (`???`, wearing a cap, red scarf, and green vest) stepped out from behind the autumn trees (`11, 14` -> `14, 15`) and reported over the phone to a female colleague that the ancient shrine's spherical pedestal was empty and that he had heard helicopters while crossing the forest. At her request, he photographed the shrine before heading back (*"Alright, all done, time to head back before she start to worry!"*).

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
- **Western Island (Bugiaret Island)**: Large western archipelago connected via a sea bridge (Route 11) from Destino City to Galinor City; contains a northern red city (Galinor City) and a triangle of 3 green towns (including Mulberry Town).
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
- **Destino Mine Inner Den — Team Siara's Fossil Plot, The Eclipsed Tyranitar & The Clear Shard (`12, 18` -> `13, 15`, Turns 32462-32472)**:
  - Inside the Inner Den (`12, 19`), Asher and Valora joined **Frio** (`14, 14`) confronting four **Team Siara Grunts** around a mining machine (`8-10, 14-15`) who were digging up fossils.
  - One of the grunts revealed **Marie**'s objective in Destino Mine: *"We will ecplise ancient Pokémon, which we will resurrect from these fossils!"*
  - Telling Asher and Valora to stay out of it (*"Tch, stay out... I'll show you all what I can do!"*), Frio single-handedly defeated all four Team Siara Grunts.
  - Before retreating with the stolen fossils, the lead grunt threw a Poké Ball releasing a rampaging **Eclipsed Tyranitar** (`12, 12`). When Valora warned Asher not to pass out like in Mt. Gerhana, Frio was puzzled (*"Huh? Did he pass out? But... as an eclipser he should have been fine..."*).
  - Much more experienced now, Asher channeled his Eclipser aura and calmed the Eclipsed Tyranitar back to its normal form without collapsing.
  - As the Tyranitar departed, a falling rock dropped toward Valora at `(14, 16)`; Frio shouted *"Watch out, idiot!"* and pulled Valora to safety before brushing off her thanks (*"Tch, whatever, be more cautious later, Blueberry..."*) and departing.
  - Picking up the rock that fell at `(14, 16)`, Asher obtained a **Clear Shard** (which can be restored into an active **Eclite Shard** using Professor Ivo's Eclicizer in Lancio Town) and automatically stepped out of the Inner Den to `(9, 17)` in the Triple-Staircase Chamber.
- **Amor Battle Center Round Three Summons & Valora's Message (`37, 31`, Turns 32488-32491)**:
  - Stepping onto `(37, 31)` outside Destino Mine in Destino City triggers two HuPhone text messages:
    1. **Amor Battle Center**: *"Dear Contestant! The third round of the Eclipse Tournament is about to start. Please, head back to the Battle Center in Amor City to participate in the round's battles. If you have any questions, be sure to ask the receptionist, in the building where you signed up. Good luck, Pokémon Trainer! - Amor Battle Center"*.
    2. **Valora**: *"Heyy, I got the message from the tourney organizers, so I'm in Amor participating! I'll text ya once I'm done, see you later ;)"*.
  - Asher resolves to take the newly reopened Destino City Metro Station back to Amor City for Round Three (*"Alright, let's take a metro to Amor and get to business!"*).
## Eclipse Tournament Round Three — Victory Over Sinnoh's Aaron
- **Round Three Bracket & Matches (Turns 32507-32553)**: Inside the Amor City Battle Centre's Round 3 Arena (`17, 17`), Asher competed in an 8-trainer single-elimination bracket on the holographic cyber-arena stage:
  1. **Quarterfinals**: Defeated **Juggler Tony** (Togetic Lv25, Ninjask Lv25, Luxio Lv26).
  2. **Semifinals**: Defeated **Black Belt Lee** (Heracross Lv25, Hitmonlee Lv25, Dewott Lv26), while Sinnoh's **Aaron** defeated Ace Trainer Marcus on the opposite side of the bracket.
  3. **Round Three Finals**: Defeated **PKMN Trainer Aaron** from the Sinnoh region (Dustox Lv25, Yanmega Lv25, Vespiquen Lv26, Scizor Lv25) to win his Round Three group and advance to Round Four of the Eclipse Tournament.
- **Post-Round-3 HuPhone Message from Professor Ivo (`11, 11`, Turns 32554-32556)**:
  - Stepping north onto `(11, 11)` in the Tournament Arena Lobby after winning Round 3 triggers a HuPhone text message from **Professor Ivo**: *"Hey, Asher! I heard Round 3 has ended, I hope you are still going strong! Anyway, I would like you to meet me in Jarro Town. There's something really interesting I would like to show you! You can reach the town from Route 12. The exit to the route is the most northerly tunnel in Amor, I'm on my way there too. See you there!"*.
  - Asher decides to text Valora and head to **Jarro Town** via **Route 12** (accessed through the northernmost tunnel in Amor City).
## Jarro Town — Sinnoh Champion Cynthia & The Ancient Hupestian Ruins
- **Encounter Outside the Jarro Town Pokémon Center & The Odd Keystone (`14, 29` -> `14, 30`, Turns 32905-32912)**: Upon arriving in snowy **Jarro Town** ("Highest of Hupest") via Route 12 and approaching the Pokémon Center (`14, 29`), Asher bumped into **Cynthia**, Champion of the Sinnoh Region. Cynthia shared that she was invited as a special guest to watch the **Eclipse Tournament**, traveled to Jarro Town because of the **Ancient Hupestian Ruins**, and praised Asher's battle style and potential above the other notable competitors (whom Asher recognized as Frio and Valora). Expecting great things from Asher in the future, Cynthia gifted him the **Odd Keystone** before departing south.
- **Ancient Hupestian Ruins & The Eklissi Prophecy (`36, 21` -> `15, 13` -> `36, 21`, Turns 32941-32946)**:
  - **The Eklissi Empire**: Inside the Ancient Hupestian Ruins (`15, 13`), Professor Ivo showed Asher three ancient stone carvings (`left: four-pointed star`, `center: winged eclipse emblem`, `right: circular lunar emblem`) inscribed in **Eklissi**, the language of an ancient empire that ruled the continent thousands of years ago before being wiped out.
  - **The Three-Part Eklissi Prophecy**:
    1. **Part 1 (Left Mural)**: *"A majestic light which once came to destroy us, will shine upon us in four millennias..."* — Suggesting the Eklissi empire was wiped out by a cataclysm that will return in 4,000 years, which Asher theorized could be the same ancient meteorite linked to the Great Eclipse.
    2. **Part 2 (Right Mural)**: *"It was an angel which made the darkness of the night bright like the cherishing Sun!"* — Describing an angelic entity or meteorite explosion whose flash turned night as bright as the Sun.
    3. **Part 3 (Center Mural)**: *"The angel lashed her anger on us and we perished to oblivion... But the next time the people will be ready... Three glimpses of light... three of the youth will arise to protect from her judgement, her anger"*
  - **Connection to Eclipsing**: Agreeing with Asher that the Eklissi prophecy is directly connected to Eclipsing, Professor Ivo departed back to her laboratory in Lancio Town to research further details, while Asher wondered when the prophecy is supposed to come true and stepped back outside to `(36, 21)` in Jarro Town.
- **Amor Battle Center Round Four Summons & Fast-Travel to Route 12 (`36, 29` -> Route 12 Main `25, 109`, Turns 32948-32949)**:
  - Stepping south onto `(36, 29)` along the Ecly Festival lantern path after visiting the Ancient Hupestian Ruins triggers a HuPhone text message from the **Amor Battle Center**: *"Dear Contestant! The fourth round of the Eclipse Tournament is about to start. Please, head back to the Battle Center in Amor City to participate in the round's battles. If you have any questions, be sure to ask the receptionist, in the building where you signed up. Good luck, Pokémon Trainer! - Amor Battle Center"*.
  - Immediately after reading the message, the game automatically fast-travels Asher to **`(25, 109)`** at the southern end of **Route 12 Main** outside Amor City.
## Eclipse Tournament Round Four — Victory Over Johto's Silver
- **Round Four Bracket & Matches (Turns 32957-32987)**: Inside the Amor City Battle Centre's Round 4 Arena (`20, 17`), Asher competed in an 8-trainer single-elimination bracket on the holographic cyber-arena stage:
  1. **Quarterfinals**: Defeated **Super Nerd Eugene** (Haunter Lv27, Diggersby Lv28, Banette Lv27, Vigoroth Lv28).
  2. **Semifinals**: Defeated **Hiker Tom** (Carnivine Lv28, Cryogonal Lv29, Quilladin Lv28), while Johto's **Silver** defeated the Worker and Picnicker on the opposite side of the bracket.
  3. **Round Four Finals**: Defeated **PKMN Trainer Silver** from the Johto Region (Weavile Lv29, Crobat Lv29, Magnezone Lv30, Feraligatr Lv31) to win his Round Four group and advance to Round Five of the Eclipse Tournament.
- **Post-Round-4 HuPhone Message from Dad (`14, 6` in Tournament Arena Lobby, Turn 32989)**:
  - Stepping onto `(14, 6)` in the Tournament Arena Lobby after winning Round 4 triggers a HuPhone text message from **Dad**: *"Hey son, I heard Round 4 has ended, I'll be in front of the Battle Center to pick you up. Ivo called me to pick you up for an emergency meeting!"*.
  - Asher wonders what could be so urgent and heads outside to meet Dad in front of the Amor City Battle Centre.
## Lancio Town Emergency Meeting — Three Eclite Energy Readings & Mission to Galinor City
- **Professor Ivo's Emergency Briefing (`59, 26` in Amor City -> `1, 8` in Ivo's Basement Lab, Turns 32991-32993)**:
  - Outside the Amor City Battle Centre (`59, 26`), Dad met Asher after Round 4 and brought him back to Professor Ivo's Basement Laboratory in Lancio Town (`1, 8`), where **Professor Ivo** (`0, 6`) and **Valora** (`0, 8`, who also passed Round 4) were waiting.
  - Displaying the Hupest World Map, Professor Ivo revealed that she detected abnormal energy readings resembling **Eclipse Shards / Eclite** at **three marked locations** (an offshore island dot in the bay south of the Destino–Galinor bridge, Solare Island in the far northwest, and a northern mountain location east of Jarro Town, plus a blue square marker east of Amor City), with the strongest readings coming from **Location 1**.
  - **Mission to Galinor City**: Professor Ivo asked Asher and Valora to head to **Galinor City** and find a boat ride to the island at Location 1 while she and Dad (Jackson) investigate whether Team Siara is headed there.
  - **Transit via Sovio Metro & Destino City**: Dad explained that because **Galinor Station** is currently closed due to a leak, Asher and Valora can take the Metro as far as **Destino City** and cross the western bridge from Destino City to reach **Galinor City**. Dad then drove Asher and Valora to the **Sovio City Metro Station** (`48, 18`).
## Galtino Bridge (Route 11) — Team Siara Diversion, Eclipsed Pidgeot & Encounter with Sinnoh's Dawn
- **Team Siara Roadblock & The Eclipsed Pidgeot (`53, 20` -> `46, 20`, Turns 33028-33033)**:
  - Crossing onto **Galtino Bridge** (`53, 20`), Asher and Valora found a crowd of onlookers watching **Dawn** from the Sinnoh Region confront three **Team Siara Grunts** blocking the bridge.
  - Realizing they were supposed to be on a boat/cruise and needed a distraction, the three grunts released a rampaging **Lv34 Eclipsed Pidgeot** on the bridge and fled west toward Galinor City.
  - While Valora calmed the crowd of civilians, Asher stepped in front of Dawn (`46, 20`) and defeated the **Lv34 Eclipsed Pidgeot** (against which Fighting-type `Aura Sphere` was *not very effective*, confirming Eclipsed Pidgeot has altered typing).
- **Introduction to Dawn & Valora's Teasing (`46, 20`, Turn 33033)**:
  - After Asher calmed the situation, **Dawn** thanked him, wondered why the Pidgeot didn't look normal, introduced herself as a fellow **Eclipse Tournament** competitor who had noticed Asher's skill (*"Hehe, and not too ugly, that's for sure."*), and headed east toward Destino City (*"See ya later, in the tournament!"*).
  - Rejoining Asher at `(46, 20)`, **Valora** teased him (*"You also seemed to have a bit too much fun after you were done... Oh, nothing, but who was she?"*) before continuing west across Galtino Bridge toward Galinor City.
## Galinor City — Dad's Message & Search for the Cargo Loading Bay
- **Arrival in Galinor City & Dad's Text (`47, 47`, Turn 33041)**:
  - Upon arriving in **Galinor City** ("The luxury resort city") at `(47, 47)`, Valora marveled at how huge and fancy the city is and wondered how they would find their boat ride.
  - Asher immediately received a HuPhone text message from **Dad**: *"Asher, I already called Harry, he should be waiting at the Cargo Loading Bay. I told him you will get there earlier, could you find him and wait for us? We will be there soon too!"*.
  - Asher and Valora set out to locate **Harry** at the **Cargo Loading Bay** in Galinor City.
## Galinor Cargo Loading Bay — Harry's Double Agent Revelation & Voyage to Solare Island
- **Reunion with Harry, Dad & Professor Ivo (`28, 18` -> `28, 17`, Turns 33057-33060)**:
  - On the Middle Pier of the Galinor Cargo Loading Bay (`28, 17-19`), Asher and Valora met **Harry**, and **Dad (Jackson)** and **Professor Ivo** arrived right behind them (`28-29, 17`).
  - Confirming they were all prepared to go after Team Siara, Harry invited everyone to board his ship (`28, 20`).
- **Harry's Past as a Former Siara Admin & Jackson's Double Agent (`28, 18`, Turns 33059-33060)**:
  - Before boarding, Asher noticed Harry was wearing a Team Siara uniform and asked why.
  - Harry revealed that he used to be very poor until Jackson gave him a job at Team Siara when Jackson was still a Boss, and that Harry even served as a **Siara Admin** alongside **Flo** (whom Harry noted is **Marie's cousin**) before stepping down to a regular grunt role.
  - When Jackson left Siara, Harry wanted to follow him because he agreed with what Jackson stood for, so Jackson asked Harry to stay inside Team Siara as a **double agent** to feed Jackson intelligence on Siara's operations without actively participating in their schemes.
  - Promising not to tell Dad that Harry shared the secret, Asher boarded the ship with Harry, and they sailed to **Solare Island** (`36, 51`, Turn 33060).
## Solare Island Inner Shrine — The Enigmatic Gem & Harry's Betrayal
- **Team Siara's Trap (`14, 26` -> `14, 17`, Turns 33372-33375)**: After Asher deactivated all four ancient Eclipser crystal barriers in Solare Island Forest and reached the Inner Shrine altar (`14, 14`) with Valora, Dad (Jackson), and Professor Ivo to examine the enigmatic gem emitting the massive energy signal, **Marie ("Mom")** and two Team Siara Grunts ambushed them. Marie revealed that because only a true Eclipser could lower the island's barriers—and Frio refused to be lured in—she let Asher clear the path to the Inner Shrine for Team Siara.
- **Siara Admin Harry's True Allegiance & Helicopter Escape (Turns 33375-33421)**: **Harry** arrived up the shrine stairs in his Team Siara uniform, knocked Jackson aside from behind, and revealed that he was never Jackson's double agent—he had remained loyal to Marie as **Siara Admin Harry** all along (*"Mom: Lesson number one about life, Ashi. Never trust anyone!"*), before challenging Asher to a 4-Pokémon boss battle (`Lapras♂ Lv32`, `Shiftry♀ Lv33`, `Zoroark♂ Lv32`, and **Eclipsed Vikavolt♂ Lv33**). After Asher defeated Harry (with Harry remarking *"Seeing Marie's own son fight for his Dad... What an honor I must say"*), a helicopter appeared above the ancient shrine and dropped a ladder, allowing Marie, Harry, and the grunts to escape with the mysterious gem from the altar (`14, 14`). As Jackson regained consciousness, Professor Ivo observed that *"Harry isn't someone who would betray a friend just like that..."*.
- **Solare Island Epilogue — The Mysterious Investigator (`14, 15`, Turns 33421-33423)**: After Professor Ivo called the authorities for a boat to bring Asher, Dad, Valora, and herself back to her laboratory in Lancio Town, an unknown trainer (`???`, wearing a cap, red scarf, and green vest) emerged from behind the trees at the Solare Island Inner Shrine (`14, 15`). Reporting over the phone to a female colleague whose radar had detected an odd signal there, he noted that a perfectly shaped sphere appeared to have been taken from the rock formation by the people in the helicopters he heard earlier, photographed the shrine for her, and departed.
## Lancio Town Basement Lab Briefing & Round Five Summons
- **Post-Solare Island Briefing (`14, 16` in Ivo's Basement Lab -> Amor City `59, 27`, Turns 33423-33425)**: Back in Professor Ivo's Basement Laboratory in Lancio Town, Ivo admitted they still do not know the purpose of the gem Team Siara stole from Solare Island, and noted that while Jackson is studying the World Map for clues, the energy signals at the other two marked locations have grown much weaker. Just then, Asher received a HuPhone message from the **Amor Battle Center** summoning him to **Round Five of the Eclipse Tournament**, along with an advertisement announcing that the **Amor Department Store ("Amor Mall!")** has officially opened in Amor City. Professor Ivo and Dad told Asher and Valora to compete in Round 5 in Amor City and return to the lab in Lancio Town afterward while they try to pinpoint the remaining signals, automatically fast-traveling Asher to **`(59, 27)`** outside the **Amor City Battle Centre**.
## Eclipse Tournament Round Five — Victory Over Sinnoh's Barry
- **Round Five Bracket & Matches (Turns 33429-33455)**: Inside the Amor City Battle Centre's Round 5 Arena (`10, 26` in the Lower Arena Ring), Asher competed in an 8-trainer single-elimination bracket on the holographic cyber-arena stage:
  1. **Quarterfinals**: Defeated **Cooltrainer Summer** (Florges Lv32, Cacturne Lv32, Venusaur Lv32).
  2. **Semifinals**: Defeated **Fisherman Otis** (Octillery Lv32, Gyarados Lv32, Sharpedo Lv33), while Sinnoh's **Barry** defeated Black Belt Adam on the opposite side of the bracket.
  3. **Round Five Finals**: Defeated **PKMN Trainer Barry** from the Sinnoh Region (Dawn's childhood friend, who recognized Asher from Galtino Bridge; uses Staraptor Lv32, Hitmontop Lv33, Empoleon Lv34, and Roserade Lv33) to win his Round Five group and advance to Round Six of the Eclipse Tournament.
- **Post-Round-5 Reunion with Dawn & Valora (`11, 10` in Tournament Arena Lobby, Turns 33457-33461)**:
  - In the Tournament Arena Lobby after Round 5, **Dawn** greeted Asher as `"Mr. Famous"`, invited him out to celebrate, and exchanged phone numbers with him when he explained he was busy.
  - Coming up the escalator (`6, 17`), **Valora** saw Dawn talking closely with Asher and became visibly flustered and jealous despite also passing Round 5, prompting them to head straight back to Professor Ivo's Basement Lab in Lancio Town (`9, 18`).
## Lancio Town Location 2 Briefing & Mission to Route 16
- **Splitting into Two Teams (`9, 18` in Ivo's Basement Lab -> Amor City `59, 27`, Turns 33461-33464)**:
  - In Professor Ivo's Basement Lab, Ivo showed on the World Map that they pinpointed the exact position of **Location 2** (east of Amor City) and that its energy signal has grown strong again, while **Location 3** (another offshore island) still emits a weaker signal in a general area.
  - Ivo and Jackson decided to split into two teams: **Professor Ivo and Valora** headed offshore to investigate **Location 3**, while **Dad (Jackson) and Asher** teamed up to tackle the more dangerous **Location 2**, which Dad explained can be reached via **Route 16** from Amor City, automatically warping Asher to **`(59, 27)`** outside the Amor City Battle Centre.
## Route 16 Collapsed Bridge — Dad & The FastSwift Service App (`76, 12`, Turns 33627-33630)
- **The Collapsed Bridge to Aurin Town (`76, 12`)**: At the eastern cliffside of Route 16 (`76, 12`), Asher discovered that the wooden bridge across the water had collapsed. **Dad (Jackson)** climbed up to join him (`76, 13`), noting that a storm had torn the bridge apart and explaining that **Aurin Town** lies on the other side of the water (*"It's not the friendliest place in the region, but we got no choice."*).
- **The FastSwift Service App (Surfing Mechanic)**: To cross the water without the bridge, Dad gave Asher the **FastSwift** service app on his **HuPhone**, which rents an inflatable boat to surf across any body of water by pressing the **A Button** while facing water (*"Asher obtained the FastSwift service app on his HuPhone! / When facing a body of water, press the 'A Button' to surf."*).
- **Father-Son Talk & Location 3 Cutscene (`75, 12` on Route 16 & `10, 16` Offshore Island, Turns 33630-33641)**:
  - Noticing Asher spacing out since Round 5, Dad gave Asher advice on apologizing to make peace even when you aren't sure what you did wrong.
  - Meanwhile, on a small offshore island south of Galinor City (**Location 3**), **Professor Ivo** and **Valora** deduced that the third signal is underwater (adjacent to a deep ocean dive trench). When Ivo asked why Valora was helping them, Valora shared that Asher's bravery in Sovio City inspired her to become strong, and Ivo thanked her for being a true friend to Asher—before accidentally letting slip that she once had feelings for Jackson before Marie ("that lunatic") appeared.
## Aurin Town — The Slum of Hupest & The Ruins of Aur Factory (`9, 19`, Turns 33722-33726)
- **Arrival in Aurin Town (`9, 19`)**: Upon entering **Aurin Town** from Route 16 East (`60, 18` <-> `1, 18`), **Dad (Jackson)** met Asher at `(9, 19)` and described Aurin Town as *"The slum of Hupest. This is where most criminals and deliquents band together..."*.
- **Clue About the Old Factory Ruins (`11, 19`)**: Questioning a local man at `(11, 19)` about anything unnaturally weird happening recently, Dad and Asher learned that wild Pokémon in the **old factory's ruins** (at the top of the northern stairs) have been behaving abnormally and violently attacking people.
- **Aur Factory**: Recognizing the ruined facility at the top of the northern cliff stairs as **Aur Factory** (*"Aur Factory huh... Or at least what's left of it. ... Yes... I know it quite well, but I never thought I would see it again after all those years... Let's go!"*), Dad joined Asher to investigate the ruins of **Aur Factory**.
  - **Origin of Siara & Bankruptcy of Aur Inc. (`26, 29` -> `24, 30` in Aur Factory 1F, Turns 33761-33764)**: Descending the ladder inside the exterior ground pit (`26, 28 -> 26, 29`) into **Aur Factory 1F**, Dad revealed that when he was Asher's age, **Aur Inc.** was a thriving industrial factory manufacturing basic items, cars, and electronics, and **Aurin Town** housed its workers—including Asher's grandparents. When outside companies entered Hupest, Aur Inc. went bankrupt, leaving the workers jobless and turning Aurin Town into an impoverished slum. Jackson originally founded **Siara** to give the poor, unemployed people of Aurin Town jobs and achieve something big, before Marie took Siara down a dark path he could not support.
  - **Aur Factory Inner Chamber — Admin Flo, The Second Gem & The Mysterious Boy (`13, 9` -> `16, 9`, Turns 33857-33864)**:
    - In a flashback (*"A little bit earlier..."*), the mysterious boy (`???`, wearing a grey cap and red scarf) confronted **Siara Admin Flo** and two grunts inside the Aur Factory inner chamber (`16, 9`), asking what they planned to do with the gems. Once her grunts retrieved the **second gem** from the stone pedestal (`16, 8`) and signaled that the helicopter had arrived, Flo escaped by helicopter with the gem, while the boy's female colleague ordered him over the phone not to pursue them and to return.
    - Entering the chamber moments later (`16, 9`), Asher and Dad spotted the mysterious boy before he vanished in a flash to escape. Inspecting the empty sphere socket on the pedestal (`16, 8`, identical to the formation on Solare Island), Asher and Dad suspected the boy might have taken whatever was inside.
    - Immediately afterward, Asher received a HuPhone text message from the **Amor Battle Center** summoning him to **Round Six of the Eclipse Tournament**, and Dad told Asher to head back to Amor City for Round Six while Dad calls Professor Ivo to arrange another meeting.
## Eclipse Tournament Round Six — Victory Over Sinnoh's Riley
- **Round Six Bracket & Matches (Turns 33867-33905)**: Inside the Amor City Battle Centre's Round 6 Arena (`13, 26` in the Lower Arena Ring), Asher competed in an 8-trainer single-elimination bracket on the holographic cyber-arena stage:
  1. **Quarterfinals**: Defeated **Scientist Albert** (Ditto Lv35, Manectric Lv35, Porygon-Z Lv36, Cryogonal Lv35).
  2. **Semifinals**: Defeated **Sailor Kyle** (Pelipper Lv35, Machamp Lv36, Whiscash Lv35, Poliwrath Lv36), while Sinnoh's **Riley** defeated Ruin Maniac Burt on the opposite side of the bracket.
  3. **Round Six Finals**: Defeated **PKMN Trainer Riley** from the Sinnoh Region (Absol Lv35, Lucario Lv37, Metang Lv35, Blaziken Lv36, Gyarados Lv36) to win his Round Six group and advance to Round Seven of the Eclipse Tournament.
- **Post-Round-6 HuPhone Message from Dad (`12, 25` in Lower Arena Ring, Turn 33906)**:
  - Stepping onto `(12, 25)` after winning Round 6 triggers a HuPhone text message from **Dad**: *"Hey, son! I heard the round ended. Hope you did well, I managed to call Ivo and we are meeting in Maple Town! We also texted Valora, so we're all metting up there!"*.
  - Asher resolves to head to **Maple Town** to meet Dad, Professor Ivo, and Valora.
## Post-Round-6 World Map Verification (Turns 33909-33916)
- **Bugiaret Island Routes & Towns**: Confirmed that **Galinor City** connects south via **Route 13** and **Route 8** to **Mulberry Town** (southwest green square) and **Maple Town** (southeast green square, directly adjacent to the Location 3 offshore island), and west/south via **Route 9** and **Route 7**.
- **Northeast & Eastern Mainland**: **Route 14** and **Hupestian Ruins / Mt. Nit** lead northeast from Amor City to **Eclipse Square** (`E.S.` on the Hupest Metro Line), while the eastern coast features **Wild Area** and **Dis Bay** (`Metro Station`).
- **Cord Island**: Southeast offshore island containing **Route 18** and **Battle Marine**.
## Route 13 Wheat Field — Reconciliation with Valora (`32, 26` -> `39, 32`, Turns 33947-33952)
- **Heart-to-Heart in the Wheat Field**: Encountering **Valora** on Route 13 (`32, 28`) on the way to Maple Town, Asher remembered Dad's advice from Route 16 and asked to talk. Valora led Asher into the golden wheat field (`39, 31-32`) for privacy and tearfully confessed that despite everything they had been through together, she felt they still had much to learn about each other, wondered what was going on between Asher and Dawn, and was afraid of drifting apart from him.
- **Asher's Promise**: Hugging Valora and apologizing for making her worry, Asher promised he would never leave her behind, vowed to open up to her more from now on, and offered to help guide her toward her goal of becoming strong and independent. Flustered (*"'ba-dump' A-alright... I mean... Alright! ... Gah... why is my heart beating so fast..."*), Valora reconciled with Asher and joined him to meet Dad and Professor Ivo in **Maple Town**.
## Maple Town — Reunion with Dad & Professor Ivo & Frio's Eavesdropping (`29, 7`, Turns 34046-34049)
- **Location 3 Underwater Briefing**: Meeting **Dad (Jackson)** and **Professor Ivo** outside the Maple Town Pokémon Center (`29, 7`), Asher and Valora learned that Professor Ivo's gladness at their reconciliation was tempered by a difficult obstacle: the third Eclite/gem signal at **Location 3** is deep underwater, and scanning the sea floor without specific clues would take too long.
- **Frio's Recognition of the Underwater Location**: Valora and Asher spotted **Frio** eavesdropping behind Professor Ivo (`28, 12`). Recognizing the underwater place they were discussing (*"Underwater location? No... They can't be talking about that damn place..."*), Frio realized he had made eye contact with Asher and Valora and hurried west into Maple Town (`row 12`).
## Mulberry Town — Frio's Terror, Round Seven Summons & Wager (`11, 18`, Turns 34175-34179)
- **Confronting Frio Outside the Western House (`8, 17` -> `11, 18`)**: In the southern plaza of Mulberry Town (`11, 18`), Asher and Valora spotted **Frio** exiting the unoccupied western house (`8, 17`, whose signpost at `9, 18` reads *"For sale! Call 515-808-2362 for details."* and whose 2F bedroom rug at `19, 6` holds an **Eclite Shard**, verified Turns 34181-34184), where he claimed to be handling personal business. (A neighboring townswoman at `14, 19-20` reveals that Frio was the son of the couple who lived in that house next door before disappearing—and that according to rumors, the family was attacked by weird Pokémon and sacrificed themselves to save their child, verified Turns 34191-34193.) When Asher and Valora explained that Team Siara had stolen two gems and that the third energy signal was at an underwater location, Frio's face was covered in terror (*"U-underwater location? Siara? Some gems?"*).
- **Round Seven Summons & Frio's Wager**: Just as Valora pleaded with Frio for information and he hesitated, all three trainers received a HuPhone text message from the **Amor Battle Center** summoning them to **Round Seven of the Eclipse Tournament**. Frio proposed a wager: if Asher advances through Round 7, Frio will share what he knows about the underwater location (*"If you manage to get through the round, I will give you two the information you need... So make sure to win! Besides... I didn't change my mind about battling you in the Finals!"*). Before heading north, Frio advised Asher that the fastest way back to Amor City is by taking the Metro from **Galinor City** via **Route 9** (*"Going through Route 9 might be better than where you came from. Good luck... Asher..."*).
## Eclipse Tournament Round Seven — Victory Over Unova's Hugh
- **Round Seven Bracket & Matches (Turns 34269-34307)**: Inside the Amor City Battle Centre's Round 7 Arena (`17, 26` in the Lower Arena Ring), Asher competed in an 8-trainer single-elimination bracket on the holographic cyber-arena stage:
  1. **Quarterfinals**: Defeated **Gentleman Jonathan** (Arcanine Lv37, Alomomola Lv38, Lumineon Lv37, Manectric Lv38).
  2. **Semifinals**: Defeated **Battle Girl Sachi** (Medicham Lv37, Hariyama Lv37, Blaziken Lv38, Emboar Lv38), while Unova's **Hugh** defeated Scientist Jesse on the opposite side of the bracket.
  3. **Round Seven Finals**: Defeated **PKMN Trainer Hugh** from the Unova Region (Unfezant Lv37, Bouffalant Lv38, Simisage Lv37, Eelektross Lv38, Samurott Lv39) to win his Round Seven group and advance to Round Eight of the Eclipse Tournament.
- **Post-Round-7 Revelation — The Abandoned Undersea Siara Laboratory & Ivo's Urgent Summons (`16, 25` -> `19, 13` -> Maple Town `43, 15`, Turns 34308-34312)**:
  - In the Tournament Arena Lobby (`19, 13`), **Frio** kept his promise and revealed that the underwater Location 3 signal is most likely an old, abandoned **undersea laboratory of Team Siara** located below sea level near **Maple Town**.
  - When Asher invited Frio to help them end Team Siara once and for all, Frio confessed he hates Team Siara more than anything in his life—only having intervened in Destino Mine because they took an Eclite Shard from him—and refused to get involved with Marie, their experiments, or that lab ever again before walking away.
  - Moments later, Asher received an urgent HuPhone message from **Professor Ivo**: *"Asher! Quick pick up Valora and come here quick! We are on a small isle from Maple to the south, this is urgent!"*. Picking up Valora, Asher fast-traveled to the southern shoreline stairs of **Maple Town** (`43, 15`).
## Small Offshore Isle (Location 3) — The Newly Opened Cave to the Abandoned Siara Lab
- **Reunion on the Southeastern Terrace (`32, 46` -> `33, 46`, Turns 34372-34373)**: On the small offshore isle in Hupest Sea (`Location 3`), Asher and Valora reunited with **Professor Ivo** (`36, 46`) and **Dad (Jackson)** (`36, 42`). When Asher shared Frio's warning that Location 3 is an old, abandoned undersea laboratory of Team Siara, Professor Ivo revealed that a cave entrance (`36, 40`) had just been opened into the cliffside since her earlier visit—meaning Team Siara had most likely already breached the path to the undersea lab. Ivo, Dad, and Valora hurried inside (`36, 40`) with Asher following right behind.
- **Entering the Abandoned Undersea Laboratory (`5, 7` -> `5, 4`, Turns 34382-34384)**: Inside the underground stairwell beneath the island cave, Professor Ivo noted that the 10-year-old facility still had electricity running. Dad repaired the jammed elevator panel (`4, 4`), and everyone entered the elevator (`6, 15`), which connects five floors (`5F` through `1F`).
- **The Offline Main Generator & Eclipsed Pokémon Warning (`37, 6` on 2F, Turns 34389-34391)**: Stepping out onto Floor 2F (`37, 6`), Asher received a HuPhone call from **Professor Ivo**, who explained that only the elevator is running on a backup generator while all security doors remain locked until the **main generator** is turned back on in the **generator room**. Ivo also warned Asher to be careful because the abandoned undersea laboratory is full of **Eclipsed Pokémon**.
- **Restoring the Main Generator & B5F Signal (`29, 12` in B3F Machine Room, Turns 34415-34420)**: In the B3F Machine Room (`29, 12`), Asher flipped the main generator switch to restore facility power. **Professor Ivo** called on the HuPhone to confirm the power was back on, revealed that the third energy signal is coming from the lowest floor (**B5F**, which requires an **Ec Card** to access), and warned Asher right before a rampaging **Lv40 Eclipsed Golem** ambushed him at the generator switch.
- **Marie's 2011 Diary (`34, 18` on B2F, Turns 34426-34429)**: On a table in the southern section of B2F, Asher found an old diary written by **Marie** on **April 5th, 2011** (shortly after Jackson left with 5-year-old Asher): *"This is it! I have finally set up the entire Laboratory. Here I'll fully develop out Eclipsing, so that Jackson will believe that it's safe. Can you believe he left with our 5 year old son?! I can't mess this up. If I prove this is completely safe we can be a family again..."*.
- **Marie's 2013 Diary on Frio, the Gem & Eclite (`30, 15` on B4F, Turns 34437-34438)**: In the B4F Community Room, Asher read a second diary entry written by **Marie** on **September 1st, 2013**: she adopted the little boy from two years earlier (whose parents in Mulberry Town were attacked by Eclipsed Pokémon), named him **Frio**, and discovered that a **gem** Frio always kept with him calmed violent Eclipsed Pokémon down and made them controllable. She also recorded that Eclipsing is tied to **Eclite**, whose extraterrestrial origin cannot be replicated with Earth elements, requiring Team Siara to gather large quantities of Eclite.
- **Marie's 2014 Diary on Frio's Eclipser Bloodline (`31, 17` on B4F, Turns 34442-34443)**: Right beside the B4F console, Asher found a third diary entry written by **Marie** on **October 31st, 2014**: she discovered that **Frio** belongs to an **Eclipser** family—a bloodline able to channel their spirit through Eclite to Eclipse Pokémon without technology—and after creating a test subject that did not require life-sustaining equipment, she resolved to train Frio's Eclipser power in the undersea laboratory to unlock the full potential of Eclite.
- **The Ec Card & Marie's 2015–2016 Evacuation Diary (`11, 18` & `13, 20` on B4F West, Turns 34460-34461)**: Inside the western room of B4F (unlocked with Code Green), Asher recovered the **Ec Card** from a broken table (`11, 18`) and read Marie's final diary entries (`13, 20`): on **June 6th, 2015**, she developed a quick, cheap method of Eclipsing Pokémon and crafted a special band for Frio's training; on **April 5th, 2016** (exactly five years after opening the lab), the Eclipsed Pokémon went berserk across the entire laboratory, forcing Marie and Team Siara to evacuate immediately and seal the facility away.
- **B5F Inner Chamber — Colen Champion Micah & Securing the Third Gem (`8, 6` -> `8, 5`, Turns 34477-34494)**:
  - Reaching the lowest floor (**B5F**) using the **Ec Card**, Asher found the mysterious boy (`???`) at the third gem pedestal (`8, 3`) before Team Siara arrived.
  - Mistaking Asher and Dad (Jackson) for Team Siara members after seeing them at Aur Factory, the boy battled Asher (`Staraptor♀ Lv40`, `Aggron♂ Lv41`, `Samurott♂ Lv41`, `Sceptile♂ Lv42`).
  - After Asher defeated him and cleared up the misunderstanding alongside Dad, Professor Ivo, and Valora, the boy introduced himself as **Micah, Champion of the Colen Region**, who came to Hupest with his support team to investigate Team Siara and learned about Eclipsing and the spheres from Cynthia.
  - Micah retrieved the **Third Gem** from the pedestal (`8, 3`) and entrusted it to **Professor Ivo**, who immediately returned to her laboratory in Lancio Town to secure it, while Micah promised to help Asher's group take down Team Siara when the time comes.
- **Location 3 Epilogue — Micah's Return to Light Island, Frio Enters the Lab & Round Eight Summons (`8, 12` on B5F -> `36, 42` at Location 3, Turns 34497-34510)**:
  - Stepping out of the B5F Inner Chamber triggered an epilogue scene outside on the Small Offshore Isle: Colen Champion **Micah** assured his female colleague over the phone that Asher's group are allies heavily involved against Team Siara and teleported back to **Light Island** in the **Colen Region** to prepare plans with his team.
  - Moments later, **Frio** arrived outside the Location 3 cave entrance (`36, 42`), forced himself to overcome his trauma (*"Here I am again... Just thinking of this place makes me feel devastated... Argh! Keep it together Frio! Don't scare quit now!"*), and walked inside (`36, 40`).
  - Exiting the cave to `(36, 42)`, Asher received a HuPhone text message from the **Amor Battle Center** summoning him to **Round Eight of the Eclipse Tournament**—the final traditional round before the Finals.
## Eclipse Tournament Round Eight — Victory Over Alola's Gladion & Qualification for the Finals
- **Round Eight Bracket & Matches (Turns 34548-34578)**: Inside the Amor City Battle Centre's Round 8 Arena (`20, 26` in the Lower Arena Ring), Asher competed in an 8-trainer single-elimination bracket on the holographic cyber-arena stage, with the host announcing that everyone who clears Round 8 will be featured in the Finals:
  1. **Quarterfinals**: Defeated **Cooltrainer Quentin** (Luxray Lv39, Toxicroak Lv39, Talonflame Lv40, Cacturne Lv40).
  2. **Semifinals**: Defeated **Cooltrainer Lola** (Gastrodon Lv39, Delphox Lv40, Ampharos Lv39, Lilligant Lv40), while Alola's **Gladion** defeated Expert Bert on the opposite side of the bracket.
  3. **Round Eight Finals**: Defeated **PKMN Trainer Gladion** from the Alola Region (Crobat Lv40, Zoroark Lv40, Lucario Lv40, Charizard Lv41, Silvally Lv42) to win his Round Eight group and officially qualify for the Eclipse Tournament Finals.
- **Post-Round-8 Announcement — Finals on Eclipse Square via Route 14 (`19, 25`, Turns 34579-34582)**:
  - Stepping onto `(19, 25)` in the Lower Arena Ring triggers the Host's PA announcement concluding Round 8 and summoning all finalists and spectators to **Eclipse Square** via **Route 14**.
  - A cutscene in the upper lobby shows that Sinnoh's **Lucas** and **Dawn** also qualified for the Finals (with **Barry** accompanying them to watch) while **Frio** stands silently nearby.
- **Route 14 River Bridge — Reunion with Valora (`26, 11`, Turns 34600-34601)**:
  - Crossing onto the wooden river bridge on Route 14 (`26, 11`), Asher reunited with **Valora** (`29, 11`), who happily shared that she also won her Round Eight group to qualify for the Finals and that Professor Ivo gave them the green light to head to **Eclipse Square** while Team Siara is quiet.
  - Insisting he wouldn't let her make such a long journey alone, Asher invited Valora to travel together, and she gladly joined him for the trek to Eclipse Square.

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
     - **Controls**: D-pad moves cursor; START button immediately snaps cursor to bottom-right '[X]' ('Close Map'); pressing A on '[X]' or B button exits back to the HuPhone menu (resetting the main HuPhone cursor to the top option `Item Storage`, so closing the HuPhone after exiting the World Map requires `Down 3 -> A` to select `Back`, verified Turn 32620).
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
    6. Lost Eevee (Paused at Explorer `42, 12` in Destino Mine 1F in Turn 32613 after auditing all accessible tiles of 1F, 2F, and the Inner Den; frees the single active quest slot for Route 12 and Jarro Town until western Destino City unlocks)
    7. Kaboom (Completed in Turn 32170 — found the lost Dynamite in the southwestern sand patch at Route 6 `27, 34`, defeated the ambushing Lv20 Gible, and delivered the Dynamite to the Coworker at Route 6 `43, 19` to blast open the collapsed Route 6 mine entrance at `44, 18-19`; rewarded **Rocky Helmet**)
    8. Valentines Gift (Active — accepted from the boy in blue overalls at Route 12 Main `16, 75` in Turn 32745; objective is to find 3 missing flowers [standard Poké Ball sprites] across Route 12, with `Flower 3` collected at `18, 47` into Key Items Pocket in Turn 32835)
    9. Angry Cubone Kid (Provider located at Jarro Town `22, 15` in front of the fenced Cubone pen `23, 13`; observed Turn 32928)
    10. Push it! (Provider: Sailor located at Galinor City `54, 41` in the shipping container yard; observed Turn 33043)
  - **Page 3 Quests**:
    11. Oak's Research (Special Quest — accepted at Azluf Town `40, 7` in Turn 28501; Task 1 [10 Pokémon caught] completed in Turn 28681, rewarding **Bulbasaur**; Task 2 [25 Pokémon caught] completed in Turn 29958, rewarding **Charmander**; Task 3 [45/50 Pokémon caught] completed in Turn 31043, rewarding **Squirtle** and bringing Owned species to **51 Hupest / 20 Colen**; Professor Oak now states *"Thank you, this will be enough, but come back later, I might have some more tasks for you!"* and `Quest Status` reports *"You aren't doing any Quest currently..."*, while `Page 3 -> 11. Oak's Research` still displays *"This Quest hasn't been completed yet."*, verified Turns 31045-31051)
    12. Elm's Research (Special Quest — accepted at Destino City `33, 18` -> `6, 6` in Turn 33006; Task 1 [60 species caught] completed in Turn 33007 rewarding a **Pokémon Egg**; Task 2 [80 species caught] completed in Turn 34586 rewarding a second **Pokémon Egg**; Task 3 assigned: show Professor Elm a PokéDex with **100 species caught**)
    13. Rowan's Research
    14. Cynthia's Research
    15. Help for Barry
  - **Page 4 Quests**:
    16. - Not available -
    17. - Not available -
    18. Roark's Opal (Completed in Turn 28444; rewarded all 11 Fossils; verified in Turn 33743 that PC Item Storage is currently empty and 0 fossils remain in Bag/PC)
    19. Pokédex!
    20. Marine Point Hunter
  - **Page 5 Quests**:
    21. Hugh's Pokémon (Special Quest — accepted from Hugh at Amor Department Store 2F `11, 7` in Turn 34675; Task: show Hugh a PokéDex with **150 species** registered to receive three rare Pokémon from Unova)
    22. Silver's Deal
    23. Back to the...
    24. Outcasts
    25. The Mods of Cord
  - 'Quest Status': When a quest is active, displays the currently tracked quest status and system instructions. When no quest is active, displays 'You aren't doing any Quest at the moment!'.
  - HuPhone Menu & Quest Navigation: Neither the main HuPhone app menu nor the Quest List dismiss with the B button. The player must explicitly navigate down to 'Back' or 'Exit' and press A to close them.

## Pokémon Center Respawn Mechanics

- **Whiteout / Blackout Respawn Point**: Respawn points are set only when speaking to Nurse Joy at the counter to heal. Simply entering a Pokémon Center without talking to Nurse Joy does NOT register a new checkpoint.

## Verified Inventory State & Field Move Capabilities

- **Items Pocket (Audited Turn 34369)**: Contains **Destiny Knot x1** (received from Professor Ivo in Lancio Town at 50 Owned species in Turn 31109), **Water Stone x2** (collected 1 at `(16, 14)` in the Closed Segment of Mt. Gerhana in Turn 31654 and 1 at Galinor Cargo Loading Bay Western Pier `18, 20` in Turn 33054), **Thunder Stone x1** (collected at Route 6 `23, 21` in Turn 32168), **Leaf Stone x1** (collected at Route 13 `50, 38` in Turn 34044), **Rocky Helmet x1** (rewarded at Route 6 `43, 19` for completing Quest #7 "Kaboom" in Turn 32170), **Repel x0**, **Super Repel x15** (purchased 20 at Destino City PokéMart in Turn 33401; used 1 at Hupest Sea `42, 32` in Turn 34369, 1 at Undersea Lab B2F `34, 17` in Turn 34424, 1 at Undersea Lab B4F `16, 18` in Turn 34457, 1 at Hupest Sea `23, 38` in Turn 34513, and 1 at Route 13 `31, 20` in Turn 34538), **Super Potion x0**, **Oval Stone x1** (collected at Route 4 `39, 20` in Turn 31853), **TinyMushroom x1** (collected at Route 6 `41, 28` in Turn 32053), **King's Rock x1** (collected at Route 6 `23, 13` in Turn 32098), **Red Shard x1** (collected at Destino Mine `40, 13` in Turn 32208), **Fire Stone x1** (collected at Destino Mine 2F `29, 21` in Turn 32381), **Hyper Potion x13** (purchased 15 at Destino City PokéMart in Turn 33401, used 1 on Sirius in Turn 33522, collected 1 at Route 13 `8, 30` in Turn 34001, used 1 on Sirius in Turn 34351, and used 1 on Sirius at Route 14 `29, 13` in Turn 34622), **Clear Shard x1** (obtained at Destino Mine Inner Den `13, 15` in Turn 32471), **Iron x1** (collected at Destino Mine 1F `42, 40` in Turn 32582), **Revive x11** (purchased 10 at Destino City PokéMart in Turn 33401; collected 1 at Undersea Lab B4F `36, 15` in Turn 34443), **Revival Herb x1** (collected at Route 13 `48, 37` in Turn 34035), **Burn Heal x1** (collected from spray bottle sprite at Route 12 Main `33, 46` in Turn 32830), **X Special x0**, **Link Cable x1** (collected from capsule sprite at Route 12 Main `23, 10` in Turn 32884), **Odd Keystone x1** (gifted by Sinnoh Champion Cynthia outside the Jarro Town Pokémon Center at `14, 30` in Turn 32911; fits the ancient stone tower in the secret Route 6 section of Destino Mine 1F), **Carbos x1** (collected from purple bottle sprite at Route 11 Main `60, 27` in Turn 33024), **Ether x1** (collected from purple spray-bottle sprite at Aur Factory Exterior `29, 12` in Turn 33806), **Big Pearl x1** (collected from gold ball sprite at Solare Island Western Shoreline `17, 47` in Turn 33249), **Max Repel x0** (collected 1 at Solare Island Forest `24, 30` in Turn 33343 and used at `46, 32` in Turn 33411), **Eclite Piece x1** (collected from gold ball sprite at Solare Island Forest `32, 27` via the `row 23` stone wall passage in Turn 33345), **Stick x1** (collected from gold ball sprite at Route 13 `25, 35` in Turn 33966), **Star Piece x1** (collected from gold ball sprite at Route 8 `23, 23` in Turn 34142), **Eclite Shard x2** (collected 1 from gold ball sprite at `19, 6` on 2F of the unoccupied 'For sale!' Western House `8, 17` in Mulberry Town in Turn 34184, and 1 behind the Code Red security door at Undersea Lab B2F `30, 4` in Turn 34431), and **Max Potion x1** (collected from spray-bottle sprite at Route 9 `13, 25` in Turn 34208), and **Full Restore x1** (collected from spray-bottle sprite at Undersea Lab B2F `38, 16` in Turn 34429).
- **Overworld Healing Animation Timing**: Using a healing item (`Super Potion`) from the overworld Bag plays a full-screen Pokémon sprite animation (~3500ms) before returning to the Party screen and displaying `"<Pokémon>'s HP was restored by <N> point(s)."` (verified Turn 33185).
- **Key Items Pocket (Audited Turn 34460)**: Contains **HuPhone**, **TM Case**, **Metro Pass**, **Eclipse Band**, **Fishing Rod**, **Rare Opal** (retained in Key Items after completing Quest #18), **Itemfinder** (rewarded at Route 4 `46, 13` for completing Quest #5 in Turn 31891; **Dynamite** was delivered to the Coworker at Route 6 `43, 19` in Turn 32170), **Flower 3** (collected at Route 12 Main `18, 47` for Quest #8 in Turn 32835), and **Ec Card** (collected at Undersea Lab B4F West `11, 18` in Turn 34460; unlocks Floor `5F`/`B5F` on the lab elevator).
- **Repel Auto-Renewal Prompt**: When an active Repel expires on a step, the engine automatically displays: "Repel's effect wore off... Use another? Yes/No" (cursor defaults to Yes; pressing A immediately consumes and applies the next Repel without opening the Bag, verified Turn 27448).
- **Bag Structure (Audited Turn 27862)**: Features 3 main horizontal pockets from left to right: **Items** (Pocket 1), **Key Items** (Pocket 2), and **Poké Balls** (Pocket 3; does not wrap around when pressing Right).
- **Poké Balls Pocket (Audited Turn 34712)**: Contains **Poké Ball x0**, **Great Ball x0**, **Ultra Ball x36** (purchased 50 at Amor Dept. 2F `8, 5` for `₽60,000` in Turn 34672, leaving `₽36,966`; used 5 catching wild Lv32 Amoonguss "Morel" at Route 14 `38, 8` in Turns 34687-34691, 2 catching wild Lv33 Sharpedo "Mako" at Route 14 `29, 8` in Turn 34699, 4 catching wild Lv32 Unfezant "Plume" at Route 14 `37, 8` in Turns 34703-34704, and 3 catching wild Lv33 Skarmory "Aegis" at Route 14 `36, 12` in Turns 34709-34711), **Dive Ball x0**, **Net Ball x0**, and **Luxury Ball x0**. Total Owned species in PokéDex: **85** (completed Task 2 of Professor Elm's Research in Turn 34586; Task 3 requires 100 species, and Hugh's Quest #21 requires 150 species).
- **Key Items Pocket (Audited Turn 27862)**:
  - **HuPhone** (registered to `[SELECT]`): *"A convenient smartphone that has many features to use."*
  - **TM Case**: *"A case that holds TMs and HMs. It is attached to the Bag's compartment for important items."*
  - **Metro Pass**: *"Its a card that can be used at the e-ticket reader gates to travel on the Hupest Metro Line."*
  - **Eclipse Band**: *"A special band designed to channel the power of Eclipse Shards to allow Eclipsing!"* (received from Professor Ivo in Azluf Town, Turn 27799).
  - **Fishing Rod**: *"A new, high-quality fishing rod. Use it by any body of water to fish for wild Pokémon."* (received from Fisherman at `37, 30` in Azluf Town, Turn 27854). Casting into water prints `. . .` dots and automatically resolves to either *"A Pokémon's on the hook!"* (requiring a single A/B press to start the wild battle, with no timing minigame) or *"Not even a nibble..."* (verified Turn 27865).
- **TMs & HMs Pocket**: Contains TM03 (collected at Route 4 `53, 17` in Turn 31892), TM08 (Payback, collected at Aur Factory 1F West `17, 17` in Turn 33815), TM10 (Dark Pulse, collected at Undersea Lab B4F Ailing Room `37, 28` in Turn 34472), TM17 (Protect), TM18 (Rain Dance, collected at Aurin Town Western Cliff Island `8, 12` in Turn 33716), TM27 (Return, collected at Hupest Sea Small Offshore Isle `32, 36` in Turn 34362), TM36 (Sludge Bomb, collected at Route 8 `21, 14` in Turn 34141), TM37 (Sandstorm, collected in Destino Mine 1F at `32, 35` in Turn 32317), TM39 (Rock Tomb, collected in Upper Mt. Gerhana at `43, 9` in Turn 31547), and TM48 (Work Up). Zero HMs in possession.

- **Empirical Constraint & Equipment Mechanic**: Interacting with cracked/rugged rocks in Sovio Sewers displays verbatim: "It's a rugged rock, but with some equipment, I could smash it." Confirmed that smashing rugged rocks is mechanic-gated by specialized equipment rather than traditional HM Rock Smash (verified at `6, 23` and `22, 10` in Sovio Sewers, Turns 27495 & 27512).

## Trainer Card Structure & Display
- **Front Layout**: Name (Asher), ID No. (54592), Money, Playtime. Features '*ROUNDS' row tracking 8 Poké Ball icons for the Eclipse Tournament.
- **Back Layout**: Displays 6 dark badge/crest silhouettes, red geometric stripes, and regional circular crest.
- **Card Controls**: Pressing A on either side initiates a 3D flip animation between Front and Back. Pressing B when settled on the Front exits back to the Start Menu.
## Start Menu Structure & Pokédex Status
- **Start Menu Entries & Cursor Memory**: Displays Pokédex, Pokémon, Bag, Asher (Trainer Card), Save, Option, Exit. The Start Menu persists its last highlighted row across openings in the overworld rather than resetting to the top entry (verified Turn 32738). In battle, switching a Pokémon out (including via forced switch moves like `Roar`) and sending it back in later in the same battle resets its Fight menu cursor to Slot 1 (verified Turn 32734).
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
- **Selecting a Destination Inside the Train Car (`4, 5` Seat Trigger)**: Stepping `Left` from `(5, 5)` into the purple passenger seat at `(4, 5)` sits Asher down and prints: *"Which city do you want to go to?"* (which requires an `A`/`B` press plus `sleep 800` to open the 8-station list box: `0: Amor`, `1: Sovio`, `2: Samurion`, `3: Destino`, `4: Galinor`, `5: E.S.`, `6: Colen`, `7: Dis Bay`; verified Turn 32996). Selecting a station not yet unlocked displays *"You can't go to that city yet!"*, while selecting an unlocked station (`Amor`, `Sovio`, `Samurion` [exits to `37, 25` in Samurion City], or `Destino` [exits to `45, 14` in Destino City]) announces *"The next station is... <City>!"* and warps to `(22, 17)` on the destination station platform (`Left 3, Down 7, Right 5` exits any Metro station to the overworld; verified Turn 32996).

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
  - **Page Flip & Two-Part PC Box Transfer**: Pressing `Select` to toggle uppercase/lowercase requires `sleep 800` before subsequent D-Pad inputs. When catching a new species, `"Gotcha! <Species> was caught!▼"` advances directly to `"<Species>'s data was added to the Pokédex.▼"` with a single `A` press (no EXP box appears on catch), and dismissing `"<Species>'s data was added to the Pokédex.▼"` requires `sleep 3500` for the Pokédex entry screen to fade in before pressing `A, sleep 2000` to reach `"Give a nickname to the captured <Species>? Yes/No"` (verified Turns 33934 & 34700). After pressing `Start` -> `A` to confirm a nickname when the party is full, two sequential messages appear (`"<Name> was transferred to Someone's PC.▼"` followed by `"It was placed in Box 'Box2.'"`), both of which ignore `B` presses and require pressing **`A`** twice (`A, sleep 1800, A, sleep 2500`) to return to the overworld (verified Turn 32248).
- **Battle Bag Fade-In Delay (`3000ms`), Cross-Battle Cursor Memory, & Safe Switch-Decline Timing**: Pressing `A` on `Bag` during battle requires a `sleep 3000` pause for the Bag UI fade-in animation to complete before D-Pad or `A` inputs register (`2500ms` can be ~100ms too short; verified Turns 32393 & 32397). The Bag remembers both the last opened pocket and the last highlighted item row even across separate battles (verified Turn 32515). On the 2x2 battle menu, pressing `Up` when the cursor is on the top row (`Fight` or `Bag`) is a safe no-op for waiting out end-of-turn animations, and `A, sleep 2000, B, sleep 1200, B, sleep 4500` safely advances EXP text and declines the `"Will Asher change Pokémon? Yes/No"` prompt without risking opening the Party screen if a move misses or fails (verified Turns 32516-32532).
- **Side-Facing Wooden Staircase Collision (`3-Tile Tall Graphic`)**: On 3-tile tall side-facing wooden staircases (such as `25, 22-24` in Destino Mine 2F), the tile adjacent to the top railing (`24, 22`) has solid cliff collision; approach along the row aligned with the middle step (`24, 23 -> 25, 23`), which automatically steps diagonally onto the top step (`25, 22`; verified Turns 32379-32380).
- **Samurion City Pokémon Center Exit Routing**: Stepping `Down` off `(7, 8)` inside the Samurion City Pokémon Center requires `sleep 2500` for the door warp to settle at `(23, 48)`, followed by `Right 2` to `(25, 48)` -> `Down 1` to `(25, 49)` -> `Right 3` to `(28, 49)` to bypass the Pokémon Center window (`24, 47`) and southern house roof peak (`24, 50`) (verified Turns 31757-31760).
- **In-Battle X-Item Dismissal & Consecutive Destiny Bond Mechanic (Verified Turns 33129-33130)**: Using a stat-boosting item (`X Special`) from the Bag in battle prints `"<Pokémon>'s <Stat> rose!▼"` inside the Bag screen, which requires an explicit `A`/`B` press before closing the Bag and executing the opponent's turn. Unlike Gen 7+, consecutive `Destiny Bond` does NOT fail in this engine build (verified when a Siara Grunt's Wobbuffet successfully used `Destiny Bond` on consecutive turns in Turns 33126 and 33130).
## FastSwift Service App (Overworld Surfing Mechanic)
- **FastSwift App (`76, 12` on Route 16, Turn 33629)**: Gifted by Dad (Jackson) on Route 16 when the bridge to Aurin Town is found collapsed. Installs the **FastSwift** service app on the **HuPhone**, allowing the player to rent an inflatable boat and surf across any body of water simply by pressing **`A`** when facing a water tile (no HM Surf move slot required).
  - **Shoreline Border Tile Behavior (Verified Turns 33642, 33658-33660, 33670, 34511-34512)**: Straight cardinal rocky water-edge border tiles (e.g. `77, 22` on Route 16, `22, 26` and `27, 23` in Aurin Town Western Bay, or `24, 43` at Location 3) are treated as **water tiles** by the engine, whereas curved corner shoreline tiles (such as `24, 41-42` at Location 3) cannot be surfed onto. Pressing `A` while standing on an adjacent land tile facing a straight shoreline border tile immediately mounts the FastSwift inflatable boat onto that border tile with no confirmation dialogue, and pressing a D-Pad direction from a shoreline border tile toward an adjacent walkable land tile immediately dismounts onto land.
- **Single-Turn Send-Out & KO Sequence (`5000ms` Send-Out Wait, Verified Turns 34292 & 34294)**: From `"<Trainer> is about to use <Pokémon>.▼"`, pressing `B, sleep 1200, B, sleep 5000, A, sleep 400, A, sleep 5500, B, sleep 2500, B, sleep 1200, B, sleep 4500` cleanly declines `"Will Asher change Pokémon?"`, waits `5000ms` for the opponent's send-out animation to reach `"What will <Pokémon> do?"`, executes the currently highlighted move, and advances through faint and EXP text to the next send-out prompt in a single turn.
- **Tournament Bracket Dialogue Box Count (`7, 17`, Verified Turn 34286)**: The initial Quarterfinal bracket announcement has 3 text boxes (`B, sleep 1200, B, sleep 1200, B, sleep 3500`), whereas the post-match Semifinal and Final bracket updates have 4 text boxes (`B, sleep 1200, B, sleep 1200, B, sleep 1200, B, sleep 3500`) before warping to `(4, 14)` on the cyber-arena bridge.
- **Bag Pocket Flip Delay (`600ms`) & In-Battle Hyper Potion Fill Timing (`5000ms`, Verified Turns 34351-34352)**: Switching between the 3 Bag pockets (`Items` <-> `Key Items` <-> `Poké Balls`) plays a ~500ms pocket-flip animation, so consecutive `Left`/`Right` presses without a delay only flip 1 pocket; place `sleep 600` between pocket switches. Using a `Hyper Potion` in battle takes ~5000ms for the HP bar to finish filling before `"<Pokémon>'s HP was restored by <N> point(s).▼"` appears on the Party screen.

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
- **Level**: Lv71
- **Nature**: Relaxed (+Def, -Speed)
- **Ability**: Steadfast (evolved from Quick Feet Riolu; verified Turn 31668)
- **Stats (IV Grades)**: HP (C, 205), Attack (C+, 193), Defense (A-, 187), Sp. Atk (C-, 180), Sp. Def (E, 122), Speed (C-, 127)
- **Current Condition**: 114/205 HP, Healthy (at Route 14 `28, 26`)
- **EXP**: Lv71 (evolved into Lucario at Lv30 during Mt. Gerhana training; declined Fire Punch at Lv32; learned Aura Sphere at Lv34; learned Bulldoze at Lv36; declined Swords Dance at Lv40; declined Low Sweep at Lv44; learned Meteor Mash at Lv48 replacing Metal Claw on Route 12 Main in Turn 32681; reached Lv52 defeating Picnicker Gracie's Leafeon in Turn 32896 and declined Dragon Pulse; reached Lv53 defeating Silver's Crobat in Turn 32979; reached Lv54 in Turn 33091; reached Lv55 in Turn 33210; reached Lv56 in Turn 33381 and declined ExtremeSpeed in Turn 33383; reached Lv57 in Turn 33434; reached Lv58 in Turn 33585; reached Lv59 in Turn 33607; reached Lv60 in Turn 33685 and declined Close Combat in Turn 33687; reached Lv61 defeating Gangster Cony's Absol in Turn 33783; reached Lv62 defeating Scientist Albert's Manectric in Turn 33874; reached Lv63 defeating Riley's Metang in Turn 33896; reached Lv64 defeating Farmer Omar's Tauros in Turn 33965 and declined Flash Cannon in Turn 33966; reached Lv65 defeating Farmer Megan's Meganium in Turn 34018; reached Lv66 defeating Gentleman Leslie's Talonflame on Route 8 in Turn 34159; reached Lv67 defeating Gentleman Jonathan's Arcanine in Round 7 Quarterfinals in Turn 34276; reached Lv68 defeating Hugh's Samurott in Round 7 Finals in Turn 34304; reached Lv69 defeating PKMN Trainer ???'s Sceptile in Undersea Lab B5F in Turn 34486; reached Lv70 defeating Gladion's Zoroark in Round 8 Finals in Turn 34570; reached Lv71 defeating Swimmer Luis's Sharpedo on Route 14 in Turn 34641)
- **Moves**:
  - Slot 1: Meteor Mash (Steel, Physical, 90 power, 90% acc, STAB, 10 PP; 20% chance to raise Attack +1; learned at Lv48 replacing Metal Claw in Turn 32681)
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
- **Level**: Lv16 (leveled up defeating Siara Executive's Lv25 Wobbuffet in Destino Mine 2F in Turn 32423; Stats: HP 48, Attack 32, Defense 23, Sp. Atk 24, Sp. Def 18, Speed 26)
- **Ability**: Intimidate (Cuts the foe's Attack stat upon entering battle; verified Turn 28053)
- **Caught**: Route 2 at `(53, 26)` in standard Poké Ball (Turns 28052-28059)
- **HP**: 48/48 HP (Healthy; healed at Mulberry Town Pokémon Center in Turn 34169)
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