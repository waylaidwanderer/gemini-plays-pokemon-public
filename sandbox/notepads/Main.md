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
1. **APOSEIDON** (Mudkip ♂) — Lv. 11 (1800 EXP) | HP: 7/33 | Nature: Gentle (+SpD, -Def) | Ability: Torrent | Stats: 21 Atk / 16 Def / 18 SpA / 17 SpD / 16 Spd | Moves: Tackle (35 PP), Bubble (30 PP), Mud Sport (15 PP), Water Gun (25 PP)
- *Note: Deposit deceased APOLLO (Lv. 4 Ralts) into the PC Graveyard box at the Petalburg / Oldale Pokémon Center.*

## Notepad Index
- `Main`: High-level dashboard, party summary, level caps, and core tactical rules.
- `Locations/Encounters`: Route-by-route encounter tracking.
- `Mechanics/Graveyard`: Fallen Pokémon, wipe post-mortems, and run history.
- `Mechanics/UIAndControls`: Verified naming keyboard grid, warp/cutscene scripting patterns, Pokémon Center healing formula, and Littleroot/Route 101/Oldale/Route 103 coordinates.