# Boss Battle Tracker — Gym Leader Bastion (Catsear City Gym)

## Opponent Team (2 Pokémon)
1. **Boomboom — Lv9** (`Fire / Steel` confirmed!, **DEFEATED Round 21 — `83` EXP**)
   - **Confirmed Typing Proof:** Immune (`0x`) to Poison (`Acid`), resists Bug (`Struggle Bug`), neutral (`1.0x`) to Fire (`Ember`).
   - **Observed Moves:** `Ember`, `Magnet Bomb`, confusion status move (`Confuse Ray` / `Supersonic`).
   - **AI Discovery (Round 13):** `Monomyth` AI automatically switches out a Pokémon at `-3 Accuracy` to clear accuracy drops! Remember on Round 1 Bastion hard-switched `Boomboom` Lv9 out against `Seraph` Lv11 — using `Fresh Water` on `Seraph` (`13 -> 33/33` HP) right now covers BOTH a `Numel` switch-in and a `Boomboom` stay-in!
2. **Numel (♂) — Lv12** (`Fire / Ground`, `~88%` HP, **ON BENCH** — accuracy reset to `0` on switch-out)
   - **Observed Moves & Remaining PP:**
     - `Magnitude` (Ground, Physical — `27 / 30` PP; used Rounds 2 & 5 into `Athena` for `0` dmg, Round 8 `Magnitude 8` KO'd `Electra`)
     - `Incinerate` (Fire, Special, destroys Berries — `10 / 15` PP; dealt `20` dmg to `Athena` on Rounds 3 & 10, `10` crit / `7` normal dmg to `Seraph` on Rounds 4 & 7, KO'd `Demeter` on Round 9)
     - `Tackle` (Normal, Physical — `34 / 35` PP; dealt `8` dmg to `Athena` on Round 6)
   - **Next Tactical Sequence:** `Athena` (`5/25` HP) goes for `Sand Attack` #3 (`40%` dodge -> `-3` Accuracy!); when `Athena` goes down, `Psyche` (`25/25` HP) enters FREE for `String Shot` (`-2 Speed`) + `Struggle Bug` (`-1 SpA`), backed by `Anansi` (`25/25` HP, `String Shot` / `Infestation`) and `Seraph` (`16/33` HP + `1x Fresh Water` reserved!).

## Master Blueprint for Attempt #2 (100% Checkmate)
1. **Why Attempt #1 Fell Short:**
   - Stacking `-3 Accuracy` (`Sand Attack` x3) on `Numel` *while `Boomboom` Lv9 was still alive* allowed `Monomyth` AI to hard-switch `Numel` out on Round 13 and reset all 3 accuracy drops for free!
   - Additionally, `Boomboom`'s confusion caused 3 consecutive self-hits on `Seraph`, burning all 28 HP of healing.
2. **Attempt #2 Winning Macro-Order — KO `Boomboom` Lv9 FIRST!**
   - First, defeat the remaining **3rd Kindler at `(12, 8)`** in Catsear Gym (`+¥140–160` for `Potion`s + levels **`Athena` to Lv8**!).
   - **Lead with `Psyche` Lv8** (NOT `Seraph`!) against Bastion:
     - Because `Boomboom` Lv9 (`Fire / Steel`) sees `Bug / Psychic` `Psyche`, Bastion **stays in with `Boomboom` Lv9** on Turn 1!
     - Turn 1: `Psyche` uses **`String Shot`** (`Boomboom` -> `-2 Speed`), eating `Ember` (`~20` dmg, surviving at ~`5/25` HP!).
     - Turn 2: Pivot `Psyche` -> **`Seraph` Lv11** (equip **`Cheri Berry`** or swap briefly if confused!) and **KO `Boomboom` Lv9 FIRST** with STAB `Ember`!
   - **Phase 2 (`Numel` Lv12 Enters LAST — CANNOT SWITCH OUT EVER!):**
     - With `Boomboom` Lv9 already fainted, `Numel` Lv12 is **locked on the field permanently** and can NEVER clear stat drops!
     - Pivot `Seraph` -> **`Athena` Lv8** on `Magnitude` (`0` dmg!), stack **`Sand Attack` x2–3 (`-2` to `-3` Accuracy PERMANENTLY!)**, then use `Psyche` / `Electra` (`String Shot` `-2 Speed` PERMANENTLY!) + `Demeter` (`GrassWhistle` + `Ingrain` + `Absorb`) + `Anansi` (`Infestation` `1/8` HP/turn) + `Seraph` (`Constrict`) to sweep!
