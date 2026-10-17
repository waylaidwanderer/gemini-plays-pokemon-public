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
- **`Underwater_Route126` (`(48, 68)` -> `(45, 65)`) & `Underwater_SootopolisCity`:**
  - After using **Dive** at `(48, 68)` on Route 126, swim `Left` 3 along `y = 68` to `(45, 68)` and `Up` 3 along `x = 45` (`(45, 68)` -> `(45, 66)` -> **`(45, 65)`**, completely bare floor with zero seaweed; note that the underwater cave arch spans `x = 44..45, y = 65`, and **only the right tile `(45, 65)`** is the active warp tile) into **`Underwater_SootopolisCity` at `(9, 8)`**.
  - Inside `Underwater_SootopolisCity` at `(9, 8)`, press **`B`** (`B, sleep 1500, A, sleep 1000, B, sleep 4500`) to surface into **Sootopolis City at `(29, 53)`**.
## Sootopolis City (`(29, 53)` -> Pokémon Center `(43, 31)` & Outer Rim)
- **Surfacing Point (from `Underwater_SootopolisCity` `(9, 8)`):** `(29, 53)`.
- **Path from `(29, 53)` to Sootopolis City Pokémon Center `(43, 31)`:**
  - Note: The western shore landing at `(16, 45)` (`x = 7..17, y = 38..47`) is an enclosed grass pocket walled off by cliffs; to access Sootopolis City's outer rim staircases, surf around Sootopolis Gym to the **Eastern Shore Landing at `(39, 37)`**.
  - From `(29, 53)`, surf `Left` 13 to `(16, 53)` (or surf `Up`/`Right` around Sootopolis Gym): from `(24, 38)`, surf `Up` 12 along `x = 24` to `(24, 26)`, `Right` 14 along `y = 26` (north of Sootopolis Gym) to `(38, 26)`, `Down` 11 along `x = 38` to `(38, 37)`, and `Right` 2 onto the **Eastern Shore Landing at `(40, 37)`**.
  - From `(40, 37)`, walk `Down` 1 to `(40, 38)` (around the signpost at `(41, 37)`), `Right` 3 to `(43, 38)`, and `Up` 7 along `x = 43` into the **Sootopolis City Pokémon Center at `(43, 31)`** (exiting steps to `(43, 32)`).
- **Eastern Rim Staircase & Shore (`(43, 32)` -> `(43, 38)`):**
  - Note: Exiting the Sootopolis City Pokémon Center `(43, 31)` to `(43, 32)` during heavy rain / intense sun requires `sleep 3000` before moving, and two NPCs at `(46, 32)` and `(47, 33)` diagonally block the terrace directly east of the Pokémon Center during the Groudon vs. Kyogre crisis.
  - Below the Pokémon Center staircase (`(43..44, 34..37)`), green grass extends south (`y = 38..42`) and east past `(45, 41)`.
- **Steven Stone Escort to Cave of Origin (`(20, 36)` -> `(31, 17)`):**
  - During the Groudon vs. Kyogre crisis, all other staircases in Sootopolis City are blocked by NPCs (`(13, 48)` on the southwest shore and `(46, 32)`/`(47, 33)` on the eastern terrace).
  - To reach **Steven Stone at `(20, 36)`**: surf to **`(23, 37)`** (west of Sootopolis Gym), press `Left` to step ashore onto **`(22, 37)`**, walk `Left` 2 to **`(20, 37)`**, face `Up`, and press **`A`** to speak with **Steven Stone at `(20, 36)`**, who automatically escorts the player up the staircase at `(19..20, 35)` to the **Cave of Origin entrance at `(31, 17)`**.
- **Cave of Origin (`CaveOfOrigin_Entrance` `(9, 20)` -> `CaveOfOrigin_1F` `(11, 17)`):**
  - Finishing Steven Stone's dialogue outside the Cave of Origin automatically warps the player into `CaveOfOrigin_Entrance` at **`(9, 20)`**.
  - Inside `CaveOfOrigin_Entrance`, walk straight `Up` 15 along `x = 9` from `(9, 20)` to **`(9, 5)`** to warp into **`CaveOfOrigin_1F` at `(11, 17)`**.
  - Inside `CaveOfOrigin_1F` (`(11, 17)` -> `(13, 5)`): walk `Left` 4 to `(7, 17)`, `Up` 8 to `(7, 9)`, `Right` 1 to `(8, 9)`, `Up` 1 to `(8, 8)`, `Right` 1 to `(9, 8)`, `Up` 1 to `(9, 7)`, `Right` 4 to `(13, 7)`, `Up` 1 to `(13, 6)`, `Right` 3 to `(16, 6)`, `Up` 1 to `(16, 5)`, and `Left` 3 onto the ladder at **`(13, 5)`** (warps to `CaveOfOrigin_B1F` at **`(9, 3)`**).
  - Inside `CaveOfOrigin_B1F` (`(9, 3)` -> Wallace `(9, 13)`): walk `Right` 2 to `(11, 3)`, `Down` 1 to `(11, 4)`, `Right` 2 to `(13, 4)`, `Down` 1 to `(13, 5)`, `Right` 1 to `(14, 5)`, `Down` 7 to `(14, 12)`, `Left` 1 to `(13, 12)`, `Down` 1 to `(13, 13)`, `Left` 1 to `(12, 13)`, `Down` 1 to `(12, 14)`, and `Left` 3 to **`(9, 14)`** facing **Wallace at `(9, 13)`**. Speak to Wallace (`Up, A`) and select **`SKY PILLAR`** (`Down, Down, A`) to unlock the Sky Pillar on Route 131.
- **Exiting Cave of Origin Courtyard (`(31, 17)` -> `(25, 13)` -> Western Shore `(22, 37)`):**
  - The Cave of Origin courtyard (`x = 24..38, y = 17..23`) is bounded by cliffs on the west (`x = 23`) and south (`y = 24`); its only exit is climbing the staircases at `(25..26, 14..19)` to **`(25, 13)`** and walking **`Right` along `y = 13`** behind the Cave of Origin: `(25, 13)` -> `(35, 13)` -> `(35, 12)` -> `(34, 12)` -> `(34, 9)` -> `(29, 9)` -> `(29, 6)` -> `(22, 6)` -> `(22, 7)` -> `(19, 7)` -> `(19, 5)` -> `(15, 5)` -> `(15, 15)` -> `(16, 15)` -> `(16, 22)` -> `(17, 22)` -> `(17, 19)` -> `(20, 19)` -> `(20, 23)` -> `(21, 23)` -> `(21, 34)` -> `(20, 34)` -> `(20, 37)` -> **`(22, 37)`**.
- **Sootopolis City Underwater Exit (`(29, 53)` -> Route 126 `(48, 68)`):**
  - From the western shore `(22, 37)`, use **Surf** `Right` onto `(23, 37)`, surf via `(24, 37)` -> `(24, 53)` -> `(29, 53)`, and use **Dive** (`A`) to descend into `Underwater_SootopolisCity` at `(9, 6)`.
  - Swim `Down` 3 from `(9, 6)` across the exit warp at **`(9, 8)`** into `Underwater_Route126` at `(45, 66)`, then swim `Down` 2 to `(45, 68)`, `Right` 3 to **`(48, 68)`**, and press **`B`** to surface onto **Route 126 at `(48, 68)`**.
- **Route 127 Trainer & Route 128 Southbound Route to Route 129:**
  - **Triathlete♂ Donny `(18, 67)` (Route 127):** Watches `(18, 64)` — `Wingull Lv. 26`, `Staryu Lv. 34` [Defeated — money `$21,787`].
  - **Route 128 `(27, 4)` to Route 129 `(59, 0)`:** From the sandbar at `(27, 4)`, wait `1000ms` for the dismount hop to finish, use **Surf** `Right` onto `(28, 4)`, surf via `(32, 4)` -> `(32, 10)` -> `(38, 10)` -> `(38, 12)` -> `(54, 12)` -> `Down` onto the sandbar at **`(54, 26)`**, use **Surf** `Right` onto `(55, 26)` -> `(56, 26)`, and surf south via `(56..59, 26..39)` into **Route 129 at `(59, 0)`**.
## Route 129 (`(53, 0)` -> `(0, 18)` -> Route 130)
- **North Entrance (from Route 128 `(59, 39)`):** `(53, 0)` (`x_route129 = x_route128 - 6`).
- **Route 129 Trainers & Westbound Path:**
  - **Swimmer♂ Reed `(35, 9)`:** Watches `(35, 8)` — `Spheal Lv. 33`, `Sharpedo Lv. 33` [Defeated — money `$22,051`]. Bypass or continue via `(36, 8)` -> `(36, 13)` -> west along `y = 13..16` to `(8, 16)`.
  - **Triathlete♀ Allison `(10, 16)`:** Watches `(8, 16)` — `Wingull Lv. 27`, `Staryu Lv. 33` [Defeated — money `$23,371`]. From `(8, 16)`, surf via `(8, 14)` -> `(7, 14)` -> `(7, 15)` -> `(5, 15)` -> `(5, 19)` -> `(0, 19)` into **Route 130 at `(79, 19)`**.
## Route 130 & Route 131 (`(79, 19)` -> Sky Pillar)
- **East Entrance of Route 130 (from Route 129 `(0, 19)`):** `(79, 19)`.
- **Swimmer♂ Rodney `(70, 15)` (Route 130):** Watches `(70, 19)` — `Gyarados Lv. 34` [Defeated — money `$23,643`].
- **Swimmer♀ Katie `(7, 24)` (Route 130):** Watches `(7, 23)` — `Goldeen Lv. 33`, `Spheal Lv. 33` [Defeated — money `$23,907`]. Surf `Left` 8 from `(7, 23)` across `(0, 23)` into **Route 131 at `(59, 23)`**.
- **Route 131 (`(59, 23)` -> Sky Pillar Entrance at `(36, 6)`):**
  - **Swimmer♂ Kevin `(52, 21)`:** Watches `(52, 20)` — `Spheal Lv. 34` [Defeated — money `$24,179`].
  - **Verified Sky Pillar Route (`(59, 23)` -> `(36, 6)`):**
    - From the east entrance `(59, 23)`, surf `Left` 7 to `(52, 20)` (defeat Swimmer♂ Kevin at `(52, 21)`), `Left` 2 to `(50, 20)`, `Up` 4 to `(50, 16)`, `Left` 3 to `(47, 16)`, `Up` 1 to `(47, 15)`, `Left` 7 to `(40, 15)`, `Down` 3 to `(40, 18)`, `Left` 7 to `(33, 18)`, `Down` 3 to `(33, 21)`, `Left` 3 to `(30, 21)`, and `Up` 3 to **`(30, 18)`**.
    - From **`(30, 18)`**, surf `Left` 3 around the pointed rock `(29..30, 16..17)` to **`(27, 18)`**, `Up` 4 along `x = 27` to **`(27, 14)`**, `Right` 9 straight along `y = 14` to **`(36, 14)`** (clamped by the pointed rock at `(37..38, 14..15)`), and `Up` 6 along `x = 36` onto the sandy beach at **`(36, 8)`**, then walk `Up` 2 into the **Sky Pillar Entrance Cave at `(36, 6)`**.
  - **`SkyPillar_Entrance` (`(6, 16)` -> `(14, 5)`):** From `(6, 16)`, walk `Up` 12 along `x = 6` to `(6, 4)`, `Right` 8 along `y = 4` to `(14, 4)`, and `Down` 1 onto the exit warp mat at **`(14, 5)`** (warps to `SkyPillar_Outside`).
  - **`SkyPillar_Outside` (`(17, 14)` -> `(14, 5)`):** Emerging from `SkyPillar_Entrance` at `(17, 14)` automatically triggers **Wallace** to walk down, unlock the Sky Pillar tower door, and escort the player to **`(14, 7)`** directly in front of the **Sky Pillar 1F doorway at `(14, 5)`**. After Wallace departs, walk `Up` 2 from `(14, 7)` into `(14, 5)` (warps to `SkyPillar_1F` at `(7, 13)`).
## Sky Pillar (`SkyPillar_1F` -> `SkyPillar_Top`)
- **Note:** Wild Pokémon (`Golbat`, `Sableye`, `Claydol`, `Banette`, `Altaria` Lv. 34–38) appear on interior floors `1F–5F`.
- **`SkyPillar_1F` (`(6, 13)` -> `(10, 1)`):**
  - Central pit spans `x = 4..9, y = 4..10`.
  - Walk `Right` 4 from `(6, 13)` to `(10, 13)` and `Up` 12 along `x = 10` into the staircase at **`(10, 1)`** (warps to `SkyPillar_2F` at `(10, 2)`).
- **`SkyPillar_2F` (`(10, 2)` -> `(3, 1)`):**
  - Walk `Left` 7 along `y = 2` from `(10, 2)` to `(3, 2)` and `Up` 1 into the staircase at **`(3, 1)`** (warps to `SkyPillar_3F` at `(3, 2)`).
- **`SkyPillar_3F` (`(3, 2)` -> `(11, 1)` & Center Alcove `(7, 1)`):**
  - The center-north staircase at `(7, 1)` (`x = 5..9, y = 2..4`) is walled off on 3F by rubble rocks (`(4, 2), (5, 3), (5, 4)` on the left and `(8, 4), (9, 3), (10, 2)` on the right) and the central pit (`x = 4..9, y = 5..10`).
  - First pass on 3F: walk `Down` 9 along `x = 3` from `(3, 2)` to `(3, 11)`, `Right` 8 along `y = 11` to `(11, 11)`, and `Up` 10 along `x = 11` into the right-side staircase at **`(11, 1)`** (warps to `SkyPillar_4F` at `(11, 2)`).
- **`SkyPillar_4F` (`(11, 2)` -> Cracked Floor `(6, 4)` -> `3F (7, 1)` -> `4F (3, 1)`):**
  - On 4F, the top-left staircase to 5F at `(3, 1)` is blocked from `(11, 2)` by a rubble rock at `(8, 2)` and a wall of rubble rocks across `(4..9, 3)` and `(10, 4)`.
  - From `(11, 2)`, walk `Down` 9 along `x = 11` to `(11, 11)`, `Left` 8 along `y = 11` to `(3, 11)`, `Up` 7 along `x = 3` to `(3, 4)`, and `Right` 3 along `y = 4` onto the **cracked floor tile at `(6, 4)`** (stepping onto `(6, 4)` and pressing `Right` toward `(7, 4)` collapses the floor and drops the player into the enclosed northern alcove of **`SkyPillar_3F` at `(6, 4)`**).
  - From `SkyPillar_3F` `(6, 4)`, walk `Right` 1 to `(7, 4)` and `Up` 3 into the center-north staircase at **`(7, 1)`**, which warps back up to **`SkyPillar_4F` at `(7, 2)`** (to the left of the rubble rock at `(8, 2)`).
  - From `SkyPillar_4F` `(7, 2)`, walk `Left` 4 along `y = 2` to `(3, 2)` and `Up` 1 into the staircase at **`(3, 1)`** (warps to `SkyPillar_5F` at `(3, 2)`).
- **`SkyPillar_5F` (`(3, 2)` -> `(10, 1)`):**
  - On 5F, the central pit is wider and deeper (`x = 3..10, y = 4..11`), and rubble rocks at `(9, 2)` and `(8, 3)` block the direct northern path to `(10, 1)`.
  - From `(3, 2)`, walk `Left` 1 to `(2, 2)`, `Down` 10 along `x = 2` to `(2, 12)`, `Right` 9 along `y = 12` to `(11, 12)`, `Up` 10 along `x = 11` to `(11, 2)`, `Left` 1 to `(10, 2)`, and `Up` 1 into the staircase at **`(10, 1)`** (warps to `SkyPillar_Top`).
- **`SkyPillar_Top` (`(16, 15)` -> `(14, 9)`):**
  - No wild encounters on the summit.
  - From `(16, 15)`, walk `Left` 4 to `(12, 15)`, `Up` 4 up the stairs to `(12, 11)`, `Right` 2 to `(14, 11)`, and `Up` 2 along `x = 14` to **`(14, 9)`** (stepping onto `(14, 9)` triggers the **Rayquaza Awakening Cutscene** [Completed]).
## Sootopolis City Post-Rayquaza Resolution & Sootopolis Gym
- **Rayquaza Cutscene Trigger:** Surfacing into Sootopolis City at `(29, 53)` after awakening Rayquaza at `SkyPillar_Top (14, 9)` automatically plays the Rayquaza vs. Groudon & Kyogre cutscene (`~16s` total) and returns overworld control surfing at `(29, 53)` [Completed].
- **Sootopolis Gym Island (`(29, 53)` -> `(29, 36)` -> `(31, 32)`):**
  - From `(29, 53)`, surf straight `Up` 16 along `x = 29` to `(29, 37)` and press `Up` 1 to step ashore onto the Sootopolis Gym island at **`(29, 36)`**.
  - On the island (`x = 27..35, y = 33..36`): **Steven Stone** is at `(29, 33)`, **Wallace** is at `(31, 33)` in front of the Gym door `(31, 32)`, the Gym sign is at `(33, 34)`, **Maxie** is at `(33, 35)`, and **Archie** is at `(34, 35)`. Speak to both Maxie `(33, 35)` and Archie `(34, 35)` so they depart, then speak to Wallace `(31, 33)` to receive **HM07 (Waterfall)** and unlock Sootopolis Gym.
## Sootopolis City Gym (`(31, 32)` -> `(8, 25)` -> Gym Leader Juan `(8, 2)`)
- **Mechanics:** Each of the 3 ice-floor puzzles on 1F must be traversed in a single Hamiltonian path visiting every ice tile exactly once and ending at `(8, y_top)` below the northern staircase, which causes the staircase wall to crumble open (`~1500ms` animation, aborts the current `press_buttons` call on the final step). Stepping onto a cracked ice tile a second time drops the player to B1F.
- **Entrance to Puzzle 1 (`(8, 25)` -> `(8, 19)`):** Walk `Up` 6 along `x = 8` from `(8, 25)` onto the bottom-center tile of Puzzle 1 at **`(8, 19)`**.
- **Puzzle 1 (`3x3`, `x = 7..9, y = 17..19`, rocks at `(7, 17)` & `(9, 19)`, 7 ice tiles):**
  - From `(8, 19)`: `["Left", "Up", "Right", "Right", "Up", "Left"]` -> ends at **`(8, 17)`**.
  - Wait `1500ms`, then step `["Up", "Up"]` onto `(8, 15)` below Puzzle 2.
- **Puzzle 2 (`7x3`, `x = 5..11, y = 12..14`, rocks at `(6, 13)` & `(10, 13)`, 19 ice tiles):**
  - From `(8, 15)`: `["Up", "Left", "Left", "Left", "Up", "Up", "Right", "Right", "Down", "Right", "Right", "Down", "Right", "Right", "Up", "Up", "Left", "Left", "Left"]` -> ends at **`(8, 12)`**.
  - Wait `1500ms`, then step `["Up", "Up"]` onto `(8, 10)` below Puzzle 3.
- **Puzzle 3 (`11x4`, `x = 3..13, y = 6..9`, rocks at `(4, 8), (5, 6), (7, 8), (9, 7), (11, 9), (12, 7)`, 38 ice tiles):**
  - From `(8, 10)`: `["Up", "Left", "Left", "Up", "Left", "Down", "Left", "Left", "Up", "Up", "Up", "Right", "Down", "Right", "Right", "Up", "Right", "Down", "Right", "Down", "Right", "Down", "Right", "Up", "Up", "Right", "Down", "Right", "Down", "Right", "Up", "Up", "Up", "Left", "Left", "Left", "Left", "Left"]` -> ends at **`(8, 6)`**.
  - Wait `1500ms`, then step `["Up", "Up", "Up"]` to `(8, 3)` facing **Gym Leader Juan at `(8, 2)`**.
  - **Gym Leader Juan `(8, 2)` Team (Single Battle, 2 Hyper Potions):**
    1. **Luvdisc Lv. 41** (`Water Pulse`, `Attract`, `Sweet Kiss`, `Flail`)
    2. **Whiscash Lv. 41** (`Water Pulse`, `Earthquake`, `Rain Dance`, `Amnesia`)
    3. **Sealeo Lv. 43** (`Aurora Beam`, `Water Pulse`, `Body Slam`, `Encore`)
    4. **Crawdaunt Lv. 43** (`Water Pulse`, `Crabhammer`, `Taunt`, `Swords Dance`)
    5. **Kingdra Lv. 46 [Chesto Berry]** (`Water Pulse`, `Ice Beam`, `Double Team`, `Rest`)
    - *[Defeated & Registered — **Rain Badge** and **TM03 (Water Pulse)** obtained]*
  - **Exit Route from `(8, 3)` via `SootopolisCity_Gym_B1F`:** Step `Down` 3 from `(8, 3)` onto the cracked ice at `(8, 6)` to drop to `SootopolisCity_Gym_B1F (8, 6)`, walk straight `Down` 16 along `x = 8` to `(8, 22)`, and `Right` 3 onto the ladder at **`(11, 22)`** (warps to 1F `(11, 22)`), then walk `Left` 3 to `(8, 22)` and `Down` 4 out `(8, 25)` to Sootopolis City `(31, 33)`.
## Route 128 East & Ever Grande City Approach
- **Route 128 `(25, 0)` to Ever Grande City `(1, 68)`:**
  - From Route 127 `(25, 79)` -> Route 128 `(25, 0)`, surf `Down` 4 onto the sandbar at `(25, 4)`, walk `Right` 2 to `(27, 4)`, and use **Surf** `Right` onto `(28, 4)`.
  - Surf `Right` 4 to `(32, 4)`, `Down` 6 to `(32, 10)`, `Right` 6 to `(38, 10)`, `Down` 2 to `(38, 12)`, and `Right` 33 along `y = 12` to `(71, 12)`.
  - From `(71, 12)`, surf `Down` 10 along `x = 71` (west of the Ever Grande cliff) to `(71, 22)`, and `Right` 30 along `y = 22` to `(101, 22)`.
  - **Swimmer♂ Harrison `(101, 23)`:** Watches `(101, 22)` — `Tentacruel Lv. 35` [Defeated — money `$29,059`].
  - From `(101, 22)`, surf `Right` 1 to `(102, 22)`, `Down` 4 along `x = 102..104` to `(104, 26)`, `Right` 9 along `y = 26` to `(113, 26)`, `Down` 2 to `(113, 28)`, and `Right` 8 along `y = 28` across `(119, 28)` into **Ever Grande City at `(1, 68)`** (`y_evergrande = y_route128 + 40`).
- **Ever Grande City Southern Approach to Waterfall Base (`(1, 68)` -> `(18, 68)`):**
  - From the western entrance at `(1, 68)`, surf `Down` 4 to `(1, 72)`, `Right` 6 to `(7, 72)`, `Down` 3 to `(7, 75)`, `Right` 11 to `(18, 75)`, and `Up` 7 along `x = 18` to the base of the **Ever Grande Waterfall at `(18, 68)`**.
- **Ever Grande City (South — Waterfall Top `(18, 59)` -> Pokémon Center `(27, 48)` & Victory Road `(18, 41)`):**
  - After using **Waterfall** from `(18, 68)` to `(18, 59)`, surf `Up` 4 onto the southern terrace at `(18, 55)`, walk `Right` 2 to `(20, 55)`, and `Up` 2 up the first staircase to the middle terrace at **`(20, 53)`**.
  - **Ever Grande City (South) Pokémon Center:** Door at **`(27, 48)`** (exiting steps to `(27, 49)`). Reached from `(20, 53)` via `Right` 7 along `y = 53` (below the dividing cliff wall `y = 44..52`) to `(27, 53)` and `Up` 5 along `x = 27` into `(27, 48)`.
  - **Victory Road South Entrance:** Cave door at **`(18, 41)`**. Reached from the Pokémon Center `(27, 49)` via `Down` 4 to `(27, 53)`, `Left` 7 along `y = 53` to `(20, 53)`, `Up` 3 up the upper staircase `(19..20, 51..52)` to `(20, 50)`, `Left` 2 to `(18, 50)`, and `Up` 9 along `x = 18` into `(18, 41)`.
## Victory Road (`VictoryRoad_1F` -> `VictoryRoad_B1F` -> `VictoryRoad_B2F` -> `VictoryRoad_1F`)
- **`VictoryRoad_1F` South Entrance (`(15, 40)` -> Rival Wally `(2, 23)`):**
  - From `(15, 40)`, walk `Up` 4 to `(15, 36)`, `Left` 1 to `(14, 36)`, `Up` 7 underneath the lower wooden bridge to `(14, 29)`, `Left` 1 to `(13, 29)`, `Up` 3 up the staircase `(13, 27..28)` to `(13, 26)`, `Left` 11 across the overhead wooden bridge to `(2, 26)`, and `Up` 3 along `x = 2` to **`(2, 23)`**.
  - **Rival Wally `(2, 23)` Team (Single Battle, 1 Full Restore):**
    1. **Altaria Lv. 44** (`DragonBreath`, `Aerial Ace`, `Dragon Dance`, `Safeguard`)
    2. **Roselia Lv. 44** (`Giga Drain`, `Magical Leaf`, `Toxic`, `Leech Seed`)
    3. **Delcatty Lv. 43** (`Sing`, `Assist`, `Charm`, `Feint Attack`)
    4. **Magneton Lv. 41** (`Thunderbolt`, `Supersonic`, `Thunder Wave`, `Tri Attack`)
    5. **Gardevoir Lv. 45** (`Psychic`, `Calm Mind`, `Future Sight`, `Double Team`)
    - *[Defeated — money `$31,759`]*
- **`VictoryRoad_1F` (`(2, 23)` -> Main Progression Ladder `(9, 14)` & Optional Lower/Bridge Paths):**
  - **Main Progression Route on `VictoryRoad_1F` (`(2, 23)` -> `(9, 14)`):**
    - From Rival Wally (`(2, 23)` before battle; stands at `(2, 24)` after battle, so bypass via `x = 3` from `(3, 26)` -> `(3, 18)`), walk north via `(2, 19) -> (3, 19) -> (3, 18) -> (4, 18) -> (4, 14) -> (9, 14)` past **Cooltrainer♀ Hope `(6, 15)`** (`Roselia Lv. 45` [Defeated — money `$33,919`]) onto the **Main Progression Ladder at `(9, 14)`**, which warps to **`VictoryRoad_B1F` at `(8, 3)`**.
  - **Optional Lower Canyon & Upper Wooden Bridge Paths on `VictoryRoad_1F`:**
    - Descending `(13, 26)` -> `(13, 29)` into the lower canyon and walking east via `(9, 29) -> (9, 22) -> (18, 22) -> (18, 24) -> (27, 24) -> (27, 33) -> (28, 35)` (past **Cooltrainer♂ Albert `(27, 34)`** — `Magneton Lv. 43`, `Muk Lv. 43` [Defeated — money `$35,983`]) leads only to a dead-end lower corridor above the impassable southeastern contour ridges (`y = 36..40`; the ladder at `(42, 38)` and Item Ball at `(37, 39)` are in an enclosed alcove reached from B1F).
    - Climbing the north-facing staircase at `(16, 21..19)` from `(16, 22)` to `(16, 17)` and crossing the two high wooden bridges `(18..24, 17)` and `(27..35, 17)` to `(38, 17)` -> staircase `(38, 19..21)` -> `(38..41, 22..26)` leads only to an Item Ball at `(40, 25)` and a south-facing 1-way ledge at `(39..40, 27)`.
- **`VictoryRoad_B1F` (`(8, 3)` -> Boulder & Rock Smash Puzzle):**
  - **Flash Note:** Once **Flash** (`HM05`) is used on `VictoryRoad_B1F`, its expanded illumination radius persists across floor warps inside Victory Road (`"This is in use already."`).
  - **Boulder #1 (`(4, 7)` -> `(3, 7)`):** From the entrance ladder at `(8, 3)`, walk `Down` 1 to `(8, 4)`, `Right` 1 to `(9, 4)`, `Down` 3 along `x = 9` to `(9, 7)`, and `Left` 4 along `y = 7` to `(5, 7)`. Activate **Strength** facing `Left` and push the boulder at **`(4, 7)` `Left` 1 into the wall recess at `(3, 7)`**.
  - **Boulder #2 (`(9, 10)` -> `(10, 10)`):** From `(5, 7)`, walk `Left` 1 to `(4, 7)`, `Down` 3 along `x = 4` to `(4, 10)`, and `Right` 4 along `y = 10` to `(8, 10)`. Push the boulder at **`(9, 10)` `Right` 1 into `(10, 10)`**, opening `(9, 10)` -> `(9, 13)`.
  - **Corridor & 2-Rock / 2-Boulder Puzzle at `(19..21, 4..5)`:**
    - From `(9, 10)`, walk `Down` 3 along `x = 9` to `(9, 13)`, `Right` 6 along `y = 13` to `(15, 13)`, `Up` 8 along `x = 15` to `(15, 5)`, and `Right` 3 to `(18, 5)`.
    - Smash the **Rock Smash rock at `(19, 5)`**, walk `Right` 1 and `Up` 1 to `(19, 4)`, face `Right` to smash the **Rock Smash rock at `(20, 4)`**, and step `Right` 1 onto `(20, 4)`.
    - From `(20, 4)`, push the **Strength boulder at `(20, 5)` `Down` 1 into the wall recess at `(20, 6)`**, walk `Down` 1 and `Right` 1 to `(21, 5)`, and push the **Strength boulder at `(21, 4)` `Up` 1 into the wall recess at `(21, 3)`**, opening the eastern corridor `(21, 4) -> (25, 4)` and south along `x = 25` underneath the wooden bridge `(23..26, 8..9)`.
  - **Cooltrainer♀ Shannon `(26, 16)` Bottleneck & Bridge `(35..38, 16)`:**
    - **Cooltrainer♀ Shannon `(26, 16)`:** Faces `Up` in a 1-tile bottleneck between `(25, 16)` and `(27, 16)`. Walk `Down` 9 from `(25, 4)` to `(25, 13)` and step `Right` 1 onto **`(26, 13)`** (`3` tiles north of `(26, 16)`) so she walks `Up` 2 tiles to `(26, 14)` (`Claydol Lv. 45` [Defeated — money `$38,143`]), vacating `(26, 15..16)`.
    - After defeating Shannon at `(26, 14)`, walk `Left` 1 from `(26, 13)` to `(25, 13)`, `Down` 2 to `(25, 15)`, `Right` 1 to `(26, 15)`, `Down` 4 along `x = 26` to `(26, 19)`, `Right` 6 along `y = 19` to `(32, 19)`, `Up` 3 up the staircase `(32, 18..17)` to `(32, 16)`, and `Right` 10 across the wooden bridge `(36..40, 16)` to `(42, 16)`.
    - From `(42, 16)`, walk `Down` 6 along `x = 42` to `(42, 22)`, `Left` 1 to `(41, 22)`, and `Down` 3 down the staircase `(41, 23..24)` to **`(41, 25)`** (note: `(42, 25)` is the optional up-ladder to the `VictoryRoad_1F (42, 38)` item alcove).
  - **Path from `(41, 25)` to `VictoryRoad_B2F` Ladder `(30, 25)`:**
    - From `(41, 25)`, walk `Left` 2 across the west-facing 1-way ledge at `(39, 25)` onto **`(38, 25)`** (note: walking north from `(38, 25)` along `x = 37..38` underneath the wooden bridge `(36..40, 15..16)` leads to **Cooltrainer♂ Samuel `(37, 12)`** — `Swellow Lv. 42`, `Mawile Lv. 42`, `Kadabra Lv. 42` [Defeated from `(36, 12)` — money `$40,159`], an optional boulder/item alcove at `(35, 6) -> (32, 3)`, and a return shortcut staircase/bridge at `(32, 11..10) -> (32, 8) -> (21, 8) -> (21, 12) -> (18, 12)`).
    - From **`(38, 25)`**, walk `Down` 1 to `(38, 26)`, `Left` 8 along `y = 26` (passing south of the rock `(34..36, 22..25)`) to `(30, 26)`, and `Up` 1 onto the **`VictoryRoad_B2F` Down-Ladder at `(30, 25)`**.
- **`VictoryRoad_B2F` (`(30, 25)` -> River, Waterfalls & Exits):**
  - **Cooltrainer♀ Julie `(35, 22)` & Lower River Surf Entry `(35, 17)`:**
    - From the arrival ladder at `(30, 25)`, walk `Right` 3 to `(33, 25)` and `Up` 3 along `x = 33` to `(33, 22)` to battle **Cooltrainer♀ Julie `(35, 22)`** (`Sandslash Lv. 42`, `Tropius Lv. 42`, `Ninetales Lv. 42` [Defeated — money `$42,175`]; use `Dive` when `Tropius` charges `SolarBeam` to dodge it underwater, then finish with `Strength`).
    - From `(33, 22)`, walk `Up` 5 via `(33..35, 21..17)` underneath the overhead wooden bridge `(28..38, 18..19)` to the water edge at **`(35, 17)`** and use **Surf** `Up` onto `(35, 16)`.
  - **Eastern Waterfall `(25, 12)`, Upper River & Western Waterfall `(8, 10)`:**
    - A rock in the lower river at `(23, 15)` separates the eastern lower river (`x = 24..35, y = 14..15`) from the western lower river (`x = 6..22, y = 14..15`), and the southern shoreline along `y = 16..18` is an impassable 3-step contour ridge wall.
    - From `(35, 16)`, surf `Up` 1 to `(35, 15)`, `Left` 10 along `y = 15` to `(25, 15)`, and `Up` 3 to the base of the **Eastern Waterfall at `(25, 12)`**, then use **Waterfall** to climb to **`(25, 8)`** on the upper river.
    - From `(25, 8)`, surf `Up` 5 to `(25, 3)` and `Left` 17 along `y = 3` (bypassing the Cooltrainer♂ on the shore at `(15, 6)`) to `(8, 3)`, then surf `Down` 7 along `x = 8` to **`(8, 10)`** (note: `(6, 6..10)` is an enclosed western shore pocket, and pressing `Down` at `(8, 10)` rides down the **Western Waterfall** to **`(8, 14)`**).
  - **Western Lower River & Main Progression Up-Ladder `(19, 12)` -> `VictoryRoad_B1F (17, 16)`:**
    - Exhaustive boundary verification on `VictoryRoad_B2F` confirms that `(27..28, 26)` is walled off on the west (`x = 26`) and south (`y = 27`), `(40..44, 20)` is a south-facing 1-way ledge above `(40, 26..23)`, `(28, 5)` is bounded by a west-facing 1-way ledge at `x = 29`, and `(5, 1)` is a solid cliff corner.
    - Therefore, from `(8, 14)` at the bottom of the Western Waterfall, surfing `Right` 9 along `y = 14` to `(17, 14)`, `Up` 1 to `(17, 13)`, stepping `Right` 1 ashore onto `(18, 13)`, and walking `Up` 1, `Right` 1 onto the **Up-Ladder at `(19, 12)`** (warping to **`VictoryRoad_B1F (17, 16)`**) is the main progression path!
- **`VictoryRoad_B1F` Southwestern Section (`(17, 16)` -> `(15, 25)`):**
  - From the arrival ladder at `(17, 16)`, walk `Down` 1 to `(17, 17)`, `Left` 2 to `(15, 17)`, and `Down` 3 along `x = 15` to `(15, 20)` (bypassing the Cooltrainer♂ at `(14, 16)` who faces `Down` along `x = 14`).
  - **Cooltrainer♀ Halle `(14, 20)`:** Rotates `Up`/`Right` to watch `(15, 20)` — `Sableye Lv. 43` (Ghost/Dark, immune to Normal/Fighting), `Absol Lv. 43` [Defeated — money `$44,239`].
  - **From `(15, 20)` to the `(20..21, 25..26)` Puzzle & Up-Ladder `(20, 20)`:**
    - Walk `Down` 5 along `x = 15` from `(15, 20)` to `(15, 25)` and `Right` 4 along `y = 25` to **`(19, 25)`** facing the 2x2 puzzle at `(20..21, 25..26)` (Rock Smash rocks at `(20, 25)` and `(21, 26)`; Strength boulders at `(20, 26)` and `(21, 25)`).
    - **4-Step Solution (do NOT push `(21, 25)` `Right` into `(22, 25)`, as `x = 22` is the 1-tile corridor to `(22, 20)`):**
      1. At `(19, 25)` facing `Right`, use **Rock Smash** on **`(20, 25)`** and step `Right` 1 onto `(20, 25)`.
      2. Face `Down` at `(20, 25)`, activate **Strength**, and push the boulder at **`(20, 26)` `Down` 1 into `(20, 27)`**.
      3. Step `Down` 1 onto `(20, 26)`, face `Right`, and use **Rock Smash** on **`(21, 26)`**.
      4. Walk `Right` 2 to `(22, 26)`, `Up` 1 to `(22, 25)`, and push the boulder at **`(21, 25)` `Left` 1 into `(20, 25)`**, then walk `Up` 4 along `x = 22` (`(22, 25) -> (22, 21)`) and `Left` 2 along `y = 21` onto the **Up-Ladder at `(20, 21)`** (warps to `VictoryRoad_1F (21, 31)`).
- **`VictoryRoad_1F` Final Exit Stretch (`(21, 32)` -> Northern Exit):**
  - From the arrival ladder at `(21, 32)` (from `VictoryRoad_B1F (20, 21)`), walk `Up` 4 up the staircase `(21, 30..29)` to `(21, 28)`, `Right` 12 across the wooden bridge to `(33, 28)`, `Down` 3 down the staircase `(33, 29..30)` to `(33, 31)`, `Right` 3 to `(36, 31)`, `Up` 7 along `x = 36` to `(36, 24)`, `Down` 1 to `(36, 25)`, `Left` 2 to `(34, 25)`, `Up` 2 to `(34, 23)`, and `Left` 1 to `(33, 23)`.
  - **Cooltrainer♂ Edgar `(33, 22)`:** Faces `Down` — `Cacturne Lv. 43`, `Pelipper Lv. 43` [Defeated — money `$46,303`].
  - **Under-Bridge Trainer Pair at `(29, 17)` & `(31, 17)`:** Stand on the lower ground corridor underneath the wooden bridge `(27..35, 17)` facing each other across `(30, 17)` (only their hair peeks above the bridge rail at `y = 16`). Walking `Up` along `x = 32` to `(32, 18)` and pressing `A` facing `Up` side-talks **Cooltrainer♂ Quincy `(31, 17)`** (`Slaking Lv. 43` [1 Full Restore], `Dusclops Lv. 43` [Defeated — money `$48,367`]) in a 1v1 Single Battle instead of triggering a Double Battle at `(30, 17)`. Use `Rock Smash` to defeat `Slaking Lv. 43` and preserve `Dive` PP for Ghost-type `Dusclops Lv. 43`.
  - **Cooltrainer♀ Katelynn `(29, 17)`:** Faces `Right` toward `(30, 17)` underneath the wooden bridge — `Gardevoir Lv. 43`, `Slaking Lv. 43` [Defeated at `(30, 17)` — money `$50,431`; `ATRITON` grew to Lv. 58].
  - **Path from `(30, 17)` to Northern Exit `(39, 6)` -> Ever Grande City (North) `(18, 28)` & Pokémon League Lobby `(18, 5)`:**
    - Walk `Up` 13 along `x = 30` from `(30, 17)` to `(30, 4)`, `Right` 9 along `y = 4` to `(39, 4)`, and `Down` 2 onto the glowing exit mat at **`(39, 6)`**, which exits `VictoryRoad_1F` into northern **Ever Grande City at `(18, 28)`** (outside the northern Victory Road cave door `(18, 27)`). Note: `(40, 3)` is a Rock Smash rock blocking the post-game side passage at `(42, 3)`.
    - From `Ever Grande City (18, 28)`, walk `Down` 2 to `(18, 30)`, `Right` 7 along `y = 30` to `(25, 30)`, `Up` 14 along `x = 25` up the stairs and through the archway to `(25, 16)`, `Left` 7 along `y = 16` to `(18, 16)`, and `Up` 11 up the grand staircase into the **Pokémon League Lobby (`EverGrandeCity_PokemonLeague_1F`) door at `(18, 5)`** (arriving inside at `(9, 11)`; exiting steps to `(18, 6)`).
    - **Pokémon League Lobby (`EverGrandeCity_PokemonLeague_1F`):**
      - **Nurse Joy:** Stand at **`(3, 4)`** facing `Up` (heals party and unlocks the northern **Ever Grande City — Pokémon League** Fly destination).
      - **Poké Mart Clerk:** Stand at **`(16, 4)`** facing `Up` (sells `Ultra Ball $1200`, `Hyper Potion $1200`, `Max Potion $2500`, `Full Restore $3000`, `Full Heal $600`, `Revive $1500`, `Max Repel $700`).
      - **Elite Four Entrance Doorway `(9, 1)`:** Speak to the guard at `(9, 2)` from `(9, 3)` to verify all 8 Gym Badges; the guards step aside to `(8, 2)` and `(11, 2)`, opening `(9, 1)` into `EverGrandeCity_Hall5 (5, 12)` (`Up` 11 along `x = 5` to `(5, 1)` warps into `EverGrandeCity_SidneysRoom` and auto-walks to `(6, 7)`).
    - **Elite Four #1: Sidney (`EverGrandeCity_SidneysRoom` `(6, 5)`):**
      - Stand at `(6, 6)` facing `Up` (`Mightyena Lv. 46` [Intimidate], `Cacturne Lv. 46`, `Shiftry Lv. 48`, `Crawdaunt Lv. 48`, `Absol Lv. 49 [Sitrus Berry]` [Defeated — money `$5,571`, `ATRITON` grew to Lv. 59]). Walk `Left` 1 to `(5, 6)`, `Up` 4 to `(5, 2)`, `Right` 1 to `(6, 2)`, and `Up` 1 into `(6, 1)` -> `EverGrandeCity_Hall1 (5, 12)` -> `Up` 11 to `(5, 1)` -> `EverGrandeCity_PhoebesRoom (6, 7)`.
    - **Elite Four #2: Phoebe (`EverGrandeCity_PhoebesRoom` `(6, 5)`):**
      - Stand at `(6, 6)` facing `Up` (`Dusclops Lv. 48` [Pressure, Turn 1 Protect, Curse], `Banette Lv. 49` [Grudge], `Sableye Lv. 50`, `Banette Lv. 49` [Shadow Ball/Thunderbolt/Psychic/Facade], `Dusclops Lv. 51 [Sitrus Berry, Pressure]` [Defeated — money `$10,671`]). Walk `Left` 1 to `(5, 6)`, `Up` 4 to `(5, 2)`, `Right` 1 to `(6, 2)`, and `Up` 1 into `(6, 1)` -> `EverGrandeCity_Hall2 (5, 12)` -> `Up` 11 to `(5, 1)` -> `EverGrandeCity_GlaciasRoom (6, 7)`.
    - **Elite Four #3: Glacia (`EverGrandeCity_GlaciasRoom` `(6, 5)`):**
      - Stand at `(6, 6)` facing `Up` (`Sealeo Lv. 50` [Encore, Hail], `Glalie Lv. 50` [Light Screen], `Sealeo Lv. 52`, `Glalie Lv. 52` [Explosion, Hail], `Walrein Lv. 53 [Sitrus Berry, Sheer Cold]` [Defeated — money `$15,971`, `ATRITON` grew to Lv. 60]). Walk `Left` 1 to `(5, 6)`, `Up` 4 to `(5, 2)`, `Right` 1 to `(6, 2)`, and `Up` 1 into `(6, 1)` -> `EverGrandeCity_Hall3 (5, 12)` -> `Up` 11 to `(5, 1)` -> `EverGrandeCity_DrakesRoom (6, 7)`.
    - **Elite Four #4: Drake (`EverGrandeCity_DrakesRoom` `(6, 5)`):**
      - Stand at `(6, 6)` facing `Up` (`Shelgon Lv. 52` [Protect, Rock Tomb, Double-Edge], `Altaria Lv. 54`, `Kingdra Lv. 53` [Smokescreen, Dragon Dance], `Flygon Lv. 53`, `Salamence Lv. 55 [Sitrus Berry, Intimidate]` [Defeated — money `$21,471`, `ATRITON` grew to Lv. 61; declined `Endeavor`]). Walk `Left` 1 to `(5, 6)`, `Up` 4 to `(5, 2)`, `Right` 1 to `(6, 2)`, and `Up` 1 into `(6, 1)` -> `EverGrandeCity_Hall4 (5, 33)` -> `Up` 32 to `(5, 1)` -> `EverGrandeCity_ChampionsRoom` (automatically initiates Champion Wallace battle upon entry).
    - **Champion Wallace (`EverGrandeCity_ChampionsRoom`):**
      - Entering `(5, 1)` from `EverGrandeCity_Hall4` auto-walks to `(6, 6)` and plays 12 pre-battle dialogue boxes before initiating battle.
      - Observed team members & Lv. 71+ `ATRITON` strategy:
        1. **Wailord Lv. 57** (`Water Spout`, `Rain Dance`, `Double-Edge`, `Blizzard`): 2HKO with `Return` x 2 (`100% -> 44% -> 0% HP`), reducing Turn 1 `Water Spout` to ~34 HP damage and KOing `Wailord` before it can use `Rain Dance` on Turn 2.
        2. **Ludicolo Lv. 56** (`Giga Drain` [5 PP], `Surf`, `Leech Seed`, `Double Team`): Without Rain (`Swift Swim` inactive), `ATRITON` outspeeds and 2HKOs with `Return` x 2; if `Ludicolo` uses `Leech Seed`, switch to a backup Pokémon on the free Shift prompt after `Ludicolo` faints to clear `Leech Seed` for free.
        3. **Tentacruel Lv. 55** (`Toxic`, `Hydro Pump`, `Sludge Bomb`, `Ice Beam`): 2HKO with `Strength` x 2 (`100% -> 42% -> 0% HP`), staying above the 25% Full Restore threshold while preserving `Return` PP.
        4. **Whiscash Lv. 56** (`Earthquake`, `Surf`, `Amnesia`, `Hyper Beam`): 2HKO with Turn 1 `Waterfall` (~67% damage before `Amnesia`) + Turn 2 Physical `Return` (ignores `Amnesia`).
        5. **Gyarados Lv. 56** (`Dragon Dance`, `Earthquake`, `Hyper Beam`, `Surf` — `Intimidate`): Switch to a conscious backup Pokémon on the free Shift prompt when Wallace announces `Gyarados` so the backup absorbs `Intimidate`; once the backup faints, `ATRITON` enters at `+0 Attack` and 2HKOs `Gyarados` with `Return` x 2 (`100% -> 44% -> 0% HP`), bypassing Full Restore.
        6. **Milotic Lv. 58 [Sitrus Berry]** (`Recover`, `Surf`, `Ice Beam`, `Toxic`): Hit lower 79 base Defense with Physical `Return` and `Strength`.