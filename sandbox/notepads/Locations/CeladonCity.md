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

## Route 16 — Secret `HM02 (Fly)` & `Snorlax` Path (Verified Turns 618–629, 817–818)
- **Fast Route from Celadon Center `(41, 10)` to `Snorlax` `(26, 10)`**: `Down * 2` -> `(41, 12)` -> `Left * 27` along brick boulevard -> `(14, 12)` -> `Down * 2` -> `(14, 14)` -> `Left * 12` (dodging any Dept. Store NPC via `y = 15`) -> `(2, 14)` -> `Down * 4` -> `(2, 18)` -> `Left * 15` -> **`Route 16 (27, 10)`** *(Snorlax sleeps at `(26, 10)`; lower Cycling Road Gatehouse entrance is directly behind Snorlax at `(23, 10)`).*
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
- **Rocket Hideout B2F Spinner Maze -> Elevator (Verified Turns 668–675)**:
  - From `B2F (21, 9)`: `Left * 2, Down * 4, Left, Up * 3, Left` onto **`(17, 10)` (`<` -> `(13, 10)` `∨` -> `(13, 12)` `>` chain)** -> `(14, 12)` -> `Down, Left * 2` onto **`(12, 13)` (`∧` -> `(12, 9)` `<` long chain, `"sleep 6500"`)** -> lands at `(2, 9)`.
  - From `(2, 9)`: `Right, Down * 2, Right` onto **`(4, 11)` (`>`)** -> `(8, 11)` -> `Right * 2, Down * 3, Right` onto **`(11, 14)` (`∨` -> `(11, 16)` `>` -> `(13, 16)` `>` -> `(15, 16)` `∨` chain)** -> `(15, 18)`.
  - From `(15, 18)`: `Left * 2` onto **`(13, 18)` (`<` -> `(11, 18)` `∨`)** -> `(11, 20)` -> `Right * 3, Down * 2, Left` onto **`(13, 22)` (`<` -> `(9, 22)` `∨`)** -> `(9, 24)` -> `Right, Down` onto **`(10, 25)` (`>`)** -> `(14, 25)` -> `Right * 2, Up * 5, Right * 4` -> `(20, 20)` (Elevator mat at **`(24..25, 19)`**!).
- **Rocket Hideout Elevator & B4F East — Giovanni & `SILPH SCOPE` (Verified Turns 676–689)**:
  - Step onto `B2F (24, 19)` and press `Down` -> enters Elevator at `(2, 2)`. Control panel at `(1, 1)` (`B1F / B2F / B4F / CANCEL`; ride takes ~3.5s, then `Right, Up` from `(1, 2)` exits onto **`B4F (25, 15)`**).
  - Walk `Up * 3` along `x = 25` to `(25, 12)` between the two Door Grunts (`(26, 12)` and `(23, 12)`); defeating both opens the electronic door at `(24..25, 11)`.
  - **Giovanni** stands at **`B4F (25, 3)`** (`Onix Lv 25, Rhyhorn Lv 24, Kangaskhan Lv 29`). After defeat, he vanishes and spawns **`SILPH SCOPE`** at **`(25, 2)`** (`1` tile north of `(25, 3)`, NOT on `(25, 3)`!). `Escape Rope` works inside Rocket Hideout B4F.

## Celadon Gym Route (Verified Turns 696–702)
- From **Celadon Pokémon Center `(41, 10)`**: walk `Down * 4` to `(41, 14)`, `Left * 4` to `(37, 14)`, `Down * 8` to `(37, 22)`, `Left * 11` to `(26, 22)`, `Down, Left * 2, Down * 8` to `(24, 31)`, `Right * 11` to `(35, 31)`.
- Chop **`Cut` bush at `(35, 32)`**, walk `Down * 3` to `(35, 34)`, `Left * 30` along `y = 34` to `(5, 34)`, climb wooden stairs at **`(5, 31)`** up to `(5, 29)`, `Right * 7` to `(12, 29)`, and `Up * 2` into **Celadon Gym `(12, 27)`**!
- **Celadon Gym Interior (Verified Turns 703–713)**:
  - Entrance spawns at `(4, 17)`. Walk `Up * 6` to `(4, 11)` (Lass Kay at `(2, 11)`), `Right, Up` to `(5, 10)` (Beauty Bridget at `(7, 10)`: `Oddish, Bellsprout, Oddish, Bellsprout Lv 21` — evolved `NAUTILUS` into **`Blastoise` at Lv. 36**, Turn 711!).
  - Walk `Up * 2` to `(5, 8)`, chop interior **`Cut` bush at `(5, 7)`**, and enter inner gazebo (`Cooltrainer♀ Mary at (5, 3)`, **Gym Leader Erika at `(4, 3)`**; note indoor flower tiles like `(4, 6)` are walkable).
  - **Erika Battle Note (`Turns 724–734`)**: `Victreebel Lv 29` (`52` Speed, 99.6%-crit `Razor Leaf` + `Sleep Powder` + `Wrap`) survives a single Lv. 36 `Blastoise` `Ice Beam` on ~18% HP and deals ~63–70 damage with crit `Razor Leaf`; `Paras` (`4x` Grass resistance) takes only ~15 damage from crit `Razor Leaf`, providing safe healing pivots.
