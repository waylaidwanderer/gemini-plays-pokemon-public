<h1><code>Main</code></h1>

# Pokémon Blue Version — Main Dashboard

## Run Overview
- **Game:** Pokémon Blue Version (Generation I, GBC-colorized QoL variant)
- **Trainer Name:** COBALT
- **Rival Name:** GARNET
- **Starter:** Squirtle (Nickname: `NAUTILUS`, evolved into Wartortle at Lv. 16, evolved into Blastoise at Lv. 36!)

## Milestones & Badges
- [x] Starter Pokémon & Pokédex (Pallet Town / Viridian City)
- [x] Boulder Badge — Brock (Pewter City)
- [x] Mt. Moon Cleared (`Helix Fossil`, `Moon Stone`, `TM01 Mega Punch`, `TM12 Water Gun`)
- [x] Cerulean Rival `GARNET` Defeated (Turn 257)
- [x] `S.S. Ticket` Obtained from Bill (Sea Cottage, Turn 343)
- [x] Cascade Badge — Misty (Cerulean City, Turn 351)
- [x] S.S. Anne Cleared — Rival `GARNET` Defeated & `HM01 (Cut)` Obtained (Turns 432–434)
- [x] Thunder Badge — Lt. Surge (Vermilion City, Turn 449)
- [x] Rainbow Badge — Erika (Celadon City, Turn 753)
- [x] Pokémon Tower Cleared & `Poké Flute` Obtained (Lavender Town, Turn 807)
- [ ] Soul Badge — Koga (Fuchsia City)
- [ ] Marsh Badge — Sabrina (Saffron City)
- [ ] Volcano Badge — Blaine (Cinnabar Island)
- [ ] Earth Badge — Giovanni (Viridian City)
- [ ] Indigo Plateau — Elite Four & Champion

## Active Party
1. **NAUTILUS** (Blastoise) — Lv. 39 (`118/118` HP) | Moves: BubbleBeam (Slot 0), Ice Beam (Slot 1), Dig (Slot 2), Bite (Slot 3) *(Note: abandon `Skull Bash` at Lv. 42 with `["B", "sleep 1500", "A", "sleep 1500"]`)*
2. **AMETHYST** (Nidoqueen) — Lv. 27 (`90/90` HP) | Moves: Body Slam, Water Gun, Tackle, Thunderbolt *(100% Electric-immune! 85-BP `Body Slam` + 95-BP `Thunderbolt`!)*
3. **CELESTE** (Clefairy) — Lv. 8 (`30/30` HP) | Moves: Pound, Growl *(1% Mt. Moon 1F catch; `HM04 Strength` compatible)*
4. **AMBER** (Paras) — Lv. 12 (`32/32` HP) | Moves: Scratch, Cut *(`HM01 Cut` & `Spore` specialist)*
5. **JASPER** (Spearow) — Lv. 22 (`52/52` HP) | Moves: Growl, Fly, Fury Attack, Mirror Move *(`HM02 Fly` aerial partner)*

## Inventory & Money
- Money: ~¥10,000+
- Key Items: Pokédex, Silph Scope, Bicycle, HM01 (Cut), HM02 (Fly) *(Town Map, Helix Fossil, S.S. Ticket, Lift Key, TM30, TM34, TM45 stored in COBALT's PC)*
- Bag (`15/20` slots):Max Ether x1, HM01 (Cut), Poké Ball x4, Bicycle, Fresh Water x1 *(save for Saffron Gatehouse!)*, HM02 (Fly), Silph Scope, Super Potion x7, Awakening x7, X Speed x8, X Defend x12, TM21 (Mega Drain), Elixer x1, X Accuracy x1

## Notepad Index
- `notepads/Main.md` — High-level dashboard & party summary
- `notepads/Scratchpad/Routing.md` — Active route planning & immediate checklists
- `notepads/Mechanics/Harness.md` — Verified harness timing & input behavior
- `notepads/Locations/` — Verified town, route, and dungeon notes (`Route9_RockTunnel.md`, `Lavender_Route8.md`, `CeladonCity.md`)


<hr>

<h1><code>Locations/CeladonCity</code></h1>

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
- **Cerulean Bike Shop**: Door at **`(13, 25)`** (`(2, 7)` indoors -> `(4, 7) -> (4, 4) -> (6, 4)` facing `Up` at counter `(6, 3)` -> exchanged `Bike Voucher` for **`BICYCLE`** Turn 464).
- **South `Cut` Bush (to/from Route 5 & Route 9)**: Located at **`(19, 28)`** (`Route 5 x = 15` north enters at `(25, 35) -> (25, 31) -> (19, 31) -> (19, 29)` facing `Up` at `(19, 28)`).
- **East Exit (to Route 9, Verified Turn 468)**: Chop `(19, 28)` from `(19, 27)`, walk `(19, 31) -> (36, 31) -> Up * 15` up the **`(36, 19)`** wooden stairs to `(36, 16)`, then `Right` onto **Route 9 `(0, 8)`**.
- **Cerulean Gym (Misty)**: Door at **`(30, 19)`** (warps indoors to `(4, 13)`; Swimmer Luis spots at `(5, 7)`, Jr. Trainer♀ Diana spots at `(5, 3)`, **Gym Leader Misty** at **`(4, 2)`** — Defeated Turn 351 for **Cascade Badge** + `TM11 BubbleBeam`).
- **Burgled House (`TM28 Dig` & South Bypass)**: Front door at **`(27, 11)`** (`(2, 7)` indoors -> walk around table `(7, 3) -> (7, 1) -> (3, 1) -> Up` out north wall hole `(3, 0)` to `(27, 9)`); Backyard Rocket at `(30, 8)` defeated Turn 356 for **`TM28 (Dig)`**; corridor at **`x = 33`** leads south around Cerulean City to **Route 5**.

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
- **Bill's Sea Cottage**: Door at **`(45, 3)`** (`(2, 7)` indoors; Clefairy-Bill wanders near `(6, 5)` — answer `YES` with `A` only, then operate PC at `(1, 5)` facing `Up`, then talk to Human Bill at `(4, 4)` for **`S.S. Ticket`**).
- **Southern Return Bypass (Sea Cottage -> Cerulean)**: Exit `(45, 4) -> Down * 8` across wooden bridge to `(45, 12) -> Left * 51` along `y = 11` onto **Route 24 `(14, 11)`** -> straight `Down * 25` to **Cerulean City `(24, 12)`** (100% wild-free & trainer-free!).
- **Express Cerulean <-> Route 25 Corridor**: `(19, 18) <-> (8, 19) <-> (8, 12) <-> (20, 12) <-> Route 24 (10, 35) <-> zigzag x=10/11 <-> (10, 8) <-> Route 25 (9, 8) <-> (9, 4) <-> (17, 4)` (100% wild-free & trainer-free).


<hr>

<h1><code>Locations/FuchsiaCity</code></h1>

# Cycling Road (`Routes 16–18`) & Fuchsia City — Verified Notes

## Cycling Road Express Route (Verified Turns 823–835)
- **Route 16 Snorlax `(26, 10)`**: `Poké Flute` (`A, A` for `USE`) wakes Lv. 30 `Snorlax` (~9s melody); flee and enter **Lower Route 16 Gatehouse at `(23, 10)`** -> spawns at `(7, 8)` -> exits west to `Route 16 (17, 10)` on Bicycle.
- **Route 17 Downhill Express**:
  - Defeat Cue Ball Luke (`(11, 10)`), Cue Ball Koji (`(8, 10)`), and Biker Lao (`(8, 11)`), then slide straight south down **`x = 8`** all the way to **`(8, 87)`** with **zero trainers**!
  - Shift `Left` onto **`x = 4..5`** (`Biker Billy at `(5, 98)` has `Grimer, Muk Lv 29`) and slide south to **`(4, 122)`**.
  - Pass through the south bollard gap at **`(6..7, 123)`** onto **`Route 18 (7, 0)`**, ride `Down` along `x = 13` to `(13, 9)`, and ride `Right` along **`y = 9`** through the **Route 18 Gatehouse** (`auto-dismounts Bicycle`) into **`Fuchsia City (3, 17)`**.

## Fuchsia City Landmarks & `Cut` Shortcuts (Verified Turns 836–855)
- **Fuchsia Poké Mart**: Door at **`(5, 13)`** (`sells Ultra Ball ¥1200, Great Ball ¥600, Super Potion ¥700, Revive ¥1500, Full Heal ¥600, Super Repel ¥500`).
  - Reachable via **`Cut` bush at `(18, 19)`** (`from (18, 20) -> Up -> (18, 14) -> Left * 13 -> (5, 14)`) or **`Cut` bush at `(26, 13)`**.
- **Safari Zone Reception Gatehouse**: Door at **`(18, 3)`** (`from (18, 8)`, walk `Right * 4` to `(22, 8)`, chop **`Cut` bush at `(22, 7)`**, then `(22, 6) -> (18, 6) -> (18, 3)`; tollbooth at `(3, 2)` costs ¥500 for 500 steps; note Safari Zone adds `500/500 / BALL×30` box and resets `Start` cursor to `POKéDEX`).
  - **Center**: Spawns at `(15, 25)`; East gate to **Area 1** is at **`(29, 10..11)`** -> spawns at **`Area 1 (0, 22)`**.
  - **Area 1 (East, Verified Turns 868–871 — 56-Step Express!)**: From `(0, 22)`, walk `Right * 8` to `(8, 22)`, `Up * 14` straight up `x = 8` to `(8, 8)`, `Right * 4` to `(12, 8)`, bridge over the `(14..15, 8..9)` tree via **`(12, 8) -> Up * 2 -> Right * 5 -> Down * 2 -> (17, 8)`**, then **`Right * 3 -> (20, 8) -> Up * 5 -> (20, 3) -> Left * 12 -> (8, 3) -> Down * 2 -> (8, 5) -> Left * 8 -> (0, 5)`** -> warps to **`Area 2 (39, 31)`**! *(Optional `Max Potion` at `Area 1 (3, 7)`.)*
  - **Area 2 (North, Verified Turns 872–877 — 98-Step Express!)**: From `(39, 31)`, walk `Left * 17` -> `(22, 31)` -> `Up * 9` (climbs `(22, 23)` stairs) -> `(22, 22)` -> `Left * 6` -> `(16, 22)` -> `Down * 8` (descends `(16, 27)` stairs) -> `(16, 30)` -> `Left * 3` -> `(13, 30)` -> `Up * 13` -> `(13, 17)` -> `Left * 7` -> `(6, 17)` -> `Down * 6` -> `(6, 23)` -> `Left * 4` -> `(2, 23)` -> `Down * 13` -> **`(2, 35)`** -> warps to **`Area 3 (26, 0)`**!
- **Safari Warden's House (`HM04 Strength`)**: Door at **`(27, 27)`**.
- **Fuchsia Pokémon Center**: Door at **`(19, 27)`** (`Fuchsia Gym` is west of it at `(5, 27)`).


<hr>

<h1><code>Locations/Lavender_Route8</code></h1>

# Route 10 South, Lavender Town & Route 8 — Verified Coordinates

## Route 10 South -> Lavender Town (Verified Turns 574–577)
- **Rock Tunnel South Exit**: `Rock Tunnel 1F (15, 33)` warps outside to **`Route 10 South (8, 54)`** *(Jr. Trainer♀ Heidi stands at `(7, 54)` facing `Down`)*.
- **Zero-Battle Path to Lavender Town**:
  1. Walk east `Right * 6` from `(8, 54)` -> `(14, 54)` and south `Down * 9` -> `(14, 63)`.
  2. **Pokémaniac Herman** stands at `(14, 64)` facing `Left`; slip behind his back via **`(15, 63) -> (15, 65) -> (11, 65)`**.
  3. Hop the south-facing ledge at **`(11, 67)`** -> `(11, 69)`, step west to `(9, 69)`, and walk south down `x = 9` into **`Lavender Town (9, 0)`**.

## Lavender Town (Verified Turns 577–579)
- **North Entrance**: `(9, 0)` (from Route 10).
- **Lavender Pokémon Center**: Door at **`(3, 5)`** *(Note: watch for wandering villager around `(7, 6..7)` when walking west along `y = 6`; verify `mgba.get_coordinates() == {'x': 3, 'y': 7}` upon entering)*.
- **Pokémon Tower**: East side `(12..17, 0..5)`, door at **`(14, 5)`**.
  - **1F**: Spawns at `(10, 17)`; walk `Up * 8` to `(10, 9)` and `Right * 8` onto **`(18, 9)`** -> **2F `(18, 9)`** *(use `"sleep 900"` on Tower stairs before menu inputs)*.
  - **2F**: **Rival `GARNET`** triggers at **`(15, 5)`** (`Pidgeotto Lv 25`, `Gyarados Lv 23` [**knows `Hydro Pump`** — keep Water-resistant `NAUTILUS` in rather than switching Ground-type `AMETHYST` into it!], `Growlithe Lv 22`, `Kadabra Lv 20`, `Ivysaur Lv 25`). West stairs to **3F** at **`(3, 9)`**.
  - **3F**: From `(3, 10)`, route `(5, 10) -> (5, 13) -> (8, 13) -> (8, 11) -> (13, 11) -> (13, 6) -> (17, 6) -> (17, 9) -> (18, 9)` -> **4F `(18, 9)`**.
  - **4F**: **`Elixer`** item ball at **`(12, 10)`**! Route `(14, 9) -> (14, 8) -> (11, 8) -> (11, 9) -> (10, 9) -> (10, 12) -> (7, 12) -> (7, 8) -> (3, 8) -> (3, 9)` -> **5F `(3, 9)`**.
  - **5F (Verified Turns 778–782)**: **Purified Healing Zone** around **`(10..11, 8..10)`** (`(11, 9)` heals entire party HP/PP + revives fainted Pokémon with zero wild encounters!). Stairs to **6F** on east wall at **`(18, 9)`**.
  - **6F (Verified Turns 784–796)**: **`X Accuracy`** item ball at **`(14, 14)`**, **`Rare Candy`** item ball at **`(6, 8)`**. Stepping onto **`(10, 16)`** triggers the restless **Lv. 30 `Marowak`** (`Silph Scope` unveils; cannot be caught, defeated Turn 796). Stepping `Left` from `(10, 16)` onto **`(9, 16)`** climbs to **7F `(9, 16)`**.
  - **7F (Verified Turns 796–807)**: Step `Right` from `(9, 16)` to `(10, 16)` and walk straight north up `x = 10` through the 3 Team Rocket Grunts (`Grunt #1` at `y = 11`, `Grunt #2` at `y = 9` [`Koffing, Drowzee` — OHKO `Drowzee` with `Dig`], `Grunt #3` at `(9, 7)` facing `Right`). **Mr. Fuji** stands at `7F (10, 3)`; talking to him warps to **Volunteer House `(3, 7)`**, where Mr. Fuji stands above the table at **`(3, 1)`** *(NOT `(6, 3)`, which is a little girl)* to give **`POKé FLUTE`** (`exits to Lavender Town (7, 10)`).
- **West Exit to Route 8**: Walk west along `y = 8..9` (`x = 0 -> Route 8 (59, 8)`).

## Route 8 (East -> West, Verified Turns 579–588)
- Enters from Lavender Town at **`Route 8 (59, 8)`**; upper `(53, 4)` is a closed flower alcove.
- Drop south through the fence gate at **`(54..55, 10)`** to **`y = 14`** and head west:
  - **Gambler Rich** (`Growlithe Lv 24, Vulpix Lv 24`): stands at `(46, 13)` facing `Down` across the fence and spots `(46, 14)` (defeated Turn 583).
  - At **`x = 42..43`**, the paved avenue turns north (`y = 14 -> y = 4..5`):
    - **Super Nerd Glenn** (`Grimer Lv 22, Muk Lv 22, Grimer Lv 22`): stands at `(42, 6)` facing `Up` and spots `(42, 4)` (Turns 584–588; note `Muk` & `Grimer` carry `Disable`, so wrap to a secondary move if `Slot 0` gets Disabled!).
  - Continue west along `y = 4` to **`(29, 4)`** (4-Trainer Wall):
    - **Super Nerd Leslie** (`Koffing Lv 26`) stands at `(26, 4)` facing `Right` and walks to `(28, 4)` (defeated Turn 590; `NAUTILUS` reached Lv. 33).
    - Step south to `(29, 5)`, west to `(27, 5)` *(trainer at `(26, 5)` faces `Left`!)*, and south down **`x = 27`** (**Lass Megan** at `(26, 6)`: `5x Lv 19` Pokémon, defeated Turn 593) to `(27, 14)`.
  - Walk west along `y = 14` to `(12..14, 14)`, bypass **Gambler Stan** (`(13, 9)` facing `Up`) via **`x = 14`**, and enter the **Underground Path (7–8) East Gatehouse at `(13, 3)`** (`indoor stairs at (4, 4)`).
- **Underground Path (7–8) & Route 7 -> Celadon City (Verified Turns 596–600)**:
  - Tunnel runs from **`(47, 2)`** (east) to **`(2, 4)`** (west stairs -> Route 7 Gatehouse `(4, 4)` -> exits to `Route 7 (5, 14)`).
  - On **Route 7**: walk around the east side of the gatehouse (`x = 8`) to `(4, 8)`, climb the **wooden stairs at `(4, 7)`** onto the upper plateau `(4, 3)`, and walk west (`x = 0, y = 3`) into **`Celadon City (49, 11)`**.


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

<h1><code>Locations/Route9_RockTunnel</code></h1>

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
- **B1F Section 1 (Southeast -> North, Verified Turns 499–520)**:
  - Arrives at **`B1F (33, 25)`**; follow corridor south/west around `(28..33, 25..33)` to **`(26, 33)`**.
  - **Pokémaniac Winston** (`Slowpoke Lv 25`): stands north of `(26, 33)` (`~(26, 30)` facing `Down`, defeated Turn 504).
  - Walk west along `y = 33` to `(14, 33)`, step to `x = 15`, and head north:
    - **Jr. Trainer♀ Sofia** (`Oddish Lv 22, Bulbasaur Lv 22`): stands at **`(14, 28)`** facing `Right` (defeated Turn 508).
    - At `(15, 24)` (`y = 22..23` wall), jog east to `x = 20..23`: **Pokémaniac Steve** (`Charmander Lv 22, Cubone Lv 22`) stands at **`(20, 21)`** facing `Right` (defeated Turn 513).
    - At `(23, 16)` (`y = 14..15` wall), step to `y = 17`, walk east to `x = 32`, north to `(32, 10)` *(trainer at `(30, 10)` bypassed via east side `x = 34`)*, north to `(34, 5)` (**Hiker Eric**: `Machop Lv 20, Onix Lv 20`, defeated Turn 520), then via `(35, 3)` west onto **Ladder #2 at `B1F (27, 3)`** -> warps to **`1F (5, 3)`**!
- **1F Section 2 (Northwest -> Center, Verified Turns 520–525)**:
  - Arrives at **`1F (5, 3)`** *(correction: earlier scratchpad guessed `B1F (27, 3)` led to `1F (17, 11)`, whereas `1F (17, 11)` is actually **Ladder #3** at the end of 1F Section 2!)*.
  - Walk south down `x = 3..5` (`Hiker` at **`(5, 16)`** facing `Down`, `3` Rock Pokémon, defeated Turn 525) to `(5, 18)`, east to `(17, 18)`, north via `x = 15` (**Hiker Lucas** at **`(17, 15)`** facing `Left`: `Geodude Lv 21, Graveler Lv 21`, defeated Turn 527) to `(15, 11)`, and east onto **Ladder #3 at `1F (17, 11)`** -> warps down to **`B1F (23, 11)`**.
- **B1F Section 2 (Northwest Maze -> Ladder #4, Verified Turns 527–545)**:
  - Arrives at **`B1F (23, 11)`**; walk west to `(14, 11)` *(north `(14, 3)` is a dead end)*, south via `x = 15` around the `x = 12..13` wall to **`(11, 15)`** (**Jr. Trainer♀ Martha**: `Jigglypuff Lv 21, Pidgey Lv 21, Meowth Lv 21`, defeated Turn 535; `NAUTILUS` hit Lv. 30).
  - Note: `(8, 3)` north and `(3, 24)` southwest are dead ends; the **true passage through the `x = 6..7` wall is the gap at `y = 10..12` (`(6..7, 11)`)**!
  - Walk north from `(11, 15)` to `(9, 11)`, west to **`(6, 11)`** (**Hiker Dudley** stands at **`(6, 10)`** facing `Down`: `Geodude Lv 21 x2, Graveler Lv 21`, defeated Turn 540), west to `(3, 11)`, and north along `x = 3` toward **Ladder #4 (`B1F (3, 3)`)**:
    - **Pokémaniac Cooper** (`Slowpoke Lv 20 x3`) triggers at **`(3, 8)`** *(Engine note: if `"REPEL's effect wore off."` triggers on the same step as a Trainer sightline, dismissing the Repel box immediately starts the queued Trainer walk-up before `Start` can open!)*.
  - **Ladder #4**: **`B1F (3, 3)`** -> warps up to **`1F (37, 17)`** (`1F Section 3`, Southeast -> Southwest Exit).
- **1F Section 3 (Southeast -> South Exit, Verified Turns 550–566)**:
  - Arrives at **`1F (37, 17)`**; walk south along `x = 35`:
    - **Jr. Trainer♀ Leah** (`Bellsprout Lv 22, Clefairy Lv 22`) triggers at **`(35, 21)`** (defeated Turn 561).
    - **Jr. Trainer♀ Ariana** (`Pidgey Lv 19, Rattata Lv 19 x2, Bellsprout Lv 19`) triggers at **`(35, 24)`** (defeated Turn 568); walk south to `(33, 29)`, west to `(26, 29)`, north to `(26, 26)`, and west along `y = 26`:
    - **Jr. Trainer♀ Dana** (`Meowth Lv 20, Oddish Lv 20, Pidgey Lv 20`) stands at **`(22, 25)`** facing `Down` (defeated Turn 573).
    - Continue west to `(15, 26)` and walk south onto the **Rock Tunnel South Exit mat at `1F (15, 33)`** -> warps outside to **`Route 10 South (8, 54)`** (Turn 574)!


<hr>

<h1><code>Locations/SaffronCity</code></h1>

# Saffron City — Verified Coordinates & Notes

## Access & Landmarks (Verified Turns 810–814)
- **West Saffron Gatehouse (`Route 7 -> Saffron City`)**:
  - On `Route 7`, brown bollards block `(11, 8..9)`; enter the gatehouse via the **`y = 10` lane (`(10, 10) -> (11, 10) -> (12, 10)`)**, spawning inside at `(0, 4)`.
  - Giving **`Fresh Water`** to the guard at `(3, 4)` permanently unlocks all 4 Saffron City gatehouses; east mat `(5, 4)` exits to **`Saffron City (2, 18)`**.
- **Saffron Pokémon Center**:
  - From `(2, 18)`, walk `Down * 12` along `x = 2` to `(2, 30)` and `Right * 7` to `(9, 30)` -> door at **`(9, 29)`**.


<hr>

<h1><code>Locations/VermilionCity</code></h1>

# Route 5, Underground Path, Route 6 & Vermilion City — Verified Coordinates

## Route 5 & Underground Path (North-South)
- **Route 5 Entrance (from Cerulean `(20, 35)`)**: Enters at `Route 5 (10, 0)` (reached via Cerulean's eastern `x = 36` corridor: `(27, 11)` Burgled House -> `(3, 0)` hole -> `(27, 9) -> (33, 9) -> (34, 14) -> (36, 14) -> (36, 31) -> (20, 31)`).
- **Route 5 West Ledge Path**: `(10, 0) -> (6, 0) -> Down` to `(6, 29) -> (7, 27) -> (13, 27) -> (13, 28) -> (17, 28) -> Up` into **Underground Path Gatehouse `(17, 27)`**.
- **Underground Path (5–6)**:
  - Route 5 Gatehouse `(3, 7)` -> stairs at `(4, 4)` warp to Tunnel `(5, 4)`.
  - Tunnel runs straight south from `y = 4` to **`(2, 41)`** stairs (warps to Route 6 Gatehouse). Collected hidden **`X Special`** at **`(4, 34)`** facing `Up` from `(4, 35)` (Turn 458).
  - **Route 5 Northbound Return (`(17, 28)` -> Cerulean `(25, 35)`, Verified Turn 459)**: From outside Route 5 Gatehouse `(17, 28)`, walk `Left * 2` to **`x = 15`** and straight `Up * 29` — 100% ledge-free and wild-grass-free into **Cerulean City `(25, 35)`**!

## Route 6 (North-South to Vermilion City, Verified Turns 368–377)
- **Underground Path Exit Gatehouse `(17, 13)`**: Exits outdoors onto `Route 6 (17, 14)`.
- **Paved Walkway Geometry**:
  - North walkway runs west: `(17, 14) -> (14, 14) -> (14, 13) -> (4, 13)` (stairs north at `(7, 11)` lead to Saffron Gatehouse).
  - West walkway `x = 4..5` runs south: `(4, 13) -> (4, 21)`.
    - **Bug Catcher Keigo** at `(0, 15)` facing `Right` (spots `(4, 15)`): `Weedle Lv 16, Caterpie Lv 16, Weedle Lv 16` (defeated Turn 374).
  - Central cross-path runs east north of pond: `(4, 20..21) -> (16..17, 20..21)` (`(14..15, 22..27)` is tall grass).
  - East walkway `x = 16..17` runs south: `(16, 20) -> (16, 29)`, turning west along `y = 28..29` south of the pond.
    - **Bug Catcher Elijah** at `(19, 26)` facing `Left` (spots `(16, 26)`): `Butterfree Lv 20` (defeated Turn 379).
  - South gate corridor `(8..9, 30..35)` -> enters **Vermilion City** at `(18, 0)`:
    - **Jr. Trainer♀ Isabelle** at `(11, 30)` facing `Left`: `Pidgey Lv 16 x3` (defeated Turn 383).
    - **Jr. Trainer♂ Jeff** at `(11, 31)` facing `Left` (spots `(8, 31)`): `Spearow Lv 16, Raticate Lv 16` (defeated Turn 390).

## Vermilion City Landmarks (Verified Turns 390–395)
- **North Entrance**: Enters at `(18, 0)` from `Route 6 (8, 35)`.
- **Fishing Guru House**: `(7, 3)` (`Old Rod`).
- **Vermilion Pokémon Center**: **`(11, 3)`** (exits to `(11, 5)` / `(11, 4)`).
- **Pokémon Fan Club**: **`(9, 13)`** (indoor exit mat `(2, 7)` -> `(0, 7) -> (0, 1) -> (2, 1)` facing Chairman at `(3, 1)` -> **`BIKE VOUCHER`** obtained Turn 395!).
- **Vermilion Poké Mart**: **`(23, 13)`**.
- **Vermilion Gym `Cut` Bush**: **`(15, 18)`** (blocks access to Vermilion Gym southwest).
- **Vermilion Harbor Pier (Verified Turns 398–400)**:
  - Reach via **`y = 14`** east past Poké Mart `(23, 13)` to **`x = 30..31`** (`(26..29, 17..25)` is water!).
  - Walk south down `(30..31, 14..27)` (Sailor checks `S.S. Ticket` around `y = 18..19`), then turn **west along `y = 26..27`** to `(18, 27)` -> south across Vermilion Dock gangplank into **S.S. Anne 1F `(27, 0)`**.

## S.S. Anne (Verified Turns 400–419)
- **1F Corridor (`y = 6..7`, `x = 2..31`)**:
  - Exiting a 1F cabin spawns you inside the `(x, 8)` doorway recess — press `Up` onto `y = 7` before walking `Left`/`Right`!
  - **`(11, 8)` (Room #2 from left)**: Youngster Tyler (`Nidoran♂ Lv 21`), Lass Ann (`Pidgey Lv 18, Nidoran♀ Lv 18`), and **`TM08 (Body Slam)`** at `(12, 15)` (collected & taught to `AMETHYST` Turn 418!).
  - **`(19, 8)` (Room #4 from left)**: **Free-Heal Woman** (instant full party & PP heal!).
  - **`(23, 8)` (Room #5 from left)**: Gentleman Arthur (`Nidoran♂ Lv 19, Nidoran♀ Lv 19`).
  - **West Stairs (`(2, 6)` -> `(2, 4)`)**: Warps up to **2F `(2, 4)`**.
- **2F Corridor (`y = 12..13`, `x = 3..37`)**:
  - `(2, 4)` = stairs to 1F; Sailor NPC at `(3, 8)`; `(2, 11)` = stairs to 3F Bow `(19, 3)`. Use **`x = 3`** (`(3, 9) <-> (3, 12)`) to avoid `(2, 11)` and `(3, 8)`.
  - **`(13, 11)` (2F Room #2 from left)**: Fisher Dale (`Goldeen Lv 17, Tentacool Lv 17, Goldeen Lv 17`), Gentleman Brooks (`Pikachu Lv 23`), and **`Max Ether`** at `(12, 1)` (collected Turn 426).
  - **East 2F Corridor (`x = 36..37`)**: **Rival `GARNET`** ambushes at `(37, 8)` (`Pidgeotto Lv 19, Raticate Lv 16, Kadabra Lv 18, Ivysaur Lv 20` — defeated Turn 432).
  - **Captain's Quarters (`(36, 4)` stairs)**: Enters at `(0, 7)` -> walk `(0, 7) -> (4, 7) -> (4, 3)` facing `Up` at Captain -> rub back for **`HM01 (Cut)`** (obtained Turn 434; exiting `2F (2, 4)` spawns at `1F (2, 6)` -> `(26, 0)` -> Vermilion Dock departure cutscene -> Harbor `(18, 28)`).

## Vermilion Gym (`(12, 19)`, Verified Turns 438–440)
- **Access**: Chop the `Cut` bush at **`(15, 18)`** from `(15, 17)` using `AMBER`'s `CUT`, then walk `(15, 17) -> (15, 20) -> (12, 20) -> Up` into `(12, 19)` (spawns indoors at `(4, 17)`).
- **5x3 Trash-Can Grid**:
  - Columns: **`x in {1, 3, 5, 7, 9}`** | Rows: **`y in {7, 9, 11}`**.
  - Open horizontal aisles at `y = 12` and `y = 10`; Sailor Dwayne (`Pikachu Lv 21 x2`) on `x = 0`, Rocker Luca at `(3, 8)` facing `Left`, Gentleman Tucker (`Pikachu Lv 23`) at `(9, 6)` facing `Left`.
  - Solved lock via `(1, 11)` -> `(3, 11)` (Turn 447); defeated **Gym Leader Lt. Surge** at `(5, 1)` (`Voltorb Lv 21, Pikachu Lv 18, Raichu Lv 24`) for **Thunder Badge** + **`TM24 (Thunderbolt)`** (Turn 449).


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
  - **New Battle (Turn 1)**: **ALL FOUR** battle menus — top-level command (`►FIGHT`), `FIGHT` move submenu (`►Slot 0`), `PKMN` party list (`►Slot 0`), **AND `ITEM` bag menu (`►Slot 0`)** — **reset to Slot 0** at the start of every new battle (verified Turns 97, 280, and 565 `filmstrip_1.png` `#04`!).
  - **Same Battle (Turn 2+)**: Within the same battle, the top-level command menu, `FIGHT` submenu, `PKMN` cursor, and `ITEM` submenu all remember their last selected positions (verified Turns 21, 67, 73, 287).
  - **Gen 1 `Wrap` / `Bind` Sub-Turn UI (Verified Turn 558 `filmstrip_1.png` `#02`)**: During an active multi-turn `Wrap`, `►FIGHT` re-opens before every single 1-tick sub-turn, and pressing `A` on `►FIGHT` immediately advances `"Enemy <PKMN>'s attack continues!"` **without opening the move list** (leaving your `FIGHT` move cursor unchanged). Use rapid `A, A` + `7` `B`s (`~5s`/sub-turn) rather than directional move switches during `Wrap`.
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
  *(Misstep fixed in Turn 62: pressing only two `A`s before `B` cancels `YES/NO` as `NO`. Also verified Turns 743 & 746: dismissing `"Here you are! Thank you!"` with `B` resets the cursor onto the **top row of the current 4-row scroll viewport**, NOT index 0 of the full list and NOT the just-bought row!)*
  - **Pokémon Center Nurse Joy (`(3, 3)` facing `Up` — Max `sleep 10000` Cap, Poison-Faint Guard & Verify!)**:
  - **CRITICAL**: `"sleep <ms>"` has a strict **10,000 ms maximum** (`"sleep 10500"` / `"sleep 11500"` rejects the entire `press_buttons` call — root cause of failed heals in Turns 259 & 266!). To wait ~12s for a 4–6 Pokémon heal jingle without consecutive sleeps, use `"A", "sleep 9500", "B", "sleep 2500"`.
  - **Overworld Poison-Faint Edge Case (Turn 290)**: Poison ticks 1 HP every 4 steps; if a poisoned Pokémon hits `0` HP on the exact step onto `(3, 3)`, `"<POKEMON> fainted!"` opens and consumes the 1st `"A"`, causing the 5th `"A"` to stop on `►HEAL / CANCEL` where `"B"` cancels! Always visually verify green HP bars in `Start -> POKéMON` after healing.
  - After arriving cleanly at `(3, 3)` from `(3, 4)` + `"sleep 500"`, run `["A", "sleep 1000"] * 4 + ["A", "sleep 9500", "B", "sleep 2500"]` followed by `["B", "sleep 700"] * 3` and `Down * 5` (`(3,3) -> (3,7) -> outside`).
- **4-Move TM / Level-Up Move Replacement Sequence (Verified Turns 235–237, 418, 453–454)**:
  - Prompts: `"trying to learn <NEW>! ▼"` -> `"can't learn more than 4 moves! ▼"` -> `"Delete an older ▼"` -> `"move to make room for <NEW>?"` (`►YES / NO` — note the TWO line-scrolls!) -> `"Which move should be forgotten?"` (`Down * k`, `A`) -> `"1, 2 and... Poof! ▼"` -> `"forgot <OLD>! ▼"` -> `"And... ▼"` -> `"learned <NEW>! ▼"`.
  - Exact verified recipe from `"Use TM on which POKéMON?"` (Verified Turn 634 `filmstrip_1.png` `#09–#36`): select Pokémon + advance to `►YES / NO` with **6 `A`s**: `["A", "sleep 1000"] * 5 + ["A", "sleep 2000"]` (`#1` selects Pokémon, `#2` scrolls `trying to learn`, `#3` clears `<MOVE>!`, `#4` scrolls `can't learn more`, `#5` clears `than 4 moves!`, `#6` scrolls `for <MOVE>?` `►YES / NO`), then `["A", "sleep 1000"]` (#7) opens `"Which move should be forgotten?"`, `["Down", "sleep 250"] * k` selects slot `k`, and `["A", "sleep 1200", "B", "sleep 1200", "B", "sleep 1200", "B", "sleep 4500", "B", "sleep 800"]` completes replacement back to `ITEM`.
  - **Declining / Abandoning a New Move (Verified Turn 549 `filmstrip_1.png`)**: Unlike `"Delete an older ▼ / move to make room ▼ / for <MOVE>?"` (which has two `▼` scrolls), pressing `B` (`NO`) on `"for <MOVE>?"` `►YES / NO` opens `"Abandon learning <MOVE>?"` `►YES / NO` **immediately with ZERO intermediate `▼` prompt** (`~1.0s` scroll). Thus from `"for <MOVE>?"` `►YES / NO`, the exact abandon recipe is `["B", "sleep 1500", "A", "sleep 1500"]` (`B` = don't delete old move, `A` = YES abandon new move).
- **Hidden Floor Item Probe (Verified Turn 458)**:
  - Because hidden floor items sit on walkable tiles, stand at `(hx, hy + 1)` already facing `Up` and send `["A", "sleep 500", "Up"]`: if `mgba.get_coordinates()` stays at `(hx, hy + 1)`, `"COBALT found <ITEM>!"` opened (wait `"sleep 4000", "B", "sleep 800"`); otherwise you step onto `(hx, hy)` immediately with zero wasted fanfare wait.
- **Cave Exit Mats vs. Building Exit Mats (Verified Turn 187)**:
  - Cave exit mats (e.g., Mt. Moon 1F `(14, 35)`) warp **immediately upon stepping onto the tile**, whereas building exit mats (e.g., Pokémon Center `(3, 7)`) require pressing `Down` while standing on the mat.
- **Multi-Round Battle Loop Pitfalls & Timeout Guardrails (Verified Turns 181–186, 198, 355)**:
  - Cap automated battle loops in `mcp_game_run_code` at **2–3 rounds max (~35–50s)** with `9–10` `B` presses (`750ms` each) so trainer intros + status/multi-box animations (`Hypnosis`/`Disable`/level-ups) never approach the 120s script wall-clock timeout (Turn 355 timed out on intro + 4 rounds x 14 `B`s).
  - If the lead Pokémon faints during an automated `["A", "A", "B"*8]` battle loop, `"Use next POKéMON?"` opens the Party list where `A` sends out Slot 1 (or repeats `"There's no will to fight!"` if cursor is on the fainted Pokémon).
  - **Safe Switch-Training**: Always place the low-level trainee in Slot 0 *before* battle and switch *out* on Turn 1 (zero damage taken by trainee), rather than switching a frail trainee *in* mid-battle into an incoming attack.
- **Field-Move Party Submenu Shift & Gen 1 TM Quirks (Verified Turns 358, 361, 636)**:
  - Teaching a field move (`DIG`, `CUT`, `SURF`, `FLY`, `STRENGTH`) inserts that move at Row 0 of that Pokémon's overworld `Start -> POKéMON` submenu (`►DIG / STATS / SWITCH / CANCEL` — 4 rows, `SWITCH` is `Down * 2`), whereas Pokémon without field moves retain the 3-row submenu (`►STATS / SWITCH / CANCEL` — `SWITCH` is `Down * 1`).
  - **`HM02 (Fly)` Town Map Selector (Verified Turns 636–637)**: **Always** opens at index `0` (`PALLET TOWN`) regardless of current city! Pressing **`Up`** increments (`0 Pallet -> 1 Viridian -> 2 Pewter -> 3 Cerulean -> 4 Lavender -> 5 Vermilion -> 6 Celadon -> ...`), whereas pressing **`Down`** decrements (`Down * 1` wraps `0 -> last visited`, `Down * 2` wraps `0 -> second-to-last`). Wait `"sleep 5500"` after confirming `A` for the full bird landing animation to complete.
  - `Nidoqueen` is `NOT ABLE` to learn `TM28 (Dig)` in Generation I (she learns `TM26 Earthquake` instead), whereas `Squirtle`/`Wartortle`/`Blastoise` and `Paras` ARE `ABLE`.
- **Overworld Grid File Availability (`latest_grid.png`, Verified Turn 370)**:
  - `screenshots/latest_grid.png` is omitted/removed whenever `<GameState>` has no `<Position>` (including when a step triggers a trainer `[!]` walk-up or wild encounter flash). Do not batch `read_file` on `latest_grid.png` when walking across tall grass or trainer sightlines.
- **In-Battle Command, Move, & Faint Cursor Nuances (Verified Turns 380–389)**:
  - Switching a Pokémon via `PKMN` **resets** the 2x2 command menu cursor to `►FIGHT` (Turn 387), whereas using a Bag item via `ITEM` keeps the 2x2 cursor on **`►ITEM`** (Turn 383 — always use `Left, Up` to clamp back to `►FIGHT`).
  - **X Items (`X Special`, `X Speed`, `X Defend`, `X Attack`, Verified Turn 752)**: Selecting an X Item in battle applies immediately to the **currently active Pokémon** on a single `A` press (`does NOT open "Use item on which POKéMON?"`), boosting the stat by +1 stage (`1.5x`).
  - Having a 1-move Pokémon (`AMBER`) open `FIGHT` clamps the `FIGHT` move index back to **Slot 0**, so a 4-move Pokémon sent out afterward in the same battle starts on **Slot 0** rather than a previously used slot (Turn 389).
  - In Gen 1, **KOing an enemy Pokémon skips the end-of-turn poison tick** for that turn (Turn 380).
  - In **Trainer battles**, a fainted Pokémon opens `"Bring out which POKéMON?"` directly without a `YES/NO` prompt, and `B` presses are safely ignored on that Party screen (Turn 388).
- **Ladder `back_d` Pitfall & `known_open_move` (Verified Turns 202–205)**:
  - Never run a `back_d` wall-probe when standing 1 tile off a ladder warp (`back_d` steps right back onto the ladder and re-warps floors!). First step 2+ tiles clear of any ladder using `known_open_move` (which flees wild encounters in place without stepping backward).
- **Multi-Spinner Slide Timing & Mid-Slide Grid Offset (Verified Turns 670–671)**:
  - Long 12–16 tile spinner chains (e.g., Rocket Hideout B2F `(12, 13) -> (2, 9)`) take ~5.5–6.0 seconds to finish sliding. If trailing `"sleep <ms>"` is shorter (e.g., `3500` ms), `<GameState>` and `latest_grid.png` snapshot mid-slide with a 1-tile camera/coordinate offset. Always use `"sleep 6500"` on long spinner chains, or call `observe` if a reported landing tile is not a gray stopper pad.
- **Player's PC (`DEPOSIT ITEM`) Cursor Reset Rule (Verified Turns 692–693)**:
  - Dismissing `"<ITEM> was stored via PC."` with `B` returns **directly** into `"What do you want to deposit?"` with the cursor **reset to Slot 0** (NOT back to the `WITHDRAW / DEPOSIT` menu). Quantity items (`× 1`, including TMs) prompt `"How many?"` (`A, A, B`), whereas Key Items (`Town Map`, `Helix Fossil`, `S.S. Ticket`, `Lift Key`) store immediately without `"How many?"` (`A, B`).
- **`Cut` Bush Regrowth After Battles (Verified Turn 721)**:
  - Completing a trainer/wild battle redraws overworld map tiles and **re-grows any chopped `Cut` bushes** in the current map (e.g., Celadon Gym `(5, 7)` re-grew immediately behind us after defeating Cooltrainer♀ Mary at `(5, 6)`).

## Navigation Scripting Guardrails & Cave Primitives (Verified Turns 53, 60, 152, 165–166)
- Always use bounded `for _ in range(N):` loops rather than unbounded `while` loops so an unexpected wall/NPC cannot trip the 150-button script abort limit, and **always `break` immediately** if `after == before` triggers a multi-second cutscene clearer (`never repeat a 10s dialogue clearer across 10 wall bumps or it will hit the 120s script timeout`, Turn 811).
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

## Pokémon Tower (`Poké Flute`) -> Saffron Unlock -> Cycling Road -> Fuchsia City (Soul Badge)
1. **Pokémon Tower (`Lavender Town (14, 5) -> 1F–7F`)**:
   - **1F -> 2F**: Defeat **Rival `GARNET`** (`Pidgeotto Lv 25` -> `Ice Beam`, `Gyarados Lv 23` -> switch to **`AMETHYST` `Thunderbolt` [4x!]**, `Growlithe Lv 22` -> `BubbleBeam`, `Kadabra Lv 20` -> `Bite` / `Body Slam`, `Ivysaur Lv 25` -> `Ice Beam`).
   - **3F–5F**: Use `Repel x4` (`Slot 0`, blocks all wild Lv 18–24 `Gastly`/`Cubone` since `NAUTILUS` is Lv. 37!); Channelers carry `Gastly`/`Haunter` (use `BubbleBeam` / `Ice Beam` / `Dig` — note `Bite` is Normal-type in Gen 1 so it misses Ghosts!). Step onto the **5F Purified Healing Pad** for free full HP/PP restore!
   - **6F**: Defeat Ghost **Lv. 30 `Marowak`** at the stairs (`identified by Silph Scope`, 2x weak to `BubbleBeam` & `Ice Beam`!).
   - **7F**: Defeat the 3 Team Rocket Grunts -> talk to **Mr. Fuji** -> auto-warps to Volunteer House `(7, 9)` -> talk to Mr. Fuji for **`POKé FLUTE`**!
2. **Unlock Saffron City (`Fresh Water × 1` in Bag Slot 5)**:
   - `Fly` to **Celadon City** -> walk east on Route 7 into **West Saffron Gatehouse** -> guard drinks `Fresh Water` and unlocks all 4 Saffron gates! Heal at **Saffron Pokémon Center** to register Saffron on the `Fly` map!
3. **Cycling Road & Fuchsia City (`HM03 Surf`, `HM04 Strength`, Badge #5 — Soul Badge)**:
   - `Fly` to **Celadon City** -> Route 16 `(27, 10)` -> play **`Poké Flute`** on **`Snorlax`** (`flee`) -> ride **`Bicycle`** down Route 17 -> Route 18 -> **Fuchsia City**!
   - Clear **Safari Zone** (`Gold Teeth` + **`HM03 Surf`** -> teach 95-BP STAB `Surf` to `NAUTILUS`!), get **`HM04 Strength`** from Warden, and sweep **Gym Leader Koga** (`Koffing x2, Muk, Weezing`) for **Soul Badge** (#5)!


<hr>