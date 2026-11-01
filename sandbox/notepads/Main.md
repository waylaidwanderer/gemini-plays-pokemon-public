# Nuzlocke Dashboard — Attempt #5

## Active Rules & Status
- **Attempt**: #5
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configure `TEXT SPEED: FAST` and `BATTLE STYLE: SET` via Start menu immediately upon arriving in the moving truck)
- **Unlimited Items & In-Battle Bag Restriction**: Rare Candies & any Berries currently in the Bag (`Cheri Berry` x99 cures Paralysis [harvested at `(3, 25)` on Route 104 North], `Pecha Berry` x99 cures Poison [harvested at `(25, 2)` on Route 102 and `(24, 41)` on Route 104 South], `Leppa Berry` x99 +10 PP [taken from wild Route 101 `Cleffa`], `Oran Berry` x99 +10 HP) auto-refill to 99 at the **turn boundary** in the overworld (never consume the last copy `x 1 -> x 0` of a newly harvested Berry before ending a turn in the free overworld!). **Using Berries/healing items directly from the Bag during battle is disabled** (selecting a Berry in battle only shows `>CANCEL`; Berries work as held items in battle or from the Bag in the overworld).

## Post-Mortem & Key Tactical Lessons (Attempts #1–#4)
- **Attempt #1**: Wiped at Turn 497 against **PKMN Trainer Red** (`(29, 8)` on Route 104 North).
- **Attempt #2**: Wiped at Turn 864 in **Rustboro Gym** against **School Kid Tammy**'s Lv 15 `Rhyhorn` (`Megahorn`), because 5 of our living Pokemon (`Chloris`, `Ahecate`, `Thetis`, `Proteus`, `Eros`) had hit **Lv 17** and been benched under the Lv 16 Level Cap.
- **Attempt #3**: Wiped at Turn 1134 in **Rustboro Gym** against **Hiker Marc**'s Lv 14 `Kabuto` (`Giga Drain`, `Rock Tomb`, `Aerial Ace`, `20 Speed`).
- **Attempt #4**: Wiped at Turn 1408 in **Rustboro Gym** against **School Kid Tammy** after losing `Luvdisc` to overworld poison ticks in Petalburg Woods, losing wild Route 115 `Kabuto` to a chained chip+ball input after `Rock Tomb`'s speed-drop textbox, losing unevolved Lv 15 `Mudkip` in School Kid Josh's battle due to an in-battle party slot swap (`Slot 1 <-> Slot 5`) into `Zubat`'s `Giga Drain`, and losing `Azurill` (pure Normal-type, weak to `Brick Break`) and `Yanma` (`4x` weak to `Rock Tomb`) to Tammy's lead Lv 13 `Aron`.
- **Core Rules for Attempt #5**:
  1. **Evolve `Mudkip -> Marshtomp` (`1,021 EXP` buffer!) and `Oddish -> Gloom` / `Bellsprout -> Weepinbell` (`763 EXP` buffer!) to Lv 16 With Rare Candies BEFORE Entering Rustboro Gym**:
     - In this ROM hack, `Mudkip -> Marshtomp`, `Oddish -> Gloom`, and `Bellsprout -> Weepinbell` all evolve at **Lv 16**! Always use **only `A` presses** (never `B`) after Rare Candy or in-battle level-ups so the ~15s evolution animation is never cancelled.
     - Keep `Mudkip` and your Grass-type at **Lv 14–15** through Route 104 North (`PKMN Trainer Red`), then feed Rare Candies in the overworld right before Rustboro Gym so they evolve into **Lv 16 `Marshtomp` (`0/1,021 EXP` into Lv 16!)** and **Lv 16 `Gloom`/`Weepinbell` (`0/763 EXP` into Lv 16!)** with **0 EXP into Lv 16**!
     - Never do multi-turn in-battle switches to split EXP (which gives opponents free `Hypnosis`/`Rock Tomb`/`Brick Break` turns and scrambles `gPlayerParty` slot indices via `Slot 1 <-> Slot k` swaps). Instead, assign each Rustboro Gym Trainer Pokemon to a dedicated OHKO/2HKO counter:
       - **School Kid Josh (`(5, 14)`, 4 Pokemon)**:
         - Lead with **Lv 16 `Luvdisc`** (`0/653 EXP`, `Water Pulse` Lv 12 + `Ice Beam` Lv 16, `~40+ Speed`) or **Lv 16 `Kabuto`** (`0/817 EXP`, `Water Pulse` + `Mega Drain` Lv 13) to OHKO `Geodude` (`276 EXP`) with `Water Pulse`, 2HKO `Zubat` (`126 EXP`, `Hypnosis`/`Giga Drain`/`Aerial Ace`) with `Ice Beam`/`Rock Tomb`, and 2HKO `Sudowoodo` (`346 EXP`), while **Lv 16 `Gloom`/`Weepinbell`** (`0/763 EXP`) or `Kabuto` OHKOs `Omanyte` (`360 EXP`) with `4x Mega Drain`!
       - **School Kid Tammy (`(5, 12)`, 5 Pokemon)**:
         - Lead with **Lv 16 `Marshtomp`** (`0/1,021 EXP`, `25+ Speed`, `Water Gun`/`Mud Shot`)! `Marshtomp` outspeeds and OHKOs `Aron` (`267 EXP`, knows `Brick Break` & `Rock Tomb`), `Rhyhorn` (`432 EXP`, knows `Megahorn`, `Magnitude`, `Ice Beam`), and `Larvitar` (`~300 EXP`, knows `Earthquake`) for `267 + 432 + 300 = 999 / 1,021 EXP` (staying at Lv 16!).
         - Switch in `Luvdisc` (`Ice Beam`) or `Yanma` (`SonicBoom`) against Tammy's Lv 11 `Yanma` (`345 EXP`), and `Gloom`/`Weepinbell` or `Kabuto` (`4x Mega Drain`) against Tammy's Lv 13 `Corsola` (`312 EXP`, knows `Aurora Beam`, `Rock Tomb`, `Water Pulse`).
       - **Hiker Marc (`(1, 8)`, 5 Pokemon)**:
         - Temporarily deposit `Marshtomp` (`999/1,021 EXP`) into `Box 1` during the Pokemon Center heal after Tammy!
         - Use **Lv 16 `Gloom`/`Weepinbell`** (`360/763 EXP`, `4x Mega Drain`) to OHKO Marc's Lv 14 `Kabuto` (`357 EXP`), and use `Luvdisc` / `Kabuto` / remaining Water/Grass/Rock answers (`Water Pulse`, `Mega Drain`, `BubbleBeam`) to sweep Marc's `Onix` (`346 EXP`) and remaining Rock/Ground Pokemon!
       - **Gym Leader Roxanne**:
         - Withdraw `Marshtomp` (`Lv 16`) and all 6 best Lv 16 Pokemon from `Box 1` before walking up to Roxanne (since party members at `<= Lv 16` when a Boss battle starts may legally level up to Lv 17+ during the Boss battle!).
  2. **Respect Omniscient `Pursuit` AI, Cure Overworld Poison at `0` Steps & Never Chain Chip Moves With Poke Ball Throws**:
     - **CRITICAL OVERWORLD POISON RULE**: Overworld poison ticks for `1 HP` every `4 steps` and will kill a poisoned Pokemon (`0 HP` = Nuzlocke death). Whenever ANY party member is poisoned (`PSN`) at the end of a battle, **NEVER chain overworld walking after the battle**—always cure poison with a `Pecha Berry` at `0` steps before walking anywhere!
     - **Never chain a damaging chip attack and a Poke Ball throw in the same `press_buttons` call** (extra stat-drop/crit textboxes shift turn timing and turn the queued `BAG -> POKE BALL` input into a 2nd `FIGHT` attack). Always execute the chip move alone, verify HP on the next turn, and then throw Poke Balls.
     - **In-Battle Party Slot Swap Rule**: Every in-battle switch swaps the incoming Pokemon with `Slot 1` (`gPlayerParty[0]`). Always track `Slot 1 <-> Slot k` swaps when switching in battle.
  3. **10 Pre-Roxanne Encounter Locations**:
     1. `Starter` (Route 101 bag — `Mudkip`)
     2. `Littleroot Town` (Old Rod at `(17, 13)` facing `Right` — `Luvdisc`)
     3. `Route 101` (tall grass at `x=5, y=14..16`)
     4. `Route 103` (tall grass)
     5. `Route 102` (tall grass)
     6. `Petalburg City` (Old Rod at `(12, 23)` facing `Left` — `Luvdisc` / `Azurill`)
     7. `Route 104` (tall grass at `(22..24, 56..61)`)
     8. `Petalburg Woods` (tall grass — `Oddish` / `Bellsprout` / `Phanpy`)
     9. `Route 116` (tall grass at `(4, 13..15)`)
     10. `Route 115` (Old Rod at `(7, 71)` facing `Left` on trainer-free southern beach — `Kabuto`)

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