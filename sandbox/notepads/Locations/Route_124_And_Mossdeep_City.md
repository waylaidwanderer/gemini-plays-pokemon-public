# Route 124 & Mossdeep City — Coordinates & Routing

## Route 124 (`(0, 26)` -> Mossdeep City)
- **West Entrance (from Lilycove City `(79, 16)`):** `(0, 26)` (`y_route124 = y_lilycove + 10`).
- **Western Channel Trainers (`(7, 26)`):**
  - **Swimmer♂ Declan `(7, 23)`:** Watches `(7, 26)` — `Gyarados Lv. 34` [Defeated].
  - **Swimmer♀ Grace `(7, 29)`:** Watches `(7, 26)` — `Marill Lv. 34` [Defeated].
- **East & South Route across Route 124 (`(7, 26)` -> `(65, 79)`):**
  - From `(7, 26)`, surf `Right` 23 along `y = 26` to `(30, 26)`, `Down` 2 to `(30, 28)` (bypassing the Swimmer♂ at `(34, 25)`), and `Right` 33 along `y = 28` to `(63, 28)`.
  - From `(63, 28)`, surf `Down` 10 along `x = 63` onto the sandbar tip at `(63, 38)`, walk `Right` 1 and `Down` 2 to `(64, 40)`, and face `Right` to use **Surf** onto `(65, 40)`.
  - From `(65, 40)`, surf `Down` 15 along `x = 65` to `(65, 55)` (south of the Diving Treasure Hunter's island at `x = 67..73, y = 44..50`; note that continuing `Down` to `y = 79` enters **Route 126** `(64, 0)`, where **Swimmer♂ Roland `(61, 74)`** — `Carvanha Lv. 34` & **Triathlete♀ Isabella `(69, 74)`** — `Staryu Lv. 34` watch `(65, 74)` [Defeated]), then surf `Right` 15 along `y = 55` across `(79, 55)` into **Mossdeep City** at `(0, 15)` (`y_mossdeep = y_route124 - 40`).

## Mossdeep City
- **West Entrance (from Route 124 `(79, 55)`):** `(0, 15)` (`y_mossdeep = y_route124 - 40`).
- **Path from Western Shore `(0, 15)` to Mossdeep Pokémon Center `(28, 16)`:**
  - Surf `Right` 9 from `(0, 15)` to step onto the walkable shallow water (`MB_SHALLOW_WATER`) at `(9, 15)`.
  - Walk `Right` 3 to `(12, 15)`, `Down` 12 along `x = 12` to `(12, 27)` (passing south of the Black Belt at `(19, 25..26)` and the cliff corner at `y = 24..26`), `Right` 13 along `y = 27` to `(25, 27)`, and `Up` 10 along `x = 25` up the white staircase `(25..26, 24..26)` to `(25, 17)`.
  - From `(25, 17)`, walk `Right` 3 to `(28, 17)` and `Up` 1 into the **Mossdeep City Pokémon Center** at `(28, 16)` (exiting steps to `(28, 17)`).
- **Steven Stone's House (`(19, 10)`):** Reached from the Pokémon Center `(28, 17)` via `Left` 7 along `y = 17` to `(21, 17)`, `Up` 6 along `x = 21` to `(21, 11)`, `Left` 2 to `(19, 11)`, and `Up` 1 into **`(19, 10)`** (exiting steps to `(19, 11)`). Entering after defeating Maxie & Tabitha at the Mossdeep Space Center automatically triggers Steven Stone to give **HM08 (Dive)** [Completed]. Note: `(18, 16)` is a resident's house to the south.
- **Mossdeep Poké Mart:** Door at `(37, 18)` (reached from `(28, 17)` via `Right` 5 to `(33, 17)`, `Down` 2 to `(33, 19)`, `Right` 4 to `(37, 19)`, and `Up` 1 into `(37, 18)`; inside, walk `Up` 4 from `(3, 7)` to `(3, 3)` and face `Left` to speak to the clerk).
- **Mossdeep City Gym:** Door at `(38, 9)` (exiting steps to `(38, 10)`). Reached from the Pokémon Center `(28, 17)` via `Right` 5 to `(33, 17)`, `Up` 7 along `x = 33` to `(33, 10)`, `Right` 5 along `y = 10` to `(38, 10)`, and `Up` 1 into `(38, 9)`.

## Mossdeep City Gym (`(38, 9)` -> `(6, 35)`)
- **Mechanics:** Stepping onto a colored Floor Switch (`Yellow`, `Blue`, `Green`, `Purple`, `Red`) slides all statues and trainers on the matching-color arrow tracks across the entire Gym by 1 tile along the arrows (4 states mod 4). The arrow tiles themselves do NOT slide the player; the player walks across uncovered arrow tiles like normal floor. Furthermore, trainers standing on conveyor arrow tiles do not spot the player on adjacent uncovered arrow tiles unless rotated by a floor switch (whereas stepping onto a normal floor tile in their line of sight triggers battle normally). In `run_code`, stepping onto a Gym floor switch aborts the current `press_buttons` call and plays the slide animation on the next `press_buttons` call (prepend `"sleep 1500"` before stepping off).
- **Room 1 (`(6, 35)` -> `(3, 28)`):**
  - From the entrance at `(6, 35)`, walk `Up` 4 to `(6, 31)`, `Left` 3 along `y = 31` to `(3, 31)`, and `Up` 1 onto the **Yellow Floor Switch at `(3, 30)`**.
  - Stepping onto `(3, 30)` rotates **Psychic Preston `(2, 30)`** (`Kirlia Lv. 36`) and **Psychic Maura `(4, 30)`** (`Kadabra Lv. 36`) to face `(3, 30)` for a Double Battle [Defeated].
  - From `(3, 30)`, walk `Up` 2 through `(3, 29)` onto the teleporter pad at **`(3, 28)`**, which warps to **Room 2 at `(1, 23)`** (note: `(7, 30)` and `(1, 33)` in Room 1 are return/later pads).
- **Room 2 (`(1, 23)` -> `(9, 18)` & `(7, 17)`):**
  - Contains a **Yellow Floor Switch at `(2, 21)`** and a 2x2 counter-clockwise conveyor loop at **`(4..5, 20..21)`**, with **Psychic Samantha `(4, 23)`** facing `Up` toward `(4, 22)` (`Xatu Lv. 36` [Defeated]) and **Psychic Blake** on the 2x2 block.
  - With Statue at `(4, 20)` and **Psychic Blake** at `(4, 21)` (`Girafarig Lv. 36` [Defeated]), `(5, 21)` and `(5, 20)` are uncovered. Walk `Right` 3 from `(2, 22)` to `(5, 22)`, `Up` 2 through `(5, 21)` to `(5, 20)`, `Right` 3 to `(8, 20)`, and `Up` 2 to `(8, 18)`.
  - From `(8, 18)`:
    - Walking `Right` 1 onto **`(9, 18)`** warps to **Room 3 at `(23, 20)`** (to press the Green Floor Switch at `(15, 34)`).
    - Walking `Left` 1 onto **`(7, 18)`** warps to **Room 5 (Blue Conveyor Room) at `(8, 12)`**.
- **Room 3 (`(23, 20)` -> Lower Room 3):**
  - Stepping `Down` 1 from `(23, 20)` onto the **Purple Floor Switch at `(23, 21)`** slides the upper 2x2 purple blocks (`(21..22, 22..23)` and `(24..25, 22..23)`) and the middle 2x2 purple block (`(22..23, 25..26)`) to State 1.
  - Stepping `Down` 1 to `(23, 22)` triggers **Hex Maniac Kathleen `(22, 22)`** (`Kadabra Lv. 36`) and **Psychic Nicholas `(24, 22)`** (`Wobbuffet Lv. 36`) in a Double Battle [Defeated].
  - From `(23, 22)`, step `Up` 1 to `(23, 21)` (State 2), `Down` 1 to `(23, 22)`, `Up` 1 to `(23, 21)` (State 3), and `Down` 3 onto the lower **Purple Floor Switch at `(23, 24)`** (State 0, which places Statues at `(23, 25..26)` blocking the Gentleman at `(22, 25)`).
  -From `(23, 24)`, walk `Right` 1 to `(24, 24)` and `Down` 1 to `(24, 25)` to battle **Psychic Macey `(25, 25)`** (`Natu Lv. 36` [Defeated]) 1v1, then continue `Down` 6 along `x = 24` to `(24, 31)`, diagonally `Down-Left` to `(21, 34)`, and `Left` 6 along `y = 34` to the **Green Floor Switch at `(15, 34)`**.
  - Press the **Green Floor Switch at `(15, 34)` twice** (`Left` onto `(15, 34)`, then `Right` to `(16, 34)` and `Left` onto `(15, 34)`) to open `(12, 34)` in Room 4 (`x = 11..13, y = 31..35`).
  - Backtrack along the corridor to `(24, 24)`, step `Left` 1 onto `(23, 24)`, and walk `Left` 3 onto the teleporter at **`(20, 24)`**, which returns to **Room 1 at `(1, 33)`** (note: `(7, 30)` in Room 1 is a white one-way arrival pad).
- **Room 4 (`(11, 35)` -> `(13, 31)`):**
  - Reached from Room 5's northern teleporter at **`(10, 3)`** (arriving at `(11, 35)`).
  - With `(12, 34)` cleared by pressing the Room 3 Green Switch at `(15, 34)` twice, walk `Right` 1 from `(11, 35)` to `(12, 35)`, `Up` 1 to `(12, 34)`, `Right` 1 to `(13, 34)`, and `Up` 3 along `x = 13` onto the teleporter at **`(13, 31)`**.
- **Room 5 (Blue & Red Conveyor Room, `(8, 12)` -> North):**
  - Reached from Room 2's teleporter at **`(7, 18)`**.
  - Contains a lower **Blue Floor Switch at `(8, 10)`**, two 2x2 Blue Conveyor loops at **`(6..7, 8..9)`** and **`(9..10, 8..9)`**, an upper **Blue Floor Switch at `(6, 7)`**, a **Red Floor Switch at `(8, 6)`**, and 2x2 Red Conveyor loops at **`(6..7, 5..6)`** and **`(10..11, 5..6)`**.
  - Pressing `(8, 10)` **3 times** (State 3) places the left Statue at `(6, 9)` and Psychic♂ at `(6, 8)` facing Right, opening `(8, 9)` -> `(7, 9)` -> `(7, 8)` -> `(7, 7)`.
  - Stepping onto the upper **Blue Floor Switch at `(6, 7)`** once sets Blue State 0 (clearing `(6, 8)`), allowing passage via `(7, 8)` -> `(7, 6)` onto the **Red Floor Switch at `(8, 6)`**.
  - Pressing `(8, 6)` **3 times** (via `(8, 5)`) sets Red State 3, moving both eastern Red Statues to `(11, 5..6)` and opening `(10, 6)` -> `(10, 5)` -> `(10, 4)` -> **`(10, 3)`**.
  - From `(8, 6)`, walk `Up` 2 to `(8, 4)` and `Left` 2 to `(6, 4)` to defeat **Psychic Hannah `(6, 3)`** (`Kirlia Lv. 36` [Defeated]), then walk via `(5, 4)` -> `(5, 6)` -> `(6, 6)` onto `(6, 7)` and press `(6, 7)` **3 times** to restore Blue State 3 (`(7, 8..9)` open).
  - From `(6, 7)`, walk `Right` 1 to `(7, 7)` to defeat **Hex Maniac Sylvia `(7, 6)`** (`Meditite Lv. 36` [Defeated]), then walk `Down` 2 to `(7, 9)`, `Right` 1 to `(8, 9)`, and `Down` 1 onto `(8, 10)` (restoring Blue State 0, which opens `(9..10, 9)`).
  - From `(8, 10)`, walk `Up` 1 to `(8, 9)`, `Right` 3 through `(9..10, 9)` to `(11, 9)`, `Up` 2 to `(11, 7)`, `Left` 1 to `(10, 7)`, and `Up` 4 through `(10, 6..4)` onto the teleporter at **`(10, 3)`**.
- **Tate & Liza's Room (`(21, 10)` -> `(23..24, 7)`):**
  - Reached from Room 4's northern teleporter at **`(13, 31)`** (arriving in the 1-tile alcove at `(21, 10)`).
  - Walk `Up` 1 from `(21, 10)` to `(21, 9)`, `Right` 2 along `y = 9` to `(23, 9)`, and `Up` 1 up the front platform steps onto `(23, 8)` to face **Gym Leaders Tate & Liza `(23..24, 7)`**.
  - **Gym Leaders Tate & Liza Team (Double Battle, 2 Hyper Potions):**
    1. **Claydol Lv. 41** (`Earthquake`, `AncientPower`, `Psychic`, `Light Screen`)
    2. **Xatu Lv. 41** (`Psychic`, `Calm Mind`, `Confuse Ray`, `Sunny Day`)
    3. **Lunatone Lv. 42 [Sitrus Berry]** (`Psychic`, `Hypnosis`, `Calm Mind`, `Light Screen`)
    4. **Solrock Lv. 42 [Sitrus Berry]** (`SolarBeam`, `Sunny Day`, `Psychic`, `Flamethrower`)
    - *[Defeated & Registered — **Mind Badge** and **TM04 (Calm Mind)** obtained]*
  - **Exit Route from `(23, 8)`:** Walk `Down` 1 to `(23, 9)`, `Left` 2 to `(21, 9)`, and `Up` 3 along `x = 21` onto the return teleporter at **`(21, 6)`** (warps to Room 1 `(7, 30)`), then walk `Down` 1 to `(7, 31)`, `Left` 1 to `(6, 31)`, and `Down` 5 along `x = 6` out `(6, 35)` to Mossdeep City `(38, 10)`.

## Mossdeep Space Center (Eastern Mossdeep City)
- **Path from Mossdeep Pokémon Center `(28, 17)` to Space Center Entrance `(64, 15)`:**
  - Walk `Right` 5 to `(33, 17)`, `Down` 2 to `(33, 19)`, `Right` 8 along `y = 19` to `(41, 19)`, and `Down` 3 along `x = 41` to **`(41, 22)`** (triggers the **Team Magma Space Center Procession Cutscene** [Completed]).
  - Continue `Down` 3 to `(41, 25)`, `Right` 6 to `(47, 25)`, `Down` 4 to `(47, 29)`, `Right` 10 along `y = 29` to `(57, 29)`, `Up` 6 up the stairs to `(57, 23)`, `Right` 7 to `(64, 23)`, and `Up` 8 up the double stairs along `x = 64` into the **Mossdeep Space Center** door at **`(64, 15)`** (exiting steps to `(64, 16)`).
- **Mossdeep Space Center 1F (`(7, 9)` -> `(13, 1)`):**
  - Round pink cushions (`(11, 3)`, etc.) are walkable floor tiles.
  - From `(7, 9)`, walk `Up` 5 to `(7, 4)`, `Right` 2 to `(9, 4)`, `Up` 1 to `(9, 3)`, and `Right` 4 across `(10..13, 3)` to `(13, 3)`.
  - **Team Magma Grunt #1 `(10, 2)`:** Watches `(10, 3)` — `Baltoy Lv. 32` [Defeated].
  - **Team Magma Grunt #2 `(13, 2)`:** Blocks the staircase to 2F at `(13, 1)`; talk to him (`Up, A` from `(13, 3)`) to battle (`Mightyena Lv. 26`, `Mightyena Lv. 28`, `Numel Lv. 30` [Defeated — moves to `(14, 2)`]), then walk `Up` 2 onto the staircase at **`(13, 1)`** to warp to 2F.
- **Mossdeep Space Center 2F (`(13, 2)` -> `(1, 8)`):**
  - **3-Grunt Gauntlet at `(13, 2)`:** Surrounded by three Team Magma Grunts at `(12, 2)`, `(14, 2)`, and `(13, 3)`. Speak to `(13, 3)` (`A`) and select `YES` (`A`) to fight all three Grunts back-to-back in 1v1 Single Battles:
    1. **Grunt #1 `(13, 3)`:** `Zubat Lv. 32` [Defeated].
    2. **Grunt #2 `(12, 2)`:** `Mightyena Lv. 32` [Defeated].
    3. **Grunt #3 `(14, 2)`:** `Baltoy Lv. 32` [Defeated — Grunt at `(13, 3)` steps `Down` to `(13, 4)`].
  - **Path from `(13, 2)` to Steven Stone `(1, 8)`:** Walk `Down` 1 to `(13, 3)`, `Right` 1 to `(14, 3)`, `Down` 2 along `x = 14` (to the right of the railing `x = 1..12, y = 4` and Grunt #3 at `(13, 4)`) to `(14, 5)`, `Left` 13 along `y = 5` to `(1, 5)`, and `Down` 2 to `(1, 7)`.
  - **Steven Stone & Multi Battle Trigger (`(1, 7)` -> `(1, 8)`):**
    - Speak to **Steven Stone** at `(1, 8)` from `(1, 7)` to trigger the cutscene where Steven steps `Right` to `(2, 8)`.
    - Step `Down` 1 onto **`(1, 8)`**, press `A` to select `YES` (`"Are you ready?"`), and select 3 Pokémon (`FIRST`, `SECOND`, `THIRD` -> cursor auto-jumps to `CONFIRM` -> press `A`) to begin the Multi Battle alongside **Steven Stone** (`Metang Lv. 42`, `Skarmory Lv. 43`, `Aggron Lv. 44`) against **Magma Leader Maxie** (`Mightyena Lv. 42`, `Camerupt Lv. 44`, `Crobat Lv. 43`) and **Magma Admin Tabitha** (`Camerupt Lv. 36`, `Mightyena Lv. 38`, `Golbat Lv. 40`) [Defeated / Completed — Team Magma departed; Steven Stone moved to his house at `(19, 10)`].
    - **Multi Battle Note:** Each trainer's send-out line (`"MAGMA LEADER MAXIE sent out..."`, `"MAGMA ADMIN TABITHA sent out..."`, `"PKMN TRAINER STEVEN sent out..."`) has a manual `[red arrow]` prompt (`B` to advance), and each KO produces two EXP text boxes (`ATRITON gained...` and `METANG gained...`).

## Route 127, Route 128 & Seafloor Cavern Approach
- **Mossdeep City `(28, 17)` to Route 127 `(25, 0)`:**
  - From the Mossdeep Pokémon Center `(28, 17)`, walk `Left` 3 to `(25, 17)`, `Down` 13 down the stairs and shallow water to `(25, 30)`, face `Down` to use **Surf** onto `(25, 31)`, and surf `Down` 9 across `(25, 39)` into **Route 127** at `(25, 0)`.
- **Route 127 (`(25, 0)` -> `(25, 79)`):**
  - Surf straight `Down` 80 along `x = 25` (`y = 0..79`, completely open water) across `(25, 79)` into **Route 128** at `(25, 0)`.
- **Route 128 (`(25, 0)` -> Dive Trench `(52, 18)`):**
  - Surf `Down` 4 from `(25, 0)` onto the shallow bank at `(25, 4)`, walk `Right` 2 to `(27, 4)`, and use **Surf** `Right` onto `(28, 4)`.
  - Surf `Right` 4 to `(32, 4)` and `Down` 10 onto the shallow sandbar at `(32, 14)`, walk `Right` 2 to `(34, 14)` and `Up` 1 to `(34, 13)`, face `Up` to use **Surf** onto `(34, 12)`, then surf `Right` 20 along `y = 12` to `(54, 12)`, `Down` 6 to `(54, 18)`, and `Left` 2 onto the deep underwater trench at **`(52, 18)`**.
- **`Underwater_Route128` (`(52, 18)` -> `(38, 27)`):**
  - Use **Dive** (`A, sleep 1500, A, sleep 1000, B, sleep 4000`) at `(52, 18)` on Route 128 to descend into **`Underwater_Route128`** at `(52, 18)`.
  - Follow the underwater canyon channel: `Left` 1 to `(51, 18)`, `Down` 7 to `(51, 25)`, `Left` 4 to `(47, 25)`, `Down` 2 to `(47, 27)`, `Left` 2 to `(45, 27)`, `Down` 2 to `(45, 29)`, `Left` 5 along `y = 29` to `(40, 29)`, and `Left` 2, `Up` 3 into the **Seafloor Cavern underwater entrance at `(38, 26)`**.
- **`Underwater_SeafloorCavern` (`(6, 7)`) & `SeafloorCavern_Entrance` (`(10, 17)` -> `(10, 1)`):**
  - Inside `Underwater_SeafloorCavern` at `(6, 7)`, press **`B`** to surface (`B, sleep 1500, A, sleep 1000, B, sleep 4000`), arriving in `SeafloorCavern_Entrance` at `(10, 17)`.
  - Surf `Up` 7 along `x = 10` onto the shallow bank at `(10, 10)`, then walk `Up` 9 along `x = 10` into the northern doorway at **`(10, 1)`** (warps to `SeafloorCavern_Room1` at `(5, 18)`).
- **`SeafloorCavern_Room1` (`(5, 18)` -> `(6, 1)`):**
  - From `(5, 18)`, walk `Left` 1 to `(4, 18)` and `Up` 8 along `x = 4` to `(4, 10)`.
  - Face `Right` at `(4, 10)` and use **Rock Smash** to break the rock at `(5, 10)`.
  - Walk `Down` 2 to `(4, 12)`, `Right` 1 to `(5, 12)`, face `Up`, activate **Strength**, and push the boulder at `(5, 11)` `Up` 1 into `(5, 10)`.
  - Walk `Up` 1 to `(5, 11)`, `Right` 6 along `y = 11` to `(11, 11)`, `Right` 1 and `Up` 1 onto `(12, 10)`, `Up` 3 along `x = 12` to `(12, 7)`, `Left` 1 to `(11, 7)`, `Up` 1 to `(11, 6)`, `Left` 1 to `(10, 6)`, `Up` 1 to `(10, 5)`, `Left` 4 along `y = 5` (passing north of the rotating Team Aqua Grunt at `(8, 6)`) to `(6, 5)`, and `Up` 4 into the northern doorway at **`(6, 1)`** (warps to `SeafloorCavern_Room2` at `(10, 7)`).
- **`SeafloorCavern_Room2` (`(10, 7)` -> `(11, 1)`):**
  - Do NOT push the central boulder at `(7, 4)` `Up` into `(7, 3)` (doing so blocks `(7, 3)`).
  - Instead, from `(10, 7)`, walk `Left` 1 to `(9, 7)`, face `Left` to smash the **Rock Smash rock at `(8, 7)`**, walk `Left` 5 across `(8..4, 7)` to `(4, 7)`, and `Up` 1 to `(4, 6)`.
  - At `(4, 6)`, activate **Strength** facing `Up` and push the western boulder at `(4, 5)` `Up` 3 times (`(4, 5)` -> `(4, 4)` -> `(4, 3)` -> `(4, 2)`).
  - Walk `Up` 1 to `(4, 3)`, `Right` 4 across `(5..8, 3)` (passing above the untouched boulder at `(7, 4)`) to `(8, 3)`, smash the **Rock Smash rock at `(9, 3)`**, step `Right` onto `(9, 3)`, push the boulder at `(10, 3)` `Right` 2 times (`(10, 3)` -> `(11, 3)` -> `(12, 3)`), and walk from `(10, 3)` via `Right` 1, `Up` 2 into the **Top-Right Doorway at `(11, 1)`** (warps to the southwest shore of `SeafloorCavern_Room6` at `(3, 23)`). Note: the Top-Left Doorway at `(6, 1)` warps to the south-central entrance of `SeafloorCavern_Room6` `(11, 21)`, which is blocked by downward currents.
- **`SeafloorCavern_Room6` (Water Current Room, `(3, 23)` -> `(5, 1)`):**
  - From `(3, 23)`, walk `Up` 2 to `(3, 21)` and `Right` 5 to `(8, 21)`, face `Right` to use **Surf** onto `(9, 21)`, surf `Right` 1 and `Down` 2 to `(10, 23)`, and surf `Right` 6 along `y = 23` onto the current at **`(16, 23)`** (slides `Right` to `(18, 23)` and `Up` to `(18, 12)`).
  - From `(18, 12)`, surf `Right` 1 onto the eastern calm water lane `(19, 12)` and `Up` 8 along `x = 19` onto the current at **`(19, 4)`** (slides via `(15, 4)` -> `(15, 7)` -> `(4, 7)` onto the calm water tile at **`(4, 10)`**).
  - From `(4, 10)`, surf `Left` 1 onto the western calm water lane `(3, 10)` and `Up` 7 along `x = 3` onto the northwest shore at **`(3, 3)`**, then walk `Right` 2 and `Up` 2 into the northern doorway at **`(5, 1)`** (warps to `SeafloorCavern_Room7`).
- **`SeafloorCavern_Room4` (Checkerboard Boulder & Shelly Room, `(9, 13)` -> `(8, 1)`):**
  - Taking the left corridor (`x = 6..7`) walks into the line of sight of the Team Aqua Grunt at `(5, 5)` and Team Aqua Admin Shelly at `(9, 5)` along `y = 5`.
  - To bypass them via the right-side checkerboard boulder puzzle (`x = 11..13, y = 7..11`), use **5 boulder pushes**:
    1. Walk `Right` 4 and `Up` 2 from `(9, 13)` to `(13, 11)`, face `Left`, activate **Strength**, and push **`(12, 11)` `Left` 1 into `(11, 11)`**.
    2. Walk `Left` 1 and `Up` 1 to `(12, 10)` and push **`(12, 9)` `Up` 1 into `(12, 8)`**.
    3. Walk `Up` 1 and `Left` 1 to `(11, 9)` and push **`(11, 8)` `Up` 3 times** along `x = 11` (`(11, 8)` -> `(11, 7)` -> `(11, 6)` -> `(11, 4)`).
  - From `(11, 6)`, walk `Up` 1 to `(11, 5)`, `Left` 1 to `(10, 5)` (behind Shelly at `(9, 5)`), `Up` 2 to `(10, 3)`, `Left` 2 to `(8, 3)`, and `Up` 2 into the northern doorway at **`(8, 1)`**.
- **`SeafloorCavern_Room8` (Final 12-Boulder Symmetrical Puzzle Room, `(5, 12)` -> `(5, 1)`):**
  - From `(5, 12)`, walk `Left` 2 to `(3, 12)`, `Up` 4 around the ledge `(4..6, 10)` to `(3, 8)`, `Right` 2 to `(5, 8)`, face `Up`, and activate **Strength**.
  - Execute the **10-push symmetrical solution** (remembering each boulder push ends a `press_buttons` call):
    1. **Push 1:** At `(5, 8)`, press **`Up`** -> pushes `(5, 7)` `Up` to `(5, 6)`.
    2. **Push 2:** Press `Up, Left` -> steps to `(5, 7)` and pushes `(4, 7)` `Left` to `(3, 7)`.
    3. **Push 3:** Press `Right` at `(5, 7)` -> pushes `(6, 7)` `Right` to `(7, 7)`.
    4. **Push 4:** Press `Left, Up, Right` -> walks via `(4, 7)` to `(4, 6)` and pushes `(5, 6)` `Right` to `(6, 6)`.
    5. **Push 5:** Press `Right, Up` -> steps to `(5, 6)` and pushes `(5, 5)` `Up` to `(5, 4)`.
    6. **Push 6:** Press `Up, Left` -> steps to `(5, 5)` and pushes `(4, 5)` `Left` to `(3, 5)`.
    7. **Push 7:** Press `Right` at `(5, 5)` -> pushes `(6, 5)` `Right` to `(7, 5)`.
    8. **Push 8:** Press `Right, Up` -> steps to `(6, 5)` and pushes `(6, 4)` `Up` to `(6, 3)`.
    9. **Push 9:** Press `Left, Left, Up` -> walks across `(5, 5)` to `(4, 5)` and pushes `(4, 4)` `Up` to `(4, 3)`.
    10. **Push 10:** Press `Up, Right` -> steps to `(4, 4)` and pushes `(5, 4)` `Right` to `(6, 4)`, opening the center aisle `(5, 4)` -> `(5, 2)` into **`SeafloorCavern_Room9` (Archie & Kyogre)**.
- **`SeafloorCavern_Room9` (Kyogre's Chamber, `(12, 8)` -> `(17, 42)`):**
  - **TM26 (Earthquake):** Item Ball on the upper northern ledge at **`(14, 5)`** (from `(12, 8)`, walk `Up` 3 to `(12, 5)`, `Right` 1 to `(13, 5)`, and press `A` facing `Right`).
  - **Path from `(12, 8)` to Kyogre's Pool `(17, 42)`:**
    - Walk straight `Down` 19 along `x = 12` from `(12, 8)` to `(12, 27)` (note: `(13..17, 26..28)` is a dead-end contour basin to the east).
    - From `(12, 27)`, walk `Left` 4 along `y = 27` (between the upper rock wall at `y = 25..26` and the lower contour ridge at `y = 28..29`) to `(8, 27)`.
    - Follow the western corridor south: `Down` 4 to `(8, 31)`, `Left` 1 to `(7, 31)`, `Down` 2 to `(7, 33)`, `Left` 1 to `(6, 33)`, `Down` 5 to `(6, 38)`, `Right` 1 to `(7, 38)`, and `Down` 2 to `(7, 40)`.
    - Follow the southern shoreline east: `Right` 5 to `(12, 40)`, `Down` 1 to `(12, 41)`, `Right` 1 to `(13, 41)`, `Down` 1 to `(13, 42)`, and `Right` 4 along `y = 42` to **`(17, 42)`** (stepping onto `(17, 42)` and pressing `Up` or any direction triggers **Team Aqua Leader Archie** — `Mightyena Lv. 41`, `Crobat Lv. 41`, `Sharpedo Lv. 43` [Defeated — awakens Kyogre and warps to Route 128]).
## Route 128 -> Route 127 -> Route 126 & Sootopolis City Approach
- **Route 128 Atoll `(38, 22)` to Route 127 `(27, 79)`:**
  - From `(38, 22)`, walk `Up` 1 to `(38, 21)`, use **Surf** `Up` onto `(38, 20)`, surf `Up` 6 onto the northern atoll rim at `(38, 14)`, walk `Up` 1 to `(38, 13)`, and use **Surf** `Up` onto `(38, 12)`.
  - From `(38, 12)`, surf `Up` 2 to `(38, 10)`, `Left` 6 along `y = 10` to `(32, 10)`, `Up` 6 along `x = 32` to `(32, 4)`, `Left` 5 onto the sandbar at `(27, 4)`, use **Surf** `Up` onto `(27, 3)`, and surf `Up` 4 across `(27, 0)` into **Route 127 at `(27, 79)`**.
- **Route 127 `(27, 79)` to Route 126 `(79, 48)`:**
  - From `(27, 79)`, surf `Up` 6 to `(27, 73)`, `Left` 3 to `(24, 73)`, `Up` 7 to `(24, 66)`, `Left` 1 to `(23, 66)`, `Up` 2 to `(23, 64)`, `Left` 9 along `y = 64` to `(14, 64)`, `Up` 2 to `(14, 62)`, `Left` 5 to `(9, 62)`, `Up` 2 to `(9, 60)`, `Left` 1 to `(8, 60)`, `Up` 6 to `(8, 54)`, `Left` 1 to `(7, 54)`, `Up` 6 to `(7, 48)`, and `Left` 8 across `(0, 48)` into **Route 126 at `(79, 48)`**.
- **Route 126 `(79, 48)` to Sootopolis Southern Dive Trench `(51, 68)`:**
  - From `(79, 48)`, surf `Left` 13 along `y = 48` to `(66, 48)`, `Down` 20 along `x = 66` (east of Sootopolis City's outer crater wall) to `(66, 68)`, and `Left` 15 along `y = 68` onto the deep underwater trench (`MB_DIVEABLE`) at **`(51, 68)`** (`x = 51..55, y = 68`).
  - **Swimmer♂ Barry `(51, 67)`:** `Gyarados Lv. 34` [Defeated — money `$13,388`]. Surf `Left` 3 from `(51, 68)` to **`(48, 68)`** (unobstructed trench tile) before pressing `A` to use **Dive**.