# Nuzlocke Dashboard — Attempt #48

## Active Rules & Status
- **Attempt**: #48
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configure `TEXT SPEED: FAST` and `BATTLE STYLE: SET` via Start menu **once** inside the moving truck after `sleep 6500` or inside the Player's House 1F; never run the `OPTION` toggle twice as `Right` wraps `FAST -> SLOW` and `SET -> SHIFT`!)
- **Unlimited Items & In-Battle Bag Restriction**: Rare Candies & any Berries currently in the Bag (`Cheri Berry` x99 cures Paralysis [harvested at `(3, 25)` on Route 104 North], `Pecha Berry` x99 cures Poison [harvested at `(25, 2)` on Route 102 and `(24, 41)` on Route 104 South], `Oran Berry` x99 +10 HP [harvested at `(24, 2)` on Route 102], plus `Leppa Berry` x99 +10 PP if taken from a wild `Cleffa`) auto-refilled to 99 at the **turn boundary** in the overworld (never consume the last copy `x 1 -> x 0` of a newly harvested Berry before ending a turn in the free overworld!). **Using Berries/healing items directly from the Bag during battle is disabled** (selecting a Berry in battle only shows `>CANCEL`; Berries work as held items in battle or from the Bag in the overworld).

## Post-Mortem & Key Tactical Lessons (Attempts #1–#47)
- **Attempt #47 Lessons (Rustboro Gym EXP Buffers, `NEXT LV.` Verification & Roxanne `Lunatone` Baiting)**:
  1. **Never Let `Luvdisc` or `Wingull` Reach Lv 16 Before Rustboro City**: In Attempt #47, `Galatea` (`Luvdisc`) and `Zephyrus` (`Wingull`) reached Lv 16 on Route 104 North (`Twins Gina & Mia` and `PKMN Trainer Red`) and entered Rustboro Gym with ~470/653 EXP already filled, causing both of our `38–39 Speed` `Lunatone` counters to cross into Lv 17 against Tammy and Hiker Marc and get benched before Roxanne! Keep all pre-Roxanne encounters at **Lv 14–15** until arriving in Rustboro City, then use Rare Candies in Rustboro City so every Lv 16 party member starts Rustboro Gym with **`0 EXP` into Lv 16** (`full 585–817 EXP buffer`).
  2. **Check Exact `NEXT LV.` Integer EXP on the Pokemon Summary Screen (`Page 2`) Before Tammy & Hiker Marc**: Never estimate remaining EXP from EXP-bar pixels (`Oddish -> Gloom` is `Medium Slow` `585 EXP` at Lv 16, so `520 + 82 = 602 > 585` leveled `Rafflesia` to Lv 17 on Hiker Marc's `Cacnea` when a 4-way split of `62 EXP` would have kept `Rafflesia` at `582 / 585 EXP`!).
  3. **Never Finish Roxanne's `Lileep` with a `Poison`-Type While Back-Row Teammates Are at Low HP (`<=16 HP`)**: Finishing `#3 Lileep` with `Poison`-type `Nidorina` baited `#4 Lunatone` (`31–35 Speed`, `Confusion` deals `16 dmg` neutral / `32–38 dmg` `2x` super-effective) while `Marshtomp`, `Kabuto`, and `Azurill` were all at `10–12 HP`. Keep `38–39 Speed` `Luvdisc` (`2: Charm` + `3: Water Pulse`) and `Marshtomp` active and healthy (`>30 HP`) for Roxanne!
- **Attempt #46 Lessons (Post-Send-Out Burn/Poison Timing & Route 115 Fossil Capture)**:
  1. **Never Chain EXP Dismissal (`"B", "sleep 8000"`) and an In-Battle Party Switch When Active Pokemon Has `BRN` or `PSN`**: After a KO, the trainer's next send-out + `"is hurt by its burn/poison!"` takes `~9.5–10.5s` total; if `Down, Left, A` fires at `8.0s`, it is eaten during the burn tick and leaves the burned Pokemon in (costing `Aposeidon` vs Red's `Squirtle` on Turn 8649). Always wait until `"What will [POKEMON] do?"` is visually open on `<CurrentScreen>` before queuing a Party switch!
  2. **Buy 22+ Poke Balls at the Rustboro Mart & Never Switch a `Rock`-Weak `Flying`-Type into Route 115 `Kabuto`/`Omanyte`**: In Gen 3, critical hits ignore negative Attack stages (`-2 Attack` from `Charm`), so a crit `2x` `Rock Tomb` dealt 26+ dmg to `Hoothoot` on Turn 8668. Always buy 22+ Poke Balls at the Rustboro Mart `(16, 45)` upon arriving in Rustboro City, and keep `Water`-resisting `Luvdisc`/`Goldeen`/`Marshtomp` on the field the entire time while chipping `Kabuto`/`Omanyte` to `<20%` red HP and throwing `Great Ball` + `25+ Poke Balls`!
  3. **Keep `Luvdisc` at Lv 14–15 Through Route 104 North & Raise `Mudkip`, `Wingull`, and `Luvdisc` to Lv 10 Before Route 102**: Right after buying Poke Balls at the Oldale Mart `(14, 6)`, raise `Mudkip` to Lv 10 (`3 Rare Candies: Lv 7 -> Lv 10`) and heal at the Oldale Pokemon Center `(6, 16)` *before* stepping into the Route 103 tall grass; then raise the Route 103 and Littleroot Town encounters to Lv 10 before stepping into the Route 102 tall grass (and use `Mudkip`'s `3: Mud Sport` on Turn 1 against wild `Electrike`); and keep `Luvdisc` at Lv 14 until Rustboro City so she enters Rustboro Gym at Lv 16 with `0 EXP` (`full 653 EXP buffer`)!
- **Attempt #45 Route 102 Berry & Route 104 South Lessons**:
  1. **Always End a Turn in the Free Overworld After Picking Route 102 `Oran` & `Pecha` Berries Before Using/Giving Them**: If a turn times out while `"The soil returned to its soft and loamy state."` is still open on screen, the Berry stays at `x 2` and using `2` copies removes it from the Bag (`x 2 -> x 0`) before auto-refilling!
  2. **Always Return to the Petalburg City Pokemon Center After Catching the Route 104 Encounter at `(23, 60)`**: Raise all 6 party members to **Lv 13–14** with Rare Candies, heal to 100% HP, and equip held `Oran Berries` *before* stepping onto the Route 104 South beach to challenge Bird Keeper Billy `(17, 66)` and Fisherman Darian `(17, 59)`, and heal between Billy and Darian!
- **Attempt #44 Lesson**: Rival Brendan's Lv 5 `Treecko` on Route 103 holds a `Berry Juice` and knows `Quick Attack`, so two critical hits can beat an unboosted Lv 5 `Mudkip`. **Always feed 2 Rare Candies (`Lv 5 -> Lv 7`) to `Mudkip` right after exiting Professor Birch's Lab** before walking to Route 103 so Rival 1 is 100% crit-proof!
- **Attempts #34–#43 Consolidated Strategic Rules**:
  1. **Old Rod Timing**: Cycle **`[2500, 2900, 3300, 3700, 4100, 4500, 4900] * 2`** (`400ms` spacing across `3..10` dots, `< 550ms` bite window) to hit every active bite window without timing out.
  2. **Overworld & Cutscene Hygiene**: Never chain the Team Magma Grunt cutscene `(26, 23)` and Turn 1 battle inputs in one turn; never chain a `Pecha Berry` cure and a long overworld walk in one turn; and always walk `Down x2, Left x3, Down, Up` from the PC `(10, 2)` to Nurse Joy `(7, 4)`.
  3. **Pre-Roxanne EXP & Rustboro Gym Rules**:
     - Keep all 9 pre-Roxanne encounters at Lv 14–15 until Rustboro City (`Mudkip -> Marshtomp` is `Medium Slow` `~658 EXP` at Lv 16), then raise them to Lv 16 (`0 EXP` into Lv 16) in Rustboro City.
     - **School Kid Josh**: OHKO `#1 Geodude` on Turn 1 (`Selfdestruct`); counter `Rock/Grass` `#3 Sudowoodo` with `Voltorb`'s `20-fixed-damage SonicBoom`.
     - **School Kid Tammy**: Pivot `Marshtomp -> Gloom -> Luvdisc (4: Ice Beam)` on `#2 Yanma`, stay in with `36-Speed` `Luvdisc` (`3: Water Pulse`) to OHKO `#3 Rhyhorn` on Turn 1, split `#4 Corsola` EXP, and OHKO `#5 Larvitar` with `Sunflora`/`Gloom`.
     - **Bank `Marshtomp` Before Hiker Marc**: Once `Marshtomp` is within `<=360 EXP` of Lv 17 after Tammy, deposit `Marshtomp` in `BOX 1` before Hiker Marc so `Marshtomp` enters Roxanne active at Lv 16. Against Hiker Marc, OHKO `#1 Onix` from 100% HP with a `20+ Sp.Atk` STAB Water/Grass move (`Selfdestruct` + `Sitrus Berry`).
     - **Gym Leader Roxanne**: Never finish any of Roxanne's first 5 Pokemon with a `Poison`-, `Fighting`-, or `Bug`-type on the field (`baits #6 Lunatone early!`). Lead `Marshtomp` (`1: Mud Shot`) -> `Kabuto` (holding `Oran Berry`) on `#1 Nosepass` (`keeping Luvdisc unparalyzed`), drop `23+ Speed` `#4 Relicanth` to `-1 Speed` before switching in `Gloom`/`Weepinbell`, and outspeed `#6 Lunatone` (`31–35 Speed`) with `36+ Speed` `Luvdisc` (`2: Charm` cuts `75 BP Rock Slide` in half).
  4. **Post-Roxanne & Dewford Gym Rules (Lv 20 Cap)**:
     - Keep party at **Lv 17–18** through Route 116 & Rusturf Tunnel so they enter Dewford Island at **Lv 18–19** with a full 2-level EXP buffer before Lv 21.
     - Heal to 100% HP + re-equip `Oran Berries` at `(70, 19)` after catching Route 106 `Seel`, and bring `Thick Fat` `Spheal` (`takes 1 dmg from Aqua Grunt #4 Sneasel's Ice Beam; never switch a Ground-type into Sneasel's Ice Beam + Surf`).
     - In Dewford Gym, hit `Bulk Up` Fighting-types (`Makuhita`, `Guts Machoke`) with **Special** moves without inflicting status on `Guts Machoke`.

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