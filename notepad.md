<h1><code>Locations/Encounters</code></h1>

# Route & Area Encounters (Attempt #9)

| Location | Pokémon | Nickname | Level | Status | Notes |
|---|---|---|---|---|---|
| Route 101 | Mudkip ♀ | CALYPSO | 13 | Active | Starter (`Met in ROUTE 101` — claims Route 101 encounter) |
| Route 103 | Wingull ♀ | ZEPHYR | 15 | Active | Caught at `(13, 15)` (Quiet, `Keen Eye`, `38 HP / 15 Atk / 16 Def / 26 SpA / 16 SpD / 27 Spd`, `Wing Attack` [Slot 1], `Water Gun` [Slot 2], `Quick Attack` [Slot 3], `BubbleBeam` [Slot 4]) |
| Route 102 | Electrike ♂ | RAIJU | 11 | Deceased | Caught at `(38, 6)` — Fainted Turn 1540 vs Lady Cindy's `Lv. 7 Azurill` (`Huge Power` + Physical `Uproar`) |
| Route 104 (South) | Cubone ♂ | ATLAS | 7 | Active | Caught at `(23, 61)` (Mild, `Lightningrod`, `Bone Club` [Slot 1], `Rock Throw` [Slot 2]) |
| Petalburg Woods | Teddiursa ♂ | ARCTURUS | 8 | Active | Caught at `(23, 35)` (Sassy, `Guts`, `27 HP / 18 Atk / 14 Def / 15 SpA / 16 SpD / 10 Spd`, `Scratch` [Slot 1], `Lick` [Slot 2], `Faint Attack` [Slot 3]) |
| Route 116 | TBD | TBD | - | Pending | Open encounter east of Rustboro City |
| Rusturf Tunnel | TBD | TBD | - | Pending | Open encounter east of Route 116 |

<hr>

<h1><code>Main</code></h1>

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
1. **ATLAS** — Cubone ♂ (Lv. 7, `25/25 HP`, Mild [`+SpA / -Def`], `Lightningrod`, Stats: `25 HP / 12 Atk / 17 Def / 12 SpA / 13 SpD / 10 Spd`, Moves: `Bone Club` [Slot 1: `Up, Left`, 20 PP], `Rock Throw` [Slot 2: `Up, Right`, 15 PP], Holds: `Oran Berry`) — Met on Route 104 South.
2. **CALYPSO** — Mudkip ♀ (Lv. 13, `38/38 HP`, `Torrent`, Stats: `38 HP / 28 Atk / 20 Def / 20 SpA / 16 SpD / 18 Spd`, Moves: `Tackle` [Slot 1: `Up, Left`], `Bubble` [Slot 2: `Up, Right`], `Mud Sport` [Slot 3: `Down, Left`], `Water Gun` [Slot 4: `Down, Right`], Holds: `Oran Berry`) — Met on Route 101 (Starter).
3. **ZEPHYR** — Wingull ♀ (Lv. 15, `38/38 HP`, Quiet [`+SpA / -Spd`], `Keen Eye`, Stats: `38 HP / 15 Atk / 16 Def / 26 SpA / 16 SpD / 27 Spd`, Moves: `Wing Attack` [Slot 1: `Up, Left`, 35 PP], `Water Gun` [Slot 2: `Up, Right`, 25 PP], `Quick Attack` [Slot 3: `Down, Left`, 30 PP], `BubbleBeam` [Slot 4: `Down, Right`, 20 PP], Holds: `Pecha Berry`) — Met on Route 103.
4. **ARCTURUS** — Teddiursa ♂ (Lv. 8, `27/27 HP`, Sassy [`+SpD / -Spd`], `Guts`, Stats: `27 HP / 18 Atk / 14 Def / 15 SpA / 16 SpD / 10 Spd`, Moves: `Scratch` [Slot 1: `Up, Left`, 35 PP], `Lick` [Slot 2: `Up, Right`, 30 PP], `Faint Attack` [Slot 3: `Down, Left`, 20 PP]) — Met in Petalburg Woods.

## Notepad Index
- `Main`: High-level dashboard, party summary, level caps, and core tactical rules.
- `Locations/Encounters`: Route-by-route encounter tracking.
- `Mechanics/Graveyard`: Fallen Pokémon, wipe post-mortems, and run history.
- `Mechanics/UIAndControls`: Verified naming keyboard grid, warp/cutscene scripting patterns, Pokémon Center healing formula, and Littleroot/Route 101/Oldale/Route 103/Route 102 coordinates.

<hr>

<h1><code>Mechanics/Graveyard</code></h1>

# Graveyard & Run History

## Attempt #1 (Turns 1–78) — WIPEOUT
- **Casualties:**
  - **TRITON** (Mudkip ♂, Lv. 5, Timid) — Died on Turn 77 on Route 103 `(4, 5)` to a Wild Wingull Lv. 4 (`Wing Attack`).
- **Root Causes of Wipe:**
  1. **Unhealed Pre-Battle HP (`14/20` HP):** Entered tall grass at `14/20` HP despite holding 2 Potions in the Bag (which can only be used in the overworld).
  2. **Queued 3 Turns Against Unverified Wild Species:** Queued 3 consecutive `Tackle` turns on Turn 75 against a Lv. 4 Wingull before seeing its moveset (`Wing Attack`, 60 BP STAB Flying, ~6–7 damage/hit).
  3. **Speed Trap on Route 103:** Lv. 4 Wingull (Base 85 Speed -> 10 Speed) outsped Lv. 5 Timid Mudkip (9 Speed), causing two consecutive `RUN` attempts (`Attempts 1 & 2`) to fail (`"Can't escape!"`) while Wingull KO'd TRITON from `3/20` HP.
- **Tactical Lessons for Attempt #2:**
  1. **Grind on Route 101 (Lv. 2–3 wilds), NOT Route 103 (Lv. 4 fast/dangerous wilds):** Train our starter to **Level 7** on Route 101 (right below Oldale Town) before crossing Route 103 to May.
  2. **Immediate Overworld Healing:** Since in-battle Bag healing is disabled (`▶CANCEL` only), heal in the overworld with Potions or at the Pokémon Center whenever HP drops below 75%.
  3. **Single-Turn Scouting & Immediate Escape:** Against fast/threatening wild Pokémon (like Wingull or Skitty on Route 103), `RUN` on Turn 1 while at full HP rather than trading hits.

## Attempt #2 (Starting Turn 79)
- **Deaths:** None

---

## Attempt #2 Wipe Post-Mortem (Turn 183)
- **Fallen Pokémon:** `AXOLOTL` (Mudkip ♂, Lv. 7, Adamant) — Fainted at `(34, 14)` on Route 102 against Youngster Calvin.
- **Enemy Details (Youngster Calvin at `(33, 14)` on Route 102):**
  - Has **3 Pokémon**:
    1. **Sentret ♂ Lv. 6**: Knows `Assist` (called `Rock Smash` from a back-line teammate, inflicting `-1 Def` drops) and `Quick Attack` (+1 priority, dealt 9 HP after two Defense drops). Took 3 `Tackle` hits (`~36%` each from Lv. 7 Adamant Mudkip) plus 1 `Bubble` to KO, yielding `72 EXP`.
    2. **Zigzagoon ♂ Lv. 6**: Outsped Lv. 7 Mudkip (`11 Spd`) and used `Swift` (60 BP STAB never-miss).
    3. **3rd Pokémon (Unseen)**: Knows `Rock Smash` (verified via Sentret's `Assist`).
- **Root Causes of Wipe:**
  1. **Underleveled for Route 102 Trainers:** Challenged Youngster Calvin at **Level 7** (`15 EXP` short of Level 8), causing `Tackle` to miss the 3HKO on Lv. 6 Sentret by ~1 HP and allowing Sentret an extra turn to land a second `-2 Def` `Quick Attack` (`10 -> 2 HP`).
  2. **Solo Party (0 Catch Captures on Routes 103 & 102):** At Level 7 (`25 HP`), wild Lv. 4 Sunkern on Route 103 and wild Lv. 6 Gulpin (`Yawn` + `Acid`) on Route 102 threatened AXOLOTL's HP too quickly, forcing us to flee both encounters and face Youngster Calvin solo with no switch-in to clear `Rock Smash` Defense drops.
- **Tactical Rules for Attempt #3:**
  1. **Level 10+ Before Route 103/102 Catches & Route 102 Trainers:** Grind Mudkip to **Level 9–10** on Route 101 / Route 103 before attempting our Route 103 and Route 102 Nuzlocke catches or fighting Youngster Calvin. Higher bulk (`~32–35 HP`) allows safely throwing multiple Poké Balls to guarantee catches, and higher Attack (`~23–25 Atk`) cleanly 2HKOs/3HKOs Lv. 6 trainer Pokémon.
  2. **Never Fight Route 102 Trainers Solo at Lv. 7:** Ensure we have **at least Lv. 10+** (and ideally a 2nd caught Pokémon from Route 103 or Route 102 to pivot out of stat drops/Yawn) before challenging Youngster Calvin at `(33, 14)`.

---

## Attempt #3 Casualties (Starting Turn 184)
- **APOLLO** (Ralts ♂, Lv. 4, Naughty, `Synchronize`) — Died on Turn 326 on Route 102 `(16, 5)` to Lass Tiana's Lv. 6 `Igglybuff` (`Present`, Ability: `Cute Charm`, held `Oran Berry`).
  - **Context & Lessons:** Using `Tackle` (a contact move) on Turn 1 against Igglybuff triggered `Cute Charm` (`50%` infatuation immobilization), because opening the Berry planting Bag screen in Turn 319 had reset our move cursor from `Water Gun` (Slot 4) to `Tackle` (Slot 1). After two consecutive infatuation immobilizations and `Present` hits dropped `APOSEIDON` to `7/33 HP`, `APOLLO` pivoted in to cure `APOSEIDON`'s infatuation, burned Igglybuff's held `Oran Berry` and dropped it into red HP with `Confusion`, and absorbed the next `Present` so `APOSEIDON` could re-enter safely with Torrent active (`90 BP` `Water Gun`) and sweep.
  - **Rule Going Forward:** Always verify that a non-contact move (`Water Gun` / `Bubble`) is selected after any overworld Bag/Party screen opening before attacking Pokémon with contact abilities (`Cute Charm`, `Static`, `Poison Point`, `Effect Spore`).
- **APOSEIDON** (Mudkip ♂, Lv. 11, Gentle) — Died on Turn 328 on Route 102 `(16, 5)` to Lass Tiana's Lv. 6 `Sunkern` (`Mega Drain`) after entering the Sunkern matchup at `7/33 HP` — **TOTAL PARTY WIPEOUT (Attempt #3 Over)**.
- **Root Causes of Attempt #3 Wipe:**
  1. **Unbounded Move Cursor Assumption After Bag Opening:** In Turn 319, re-interacting with the Berry tree soil opened the Bag (`BERRIES POCKET`), which reset the in-battle move cursor to Slot 1 (`Tackle`). On Turn 1 vs Lass Tiana's `Lv. 6 Igglybuff`, pressing `A, A` used contact `Tackle` instead of non-contact `Water Gun`, triggering `Cute Charm` and locking `APOSEIDON` in love for 2 consecutive turns (`28 -> 7/33 HP`).
  2. **Unequipped Oran Berries & Pre-Battle Chip (`28/33 HP`):** We had just picked 2 `Oran Berries` (`+10 HP` automatic in-battle heal) and held 3 `Potions`, but challenged Lass Tiana at `28/33 HP` without topping up or equipping an `Oran Berry`.
  3. **Grass Weakness & `Mega Drain` on Lass Tiana's Sunkern:** Pure Water `Mudkip` is **2x weak to Grass**, and Lass Tiana's `Lv. 6 Sunkern` knows **`Mega Drain` (40 BP Grass)**, which heals Sunkern by 50% of damage dealt and KOs Mudkip from `7 HP`.
- **Tactical Rules for Attempt #4:**
  1. **Deterministic Bounded 2x2 Move Selection:** Because the 2x2 move menu does NOT wrap around, **ALWAYS press `Down, Right` before `A` to select Slot 4 (`Water Gun`), `Up, Right` for Slot 2 (`Bubble`), and `Up, Left` for Slot 1 (`Tackle`)**! This is 100% immune to cursor memory resets.
  2. **Equip Held Oran Berry & Heal to 100% HP Before Every Trainer:** Harvest the 2 `Oran Berries` at `(24, 2)` and 2 `Pecha Berries` at `(25, 2)` on Route 102 and immediately `GIVE` an `Oran Berry` to our active Pokémon before challenging Lass Tiana (`(15, 5)`).
  3. **Use Physical `Tackle` (`Up, Left`) at Full HP Against Lass Tiana's `Lv. 6 Sunkern`:** Do not let `Mudkip` face `Sunkern` (`Mega Drain`) at low HP; use `Water Gun` (`Down, Right`, non-contact) to 2HKO `Igglybuff` without triggering `Cute Charm`, then use `Tackle` (`Up, Left`) or a trained Bug/Flying/Normal teammate to 2HKO `Sunkern`.

---

## Attempt #4 Wipe Post-Mortem (Turn 418)
- **Fallen Pokémon:** `NEPTUNE` (Mudkip ♂, Lv. 8, `-Speed` nature [9 Spd at Lv. 8]) — Fainted on Northern Route 101 `(5, 4)` to a wild Lv. 3 `Sentret` (`Quick Attack`) during `level10_grinder` subagent execution.
- **Root Causes of Wipe:**
  1. **Unverified Overworld `START` Menu Healing by Subagent:** At `9/28 HP` on Route 101 `(7, 4)`, the `level10_grinder` subagent attempted to open `BAG` via `Start -> Down, Down, A` assuming the `START` cursor started on `POKéDEX` (Row 0). Because `START` remembered `BAG` (Row 2) from an earlier open, `Down, Down, A` selected `SAVE` (Row 4), leaving `NEPTUNE` unhealed at `9/28 HP` before entering two wild battles (`Lv. 2 Caterpie` -> `7/28 HP`, `Lv. 3 Sentret` -> `0/28 HP`).
  2. **Ignoring the Adjacent Oldale Pokémon Center:** `(7, 4)` on Route 101 is only 15 grass-free steps from the Oldale Town Pokémon Center `(6, 16)`, which heals HP and PP deterministically without touching the `START` menu.
- **Tactical Rules for Attempt #5:**
  1. **Subagent Strict Prohibition on `START` / `BAG` Menus:** `level10_grinder` is updated to **NEVER press `Start` or open the `BAG`**; all healing during Route 101/103 grinding must be performed exclusively with Nurse Joy at the Oldale Pokémon Center `(6, 16)` after every 2–3 battles.
  2. **Check Starter Speed Stat Early:** `NEPTUNE` had a `-Speed` nature (`9 Speed` at Lv. 8), allowing wild Pokémon to outspeed or tie more often. Verify the starter's stats/nature in the Summary screen or level-up box so escape and turn-order calculations use exact Speed.

---

## Attempt #5 Casualties (Starting Turn 419)
- **GAIA** (Cubone ♀, Lv. 7, Careful, `Rock Head`) — Died on Turn 643 on Route 104 South `(18, 59)` to Fisherman Darian's Lv. 8 `Feebas` (`Water Pulse` — 2x Super Effective + 2x Critical Hit from `20/24 HP`).
  - **Lesson:** Never switch a 2x Water-weak Ground-type into an enemy Water-type that knows `Water Pulse` (60 BP STAB), because a `2x` Super Effective hit (`11–13 HP`) becomes `22–26 HP` on a `1/16` Critical Hit. Always use neutral/resistant pivots (`LYNX` / `GULPIN` / `AAAAAAAAAA`) against Water moves and train new catches to Lv. 10+ before using them against trainers.
- **GULPIN** (Gulpin ♂, Lv. 7, Modest, `Liquid Ooze`) — Died on Turn 645 on Route 104 South `(18, 59)` to Fisherman Darian's Lv. 8 `Feebas` (`Water Pulse`), sacrificing himself after chipping `Feebas` to `~60% HP` so `LYNX` and `AAAAAAAAAA` would not have to take two consecutive hits on a hard switch into a faster `Feebas`.
  - **Enemy Details (Fisherman Darian `(15, 58)` on Route 104 South):** Has `Lv. 9 Magikarp` (`Bounce`, `Tackle`) and `Lv. 8 Feebas` (custom boosted bulk/stats; knows `Hypnosis`/`Yawn`, `Facade`, `Water Pulse`). Avoidable or only challenge after equipping `Chesto` / `Oran Berries` and training party to Lv. 13+.
- **LYNX** (Skitty ♂, Lv. 4, Adamant, `Cute Charm`) — Died on Turn 650 on Route 104 South `(18, 59)` to Fisherman Darian's Lv. 8 `Feebas` (`Water Pulse`), giving `AAAAAAAAAA` a clean post-faint free switch.
- **AAAAAAAAAA** (Mudkip ♂, Lv. 12, Quiet [`-Speed`], `Torrent`) — Died on Turn 653 on Route 104 South `(18, 59)` to Fisherman Darian's Lv. 8 `Feebas` (`Facade`) after `Feebas` consumed a held `Sitrus Berry` (`+30 HP`) — **TOTAL PARTY WIPEOUT (Attempt #5 Over)**.
- **Root Causes of Attempt #5 Wipe:**
  1. **Unhealed Chip From `Magikarp`'s `Bounce` + Quiet (`-Speed`) Nature (`15/37 HP` entering `Feebas`):** Because `AAAAAAAAAA` had a `-Speed` nature (`12 Spd` at Lv. 12), Fisherman Darian's `Lv. 9 Magikarp` (`~15 Spd`) outsped and stalled with `Bounce` for 10 turns, chipping `AAAAAAAAAA` from `37/37` down to `15/37 HP` before `Lv. 8 Feebas` (`~15 Spd`, `Yawn`/`Hypnosis`, `Water Pulse`, `Facade`, held `Sitrus Berry`) entered and put `AAAAAAAAAA` to sleep immediately.
  2. **Missed Route 104 South Berry Trees at `(37, 57)`–`(38, 57)` (No Held `Oran Berry`):** After consuming our Route 102 `Oran Berries` against Lass Tiana and Bug Catcher Allen, we walked past the 2 Berry trees at `(37, 57)` and `(38, 57)` at the eastern entrance of Route 104 South without harvesting and equipping them.
  3. **Three Underleveled Teammates (`Lv. 4 LYNX`, `Lv. 7 GULPIN`, `Lv. 7 GAIA`):** Despite our rule to train teammates to Lv. 10+, we brought Lv. 4 and Lv. 7 teammates to Route 104 South and switched 2x Water-weak `GAIA` (`Cubone`) into `Feebas`'s `Water Pulse` (dying to a 4x SE+Crit hit).
- **Tactical Rules for Attempt #6:**
  1. **Harvest & Equip Route 104 South Berries at `(22, 41)` & `(24, 41)`:** Harvest the 2 `Oran Berries` at `(22, 41)` and 2 `Pecha Berries` at `(24, 41)` north of Mr. Briney's Cottage on Route 104 South (note: the trees north of `y=56` at the eastern entrance are behind an impassable forest wall).
  2. **Train Caught Teammates to Lv. 10–12 Before Route 104 South Trainers:** Do not leave caught teammates at Lv. 4–7; grind our primary backup teammate(s) to **Lv. 10–12** so they can independently defeat Lv. 8–9 trainer Pokémon (`Magikarp` / `Feebas`).
  3. **Against Fisherman Darian `(15, 58)` / `(15, 59)`:** Lead with a trained secondary teammate against `Lv. 9 Magikarp` (`Bounce`) so `Mudkip` enters `Lv. 8 Feebas` at **100% HP holding an `Oran Berry`**, and never switch a Ground-type into `Water Pulse`.

---

## Attempt #6 Wipe Post-Mortem (Turn 953 — Petalburg Woods)
- **Casualties (vs Team Magma Grunt at `(26, 23)` in Petalburg Woods):**
  - **MUDKIP** (Mudkip ♀, Lv. 10, Brave) — Died on Turn 946 to Team Magma Grunt's `Lv. 9 Houndour` (`Pursuit` doubled to 80 BP on switch-out from `10/31 HP` after `Koffing`'s `Thief` had stolen `MUDKIP`'s held `Oran Berry`).
  - **NOCTIS** (Hoothoot ♂, Lv. 8) — Died on Turn 948 to Team Magma Grunt's `Lv. 9 Houndour` (`Ember`).
  - **ATHENA** (Spearow ♀, Lv. 15, Rash, `Keen Eye`, `Secret Power`) — Died on Turn 950 to Team Magma Grunt's `Lv. 9 Houndour` (`Pursuit`) after rolling 25% full paralysis at `2/39 HP`.
  - **CIRCE** (Spoink ♀, Lv. 8) & **MERLIN** (Ralts ♂, Lv. 4) — Died on Turns 950–953 to `Lv. 9 Houndour` (immune to Psychic moves) — **TOTAL PARTY WIPEOUT (Attempt #6 Over)**.
- **Root Causes of Attempt #6 Wipe:**
  1. **Lopsided Party Levels (`Lv. 15 ATHENA` vs `Lv. 10 MUDKIP`):** We trained `ATHENA` all the way to the Lv. 15 cap while leaving `MUDKIP` at Lv. 10 (`13 Speed`, `31 HP`). Because `MUDKIP` was only Lv. 10, `Lv. 9 Houndour` (`~16 Speed`) outsped `MUDKIP`, forcing a switch at `10/31 HP` into `Houndour`'s `Pursuit`.
  2. **Unequipped `Pecha Berries` Against `Lv. 8 Koffing` (`Toxic`, `Protect`, `Thief`):** We had 4 `Pecha Berries` in our Bag that we never equipped. Equipping a `Pecha Berry` against `Koffing` immediately cures Turn 1 `Toxic` AND consumes the berry before Turn 2 `Thief` can steal an `Oran Berry`!
- **Tactical Rules for Attempt #7:**
  1. **Train BOTH `Mudkip` AND our Secondary Sweeper to Lv. 13–14 Before Entering Petalburg Woods:** Train `Mudkip` to **Lv. 13–14** (`~38–40 HP`, `~17–19 Speed`) before fighting the Petalburg Woods Team Magma Grunt `(26, 23)` so `Mudkip` outspeeds `Lv. 9 Houndour` and OHKOs it with `Water Gun` (and uses `Mud Sport` + `Water Gun` to beat lead `Lv. 8 Magnemite`).
  2. **Equip `Pecha Berry` Against `Lv. 8 Koffing` & Never Switch Out Against `Lv. 9 Houndour` (`Pursuit`):** Equip a `Pecha Berry` to auto-cure `Koffing`'s `Toxic` (and deny `Thief`), and never switch out of `Lv. 9 Houndour` (`Pursuit`).

---

## Attempt #7 Casualties & Wipe Post-Mortem (Turn 1128 — Route 102)
- **HELIOS** (Sunkern ♂, Lv. 4, `16 HP`, `Absorb`) — Died on Turn 1125 on Route 102 `(16, 5)` against Lass Tiana's `Lv. 6 Sunkern` (`Struggle` recoil from `1/16 HP`).
- **AKRAKEN** (Mudkip ♂, Lv. 11, `34 HP`, `Torrent`) — Died on Turn 1127 on Route 102 `(16, 5)` to end-of-turn `Leech Seed` sap (`1/34 -> 0/34 HP`) right as Lass Tiana sent out `Lv. 5 Togepi` after `AKRAKEN` KO'd `Lv. 6 Sunkern` — **TOTAL PARTY WIPEOUT (Attempt #7 Over)**.
- **Root Causes of Attempt #7 Wipe:**
  1. **Crit-KOing Our Route 102 Wild Encounter (`Lv. 6 Electrike`) with `Water Gun` (Turn 1090):** Used 40-BP `Water Gun` instead of 20-BP `Bubble` to weaken full-HP `Lv. 6 Electrike`, resulting in a `1/16` critical-hit OHKO and leaving us without a second real attacker on Route 102.
  2. **Challenging Optional Trainer Lass Tiana `(15, 5)` Without a Grass Counter:** Lass Tiana (`Lv. 6 Igglybuff`, `Lv. 6 Sunkern` [holds `Berry Juice`, knows `Leech Seed` (16 PP), `Protect` (10 PP), `Mega Drain` (10 PP), `Synthesis` (8 PP)], `Lv. 5 Togepi`) has **0 vision range / is 100% optional** (walking along `y=4` from `(25, 4)` to `(13, 4)` bypasses her completely!). Fighting her with only `Mudkip` + `Lv. 4 Sunkern` allowed her `Sunkern` to stall with `Synthesis` + `Berry Juice` + `Leech Seed`.
  3. **Gen 3 End-of-Turn `Leech Seed` Tick After KOing an Opponent (`Turn 1127 #118`):** In Gen 3, if you KO a Trainer's Pokémon while seeded by `Leech Seed`, end-of-turn `Leech Seed` STILL ticks at the end of that turn after the Trainer sends out their next Pokémon (`Togepi`). Because `Torrent Water Gun` left `40% HP` `Sunkern` at `1 HP` on Turn 1, `Sunkern` re-seeded `AKRAKEN` (`5 -> 1/34 HP`), and KOing `Sunkern` on Turn 2 triggered the fatal `1 -> 0/34 HP` `Leech Seed` tick upon `Togepi`'s send-out.
- **Tactical Rules for Attempt #8:**
  1. **Always Use `Bubble` (`Up, Right`, 20 BP) to Weaken Wild Encounters:** Never use `Water Gun` (40 BP) on a full-HP wild Pokémon so a `1/16` crit cannot KO our Nuzlocke encounter.
  2. **Skip Optional Lass Tiana `(15, 5)` Unless We Have a Flying/Bug/Poison Sweeper:** After harvesting the Route 102 Berries at `(24, 2)` and `(25, 2)`, walk `Down` 1 to `(25, 4)` and `Left` 12 along `y=4` to `(13, 4)` to fight **Bug Catcher Allen `(13, 2)`** and enter **Petalburg City** (unlocking Route 104 South and Petalburg Woods encounters!) without talking to Lass Tiana unless we caught a Flying/Bug/Poison counter (`Spearow`, `Wingull`, `Hoothoot`, `Gulpin`, `Ledyba`).

---

## Attempt #8 Wipe Post-Mortem (Turn 1224 — Oldale Town / Route 101)
- **Casualties:**
  - **ALEVIATHAN** (Mudkip ♂, Lv. 6, `22 HP`) — Fainted on Turn 1222 inside the Oldale Town Pokémon Center `(7, 5)` to overworld Poison (`PSN`) ticks (`1/22 -> 0/22 HP`) after being poisoned by a wild `Lv. 3 Weedle` (`Poison Sting`) on northern Route 101 — **TOTAL PARTY WIPEOUT (Attempt #8 Over)**.
- **Root Causes of Attempt #8 Wipe:**
  1. **Battling Wild `Weedle` (`Poison Sting`) Instead of Running:** On northern Route 101, `route101_trainer` stayed in for 3 turns against a wild `Lv. 3 Weedle`, getting inflicted with `PSN` at `11/22 HP`.
  2. **Single-Call Door Warp Desync in Subagent Healing Script:** When entering the Oldale Pokémon Center door `(6, 16)`, `route101_trainer` passed `["Up", "sleep 2000", "Up", "Up", "Up", "Up"]` in a single `press_buttons` call. Because `press_buttons` aborts the entire list as soon as the door warp triggers on the first `"Up"`, the `"sleep 2000"` and interior `"Up"` steps were skipped, and the subsequent call walked back out the door unhealed and took 7 overworld poison ticks walking back to Route 101 (`11 -> 4 -> 0/22 HP`).
- **Tactical Rules for Attempt #9:**
  1. **Immediately `RUN` (`Down, Right, A`) From Wild `Weedle` (`Poison Sting`) and `Pichu` (`ThunderShock` / `Static`) on Route 101:** Never trade hits with `Weedle` or `Pichu` during early Route 101 grinding.
  2. **Two-Call Pokémon Center Door Warp Rule:** Always separate stepping onto the Pokémon Center door `(6, 16)` (`tools.press_buttons([..., "Up"])`) from the interior healing sequence (`tools.press_buttons(["B", "sleep 1500", "Up", "Up", "Up", "Up", "Up", ...])`), and verify `HP == max_HP` before walking back into tall grass.

---

## Attempt #9 Casualties (Starting Turn 1225)
- **RAIJU** (Electrike ♂, Lv. 11, `31 HP`, Bashful, `Lightningrod`) — Died on Turn 1540 on Route 104 South `(10, 40)` against Lady Cindy's `Lv. 7 Azurill` (`Uproar`).
  - **Root Cause & Tactical Lesson:** In Generation 3, **ALL Normal-type moves (including `Uproar`, `Hyper Voice`, and `Swift`) are Physical**, and Lady Cindy's `Lv. 7 Azurill` is pure Normal-type (so it is NOT weak to Electric `ThunderShock`, unlike Water-type `Marill`) and can have **`Huge Power` (`2x Attack`)**, causing STAB `Uproar` (50 BP) to deal `23 HP` per hit (`31 -> 8 -> 0/31 HP`). Always use a fast high-power STAB sweeper (`ZEPHYR`'s 65-BP `BubbleBeam` or `CALYPSO`'s `Water Gun`) against `Azurill`, and remember that `Azurill` is Normal-type, not Water-type!

<hr>

<h1><code>Mechanics/UIAndControls</code></h1>

# UI, Controls & Overworld Mechanics (Verified)

## Naming Screen Keyboard (Turn 6)
- **Controls:**
  - `Select`: Cycle character sets (`UPPER` -> `lower` -> `OTHERS`).
  - `B`: Backspace (`BACK`).
  - `Start`: Jump cursor directly to `OK` button (press `A` after `Start` to confirm name).
- **Uppercase Grid (4 rows x 8 cols, cursor starts at `(0, 0)` = `A`):**
  - Row 0: `A` (0), `B` (1), `C` (2), `D` (3), `E` (4), `F` (5), ` ` (6), `.` (7)
  - Row 1: `G` (0), `H` (1), `I` (2), `J` (3), `K` (4), `L` (5), ` ` (6), `,` (7)
  - Row 2: `M` (0), `N` (1), `O` (2), `P` (3), `Q` (4), `R` (5), `S` (6), ` ` (7)
  - Row 3: `T` (0), `U` (1), `V` (2), `W` (3), `X` (4), `Y` (5), `Z` (6), ` ` (7)

## Cutscene & Warp Scripting (Turns 11–20)
- **Dialogue Advancement:** Pressing `B` with `sleep 1000` advances standard dialogue boxes cleanly at `FAST` text speed and is completely inert once overworld control returns (preventing accidental NPC/sign re-interactions).
- **Warp + Cutscene Combo in `run_code`:** A `tools.press_buttons` call that steps onto a warp tile automatically terminates upon leaving the overworld. A subsequent `tools.press_buttons(["B", "sleep 1000", ...])` call in the same `run_code` script executes during the post-warp cutscene, clearing both the warp and cutscene in one turn.

## Littleroot Town Coordinates (Turns 12–21)
- **Player's House (Brendan / Left House):**
  - Exterior Door: `(5, 8)`
  - 1F: Exit mat `(8, 8)` (step `Down` to exit), Stairs to 2F `(8, 2)` (step `Up` onto `(8, 2)` to warp).
  - 2F: Stairs doorway `(7, 1)` (step `Up` from `(7, 2)` to warp), Wall Clock `(5, 1)` (interact from `(5, 2)` facing `Up`; confirmation defaults to `NO`), Desk PC `(0, 1)` (interact from `(0, 2)` facing `Up`).
- **Rival's House (May / Right House):**
  - Exterior Door: `(14, 8)` (exits to `(14, 9)`).
  - 1F: Entry mat `(2, 8)`, Stairs to 2F at `(2, 2)` (walk `Up` 6 tiles from `(2, 8)` onto `(2, 2)` to warp!).
  - 2F: Entry at `(1, 2)`, Poké Ball at `(5, 4)` (walk `Down, Down, Right, Right, Right` to `(4, 4)` facing `Right` and press `A` to trigger May's entrance; exit via stairs at `(1, 1)`).
  - Littleroot North Exit (after meeting May): NPC girl stands at `(10, 1)`; bypass via `(11, 1) -> (11, 0)` onto Route 101!

## Battle & Menu Persistence Mechanics (Turns 29–42)
- **No In-Battle Bag Healing (Turn 36):** Selecting `POTION` in the `BAG` during battle only shows `▶CANCEL`. Healing items from the Bag can only be used in the overworld. Held items (e.g. `BERRY JUICE`) still activate automatically in battle.
- **Battle Menu Cursor Memory & Drain Move Timing (Turns 36, 238, 293, 1113):** The 2x2 battle menu (`FIGHT` / `BAG` / `POKéMON` / `RUN`) resets to `▶FIGHT` at the start of each new battle, and remembers the last used quadrant within the same battle; always press bounded `Up, Left, A` on the action menu to guarantee `▶FIGHT`. The move menu (`FIGHT`) and Bag pocket (`ITEMS` / `POKé BALLS`) persist across battles. Note that when two HP-draining moves (e.g., `Mega Drain` + `Absorb`) execute in the same turn, the animations and drain text take ~15.0s total—use `["Up", "Left", "A", "sleep 600", "<Move>", "sleep 9500", "B", "sleep 5000", "B", "sleep 1500"]` (16.6s/turn) in multi-turn loops to prevent input desync.
- **Start Menu, Bag Row & Party Slot Cursor Memory (Turns 41–42, 296, 306, 575, 926, 1092, 1096, 1349):** The Start menu remembers its cursor row index across openings (`0: POKéDEX`, `1: POKéMON`, `2: BAG`, `3: ORION`, `4: SAVE`, `5: OPTION`, `6: EXIT`). Note: if `intro_runner` sets `TEXT SPEED: FAST` from the pre-game Main Menu without opening the overworld `Start` menu, the first overworld `Start` press starts at **Row 0 (`▶POKéDEX`)** (`Down` 5 times to `OPTION`); if `intro_runner` opened `OPTION` in the overworld before obtaining the Pokédex, the first `Start` press after obtaining the Pokédex starts at **Row 3 (`▶ORION`)**. Inside the `BAG`, switching pockets (`Left`/`Right`) wraps between Dot 1 (`ITEMS`) and Dot 5 (`KEY ITEMS`) and preserves the vertical row index across pockets (`Row 1` in `BERRIES` stays `Row 1` in `ITEMS`); always press bounded `Up` inside `ITEMS` to guarantee Row 0 (`POTION`). Also, using an item from the `BAG` in the overworld opens the Party screen with the cursor on whichever Party slot was last selected during an in-battle switch; **NEVER press `Up` from Slot 1 on the Party screen because `Up` wraps vertically to `CANCEL` (and `Left` from `CANCEL` stays on `CANCEL`!)**—instead, press `Left` alone in the overworld to select Slot 1. When backing out of a Pokémon's `SUMMARY` screen with `B`, the Party screen reappears with that Pokémon's `▶SUMMARY / SWITCH / ITEM / CANCEL` popup menu still open (press `B` a second time to close the popup before moving the Party cursor). Note that **in battle**, switching Pokémon swaps their Party screen boxes so the **currently active Pokémon on the field is ALWAYS in the Left Box (Slot 1)** and the benched Pokémon is in the **Right Column (Slot 2)**—so switching back to a benched Pokémon in battle requires pressing **`Right, A, sleep 600, A`**! Opening or closing the `BAG` or `POKéMON` menu triggers a ~2.0–2.5s screen fade; always wait `sleep 2500` after selecting or backing out of those submenus.
- **Weakening Wild Encounters Without Crit Risk (Turn 1090):** Never use `Water Gun` (40 BP) to weaken a full-HP wild Pokémon when `Bubble` (Slot 2: `Up, Right`, 20 BP) can safely chip it without risking a `1/16` critical-hit OHKO.
- **Birch's Lab Coordinates (Turn 42):** Birch stands at `(6, 4)`, player stands at `(6, 5)`, exit mat is straight down at `(6, 12)`.

## Pokémon Center Healing Formula (Verified Turn 57)
- **Interior Coordinates:** Enter at `(7, 8)`. Walk 5 tiles `Up` to stand at `(7, 4)` facing Nurse Joy across the counter at `(7, 3)`. The Pokémon Storage PC is at `(10, 1)` (interact from `(10, 2)` facing `Up`; `(11, 2)` is the Profile NPC). To deposit a Pokémon: press `A` 4 times (`sleep 1500`), `Down, A` (`sleep 2500`) to open `DEPOSIT POKéMON` (cursor starts on Slot 1 left column; `Right` moves to Slot 2 top-right), `A, A, A, A` to deposit into `BOX 1`, and `B` 4 times to log off. From `(10, 2)`, walk `Down` 2 to `(10, 4)`, `Left` 3 to `(7, 4)`, and `Down` **5** times (`y=4 -> y=8`, plus 1 step `Down` off `(7, 8)`) to exit.
- **Button Sequence:**
  - Press `A` **4 times** with `sleep 1200` between presses (clears Nurse Joy's 3 intro lines and confirms `▶YES` on the 4th `A`).
  - Wait `sleep 5500` for the healing jingle to finish.
  - Press `B` **4 times** with `sleep 1000` between presses to close her post-healing dialogue without re-talking.
  - Press `Down` **5 times** to exit back to the overworld.

## Verified Route & Town Coordinates (Turns 45–60, 1079–1091)
- **Littleroot Town (Lab to Route 101):**
  - Birch's Lab exterior door: `(7, 16)`; exiting the Lab places you at `(7, 17)` (already below the Lab sign row; note that the Lab signpost is at `(9, 11)` next to the top-right corner of the Lab roof). From `(7, 17)`, walk `Right` 3 tiles to `(10, 17)`, then `Up` 17 tiles along `x=10` to `(10, 0)`. When walking south along `x=10` from `(10, 0)` to `(10, 17)`, use a coordinate-checking loop in case a wandering NPC temporarily stands on `(10, 13..15)`.
- **Route 101 Pathing:**
  - **100% Grass-Free Northbound (Littleroot -> Oldale, Verified Turn 1287):** Enter at `(10, 19)` -> `Up` 4 to `(10, 15)` -> `Left` 3 to `(7, 15)` -> `Up` 5 to `(7, 10)` -> `Right` 6 to `(13, 10)` -> `Up` 1 to `(13, 9)` -> `Right` 4 to `(17, 9)` -> `Up` 5 to `(17, 4)` -> `Left` 2 to `(15, 4)` -> `Up` 1 to `(15, 3)` -> `Left` 1 to `(14, 3)` -> `Up` 1 to `(14, 2)` -> `Left` 4 to `(10, 2)` -> `Up` 5 into Oldale Town `(10, 17)`. Note: On northern Route 101 row `y=2`, `(5..10, 2)` is clear ground while `(3..4, 2)` is tall grass.
  - **Southbound (Oldale -> Littleroot):** Jump straight `Down` along `x=10` over the two south-facing ledges at `y=6` and `y=13`!
- **Oldale Town:**
  - South border (from Route 101): `(10, 19)` / `(11, 19)`.
  - Pokémon Center door: `(6, 16)` (exits to `(6, 17)`). After stepping `Down` out of the Pokémon Center `(6, 16)` or Poké Mart `(14, 6)`, always wait `["B", "sleep 2500"]` for the door-exit step animation to finish before sending directional inputs. From `(6, 17)`, walk `Right` 5 to `(11, 17)` and `Up` 7 along column **`x=11`** to `(11, 10)` to bypass the wandering girl NPC at `x=8..9, y=13..14`, then walk `Left` along `y=10` into Route 102 `(49, 10)`.
  - Poké Mart door: `(14, 6)` (exits to `(14, 7)`; free Potion clerk stands at `(13, 7)`, so step `Down` from `(14, 7)` to `(14, 8)` before walking `Left`).
  - North border (to Route 103): `x=10, y=0` (transitions to `(10, 21)` on Route 103).

## Verified Findings (Turns 124–150)
- **Mudkip Growth & Modified Learnset (Turns 124, 301):**
  - Uses the **Slow EXP group** (`5 * n^3 / 4`: 135 EXP for Lv. 5, 270 for Lv. 6, 428 for Lv. 7, 1250 for Lv. 10).
  - Learns `Bubble` (20 BP Water Special, 30 PP) at **Lv. 6**, `Mud Sport` (15 PP) at **Lv. 7**, and `Water Gun` (40 BP Water Special, 25 PP) at **Lv. 10**.
- **Wild Encounter Pools Observed:**
  - **Route 101 (Claimed by Starter):** Lv. 2–3 `Wurmple` (`Tackle`, `String Shot`), `Weedle` (`Poison Sting`, `String Shot`), `Caterpie` (`Tackle`, `String Shot`), `Pidgey`, `Sentret` (`Quick Attack`), `Rattata` (`Quick Attack`, `Tail Whip`), `Poochyena` (`Tackle`, `Howl`), `Zigzagoon` (`Swift`, `Sand-Attack`, holds `Berry Juice`), `Pichu` (`ThunderShock`, `Charm`, Ability: `Static`), `Togepi` (`Growl`, `Charm`, `Metronome`), `Igglybuff` (`Sing`, `Charm`), `Cleffa` (`Charm`, `Encore`, Ability: `Cute Charm`). Note: The left northern grass patch sits at `x=4..6, y=2..4` while `x=7..10, y=1..4` is a grass-free corridor.
  - **Two-Attempt `RUN` Cadence (Verified Turn 472):** `"Can't escape!▼"` prints in 1.5s and waits for a `B` press before the wild Pokémon executes its ~7.5s attack. Use `["Down", "Right", "A", "sleep 1800", "B", "sleep 7500", "B", "sleep 1000", "A", "sleep 1800", "B", "sleep 2500"]`—if Attempt 1 succeeds, the trailing `A` and `B` are completely inert in the overworld; if Attempt 1 fails, the cursor stays on `▶RUN` so the second `A` triggers Attempt 2 cleanly.
  - **Options `TEXT SPEED` Wrap-Around (Verified Turn 465):** In `OPTION`, `TEXT SPEED` wraps around (`SLOW -> MID -> FAST -> SLOW`). Pressing `Right` once from `MID` selects `FAST`, whereas pressing `Right` twice from `MID` wraps back to `SLOW`.
  - **Route 103:** Lv. 4 `Poliwag` (`Water Gun`, 44 EXP), `Skitty` (`Attract`), `Wingull` (`Water Gun`, `Wing Attack` 60 BP STAB, 10 Speed), `Ledyba` (`Silver Wind` — **100% chance to boost all 5 stats `+1 Atk/Def/SpA/SpD/Spd` on every hit in this ROM!**), `Sunkern` (`Absorb`, `Growth`), `Spoink` (`Confusion`), `Ekans`, `Spearow`, `Hoppip`, `Mareep` (`ThunderShock`). Note: Optimal **1-grass-tile** path to Rival May `(10, 3)`/`(10, 4)` (who wanders vertically between `(10, 3)` and `(10, 4)`): from Oldale `(10, 17)`, take **26** steps `Up` to `(10, 13)` -> `Right` 4 to `(14, 13)` -> `Up` **7** to `(14, 6)` -> `Left` 9 along `y=6` to `(5, 6)` (the **only** grass tile!) -> `Up` 2 through `(5, 5)` to `(5, 4)` -> `Right` 4 to `(9, 4)` (or `(9, 3)`). Initiate May's dialogue and confirm the battle starts before queuing move inputs.
  - **Route 102:** Lv. 6 `Gulpin` (`Yawn` [inflicts immediate sleep], `Acid`, `Pound`), Lv. 4 `Ralts` (`Confusion`, Ability: `Synchronize`), Lv. 6 `Hoothoot`, Lv. 6 `Electrike` (`ThunderShock`, Ability: `Static`), Lv. 6 `Nidoran♀`.
  - **Route 104 (South):** Lv. 7 `Cubone` (`Bone Club` / `Headbutt`), Lv. 7 `Spoink` (`Confusion`, `Psywave`, `Splash` — Base 80 SpD vs Base 35 Def; use physical `Tackle` or `Wing Attack`, never `Water Gun`!), Lv. 7 `Natu` (`Peck`, `Leer`, `Night Shade`), Lv. 7 `Venonat` (`Leech Life`), Lv. 7 `Nidoran♀` (`Poison Point`), Lv. 7 `Jigglypuff` (`Sing`, `Cute Charm` — `RUN` immediately), Lv. 7 `Snubbull` (`Intimidate`), Lv. 7 `Mareep` (`ThunderShock`, `Thunder Wave`, `Static` — `RUN` immediately), Lv. 7 `Seedot` (Grass — `RUN` immediately).
  - **Petalburg Woods:** Lv. 8 `Teddiursa` (`Scratch`, `Lick`, `Faint Attack`, Ability: `Guts`), Lv. 8 `Pineco` (`Selfdestruct` risk — `RUN` immediately!), Lv. 8 `Hoothoot`.
- **Petalburg City West Border Tree `(1, 11)` (Verified Turn 1505):** Walking east from Route 104 South `(39, 61)` into Petalburg City `(0, 11)` hits a tree at `(1, 11)`. Always enter Petalburg City from Route 104 South along `y=62` (`(28, 61)` -> `Up` to `(28, 60)` -> `Right` 6 to `(34, 60)` -> `Down` 2 to `(34, 62)` -> `Right` 6 into Petalburg City `(0, 12)` -> `Right` 2 to `(2, 12)` -> `Up` 1 to `(2, 11)` -> `Right` 16 along `y=11` to `(18, 11)`).
- **Southbound Grass-Free Ledge Corridor & Mom's Heal (Turns 130–146):**
  - Walking straight `Down` along column **`x=10`** from `(10, 4)` on Route 103 jumps over both ledges (`y=5`, `y=12`) into Oldale Town with **0 grass tiles**.
  - Walking straight `Down` along column **`x=10`** across Route 101 jumps over both ledges (`y=6`, `y=13`) into Littleroot Town with **0 grass tiles**.
  - Inside the Littleroot 1F house (door `(5, 8)` -> mat `(8, 8)`), **Mom** sits at **`(2, 6)`** (talk from `(2, 5)` facing `Down`) and provides a free full HP + status heal.
- **Overworld Warp & Grass Timing Workarounds (Turns 124–149):**
  - Insert `["B", "sleep 800"]` (or `["B", "sleep 2500", "B"]`) between a door warp step and subsequent movement so the transition fade completes before walking.
  - Insert `"sleep 300"` before changing direction inside tall grass so the 4-frame grass-rustle animation does not drop the turn input.
- **Nickname Prompt Transition (Turns 207, 534):** When catching a **new** Pokédex species, advancing from `"Gotcha! X was caught!▼"` to selecting `▶YES` on `"Give a nickname to the captured X?"` requires **4 `A` presses** (`A #1` -> `"X's data was added to the POKéDEX.▼"`, `A #2` -> Pokédex entry page, `A #3` -> `"Give a nickname...?"`, `A #4` -> `▶YES` opens keyboard at `(0, 0) = 'A'`). Do not send an extra `A` after the 4th `A` before directional inputs on the naming grid, or it will type `'A'` as the first character.
- **Route 102 Layout & Trainers (Turns 175–177, 303–314, 529–570, 1095–1110):**
  - Enter Route 102 from Oldale Town `(0, 10)` at `(49, 10)`.
  - Safe northern tall grass patch (away from trainers): `x=37..38, y=3..6` (approach via `(38, 10) -> (38, 7) -> (37, 7) -> (37, 6)`).
  - Grass-free path to Youngster Calvin: walk `Left` to `(38, 10)`, `Down` 4 tiles to `(38, 14)`, and `Left` 4 tiles to `(34, 14)`.
  - **Youngster Calvin** stands at **`(33, 14)`** facing `Down` and has 3 Lv. 6 Pokémon (`Sentret` [Assist->Rock Smash / Mud-Slap / Super Fang, Quick Attack], `Zigzagoon` [Swift, Sand-Attack], `Poochyena` [Super Fang, Rock Smash, Howl]).
  - Grass-free path from `(34, 14)` to Bug Catcher Rick: `Down` 2 to `(34, 16)`, `Left` 6 to `(28, 16)`, `Up` 1 to `(28, 15)`, `Left` 2 to `(26, 15)`.
  - **Bug Catcher Rick** stands at **`(25, 15)`** facing `Up` and has 4 Lv. 5 Pokémon (`Caterpie` [holds `Berry Juice`], `Wurmple` [String Shot], `Kakuna` [holds `Berry Juice`, Poison Sting], `Cascoon` [holds `Berry Juice`, knows `Iron Defense`, `Tackle`]).
  - **In-Battle Shift & Move Cursor Rules (Turns 308–313):** Using a Potion on a party Pokémon in the overworld resets the in-battle move cursor back to Slot 0 (`Tackle`). In Trainer battles with 2+ party Pokémon on `SHIFT` mode, follow potential KO attacks ONLY with `B` presses so `B` automatically selects `NO` on `"Will ORIQP change POKéMON?"`.
  - **Lass Tiana** wanders across **`(15..16, 5..6)`** and has 3 Pokémon (`Lv. 6 Igglybuff` [Ability: `Cute Charm`, holds `Oran Berry`, uses `Present`], `Lv. 6 Sunkern` [holds `Berry Juice`, knows `Leech Seed`, `Protect`, `Mega Drain`, `Absorb`], `Lv. 5 Togepi`).
  - **Bug Catcher Allen** stands at **`(13, 2)`** facing `Down` and has 4 Lv. 7 Pokémon (`Weedle` [`Poison Sting`], `Silcoon` [holds `Sitrus Berry`, `Iron Defense`], `Wurmple` [`Tackle`], `Metapod`).
  - **Grass-Free Exit from Bug Catcher Allen `(13, 4)` to Petalburg City (Verified Turn 586):** Walk `Left` 2 to `(11, 4)`, `Down` 4 to `(11, 8)`, and `Left` 12 along grass-free `y=8` into Petalburg City at `(29, 18)`.
  - **Petalburg City Coordinates (Verified Turns 588–590):**
    - East entrance (from Route 102): `(29, 18)`.
    - Pokémon Center door: `(20, 16)` (exits to `(20, 17)`).
    - Poké Mart door: `(25, 12)` (exits to `(25, 13)`; approach from `(18, 11)` via `Right` 5 to `(23, 11)`, `Down` 2 to `(23, 13)`, `Right` 2 to `(25, 13)`, `Up` 1 into `(25, 12)`).
    - Petalburg Gym door: `(15, 8)` (exits to `(15, 9)`).
    - West exit (to Route 104 South): From `(15, 9)`, walk `Left` 3 to `(12, 9)`, `Down` 2 to `(12, 11)`, `Left` 10 to `(2, 11)` (triggers Scott's intro dialogue at `(4, 11)`), `Down` 1 to `(2, 12)`, and `Left` 3 onto Route 104 South at `(39, 62)`.
  - **Route 104 (South) Coordinates (Verified Turns 601–653, 885–888):**
    - East entrance (from Petalburg City `(0, 12)`): `(39, 62)` (`x=32..39, y=61..63` is grass-free; solid forest trees occupy `x=33..42, y=56..60`, blocking the trees above `y=56`, and a non-trainer NPC stands at `(29, 61)`).
    - Tall grass patch: `x=22..24, y=60..61` (approach from `(38, 61)` via `Left` 4 to `(34, 61)`, `Up` 1 to `(34, 60)`, `Left` 6 along `y=60` above the NPC at `(29, 61)` to `(28, 60)`, `Down` 1 to `(28, 61)`, and `Left` 4 into `(24, 61)`).
    - Stairs to lower beach: `x=27..28, y=69..70` (walk `Down` along `x=28` to `(28, 71)` to clear the cliff corner at `(26, 70)`, then `Left` onto the beach at `x=20`).
    - **Bird Keeper Billy `(23, 66)`:** Turns toward footsteps on sand; has 3 Lv. 7 Pokémon (`Pidgey` [`Sand-Attack`], `Wingull` [holds `Oran Berry`, `Supersonic`, `Gust`, `Water Gun`], `Taillow`).
    - **Fisherman Darian `(15, 59)`:** Mandatory trainer facing `Right` across the 3-tile beach bottleneck `x=16..18, y=59` (directly above the non-trainer straw-hat NPC at `(15, 60)`). Has **4 Pokémon** (`Lv. 9 Magikarp` [`Bounce`, `Tackle`], `Lv. 8 Feebas` [holds `Sitrus Berry` +30 HP, knows `Yawn`/`Hypnosis`, `Water Pulse`, `Facade`], `Lv. 7 Goldeen` [holds `Berry Juice`, `Rain Dance`, `Peck`], and `Lv. 7 Luvdisc`).
    - **Northern Route 104 South Berry Trees & Lady Cindy (Verified Turns 910–913, 1495):** Stairs from beach to Mr. Briney's Cottage are at `x=16..17, y=54`. From `(17, 52)`, walk `Right` 4 to `(21, 52)` and `Up` 10 along `x=21` to `(21, 42)` to reach the Berry trees at `(22, 41)` (`2 Oran Berries`) and `(24, 41)` (`2 Pecha Berries`). **Lady Cindy** stands at **`(11, 40)`** facing `Left` across the 2-tile dirt entrance `(10..11, 40)` to Petalburg Woods (`(10..11, 38)`); she has **3 Pokémon** (`Lv. 8 Cleffa`, `Lv. 8 Pichu`, `Lv. 7 Azurill` — all OHKO'd by `ATHENA`'s `Secret Power`, paying `$1,400`).
  - **Petalburg Woods Coordinates & Trainers (Verified Turns 915–921):**
    - South entrance (from Route 104 South `(10, 38)`): `(16, 38)` (or `(17, 38)` from `(11, 38)`).
    - Safe tall grass patch near south entrance: `x=21..23, y=33..35` (approach from `(16, 38)` via `Up` 3 to `(16, 35)` and `Right` 5 to `(21, 35)`).
    - **Bug Maniac Lyle `(13, 35)`:** Faces `Up` across `(13, 34)`; has **3 Lv. 8 Pokémon** (`Spinarak`, `Ledyba`, `Venonat` — all OHKO'd by `ATHENA`'s `Peck`).
    - **Western Grass-Free Corridor & Bug Catcher James (Verified Turns 923–924):** From `(13, 34)`, walk `Left` 6 to `(7, 34)`, `Up` 2 to `(7, 32)`, `Left` 2 to `(5, 32)`, `Up` 6 along grass-free `x=5` to `(5, 26)`, `Right` 1 to `(6, 26)`, `Up` 2 to `(6, 24)`, and `Right` 3 to `(9, 24)` (facing **Bug Catcher James** at `(10, 24)` with **0 grass tiles**). James has **3 Pokémon** (`Lv. 9 Paras`, `Lv. 8 Surskit`, `Lv. 9 Nincada`).
    - **Central Grass-Free Corridor to Team Magma Grunt (Verified Turns 927–947):** From `(9, 24)`, walk `Left` 2 to `(7, 24)`, `Down` 1 to `(7, 25)`, `Right` 8 along grass-free `y=25` to `(15, 25)`, `Down` 1 to `(15, 26)`, `Right` 11 along grass-free `y=26` to `(26, 26)`, and `Up` along grass-free `x=26..28` to trigger the Devon Researcher & **Team Magma Grunt** `(26, 23)` cutscene with **0 grass tiles**. The Team Magma Grunt has **4 Pokémon** (`Lv. 8 Magnemite` [`Thunder Wave`, `ThunderShock`], `Lv. 8 Koffing` [`Toxic`, `Protect`, `Thief`], `Lv. 9 Houndour` [`Ember`, `Pursuit`], and 4th unseen).
  - **Grass-Free Corridor Past Ledge to Berry Trees `(24, 3)` (Verified Turns 1105, 1460):** There is a split south-facing ledge at `y=6` (`x=16..17, y=6` and `x=19..25, y=6`) with a **1-tile gap at `(18, 6)`**, and both column `x=25` (`y=7..13`) and row `y=7` (`x=16..25`) are 100% grass-free! From Bug Catcher Rick `(26, 15)`, walk `Up` 2 to `(26, 13)`, `Left` 1 to `(25, 13)`, `Up` 6 along grass-free `x=25` to `(25, 7)`, `Left` 7 along grass-free `y=7` to `(18, 7)`, `Up` 3 through the `(18, 6)` ledge gap to `(18, 4)`, `Right` 6 along `y=4` to `(24, 4)`, and `Up` 1 to `(24, 3)` (**0 grass tiles!**).
  - **Berry Tree Harvesting & Equipping Formula (Turns 319, 560):** Press `A` **3 times** with `sleep 1200` (`sleep 3000` after the 3rd `A`) to confirm picking the Berries, then press `B` **3 times** (`sleep 1200`) to close the text without re-interacting with the loamy soil (which otherwise opens the `BERRIES POCKET` and resets the in-battle move cursor to Slot 0). Inside the `BAG -> BERRIES` pocket (Dot 4), Berries are sorted by Berry Number (`No03 PECHA BERRY` Row 0, `No07 ORAN BERRY` Row 1), and the 2x2 Berry popup menu starts at `▶CHECK TAG` (`Down, Right, A` selects `GIVE`). Note that in Gen 3, end-of-turn `Leech Seed` damage does NOT trigger a held `Oran Berry` on the turn it drops HP below 50%, whereas switching in or taking direct attack damage at `<50% HP` triggers it immediately!
  - **Poké Mart Overworld Purchase Formula (Turns 377, 792):** Poké Mart interior entry mat is at `(3, 7)`; walk `Up` 4 tiles to `(3, 3)` and `Left` to face the clerk, and `Down` 5 tiles to exit back outside. Talking to a Mart clerk from the overworld requires **3 `A` presses** to open the `BUY` screen (`"A", "sleep 1200"` for `"Welcome!"`, `"A", "sleep 1200"` for `"How may I serve you?"`, and `"A", "sleep 3000"` to select `▶BUY` and wait for the 2.7s fade-in).
  - **Deterministic Wild Encounter Detection & 150-Button Limit in `run_code` (Turns 371, 897):** Because `tools.press_buttons` returns `"Success"` in Python even when aborted by a wild battle, pass pure movement steps across grass without interleaved sleeps and check `mgba.get_coordinates()` afterward. Note that the 150-button cumulative limit per `run_code` script counts the full length of each list passed to `tools.press_buttons()` even if movement aborts early on a warp or wild encounter; pass smaller 16-button chunks in a loop when searching grass.

<hr>