# Pokémon Emerald Nuzlocke — Main Dashboard

## Run Status
- **Game:** Pokémon Emerald (Emerald Kaizo / Modified ruleset: In-battle Bag healing items are DISABLED [Cancel only]; wild/trainer Pokémon have custom movesets & held items!)
- **Player Name:** ORION (Boy / Brendan)
- **Attempt:** #6
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

## Key Tactical Rules (Learned from Attempts #1–#4)
- **Deterministic Bounded 2x2 Move Selection (Verified Turn 328):** Opening the Bag or Party menu in the overworld resets the in-battle move cursor to Slot 1 (`Tackle`). Because the 2x2 move grid does not wrap, **ALWAYS press `Down, Right` for Slot 4 (`Water Gun`), `Up, Right` for Slot 2 (`Bubble`), and `Up, Left` for Slot 1 (`Tackle`)**!
- **Starter Claims Route 101 (Verified Turn 141):** Because the starter's summary reads `Met in ROUTE 101`, the Nuzlocke harness treats Route 101 as already used and blocks Poké Ball throws on Route 101.
- **Lowered Wild Catch Rates & Crit Range Rule (Turns 158–161, 252, 293):** Poké Balls thrown at **Green HP (`>50%`)** pop out on Shake 0 in this ROM. Always weaken wild encounters into **Yellow (`<50%`) or Red (`<20%`) HP** before throwing a Poké Ball, and immediately `RUN` if HP drops into `2x` enemy attack damage (crit range).
- **Modified Move Mechanics (Turns 169, 384):**
  - `Yawn` inflicts Sleep (`SLP`) immediately on the turn it is used.
  - `Silver Wind` (`Ledyba` on Route 103) has a **100% omni-boost rate** (`+1 Atk/Def/SpA/SpD/Spd` on every hit).
- **Route 102 Trainer Teams (Verified Turns 177–182, 303–328, 537–570):**
  1. **Youngster Calvin `(33, 14)`:** 3 Lv. 6 Pokémon (`Sentret` [Assist->Rock Smash / Mud-Slap, Quick Attack], `Zigzagoon` [Swift], `Poochyena` [Rock Smash, Howl]).
  2. **Bug Catcher Rick `(25, 15)`:** 4 Lv. 5 Pokémon (`Caterpie`, `Wurmple`, `Kakuna` [holds `Berry Juice`, Poison Sting], `Cascoon` [holds `Berry Juice`, Iron Defense, Tackle]).
  3. **Lass Tiana `(15, 5)`:** 3 Pokémon (`Lv. 6 Igglybuff` [`Cute Charm` contact infatuation, holds `Oran Berry`, uses `Present` — **use non-contact `Water Gun` (`Down, Right`)!**], `Lv. 6 Sunkern` [holds `Berry Juice`, knows `Leech Seed`, `Protect`, `Mega Drain` — **counter with `Liquid Ooze` `GULPIN` (`Acid`) or physical `Tackle`!**], `Lv. 5 Togepi`).
  4. **Bug Catcher Allen `(13, 2)`:** Faces `Down` at the western exit of Route 102; has **4 Lv. 7 Pokémon** (`Weedle` [`Poison Sting`], `Silcoon` [holds `Sitrus Berry`, `Iron Defense`], `Wurmple` [`Tackle`], `Metapod`).
- **Route 104 (South) Trainer Teams & Berries (Verified Turns 599–653, 886–913):**
  - **Bird Keeper Billy `(23, 66)`:** Turns toward footsteps on sand; has 3 Lv. 7 Pokémon (`Pidgey` [`Sand-Attack`], `Wingull` [holds `Oran Berry`, `Supersonic`, `Gust`, `Water Gun`], `Taillow`).
  - **Fisherman Darian `(15, 59)`:** Mandatory trainer facing `Right` across the 3-tile beach bottleneck `x=16..18, y=59`; has **4 Pokémon** (`Lv. 9 Magikarp` [`Bounce`, `Tackle`], `Lv. 8 Feebas` [holds `Sitrus Berry` +30 HP, knows `Yawn`/`Hypnosis`, `Water Pulse`, `Facade` — OHKO'd from 100% to 0 HP by Lv. 13 `ATHENA`'s STAB `Secret Power`!], `Lv. 7 Goldeen` [holds `Berry Juice`, `Rain Dance`, `Peck`, `Swift Swim`], and `Lv. 7 Luvdisc`).
  - **Northern Route 104 South Berries & Lady Cindy `(11, 40)`:** Berry trees at `(22, 41)` (`2 Oran Berries`) and `(24, 41)` (`2 Pecha Berries`) north of Mr. Briney's Cottage. **Lady Cindy `(11, 40)`** guards the Petalburg Woods entrance and has **3 Pokémon** (`Lv. 8 Cleffa`, `Lv. 8 Pichu`, `Lv. 7 Azurill`, `$1,400` payout).
- **Petalburg Woods Trainers (Verified Turns 920–925):**
  1. **Bug Maniac Lyle `(13, 35)`:** Faces `Up` near the south entrance; has **3 Lv. 8 Pokémon** (`Spinarak`, `Ledyba`, `Venonat`).
  2. **Bug Catcher James `(10, 24)`:** Faces `Down`; has **3 Pokémon** (`Lv. 9 Paras`, `Lv. 8 Surskit`, `Lv. 9 Nincada` [`Giga Drain`, `Scratch`]).
  3. **Team Magma Grunt `(26, 23)`:** Cutscene triggers along `x=26..28, y=23`; has **4 Pokémon** (leads with `Lv. 8 Magnemite`).
- **Level 15 Cap Management Plan (Roxanne Cap = Lv. 15):**
  - `ATHENA` (Lv. 15, `61 / 721 EXP` into Lv. 15 = `660 EXP` headroom before Lv. 16) will defeat the Team Aqua Grunt in Petalburg Woods (or pivot to `MUDKIP` on Water-weak foes), after which the Devon Researcher heals the party to 100% HP/PP.
  - Immediately after the Team Aqua Grunt battle, swap **`MUDKIP` (`Lv. 10`) into Party Slot 1** so `ATHENA` never reaches Lv. 16 before Roxanne, and feed all remaining trainers and wild encounters on Route 104 North / Route 116 to **`MUDKIP` (to reach Lv. 14–15 for Roxanne)** and **`CIRCE` / `NOCTIS`**.
- **Oldale & Petalburg Mart Prices (Turns 153, 593):** Poké Balls cost only **$10** each (10+ awards a Premier Ball); Potions cost $300; Antidotes cost $100; Parlyz Heals cost $200; Awakenings cost $250; Repels cost $350.
- **Heal in Overworld to 100% HP & Equip Oran Berries:** Bag Potions cannot be used in battle, but held `Oran Berries` (`(24, 2)` on Route 102 and `(22, 41)` on Route 104 South) activate automatically in battle!
- **Train Caught Teammates to Lv. 10–12 Before Trainers:** Never bring a base-level (Lv. 4–7) catch into Route 102 or Route 104 trainer battles. Train our caught teammates up to **Lv. 10–12** alongside the starter before challenging route trainers.

## Active Party (`BATTLE STYLE: SET`, `START` cursor on Row 2 `BAG`)
1. **ATHENA** — Spearow ♀ (Lv. 15 [AT CAP: `61/721 EXP`], `21/39 HP` [`PAR`], Rash, `Keen Eye`, Stats: `39 HP / 27 Atk / 14 Def / 18 SpA / 16 SpD / 29 Spd`, Moves: `Peck` [Slot 1: `Up, Left`], `Pursuit` [Slot 2: `Up, Right`], `Tackle` [Slot 3: `Down, Left`], `Secret Power` [Slot 4: `Down, Right`, 70 BP STAB Normal! Note: Party menu popup has `SECRET POWER` at Row 1 and `SWITCH` at Row 2]) — Met on Route 103.
2. **MUDKIP** — Mudkip ♀ (Lv. 10 [`164/413 EXP`], `31/31 HP`, Held: `Oran Berry`, Brave, `Torrent`, Stats: `31 HP / 20 Atk / 18 Def / 17 SpA / 15 SpD / 13 Spd`, Moves: `Tackle` [Slot 1: `Up, Left`], `Bubble` [Slot 2: `Up, Right`], `Mud Sport` [Slot 3: `Down, Left`], `Water Gun` [Slot 4: `Down, Right`]) — Met on Route 101 (Starter).
3. **MERLIN** — Ralts ♂ (Lv. 4, `16/16 HP`, Held: `Oran Berry`, Jolly, `Synchronize`, Stats: `16 HP / 7 Atk / 7 Def / 8 SpA / 7 SpD / 8 Spd`, Moves: `Confusion`) — Met on Route 102.
4. **CIRCE** — Spoink ♀ (Lv. 7, `19/27 HP`, Moves: `Confusion` [Slot 1: `Up, Left`], `Psywave` [Slot 2: `Up, Right`]) — Met on Route 104 (South).
5. **NOCTIS** — Hoothoot ♂ (Lv. 8, `Confusion`, `Growl`) — Met in Petalburg Woods.

## Notepad Index
- `Main`: High-level dashboard, party summary, level caps, and core tactical rules.
- `Locations/Encounters`: Route-by-route encounter tracking.
- `Mechanics/Graveyard`: Fallen Pokémon, wipe post-mortems, and run history.
- `Mechanics/UIAndControls`: Verified naming keyboard grid, warp/cutscene scripting patterns, Pokémon Center healing formula, and Littleroot/Route 101/Oldale/Route 103/Route 102 coordinates.