# Nuzlocke Dashboard — Attempt #45

## Active Rules & Status
- **Attempt**: #45
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configure `TEXT SPEED: FAST` and `BATTLE STYLE: SET` via Start menu **once** inside the moving truck after `sleep 6500` or inside the Player's House 1F; never run the `OPTION` toggle twice as `Right` wraps `FAST -> SLOW` and `SET -> SHIFT`!)
- **Unlimited Items & In-Battle Bag Restriction**: Rare Candies & any Berries currently in the Bag (`Cheri Berry` x99 cures Paralysis [harvested at `(3, 25)` on Route 104 North], `Pecha Berry` x99 cures Poison [harvested at `(25, 2)` on Route 102 and `(24, 41)` on Route 104 South], `Oran Berry` x99 +10 HP [harvested at `(24, 2)` on Route 102], plus `Leppa Berry` x99 +10 PP if taken from a wild `Cleffa`) auto-refilled to 99 at the **turn boundary** in the overworld (never consume the last copy `x 1 -> x 0` of a newly harvested Berry before ending a turn in the free overworld!). **Using Berries/healing items directly from the Bag during battle is disabled** (selecting a Berry in battle only shows `>CANCEL`; Berries work as held items in battle or from the Bag in the overworld).

## Post-Mortem & Key Tactical Lessons (Attempts #1–#45)
- **Attempt #45 Route 104 South Lesson**: Always raise all active party members (including `Triton`, `Galatea`, `Artemis`, and `Mudkip`) to **Lv 12–14** with Rare Candies and heal to 100% HP right after catching the Route 104 encounter at `(23, 60)` *before* stepping onto the `x=17` beach path where Bird Keeper Billy `(17, 66)` and Fisherman Darian `(17, 59)` trigger.
- **Attempt #44 Lesson**: Rival Brendan's Lv 5 `Treecko` on Route 103 holds a `Berry Juice` and knows `Quick Attack`, so two critical hits can beat an unboosted Lv 5 `Mudkip`. **Always feed 2 Rare Candies (`Lv 5 -> Lv 7`) to `Mudkip` right after exiting Professor Birch's Lab** before walking to Route 103 so Rival 1 is 100% crit-proof!
- **Attempts #34–#43 Consolidated Strategic Rules**:
  1. **Old Rod Timing**: Cycle **`[2500, 3150, 3850, 4500] * 4`** (`or * 3`) to hit every 2-dot bite window before timeout.
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