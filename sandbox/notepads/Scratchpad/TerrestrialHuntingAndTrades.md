# Scratchpad: Terrestrial Hunting & Trade Planning
## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target Pokémon: PSYDUCK (MIGRAINE Lv 29, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 26,224 [Turn 38838].
  - Milestone Next: Lv 30 = 30^3 = 27,000 EXP (776 EXP remaining, ~2-3 battles).
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (9,713 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 73) / Mewtwo (OMEGA Lv 73)

### Expedition 12 Systematic Encounter Log (N=4)
| Battle | Turn | Opponent | Sweeper | Sweeper Damage Taken | Sweeper End HP / PP | Trainee Gain | DUX Gain | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B132** | 38806 | Magneton Lv 46 | Mewtwo (Psychic) | 8 (took 8 dmg on switch) | Mewtwo 246/254 HP, 9/10 PP | +327 EXP (262+65) | +97 EXP | OHKO with Psychic. |
| **B133** | 38818 | Venomoth Lv 49 | Mewtwo (Flute/Psychic) | 0 (woke via Flute; Stun Spore failed) | Mewtwo 246/254 HP, 8/10 PP | +294 EXP (238+56) | +84 EXP | OHKO with Psychic after Poké Flute wakeup. |

### Active Expedition 12 Sweeper Attrition & Condition Log:
- Primary Sweeper: MEWTWO (OMEGA) [Lv 73, Psychic]
  - Status: Healthy, HP: 246 / 254 [Verified Screen Turn 38838]
  - Stats: Attack 186, Defense 169, Speed 215, Special 254
  - Active Move PP: Psychic (8/10), Swift (20/20), Barrier (30/30), Recover (20/20)
  - Protocol Trigger Check: Mewtwo Psychic PP = 8 (Green).
- Secondary Sweeper: BLASTOISE (SHELDON) [Lv 73, Water]
  - Status: Healthy, HP: 233 / 233 [Healed Turn 38768]
  - Stats: Attack 174, Defense 201, Speed 173, Special 180
  - Active Move PP: Surf (15/15), Ice Beam (10/10), Body Slam (15/15), Double-Edge (15/15)
  - Protocol Trigger Check: Blastoise HP = 233, Surf PP = 15 (Green).
- Support / Flyer: FARFETCH'D (DUX) [Lv 21, Boosted EXP]
  - Status: Healthy, HP: 56 / 56 [Verified Lv 21 Screen Turn 38757]


### EXP.ALL N=4 Party Dilution Model & Verified Yields
- **Setup:** 4-member party: Psyduck (Slot 1), Mewtwo (Slot 2), Blastoise (Slot 3), Farfetch'd (Slot 4).
- **Disproven Continuous Formulas & 65 EXP Plateau:** While Sandslash (1188) yields 74 EXP (matching floor(1188/16)), strict floor(E/16) is definitively FALSIFIED by Golbat (observed 65 vs 69 predicted), Hypno (observed 65 vs 67 predicted), and Dodrio (observed 63 vs 68 predicted). Similarly, a continuous 65 EXP plateau is disproven by Dodrio's 63 EXP. Discrete assembly division routines and truncation determine each species yield independently without a single global closed-form equation.
  - Effective divisor K scales from ~24..27 (N=6) down to ~16..17 (N=4), proportional to party size reduction.
  - Participant Share (Psyduck + Sweeper) = floor(E_half / 2) = floor(total_EXP / 4).
  - Traded Pokémon Boost: boosted = base + floor(base / 2) (e.g. 65 + 32 = 97 EXP; 56 + 28 = 84 EXP).
- **N=4 Yield Table:**
| Species | Level | Total EXP | Part Share (E/4) | Team Share (N=4) | Trainee Gain (Part+Team) | DUX Gain (Boosted) | Verification Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Golbat** | 46 | 1,104 | 276 | **65 EXP** | **341 EXP** | **97 EXP** | Verified (B100, B102, B104, B113, B114, B118, B119, B126, B127, B129, B130) |
| **Hypno** | 46 | 1,076 | 269 | **65 EXP** | **334 EXP** | **97 EXP** | Verified (B98, B103, B117, B121, B125) |
| **Magneton** | 46 | 1,050 | 262 | **65 EXP** | **327 EXP** | **97 EXP** | Verified (B97, B101, B108, B109, B112, B115, B128, B131, B132) |
| **Dodrio** | 49 | 1,092 | 273 | **63 EXP** | **336 EXP** | **94 EXP** | Verified (B111, B124) |
| **Sandslash**| 52 | 1,188 | 297 | **74 EXP** | **371 EXP** | **111 EXP** | Verified (B120, B123) |
| **Kadabra** | 49 | 1,008 | 252 | **63 EXP** | **315 EXP** | **94 EXP** | Verified (B107) |
| **Venomoth** | 49 | 952 | 238 | **56 EXP** | **294 EXP** | **84 EXP** | Verified (B99, B110, B122, B133) |
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
