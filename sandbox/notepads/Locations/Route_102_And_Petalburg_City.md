# Route 102 & Petalburg City — Coordinates & Routing

## Route 102
- **East Entrance (from Oldale Town):** `(49, 10)`
- **West Exit (to Petalburg City):** `(0, 8)` -> enters Petalburg City at `(29, 18)`
- **Westbound Path (Oldale -> Petalburg):**
  - `(49, 10)` -> `Left` to `(36, 10)` -> `Down` 5 to `(36, 15)` -> `Left` along `y = 15` past Youngster Calvin at `(33, 14)` to `(24, 13)`.
  - From `(24, 13)`, walk `Up` 3 to `(24, 10)`, `Left` 6 to `(18, 10)`, `Up` 6 through the ledge gap at `(18, 6)` to `(18, 4)`.
  - From `(18, 4)`, walk `Left` 7 along `y = 4` (bypasses Youngster Allen at `(19, 4)`) to `(11, 4)`.
  - From `(11, 4)`, walk `Down` 4 to `(11, 8)` and `Left` 11 along `y = 8` (bypasses grass `x = 4..10, y = 4..7`) into Petalburg City `(29, 18)`.
- **Trainers Defeated:**
  - Youngster Calvin `(33, 14)` — Poochyena Lv. 5 [Defeated]
  - Bug Catcher Rick `(25, 15)` — Wurmple Lv. 4 x2 [Defeated]
  - Lass Tiana `(8, 7)` — Zigzagoon Lv. 4, Shroomish Lv. 4 [Defeated]

## Petalburg City
- **East Entrance (from Route 102):** `(29, 18)`
- **Pokémon Center Door:** `(20, 16)` (exiting steps to `(20, 17)`)
- **Petalburg Poké Mart Door:** `(25, 12)` (interior doormat at `(3, 7)..(4, 7)`; clerk at `(1, 3)` faced from `(3, 3)`).
- **Petalburg Gym Door:** `(15, 8)` (exiting steps to `(15, 9)`; interior entrance mat is `(4, 111)`).
  - **4-Badge Gym Route (3 Rooms to Norman):** Trainers in Petalburg Gym do not have line-of-sight triggers (talk to them with `A`), and sliding doors are opened by facing them and pressing `A` twice (`A, sleep 1500, A, sleep 1500, A, sleep 3500`):
    1. **Entrance Room `(4, 111)` -> Left Door `(1, 106)`:** Enters **Tier 1 Speed Room `(7, 85)`** (**Cooltrainer Randall `(4, 81)`** — `Swellow Lv. 26` [Defeated]).
    2. **Speed Room `(7, 85)` -> Left Door `(1, 80)`:** Enters **Tier 2 Confusion Room `(7, 46)`** (**Cooltrainer Parker `(4, 42)`** — `Spinda Lv. 26` [Defeated]; note: Right Door `(7, 80)` leads to Defense Room `(1, 59)` with **Cooltrainer Alexia `(4, 55)`** — `Wigglytuff Lv. 26`).
    3. **Confusion Room `(7, 46)` -> Right Door `(7, 41)`:** Enters **Tier 3 Strength Room `(1, 20)`** (**Cooltrainer Jody `(4, 16)`** — `Zangoose Lv. 26` [Defeated]).
    4. **Strength Room `(1, 20)` -> Right Door `(7, 15)`:** Enters **Gym Leader Norman's Room `(1, 7)`** (**Gym Leader Norman `(4, 2)`** — `Spinda Lv. 27`, `Vigoroth Lv. 27`, `Linoone Lv. 29`, `Slaking Lv. 31` [Defeated & Registered — awards Balance Badge & TM42 Facade, followed by Wally's dad escorting the player to Wally's House to award HM03 Surf]).
- **Wally Tutorial Event:** Completed on Turn 107–108, unlocking the western exit of Petalburg City into Route 104 South.
- **Southwestern Pond Items (`(4, 28)` & Hidden Rare Candy `(6, 29)`):** From the Petalburg Pokémon Center `(20, 17)`, walk `Left` 7 to `(13, 17)` and `Down` 7 to `(13, 24)`, step `Left` 2 to `(11, 24)`, and use **Surf** `Left` onto `(10, 24)`. Surf `Down` 3 to `(10, 27)`, `Left` 5 along `y = 27` to `(5, 27)`, and step `Down` 1 to dismount onto `(5, 28)`: facing `Left` at `(5, 28)` claims the visible Item Ball at `(4, 28)` (**Ether**), and stepping `Right` 1 into the 1-tile grass gap at `(6, 28)` facing `Down` claims the hidden **Rare Candy** at `(6, 29)`.
- **West Exit (to Route 104 South):** `(0, 12)` (Scott's cutscene at `(4, 12)` completed on Turn 110).

## Route 104 South
- **East Entrance (from Petalburg City):** `(34, 62)`
- **Beach Bypass Route (Zero Tall Grass):**
  - From Petalburg City `(14, 12)`, walk `Left` 22 (14 to `(0, 12)`, 1 across the border onto `(34, 62)`, and 7 to `(27, 62)`..`(28, 62)`) -> `Down` 9 via east beach steps `(28, 70)` to `(28, 71)`.
  - `Left` 6 to `(22, 71)` -> `Up` 8 to `(22, 63)` -> `Left` 3 to `(19, 63)` -> `Up` 4 to `(19, 59)` -> `Left` 2 to `(17, 59)` -> `Up` 6 via west beach steps `(17, 54)` to `(17, 53)` (in front of **Mr. Briney's Cottage** door at `(17, 50)`; interior entrance mat is `(5, 8)..(6, 8)`, and standing at `(6, 7)` facing `Up` catches Mr. Briney at `(6, 6)` as he circles the table to sail to Dewford Town).
  - From `(17, 53)`, walk `Right` 5 to `(22, 53)` and `Up` 10 along `x = 22` to `(22, 43)` (Oran Berry tree at `(22, 41)`, Pecha Berry tree at `(24, 41)`).
  - From `(22, 43)`, walk `Left` 11 along `y = 43` to `(11, 43)` (Lady Cindy at `(11, 44)` — Zigzagoon Lv. 7 [Defeated]), then `Up` 5 along `x = 11` into **Petalburg Woods** at `(11, 38)`.

## Petalburg Woods
- **South Entrance (from Route 104 South `(11, 38)`):** `(17, 38)`
- **Path to Western Corridor & Devon Researcher:**
  - From `(17, 38)`, walk `Up` 4 tiles to `(17, 34)` and `Left` 10 tiles along `y = 34` (clear ground below grass `x = 10..14, y = 32..33`) to `(7, 34)` (Bug Catcher Lyle at `(7, 33)` — Wurmple Lv. 3 x4 [Defeated]).
  - From `(7, 34)`, step `Left` 1 to `(6, 34)` and walk `Up` 10 tiles along `x = 6` through tall grass `(6, 32..26)` onto clear ground at `(6, 24)`.
  - From `(6, 24)`, follow the clear footpath: `Right` 8 to `(14, 24)` -> `Down` 3 to `(14, 27)` -> `Right` 12 along `y = 27` to `(26, 27)` -> `Up` 4 along `x = 26` to `(26, 23)` (triggers the Devon Researcher & Team Aqua Grunt cutscene; Team Aqua Grunt — Poochyena Lv. 9 [Defeated]; received Great Ball x1 from Researcher).
  - From `(26, 23)`, walk `Up` 7 along `x = 26` to `(26, 16)`, `Left` 18 along `y = 16` (`x = 10..8` is tall grass) to `(8, 16)`, then `Left, Up, Left, Up` through `(7, 16)` and `(7, 15)` onto clear ground at `(6, 14)` (Bug Catcher James at `(4, 14)` — Nincada Lv. 6 x2 [Defeated]).
  - From `(6, 14)`, walk `Up` 4 to `(6, 10)` (Ether item ball is at `(4, 8)`), `Right` 8 (`x = 7..10` is tall grass) to `(14, 10)`, and `Up` 5 to the **North Exit** at `(14, 5)` (step `Up` from `(14, 5)` to exit onto Route 104 North).
- **Petalburg Woods Southbound Center Ledges (Zero Tall Grass):** From the North Exit `(14, 5)`, walk `Down` 19 along `x = 14` (jumps the ledges at `(14, 14)` and `(14, 22)`) to `(14, 26)`, `Right` 3 to `(17, 26)`, and `Down` 13 along `x = 17` (jumps the ledge at `(17, 30)` and steps out the South Exit at `(17, 38)`) onto Route 104 South `(11, 39)`.