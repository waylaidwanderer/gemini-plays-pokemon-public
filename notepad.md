<h1><code>Main</code></h1>

# Pokémon Blue Version — Main Dashboard

## Run Overview
- **Game:** Pokémon Blue Version (Generation I, GBC-colorized QoL variant)
- **Trainer Name:** COBALT
- **Rival Name:** GARNET
- **Starter:** Squirtle (Nickname: `NAUTILUS`, evolved into Wartortle at Lv. 16)

## Badges & Milestones
- [x] Starter Pokémon & Pokédex (Pallet Town / Viridian City)
- [x] Boulder Badge — Brock (Pewter City)
- [x] Mt. Moon Cleared (`Helix Fossil`, `Moon Stone`, `TM01 Mega Punch`, `TM12 Water Gun`)
- [x] Cerulean Rival `GARNET` Defeated (Turn 257)
- [x] `S.S. Ticket` Obtained from Bill (Sea Cottage, Turn 343)
- [ ] Cascade Badge — Misty (Cerulean City)
- [ ] Thunder Badge — Lt. Surge (Vermilion City)
- [ ] Rainbow Badge — Erika (Celadon City)
- [ ] Soul Badge — Koga (Fuchsia City)
- [ ] Marsh Badge — Sabrina (Saffron City)
- [ ] Volcano Badge — Blaine (Cinnabar Island)
- [ ] Earth Badge — Giovanni (Viridian City)
- [ ] Indigo Plateau — Elite Four & Champion

## Active Party
1. **AMETHYST** (Nidoqueen) — Lv. 16 (`55/55` HP) | Moves: Water Gun, Scratch, Tackle, Poison Sting *(Evolved Turn 328! Learns Body Slam at Lv. 23!)*
2. **NAUTILUS** (Wartortle) — Lv. 24 (`51/65` HP) | Moves: Water Gun, Mega Punch, Tackle, Bite
3. **CELESTE** (Clefairy) — Lv. 8 (`30/30` HP) | Moves: Pound, Growl *(1% Mt. Moon 1F catch)*
4. **AMBER** (Paras) — Lv. 12 (`32/32` HP) | Moves: Scratch *(`HM01 Cut` & `Spore` specialist)*

## Inventory & Money
- Money: ~¥7,000 (+ `Nugget` worth ¥5,000!)
- Key Items: Pokédex, Town Map, Helix Fossil, S.S. Ticket
- Bag: Antidote x1, Poké Ball x2, TM34 (Bide), Town Map, HP Up x1, Escape Rope x1, Nugget x1, TM45 (Thunder Wave)

## Notepad Index
- `notepads/Main.md` — High-level dashboard & party summary
- `notepads/Scratchpad/Routing.md` — Active route planning & immediate checklists
- `notepads/Mechanics/Harness.md` — Verified harness timing & input behavior
- `notepads/Locations/` — Verified town, route, and dungeon notes


<hr>

<h1><code>Locations/CeruleanCity</code></h1>

# Cerulean City, Route 24 & Route 25 — Verified Coordinates & Landmarks

## Map Connections & Elevation Topology (Verified Turns 245–272)
- **West Entrance (from Route 4 East `(89, 8)`)**: Enters Cerulean City at `(0, 18)`.
- **North/South Ledge Divide (`y = 15`)**:
  - **Going North (`y = 18..19 -> y = 12`)**: MUST climb the wooden stairs at **`(8, 15)`** (`(8, 16) -> Up * 4 -> (8, 12)`). Both `(9..11, 15)` and the lawn east of the Pokémon Center (`x = 22`) have one-way south-facing ledges!
  - **Going South Shortcut (`y = 12 -> y = 18`)**: From `(20, 12)`, walking `Right * 2` to `(22, 12)` and `Down * 6` hops the south-facing ledge straight down to `(22, 18)` right next to the Pokémon Center `(19, 17)` (verified Turn 265).
- **North Exit (to Route 24 / Nugget Bridge)**: Walk east along `y = 12` to `(20, 12)`, then `Up` along `x = 20` (`(20, 0)` transitions to **Route 24 `(10, 35)`**). Rival `GARNET` ambushes at `(20, 6)` (defeated Turn 257).

## Key Cerulean City Buildings
- **Badge Guy House (Backyard Rare Candy)**: Front door at **`(9, 11)`** (`(2, 7)` indoors); north back door exits to `(9, 9)` in fenced backyard where hidden **`Rare Candy`** is at **`(15, 8)`** (collected Turn 275 facing `Right` from `(14, 8)`).
- **Trade House (`Jynx` for Poliwhirl)**: Door at `(13, 15)`.
- **Cerulean Pokémon Center**: Door at **`(19, 17)`** (warps indoors to `(3, 7)`; Nurse Joy counter at `(3, 3)` facing `Up`). Note: `POKé` sign sits at `(20, 17)`.
- **Cerulean Gym (Misty)**: Located SE of Pokémon Center (`x = 24..27`, roof at `y = 16..18`).
- **Burgled House (`TM28 Dig` Rocket)**: NE Cerulean `(27, 11)` (opens after visiting Bill on Route 25).

## Route 24 (Nugget Bridge, `x = 10..11`)
- Enters from Cerulean `(20, 0)` at **Route 24 `(10, 35)`**.
- Alternating trainer column positions (defeated trainers remain standing on their tile, so zigzag `x = 10 <-> 11`):
  1. **Bug Catcher Cale** at **`(11, 31)`** facing `Left` (Defeated Turn 263).
  2. **Lass Ali** at **`(10, 28)`** facing `Right` (Defeated Turn 279).
  3. **Youngster Timmy** at **`(11, 25)`** facing `Left` (Defeated Turn 282).
  4. **Lass Reli** at **`(10, 22)`** facing `Right` (Defeated Turn 284).
  5. **Jr. Trainer♂ Shane** at **`(11, 19)`** facing `Left` (Defeated Turn 284).
  6. **Team Rocket Grunt (`Nugget`)** at **`(11, 15)`** (Awarded `Nugget` Turn 285; defeated Turn 289).
- **Northern Plateau Item**: Climb wooden stairs at **`(6, 7)`** -> **`TM45 (Thunder Wave)`** item ball at **`(10, 5)`** (collected Turn 294); hop south ledge `(7..12, 7)` back down to `y = 8` and walk east (`(19, 8) -> Route 25 (0, 8)`).

## Route 25 (West -> Sea Cottage)
- Enters from Route 24 `(19, 8)` at **Route 25 `(0, 8)`**.
- **Verified Trainer Positions (West Half)**:
  1. **Hiker #1 (Franklin)** at **`(8, 4)`** facing `Down` (`Machop Lv 15, Geodude Lv 15` — Defeated Turn 297).
  2. **Hiker #2 (Wayne)** at **`(13, 7)`** facing `Left` (`Onix Lv 17` — Defeated Turn 297 via `(9, 8) -> (9, 4) -> (13, 4) -> (13, 6)`).
  3. **Youngster Joey** walked from `(14, 2)` to **`(14, 3)`** (`Rattata Lv 15, Spearow Lv 15` — Defeated Turn 299; walking him down 1 tile also opens the `(13, 2)` gap to `TM19 Seismic Toss`!).
  4. **Youngster Dan** at **`(18, 5)`** (`Slowpoke Lv 17` — Defeated Turn 311 from `(17, 5)`).
  5. **Lass Kelsey** at **`(18, 8)`** facing `Left` (`Nidoran♂ Lv 15, Nidoran♀ Lv 15` — Defeated Turn 315; bypass via `(17, 7) -> (20, 7) -> (20, 8)`).
  6. **Hiker Nob** at **`(23, 9)`** facing `Up` (`Geodude x3, Machop Lv 13` — Defeated Turn 323).
  7. **Jr. Trainer♂ Flint** at **`(24, 4)`** facing `Down` (`Rattata Lv 14, Ekans Lv 14` — Defeated Turn 333).
  8. **Youngster Chad** at **`(32, 3)`** facing `Left` (`Ekans Lv 14, Sandshrew Lv 14` — Defeated Turn 336 from `(30, 3)`).
  9. **Jr. Trainer♀** at **`(37, 4)`** facing `Down` (`Oddish Lv 13, Pidgey Lv 13, Oddish Lv 13` — Defeated Turn 339 at `(37, 6)`).
- **Cuttable Bush (`TM19 Seismic Toss`)**: Located at **`(26, 3)`**.
- **Bill's Sea Cottage**: Door at **`(45, 3)`** (courtyard at `(45, 6)`, wooden bridge south to southern return ledge at `x = 44..47, y = 8+`).
- **Express Cerulean <-> Route 25 Corridor**: `(19, 18) <-> (8, 19) <-> (8, 12) <-> (20, 12) <-> Route 24 (10, 35) <-> zigzag x=10/11 <-> (10, 8) <-> Route 25 (9, 8) <-> (9, 4) <-> (17, 4)` (100% wild-free & trainer-free).


<hr>

<h1><code>Locations/PalletTown</code></h1>

# Pallet Town — Verified Coordinates & Landmarks

## Red / Cobalt's House
- **2F (Bedroom)**:
  - Initial spawn: `(3, 6)`
  - Bedroom PC: `(0, 1)` — interact from `(0, 2)` facing `Up` (contains 1 free `POTION` at start).
  - Stairs to 1F: `(7, 1)`
- **1F (Living Room)**:
  - Stairs arrival from 2F: `(7, 1)`
  - Clear route to exit: `(7, 1) -> (6, 1..6) -> (3, 6..7) -> Down`
  - Exits to Pallet Town at `(5, 6)`.

## Pallet Town Overworld
- Cobalt's House door: `(5, 5)` (exits to `(5, 6)`).
- North tall-grass Route 1 entrance: `(10, 1)` and `(11, 1)`.
- Professor Oak's Lab door: `(12, 11)` (exits to `(12, 12)`).
- Rival's House (Daisy / Town Map): Northeast house (`x = 12..15, y = 3..5`, door at `(13, 5)`).

## Professor Oak's Lab
- Starter Poké Ball table: `(6, 3)` Charmander, `(7, 3)` Squirtle, `(8, 3)` Bulbasaur.
- Table front apron `(6..8, 4)` is walkable floor; interact facing `Up` from `(x, 4)`.
- Central aisle: `x = 4..5`; Rival first battle triggers at `y = 6` (`(4, 6)` or `(5, 6)`).
- Exit mat: `(4, 11)` and `(5, 11)` (`Down` exits to Pallet Town).


<hr>

<h1><code>Locations/PewterCity</code></h1>

# Pewter City — Verified Coordinates & Landmarks

## Map Connections
- **South Entrance (from Route 2 North)**: Enters at `(18, 35)`.
- **East Exit (to Route 3)**: Walk East from `(23, 18)` along `y = 18..19` to `x = 39 -> Right` warps to Route 3 `(0, 10)`.
  - **Route 3 Early Landmarks**: Lass #1 triggers at `(14, 9)` (`2x Pidgey Lv 9`); Bug Catcher #1 triggers at `(11, 6)` (`Caterpie Lv 10, Weedle Lv 10, Caterpie Lv 10`).

## Key Buildings
- **Pokémon Center**: Door at `(13, 25)` (approached via `(18, 35) -> (18, 26) -> (13, 26)`).
- **Poké Mart**: Door at `(23, 17)` (east of central `x = 19` road).
- **Pewter City Gym**: Door at `(16, 17)`.
  - Verified loop from `(13, 26)` PokéCenter: `(13, 26) -> (19, 26) -> (19, 12) -> (11, 12) -> (11, 16) -> (10, 16) -> (10, 18) -> (16, 18) -> Up` into `(16, 17)` (reverse to exit).
  - Interior: Spawn at `(4, 13)`, Jr. Trainer♂ triggers at `(4, 6)`, Brock stands at `(4, 1)` (talk from `(4, 2)`).


<hr>

<h1><code>Locations/Route1</code></h1>

# Route 1 — Verified Coordinates & Navigation

## Map Connections
- **South Exit (to Pallet Town)**: `x = 10..11, y = 35` -> `Down` warps to Pallet Town `(10..11, 0)`.
- **North Exit (to Viridian City)**: `x = 10..11, y = 0` -> `Up` warps to Viridian City `(20..21, 35)`.

## Key NPCs
- **Poké Mart Sample Clerk (Free Potion)**: Wanders around `(5, 24..25)` in the west-central clearing.

## Verified Northbound Path (Pallet -> Viridian)
1. Enter at `(10, 35)` -> `Up` x 7 to `(10, 28)`.
2. `Left` x 2 to `(8, 28)` -> `Up` x 2 to `(8, 26)` -> `Right` x 5 to `(13, 26)` -> `Up` x 6 to `(13, 20)`.
3. `Left` x 8 to `(5, 20)` -> `Up` x 6 to `(5, 14)`.
4. `Right` x 10 to `(15, 14)` (avoids Boy NPC at `(14, 13)`) -> `Up` x 3 to `(15, 11)`.
5. `Left` x 4 to `(11, 11)` -> `Up` x 5 to `(11, 6)` -> `Right` x 3 to `(14, 6)` -> `Up` x 2 to `(14, 4)` -> `Left` x 3 to `(11, 4)` -> `Up` x 5 into Viridian City.

## Verified Southbound Ledge Chain (Viridian -> Pallet, Minimal Grass)
1. Enter at `(10, 0)` -> `Down` x 3 to `(10, 3)` -> `Left` x 2 to `(8, 3)`.
2. `Down` along column `x = 8` down to `(8, 18)` (hops 3 ledges at `y = 5, 9, 13` with ZERO tall grass tiles!).
3. `Right` x 5 to `(13, 18)` -> `Down` to `(13, 26)` (hops `y = 19` ledge; 4 grass tiles `y = 22..25`).
4. `Left` x 3 to `(10, 26)` -> `Down` to `(10, 35)` -> `Down` into Pallet Town `(10, 0)` (hops `y = 27` ledge; 4 grass tiles `y = 32..35`).



<hr>

<h1><code>Locations/Route2_ViridianForest</code></h1>

# Route 2 & Viridian Forest — Verified Coordinates

## Route 2 (South Half)
- **South Entrance (from Viridian City)**: Enters at `(8, 71)`.
- **Verified Path to Viridian Forest South Gate**:
  - `(8, 71) -> (8, 63) -> (7, 63) -> (7, 59)` (crosses `(7, 61)` bridge).
  - `(7, 59) -> (3, 59) -> (3, 48) -> (8, 48) -> (8, 46) -> (3, 46) -> (3, 43)` (South Gate door).
- **Viridian Forest South Gate (`10x8`)**:
  - South entrance arrives at `(4, 7)`.
  - North exit door to Viridian Forest is at `(5, 0)`.

## Viridian Forest (`34x48`)
- **South Entrance**: Arrives at `(17, 47)`.
- **Verified Low-Grass S-Curve Route**:
  1. `(17, 47) -> (17, 43) -> (27, 43) -> (27, 41) -> (26, 41) -> (26, 33)` (Bug Catcher #1 at `(27, 33)`).
  2. `(26, 33) -> (26, 32) -> (31, 32) -> (31, 8)` (100% grass-free east lane!).
  3. `(31, 8) -> (16, 8) -> (16, 19) -> (12, 19) -> (12, 4) -> (11, 4) -> (11, 2) -> (6, 2) -> (6, 25) -> (1, 25)`.
  4. `(1, 25) -> (1, 18)` (Bug Catcher Sammy: `Weedle Lv 9`) -> `(1, 0)` (North Gate warp).
- **Viridian Forest North Gate (`10x8`)**:
  - South entrance arrives at `(4, 7)`; North exit door at `(5, 0)` -> Route 2 North `(3, 11)`.
- **Route 2 (North Exit to Pewter City)**:
  - `(3, 11) -> (8, 2) -> (8, 0) -> Up` warps to Pewter City `(18, 35)`.



<hr>

<h1><code>Locations/Route3_MtMoon</code></h1>

# Route 3 & Route 4 West — Verified Coordinates & Landmarks

## Route 3 (`x = 0..59`)
- **West Entrance (from Pewter City `(39, 18)`)**: Enters at `(0, 10)`.
- **Verified Trainers & Obstacles**:
  - **Lass #1**: `(14, 9)` (`2x Pidgey Lv 9`) — Defeated.
  - **Bug Catcher #1**: `(11, 6)` (`Caterpie Lv 10, Weedle Lv 10, Caterpie Lv 10`) — Defeated.
  - **Youngster #1**: `(14, 6)` (`Rattata Lv 11, Ekans Lv 11`) — Defeated.
  - **Bug Catcher #2**: `(19, 5)` facing Left/Down, triggered at `(19, 6)` (`Weedle Lv 9, Kakuna Lv 9, Caterpie Lv 9, Metapod Lv 9`) — Defeated (Turn 141).
  - **Lass #2**: Starts at `(23, 4)` facing Left, spots player at `(20, 4)` and walks to `(21, 4)` (`Rattata Lv 10, Nidoran♂ Lv 10`) — Defeated (Turn 146; `NAUTILUS` reached Lv 16).
  - **Tree Wall & Ledges around `x = 17..24`**:
    - Vertical bush barriers at `(17, 6)..(17, 10)` and `(23, 6)..(23, 10)`.
    - South-facing ledge along `y = 7` (`(15, 7)..(16, 7)`, `(18, 7)..(22, 7)`, `(24, 7)`).
    - Open eastward gap between rock wall (`y = 3`) and bush column (`x = 23, y >= 6`) runs along `y = 4..5` (`(20, 5) -> (24, 5)` bypasses `(21, 4)` Lass #2).
    - **Bug Catcher #3**: Stands at `(24, 6)` facing Right; spots player at `(27, 6)` (`Caterpie Lv 11, Metapod Lv 11`) — Defeated (Turn 152). Wooden stairs across the `y = 7` ledge are at `(27, 7)`.
    - **Youngster #2**: Visible at `(22, 9)` facing Left (south of `y = 7` ledge).
    - **Lass #3**: Triggers at `(33, 8)` (`Jigglypuff Lv 14`) — Defeated (Turn 155; `NAUTILUS` reached Lv 17).
  - **East Exit to Route 4**:
    - From `(33, 8)` -> `(37, 8)` -> stairs at `(37, 7)` -> `(37, 4)` -> East along `y = 4` to `(49, 4)` -> South down stairs `(49, 7)` to `(49, 10)` -> East to `(56, 10)` -> `(56, 8)` -> `(59, 8)` -> North up stairs `(59, 7)` along `x = 59` to `(59, 0) -> Up`, which connects to **Route 4 `(9, 17)`**.

## Route 4 West (Outside Mt. Moon)
- **South Connection (from Route 3 `(59, 0)`)**: Enters at `(9, 17)` (dodge south ledges `(6, 15)..(9, 15)` via `x = 10..11` and `(7, 11)..(11, 11)` via `x = 12..13`).
- **Mt. Moon Pokémon Center**: Door at `(11, 5)` (settles last-visited heal checkpoint right outside Mt. Moon!).
- **Mt. Moon 1F Entrance**: Walk East along `y = 6` from `(11, 6)` to `(18, 6) -> Up` into `(18, 5)`.

## Mt. Moon 1F (`40 x 36`)
- **Entrance / Exit Mat**: `(14, 35)..(15, 35)` (stepping onto `(14, 35)` auto-warps back to Route 4 `(18, 6)`; entire column `x = 14, y = 24..35` is straight open floor).
- **Southwest Chamber (`TM12 Water Gun` & `Potion`)**:
  - From `(14, 35)` walk `Up * 7` to `(14, 28)` -> `Left * 9` to `(5, 28)`.
  - **`TM12 (Water Gun)`**: Item ball at **`(5, 32)`** — Collected (Turn 175; note: `Nidoran♀` is `NOT ABLE` to learn `TM12`, save for `Nidoqueen`!).
  - **`Potion`**: Item ball at **`(2, 20)`** (reached via `x = 5, y = 31 -> 20`, then `Left` to `(3, 20)`) — Collected (Turn 180).
  - **Bug Catcher Kent**: Stands at **`(7, 22)`** facing `Down` (`Weedle Lv 11, Kakuna Lv 11`) — Defeated (Turn 182).
- **Central Hall & Ladders**:
  - Signpost at `(15, 23)`; **Lass Iris** stands at **`(16, 23)`** facing `Down` (`Clefairy Lv 14`, defeated Turn 193).
  - Northward inner corridor at **`x = 20`** (`(20, 24) -> (20, 10)`).
  - **Ladder #2 (`(25, 15)`)**: Leads via B1F `(25, 15) -> (25, 27) -> (13, 27)` to B2F side pocket `(15, 27)` with Rocket Grunt #1 (`Sandshrew Lv 11, Rattata Lv 11, Zubat Lv 11`, defeated Turn 200) and raised-platform item ball at **`(25, 21)`** — Collected (Turn 202).
  - **East & North Outer Corridors**:
    - Reached via `(25, 12) -> (31, 12) -> (31, 11) -> (35, 11)`.
    - **`Escape Rope`**: Item ball at **`(36, 23)`** — Collected (Turn 207).
    - **`Rare Candy`**: Item ball at **`(35, 31)`** — Collected (Turn 208).
    - North wall runs clear along **`y = 2`** from `(35, 2)` past `(17, 2)`.
  - **Northwest Chamber (`Moon Stone` & Main Exit Ladder)**:
    - Reached via `(14, 2) -> (14, 16)` (Youngster Josh defeated Turn 219) -> `(14, 17) -> (3, 17) -> (3, 2)`.
    - **`Moon Stone`**: Item ball at **`(2, 2)`** — Collected (Turn 221).
    - **Hiker Marcos**: Stands at `(5, 6)` facing `Down` (bypassable from north).
    - **Main Exit Ladder (`(5, 5)`)**: Warps to B1F `(5, 5) -> (5, 17) -> (21, 17)` onto **Mt. Moon B2F Main Floor**.

## Mt. Moon B2F Main Floor
- **Entry Ladder (from B1F `(21, 17)`)**: Spawns at `(21, 17)`.
- **Verified East & South Ring to Fossil Corridor**:
  - `(21, 17) -> (23, 17) -> (23, 13) -> (27, 13) -> (27, 16) -> (32, 16)` (bypasses `(29, 17)` Rocket Grunt along `y = 16`) -> `(32, 12) -> (36, 12) -> (36, 24) -> (33, 24) -> (33, 32) -> (11, 32) -> (11, 19)` (Rocket Grunt #4 defeated Turn 233) -> `(12, 16) -> (12, 9) -> (13, 8)` (**Super Nerd Miguel**, defeated Turn 240).
  - **Fossils**: Dome Fossil at `(12, 6)`, **Helix Fossil** at **`(13, 6)`** — Claimed Helix Fossil (Turn 241).
  - **Exit to Route 4 East**: `(13, 7) -> (13, 4) -> (5, 4) -> (3, 4) -> (3, 6) -> (5, 7)` ladder -> B1F Exit Corridor `(23, 3) -> Right * 4 -> (27, 3)` -> warps outside to **Route 4 East `(24, 6)`**.

## Route 4 East (Mt. Moon Exit to Cerulean City)
- From `(24, 6)`: hop south ledge to `(24, 11)` -> East along `y = 11` to `(61, 11)` -> North to `(61, 8)` (clears top of `x = 62` bush column) -> East across `x = 62..89` into **Cerulean City `(0, 18)`** (verified Turn 245).


<hr>

<h1><code>Locations/ViridianCity</code></h1>

# Viridian City — Verified Coordinates & Landmarks

## Map Connections
- **South Exit (to Route 1)**: `x = 20..21, y = 35` -> `Down` warps to Route 1 `(10..11, 0)`.
- **West Exit (to Route 22)**: `y = 17, x = 0` (reached via `(19, 18) -> (4, 18) -> (4, 17) -> (0, 17)`) -> `Left` warps to Route 22 `(39, 9)`.
  - **Route 22 Safe East Grass**: `(39, 9) -> (35, 9) -> (35, 12) -> (33, 12) -> (33, 8..11)` (safely east of `x = 29` Rival 2 trigger; contains Spearow, Nidoran♀/♂, Rattata).
- **North Exit (to Route 2)**: Straight `Up` along `x = 18..19` from `(19, 18)` to `y = 0`.
- **South Entrance Ledge**: Row `y = 27`; northbound wooden bridge gap at `(19, 27)`; southbound hop available along `x = 20` (`(20, 26) -> (20, 28)`, completely unobstructed down column `x = 20` to `y = 35`).

## Key Buildings
- **Pokémon Center**: Door at `(23, 25)` (south road along `y = 26`).
- **Poké Mart**: Door at `(29, 19)` (reached via `(29, 26) -> (29, 20)` or `(27, 26) -> (27, 20) -> (29, 20)`).
  - Interior (`8x8`): Exit mat at `(3, 7)` and `(4, 7)` (Parcel cutscene leaves player at `(2, 5)`, requiring `Right` to `x = 3` before exiting `Down`).



<hr>

<h1><code>Mechanics/Harness</code></h1>

# Harness & Emulator Mechanics (Verified)

## Tool Sequencing (Verified Turns 2–4)
- Top-level tool calls execute sequentially in the order emitted.
- Calling `mcp_game_press_buttons` followed by `read_file` on `screenshots/latest.png` in the same turn reliably reads the newly settled screen produced at the end of `press_buttons`.

## Real-Time Emulation Clock (Verified Turn 3 `filmstrip_1.png`)
- The emulator runs continuously in real time during `[THINKING]` (observed `#01 +0.00s` -> `#03 +28.53s` in Turn 3).
- Implications:
  - Keep deliberation concise to avoid unnecessary real-time drift in areas with wandering NPCs.
  - Static menus, dialogue prompts, and battle command menus safely wait for input regardless of elapsed thinking time.

## Gen 1 Dialogue Safety
- Pressing `B` advances standard `▼` text boxes and accelerates text scrolling without accidentally confirming `YES/NO` prompts (defaults to `NO`/cancel) or list menus like `YOUR NAME?` that disallow `B` cancellation.

## Gen 1 Naming Screen Grid (Verified Turn 6)
9 columns (`0..8`) x 5 character rows (`0..4`), cursor starts at `(0, 0)` (`A`):
- Row 0: `A B C D E F G H I`
- Row 1: `J K L M N O P Q R`
- Row 2: `S T U V W X Y Z [space]`
- Row 3: `× ( ) : ; [ ] PK MN`
- Row 4: `- ? ! ♂ ♀ / . , ED` (where `(8, 4)` is `ED` = End/Confirm; Note: filling max length auto-jumps cursor to `ED`!)
- Row 5: `lower case` toggle across bottom row.
- Reusable Python generator (for names shorter than max length: <7 for trainer/rival, <10 for Pokémon):
```python
ROWS = ["ABCDEFGHI", "JKLMNOPQR", "STUVWXYZ "]
def name_buttons(word):
    cx, cy, seq = 0, 0, []
    for ch in word:
        for ry, r in enumerate(ROWS):
            if ch in r: tx, ty = r.index(ch), ry; break
        seq += (["Right"]*(tx-cx) if tx>cx else ["Left"]*(cx-tx))
        seq += (["Down"]*(ty-cy) if ty>cy else ["Up"]*(cy-ty)) + ["A"]
        cx, cy = tx, ty
    return seq + ["Right"]*(8-cx) + ["Down"]*(4-cy) + ["A"]
```

## Event & Fanfare Timings (Verified Turns 2–41)
- **ROM Variant**: Colorized Pokémon Blue enhancement with GBC palettes and a live blue EXP bar under player HP in battle (verified Turn 27). Maps, items, and encounters match Pokémon Blue.
- **Battle Move Cursor Memory**:
  - **New Battle (Turn 1)**: BOTH the top-level command menu (`►FIGHT`) AND the `FIGHT` move submenu (`►Slot 1`) **reset to Slot 1** at the start of every new battle (verified Turn 97 `filmstrip_1.png` — earlier assumption that `FIGHT` remembered across battles was false!).
  - **Same Battle (Turn 2+)**: Within the same battle, the top-level command menu, `FIGHT` submenu, and `ITEM` submenu all remember their last selected positions (verified Turns 21, 67, 73).
  - *(Tip — Verified `Select` Swap Mechanics, Turns 110, 121, 125)*:
    - In the **`FIGHT` move menu**, `Select -> Down * k -> Select` swaps Slot `k` into Slot 0 and **automatically resets the cursor onto Slot 0** (and note: `FIGHT` wraps vertically, so pressing `Up` from Slot 0 wraps to the bottom move!).
    - In the **`ITEM` bag menu**, `Select -> Down * k -> Select` leaves the cursor at Slot `k`; always verify the highlighted item before pressing `A` after reordering items.
  - In `SHIFT` trainer battles, `B`-clearing between attack rounds safely declines `"Will COBALT change POKéMON?"` (`NO`). Use 8–10 `B` presses (`"sleep 650"`) per round when stat-drop or poison ticks occur (Turns 83, 95).
- **Catching & Nickname Safety (Verified Turns 66–75, 173–175, 230)**:
  - Never spam `B` after throwing a Poké Ball (`B` cancels `"give a nickname?"` as `NO`). Wait `"sleep 9500"` after throwing a Ball to inspect catch outcome.
  - Once `"All right! <POKEMON> was..."` appears, wait `"sleep 5500"` + `A` -> `"will be added for <POKEMON>!"`, then `["A", "sleep 2500", "A", "sleep 1200", "A", "sleep 1800", "A", "sleep 1200"]` lands directly on `"give a nickname?"` `►YES / NO`.
- **High-Density Cave Chunking & NPC Facing (Verified Turns 213, 228)**:
  - High-encounter floors (e.g., Mt. Moon B2F) trigger wild battles every ~6–8 steps; cap `run_code` cave marches at **18–20 steps max** so wild-flee animations never approach the 120s script timeout.
  - Rocket Grunts showing a solid horizontal orange stripe across the back of a black cap are facing **Up** (not Down).
- **Evolution `B`-Cancel Warning & Verified Safe Evolution Recipe (Verified Turn 146)**:
  - Pressing `B` during a post-battle evolution animation (`"What? <POKEMON> is evolving!"`) **cancels the evolution** in Gen 1!
  - Evolution ONLY triggers **after the entire battle ends** (never mid-battle when KOing an earlier trainer Pokémon, and never if the evolving Pokémon faints before the battle ends).
  - Verified recipe when KOing the final opposing Pokémon on an evolution battle: execute the attack (`["A", "sleep 400", "A", "sleep 3500"]`), then use **ONLY `A`** (`["A", "sleep 1100"] * 6 + ["A", "sleep 10000", "A", "sleep 6000", "A", "sleep 1500", "A", "sleep 1500"]`) — `A` advances victory dialogue without ever cancelling evolution.
- **Gen 1 Battle Quirks (Verified Turns 137–139)**:
  - `Bubble` is 20 BP (half of `Water Gun`'s 40 BP), and 100%-accurate moves in Gen 1 still have a `1/256` miss chance (observed on `Water Gun` in Turn 139 `filmstrip_1.png` `#18`). Always verify KO outcomes before assuming fixed hit counts.
- **Coordinate Behavior in Battles & Warps**:
  - `mgba.get_coordinates()` continues returning the underlying overworld `(x, y)` during battles (`<GameState>` omits `<Position>` when in battle).
  - Step-by-step `before == after` comparison reliably detects wild encounters in tall grass; following a blocked grass step with `["sleep 800", "B"] * 8` (~6.4s) lands cleanly on `►FIGHT`.
  - Door warps have a ~0.5s white fade; ending a script immediately on a door step can capture the white transition frame before indoor coordinates update (Turn 41). Call `tools.observe()` or include a short post-warp settle when inspecting a new room.
- **Title Screen**: Pressing `Start` during a starter sprite swap is ignored; wait or append `"sleep 1500"` for the starter cry to finish before Main Menu input.
- **Pokémon Obtained Fanfare**: Lasts ~4.5 seconds before `"received a <POKEMON>!"` accepts `A`/`B` dismissal (`"sleep 3500"` was slightly early in Turn 18).
- **Cutscene Clearing**: Spacing `B` presses with `"sleep 700"`–`"sleep 900"` safely clears multi-box dialogues and lands cleanly on `►FIGHT` (in battles) or `YOUR NAME?` without triggering unwanted `YES` confirmations or attacks.

## Poké Mart & Pokémon Center Recipes (Verified Turns 52–62)
- **Poké Mart Buying (Requires THREE `A`s after Quantity!)**:
  1. Select item with `A`, `"sleep 900"` -> opens `×01` (`Up` increments quantity).
  2. `A` #1 (`"sleep 900"`) -> `"<ITEM>? ▼"`
  3. `A` #2 (`"sleep 900"`) -> `"That will be ¥<PRICE>. OK?"` `►YES / NO`
  4. `A` #3 (`"sleep 900"`) -> `"Here you are! Thank you! ▼"` (always verify `MONEY` box decreased before pressing `B`!).
  *(Misstep fixed in Turn 62: pressing only two `A`s before `B` cancels `YES/NO` as `NO`.)*
  - **Pokémon Center Nurse Joy (`(3, 3)` facing `Up` — Max `sleep 10000` Cap, Poison-Faint Guard & Verify!)**:
  - **CRITICAL**: `"sleep <ms>"` has a strict **10,000 ms maximum** (`"sleep 10500"` / `"sleep 11500"` rejects the entire `press_buttons` call — root cause of failed heals in Turns 259 & 266!). To wait ~12s for a 4–6 Pokémon heal jingle without consecutive sleeps, use `"A", "sleep 9500", "B", "sleep 2500"`.
  - **Overworld Poison-Faint Edge Case (Turn 290)**: Poison ticks 1 HP every 4 steps; if a poisoned Pokémon hits `0` HP on the exact step onto `(3, 3)`, `"<POKEMON> fainted!"` opens and consumes the 1st `"A"`, causing the 5th `"A"` to stop on `►HEAL / CANCEL` where `"B"` cancels! Always visually verify green HP bars in `Start -> POKéMON` after healing.
  - After arriving cleanly at `(3, 3)` from `(3, 4)` + `"sleep 500"`, run `["A", "sleep 1000"] * 4 + ["A", "sleep 9500", "B", "sleep 2500"]` followed by `["B", "sleep 700"] * 3` and `Down * 5` (`(3,3) -> (3,7) -> outside`).
- **4-Move TM / Level-Up Move Replacement Sequence (Verified Turns 235–237)**:
  - Prompts: `"trying to learn <NEW>! ▼"` -> `"can't learn more than 4 moves! ▼"` -> `"Delete an older ▼"` -> `"move to make room for <NEW>?"` (`►YES / NO` — note the TWO line-scrolls!) -> `"Which move should be forgotten?"` (`Down * k`, `A`) -> `"1, 2 and... Poof! ▼"` -> `"forgot <OLD>! ▼"` -> `"And... ▼"` -> `"learned <NEW>! ▼"`.
- **Cave Exit Mats vs. Building Exit Mats (Verified Turn 187)**:
  - Cave exit mats (e.g., Mt. Moon 1F `(14, 35)`) warp **immediately upon stepping onto the tile**, whereas building exit mats (e.g., Pokémon Center `(3, 7)`) require pressing `Down` while standing on the mat.
- **Multi-Round Battle Loop Pitfalls & Timeout Guardrails (Verified Turns 181–186, 198)**:
  - Cap automated battle loops in `mcp_game_run_code` at **3–4 rounds max (~40–55s)** so slow enemy moves/status text never approach the 120s script wall-clock timeout.
  - If the lead Pokémon faints during an automated `["A", "A", "B"*8]` battle loop, `"Use next POKéMON?"` opens the Party list where `A` sends out Slot 1 (or repeats `"There's no will to fight!"` if cursor is on the fainted Pokémon).
  - **Safe Switch-Training**: Always place the low-level trainee in Slot 0 *before* battle and switch *out* on Turn 1 (zero damage taken by trainee), rather than switching a frail trainee *in* mid-battle into an incoming attack.
- **Ladder `back_d` Pitfall & `known_open_move` (Verified Turns 202–205)**:
  - Never run a `back_d` wall-probe when standing 1 tile off a ladder warp (`back_d` steps right back onto the ladder and re-warps floors!). First step 2+ tiles clear of any ladder using `known_open_move` (which flees wild encounters in place without stepping backward).

## Navigation Scripting Guardrails & Cave Primitives (Verified Turns 53, 60, 152, 165–166)
- Always use bounded `for _ in range(N):` loops rather than unbounded `while` loops so an unexpected wall/NPC cannot trip the 150-button script abort limit.
- Never dodge `Down` when walking directly above a south-facing ledge (e.g., Viridian `y = 26`).
- **Gen 1 Menu Wrapping Summary (Verified Turns 124, 155, 184)**:
  - `Start` menu (`POKéDEX .. EXIT`) **wraps** vertically (`Up` from `POKéDEX` jumps to `EXIT`, `Down` from `EXIT` jumps to `POKéDEX`). Fighting a battle resets `Start` back to Slot 0 (`POKéDEX`, verified Turn 290), whereas healing at Nurse Joy without a battle leaves `Start` on its previous slot (Turn 270).
  - `POKéMON` party list remembers its last cursor slot in overworld `Start -> POKéMON`, **EXCEPT at the start of every new battle**, where in-battle `PKMN` **resets to Slot 0** just like `FIGHT` (verified Turn 280! Thus Turn-1 switch from Slot 0 to Slot 1 in a new battle is ALWAYS `Right, A, Down, A, A`). Within the same battle, selecting Slot `k` via `PKMN` OR `"Use item on which POKéMON?"` updates the in-battle Party cursor to Slot `k` (verified Turn 287).
  - **Verified Direct-Talk Trainer Intro Recipe (13.5s, Turn 280)**: Talking to a trainer with `A` takes ~12.6s to reach `►FIGHT` (shorter sleeps drop Turn-1 switch inputs during `"Go! <PKMN>!"`, Turn 277). Use `["A", "sleep 1000", "B", "sleep 1000", "B", "sleep 4000", "B", "sleep 1200", "B", "sleep 2500", "B", "sleep 3000", "B", "sleep 800"]` to land cleanly on `►FIGHT`.
  - Battle `FIGHT` move menu **wraps** vertically.
  - `ITEM` bag menu **clamps** (does NOT wrap) at Slot 0 (`Up` at top stays on Slot 0). Using an overworld Bag item without evolution keeps the Bag cursor on the same slot, whereas **any item-triggered evolution (`Rare Candy` or `Moon Stone`) auto-returns to the Bag after the fanfare and resets the Bag cursor to Slot 0** (verified Turns 326 & 328).
  - Battle 2x2 command menu (`FIGHT / PKMN / ITEM / RUN`) **clamps** (`Left, Up` always lands on `►FIGHT`). Probing `Left` or `Up` onto a known-open overworld tile after an attack round is a **100% pure no-op** if still on `►FIGHT` (no restore press needed!).
  - The 2x2 battle command menu (`FIGHT / PKMN / ITEM / RUN`) does **not** wrap, so `["Left", "sleep 150", "Up", "sleep 150"]` deterministically resets the cursor to `►FIGHT` from any quadrant, and pressing `Left` or `Up` while already on `►FIGHT` is a pure no-op in battle.
  - When a step `d` from `b` fails (`after == b`), clearing potential battle intro (`["sleep 1200"] + ["B", "sleep 700"] * 8`) and probing `back_d` (the known-open tile you just came from) cleanly distinguishes a **wall** (`pos != b`) from an active **battle** (`pos == b`), and in Gen 1 `PlayerSpeed >= EnemySpeed` guarantees 100% first-try escape via `RUN`.





<hr>

<h1><code>Scratchpad/Routing</code></h1>

# Active Routing & Immediate Checklist

## Cerulean City -> Route 24/25 -> Cascade Badge -> Vermilion City
1. **Badge Guy Backyard (`(9, 11)`)**:
   - Exit north back door into fenced backyard -> pick up **Hidden Rare Candy #2** (`Rare Candy x2` total in Bag!).
   - Return through Badge Guy's house to `(9, 12)` -> walk east to `(20, 12)` -> north onto **Route 24 (`x = 10`)**.
2. **Nugget Bridge Switch-Training (`AMETHYST` Slot 0 -> `NAUTILUS` Slot 1)**:
   - Note: `POKéMON` cursor is pre-positioned on Slot 1 (`NAUTILUS`)! On `NAUTILUS`'s next `FIGHT` menu, swap `WATER GUN` (Slot 1) to Slot 0 (`Select, Down, Select`) so 100%-accurate `Water Gun` is Slot 0 and 80-BP `Mega Punch` is Slot 1.
   - Defeat Trainers #2–#5 + Rocket Grunt (`Nugget` worth ¥5,000!) along `x = 10`:
     - #2 Lass (`Pidgey Lv 14, Nidoran♀ Lv 14`)
     - #3 Youngster (`Rattata Lv 14, Ekans Lv 14, Zubat Lv 14`)
     - #4 Lass (`Pidgey Lv 16, Nidoran♀ Lv 16`)
     - #5 Jr. Trainer♂ (`Mankey Lv 18`)
     - #6 Rocket Grunt (`Ekans Lv 15, Zubat Lv 15` — awards `Nugget` first)
   - Grab `TM45 (Thunder Wave)` on NW plateau of Route 24 if convenient.
3. **Route 25, Sea Cottage (`S.S. TICKET`), & Nidoqueen Power Spike**:
   - Switch-train `AMETHYST` across Route 25 trainers until **Level 14** (remember `NAUTILUS` learns **Bite** at Lv. 24 — replace `Bubble` or `Tackle`!).
   - At **Level 14**, use **`Rare Candy x2`** -> `AMETHYST` evolves into **Nidorina** at Lv. 16 -> use **`Moon Stone`** -> evolves into **Nidoqueen** -> teach **`TM12 (Water Gun)`**!
   - Enter **Sea Cottage** -> help **Bill** (`YES` = `A`, then check PC, then talk to Bill) -> obtain **`S.S. TICKET`**.
4. **Cerulean Gym & `TM28 (Dig)`**:
   - Heal at Cerulean Pokémon Center `(19, 17)`.
   - Sweep **Cerulean Gym** (`Misty`: `Staryu Lv 18, Starmie Lv 21` using `Mega Punch` / `Bite` + `Nidoqueen`) -> **Cascade Badge** + `TM11 (BubbleBeam)`.
   - Enter burgled house `(27, 11)` -> defeat Backyard Rocket -> obtain **`TM28 (Dig)`** (teach to **Nidoqueen** for 100-BP STAB Ground!).
   - Head south down Route 5 (`Underground Path`) -> Route 6 -> **Vermilion City** (`S.S. Anne` for `HM01 Cut` -> Lt. Surge).


<hr>