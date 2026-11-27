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

## Victory Road 2F (`Verified Turns 1199–1210, 1430–1442`)
- Spawns at `(0, 8)` from `1F (1, 1)` (or `(29, 7)` from `Route 23 (14, 31)`); dark-checkered dirt tiles are walkable cave floor, **except `(10..13, 8)` is a north-facing cliff edge** (`stepping Up onto (10..13, 7) is blocked`, Turn 1438) and `x = 8` (`(8, 4..17)` + `(7, 8..9)` Switch #2A barrier) seals the west half from the east half (`Turn 1437`), with zero `3F` holes above `(11, 5)` (`Turn 1442`).
- **`Moltres Lv. 50` (`2F (11, 5)`) Route**: Must enter from **Victory Road `1F`** (`(8, 17)` -> push `(5, 15)` boulder onto `(17, 13)` switch -> `1F (1, 1)` ladder -> `2F (0, 8)`), activate `Strength` on `2F`, push **`2F (5, 5)` boulder** `Up`, and walk east above `(8, 4)` rock (`y = 1..3`) to `(11, 4)` facing **`Moltres`** at **`(11, 5)`**.
- **Boulder #2A (`(4, 14) -> Switch (1, 16)`)**: Because `(1, 13)` is a rock, push `(4, 14)` `Left` to `(3, 14)`, `Down * 2` to `(3, 16)`, and `Left * 2` onto **`(1, 16)` Switch**.
- **Route to 3F Ladder `(23, 7)`**: Climb `(5, 10)` stairs onto the plateau `(5, 8) -> (14, 8)` (`passing behind left-facing Blackbelt at (12, 9)`), walk `(14, 13) -> (18, 13)` (`defeat Juggler Nelson at (21, 13)`), descend `(21, 15)` stairs to `(21, 16)`, loop `(28, 16) -> (28, 11) -> (21, 11) -> (21, 6)` (`bypassing downward-facing trainer at (19, 8)`), and climb **`(23, 7)`** to **Victory Road 3F**.

## Victory Road 3F (`Verified Turns 1211–1224`)
- Spawns at `(23, 7)`; row **`y = 0`** is walkable floor across `x = 6..27` (`top rock wall is at y = -1`).
- **North Boulder (`(22, 3) -> Switch (3, 5)`)**: Push `Up * 2` to `y = 1`, `Left` across `y = 1` to `(6, 1)`, `Down` from `(6, 0)` to `(6, 2)`, `Left * 4` to `(2, 2)` *(note `(4, 1)` is a rock)*, `Down * 3` to `(2, 5)`, and `Right` from `(1, 5)` onto **`(3, 5)` Switch**.
- **Southeast Drop Boulder (`(22, 15) -> Hole (23, 15)`) & Final 2F Exit**:
  - Walk back along `y = 1` to `(20, 6) -> (17, 6) -> (17, 4)` up `(17, 5)` stairs onto the 3F plateau, cross `(17, 4) -> (9, 4) -> (9, 10) -> (5, 10) -> (5, 7) -> (1, 8)`, descend `(1, 9)` stairs to `(1, 15)`, and walk straight east along **`y = 16`** (`passing below all trainers with zero aggro!`) to `(21, 15)`.
  - Shove `(22, 15)` `Right` into `(23, 15)` hole and step into `(23, 15)` behind it -> lands on **2F `(22, 16)`** next to the dropped boulder `(23, 16)`.
  - Re-activate `Strength` on 2F, push `(23, 16)` straight `Left * 14` onto **`(9, 16)` Switch #2B**, climb `(15, 15)` stairs to `(15, 14)`, walk `Right * 10` onto **`(25, 14)` ladder** -> **`3F (27, 15)`** -> `Up * 7, Left` onto **`(26, 8)` ladder** -> **`2F (27, 7)`** -> `Right * 2` onto **`(29, 7)` exit mat**!

## Route 23 North & Indigo Plateau (`Verified Turns 1225–1238`)
- **Victory Road Exit Door Trap**: Stepping onto `2F (29, 7)` spawns outside at `Route 23 (14, 32)` directly below the cave mouth `(14, 31)` (`pressing Up at (14, 32) re-enters Victory Road!`). Step `Down` to `(14, 33)`, walk `Right * 4` to `(18, 33)` east of the `(17, 29..31)` statue wall, climb north to `(19, 18)`, bypass the `(15, 18..19)` statue via `(19, 20) -> (10, 20)`, and walk straight north up **`x = 10`** onto `Indigo Plateau (10, 17) -> (10, 6)` into **Indigo Plateau Lobby (`(7, 11)`)**.
- **Indigo Plateau Lobby Landmarks**:
  - **Nurse Joy**: `(7, 5)` (`stand at (7, 7)` facing `Up`).
  - **Poké Mart**: `(0, 5)` (`stand at (2, 5)` facing `Left`; sells `Full Restore ¥3,000`, `Max Potion ¥2,500`, `Revive ¥1,500`, `Full Heal ¥600`).
  - **Elite Four Entrance**: **`(8, 0)`** (`auto-steps to (4, 5)` inside Lorelei's chamber with a ~2s door-lock animation; Elite Four member stands at `(5, 2)` and north exit opens at `(4..5, 0)`).
- **Lorelei Setup Strategy (`Turns 1236–1238`)**: Lead `Dewgong Lv 54` deals negligible damage (~14 HP over 5 turns) against `Blastoise`; setting up `X Speed x1` + `X Special x4` (`3.0x` Special) lets `Surf` 2HKO `Dewgong`/`Slowbro`/`Lapras` and OHKO `Cloyster`/`Jynx`.
- **Bruno, Agatha, & Lance Chamber Notes (`Turns 1241–1259`)**:
  - **Bruno (`(5, 2)`)**: Curing `PAR` via `Full Restore` (`Slot 16`) on Turn 1 followed by `X Speed` (`Slot 3`) on Turn 2 recalculates `Blastoise`'s Speed without the `0.25x` paralysis drop; `+3` Special `Surf` OHKOs all 5 Pokémon including `Machamp Lv 58`.
  - **Agatha (`(5, 2)`)**: X-Items apply cleanly even while asleep (`SLP`). Watch the blue EXP bar so X-Items aren't over-invested right before a mid-battle level-up (`CalcStats` resets active stat stages to `1.0x`). Against `Gengar Lv 56`/`60` while outspeeding at `+1` Speed, `Dig` (`100` BP in Gen 1, `2x` vs Poison) dodges Turn 1 `Hypnosis`/`Confuse Ray` underground and sets up a clean Turn 3 `Surf` KO.
  - **Lance (`(6, 1)`)**: Stepping through Agatha's `(4, 0)` exit auto-walks around the outer corridor to `(6, 11)`. Walking `Up * 9` to `(6, 2)` auto-triggers Lance at `(6, 1)` (`with (5, 2)` open on the left leading north to `(5, 0)` into the Champion's chamber).
