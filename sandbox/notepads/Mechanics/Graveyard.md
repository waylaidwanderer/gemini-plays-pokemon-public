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
- **ZEPHYR** (Wingull ♀, Lv. 15, Quiet), **ARCTURUS** (Teddiursa ♂, Lv. 8, Sassy), **CALYPSO** (Mudkip ♀, Lv. 14), & **ATLAS** (Cubone ♂, Lv. 8, Mild) — Died on Turns 1638–1644 on Route 104 North `(24, 8)` against **PKMN Trainer Red**'s `Lv. 9 Pikachu` (`Shock Wave`, `Surf`, `Thunder Wave`, holds `Sitrus Berry` [+30 HP], custom boosted stats `~36 HP` / `~21 Spd`) — **TOTAL PARTY WIPEOUT (Attempt #9 Over)**.
- **Root Causes of Attempt #9 Wipe:**
  1. **Didn't Set Up `Mud Sport` (`Down, Left`) Against Red's Passive Lead `Lv. 9 Eevee` (`Curse`):** Red's lead `Lv. 9 Eevee` used `Curse` 4 turns in a row for 0 damage. In Gen 3, `Mud Sport` (`STATUS3_MUDSPORT`) persists on `Mudkip` across enemy KOs as long as `Mudkip` stays on the field. Had `CALYPSO` used `Mud Sport` on Turn 1 against `Eevee` before 4HKOing `Eevee` with `Water Gun`, `CALYPSO` would have faced `Lv. 9 Pikachu` at `40/40 HP` with `Mud Sport` ALREADY active (halving `Shock Wave` from `23` to `11 damage`)!
  2. **Entered PKMN Trainer Red `(29, 8)` with Two Untrained `Lv. 8` Teammates (`ATLAS` at `13/27 HP` Unhealed, `ARCTURUS` at `Lv. 8`) and Unused `Oran Berries` in the Bag:** We had 2 `Oran Berries` in the Bag that we never equipped on `CALYPSO` or `ATLAS`, left `ATLAS` at `13/27 HP`, and left both `ATLAS` and `ARCTURUS` at Level 8 instead of training our 3rd and 4th teammates to Level 13–14 before crossing the Route 104 North bridge.
- **Tactical Rules for Attempt #10:**
  1. **Train 3–4 Party Members to Level 13–14 Before Route 104 North:** Never challenge Route 104 North (`PKMN Trainer Red` at `(29, 8)` has 6 Lv. 9 Pokémon holding `Sitrus Berries`) with Lv. 8 filler teammates. Train `Mudkip` to **Lv. 14–15** AND train at least **2–3 caught teammates to Lv. 13–14** before crossing the Route 104 North bridge.
  2. **Heal to 100% HP, Equip `Oran Berries`, and Use `Mud Sport` on Turn 1 vs Red's Lead `Lv. 9 Eevee`:** Before stepping onto `(24, 8)`, heal all party members to 100% HP and equip `Oran Berries` from `(3, 23)`. On Turn 1 vs `PKMN Trainer Red`'s lead `Lv. 9 Eevee` (`Curse`), use **`Mud Sport` (Slot 3: `Down, Left`)** on `Mudkip` BEFORE knocking out `Eevee` with `Water Gun` so `Mud Sport` is already active when `Lv. 9 Pikachu` (`Shock Wave`, `Surf`, `Thunder Wave`, `Sitrus Berry`) is sent out!
---

## Attempt #10 Casualties (Starting Turn 1646)
- **OBERON** (Ledyba ♂, Lv. 8, `26 HP`, Brave, `Swarm`, `Silver Wind`, `Aerial Ace`) — Died on Turn 1915 on Route 101 `(4, 2)` to a wild `Lv. 3 Pidgey` (`Quick Attack`) during `level10_grinder` execution after taking two `Quick Attack` hits from a wild `Lv. 3 Sentret` (`16 -> 6 -> 0/26 HP`).
  - **Lesson:** Do not delegate fragile early-stage Bug/Flying Pokémon (`Lv. 4–8 Ledyba`, Base 30 Defense) to `level10_grinder` on Route 101 where wild `Sentret`, `Rattata`, and `Pidgey` spam priority `Quick Attack`; instead, switch-train fragile catches or level them directly with supervised healing.
- **.pw'** (Mudkip ♂, Lv. 10, `32 HP`, `Torrent`, `Water Gun`) — Died on Turn 1919 on Route 102 `(26, 15)` against Bug Catcher Rick's `Lv. 5 Kakuna` / `Lv. 5 Cascoon` after queuing a 4-turn `Water Gun` loop while poisoned (`PSN`) instead of switching to `TERRA` or executing 1 turn at a time.
  - **Lesson:** NEVER queue multi-turn attack loops when your active Pokémon is poisoned (`PSN`); switch immediately to an unpoisoned teammate or step 1 turn at a time to monitor HP after every poison tick.
- **TERRA** (Sandshrew ♂, Lv. 10, `31 HP`, Rash, `Sand Veil`) — Died on Turn 1933 on Route 102 `(15, 4)` against Lass Tiana's `Lv. 6 Sunkern` (`Mega Drain` + `Leech Seed` from `13/31 HP`) after accidentally stepping into Lass Tiana's upward line of sight at `(15, 4)` while unhealed (`21/31 HP`) and with our newly harvested `Oran Berries` still unequipped in the Bag — **TOTAL PARTY WIPEOUT (Attempt #10 Over)**.
- **Root Causes of Attempt #10 Wipe:**
  1. **Unsupervised Subagent Grinding with Fragile `Lv. 4–8 Ledyba` (`OBERON`):** Delegated `OBERON` (Base 30 Def) to `level10_grinder` on Route 101 where wild `Sentret`/`Pidgey` use priority `Quick Attack`.
  2. **Multi-Turn Loop While Poisoned Against Bug Catcher Rick (`.pw'`):** Queued a 4-turn `Water Gun` loop while `.pw'` was poisoned (`PSN`) by `Kakuna`'s `Poison Sting`, instead of switching to `TERRA` or stepping 1 turn at a time.
  3. **Walking Across `(15..16, 4)` Before Equipping `Oran Berries` or Checking Lass Tiana's Facing Direction (`TERRA`):** After harvesting the `Oran` and `Pecha` Berries at `(24..25, 2)`, we walked straight to `(14, 4)` before healing or equipping an `Oran Berry`, and stepped onto `(15, 4)` right when Lass Tiana at `(15, 5)` was facing `Up`.
- **Tactical Rules for Attempt #11:**
  1. **Never Queue Multi-Turn Loops When Poisoned (`PSN`):** Switch out immediately or execute 1 turn at a time whenever poisoned.
  2. **Heal & Equip `Oran` / `Pecha` Berries Right at `(25, 3)` Immediately After Harvesting:** As soon as we pick the Berries at `(24, 2)` and `(25, 2)`, open the Bag right at `(25, 3)` to heal to 100% HP and equip an `Oran Berry` / `Pecha Berry` BEFORE taking a single step west toward `x=15..16`!
  3. **Pause at `(17, 4)` to Check Lass Tiana `(15..16, 5..6)`:** Stop at `(17, 4)` and inspect `<CurrentScreen>`: if we have a Flying/Bug/Poison counter (`Wingull`/`Spearow`/`Ledyba`/`Gulpin`/`Hoothoot`), challenge her at 100% HP with an `Oran Berry` equipped; if not, wait until she is on `y=6` or facing away from `Up` before walking `Left` 4 across `(16..13, 4)` to `(13, 4)`.

---

## Attempt #11 Casualties (Starting Turn 1935)
- **BOREAS** (Wingull ♂, Lv. 13, `34 HP`, Lax, `Keen Eye`, `BubbleBeam`, `Wing Attack`) — Died on Turn 2353 in Petalburg Woods `(26, 23)` to Team Magma Grunt's `Lv. 8 Bagon` (`Headbutt` critical hit `21 damage` + two consecutive confusion self-hits `34 -> 30 -> 9 -> 5 -> 0/34 HP`).
  - **Root Cause & Tactical Rule:** Queued a 2-turn `BubbleBeam` loop while `BOREAS` was still confused from `Duskull`'s `Confuse Ray`, instead of switching out to cure confusion or executing 1 turn at a time. **Rule:** NEVER queue multi-turn attack loops while confused (`Confuse Ray` / `Supersonic` / `Sweet Kiss` / `Water Pulse`); either switch out immediately to clear confusion for free or execute strictly 1 turn at a time.
- **MUDKIP** (Mudkip ♂, Lv. 13, `38 HP`, `Torrent`, `Bubble`, `Water Gun`, `Mud Sport`) — Died on Turn 2521 on Route 104 North `(28, 16)` in the Double Battle against Twins Gina & Mia's two `Lv. 8 Smeargle`.
  - **Root Cause & Tactical Lesson:** Right `Smeargle` (`Follow Me`, `Teeter Dance`, `Milk Drink`) re-confused `MUDKIP` with `Teeter Dance` on Turn 2519. On Turn 2521, `MUDKIP` hurt itself in confusion (`32 -> 26/38 HP`) while Right `Smeargle`'s `Follow Me` redirected `GAIA`'s single-target `Secret Power`, allowing Left `Smeargle` (`~10% HP`) to land an uninterrupted `Focus Punch` (`26 damage -> 0/38 HP`). **Rule:** Against Twins Gina & Mia, remember that Right `Smeargle` spams `Teeter Dance` (confusing the whole field) + `Follow Me`, and Left `Smeargle`'s `Focus Punch` deals `~26 HP` to neutral targets; use Poison-types (`Oddish` / `Gulpin`) that resist `Focus Punch` (`0.5x`) and use **`Acid`** (a 2-target spread move in Gen 3 that bypasses `Follow Me`!), and switch out confused Pokémon if in `Focus Punch` KO range.
- **GAIA** (Cubone ♀, Lv. 16, `45 HP`, Adamant, `Rock Head`, `Bone Club`, `Rock Throw`, `Secret Power`, `Headbutt`) — Died on Turn 2677 in Rustboro Gym `(5, 14)` to School Kid Josh's lead `Lv. 15 Geodude` (`Selfdestruct` after 85%-accurate `Bone Club` missed).
  - **Root Cause & Tactical Lesson:** In Rustboro Gym, trainers stand at `(1, 12)` and `(1, 11)` to block the left-aisle bypass, and School Kid Josh at `(8, 14)` leads with a **`Lv. 15 Geodude` that knows `Selfdestruct`** (`200 BP`, halving Defense in Gen 3). Using `GAIA`'s 85%-accurate physical `Bone Club` against `Geodude`'s Base 100 Defense risked both a 15% miss and failing to OHKO before `Selfdestruct`, whereas a Special Grass/Water attacker (`Gloom`'s never-miss 4x SE `Magical Leaf` or `Mudkip`'s 4x SE `Water Gun` against `Geodude`'s Base 30 Special Defense) outspeeds and OHKOs `Lv. 15 Geodude` on Turn 1 before it can use `Selfdestruct`. Always budget EXP using `Page 2: POKéMON SKILLS` (`NEXT LV.`) so your Special Grass/Water sweeper has ~500+ EXP of room to sweep the Rustboro Gym Trainers at Level 15–16!
- **HERMES** (Yanma ♂, Lv. 12, `40 HP`, Careful, `Speed Boost`, `Silver Wind`, `Foresight`, `Quick Attack`) — Died on Turn 2799 on Route 116 `(36, 17)` to Bug Maniac Jose's 4th Pokémon, `Lv. 10 Beedrill` (`Secret Power` critical hit `24 damage` on switch-in from `20/40 HP`).
  - **Root Cause & Tactical Lesson:** Switched `HERMES` (`20/40 HP`, `17 Defense`, where 70-BP `Secret Power` deals `12 damage` normal / `24 damage` crit) into `12% HP` `Lv. 10 Beedrill` to avoid giving EXP to `Lv. 20 ADONIS` (`20/59 HP`, `39 Defense`, where `Secret Power` deals only `5–6 damage` normal / `10–12 damage` crit). **Rule:** Never switch a fragile Pokémon into `1/16` critical-hit KO range (`2x` normal damage `>=` current HP) to preserve another teammate's level cap when a high-Defense teammate can tank even a critical hit.
- **RHEA** (Sandshrew ♀, Lv. 16, `45 HP`, Jolly, `Sand Veil`, `Dig`, `Sand-Attack`, `Scratch`, `Poison Sting`) — Died on Turn 2949 in Rustboro Gym `(5, 12)` to School Kid Tammy's 3rd Pokémon, `Lv. 15 Rhyhorn` (`Ice Beam` `30 damage` + `Megahorn` from `11/45 HP` after `Dig` dealt ~65% HP) — **TOTAL USABLE PARTY WIPEOUT (Attempt #11 Over; remaining party members `MEDEA` [Lv. 18] and `ADONIS` [Lv. 23] exceeded the Lv. 16 level cap)**.
- **Root Causes of Attempt #11 Wipe:**
  1. **Overleveling Our Grass Sweepers (`ADONIS` at Lv. 23, `MEDEA` at Lv. 18) Above the Lv. 16 Cap on Route 116:** We used `ADONIS` (`Gloom`, `Magical Leaf`) and `MEDEA` (`Gulpin`) to clear all of Route 116 after they had already reached Level 16, pushing both of them above the Level 16 cap so neither could be used in Rustboro Gym.
  2. **Losing Earlier Water/Flying/Ground Encounters (`MUDKIP`, `BOREAS`, `GAIA`) to Confusion & `Selfdestruct`:** Losing `MUDKIP` (Lv. 13) to Twins Gina & Mia's `Teeter Dance` + `Focus Punch` and `GAIA` (Lv. 16) to School Kid Josh's `Lv. 15 Geodude` (`Selfdestruct`) left `RHEA` (`Lv. 16 Sandshrew`) as our only `<= Lv. 16` Pokémon for Rustboro Gym.
  3. **School Kid Tammy `(1, 12)` Spots `(5, 12)` Across Row `y=12` & Carries `Lv. 13 Aron`, `Lv. 13 Corsola` (`Rock Tomb`, `Water Pulse`), and `Lv. 15 Rhyhorn` (`Ice Beam`, `Megahorn`):** In Rustboro Gym, `(2..5, 12)` is an open horizontal corridor, so School Kid Tammy at `(1, 12)` is mandatory and her 3rd Pokémon (`Lv. 15 Rhyhorn`) carries coverage `Ice Beam` (95 BP Ice) and `Megahorn` (120 BP Bug), which 2HKO a solo Ground-type.
- **Tactical Rules for Attempt #12:**
  1. **Strict Level Cap Budgeting (`<= Lv. 15` Entering Rustboro Gym, Never Exceed `Lv. 16` Before Roxanne):** Never allow ANY party Pokémon to exceed **Level 16** prior to defeating Roxanne. With 99 `Rare Candies` automatically refilled in the overworld, keep a balanced 5–6 Pokémon team at **Level 14–15** across Route 102, Route 104, Petalburg Woods, and Route 116 (skipping optional Route 116 trainers until after Roxanne if needed so nobody overlevels `Lv. 16`!).
  2. **Use `Battle Style: SET` Immediately in Options:** Ensure `BATTLE STYLE: SET` is configured in the `OPTION` menu alongside `TEXT SPEED: FAST`.
  3. **Preserve `Mudkip` -> `Marshtomp` (`Lv. 16`) + Grass/Water Teammates for Rustboro Gym:** Keep `Mudkip` alive (using `Bubble` spread move against Twins Gina & Mia!) and evolve it into **`Marshtomp` at Level 16** so `Marshtomp` + our Grass/Water teammates effortlessly sweep School Kid Josh (`(8, 14)`), School Kid Tammy (`(1, 12)`), and Gym Leader Roxanne within the Level 16 cap!

---

## Attempt #12 Casualties (Starting Turn 2951)
- **THETIS** (Poliwag ♀, Lv. 16, `41 HP`, Careful, `Swift Swim`, `BubbleBeam`, `Water Gun`, `Hypnosis`) — Died on Turn 3223 in Rustboro Gym `(5, 14)` to School Kid Josh's final Pokémon, `Lv. 14 Omanyte` (`Rock Tomb` + `Water Pulse`).
  - **Root Cause & Tactical Rule:** After `SIREN`'s `Seismic Toss` (`-15 HP`) and `THETIS`'s first `BubbleBeam`, we queued the second `BubbleBeam` alongside post-battle exit steps and Pokémon Center `A` presses in a single `run_code` script. When `Omanyte` survived the second `BubbleBeam` at `1 HP` and dropped `THETIS` to `6/41 HP` and `-2 Speed` (`18 Speed` vs `Omanyte`'s `19–20 Speed`) with `Rock Tomb`, the trailing `Up` and `A` presses from the Pokémon Center healing sequence selected `FIGHT -> BubbleBeam` on the next turn instead of switching out. **Rule:** NEVER queue post-battle overworld movement or `A` presses in the same `run_code` script as an in-battle attack turn; always end battle turns with `B` presses only and visually confirm the battle has ended on `<CurrentScreen>` before sending overworld inputs.
- **HERACLES** (Makuhita ♂, Lv. 15, `49 HP`, Modest, `Thick Fat`, `Vital Throw`, `Force Palm`) — Died on Turn 3230 in Rustboro Gym `(5, 12)` to School Kid Tammy's lead `Lv. 13 Aron` (`Aerial Ace`).
  - **Root Cause & Tactical Rule:** On Turn 1, `HERACLES` (`15 Speed`) won a 50/50 Speed tie against `Lv. 13 Aron` (`15 Speed`) and left `Aron` at `1 HP` with `Force Palm` while `Aron`'s `Aerial Ace` dealt `32 damage` (`49 -> 17/49 HP`). We mistakenly assumed `HERACLES` moving first on Turn 1 meant `HERACLES` was strictly faster rather than speed-tied (`15 Speed == 15 Speed`), and stayed in at `17/49 HP` (`< 32` normal damage), losing the 50/50 Speed tie on Turn 2. **Rule:** Moving first once only proves `YourSpeed >= EnemySpeed` (which includes a 50/50 Speed tie!). Never stay in when `Current HP <= Enemy Attack Damage` (`17 <= 32`) unless your Speed is verified to be strictly higher than the enemy's maximum possible Speed.
- **NOCTUA** (Hoothoot ♂, Lv. 16, `46 HP`, Quiet, `Insomnia`, `Hypnosis`, `Peck`, `Confusion`, `Aerial Ace`) — Died on Turn 3237 in Rustboro Gym `(5, 12)` to School Kid Tammy's `Lv. 15 Rhyhorn` (`Rock Tomb`).
  - **Root Cause & Tactical Rule:** When we switched from `AETHER` to `NOCTUA` against Tammy's `~15% HP` `Lv. 11 Yanma`, we queued `Aerial Ace` for the following turn in the same `run_code` script. Tammy's AI withdrew `15% HP` `Yanma` on the exact same turn we switched and sent in `Lv. 15 Rhyhorn`, causing the pre-queued `Aerial Ace` to keep `NOCTUA` in against `Rhyhorn`'s 2x Super Effective `Rock Tomb`. **Rule:** NEVER queue a switch on Turn N and an attack on Turn N+1 in the same `run_code` script! Trainer AI in this ROM frequently withdraws low-HP or disadvantaged Pokémon on the same turn you switch. Always execute a switch as a standalone turn and inspect `<CurrentScreen>` before selecting your next action.
- **SIREN** (Jigglypuff ♀, Lv. 15, `59 HP`, Modest, `Cute Charm`, `Sing`, `Pound`, `Disable`, `Seismic Toss`) — Died on Turn 3243 in Rustboro Gym `(5, 12)` to School Kid Tammy's final Pokémon, `Lv. 11 Yanma` (`AncientPower`), after chipping `Yanma` down to `6/34 HP` with `Seismic Toss` so `AETHER` could enter on a free switch.
  - **Note on Modified Move Mechanic (Verified Turn 3243):** In this ROM, both `Silver Wind` and `AncientPower` trigger the all-stats-up boost (`+1 Atk/Def/SpA/SpD/Spd`) reliably.
- **AETHER** (Electrike ♂, Lv. 16, `43 HP`, Modest, `Static`, `ThunderShock`, `Thunder Wave`, `Quick Attack`, `Bite`) — Died on Turn 3245 in Rustboro Gym `(5, 12)` to School Kid Tammy's final Pokémon, `Lv. 11 Yanma` (`Silver Wind` at `+2 Attack`).
- **OCEANUS** (Marshtomp ♂, Lv. 16, `49 HP`, Hardy, `Torrent`, `Mud Shot`, `Bubble`, `Mud Sport`, `Water Gun`) — Died on Turn 3247 in Rustboro Gym `(5, 12)` to School Kid Tammy's final Pokémon, `Lv. 11 Yanma` (`Giga Drain` at `+2 SpA` — 4x Super Effective) — **TOTAL PARTY WIPEOUT (Attempt #12 Over)**.
- **Root Causes of Attempt #12 Wipe:**
  1. **Queueing Post-Battle Overworld Inputs in the Same Script as an In-Battle Attack (`THETIS`, Turn 3223):** Queued `BubbleBeam` + post-battle Gym exit + Pokémon Center `A` presses in one script against School Kid Josh's `Lv. 14 Omanyte`. When `Omanyte` survived at `1 HP` and dropped `THETIS` to `6/41 HP` and `-2 Speed` with `Rock Tomb`, the trailing `Up` and `A` presses selected `FIGHT -> BubbleBeam` on the next turn instead of switching out.
  2. **Staying In on a 50/50 Speed Tie (`HERACLES`, Turn 3230):** Won a 50/50 Speed tie (`15 Speed == 15 Speed`) on Turn 1 vs Tammy's lead `Lv. 13 Aron` and stayed in at `17/49 HP` (`< 32` `Aerial Ace` damage), losing the Speed tie on Turn 2.
  3. **Queueing a Switch (Turn N) + Attack (Turn N+1) in a Single Script (`NOCTUA`, Turn 3237):** When switching from `AETHER` to `NOCTUA` against Tammy's `5 HP` `Lv. 11 Yanma`, we queued `Aerial Ace` for Turn N+1 in the same script. Tammy's AI withdrew `5 HP` `Yanma` on the same turn we switched and sent in `Lv. 15 Rhyhorn`, causing the pre-queued `Aerial Ace` to keep `NOCTUA` in against `Rhyhorn`'s `Rock Tomb` (costing us our `Yanma` counter!).
  4. **Allowing `Lv. 11 Yanma` (`Speed Boost`, `Giga Drain`, `Silver Wind`, `AncientPower`) to Set Up Omni-Boosts:** Both `Silver Wind` and `AncientPower` reliably boost all 5 stats (`+1 Atk/Def/SpA/SpD/Spd`) in this ROM, allowing `Yanma` to snowball to `+2` all stats against `SIREN`.
- **Tactical Rules for Attempt #13:**
  1. **Strictly Separate Battle Turns From Overworld Inputs & Switches From Next-Turn Attacks:**
     - NEVER queue post-battle overworld steps or `A` presses in the same `run_code` script as an attack turn.
     - NEVER queue an attack on Turn N+1 in the same `run_code` script as a switch on Turn N (because Trainer AI frequently switches out low-HP Pokémon on the same turn you switch!).
  2. **Verify Speed Strict Inequality Before Staying In at Low HP:** Moving first once only proves `YourSpeed >= EnemySpeed` (which includes a 50/50 Speed tie).
  3. **Evolve `Mudkip -> Lv. 16 Marshtomp` (`Mud Shot` + `Water Gun`) & Bring All 6 Teammates to Level 15–16 Before Rustboro Gym:** Use `Rare Candies` to bring our entire 6-Pokémon party to Level 15–16, preserve our Flying/Fire/Rock/Electric counters for Tammy's `Lv. 11 Yanma`, and never pre-queue moves across switches.

---

## Attempt #13 Wipe Post-Mortem (Turn 3293 — Route 103)
- **Casualties:**
  - **MUDKIP** (Mudkip ♂, Lv. 11, `32 HP`, `Torrent`) — Died on Turn 3293 on Route 103 `(11, 14)` to a wild `Lv. 4 Wingull` (`Wing Attack` critical hit from `8/32 HP`) — **TOTAL PARTY WIPEOUT (Attempt #13 Over)**.
- **Root Causes of Attempt #13 Wipe:**
  1. **Walking Across Tall Grass at Low HP (`8/32 HP`) Without Using Our Overworld `Potion` First:** After fleeing `Lv. 4 Sunkern` at `8/32 HP` on `(12, 14)`, we tried to walk across tall grass `(11, 14)` back to the Oldale Pokémon Center instead of opening the Bag right at `(12, 14)` to use our PC `Potion` (`+20 HP -> 28/32 HP`).
  2. **Queueing `heal_seq` (`Up, A, A, A, A`) in the Same `run_code` Script After Walking Through Tall Grass:** Stepping onto `(11, 14)` triggered two consecutive wild encounters, so `heal_seq` executed inside the second wild battle (`Lv. 4 Wingull`) and selected `FIGHT -> Tackle` at `8/32 HP` instead of `RUN`.
- **Tactical Rules for Attempt #14:**
  1. **Never Queue Pokémon Center `heal_seq` (`Up, A, A, A, A`) in the Same `run_code` Script as Tall-Grass Movement:** Always confirm you have entered the Pokémon Center (or reached grass-free ground) before sending `A` presses.
  2. **Buy 5 Potions Alongside 10 Poké Balls at the Oldale Poké Mart & Heal in Place Before Stepping in Grass:** Always heal to `100% HP` in the overworld immediately after a battle before taking a single step in tall grass.
  3. **Enter Route 103 Grass at `(10, 15)` (1 Step from Grass-Free `(10, 16)`):** Step into `(10, 15)` from `(10, 16)` on Route 103 so that 1 step `Down` returns directly to grass-free `(10, 16)`.

---

## Attempt #14 Casualties (Starting Turn 3294)
- **HERA** (Nidoran♀, Lv. 14, `42 HP`, Bold, `Poison Point`, `Poison Sting`, `Scratch`, `Bite`, `Double Kick`) — Died on Turn 3401 in Petalburg Woods `(23, 35)` to a wild `Lv. 8 Phanpy ♂` (`Mud Shot` — 2x Super Effective + `-1 Speed` drop on Turn 1 [`40 -> 27/42 HP`], followed by a 2x Super Effective + 2x Critical Hit `Mud Shot` [`27 -> 0/42 HP`] on Turn 2 of a pre-queued 2-turn `Double Kick` + `Scratch` sequence; `Phanpy` also had custom ability `Cute Charm`).
  - **Root Cause & Tactical Rule:** Kept a 2x Ground-weak Poison-type (`HERA`) in against a Ground-type (`Lv. 8 Phanpy`) and queued 2 consecutive weakening turns (`Double Kick` + `Scratch`) after seeing `Phanpy` use a weak move on Turn 1. When `Phanpy` used 55-BP STAB `Mud Shot` on Turn 1 of the queued sequence (`13 damage` + `-1 Speed` drop, leaving `HERA` at `27/42 HP` and slower than `Phanpy`), the pre-queued Turn 2 `Scratch` prevented switching out and allowed `Phanpy` to outspeed and land a `27-damage` critical-hit `Mud Shot` on Turn 2 (and the trailing `B` presses selected `No` on `"Use next POKéMON?"`, fleeing the encounter). **Rule:** NEVER keep a 2x type-weak Pokémon in against a wild Pokémon of that offensive type, and NEVER queue 2 turns in a row when weakening a wild encounter! Always execute wild weakening 1 turn at a time with a neutral/resistant Pokémon.
- **SELENE** (Delcatty ♀, Lv. 16, `48 HP`, Lax, `Cute Charm`, `Fake Out`, `Attract`, `Sing`, `Secret Power`) — Died on Turn 3445 in Petalburg Woods `(26, 23)` to Team Magma Grunt's final Pokémon, `Lv. 8 Duskull` (`Will-O-Wisp` burn ticks + `Confuse Ray` + 3 consecutive `Protect`s).
  - **Root Cause & Tactical Lesson:** Kept `SELENE` in to burn `Secret Power` / `Fake Out` PP while `Duskull` was asleep, not knowing `Duskull`'s 4th move was `Will-O-Wisp`. When `Duskull` woke up and inflicted `BRN` (`-6 HP/turn`), `SELENE` was placed on a burn timer and `Duskull` rolled 3 consecutive `Protect`s (`100% * 50% * 25%`) to stall out her remaining burn HP. **Rule:** Team Magma Grunt's `Lv. 8 Duskull` knows **4 moves: `Protect`, `Night Shade`, `Confuse Ray`, and `Will-O-Wisp`** (holds `Leftovers`). Always cure paralysis on `Mudkip` or keep `Mudkip` at high HP (`>25 HP`) entering `Duskull` so `Mudkip` outspeeds `Duskull` (`7 Speed`) and 2HKOs it with `Water Gun` without relying on sleep turns.
- **ATETHYS** (Marshtomp ♀, Lv. 17, `53 HP`, Careful, `Torrent`, `Mud Shot`, `Bubble`, `Mud Sport`, `Water Gun`) — Retired on Turn 3474 on Route 104 North `(24, 8)` after exceeding the Level 16 cap (`Lv. 17`) during the mandatory battle against PKMN Trainer Red — **TOTAL USABLE PARTY WIPEOUT (Attempt #14 Over; 0 usable Pokémon remaining within the Lv. 16 cap)**.
- **Root Causes of Attempt #14 Wipe:**
  1. **Leaving 2x Ground-Weak `HERA` (`Nidoran♀`) In for 2 Queued Turns Against Wild `Lv. 8 Phanpy` (`Mud Shot`):** Queued `Double Kick` + `Scratch` with Poison-type `HERA` against Ground-type `Phanpy`, which used 55-BP STAB `Mud Shot` (`-1 Speed`) on Turn 1 and landed a fatal 2x SE critical hit on Turn 2.
  2. **Stalling PP with `SELENE` (`Delcatty`) Against Team Magma Grunt's `Lv. 8 Duskull` (`Will-O-Wisp` + 3x `Protect`):** Burned `SELENE`'s moves while `Duskull` slept instead of keeping `ATETHYS` healthy/unparalyzed, allowing `Duskull` to wake up, inflict `Will-O-Wisp` burn (`-6 HP/turn`), and roll 3 consecutive `Protect`s to stall out `SELENE`'s burn timer.
  3. **Forced Solo EXP Funneling on Route 104 North (`Winston` + `Haley` + `Red`):** With `HERA` and `SELENE` both fallen and no remaining encounter areas before Rustboro City, `ATETHYS` had to fight Rich Boy Winston (who has a 4-tile sight range up to `y=22`), Lass Haley, and PKMN Trainer Red solo, pushing `ATETHYS` to Level 17 (over the Level 16 cap) with 0 usable teammates remaining.
- **Tactical Rules for Attempt #15:**
  1. **Strictly 1 Turn at a Time When Weakening Wild Encounters & Never Use a 2x Weak Type:** Always chip wild encounters 1 turn at a time with a neutral/resistant Pokémon (`Mudkip`'s 20-BP `Bubble` or `Tackle`).
  2. **Keep 4–5 Active Teammates Alive & at Level 13–14 Across Petalburg Woods and Route 104 North:** Spread trainer EXP across 4–5 teammates (`Mudkip` + Route 103, Route 102, Route 104, and Petalburg Woods catches) so no Pokémon exceeds **Level 15** before entering Rustboro City.
  3. **Against Team Magma Grunt's `Lv. 8 Duskull` (`Protect`, `Night Shade`, `Confuse Ray`, `Will-O-Wisp`):** Attack `Duskull` directly with `Bite` / `Water Gun` / `BubbleBeam` / `Aerial Ace` from a `>25 HP` unparalyzed attacker rather than attempting to PP-stall `Duskull`.

---

## Attempt #15 Casualties (Starting Turn 3475)
- **FLORA** (Hoppip ♀, Lv. 11, `29 HP`, `Grass/Flying`, `Confusion`, `PoisonPowder`, `Mega Drain`, `Gust`) — Died on Turn 3546 on Route 102 `(26, 15)` to Bug Catcher Rick's final Pokémon, `Lv. 5 Kakuna` (`Poison Sting` — 2x Super Effective `7 damage` + end-of-turn `PSN` tick `10 -> 3 -> 0/29 HP` after non-STAB `Confusion` from `12 SpA` left `Kakuna` at `1 HP`).
  - **Root Cause & Tactical Rule:** Kept a poisoned (`PSN`, `10/29 HP`) 2x Poison-weak `Grass/Flying` Pokémon in against `Lv. 5 Kakuna` (`Poison Sting`) expecting non-STAB `Confusion` (`50 BP` from `12 SpA`) to OHKO, instead of switching to our healthy `Ground`-type `TALOS` (`24/32 HP`, `24 Defense`, resists `Poison Sting` `0.5x`) or `NEREUS` (`Water Gun` `60 effective BP` from `18 SpA`). **Rule:** Never leave a poisoned (`PSN`) `<50% HP` Pokémon in against a 2x Super Effective enemy move when a healthy resistant teammate is available on the bench!
- **NEREUS** (Mudkip ♂, Lv. 11, `33 HP`, Sassy, `Torrent`, `Tackle`, `Bubble`, `Mud Sport`, `Water Gun`) — Died on Turn 3575 on Route 102 `(15, 2)` to Lass Tiana's `Lv. 5 Togepi` (`Metronome` -> critical-hit `Smog` `7 -> 1/33 HP` + residual `Leech Seed` sap `1 -> 0/33 HP` from `Sunkern`).
  - **Root Cause & Tactical Rule:** Kept `NEREUS` in while seeded by `Leech Seed` (`-4 HP/turn`) after knocking out `Lv. 6 Sunkern` at `15/33 HP`, instead of immediately pivoting `NEREUS` (`15/33 HP`) -> `TALOS` (`4/32 HP`) -> `NEREUS` (`15/33 HP`) on `Togepi`'s send-out turn to clear `Leech Seed` before attacking.