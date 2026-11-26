# Celadon City — Verified Coordinates & Notes

## Overworld Landmarks (Verified Turns 600–604)
- **East Entrance (from Route 7 `(0, 3)`)**: Enters at **`Celadon City (49, 11)`**.
- **Celadon Pokémon Center**: Door at **`(41, 9)`** *(Note: always attach post-warp `"sleep 700"` to the `"Up"`/`"Down"` button rather than a standalone `press_buttons(["sleep ..."])`, which is prohibited)*.
- **Main East-West Boulevard**: `y = 11..13` runs straight from `(41, 12)` to the east wall of Celadon Dept. Store (`x = 14`), dropping to `y = 14` in front of the store doors.
- **Celadon Department Store**: Doors at **`(8, 13)`** and **`(10, 13)`** (`MART` sign at `(12, 13)`).

## Celadon Department Store Interior (Verified Turns 604–618)
- Entering `(10, 13)` spawns at **`1F (16, 7)`** (`exit mat at (16..17, 7)`).
- **Exact Floor-to-Floor Stair Pairs** *(white treads = UP, dark stairwell = DOWN; arriving auto-steps to `y = 2`)*:
  - `1F (12, 1)` <-> `2F (12, 1)`
  - `2F (16, 1)` <-> `3F (16, 1)`
  - `3F (12, 1)` <-> `4F (12, 1)`
  - `4F (16, 1)` <-> `5F (16, 1)`
  - `5F (12, 1)` <-> `6F (15, 2)` (Rooftop Square)
- **6F Rooftop Square**:
  - Vending Machines at `(11, 1)` and **`(12, 2)`** (`Fresh Water ¥200`, `Soda Pop ¥300`, `Lemonade ¥350`; note `"Clang! ▼"` + `"<DRINK> popped out! ▼"` needs **two** `B` presses per drink).
  - **Thirsty Girl** wanders around **`(5, 5)`**: trading `Fresh Water` yields **`TM13 (Ice Beam)`** (taught to `NAUTILUS` replacing `Mega Punch`, Turn 617).

## Route 16 — Secret `HM02 (Fly)` Path (Verified Turns 618–629)
- Exit west of Celadon City along **`y = 18`** onto `Route 16 (39, 10)` *(Snorlax sleeps at `(26, 10)`).*
- Chop **`Cut` bush at `Route 16 (34, 9)`** from `(34, 10)`; upper tall grass `(28..34, 4)` has `Spearow` & `Doduo` (caught Lv. 22 `Spearow` **`JASPER`**, Turn 628).
- Enter **Upper Route 16 Gatehouse at `(23, 5)`** -> spawns at `(7, 3)`; bypass NPC at `(4, 3)` via **`y = 2`** (`(0, 2) -> Left` exits to West Route 16).
- **Secret House (`HM02 Fly`)**: Door at **`Route 16 (7, 5)`**; girl at `(2, 3)` gives `HM02 (Fly)` (Turn 632).

## Celadon Game Corner & Rocket Hideout (Verified Turns 639–650)
- **Game Corner Entrance**: Door at **`Celadon City (28, 19)`** -> spawns at **`(15, 17)`**.
- **Poster Switch**: Defeat Rocket Grunt at **`(9, 5)`**, then inspect **`(9, 4)`** (`["A", "sleep 1200", "A", "sleep 1200", "A", "sleep 2500"]` — note `"Let's push it!"` closes with no extra `"Click!"` box) -> opens secret staircase down to **Rocket Hideout B1F** at **`(17, 4)`**!
- **Direct B1F -> B2F -> B3F Shortcut (Zero Trainers, Bypasses B2F Spinner Maze!)**:
  - `Game Corner (17, 4)` -> **`B1F (21, 2)`** -> walk `Right * 2` onto **`B1F (23, 2)`** -> **`B2F (27, 8)`**.
  - On **B2F**: walk `Down * 6` to `(27, 14)`, `Left * 5` to `(22, 14)`, `Up * 6` along `x = 22` (outside sightline of Rocket Grunt facing `Down` at `(20, 12)`) to `(22, 8)`, then `Left` onto **`B2F (21, 8)`** -> warps directly to **`B3F (25, 6)`**!
- **Rocket Hideout B3F Spinner Maze (Verified Turns 654–660)**:
  - From `B3F (25, 6)`: `Left * 5` -> `(20, 6)` -> `Down * 3` -> `(20, 9)` -> `Left * 7` -> `(13, 9)` -> `Down * 2` -> `(13, 11)` -> `Left` onto **`(12, 11)` (`<` spinner)** -> lands at `(10, 11)`.
  - From `(10, 11)`: `Down * 2` onto **`(10, 13)` (`>` spinner)** -> lands at `(14, 13)` -> `Left * 2` -> `(12, 13)` -> `Down * 3` -> `(12, 16)` -> `Left * 3` -> `(9, 16)` -> `Down * 2` -> `(9, 18)` -> `Right * 2` onto **`(11, 18)` (`>` -> `(15, 18)` `∨` spinner chain)** -> lands at `(15, 22)`!
  - From `(15, 22)`: `Left * 2, Down * 4, Right * 6, Up * 8` onto **`B3F (19, 18)`** -> warps to **`B4F (19, 10)`**.
  - **Return up B3F**: From `B3F (19, 18)` -> `Left, Up * 2` onto `(18, 16)` (`∧`) -> `(18, 15)` -> `Left * 2, Up * 2` onto `(16, 13)` (`∧`) -> `(16, 11)` -> `Right * 4, Up * 5, Right * 5` to `B3F (25, 6)`.
- **Rocket Hideout B4F West — `LIFT KEY` Spawn Rule (Verified Turns 662–665)**:
  - Walk `Up * 6` from `(19, 10)` to `(19, 4)`, `Left * 5` to `(14, 4)`, `Up, Left * 3` to `(11, 3)` to fight the Lift Key Rocket Grunt at **`(11, 2)`** (`Koffing, Zubat Lv 21`).
  - **CRITICAL**: Defeating him does NOT auto-spawn the `Lift Key` (`(9, 4)` is a separate item ball)! You **must talk to him once** after battle (`Up, A`) so he says `"Oh no! I dropped the LIFT KEY!"`, spawning the **`LIFT KEY`** ball at **`(10, 2)`**!
