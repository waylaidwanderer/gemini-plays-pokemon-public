# UI, Controls & Overworld Mechanics (Verified)

## Naming Screen Keyboard (Turn 6)
- **Controls:**
  - `Select`: Cycle character sets (`UPPER` -> `lower` -> `OTHERS`).
  - `B`: Backspace (`BACK`).
  - `Start`: Jump cursor directly to `OK` button (press `A` after `Start` to confirm name).
- **Uppercase Grid (4 rows x 8 cols, cursor starts at `(0, 0)` = `A`):**
  - Row 0: `A` (0), `B` (1), `C` (2), `D` (3), `E` (4), `F` (5), ` ` (6), `.` (7)
  - Row 1: `G` (0), `H` (1), `I` (2), `J` (3), `K` (4), `L` (5), ` ` (6), `,` (7)
  - Row 2: `M` (0), `N` (1), `O` (2), `P` (3), `Q` (4), `R` (5), `S` (6), ` ` (7)
  - Row 3: `T` (0), `U` (1), `V` (2), `W` (3), `X` (4), `Y` (5), `Z` (6), ` ` (7)

## Cutscene & Warp Scripting (Turns 11–20)
- **Dialogue Advancement:** Pressing `B` with `sleep 1000` advances standard dialogue boxes cleanly at `FAST` text speed and is completely inert once overworld control returns (preventing accidental NPC/sign re-interactions).
- **Warp + Cutscene Combo in `run_code`:** A `tools.press_buttons` call that steps onto a warp tile automatically terminates upon leaving the overworld. A subsequent `tools.press_buttons(["B", "sleep 1000", ...])` call in the same `run_code` script executes during the post-warp cutscene, clearing both the warp and cutscene in one turn.

## Littleroot Town Coordinates (Turns 12–21)
- **Player's House (Brendan / Left House):**
  - Exterior Door: `(5, 8)`
  - 1F: Exit mat `(8, 8)` (step `Down` to exit), Stairs to 2F `(8, 2)` (step `Up` onto `(8, 2)` to warp).
  - 2F: Stairs doorway `(7, 1)` (step `Up` from `(7, 2)` to warp), Wall Clock `(5, 1)` (interact from `(5, 2)` facing `Up`; confirmation defaults to `NO`), Desk PC `(0, 1)` (interact from `(0, 2)` facing `Up`).
- **Rival's House (May / Right House):**
  - Exterior Door: `(14, 8)` (exits to `(14, 9)`).
  - 1F: Entry mat `(2, 8)`, Stairs to 2F at `(2, 2)` (walk `Up` 6 tiles from `(2, 8)` onto `(2, 2)` to warp!).
  - 2F: Entry at `(1, 2)`, Poké Ball at `(5, 4)` (walk `Down, Down, Right, Right, Right` to `(4, 4)` facing `Right` and press `A` to trigger May's entrance; exit via stairs at `(1, 1)`).
  - Littleroot North Exit (after meeting May): NPC girl stands at `(10, 1)`; bypass via `(11, 1) -> (11, 0)` onto Route 101!

## Battle & Menu Persistence Mechanics (Turns 29–42)
- **No In-Battle Bag Healing (Turn 36):** Selecting `POTION` in the `BAG` during battle only shows `▶CANCEL`. Healing items from the Bag can only be used in the overworld. Held items (e.g. `BERRY JUICE`) still activate automatically in battle.
- **Battle Menu Cursor Memory (Turn 36, 238, 293):** The 2x2 battle menu (`FIGHT` / `BAG` / `POKéMON` / `RUN`) resets to `▶FIGHT` at the start of each new battle, and remembers the last used quadrant within the same battle. The move menu (`FIGHT`) and Bag pocket (`ITEMS` / `POKé BALLS`) persist across battles.
- **Start Menu Cursor Memory (Turns 41–42, 296, 306):** The Start menu remembers its cursor row index across openings. With the Pokédex obtained, rows are `0: POKéDEX`, `1: POKéMON`, `2: BAG` (current cursor position), `3: ORIQP`, `4: SAVE`, `5: OPTION`, `6: EXIT`. Opening or closing the `BAG` or `POKéMON` menu triggers a ~2.0–2.5s screen fade; always wait `sleep 2500` after selecting or backing out of those submenus.
- **Birch's Lab Coordinates (Turn 42):** Birch stands at `(6, 4)`, player stands at `(6, 5)`, exit mat is straight down at `(6, 12)`.

## Pokémon Center Healing Formula (Verified Turn 57)
- **Interior Coordinates:** Enter at `(7, 8)`. Walk 5 tiles `Up` to stand at `(7, 4)` facing Nurse Joy across the counter at `(7, 3)`.
- **Button Sequence:**
  - Press `A` **4 times** with `sleep 1200` between presses (clears Nurse Joy's 3 intro lines and confirms `▶YES` on the 4th `A`).
  - Wait `sleep 5500` for the healing jingle to finish.
  - Press `B` **4 times** with `sleep 1000` between presses to close her post-healing dialogue without re-talking.
  - Press `Down` **5 times** to exit back to the overworld.

## Verified Route & Town Coordinates (Turns 45–60)
- **Littleroot Town (Lab to Route 101):**
  - Birch's Lab exterior door: `(7, 16)`; exiting the Lab places you at `(7, 17)` (already below the Lab sign row). From `(7, 17)`, walk `Right` 3 tiles to `(10, 17)`, then `Up` 17 tiles along `x=10` to `(10, 0)`.
- **Route 101 Pathing:**
  - **Northbound (Littleroot -> Oldale):** Enter at `(10, 19)` -> `Up` 4 to `(10, 15)` -> `Left` 4 to `(6, 15)` -> `Up` 4 to `(6, 11)` -> `Right` 4 to `(10, 11)` -> `Up` 1 to `(10, 10)` -> `Right` 7 to `(17, 10)` -> `Up` 6 to `(17, 4)` -> `Left` 6 to `(11, 4)` -> `Up` 5 into Oldale Town `(11, 19)`.
  - **Southbound (Oldale -> Littleroot):** Jump straight `Down` along `x=10` over the two south-facing ledges at `y=6` and `y=13`!
- **Oldale Town:**
  - South border (from Route 101): `(10, 19)` / `(11, 19)`.
  - Pokémon Center door: `(6, 16)` (approach along `y=17` from `(9, 17)` or `(11, 17)`, then step `Up` into `(6, 16)`).
  - Poké Mart door: `(14, 6)` (free Potion clerk started at `(13, 14)`, now stands at `(13, 7)`).
  - North border (to Route 103): `x=10, y=0` (transitions to `(10, 21)` on Route 103).

## Verified Findings (Turns 124–150)
- **Mudkip Growth & Modified Learnset (Turns 124, 301):**
  - Uses the **Slow EXP group** (`5 * n^3 / 4`: 135 EXP for Lv. 5, 270 for Lv. 6, 428 for Lv. 7, 1250 for Lv. 10).
  - Learns `Bubble` (20 BP Water Special, 30 PP) at **Lv. 6**, `Mud Sport` (15 PP) at **Lv. 7**, and `Water Gun` (40 BP Water Special, 25 PP) at **Lv. 10**.
- **Wild Encounter Pools Observed:**
  - **Route 101 (Claimed by Starter):** Lv. 2–3 `Wurmple` (`Tackle`, `String Shot`), `Weedle` (`Poison Sting`, `String Shot`), `Caterpie` (`Tackle`, `String Shot`), `Pidgey`, `Sentret` (`Quick Attack`), `Rattata` (`Quick Attack`, `Tail Whip`), `Poochyena` (`Tackle`, `Howl`), `Zigzagoon` (`Swift`, `Sand-Attack`, holds `Berry Juice`), `Pichu` (`ThunderShock`, `Charm`, Ability: `Static`), `Togepi` (`Growl`, `Charm`, `Metronome`), `Igglybuff` (`Sing`, `Charm`), `Cleffa` (`Charm`, `Encore`, Ability: `Cute Charm`). Note: The left northern grass patch sits at `x=4..6, y=2..4` while `x=7..10, y=1..4` is a grass-free corridor.
  - **Two-Attempt `RUN` Cadence (Verified Turn 472):** `"Can't escape!▼"` prints in 1.5s and waits for a `B` press before the wild Pokémon executes its ~7.5s attack. Use `["Down", "Right", "A", "sleep 1800", "B", "sleep 7500", "B", "sleep 1000", "A", "sleep 1800", "B", "sleep 2500"]`—if Attempt 1 succeeds, the trailing `A` and `B` are completely inert in the overworld; if Attempt 1 fails, the cursor stays on `▶RUN` so the second `A` triggers Attempt 2 cleanly.
  - **Options `TEXT SPEED` Wrap-Around (Verified Turn 465):** In `OPTION`, `TEXT SPEED` wraps around (`SLOW -> MID -> FAST -> SLOW`). Pressing `Right` once from `MID` selects `FAST`, whereas pressing `Right` twice from `MID` wraps back to `SLOW`.
  - **Route 103:** Lv. 4 `Poliwag` (`Water Gun`, 44 EXP), `Skitty` (`Attract`), `Wingull` (`Water Gun`, `Wing Attack` 60 BP STAB, 10 Speed), `Ledyba` (`Silver Wind` — **100% chance to boost all 5 stats `+1 Atk/Def/SpA/SpD/Spd` on every hit in this ROM!**), `Sunkern` (`Absorb`, `Growth`), `Spoink` (`Confusion`), `Ekans`, `Spearow`, `Hoppip`, `Mareep` (`ThunderShock`). Note: Optimal **1-grass-tile** path to Rival May `(10, 4)`: from Oldale `(10, 17)`, take **26** steps `Up` to `(10, 13)` -> `Right` 4 to `(14, 13)` -> `Up` **7** to `(14, 6)` -> `Left` 9 along `y=6` to `(5, 6)` (the **only** grass tile!) -> `Up` 2 through `(5, 5)` to `(5, 4)` -> `Right` 5 to `(10, 4)`.
  - **Route 102:** Lv. 6 `Gulpin` (`Yawn` [inflicts immediate sleep], `Acid`, `Pound`), Lv. 4 `Ralts` (`Confusion`, Ability: `Synchronize`), Lv. 6 `Hoothoot`.
- **Southbound Grass-Free Ledge Corridor & Mom's Heal (Turns 130–146):**
  - Walking straight `Down` along column **`x=10`** from `(10, 4)` on Route 103 jumps over both ledges (`y=5`, `y=12`) into Oldale Town with **0 grass tiles**.
  - Walking straight `Down` along column **`x=10`** across Route 101 jumps over both ledges (`y=6`, `y=13`) into Littleroot Town with **0 grass tiles**.
  - Inside the Littleroot 1F house (door `(5, 8)` -> mat `(8, 8)`), **Mom** sits at **`(2, 6)`** (talk from `(2, 5)` facing `Down`) and provides a free full HP + status heal.
- **Overworld Warp & Grass Timing Workarounds (Turns 124–149):**
  - Insert `["B", "sleep 800"]` (or `["B", "sleep 2500", "B"]`) between a door warp step and subsequent movement so the transition fade completes before walking.
  - Insert `"sleep 300"` before changing direction inside tall grass so the 4-frame grass-rustle animation does not drop the turn input.
- **Nickname Prompt Transition (Turns 207, 534):** When catching a **new** Pokédex species, advancing from `"Gotcha! X was caught!▼"` to selecting `▶YES` on `"Give a nickname to the captured X?"` requires **4 `A` presses** (`A #1` -> `"X's data was added to the POKéDEX.▼"`, `A #2` -> Pokédex entry page, `A #3` -> `"Give a nickname...?"`, `A #4` -> `▶YES` opens keyboard at `(0, 0) = 'A'`). Do not send an extra `A` after the 4th `A` before directional inputs on the naming grid, or it will type `'A'` as the first character.
- **Route 102 Layout & Trainers (Turns 175–177, 303–314, 529–570):**
  - Enter Route 102 from Oldale Town `(0, 10)` at `(49, 10)`.
  - Safe northern tall grass patch (away from trainers): `x=37..38, y=3..6` (approach via `(38, 10) -> (38, 7) -> (37, 7) -> (37, 6)`).
  - Grass-free path to Youngster Calvin: walk `Left` to `(38, 10)`, `Down` 4 tiles to `(38, 14)`, and `Left` 4 tiles to `(34, 14)`.
  - **Youngster Calvin** stands at **`(33, 14)`** facing `Down` and has 3 Lv. 6 Pokémon (`Sentret` [Assist->Rock Smash / Mud-Slap, Quick Attack], `Zigzagoon` [Swift], `Poochyena` [Rock Smash, Howl]).
  - Grass-free path from `(34, 14)` to Bug Catcher Rick: `Down` 2 to `(34, 16)`, `Left` 6 to `(28, 16)`, `Up` 1 to `(28, 15)`, `Left` 2 to `(26, 15)`.
  - **Bug Catcher Rick** stands at **`(25, 15)`** facing `Up` and has 4 Lv. 5 Pokémon (`Caterpie`, `Wurmple` [String Shot], `Kakuna` [holds `Berry Juice`, Poison Sting], `Cascoon` [holds `Berry Juice`, knows `Iron Defense`, `Tackle`]).
  - **In-Battle Shift & Move Cursor Rules (Turns 308–313):** Using a Potion on a party Pokémon in the overworld resets the in-battle move cursor back to Slot 0 (`Tackle`). In Trainer battles with 2+ party Pokémon on `SHIFT` mode, follow potential KO attacks ONLY with `B` presses so `B` automatically selects `NO` on `"Will ORIQP change POKéMON?"`.
  - **Lass Tiana** stands at **`(15, 5)`** facing `Up` and has 3 Pokémon (`Lv. 6 Igglybuff` [Ability: `Cute Charm`, holds `Oran Berry`, uses `Present`], `Lv. 6 Sunkern` [holds `Berry Juice`, knows `Leech Seed`, `Protect`, `Mega Drain`, `Absorb`], `Lv. 5 Togepi`).
  - **Grass-Free Path from Bug Catcher Rick `(26, 15)` to Berry Trees `(24, 3)` (Verified Turn 557):** There is a south-facing ledge along `x=19..25, y=6` with tall grass on `(19..25, 7)` and `(19..23, 8..9)`. Column **`x=18`** is the 1-tile grass-free corridor between the trees (`x=17`) and the tall grass (`x=19`). To reach `(24, 3)` with **0 grass tiles**, walk `Up` 2 to `(26, 13)`, `Left` 1 to `(25, 13)`, `Up` 3 to `(25, 10)`, `Left` 7 along grass-free `y=10` to `(18, 10)`, `Up` 6 along grass-free `x=18` to `(18, 4)`, `Right` 6 to `(24, 4)`, and `Up` 1 to `(24, 3)`.
  - **Berry Tree Harvesting & Equipping Formula (Turns 319, 560):** Press `A` **3 times** with `sleep 1200` (`sleep 3000` after the 3rd `A`) to confirm picking the Berries, then press `B` **3 times** (`sleep 1200`) to close the text without re-interacting with the loamy soil (which otherwise opens the `BERRIES POCKET` and resets the in-battle move cursor to Slot 0). Inside the `BAG -> BERRIES` pocket (Dot 4), Berries are sorted by Berry Number (`No03 PECHA BERRY` Row 0, `No07 ORAN BERRY` Row 1), and the 2-column Berry popup menu starts at `▶CHECK TAG` (`Down, Right, A` selects `GIVE`).
  - **Poké Mart Overworld Purchase Formula (Turn 377):** Talking to a Mart clerk from the overworld requires **3 `A` presses** to open the `BUY` screen (`"A", "sleep 1200"` for `"Welcome!"`, `"A", "sleep 1200"` for `"How may I serve you?"`, and `"A", "sleep 3000"` to select `▶BUY` and wait for the 2.7s fade-in).
  - **Deterministic Wild Encounter Detection in `run_code` (Turn 371):** Because `tools.press_buttons` returns `"Success"` in Python even when aborted by a wild battle, pass pure movement steps across grass without interleaved sleeps and check `mgba.get_coordinates()` afterward; if the player has not reached the target `(x, y)` coordinate, a wild battle aborted the path!