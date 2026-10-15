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
- **Mossdeep Poké Mart:** Door at `(37, 18)`.
- **Mossdeep City Gym:** Door at `(38, 9)` (exiting steps to `(38, 10)`). Reached from the Pokémon Center `(28, 17)` via `Right` 5 to `(33, 17)`, `Up` 7 along `x = 33` to `(33, 10)`, `Right` 5 along `y = 10` to `(38, 10)`, and `Up` 1 into `(38, 9)`.

## Mossdeep City Gym (`(38, 9)` -> `(6, 35)`)
- **Mechanics:** Stepping onto a colored Floor Switch (`Yellow`, `Blue`, `Green`, `Purple`, `Red`) slides the statues and trainers on the matching-color arrow track by 1 tile along the arrows (4 states mod 4). The arrow tiles themselves do NOT slide the player; the player walks across uncovered arrow tiles like normal floor. In `run_code`, stepping onto a Gym floor switch aborts the current `press_buttons` call and plays the slide animation on the next `press_buttons` call (prepend `"sleep 1500"` before stepping off).
- **Room 1 (`(6, 35)` -> `(3, 28)`):**
  - From the entrance at `(6, 35)`, walk `Up` 4 to `(6, 31)`, `Left` 3 along `y = 31` to `(3, 31)`, and `Up` 1 onto the **Yellow Floor Switch at `(3, 30)`**.
  - Stepping onto `(3, 30)` rotates **Psychic Preston `(2, 30)`** (`Kirlia Lv. 36`) and **Psychic Maura `(4, 30)`** (`Kadabra Lv. 36`) to face `(3, 30)` for a Double Battle [Defeated].
  - From `(3, 30)`, walk `Up` 2 through `(3, 29)` onto the teleporter pad at **`(3, 28)`**, which warps to **Room 2 at `(1, 23)`** (note: `(7, 30)` and `(1, 33)` in Room 1 are return/later pads).
- **Room 2 (`(1, 23)` -> `(9, 18)`):**
  - Contains a **Yellow Floor Switch at `(2, 21)`** and a 2x2 counter-clockwise conveyor loop at **`(4..5, 20..21)`**, with **Psychic Samantha `(4, 23)`** facing `Up` toward `(4, 22)` (`Xatu Lv. 36` [Defeated]) and **Psychic Blake** on the 2x2 block.
  - After **1 press** of `(2, 21)` (State 1), `(4..5, 20..21)` has Statue at `(4, 20)` and **Psychic Blake** facing `Down` at `(4, 21)` (`Girafarig Lv. 36` [Defeated]), leaving `(5, 21)` and `(5, 20)` uncovered. Walk `Right` 3 from `(2, 22)` to `(5, 22)` (defeating Psychic Blake at `(4, 22)`), walk `Up` 2 through `(5, 21)` to `(5, 20)`, `Right` 3 to `(8, 20)`, `Up` 2 to `(8, 18)`, and `Right` 1 onto the teleporter at **`(9, 18)`**.