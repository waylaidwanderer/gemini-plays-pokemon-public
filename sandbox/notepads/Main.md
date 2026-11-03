# Nuzlocke Dashboard — Attempt #14

## Active Rules & Status
- **Attempt**: #14
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configure `TEXT SPEED: FAST` and `BATTLE STYLE: SET` via Start menu immediately upon arriving in the moving truck)
- **Unlimited Items & In-Battle Bag Restriction**: Rare Candies & any Berries currently in the Bag (`Cheri Berry` x99 cures Paralysis [harvested at `(3, 25)` on Route 104 North], `Pecha Berry` x99 cures Poison [harvested at `(25, 2)` on Route 102 and `(24, 41)` on Route 104 South], `Oran Berry` x99 +10 HP [harvested at `(24, 2)` on Route 102], plus `Leppa Berry` x99 +10 PP if taken from a wild `Cleffa`) auto-refilled to 99 at the **turn boundary** in the overworld (never consume the last copy `x 1 -> x 0` of a newly harvested Berry before ending a turn in the free overworld!). **Using Berries/healing items directly from the Bag during battle is disabled** (selecting a Berry in battle only shows `>CANCEL`; Berries work as held items in battle or from the Bag in the overworld).

## Post-Mortem & Key Tactical Lessons (Attempts #1–#11)
- **Attempt #1**: Wiped at Turn 497 against **PKMN Trainer Red** (`(29, 8)` on Route 104 North).
- **Attempt #2**: Wiped at Turn 864 in **Rustboro Gym** against **School Kid Tammy**'s Lv 15 `Rhyhorn` (`Megahorn`), because 5 of our living Pokemon (`Chloris`, `Ahecate`, `Thetis`, `Proteus`, `Eros`) had hit **Lv 17** and been benched under the Lv 16 Level Cap.
- **Attempt #3**: Wiped at Turn 1134 in **Rustboro Gym** against **Hiker Marc**'s Lv 14 `Kabuto` (`Giga Drain`, `Rock Tomb`, `Aerial Ace`, `20 Speed`).
- **Attempt #4**: Wiped at Turn 1408 in **Rustboro Gym** against **School Kid Tammy** after losing `Luvdisc` to overworld poison ticks in Petalburg Woods, losing wild Route 115 `Kabuto` to a chained chip+ball input, and losing `Mudkip` in School Kid Josh's battle due to an in-battle party slot swap (`Slot 1 <-> Slot 5`).
- **Attempt #5**: Defeated all 3 Rustboro Gym trainers (`Josh`, `Tammy`, `Marc`) for the first time and reached **Gym Leader Roxanne**, defeating her lead Lv 15 `Nosepass` and Lv 14 `Lileep` before wiping at Turn 1698 to her 3rd Pokemon, Lv 15 `Lunatone` (`Rock Slide`), because 4 of our living powerhouses had reached **Lv 17** prior to Roxanne.
- **Attempt #6**: Reset early on Route 102 at Turn 1758 after losing Lv 5 `Goldeen` to a wild Lv 6 `Spoink`.
- **Attempt #7**: Went 7-for-7 on catches with 0 deaths in 118 turns, but stepped onto `(26, 23)` in Petalburg Woods before pre-Magma-Grunt menu prep.
- **Attempt #8**: Went 7-for-7 on catches, reset at Turn 1976 in Petalburg Woods after losing `Oddish` to Bug Catcher James.
- **Attempt #9**: Went **9-for-9 on pre-Roxanne catches with 0 deaths**, cleared all 3 Rustboro Gym trainers, and reached **Gym Leader Roxanne** with a 5-Pokemon Lv 16 squad, defeating her lead `Nosepass` before wiping at Turn 2166 to her Lv 15 `Lunatone` (`Hypnosis` + `Confusion` + `Rock Slide`, `29 Speed`).
- **Attempt #10**: Reset on Route 102 at Turn 2213 after losing Lv 12 `Sandshrew` to Lass Tiana's `Sunkern`.
- **Attempt #11**: Reached Rustboro City with 0 deaths (discovering that `Azurill` learns `85 BP Body Slam` at Lv 15 which sweeps Lass Haley, Twins Gina & Mia alongside `Meowth`'s spread `Swift`, and PKMN Trainer Red, and that `Voltorb` is in the `Slow` EXP group [`1,021 EXP` buffer at Lv 16!] and learns `60 BP Shock Wave` + `20-fixed-damage SonicBoom` at Lv 15!), but reset at Turn 2372 in Rustboro Gym after:
  1. Chaining a Party switch (`SHIFT`) with a Poke Ball throw against wild Route 115 `Kabuto` (where `SHIFT + Rock Tomb + Speed fell` took `13.0s`, shifting `Up, Right` into the animation so `A, A` clicked `FIGHT -> Mega Drain`).
  2. Pressing `Up, Up` without `Left` first on the Party screen (`accidentally selecting Slot 1 EROS instead of Slot 6 CHLORIS`) and batching a PC interaction right after `Oddish -> Gloom`'s Lv 16 evolution (`where Magical Leaf's 3s fanfare caused the queued PC A presses to feed a 2nd Rare Candy to Lv 17`).
  3. Chaining `"B", "sleep 1500", "B", "sleep 5000"` (`to dismiss "Foe ARON fainted!" and "MARSHTOMP gained 267 EXP"`) with `"Down", "Left", "A"` (`to switch MARSHTOMP out on School Kid Tammy's Yanma`), where the `267 EXP` bar fill + `Yanma` send-out took `5.2s` instead of `5.0s`, so `"Down"` fired `0.17s` before `"What will MARSHTOMP do?"` opened and `"A"` clicked `FIGHT -> Mud Sport` instead of `POKEMON`, letting `Yanma` KO `Marshtomp` with `4x` `Giga Drain`.
- **Attempt #12**: Caught 7 encounters with 0 deaths (discovering that Route 103 `Skitty` holding a wild `Moon Stone` evolves into `Delcatty` with `50 HP, 32 Speed` at Lv 15 and `Sing` + `Attract` + `70 BP STAB Secret Power`, and that Route 104 `Snubbull` has `Intimidate` and learns `70 BP STAB Headbutt` at Lv 13), but reset at Turn 2471 in Petalburg Woods after leading pure-Water `Mudkip` against the Team Magma Grunt's lead `Magnemite` (`Thunder Wave` + `2x` `ThunderShock`) and leaving paralyzed `16/44 HP` `Mudkip` in to KO `Koffing`, allowing incoming `Houndour` (`Pursuit`) to outspeed paralyzed `Mudkip` and KO him after a Turn 1 full paralysis. Never lead pure-Water `Mudkip` into `Magnemite` (`Thunder Wave` + `ThunderShock`), and never leave a paralyzed or `< 75% HP` Pokemon in to KO `Koffing` before `Houndour` enters! Also, in Attempt #13 against Twins Gina & Mia (`2x` Lv 8 `Smeargle`), never bring a `Normal`-type (`2x` weak to Left `Smeargle`'s `150 BP Focus Punch`), as Right `Smeargle`'s `Teeter Dance` confuses both allies and a double confusion self-hit lets `Focus Punch` OHKO a `Normal`-type.
- **Attempt #13 (Full 6-Pokemon Roxanne Team Verified!)**: Went 9-for-9 on pre-Roxanne catches, cleared all 3 Rustboro Gym trainers (`Josh`, `Tammy`, `Marc`) with **0 deaths and all 8 living Pokemon at exact Lv 16**, leveled 4 Pokemon (`Marshtomp`, `Kabuto`, `Luvdisc`, `Makuhita`) to **Lv 17 mid-battle** against Gym Leader Roxanne, and defeated her first **5 Pokemon** (`1. Nosepass Lv 15`, `2. Lileep Lv 14`, `3. Anorith Lv 14`, `4. Relicanth Lv 14`, `5. Shuckle Lv 14`) with **all 6 of our Pokemon still alive** before wiping at Turn 2714 with her 6th and final Pokemon, `6. Lunatone Lv 15` (`Psychic` 90 BP, `Confusion` 50 BP, `Rock Slide` 75 BP, `Hypnosis`, `29 Speed`, holds `Sitrus Berry`), down to **29% yellow HP**. **CRITICAL LESSONS FOR ROXANNE IN ATTEMPT #14**:
  1. `Luvdisc` at Lv 16–17 has **`37–39 Speed` (`8–10 points FASTER than Lv 15 Lunatone's 29 Speed!`)**, and `Kabuto` at Lv 17 has **`28 Speed`**, but BOTH were paralyzed (`PAR` -> `9` and `7` Speed) because we switched them into `#1 Nosepass` (`Thunder Wave`)! Never switch `Luvdisc` into `Nosepass` (`lead Ground-type Marshtomp [immune to Thunder Wave!] and pivot to Kabuto holding a Cheri Berry on Nosepass, and use Kabuto on #3 Anorith so Marshtomp stays at 100% HP`), keeping **`Luvdisc` (`37–39 Speed`, holding `Oran Berry`, `Water Pulse`) 100% UNPARALYZED AND AT 100% FULL HP ON THE BENCH UNTIL `#6 LUNATONE` ENTERS** so `Luvdisc` outspeeds `Lunatone` (`39 > 29 Speed`) and 2HKOs it cleanly!
  2. `#5 Shuckle` uses **`Sunny Day`** (which halves `Water` moves by `0.5x` for 5 turns); always make sure `Sunny Day` has faded before `#6 Lunatone` enters so `Luvdisc`'s `Water Pulse` and `Marshtomp`'s `Water Gun` hit `Lunatone` at 100% full `2x` super-effective power!
- **Core Rules for Attempt #13 (Guaranteed 6v6 Lv 16 Squad vs Gym Leader Roxanne)**:
  1. **Strict Separation of Enemy Send-Outs, Party Switches, and Lv 16 Rare Candies**:
     - **NEVER chain `"B"` (dismissing `"fainted!"` / `"gained EXP"`) and a Party switch (`Down, Left, A`) in the same `press_buttons` call**! Always advance `"fainted!"` + `"gained EXP"` first so that the trainer's next Pokemon is visibly on the field and `"What will [POKEMON] do?"` is open at `+0.00s` on `<CurrentScreen>` before executing a Party switch!
     - **NEVER chain a Party switch (`SHIFT`) or chip attack with a Poke Ball throw in the same `press_buttons` call**!
     - **Standalone Lv 15 -> Lv 16 Rare Candy Rule**: Always raise Pokemon to **Lv 14–15** first (clamping with **`"Left"`** before any `Down * k` or `Up, Up`!) followed by an `8-B` Overworld Sync Barrier, and then execute each **Lv 15 -> Lv 16** Rare Candy in its own standalone `press_buttons` call with **NO** PC or second-slot `A` presses batched after it!
     - Never walk into wild grass or trainer battles with a Lv 11–12 Pokemon when the cap is Lv 16! Raise `Mudkip` to **Lv 13 (`36+ HP`)** in Birch's Lab and raise every newly caught Pokemon directly to **Lv 13–14** at `0` steps!
     - Never use `Select` move-swapping in battle; clamp explicitly on Turn 1 (`Up, Left` / `Up, Right` / `Up, Left, Down` / `Down, Right`), and when 2 Pokemon participated in a KO (`split EXP` = 2 `"gained EXP"` textboxes), wait for the 2nd send-out (`["B", "sleep 1200", "B", "sleep 5000"]`) before clamping to a new move slot! Against Bug Catcher James's lead `Paras` (`Bug/Grass`), always use a `4x` Flying move (`Peck` / `Wing Attack`) on Turn 1 to OHKO before `Spore`.
     - Keep all 9 pre-Roxanne encounters at **Lv 14–15** through Route 104 North (`PKMN Trainer Red`), then in Rustboro City Rare-Candy all 8–9 encounters to **Lv 16 (`0 EXP` into Lv 16!)** (`Mudkip -> Marshtomp` `1,021 EXP` buffer, `Oddish -> Gloom` / `Bellsprout -> Weepinbell` `585 EXP` buffer; always use **only `A` presses** after Rare Candy or in-battle level-ups so the ~15s evolution animation is never cancelled).
  2. **Exact Rustboro Gym EXP Budget (`3,773 EXP` Total Across Josh, Tammy, and Marc) to Keep All 6 Best Pokemon at Lv 16 for Roxanne**:
     - Use secondary encounters (#7, #8, #9 — e.g. `Wingull`, 2nd `Luvdisc`/`Azurill`, `Route 102`/`Route 104`/`Route 116` encounters) via PC rotation to absorb EXP on `Marc's Onix` (`346 EXP`), `Marc's Baltoy` (`148 EXP`), `Marc's Cacnea` (`248 EXP`), and split EXP on `Josh's Omanyte` / `Tammy's Corsola` / `Marc's Kabuto`, keeping our **Top 6 Roxanne Team** strictly `< Lv 17`:
       - **`Weepinbell` / `Gloom` (`0 / 585 EXP` buffer — `Medium Slow`)**:
         - **ONLY** use on the three `4x`-weak `Water/Rock` threats by **switching in (`50/50` EXP split!)**:
           1. `Josh`'s Lv 14 `Omanyte` (`360 / 2 = 180 EXP`)
           2. `Tammy`'s Lv 13 `Corsola` (`309 / 2 = 154 EXP`, note `Vine Whip` 2HKOs if low roll, taking 12 dmg from `Rock Tomb`)
           3. `Marc`'s Lv 14 `Kabuto` (`357 / 2 = 178 EXP`)
         - Total = **`180 + 154 + 178 = 512 / 585 EXP`** -> **Enters Gym Leader Roxanne at Lv 16 (`512/585 EXP`) and levels to Lv 17 after Roxanne's 1st Pokemon!**
       - **`Marshtomp` (`0 / 1,021 EXP` buffer — `Slow`)**:
         - Lead vs `Tammy`: OHKO `Aron` (`267 EXP`) with `Mud Shot`, switch out on `Yanma` (`345 / 2 = 172 EXP`), switch in on `Rhyhorn` (`432 / 2 = 216 EXP`) and OHKO with `Water Gun`, switch out on `Larvitar` (`213 / 2 = 106 EXP`) = **`761 / 1,021 EXP`** -> **Deposit/bench during Marc so `Marshtomp` enters Gym Leader Roxanne at Lv 16 (`761/1,021 EXP`) and levels to Lv 17 after Roxanne's 1st Pokemon (`Nosepass` gives `346 EXP`)!**
       - **`Omanyte` / `Kabuto` (`0 / 817 EXP` buffer — `Medium Fast`)**:
         - Use on `Josh`'s `Sudowoodo` (`346 EXP`) + `180 EXP` split from `Josh`'s `Omanyte` + `178 EXP` split from `Marc`'s `Kabuto` = **`704 / 817 EXP`** (let `Wingull` / 2nd `Luvdisc` / `Azurill` OHKO `Marc`'s `Onix` `346 EXP`!) -> **Enters Gym Leader Roxanne at Lv 16 (`704/817 EXP`), where `Omanyte`/`Kabuto`'s `41+ Defense` and `Rock` typing `0.5x` resists `Nosepass`'s `Selfdestruct` and `Lunatone`'s `Rock Slide`!**
       - **`Luvdisc #1` (`0 / 653 EXP` buffer — `Fast`)**:
         - Lead vs `Josh`: OHKO `Geodude` (`276 EXP`) with `Water Pulse`, 2HKO `Zubat` (`126 EXP`) with `Ice Beam`, and switch in to OHKO `Tammy`'s `Yanma` (`345 / 2 = 172 EXP`) with `Ice Beam` = **`574 / 653 EXP`** -> **Enters Gym Leader Roxanne at Lv 16 (`574/653 EXP`)!**
       - **`Slots 5 & 6 for Roxanne` (`Wingull` / `Azurill` / 2nd `Luvdisc` / `Grimer` [learns `90 BP` `Sludge Bomb` at Lv 13!] / `Phanpy` / `Cubone` / `Sandshrew`)**:
         - Rotate through `Box 1` between Josh, Tammy, and Marc so we walk up to **Gym Leader Roxanne** with a **full 6-Pokemon Lv 16 team**!
  3. **Respect Omniscient `Pursuit` AI, Cure Overworld Poison at `0` Steps & Never Chain Chip Moves With Poke Ball Throws**:
     - **CRITICAL OVERWORLD POISON RULE**: Overworld poison ticks for `1 HP` every `4 steps` and will kill a poisoned Pokemon (`0 HP` = Nuzlocke death). Cure poison with a `Pecha Berry` at `0` steps before walking anywhere! Against trainers who have both a `Toxic` user (`Koffing`) and a `Pursuit` user (`Houndour`), switch the `Toxic`-poisoned Pokemon out *before* KOing the `Toxic` user so `Houndour` cannot trap it at low HP.
     - **Never chain a damaging chip attack and a Poke Ball throw in the same `press_buttons` call**.
     - **In-Battle Party Slot Swap Rule & `Set`-Mode 3-Way EXP Split Pivot**: Every in-battle switch swaps the incoming Pokemon with `Slot 1` (`gPlayerParty[0]`) for the remainder of that battle, reverting to the pre-battle overworld order when the battle ends (`B_OUTCOME_WON`). In `Set` mode, the Pokemon that KOs enemy #N automatically faces enemy #(N+1) on Turn 1; if its remaining Lv 16 EXP buffer is smaller than a 50/50 split (`EXP // 2`), pivot through a high-buffer teammate (`A -> B -> C`) so enemy #(N+1)'s EXP is divided **3 ways (`EXP // 3`)** instead of 2!
  4. **9 Pre-Roxanne Encounter Locations** (Note: `Starter` is met on `Route 101`, so `Route 101` wild catches are NOT permitted):
     1. `Starter` (`Route 101` — `Mudkip`)
     2. `Littleroot Town` (Old Rod at `(17, 13)` facing `Right` — `Luvdisc`)
     3. `Route 103` (tall grass)
     4. `Route 102` (tall grass)
     5. `Petalburg City` (Old Rod at `(11, 22)` facing `Down` — `Luvdisc` / `Azurill`)
     6. `Route 104` (tall grass at `(22..24, 56..61)`)
     7. `Petalburg Woods` (tall grass — `Oddish` / `Bellsprout` / `Phanpy`)
     8. `Route 116` (tall grass at `(4, 13..15)` — `Grimer` learns `Sludge Bomb` at Lv 13; `Yanma` learns `SonicBoom` at Lv 13; `Makuhita` learns `Vital Throw` at Lv 13)
     9. `Route 115` (Old Rod at `(7, 71)` facing `Left` on trainer-free southern beach — `Kabuto` / `Omanyte`)

## Level Cap Schedule
1. **Roxanne (Rustboro Gym)**: Lv 16
2. **Brawly (Dewford Gym)**: Lv 20
3. **Wattson (Mauville Gym)**: Lv 29
4. **Flannery (Lavaridge Gym)**: Lv 42
5. **Norman (Petalburg Gym)**: Lv 48
6. **Winona (Fortree Gym)**: Lv 55
7. **Tate & Liza (Mossdeep Gym)**: Lv 70
8. **Wallace / Juan (Sootopolis Gym)**: Lv 77
9. **Champion (Pokemon League)**: Lv 100

## Notepad Index
- `Locations/Encounters`: Route-by-route Nuzlocke encounter tracking & status
- `Mechanics/UI_And_Tools`: Verified menu, Bag, fishing, and overworld mechanics
- `Scratchpad/Routing`: Verified early-game maps, trainers, and routing