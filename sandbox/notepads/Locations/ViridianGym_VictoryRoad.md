# Viridian Gym, Route 22/23, & Victory Road — Verified Notes

## Viridian City -> Viridian Gym `(32, 7)` (Verified Turns 1142–1144)
- From Viridian Pokémon Center `(23, 26)`, walk `Left * 3` to `(20, 26)` (never step `Down` onto the `y = 27` ledge) and north up `x = 19..20` to `(19, 5)`.
- Cross above the Trainer School along **`y = 5`** (`(19, 5) -> (26, 5)`).
- Because a stationary NPC at `(30, 8)` blocks the west approach above the `y = 9` ledge, loop over the north roof of Viridian Gym along **`y = 3`** (`(26, 3) -> (34, 3) -> (34, 8) -> (32, 8) -> Up` into `(32, 7)`).

## Viridian Gym — Verified Spinner & Trainer Route (`Turns 1144–1154`)
- Entrance spawns at `(16, 17)`.
- **Key Puzzle Mechanic (`Tamer at (10, 1)`)**:
  - Riding `(19, 11)` `Up` spinner -> `(19, 2)` -> `(19, 1)` `Left` spinner (`use sleep 6500!`) lands at stopper `(11, 1)`, which is initially blocked on the west by a downward-facing Trainer standing on **`(10, 1)`** (and `(11, 2)` is a `Right` spinner back to `(17, 2)` -> `(18, 2)` `Down` spinner -> `(18, 11)`).
  - **How to Pull `(10, 1)` Off the Top Row**:
    1. Walk `(16, 17) -> (14, 13) -> (14, 9) -> (13, 9) -> (13, 7) -> (15, 7)` *(optional `Revive` ball at `(16, 9)` from `(16, 8)`)* `-> (15, 5)` (defeat right-facing Cooltrainer at `(13, 5)` -> `(14, 5)`).
    2. Walk around Cooltrainer via `(15, 4) -> (13, 4) -> (13, 5) -> (10, 5) -> (10, 4)`: stepping onto `(10, 4)` pulls the `(10, 1)` Trainer south to `(10, 3)`, permanently vacating `(10, 1)` for the current room load!
    3. Do **not** exit the Gym (which would reset NPC positions). Loop back `(9, 4) -> (9, 5) -> (13, 5) -> (13, 4) -> (15, 4) -> (15, 7) -> (13, 7) -> (13, 9) -> (14, 9) -> (14, 13) -> (19, 13) -> (19, 11)` [`Up` spinner] `-> (19, 2) -> (19, 1)` [`Left` spinner] `-> (11, 1)` and walk straight west across vacated `(10, 1)` to **Gym Leader Giovanni**!

## Route 22 -> Pokémon League Front Gate (`Verified Turns 1165–1171`)
- Exit Viridian City west along `y = 18` -> `(4, 17)` -> `(0, 17)` (`arrives at Route 22 (39, 9)`).
- **Important Ledge Trap**: Do **not** jump south over `y = 13` (`(33, 13)` is a one-way south ledge onto the eastbound return track `y = 14..16`).
- Instead, walk `(37, 9) -> (37, 12) -> (30, 12)` (`staying ABOVE y = 13`), walk north through the tall grass via `(30, 12) -> (31, 7)` (wooden bridge in `y = 7`) `-> (31, 5)`, and walk west to **`(29, 5)`** where Rival `GARNET` triggers.
- After defeating `GARNET`, bypass the `(14..15, 4..11)` pillars on the south via **`y = 12`** (`(16, 12) -> (4, 12) -> (4, 10) -> (11, 10)`), cross the `(11, 9)` wooden bridge north to `(8, 6)`, and enter the **Pokémon League Front Gate (`(8, 5)`)**.
- **Route 23 (`Turns 1180–1189`)**: Weave north past staggered badge gates (`x = 7..13`), `Surf` across `y = 103..78`, bypass diagonal rocks `(8..10, 44..47)` via `(11, 48) -> (7, 48)`, pass the final Cascade Badge guard at `(4, 35)`, and enter **Victory Road 1F at `(4, 31)`**.

## Victory Road 1F (`Verified Turns 1189–1196`)
- Entrance spawns at `(8, 17)`; activate `Strength` immediately (`resets each floor load`).
- **Exact Boulder #1 Route (`(5, 15) -> Switch (17, 13)`)**:
  - Push `(5, 15)` `Down` to `(5, 16)`, `Right * 3` to `(8, 16)`, `Up` to `(8, 15)` *(note `(7, 14)` is a rock!)*, `Right` to `(9, 15)`, `Up` to `(9, 14)`, `Right * 7` to `(16, 14)`, `Up * 2` to `(16, 12)` *(around `(15, 13)` rock)*, `Right` to `(17, 12)`, and `Down` onto **`(17, 13)` switch**.
- **Route to 2F Ladder `(1, 1)`**: Walk back to `(5, 14) -> (5, 12)` up `(5, 13)` stairs, loop `(5, 12) -> (11, 12) -> (11, 6) -> (7, 6)` (`1 row below right-facing Cooltrainer♀ at (7, 5)`), descend `(7, 7)` stairs to `(7, 8) -> (3, 8) -> (3, 4)` (defeat Cooltrainer♂ at `(3, 2)`), and climb **`(1, 1)`** to **Victory Road 2F**.

## Victory Road 2F (`Verified Turns 1199–1210`)
- Spawns at `(0, 8)`; dark-checkered dirt tiles are walkable cave floor.
- **Boulder #2A (`(4, 14) -> Switch (1, 16)`)**: Because `(1, 13)` is a rock, push `(4, 14)` `Left` to `(3, 14)`, `Down * 2` to `(3, 16)`, and `Left * 2` onto **`(1, 16)` Switch**.
- **Route to 3F Ladder `(23, 7)`**: Climb `(5, 10)` stairs onto the plateau `(5, 8) -> (14, 8)` (`passing behind left-facing Blackbelt at (12, 9)`), walk `(14, 13) -> (18, 13)` (`defeat Juggler Nelson at (21, 13)`), descend `(21, 15)` stairs to `(21, 16)`, loop `(28, 16) -> (28, 11) -> (21, 11) -> (21, 6)` (`bypassing downward-facing trainer at (19, 8)`), and climb **`(23, 7)`** to **Victory Road 3F**.

## Victory Road 3F (`Verified Turns 1211–1217`)
- Spawns at `(23, 7)`; row **`y = 0`** is walkable floor across `x = 6..27` (`top rock wall is at y = -1`).
- **North Boulder (`(22, 3) -> Switch (3, 5)`)**: Push `Up * 2` to `y = 1`, `Left` across `y = 1` to `(6, 1)`, `Down` from `(6, 0)` to `(6, 2)`, `Left * 4` to `(2, 2)` *(note `(4, 1)` is a rock)*, `Down * 3` to `(2, 5)`, and `Right` from `(1, 5)` onto **`(3, 5)` Switch**.
