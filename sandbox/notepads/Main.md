# Nuzlocke Dashboard — Attempt #4

## Active Rules & Status
- **Attempt**: #4
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configure `TEXT SPEED: FAST` and `BATTLE STYLE: SET` via Start menu immediately upon arriving in the moving truck)
- **Unlimited Items & In-Battle Bag Restriction**: Rare Candies & any Berries currently in the Bag (`Cheri Berry` x99 cures Paralysis [harvested at `(3, 25)` on Route 104 North], `Pecha Berry` x99 cures Poison [harvested at `(25, 2)` on Route 102 and `(24, 41)` on Route 104 South], `Oran Berry` x99 +10 HP) auto-refill to 99 at the **turn boundary** in the overworld (never consume the last copy `x 1 -> x 0` of a newly harvested Berry before ending a turn in the free overworld!). **Using Berries/healing items directly from the Bag during battle is disabled** (selecting a Berry in battle only shows `>CANCEL`; Berries work as held items in battle or from the Bag in the overworld).

## Post-Mortem & Key Tactical Lessons (Attempts #1, #2 & #3)
- **Attempt #1**: Wiped at Turn 497 against **PKMN Trainer Red** (`(29, 8)` on Route 104 North).
- **Attempt #2**: Wiped at Turn 864 in **Rustboro Gym** against **School Kid Tammy**'s Lv 15 `Rhyhorn` (`Megahorn`), because 5 of our living Pokemon (`Chloris`, `Ahecate`, `Thetis`, `Proteus`, `Eros`) had hit **Lv 17** and been benched under the Lv 16 Level Cap, leaving only `Hermes` (Lv 16 Meowth) usable.
- **Attempt #3**: Defeated **School Kid Josh** and **School Kid Tammy** in Rustboro Gym, but wiped at Turn 1134 against the 3rd Gym Trainer, **Hiker Marc** at `(1, 8)`, specifically to his Lv 14 `Kabuto` (`75 BP / 10 PP Giga Drain`, `Rock Tomb`, `Aerial Ace`, `20 Speed`), because we kept `Mudkip` unevolved at Lv 15 (fainting to Tammy's Lv 15 `Larvitar`'s `Earthquake`) and spent multiple turns pivoting around `Kabuto` to split its EXP instead of rotating high-EXP Lv 16s through the PC between Gym Trainers.
- **Core Rules for Attempt #4**:
  1. **Strict Level Cap Buffer Management & Rustboro Gym 3-Trainer PC Rotation**:
     - Level party members to **Lv 12–13** for early routes (`Route 102`, `Route 104 South`), **Lv 14** for `Petalburg Woods` and `Route 104 North`, and **Lv 14–15** for **PKMN Trainer Red** (`(29, 8)` on Route 104 North; defeated easily in Attempts #2 and #3).
     - **DO NOT fight ANY trainers on Route 116 before defeating Roxanne!** Only catch the Route 116 wild encounter in the western tall grass at `(4, 13)` and the Route 115 Old Rod encounter on the trainer-free southern beach at `(7, 71)`. Save all Route 116 trainers until after defeating Roxanne (when the Level Cap advances to **Lv 20** and `HM01 Cut` unlocks the `Chesto Berry` patch at `(19..20, 2)`).
     - **Enter Rustboro Gym with a full 6-Pokemon party at Lv 15–16 and rotate high-EXP Lv 16s through the PC between the 3 Gym Trainers (`Josh -> Tammy -> Marc -> Roxanne`)**:
       - Rustboro Gym has **3 mandatory trainers** before Roxanne: **School Kid Josh** at `(5, 14)` (`4 Pokemon, 1,108 EXP`), **School Kid Tammy** at `(5, 12)` (`5 Pokemon, ~1,568 EXP`, ends with Lv 15 `Larvitar` with `18+ Speed` and `Earthquake`), and **Hiker Marc** at `(1, 8)` (`5 Pokemon`, leads with Lv 15 `Onix` 346 EXP and Lv 14 `Kabuto` 357 EXP with `75 BP / 10 PP Giga Drain`, `Rock Tomb`, `Aerial Ace`, and `20 Speed`).
       - **Evolve `Mudkip -> Marshtomp` at Lv 16** (`0 EXP` into Lv 16 = `763 EXP` buffer before Lv 17!) before fighting **School Kid Tammy** so `Marshtomp` (`23+ Speed`, `53+ HP`, `Mud Shot`) outspeeds and OHKOs Tammy's `Aron`, `Rhyhorn`, and `Larvitar` (`18+ Speed`, `Earthquake`).
       - **Never do multi-turn in-battle pivots to split EXP!** Instead, OHKO/2HKO every Gym Trainer Pokemon directly, and during your Pokemon Center heal trip between `Josh`, `Tammy`, and `Marc`, temporarily deposit any Lv 16 Pokemon whose EXP bar is >50% full into `Box 1` (swapping in a fresh Lv 15–16 encounter from `Box 1`), then withdraw your 6 best Lv 16 Pokemon right before walking up to **Gym Leader Roxanne**!
  2. **Respect Omniscient `Pursuit` AI & Never Blind-Chain Battle Turns**:
     - Enemy AI predicts player switches and **always clicks `Pursuit` (`80 BP` doubled)** if you switch out against a Pokemon that knows `Pursuit` (such as Petalburg Woods Magma Grunt's Lv 9 `Houndour`). Never switch out against a `Pursuit` user unless the active Pokemon can safely tank an `80 BP` STAB `Pursuit`.
     - **Never start a trainer battle AND clamp move slots in the same blind `press_buttons` call** (if `sleep 5500` runs before `"[TRAINER] would like to battle!♥"` is dismissed, your move-slot clamp fires during the send-out animation and defaults to Move Slot 1). Instead, advance the trainer intro with `["B", "sleep 1200"] * 10` so you visually confirm `"What will [POKEMON] do?"` first, and only execute 1–3 combat turns per turn so you can react to status/damage.
  3. **9 Pre-Roxanne Encounter Locations**:
     1. `Starter` (Route 101 bag)
     2. `Littleroot Town` (Old Rod at `(17, 13)` facing `Right`)
     3. `Route 101` (tall grass at `x=5, y=14..16`)
     4. `Route 103` (tall grass)
     5. `Route 102` (tall grass)
     6. `Petalburg City` (Old Rod at `(12, 23)` facing `Left`)
     7. `Route 104` (tall grass at `(22..24, 56..61)`)
     8. `Petalburg Woods` (tall grass)
     9. `Route 116` (tall grass at `(4, 13..15)`)
     10. `Route 115` (Old Rod at `(7, 71)` facing `Left` on trainer-free southern beach)

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