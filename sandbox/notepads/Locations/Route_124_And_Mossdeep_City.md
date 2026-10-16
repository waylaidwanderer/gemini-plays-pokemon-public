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
  - From `(25, 17)`, walk `Right` 3 to `(28, 17)` and `Up` 1 into the **Mossdeep City Pokémon Center** at `(28, 16)` (exiting steps to `(28, 17)`). Note: **Steven Stone's House** is at `(18, 16)` to the west.
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
  - Walk `Up` 1 from `(21, 10)` to `(21, 9)`, `Right` 2 along `y = 9` to `(23, 9)`, and `Up` 1 up the front platform steps onto `(23, 8)` to face **Gym Leaders Tate & Liza `(23..24, 7)`** (note: `(21, 7)` is the return teleporter pad to Room 1 `(7, 30)`).
  - **Gym Leaders Tate & Liza Team (Double Battle, 2 Hyper Potions):**
    1. **Claydol Lv. 41** (`Earthquake`, `AncientPower`, `Psychic`, `Light Screen`)
    2. **Xatu Lv. 41** (`Psychic`, `Calm Mind`, `Confuse Ray`, `Sunny Day`)
    3. **Lunatone Lv. 42 [Sitrus Berry]** (`Psychic`, `Hypnosis`, `Calm Mind`, `Light Screen`)
    4. **Solrock Lv. 42 [Sitrus Berry]** (`SolarBeam`, `Sunny Day`, `Psychic`, `Flamethrower`)
    - *[Defeated & Registered — **Mind Badge** and **TM04 (Calm Mind)** obtained]*
  - **Exit Route from `(23, 8)`:** Because `(21, 7)` is on the raised platform level, stay on the platform at `(23, 8)` and walk `Left` 1 to `(22, 8)`, `Up` 1 to `(22, 7)`, and `Left` 1 onto the glowing white return teleporter at **`(21, 7)`** (warps to Room 1 `(7, 30)`), then walk `Down` 1 to `(7, 31)`, `Left` 1 to `(6, 31)`, and `Down` 5 along `x = 6` out `(6, 35)` to Mossdeep City `(38, 10)`.