# Route 9, Route 10 & Rock Tunnel — Verified Coordinates & Topology

## Route 9 (West -> East, Verified Turns 468–482)
- **West Entrance (from Cerulean `(39, 16)`)**: Enters at `Route 9 (0, 8)`; chop the **`Cut` bush at `(5, 8)`** from `(4, 8)`.
- **Verified Ledge & Stair Route East**:
  1. `(4, 8) -> (13, 8)`: **Jr. Trainer♀ Alicia** at `(13, 10)` facing `Left` (`Oddish Lv 18 x2, Bellsprout Lv 18 x2`, defeated Turn 472).
  2. Hop south ledge at `(12, 11)` -> `(12, 15)`:
     - **`TM30 (Teleport)`** item ball at **`(10, 15)`** (collected Turn 473).
     - **Hiker Jeremy** at `(16, 15)` facing `Left` (`Machop Lv 20 x2, Onix Lv 20`, defeated Turn 474; bypass on `y = 14`).
  3. Walk east along `y = 14..15` to **`(29, 14)`** *(Note: `(19, 13)` stairs lead to `(28, 15)` hop -> `(29, 15)`; going past `x = 29` on `y = 14` leads to a dead-end at `(53, 14)`!)*.
  4. Climb wooden stairs #1 at **`(29, 13)`** (`(29, 14) -> Up * 2 -> (29, 12)`), walk `Right * 12` along `y = 12` to **`(41, 12)`**, and climb wooden stairs #2 at **`(41, 11)`** (`(41, 12) -> Up * 4 -> (41, 8)`):
     - **Bug Catcher Brent** at `(40, 8)` facing `Right` (`Beedrill Lv 19 x2, Venonat Lv 20`, defeated Turn 482). *(Do NOT hop south ledge `(46, 11)`!)*
  5. Climb wooden stairs #3 at **`(39, 5)`** (`(41, 7) -> (41, 6) -> (39, 6) -> Up * 3 -> (39, 3)`):
     - **Hiker Alan** at `(43, 3)` facing `Left` (`Geodude Lv 20, Machop Lv 20, Geodude Lv 20`, defeated Turn 485).
     - Bypass rock mound via `y = 3` (`(45, 4) -> (45, 3) -> (51, 3)`), hop **`(51, 6)`** south ledge onto **`(51, 8)`** middle paved road *(do NOT hop `(51, 13)`!)*, and walk `Right` onto **Route 10 `(0, 8)`** (Turn 487).

## Route 10 North & Rock Tunnel Entrance (Verified Turns 487–490)
- Enters from `Route 9 (59, 8)` at **`Route 10 (0, 8)`**.
- Walk `(0, 8) -> (5, 8) -> (5, 13) -> (14, 13) -> (14, 20) -> (11, 20)` (`x = 14` cleanly bypasses the Route 10 Pokémon Center on its east side; `x = 9` has a cliff block at `(9, 14)`).
- **Route 10 Pokémon Center**: Door at **`(11, 19)`**.
- **2-Bush Shortcut to Rock Tunnel**: From `(9, 21)`, chop the two `Cut` bushes at **`(9, 20)`** and **`(9, 18)`**, then step onto **`Rock Tunnel North Entrance (8, 17)`** -> warps to **`Rock Tunnel 1F (15, 3)`**.

## Rock Tunnel Mechanics & Verified Coordinates (Turns 490–503)
- **Un-Flashed Visibility**: Without `HM05 (Flash)`, overworld sprites (player, items, and Trainers) are black, **but all rock walls and `|=|` ladder tiles render in dark maroon outlines** on `latest.png` and `latest_grid.png`.
- **100% Repel Coverage**: Max wild Pokémon level in Rock Tunnel (1F & B1F) is **Lv. 18**, so leading with a Lv. 27+ Pokémon (`NAUTILUS` / `AMETHYST`) + `Repel` (in Bag Slot 0) eliminates 100% of wild encounters.
- **Navigation Rule**: Step single tiles in `run_code` and break immediately when `after == before` so `latest.png` cleanly reveals any `"REPEL's effect wore off!"` prompt, invisible Trainer sightline, or wall.
- **1F Section 1 (Northeast)**:
  - Entrance mat: **`1F (15, 3)`** (exit mat at `(15, 3)`).
  - **Pokémaniac Ashton** at **`1F (22, 8)`** (defeated Turn 494).
  - **Ladder #1**: **`1F (37, 3)`** -> warps down to **`B1F (33, 25)`** *(Note: Ladder #2's upper end `1F (17, 11)` is visible across the wall south of Section 1)*.
- **B1F Section 1 (Southeast -> North)**:
  - Arrives at **`B1F (33, 25)`**; follow corridor south/west around `(28..33, 25..33)` to **`(26, 33)`**.
  - **Pokémaniac Winston** (`Slowpoke Lv 25`): stands north of `(26, 33)` (`~(26, 30)` facing `Down`) and walks down to `(26, 32)` when stepping onto `(26, 33)` (Turns 499–503).
