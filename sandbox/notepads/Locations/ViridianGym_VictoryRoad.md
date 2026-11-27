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
