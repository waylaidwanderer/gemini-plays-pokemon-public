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