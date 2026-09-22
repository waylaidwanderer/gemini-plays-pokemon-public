# Scratchpad: Terrestrial Hunting & Trade Planning
## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target PokÃÂ©mon: PSYDUCK (MIGRAINE Lv 24, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 14,067 [Turn 38021]. Psyduck reached Level 24!
  - Milestone Next: Lv 25 = 25^3 = 15,625 EXP (1,558 EXP remaining, ~5 battles).
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (21,870 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 72)

### Active Expedition Sweeper Attrition & Condition Log (Battle 96 Hypno, Turn 38021):
- Trainee: PSYDUCK (MIGRAINE) [Lv 24, Water, Lead Slot]
  - Status: Healthy
  - HP: ~63 / 63
  - EXP: 14,067 (1,558 to Lv 25) [Battle 96: +308 EXP]
  - Stats: Attack 37, Defense 30, Speed 37, Special 37 [Verified Lv 24 Screen Turn 38021]
- Primary Sweeper: BLASTOISE (SHELDON) [Lv 72, Water]
  - HP: 229 / 229
  - Status: Healthy (Poison cured Turn 38045)
  - Active Move PP: Surf (15/15), Ice Beam (10/10), Body Slam (15/15), Double-Edge (15/15)
- Reserve Sweeper: MEWTWO (OMEGA) [Lv 72, Psychic]
  - HP: 249 / 249
  - Status: Healthy
  - Active Move PP: Psychic (10/10), Swift (20/20), Barrier (30/30), Recover (20/20)
- Protocol Trigger Check:
  - Mewtwo HP: 221 (> 60 trigger). Psychic PP: 8 (> 3 trigger).
  - Blastoise HP: 182 (> 60 trigger). Surf PP: 13 (> 3 trigger).
  - Protocol Status: Pit Stop Initiated (Turn 38033). Flying to Cerulean City Pokémon Center to heal Blastoise PSN and deposit Jolteon and Geodude into Box 1 for EXP.ALL Dilution Test (4-member party).

### Cerulean Cave 1F EXP Yield Table (Live Exp. All Yields: Participant + Team Share, 100% Empirically Verified)
| Species | Level | Total Wild EXP | Trainee Total Gain (Part+Team) | DUX Gain (Boosted) | Primary Sweeper Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Raichu** | 53 | 908 | **264 EXP** (227+37) | 55 EXP | Mewtwo (STAB Psychic OHKO) |
| **Venomoth** | 49 | 952 | **273 EXP** (238+35) | 52 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Magneton** | 46 | 1,050 | **301 EXP** (262+39) | 58 EXP | Mewtwo (STAB Psychic OHKO) |
| **Hypno** | 46 | 1,076 | **308 EXP** (269+39) | 58 EXP | Mewtwo (STAB Psychic / Swift) |
| **Golbat** | 46 | 1,104 | **322 EXP** (276+46) | 69 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Sandslash** | 52 | 1,188 | **341 EXP** (297+44) | 66 EXP | Blastoise (STAB Surf 2x SE OHKO) / Mewtwo |
| **Kadabra** | 49 | 1,008 | **294 EXP** (252+42) | 63 EXP | Blastoise (Surf / Body Slam) / Mewtwo |
| **Parasect** | 52 | 950 | **274 EXP** (237+37) | 55 EXP | Blastoise (Ice Beam 2x SE OHKO) |
| **Dodrio** | 49 | 1,092 | **315 EXP** (273+42) | 63 EXP | Mewtwo (STAB Psychic OHKO) |



### Exp. All Empirical Model Audit & Observations Across Battles 1-96
- Mathematical Model Analysis:
  - Participant Share is strictly: floor(floor(E / 2) / n_participants) = floor(E / 4) for 2 participants.
  - Exp. All Base Share (Empirically Observed Range E/24 to E/27):
    - Golbat (E=1104, base=46 = E/24.0) [B1,6-8,12,17,20,29,32,38,40,44,48,55,58,64,66,67,68,81,86,92,93]
    - Kadabra (E=1008, base=42 = E/24.0) [B2,16,25,72]
    - Raichu (E=908, base=37 = E/24.5) [B19,35,53,60,78]
    - Dodrio (E=1092, base=42 = E/26.0) [B3,18,26,30,36,37,59,70,77,85,87]
    - Magneton (E=1050, base=39 = E/26.9) [B13,22,27,31,50,61,62,79,80,95]
    - Sandslash (E=1188, base=44 = E/27.0) [B5,9,10,14,23,56,65,89]
    - Venomoth (E=952, base=35 = E/27.2) [B15,21,28,33,34,52,71,76,83,84]
    - Parasect (E=950, base=37 = E/25.7) [B41,42,46,91,94]
    - Hypno (E=1076, base=39 = E/27.6) [B4,11,24,39,43,45,47,49,51,54,57,63,69,73,74,75,82,88,90,96]
    Division Variance Testable Hypothesis (Gen 1 Assembly Implementation):
    - Context & Phenomenon: Across all battles with a healthy 6-member party, the Exp. All team base share is consistently floor(E / K) where effective divisor K ranges from 24.0 to 27.6:
      - Golbat (E=1104, base=46, K=24.0), Kadabra (E=1008, base=42, K=24.0), Raichu (E=908, base=37, K=24.5)
      - Parasect (E=950, base=37, K=25.7), Dodrio (E=1092, base=42, K=26.0), Magneton (E=1050, base=39, K=26.9)
      - Sandslash (E=1188, base=44, K=27.0), Venomoth (E=952, base=35, K=27.2), Hypno (E=1076, base=39, K=27.6)
    - Mathematical Variable Analysis: In Gen 1 assembly (engine/battle/experience.asm), Exp. All calculates:
      1. `E_half = floor(total_EXP / 2)`
      2. The team share divides `E_half` among non-fainted party members (N=6): `floor(E_half / 6) = floor(floor(total_EXP / 2) / 6) = floor(total_EXP / 12)`.
      3. For the individual participant vs non-participant allocation routine, the engine performs a second division step (e.g. dividing by 2 or by number of participants M): when dividing by 2, `floor(floor(total_EXP / 12) / 2) = floor(total_EXP / 24)`.
      4. Discrepancies where K > 24 (25..27) are hypothesized to stem from species base experience byte scaling routines or intermediate 8-bit division register truncation where high bytes of total EXP are processed separately from low bytes, causing truncation losses proportional to `(total_EXP % 256)`.
    - Testable Prediction: Any species yielding total EXP divisible by 24 with low remainder (e.g. Golbat 1104 / 24 = exactly 46) will yield K=24.0, whereas values with fractional register remainder drop K toward 26-27.
  - Boosted Exp. All Share strictly adheres to Gen 1 integer arithmetic: boosted = base + floor(base / 2) (100% verified across all 83 battles!).

### Psyduck Switch-Training Combat Protocol
- Vulnerability Profile: Psyduck (Water, Lv 15, HP 42, Attack 24, Defense 20, Speed 24, Special 24) has very low stats compared to Lv 46-53 Cerulean Cave wild PokÃÂÃÂ©mon. Any hit will be lethal.
- Turn 1 Rule: NEVER attack with Psyduck. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Sweeper Matchups:
  - Poison / Bug / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu): Switch to Mewtwo (OMEGA Lv 72). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass (Dodrio, Sandslash, Parasect, Ditto, Hypno): Switch to Blastoise (SHELDON Lv 72). High Defense (197) absorbs physical hits; retaliates with STAB Surf / 2x Ice Beam.
- PP Budget & Pit-Stop Protocol:
  - Retreat Triggers: Active sweeper reaching primary SE PP <= 3 (Mewtwo Psychic <= 3 triggers immediate pit stop to restore PP) or HP < 60, or major persistent status (PAR) combined with low PP.

### Other Post-Game Evolution Candidates
1. SLOWPOKE (DOPEY Lv 15, Box 1):
   - Growth Group: Medium Fast (EXP = Level^3)
   - Target EXP: 50,653 EXP (Lv 37 Slowbro #080)
   - Prerequisite Status: Caught, stored in Box 1 [Verified Box 2 empty Turn 37268].
2. In-Game Trades:
   - Route 2 Gatehouse: Trade Abra for Mr. Mime (MARCEL, #122).
     - Prerequisite Status: Wild Abra NOT yet caught (unobtained asset). Needs hunting on Route 24 or Route 8.
   - Route 18 Gatehouse 2F: Trade Slowbro for Lickitung (MARC, #108).
     - Prerequisite Status: Slowpoke owned (Box 1), but not yet evolved into Slowbro (unobtained asset).
3. Evolution Stones:
   - Celadon Dept Store 4F: Water Stone, Fire Stone, Leaf Stone, Thunder Stone purchasable for ÃÂÃÂ¥2,100 each.
   - Current Bag/PC Stones: Moon Stone x1 in PC. Money: ÃÂÃÂ¥3056.

### Testable Hypothesis: Exp. All Party Size Dilution

### EXP.ALL N=4 Party Dilution Testable Predictions (Expedition 9)
- **Setup:** Party reduced to 4 members: Psyduck (Slot 1), Mewtwo (Slot 2), Blastoise (Slot 3), Farfetch'd (Slot 4).
- **Hypothesis A (Dynamic Active Party Divisor N=4):**
  - E_half = floor(total_EXP / 2)
  - Team Share = floor(E_half / 4)
  - Participant Share (Psyduck + Sweeper) = floor(E_half / 2) = floor(total_EXP / 4)
  - Total Psyduck Gain = Participant Share + Team Share
- **Hypothesis B (Hardcoded Engine Divisor N=6):**
  - Team Share remains invariant at floor(E / 24..27) (~35-46 EXP).
- **Pre-Calculated Yields for First Encounter Verification:**
  | Species | Level | Total EXP | Part Share (E/4) | Hyp A Team Share | Hyp A Psyduck Total | Hyp A DUX (Boosted) | Hyp B Team Share | Hyp B Psyduck Total | Hyp B DUX (Boosted) |
  | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
  | **Golbat** | 46 | 1,104 | 276 | **138 EXP** | **414 EXP** | **207 EXP** | 46 EXP | 322 EXP | 69 EXP |
  | **Hypno** | 46 | 1,076 | 269 | **134 EXP** | **403 EXP** | **201 EXP** | 39 EXP | 308 EXP | 58 EXP |
  | **Magneton** | 46 | 1,050 | 262 | **131 EXP** | **393 EXP** | **196 EXP** | 39 EXP | 301 EXP | 58 EXP |
  | **Sandslash**| 52 | 1,188 | 297 | **148 EXP** | **445 EXP** | **222 EXP** | 44 EXP | 341 EXP | 66 EXP |
  | **Kadabra**  | 49 | 1,008 | 252 | **126 EXP** | **378 EXP** | **189 EXP** | 42 EXP | 294 EXP | 63 EXP |
  | **Dodrio**   | 49 | 1,092 | 273 | **136 EXP** | **409 EXP** | **204 EXP** | 42 EXP | 315 EXP | 63 EXP |
  | **Venomoth** | 49 | 952   | 238 | **119 EXP** | **357 EXP** | **178 EXP** | 35 EXP | 273 EXP | 52 EXP |
  | **Raichu**   | 53 | 908   | 227 | **113 EXP** | **340 EXP** | **169 EXP** | 37 EXP | 264 EXP | 55 EXP |
  | **Parasect** | 52 | 950   | 237 | **118 EXP** | **355 EXP** | **177 EXP** | 37 EXP | 274 EXP | 55 EXP |

- **Observation:** All 92 battles have been conducted with a 6-member party, yielding ~40-46 base team share (divisor K ~ 24..27).
- **Hypothesis:** In Gen 1, Exp. All divides the team share half (E_half) by the number of non-fainted party members (N). With N=6, share is E/12 (or E/24 per participant). If the party size is reduced to N=2 (only Psyduck and 1 Sweeper), the team share would be floor(E_half / 2) = floor(E / 4), which would dramatically increase Exp. All gains from ~40 to ~250+ EXP per battle!
- **Test Protocol:** At the next PokÃÂ©mon Center visit, deposit Jolteon, Geodude, and Farfetch'd into the PC, leaving only Psyduck and Mewtwo (or Blastoise). Conduct a test battle in Cerulean Cave 1F and measure the exact Exp. All yield received by Psyduck!

### Expedition 8 Summary (Psyduck Trainee, Battles 93-96):
- Battles 93-96 completed: Golbat (+322 EXP), Parasect (+274 EXP), Magneton (+301 EXP), Hypno (+308 EXP).
- Psyduck achieved Level 24 milestone (14,067 EXP, verified stats: Atk 37, Def 30, Spd 37, Spc 37).
- Remaining to Lv 25 (15,625 EXP): 1,558 EXP (~5 battles with N=6, ~4 battles with N=4).