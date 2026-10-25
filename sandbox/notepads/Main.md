# Pokémon Emerald Nuzlocke — Main Dashboard

## Run Status
- **Game:** Pokémon Emerald (Emerald Kaizo / Modified ruleset: In-battle Bag healing items are DISABLED [Cancel only]; wild/trainer Pokémon have custom movesets & held items!)
- **Player Name:** ORION (Boy / Brendan)
- **Attempt:** #9
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

## Key Tactical Rules (Learned from Attempts #1–#7)
- **Deterministic Bounded 2x2 Move Selection (Verified Turn 328):** Opening the Bag or Party menu in the overworld resets the in-battle move cursor to Slot 1 (`Tackle`). Because the 2x2 move grid does not wrap, **ALWAYS press `Down, Right` for Slot 4 (`Water Gun`), `Up, Right` for Slot 2 (`Bubble`), and `Up, Left` for Slot 1 (`Tackle`)**!
- **Starter Claims Route 101 (Verified Turn 141):** Because the starter's summary reads `Met in ROUTE 101`, the Nuzlocke harness treats Route 101 as already used and blocks Poké Ball throws on Route 101.
- **Lowered Wild Catch Rates & Crit Range Rule (Turns 158–161, 252, 293, 1090):** Poké Balls thrown at **Green HP (`>50%`)** pop out on Shake 0 in this ROM. Always weaken wild encounters into **Yellow (`<50%`) or Red (`<20%`) HP** using **`Bubble` (`Up, Right`, 20 BP — never `Water Gun`!)** so a `1/16` crit cannot KO, and immediately `RUN` if HP drops into `2x` enemy attack damage (crit range).
- **Modified Move Mechanics (Turns 169, 384):**
  - `Yawn` inflicts Sleep (`SLP`) immediately on the turn it is used.
  - `Silver Wind` (`Ledyba` on Route 103) has a **100% omni-boost rate** (`+1 Atk/Def/SpA/SpD/Spd` on every hit).
- **Route 102 Trainer Teams (Verified Turns 177–182, 303–328, 537–570, 1095–1127):**
  1. **Youngster Calvin `(33, 14)`:** 3 Lv. 6 Pokémon (`Sentret` [Assist->Rock Smash / Mud-Slap / Super Fang, Quick Attack], `Zigzagoon` [Swift, Sand-Attack], `Poochyena` [Super Fang, Rock Smash, Howl]).
  2. **Bug Catcher Rick `(25, 15)`:** 4 Lv. 5 Pokémon (`Caterpie` [holds `Berry Juice`], `Wurmple` [String Shot, Tackle], `Kakuna` [holds `Berry Juice`, Poison Sting, Harden], `Cascoon` [holds `Berry Juice`, Iron Defense, Tackle]).
  3. **Lass Tiana `(15..16, 5..6)` (OPTIONAL — wanders with 0 vision range):** 3 Pokémon (`Lv. 6 Igglybuff` [`Cute Charm` contact infatuation, holds `Oran Berry`, uses `Present`], `Lv. 6 Sunkern` [holds `Berry Juice`, knows `Leech Seed` (16 PP), `Protect` (10 PP), `Mega Drain` (10 PP), `Synthesis` (8 PP) — **OHKO'd from 100% to 0 HP right through `Berry Juice` by `Lv. 11 ZEPHYR`'s `Wing Attack`!**], `Lv. 5 Togepi` [holds `Berry Juice`, knows `Hidden Power`, `Sing`, `Metronome` (`Lock-On`, `Softboiled`)]).
  4. **Bug Catcher Allen `(13, 2)`:** Faces `Down` at the western exit of Route 102; has **4 Lv. 7 Pokémon** (`Weedle` [`Poison Sting`], `Silcoon` [holds `Sitrus Berry`, `Iron Defense`], `Wurmple` [`Tackle`], `Metapod` [holds `Sitrus Berry`, `Iron Defense`]).
- **Route 104 (South) Trainer Teams & Berries (Verified Turns 599–653, 886–913):**
  - **Bird Keeper Billy `(23, 66)`:** Turns toward footsteps on sand; has 3 Lv. 7 Pokémon (`Pidgey` [`Sand-Attack`], `Wingull` [holds `Oran Berry`, `Supersonic`, `Gust`, `Water Gun`], `Taillow`).
  - **Fisherman Darian `(15, 59)`:** Mandatory trainer facing `Right` across the 3-tile beach bottleneck `x=16..18, y=59`; has **4 Pokémon** (`Lv. 9 Magikarp` [`Bounce`, `Tackle` — once `Bounce` paralyzes `RAIJU` (`5 Spd`), `Magikarp` (`~19 Spd`) lands FIRST on Turn 2 of `Bounce` for only 3 damage and `RAIJU` attacks SECOND on the ground to OHKO `Magikarp`, while `PAR` makes `RAIJU` 100% immune to `Feebas`'s `Yawn`/`Hypnosis`!], `Lv. 8 Feebas` [holds `Sitrus Berry` +30 HP, knows `Yawn`/`Hypnosis`, `Water Pulse`, `Facade`, `Icy Wind` — walled and 3HKO'd through `Sitrus Berry` by `Lv. 12 ZEPHYR`'s `Wing Attack`!], `Lv. 7 Goldeen` [holds `Berry Juice`, `Rain Dance`, `Peck`, `Swift Swim`], and `Lv. 7 Luvdisc` [knows `Dive`, `Swift Swim` — faster than `CALYPSO`, so on Turn 2 of `Dive` it surfaces first for 3 damage and `CALYPSO` hits it on the surface!]).
  - **Northern Route 104 South Berries & Lady Cindy `(11, 40)`:** Berry trees at `(22, 41)` (`2 Oran Berries`) and `(24, 41)` (`2 Pecha Berries`) north of Mr. Briney's Cottage. **Lady Cindy `(11, 40)`** guards the Petalburg Woods entrance and has **3 Pokémon** (`Lv. 8 Cleffa ♀` [`Cute Charm`, `Pound`, `Charm`, `Encore`], `Lv. 8 Pichu ♀` [`Thunder Wave`, `ThunderShock`, `Static`], `Lv. 7 Azurill` [pure Normal-type with `Huge Power` + Physical `Uproar` (50 BP STAB dealing ~23 HP/hit) — OHKO with `BubbleBeam`/`Water Gun`!], `$1,400` payout).
- **Petalburg Woods Trainers (Verified Turns 920–925):**
  1. **Bug Maniac Lyle `(13, 35)`:** Faces `Up` near the south entrance; has **3 Lv. 8 Pokémon** (`Spinarak`, `Ledyba`, `Venonat`).
  2. **Bug Catcher James `(10, 24)`:** Faces `Down`; has **3 Pokémon** (`Lv. 9 Paras`, `Lv. 8 Surskit`, `Lv. 9 Nincada` [`Giga Drain`, `Scratch`]).
  3. **Team Magma Grunt `(26, 23)`:** Cutscene triggers along `x=26..28, y=23`; has **4 Pokémon** (`Lv. 8 Magnemite` [`Thunder Wave`, `ThunderShock`], `Lv. 8 Koffing` [`Toxic`, `Protect`, `Thief` — steals held Berries!], `Lv. 9 Houndour` [`Ember`, `Pursuit` — punishes switches!], and 4th unseen).
- **Level 15 Cap & Team Magma Grunt Strategy (Roxanne Cap = Lv. 15):**
  - Train **BOTH `Mudkip` AND our Secondary Sweeper to Lv. 13–14** before fighting the Petalburg Woods Team Magma Grunt `(26, 23)` (`Lv. 8 Magnemite`, `Lv. 8 Koffing`, `Lv. 9 Houndour`, + 4th).
  - Lead with **Lv. 13–14 `Mudkip`** (`Mud Sport` + `Water Gun`) against `Lv. 8 Magnemite`, equip a **`Pecha Berry`** on our `Koffing` answer so `Toxic` is immediately cured on Turn 1 (denying `Thief` on Turn 2), and **never switch out against `Lv. 9 Houndour` (`Pursuit`)**—use Lv. 13–14 `Mudkip` (`Water Gun` OHKO) or a full-HP physical sweeper (`Secret Power` OHKO).
- **Oldale & Petalburg Mart Prices (Turns 153, 593):** Poké Balls cost only **$10** each (10+ awards a Premier Ball); Potions cost $300; Antidotes cost $100; Parlyz Heals cost $200; Awakenings cost $250; Repels cost $350.
- **Heal in Overworld to 100% HP & Equip Oran Berries:** Bag Potions cannot be used in battle, but held `Oran Berries` (`(24, 2)` on Route 102 and `(22, 41)` on Route 104 South) activate automatically in battle!
- **Train Caught Teammates to Lv. 10–12 Before Trainers:** Never bring a base-level (Lv. 4–7) catch into Route 102 or Route 104 trainer battles. Train our caught teammates up to **Lv. 10–12** alongside the starter before challenging route trainers.

## Active Party
1. **CALYPSO** — Mudkip ♀ (Lv. 13, `38/38 HP`, `Torrent`, Stats: `38 HP / 28 Atk / 20 Def / 20 SpA / 16 SpD / 18 Spd`, Moves: `Tackle` [Slot 1: `Up, Left`], `Bubble` [Slot 2: `Up, Right`], `Mud Sport` [Slot 3: `Down, Left`], `Water Gun` [Slot 4: `Down, Right`]) — Met on Route 101 (Starter).
2. **ZEPHYR** — Wingull ♀ (Lv. 14, `36/36 HP`, Quiet [`+SpA / -Spd`], `Keen Eye`, Stats: `36 HP / 14 Atk / 15 Def / 25 SpA / 15 SpD / 26 Spd`, Moves: `Wing Attack` [Slot 1: `Up, Left`, 35 PP], `Water Gun` [Slot 2: `Up, Right`, 25 PP], `Quick Attack` [Slot 3: `Down, Left`, 30 PP], `BubbleBeam` [Slot 4: `Down, Right`, 20 PP]) — Met on Route 103.
3. **ATLAS** — Cubone ♂ (Lv. 7, `25/25 HP`, Mild [`+SpA / -Def`], `Lightningrod`, Stats: `25 HP / 12 Atk / 17 Def / 12 SpA / 13 SpD / 10 Spd`, Moves: `Bone Club` [Slot 1: `Up, Left`, 20 PP], `Rock Throw` [Slot 2: `Up, Right`, 15 PP]) — Met on Route 104 South.
4. **ARCTURUS** — Teddiursa ♂ (Lv. 8, `27/27 HP`, Sassy [`+SpD / -Spd`], `Guts`, Stats: `27 HP / 18 Atk / 14 Def / 15 SpA / 16 SpD / 10 Spd`, Moves: `Scratch` [Slot 1: `Up, Left`, 35 PP], `Lick` [Slot 2: `Up, Right`, 30 PP], `Faint Attack` [Slot 3: `Down, Left`, 20 PP]) — Met in Petalburg Woods.

## Notepad Index
- `Main`: High-level dashboard, party summary, level caps, and core tactical rules.
- `Locations/Encounters`: Route-by-route encounter tracking.
- `Mechanics/Graveyard`: Fallen Pokémon, wipe post-mortems, and run history.
- `Mechanics/UIAndControls`: Verified naming keyboard grid, warp/cutscene scripting patterns, Pokémon Center healing formula, and Littleroot/Route 101/Oldale/Route 103/Route 102 coordinates.