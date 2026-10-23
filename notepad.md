<h1><code>Locations/Encounters</code></h1>

# Route & Area Encounters (Attempt #3)

| Location | Pokémon | Nickname | Level | Status | Notes |
|---|---|---|---|---|---|
| Route 101 | Mudkip ♂ | APOSEIDON | 7 | Active | Starter (`Met in ROUTE 101` — claims Route 101 encounter) |
| Route 103 | Wingull ♀ | - | 4 | Forfeited | Broke out on Shake 0 at ~52% green HP; fled at 10/25 HP to avoid 14-damage Wing Attack crit range |
| Route 102 | Ralts ♂ | APOLLO | 4 | Active | Caught at (38, 6) in red HP after 2x Bubble; knows Confusion |
| Route 104 (South) | TBD | TBD | - | Pending | Open encounter west of Petalburg City |
| Petalburg Woods | TBD | TBD | - | Pending | Open encounter north of Route 104 South |

<hr>

<h1><code>Main</code></h1>

# Pokémon Emerald Nuzlocke — Main Dashboard

## Run Status
- **Game:** Pokémon Emerald (Emerald Kaizo / Modified ruleset: In-battle Bag healing items are DISABLED [Cancel only]; wild/trainer Pokémon have custom movesets & held items!)
- **Player Name:** ORIQP (Boy / Brendan)
- **Attempt:** #3
- **Badges:** 0 / 8

## Nuzlocke Rules & Level Caps
1. **Permadeath:** Fainted Pokémon (0 HP) are permanently dead and must be boxed in the Graveyard.
2. **First Encounter Only:** Catch only the first wild Pokémon encountered in each unique area once Poké Balls are obtained (`Locations/Encounters.md`).
3. **Nicknames:** Always give creative nicknames to every Pokémon caught/received.
4. **Level Caps:**
   - Gym 1 (Roxanne): **Lv. 15**
   - Gym 2 (Brawly): **Lv. 19**
   - Gym 3 (Wattson): **Lv. 24**
   - Gym 4 (Flannery): **Lv. 29**
   - Gym 5 (Norman): **Lv. 31**
   - Gym 6 (Winona): **Lv. 33**
   - Gym 7 (Tate & Liza): **Lv. 42**
   - Gym 8 (Juan): **Lv. 46**
   - Elite Four / Champion: **Lv. 58**

## Key Tactical Rules (Learned from Attempts #1 & #2)
- **Starter Claims Route 101 (Verified Turn 141):** Because the starter's summary reads `Met in ROUTE 101`, the Nuzlocke harness treats Route 101 as already used and blocks Poké Ball throws on Route 101.
- **Lowered Wild Catch Rates & Crit Range Rule (Turns 158–161, 252):** Poké Balls thrown at **Green HP (`>50%`)** pop out on Shake 0 in this ROM. Always weaken wild encounters into **Yellow (`<50%`) or Red (`<20%`) HP** before throwing a Poké Ball, and immediately `RUN` if HP drops into `2x` enemy attack damage (crit range).
- **Modified Move Mechanics — Immediate Yawn (Turn 169):** In this ROM, `Yawn` inflicts Sleep (`SLP`) immediately on the turn it is used rather than drowsy delayed sleep.
- **Route 102 Trainer Scaling (Verified Turn 177–182):** Youngster Calvin at `(33, 14)` on Route 102 has **3 Lv. 6 Pokémon** (`Sentret` with `Assist` -> `Rock Smash` + `Quick Attack`; `Zigzagoon` with `Swift`; plus a 3rd Pokémon with `Rock Smash`). **DO NOT challenge Youngster Calvin at Level 7!** Grind to **Level 10+** and catch Route 103 / Route 102 encounters first!
- **Oldale Mart Prices (Turn 153):** Poké Balls cost only **$10** each (10+ awards a Premier Ball); Potions cost $300; Antidotes cost $100.
- **Heal in Overworld Above 75% HP:** Bag Potions cannot be used in battle.

## Active Party
1. **APOSEIDON** (Mudkip ♂) — Lv. 9 (1242/1250 EXP, 8 EXP to Lv. 10) | HP: 29/29 | Nature: Gentle (+SpD, -Def) | Ability: Torrent | Stats: 18 Atk / 13 Def / 15 SpA / 15 SpD / 14 Spd | Moves: Tackle (35 PP), Bubble (30 PP), Mud Sport (15 PP)
2. **APOLLO** (Ralts ♂) — Lv. 4 (80/156 EXP) | HP: 16/16 | Nature: Naughty (+Atk, -SpD) | Ability: Synchronize | Stats: 8 Atk / 7 Def / 9 SpA / 7 SpD / 8 Spd | Moves: Confusion (25 PP)

## Notepad Index
- `Main`: High-level dashboard, party summary, level caps, and core tactical rules.
- `Locations/Encounters`: Route-by-route encounter tracking.
- `Mechanics/Graveyard`: Fallen Pokémon, wipe post-mortems, and run history.
- `Mechanics/UIAndControls`: Verified naming keyboard grid, warp/cutscene scripting patterns, Pokémon Center healing formula, and Littleroot/Route 101/Oldale/Route 103 coordinates.

<hr>

<h1><code>Mechanics/Graveyard</code></h1>

# Graveyard & Run History

## Attempt #1 (Turns 1–78) — WIPEOUT
- **Casualties:**
  - **TRITON** (Mudkip ♂, Lv. 5, Timid) — Died on Turn 77 on Route 103 `(4, 5)` to a Wild Wingull Lv. 4 (`Wing Attack`).
- **Root Causes of Wipe:**
  1. **Unhealed Pre-Battle HP (`14/20` HP):** Entered tall grass at `14/20` HP despite holding 2 Potions in the Bag (which can only be used in the overworld).
  2. **Queued 3 Turns Against Unverified Wild Species:** Queued 3 consecutive `Tackle` turns on Turn 75 against a Lv. 4 Wingull before seeing its moveset (`Wing Attack`, 60 BP STAB Flying, ~6–7 damage/hit).
  3. **Speed Trap on Route 103:** Lv. 4 Wingull (Base 85 Speed -> 10 Speed) outsped Lv. 5 Timid Mudkip (9 Speed), causing two consecutive `RUN` attempts (`Attempts 1 & 2`) to fail (`"Can't escape!"`) while Wingull KO'd TRITON from `3/20` HP.
- **Tactical Lessons for Attempt #2:**
  1. **Grind on Route 101 (Lv. 2–3 wilds), NOT Route 103 (Lv. 4 fast/dangerous wilds):** Train our starter to **Level 7** on Route 101 (right below Oldale Town) before crossing Route 103 to May.
  2. **Immediate Overworld Healing:** Since in-battle Bag healing is disabled (`▶CANCEL` only), heal in the overworld with Potions or at the Pokémon Center whenever HP drops below 75%.
  3. **Single-Turn Scouting & Immediate Escape:** Against fast/threatening wild Pokémon (like Wingull or Skitty on Route 103), `RUN` on Turn 1 while at full HP rather than trading hits.

## Attempt #2 (Starting Turn 79)
- **Deaths:** None

---

## Attempt #2 Wipe Post-Mortem (Turn 183)
- **Fallen Pokémon:** `AXOLOTL` (Mudkip ♂, Lv. 7, Adamant) — Fainted at `(34, 14)` on Route 102 against Youngster Calvin.
- **Enemy Details (Youngster Calvin at `(33, 14)` on Route 102):**
  - Has **3 Pokémon**:
    1. **Sentret ♂ Lv. 6**: Knows `Assist` (called `Rock Smash` from a back-line teammate, inflicting `-1 Def` drops) and `Quick Attack` (+1 priority, dealt 9 HP after two Defense drops). Took 3 `Tackle` hits (`~36%` each from Lv. 7 Adamant Mudkip) plus 1 `Bubble` to KO, yielding `72 EXP`.
    2. **Zigzagoon ♂ Lv. 6**: Outsped Lv. 7 Mudkip (`11 Spd`) and used `Swift` (60 BP STAB never-miss).
    3. **3rd Pokémon (Unseen)**: Knows `Rock Smash` (verified via Sentret's `Assist`).
- **Root Causes of Wipe:**
  1. **Underleveled for Route 102 Trainers:** Challenged Youngster Calvin at **Level 7** (`15 EXP` short of Level 8), causing `Tackle` to miss the 3HKO on Lv. 6 Sentret by ~1 HP and allowing Sentret an extra turn to land a second `-2 Def` `Quick Attack` (`10 -> 2 HP`).
  2. **Solo Party (0 Catch Captures on Routes 103 & 102):** At Level 7 (`25 HP`), wild Lv. 4 Sunkern on Route 103 and wild Lv. 6 Gulpin (`Yawn` + `Acid`) on Route 102 threatened AXOLOTL's HP too quickly, forcing us to flee both encounters and face Youngster Calvin solo with no switch-in to clear `Rock Smash` Defense drops.
- **Tactical Rules for Attempt #3:**
  1. **Level 10+ Before Route 103/102 Catches & Route 102 Trainers:** Grind Mudkip to **Level 9–10** on Route 101 / Route 103 before attempting our Route 103 and Route 102 Nuzlocke catches or fighting Youngster Calvin. Higher bulk (`~32–35 HP`) allows safely throwing multiple Poké Balls to guarantee catches, and higher Attack (`~23–25 Atk`) cleanly 2HKOs/3HKOs Lv. 6 trainer Pokémon.
  2. **Never Fight Route 102 Trainers Solo at Lv. 7:** Ensure we have **at least Lv. 10+** (and ideally a 2nd caught Pokémon from Route 103 or Route 102 to pivot out of stat drops/Yawn) before challenging Youngster Calvin at `(33, 14)`.

<hr>

<h1><code>Mechanics/UIAndControls</code></h1>

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
  - Exterior Door: `(14, 8)`

## Battle & Menu Persistence Mechanics (Turns 29–42)
- **No In-Battle Bag Healing (Turn 36):** Selecting `POTION` in the `BAG` during battle only shows `▶CANCEL`. Healing items from the Bag can only be used in the overworld. Held items (e.g. `BERRY JUICE`) still activate automatically in battle.
- **Battle Menu Cursor Memory (Turn 36, 238, 293):** The 2x2 battle menu (`FIGHT` / `BAG` / `POKéMON` / `RUN`) resets to `▶FIGHT` at the start of each new battle, and remembers the last used quadrant within the same battle. The move menu (`FIGHT`) and Bag pocket (`ITEMS` / `POKé BALLS`) persist across battles.
- **Start Menu Cursor Memory (Turns 41–42, 296):** The Start menu remembers its cursor row index across openings. With the Pokédex obtained, rows are `0: POKéDEX`, `1: POKéMON` (current cursor position), `2: BAG`, `3: ORIQP`, `4: SAVE`, `5: OPTION`, `6: EXIT`.
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
  - **Northbound (Littleroot -> Oldale):** Enter at `(10, 19)` -> `Up` 4 to `(10, 15)` -> `Left` 4 to `(6, 15)` -> `Up` 4 to `(6, 11)` -> `Right` 4 to `(10, 11)` -> `Up` 1 to `(10, 10)` -> `Right` 7 to `(17, 10)` -> `Up` 6 to `(17, 4)` -> `Left` 6 to `(11, 4)` -> `Up` 5 into Oldale Town.
  - **Southbound (Oldale -> Littleroot):** Jump straight `Down` along `x=10` over the two south-facing ledges at `y=6` and `y=13`!
- **Oldale Town:**
  - South border (from Route 101): `(10, 19)` / `(11, 19)`.
  - Pokémon Center door: `(6, 16)` (approach along `y=17` from `(9, 17)` or `(11, 17)`, then step `Up` into `(6, 16)`).
  - Poké Mart door: `(14, 6)` (free Potion clerk started at `(13, 14)`, now stands at `(13, 7)`).
  - North border (to Route 103): `x=10, y=0` (transitions to `(10, 21)` on Route 103).

## Verified Findings (Turns 124–150)
- **Mudkip Growth & Modified Learnset (Turn 124):**
  - Uses the **Slow EXP group** (`5 * n^3 / 4`: 135 EXP for Lv. 5, 270 for Lv. 6, 428 for Lv. 7).
  - Learns `Bubble` (20 BP Water Special, 30 PP) at **Lv. 6** and `Mud Sport` (15 PP) at **Lv. 7**.
- **Wild Encounter Pools Observed:**
  - **Route 101 (Claimed by Starter):** Lv. 2–3 `Wurmple` (`Tackle`, `String Shot`), `Weedle` (`Poison Sting`, `String Shot`), `Caterpie` (`Tackle`, `String Shot`), `Pidgey`, `Sentret` (`Quick Attack`), `Rattata` (`Quick Attack`, `Tail Whip`), `Poochyena` (`Tackle`, `Howl`), `Zigzagoon` (`Swift`, `Sand-Attack`, holds `Berry Juice`), `Pichu` (`ThunderShock`, `Charm`, Ability: `Static`), `Togepi` (`Growl`, `Charm`, `Metronome`), `Igglybuff` (`Sing`, `Charm`). Note: The left northern grass patch sits at `x=4..6, y=2..4` while `x=7..10, y=1..4` is a grass-free corridor.
  - **Route 103:** Lv. 4 `Poliwag` (`Water Gun`, 44 EXP), `Skitty` (`Attract`), `Wingull` (`Water Gun`, `Wing Attack` 60 BP STAB, 10 Speed), `Ledyba` (`Silver Wind`), `Sunkern` (`Absorb`, `Growth`), `Spoink` (`Confusion`), `Ekans`, `Spearow`, `Hoppip`, `Mareep` (`ThunderShock`). Note: Bypass the lower ledge (`y=12`) grass-free via the 1-tile gap at `(14, 12)`.
- **Southbound Grass-Free Ledge Corridor & Mom's Heal (Turns 130–146):**
  - Walking straight `Down` along column **`x=10`** from `(10, 4)` on Route 103 jumps over both ledges (`y=5`, `y=12`) into Oldale Town with **0 grass tiles**.
  - Walking straight `Down` along column **`x=10`** across Route 101 jumps over both ledges (`y=6`, `y=13`) into Littleroot Town with **0 grass tiles**.
  - Inside the Littleroot 1F house (door `(5, 8)` -> mat `(8, 8)`), **Mom** sits at **`(2, 6)`** (talk from `(2, 5)` facing `Down`) and provides a free full HP + status heal.
- **Overworld Warp & Grass Timing Workarounds (Turns 124–149):**
  - Insert `["B", "sleep 800"]` (or `["B", "sleep 2500", "B"]`) between a door warp step and subsequent movement so the transition fade completes before walking.
  - Insert `"sleep 300"` before changing direction inside tall grass so the 4-frame grass-rustle animation does not drop the turn input.
- **Nickname Prompt Transition (Turn 207):** Pressing `A` on `"YES"` to nickname a Pokémon immediately opens the naming keyboard at `(0, 0) = 'A'`. Do not send an extra `A` before directional inputs on the naming grid, or it will type `'A'` as the first character.
- **Route 102 East Layout & Youngster Calvin (Turns 175–177):**
  - Enter Route 102 from Oldale Town `(0, 10)` at `(49, 10)`.
  - Grass-free path to Youngster Calvin: walk `Left` to `(38, 10)`, `Down` 4 tiles to `(38, 14)`, and `Left` 4 tiles to `(34, 14)`.
  - **Youngster Calvin** stands at **`(33, 14)`** facing `Down` and has 3 Lv. 6 Pokémon (`Sentret` [Assist->Rock Smash, Quick Attack], `Zigzagoon` [Swift], 3rd Pokémon with `Rock Smash`).

<hr>