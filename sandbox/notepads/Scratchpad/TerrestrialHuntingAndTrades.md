# Scratchpad: Terrestrial Hunting & Trade Planning
## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target Pokémon: PSYDUCK (MIGRAINE Lv 28, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 22,250 [Turn 38502]. Psyduck reached Level 28!
  - Milestone Next: Lv 29 = 29^3 = 24,389 EXP (2,139 EXP remaining, ~6-7 battles).
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (13,687 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 73) / Mewtwo (OMEGA Lv 73)

### Active Expedition 11 Sweeper Attrition & Condition Log:
- Trainee: PSYDUCK (MIGRAINE) [Lv 28, Water, Lead Slot]
  - Status: Healthy, HP: 72 / 72 [Verified Screen Turn 38526]
  - EXP: 22,250 (2,139 to Lv 29 milestone at 24,389 EXP)
  - Stats: Attack 43, Defense 35, Speed 43, Special 43 [Verified Lv 28 Screen Turn 38501]
- Primary Sweeper: MEWTWO (OMEGA) [Lv 73, Psychic]
  - Status: Healthy, HP: 254 / 254
  - Stats: Attack 186, Defense 169, Speed 215, Special 254
  - Active Move PP: Psychic (10/10), Swift (20/20), Barrier (30/30), Recover (20/20)
  - Protocol Trigger Check: Mewtwo Psychic PP = 10 (Full PP / Green).
- Secondary Sweeper: BLASTOISE (SHELDON) [Lv 73, Water]
  - Status: Healthy, HP: 233 / 233
  - Stats: Attack 174, Defense 201, Speed 173, Special 180 [Verified Lv 73 Screen Turn 38238]
  - Active Move PP: Surf (15/15), Ice Beam (10/10), Body Slam (15/15), Double-Edge (15/15)
  - Protocol Trigger Check: Blastoise HP = 233, Surf PP = 15. Status: Full PP / Green.
- Support / Flyer: FARFETCH'D (DUX) [Lv 20, Boosted EXP]
  - Status: Healthy, HP: 54 / 54 [Verified Screen Turn 38526]


### EXP.ALL N=4 Party Dilution Model & Predictions (Expedition 10)
- **Setup:** 4-member party: Psyduck (Slot 1), Mewtwo (Slot 2), Blastoise (Slot 3), Farfetch'd (Slot 4).
- **Disproven Continuous Formulas & 65 EXP Plateau:** While Sandslash (1188) yields 74 EXP (matching floor(1188/16)), strict floor(E/16) is definitively FALSIFIED by Golbat (observed 65 vs 69 predicted), Hypno (observed 65 vs 67 predicted), and Dodrio (observed 63 vs 68 predicted). Similarly, a continuous 65 EXP plateau is disproven by Dodrio's 63 EXP. Discrete assembly division routines and truncation determine each species yield independently without a single global closed-form equation.
  - Effective divisor K scales from ~24..27 (N=6) down to ~16..17 (N=4), proportional to party size reduction.
  - Participant Share (Psyduck + Sweeper) = floor(E_half / 2) = floor(total_EXP / 4).
  - Traded Pokémon Boost: boosted = base + floor(base / 2) (e.g. 65 + 32 = 97 EXP; 56 + 28 = 84 EXP).
- **N=4 Yield Table:**
| Species | Level | Total EXP | Part Share (E/4) | Team Share (N=4) | Trainee Gain (Part+Team) | DUX Gain (Boosted) | Verification Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Golbat** | 46 | 1,104 | 276 | **65 EXP** | **341 EXP** | **97 EXP** | Verified (B100, B102, B104, B113, B114, B118, B119) |
| **Hypno** | 46 | 1,076 | 269 | **65 EXP** | **334 EXP** | **97 EXP** | Verified (B98, B103, B117, B121) |
| **Magneton** | 46 | 1,050 | 262 | **65 EXP** | **327 EXP** | **97 EXP** | Verified (B97, B101, B108, B109, B112, B115) |
| **Dodrio** | 49 | 1,092 | 273 | **63 EXP** | **336 EXP** | **94 EXP** | Verified (B111) |
| **Sandslash**| 52 | 1,188 | 297 | **74 EXP** | **371 EXP** | **111 EXP** | Verified (B120) |
| **Kadabra** | 49 | 1,008 | 252 | **63 EXP** | **315 EXP** | **94 EXP** | Verified (B107) |
| **Venomoth** | 49 | 952 | 238 | **56 EXP** | **294 EXP** | **84 EXP** | Verified (B99, B110) |
| **Raichu** | 53 | 908 | 227 | **Pending** | Pending | Pending | Pending Empirical Encounter |
| **Ditto** | 53 | ~763 | ~190 | **Pending** | Pending | Pending | Pending Empirical Encounter |
| **Parasect** | 52 | 950 | 237 | **59 EXP** | **296 EXP** | **88 EXP** | Verified (B105, B106, B116) |

### Psyduck Switch-Training Combat Protocol
- Vulnerability Profile: Psyduck has low defense compared to Lv 46-53 Cerulean Cave wild Pokémon. Any direct hit is lethal.
- Turn 1 Rule: NEVER attack with Psyduck. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Sweeper Matchups:
  - Poison / Bug / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu): Switch to Mewtwo (OMEGA Lv 73). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass & Low-Defense Targets (Dodrio, Sandslash, Parasect, Ditto, Hypno [Psychic, Def 70]): Switch to Blastoise (SHELDON Lv 73). High Defense (201) absorbs physical hits; retaliates with STAB Surf / Ice Beam.
- Retreat Protocol: Trigger pit-stop when Mewtwo Psychic PP <= 3 or HP < 60, or Blastoise HP < 60 / Surf PP <= 3.

### Other Post-Game Evolution Candidates
1. SLOWPOKE (DOPEY Lv 15, Box 1): Medium Fast, target 50,653 EXP (Lv 37 Slowbro #080).
2. In-Game Trades: Route 2 Gatehouse (Abra -> Mr. Mime #122); Route 18 Gatehouse 2F (Slowbro -> Lickitung #108).
3. Evolution Stones: Celadon Dept Store 4F (Water, Fire, Leaf, Thunder ¥2,100 each). Money: ¥3056.
