# Pokémon Emerald Nuzlocke — Main Dashboard

## Run Status
- **Game:** Pokémon Emerald (Emerald Kaizo / Modified ruleset: In-battle Bag healing items are DISABLED [Cancel only]; wild/trainer Pokémon have custom movesets & held items!)
- **Player Name:** ORION (Boy / Brendan)
- **Attempt:** #11
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
- **Deterministic Bounded 2x2 Move Selection (Verified Turns 328, 2438):** Opening the Bag or Party menu in the overworld resets the in-battle move cursor to Slot 1 (`Tackle`). Because the 2x2 move grid does not wrap, **ALWAYS press `Down, Right` for Slot 4 (`Water Gun`), `Up, Right` for Slot 2 (`Bubble`), `Up, Left` for Slot 1 (`Tackle`), and `Left, Down` (NEVER `Down, Left` when Slot 4 `-` is empty!) for Slot 3 (`Secret Power` / `Toxic`)**!
- **Starter Claims Route 101 (Verified Turn 141):** Because the starter's summary reads `Met in ROUTE 101`, the Nuzlocke harness treats Route 101 as already used and blocks Poké Ball throws on Route 101.
- **Lowered Wild Catch Rates & Crit Range Rule (Turns 158–161, 252, 293, 1090):** Poké Balls thrown at **Green HP (`>50%`)** pop out on Shake 0 in this ROM. Always weaken wild encounters into **Yellow (`<50%`) or Red (`<20%`) HP** using **`Bubble` (`Up, Right`, 20 BP — never `Water Gun`!)** so a `1/16` crit cannot KO, and immediately `RUN` if HP drops into `2x` enemy attack damage (crit range).
- **Modified Move Mechanics (Turns 169, 384, 2225):**
  - `Yawn` is a direct sleep move (`EFFECT_SLEEP` with <100% accuracy, not delayed 2-turn sleep): when it hits, it inflicts Sleep (`SLP`) immediately on that turn; when it misses, it prints `"attack missed!"` with no delayed sleep effect.
  - `Silver Wind` (`Ledyba` on Route 103) boosts all 5 stats (`+1 Atk/Def/SpA/SpD/Spd`).
- **Route 102 Trainer Teams (Verified Turns 177–182, 303–328, 537–570, 1095–1127):**
  1. **Youngster Calvin `(33, 14)`:** 3 Lv. 6 Pokémon (`Sentret` [Assist->Rock Smash / Mud-Slap / Super Fang, Quick Attack], `Zigzagoon` [Swift, Sand-Attack], `Poochyena` [Super Fang, Rock Smash, Howl]).
  2. **Bug Catcher Rick `(25, 15)`:** 4 Lv. 5 Pokémon (`Caterpie` [holds `Berry Juice`], `Wurmple` [String Shot, Tackle], `Kakuna` [holds `Berry Juice`, Poison Sting, Harden], `Cascoon` [holds `Berry Juice`, Iron Defense, Tackle]).
  3. **Lass Tiana `(15..16, 5..6)` (wanders/turns; spots `(15..16, 4)` when facing `Up`):** 3 Pokémon (`Lv. 6 Igglybuff` [`Cute Charm` contact infatuation, holds `Oran Berry`, uses `Present` — note that `Poison Sting` is a non-contact move in Gen 3 and bypasses `Cute Charm`!], `Lv. 6 Sunkern` [pure Grass-type, holds `Berry Juice`, knows `Leech Seed` (16 PP), `Protect` (10 PP), `Mega Drain` (10 PP), `Synthesis` (8 PP) — weak to `Poison Sting` + `PSN`!], `Lv. 5 Togepi` [holds `Berry Juice`, knows `Hidden Power`, `Sing`, `Metronome` (`Lock-On`, `Softboiled`)]).
  4. **Bug Catcher Allen `(13, 2)`:** Faces `Down` at the western exit of Route 102; has **4 Lv. 7 Pokémon** (`Weedle` [`Poison Sting`], `Silcoon` [holds `Sitrus Berry`, `Iron Defense`], `Wurmple` [`Tackle`], `Metapod` [holds `Sitrus Berry`, `Iron Defense`]).
- **Route 104 (South) Trainer Teams & Berries (Verified Turns 599–653, 886–913):**
  - **Bird Keeper Billy `(23, 66)`:** Turns toward footsteps on sand; has 3 Lv. 7 Pokémon (`Pidgey` [`Sand-Attack`], `Wingull` [holds `Oran Berry`, `Supersonic`, `Gust`, `Water Gun`], `Taillow`).
  - **Fisherman Darian `(15, 59)`:** Mandatory trainer facing `Right` across the 3-tile beach bottleneck `x=16..18, y=59`; has **4 Pokémon** (`Lv. 9 Magikarp` [`Bounce`, `Tackle` — once `Bounce` paralyzes `RAIJU` (`5 Spd`), `Magikarp` (`~19 Spd`) lands FIRST on Turn 2 of `Bounce` for only 3 damage and `RAIJU` attacks SECOND on the ground to OHKO `Magikarp`, while `PAR` makes `RAIJU` 100% immune to `Feebas`'s `Yawn`/`Hypnosis`!], `Lv. 8 Feebas` [holds `Sitrus Berry` +30 HP, knows `Yawn`/`Hypnosis`, `Water Pulse`, `Facade`, `Icy Wind` — walled and 3HKO'd through `Sitrus Berry` by `Lv. 12 ZEPHYR`'s `Wing Attack`!], `Lv. 7 Goldeen` [holds `Berry Juice`, `Rain Dance`, `Peck`, `Swift Swim`], and `Lv. 7 Luvdisc` [knows `Dive`, `Swift Swim` — faster than `CALYPSO`, so on Turn 2 of `Dive` it surfaces first for 3 damage and `CALYPSO` hits it on the surface!]).
  - **Northern Route 104 South Berries & Lady Cindy `(11, 40)`:** Berry trees at `(22, 41)` (`2 Oran Berries`) and `(24, 41)` (`2 Pecha Berries`) north of Mr. Briney's Cottage. **Lady Cindy `(11, 40)`** guards the Petalburg Woods entrance and has **3 Pokémon** (`Lv. 8 Cleffa ♀` [`Cute Charm`, `Pound`, `Charm`, `Encore`, `Metronome`], `Lv. 8 Pichu ♀` [`Thunder Wave`, `ThunderShock`, `Sweet Kiss`, `Thief`, `Static`], `Lv. 7 Azurill ♀` [pure Normal-type with `Huge Power` + Physical `Uproar` (50 BP STAB dealing ~12–14 normal / ~21 crit damage) — 2HKO'd by `Lv. 11 BOREAS`'s `Water Gun`!], `$1,400` payout).
- **Petalburg Woods Trainers (Verified Turns 920–925, 1561–1572, 2289–2299):**
  1. **Bug Maniac Lyle `(13, 35)`:** Faces `Up` near the south entrance; has **3 Lv. 8 Pokémon** (`Lv. 8 Spinarak` [holds `Berry Juice`, knows `Night Shade`], `Lv. 8 Ledyba` [knows `Protect`], `Lv. 8 Venonat` [knows `Stun Spore`]).
  2. **Bug Catcher James `(10, 24)`:** Faces `Down`; has **3 Pokémon** (`Lv. 9 Paras` [4x weak to Fire], `Lv. 8 Surskit` [knows `Psybeam`, `Mega Drain`], `Lv. 9 Nincada` [`Giga Drain`, `Scratch`; Base 90 Def vs Base 30 SpD — OHKO'd by Special Fire/Water moves]).
  3. **Team Magma Grunt `(26, 23)`:** Cutscene triggers along `x=26..28, y=23`; has **5 Pokémon** (`Lv. 8 Magnemite` [`Flash Cannon`, `Thunder Wave`, `ThunderShock` — 2HKO'd by `Mudkip`'s `Mud Sport` + `Water Gun` or OHKO'd from 52% HP by `Lv. 14 MEDEA`'s `Fire Punch`], `Lv. 8 Koffing` [`Toxic`, `Protect`, `Thief` — hard-countered by `Lv. 14 MEDEA`'s Poison typing + `Sticky Hold` + `Fire Punch`], `Lv. 9 Houndour` [`Ember`, `Pursuit` — OHKO'd by `Lv. 14 MEDEA`'s 90-BP STAB `Sludge Bomb` against its Base 30 Defense without switching out!], `Lv. 8 Bagon` [`Headbutt` — 2HKO'd by `BOREAS`'s `BubbleBeam`], and `Lv. 8 Duskull` [`Protect`, `Night Shade`, `Confuse Ray`, holds `Leftovers`]).
- **Route 104 (North) Trainers (Verified Turns 1601–1617):**
  1. **Rich Boy Winston `(21, 26)`:** Faces `Up` across `(21, 25)`; has **3 Lv. 8 Pokémon** (`Lv. 8 Snubbull` [`Intimidate`, `Pay Day`, holds `Oran Berry`], `Lv. 8 Electrike` [`ThunderShock`, `Quick Attack`, holds `Oran Berry`], `Lv. 8 Growlithe` [`Intimidate`, `Bite`, holds `Oran Berry`]).
  2. **Lass Haley `(32, 22)`:** Faces `Left` across `(30..31, 22)` at the south end of the bridge; has **3 Lv. 9 Pokémon** (`Lv. 9 Skitty ♀` [`Assist`], `Lv. 9 Oddish ♀` [`Acid`, `Protect`, `Sleep Powder`/`Stun Spore`], `Lv. 9 Vulpix` [`Confuse Ray`]).
  3. **Twins Gina & Mia `(27..28, 15)`:** Mandatory Double Battle facing `Down` across `(27..28, 16)` on the bridge; have **2 Lv. 8 Pokémon** (`Lv. 8 Smeargle ♂` [Left: `Focus Punch`] and `Lv. 8 Smeargle ♂` [Right: `Follow Me`, holds `Sitrus Berry`]). **Solution:** Use `CALYPSO`'s spread move **`Bubble` (Slot 2: `Up, Right`)**, which hits BOTH foes (skipping target selection), bypasses `Follow Me`, and causes Left `Smeargle`'s `Focus Punch` to fail every turn while `ATLAS`'s `Bone Club` KOs Right `Smeargle`!
  4. **PKMN Trainer Red `(29, 8)`:** Mandatory 6-Pokémon boss trainer with a Fisherman overworld sprite facing `Left` with a 5-tile sight range across `(24..28, 8)` at the north end of the bridge; leads with `Lv. 9 Eevee ♂` (`Curse`, holds `Sitrus Berry`) and `Lv. 9 Pikachu ♂` (`Shock Wave`, `Surf`, `Thunder Wave`, holds `Sitrus Berry`, custom boosted stats `~36 HP` / `~21 Spd`). **Solution:** Train 3–4 party members to Lv. 13–14, equip `Oran Berries` from `(3, 23)`, and use **`Mud Sport` (Slot 3: `Down, Left`)** on `Mudkip` on Turn 1 against Red's passive lead `Lv. 9 Eevee` (`Curse`) BEFORE knocking out `Eevee` with `Water Gun` so `Mud Sport` (`0.5x` Electric power) is already active when `Lv. 9 Pikachu` enters battle!
- **Attempt #11 Level 15 Cap & Balanced Team Training Rule (Roxanne Cap = Lv. 15):**
  - Keep all party members at or below **Level 15** before challenging Gym Leader Roxanne.
  - Before crossing the Route 104 North bridge to `PKMN Trainer Red` `(29, 8)`, train `Mudkip` and at least **2–3 caught teammates to Level 13–14**, equip each with a held `Oran Berry` (`+10 HP`), and use **`Mud Sport` (Slot 3: `Down, Left`)** on Turn 1 vs Red's passive lead `Lv. 9 Eevee` (`Curse`).
  - Never queue multi-turn attack loops when poisoned (`PSN`); heal & equip `Oran`/`Pecha` Berries right at `(25, 3)` on Route 102 immediately after harvesting them; and pause at `(17, 4)` to visually verify Lass Tiana's position/facing before crossing `(15..16, 4)`.
- **Oldale & Petalburg Mart Prices (Turns 153, 593):** Poké Balls cost only **$10** each (10+ awards a Premier Ball); Potions cost $300; Antidotes cost $100; Parlyz Heals cost $200; Awakenings cost $250; Repels cost $350.
- **Heal in Overworld to 100% HP & Equip Oran Berries:** Bag Potions cannot be used in battle, but held `Oran Berries` (`(24, 2)` on Route 102 and `(22, 41)` on Route 104 South) activate automatically in battle!
- **Train Caught Teammates to Lv. 10–12 Before Trainers:** Never bring a base-level (Lv. 4–7) catch into Route 102 or Route 104 trainer battles. Train our caught teammates up to **Lv. 10–12** alongside the starter before challenging route trainers.

## Active Party
1. **GAIA** — Cubone ♀ (Lv. 11, `23/34 HP`, Adamant [`+Atk / -SpA`], `Rock Head`, Stats: `34 HP / 17 Atk / 29 Def / 13 SpA / 16 SpD / 13 Spd`, Moves: `Bone Club` [Slot 1: `Up, Left`, 20 PP], `Rock Throw` [Slot 2: `Up, Right`, 15 PP], `Secret Power` [Slot 3: `Down, Left`, 20 PP]) — Met on Route 104 South.
2. **MEDEA** — Gulpin ♀ (Lv. 15, `47/47 HP`, Quirky, `Sticky Hold`, Stats: `47 HP / 18 Atk / 22 Def / 20 SpA / 23 SpD / 17 Spd`, Moves: `Acid` [Slot 1: `Up, Left`, 30 PP], `Yawn` [Slot 2: `Up, Right`, 10 PP], `Fire Punch` [Slot 3: `Down, Left`, 15 PP], `Sludge Bomb` [Slot 4: `Down, Right`, 15 PP]) — Met on Route 102.
3. **ADONIS** — Oddish ♂ (Lv. 14, `40/40 HP`, Careful [`+SpD / -SpA`], `Chlorophyll`, Stats: `40 HP / 19 Atk / 24 Def / 24 SpA / 28 SpD / 13 Spd`, Moves: `Mega Drain` [Slot 1: `Up, Left`, 10 PP], `Acid` [Slot 2: `Up, Right`, 30 PP], `Toxic` [Slot 3: `Down, Left`, 10 PP]) — Met in Petalburg Woods.
4. **MUDKIP** — Mudkip ♂ (Lv. 13, `38/38 HP`, `Torrent`, Stats: `38 HP / 25 Atk / 19 Def / 21 SpA / 18 SpD / 18 Spd`, Moves: `Tackle` [Slot 1: `Up, Left`], `Bubble` [Slot 2: `Up, Right`], `Mud Sport` [Slot 3: `Down, Left`], `Water Gun` [Slot 4: `Down, Right`], Holds: `Pecha Berry`) — Met on Route 101 (Starter).

## Notepad Index
- `Main`: High-level dashboard, party summary, level caps, and core tactical rules.
- `Locations/Encounters`: Route-by-route encounter tracking.
- `Mechanics/Graveyard`: Fallen Pokémon, wipe post-mortems, and run history.
- `Mechanics/UIAndControls`: Verified naming keyboard grid, warp/cutscene scripting patterns, Pokémon Center healing formula, and Littleroot/Route 101/Oldale/Route 103/Route 102 coordinates.