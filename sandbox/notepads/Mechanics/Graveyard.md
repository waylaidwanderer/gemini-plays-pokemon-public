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