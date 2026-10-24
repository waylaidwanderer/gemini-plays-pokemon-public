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
- **Route 104 (South) Trainer Teams & Berries (Verified Turns 599–653):**
  - **Berry Trees at `(37, 57)` & `(38, 57)`:** Located in the grass-free clearing just north of the eastern entrance `(39, 62)` — harvest and equip before the beach trainers!
  - **Bird Keeper Billy `(23, 66)`:** Turns toward footsteps on sand; has 3 Lv. 7 Pokémon (`Pidgey` [`Sand-Attack`], `Wingull` [holds `Oran Berry`, `Supersonic`, `Gust`, `Water Gun`], `Taillow`).
  - **Fisherman Darian `(15, 58)` / `(15, 59)`:** Has 2 Pokémon (`Lv. 9 Magikarp` [`Bounce`, `Tackle` — outspeeds 12-Spd Mudkip to jump on Odd turns and land on Even turns] and `Lv. 8 Feebas` [holds `Sitrus Berry` +30 HP, knows `Yawn`/`Hypnosis`, `Water Pulse`, `Facade`]). **Lead with a trained Lv. 10–12 secondary teammate against `Magikarp` so `Mudkip` enters `Feebas` at 100% HP holding an `Oran Berry`!**
- **Oldale & Petalburg Mart Prices (Turns 153, 593):** Poké Balls cost only **$10** each (10+ awards a Premier Ball); Potions cost $300; Antidotes cost $100; Parlyz Heals cost $200; Awakenings cost $250; Repels cost $350.
- **Heal in Overworld to 100% HP & Equip Oran Berries:** Bag Potions cannot be used in battle, but held `Oran Berries` (`(24, 2)` on Route 102 and `(37, 57)` on Route 104 South) activate automatically in battle!
- **Train Caught Teammates to Lv. 10–12 Before Trainers:** Never bring a base-level (Lv. 4–7) catch into Route 102 or Route 104 trainer battles. Train our caught teammates up to **Lv. 10–12** alongside the starter before challenging route trainers.

## Active Party (`BATTLE STYLE: SET`, `START` cursor on Row 5 `OPTION`)
1. **ATHENA** — Spearow ♀ (Lv. 11, `14/31 HP`, `Keen Eye`, Stats: `31 HP / 21 Atk / 11 Def / 15 SpA / 12 SpD / 22 Spd`, Moves: `Peck` [Slot 1: `Up, Left`], `Pursuit` [Slot 2: `Up, Right`], `Tackle` [Slot 3: `Down, Left`]) — Met on Route 103.
2. **MUDKIP** — Mudkip ♀ (Lv. 10, `31/31 HP`, `Torrent`, Stats: `31 HP / 20 Atk / 18 Def / 17 SpA / 15 SpD / 13 Spd`, Moves: `Tackle` [Slot 1: `Up, Left`], `Bubble` [Slot 2: `Up, Right`], `Mud Sport` [Slot 3: `Down, Left`], `Water Gun` [Slot 4: `Down, Right`]) — Met on Route 101 (Starter).
3. **MERLIN** — Ralts ♂ (Lv. 4, `18/18 HP`, `Growl`, `Confusion`) — Met on Route 102.

## Notepad Index
- `Main`: High-level dashboard, party summary, level caps, and core tactical rules.
- `Locations/Encounters`: Route-by-route encounter tracking.
- `Mechanics/Graveyard`: Fallen Pokémon, wipe post-mortems, and run history.
- `Mechanics/UIAndControls`: Verified naming keyboard grid, warp/cutscene scripting patterns, Pokémon Center healing formula, and Littleroot/Route 101/Oldale/Route 103/Route 102 coordinates.