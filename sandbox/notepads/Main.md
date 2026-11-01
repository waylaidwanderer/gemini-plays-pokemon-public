# Nuzlocke Dashboard — Attempt #3

## Active Rules & Status
- **Attempt**: #3
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configure `TEXT SPEED: FAST` and `BATTLE STYLE: SET` via Start menu immediately upon arriving in the moving truck)
- **Unlimited Items & In-Battle Bag Restriction**: Rare Candies & any Berries currently in the Bag (`Cheri Berry` x99 cures Paralysis [harvested at `(3, 25)` on Route 104 North], `Pecha Berry` x99 cures Poison, `Oran Berry` x99 +10 HP) auto-refill to 99 at the **turn boundary** in the overworld (never consume the last copy `x 1 -> x 0` of a newly harvested Berry before ending a turn in the free overworld!). **Using Berries/healing items directly from the Bag during battle is disabled** (selecting a Berry in battle only shows `>CANCEL`; Berries work as held items in battle or from the Bag in the overworld).

## Post-Mortem & Key Tactical Lessons (Attempts #1 & #2)
- **Attempt #1**: Wiped at Turn 497 against **PKMN Trainer Red** (`(29, 8)` on Route 104 North).
- **Attempt #2**: Wiped at Turn 864 in **Rustboro Gym** against **School Kid Tammy**'s Lv 15 `Rhyhorn` (`Megahorn`), because 5 of our living Pokemon (`Chloris`, `Ahecate`, `Thetis`, `Proteus`, `Eros`) had hit **Lv 17** and been benched under the Lv 16 Level Cap, leaving only `Hermes` (Lv 16 Meowth) usable.
- **Core Rules for Attempt #3**:
  1. **Strict Level Cap Buffer Management (Do Not Pre-Level to Lv 16 Too Early!)**:
     - Level party members to **Lv 12–13** for early routes (`Route 102`, `Route 104 South`), **Lv 14** for `Petalburg Woods` and `Route 104 North`, and **Lv 14–15** for **PKMN Trainer Red** (`(29, 8)` on Route 104 North; defeated easily in Attempt #2).
     - **DO NOT fight ANY trainers on Route 116 before defeating Roxanne!** Only catch the Route 116 wild encounter in the western tall grass at `(4, 13)` and the Route 115 Old Rod encounter on the trainer-free southern beach at `(7, 71)`. Save all Route 116 trainers until after defeating Roxanne (when the Level Cap advances to **Lv 20** and `HM01 Cut` unlocks the `Chesto Berry` patch at `(19..20, 2)`).
     - **Enter Rustboro Gym with a full 6-Pokemon party at Lv 14–15** (never Lv 16!) so your team has `6,000+ EXP` of buffer to clear the Gym Trainers (`School Kid Josh` gives `1,108 EXP` across 4 Pokemon; `School Kid Tammy` gives `~800 EXP` across 3 Pokemon), and **only Rare-Candy up to Lv 16 when standing directly in front of Gym Leader Roxanne!**
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