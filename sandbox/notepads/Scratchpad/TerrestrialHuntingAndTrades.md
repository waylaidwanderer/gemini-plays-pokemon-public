# Scratchpad: Terrestrial Hunting & Trade Planning
## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target Pokémon: PSYDUCK (MIGRAINE Lv 26, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 19,906 [Turn 38396]. Psyduck at Level 27.
  - Milestone Next: Lv 28 = 28^3 = 21,952 EXP (2,046 EXP remaining, ~6 battles).
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (16,031 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 73) / Mewtwo (OMEGA Lv 73)

### Active Expedition 10 Sweeper Attrition & Condition Log:
- Trainee: PSYDUCK (MIGRAINE) [Lv 27, Water, Lead Slot]
  - Status: Healthy, HP: 67 / 67 [Verified Lv 26 Screen Turn 38240]
  - EXP: 19,906 (2,046 to Lv 28 milestone at 21,952 EXP)
  - Stats: Attack 42, Defense 34, Speed 42, Special 41 [Verified Lv 27 Screen Turn 38394]
- Primary Sweeper: MEWTWO (OMEGA) [Lv 73, Psychic]
  - Status: Healthy, HP: 227 / 254
  - Stats: Attack 186, Defense 169, Speed 215, Special 254
  - Active Move PP: Psychic (5/10), Swift (20/20), Barrier (30/30), Recover (20/20)
  - Protocol Trigger Check: Mewtwo Psychic PP = 5. Status: Full PP / Green.
- Secondary Sweeper: BLASTOISE (SHELDON) [Lv 73, Water]
  - Status: Healthy, HP: 221 / 233
  - Stats: Attack 174, Defense 201, Speed 173, Special 180 [Verified Lv 73 Screen Turn 38238]
  - Active Move PP: Surf (14/15), Ice Beam (10/10), Body Slam (15/15), Double-Edge (15/15)
  - Protocol Trigger Check: Blastoise HP = 221, Surf PP = 14. Status: Full PP / Green.
- Support / Flyer: FARFETCH'D (DUX) [Lv 19, Boosted EXP]
  - Status: Healthy, HP: 52 / 52 [Verified Screen Turn 38300]


### EXP.ALL N=4 Party Dilution Model & Predictions (Expedition 9)
- **Setup:** 4-member party: Psyduck (Slot 1), Mewtwo (Slot 2), Blastoise (Slot 3), Farfetch'd (Slot 4).
- **Disproven 65 EXP Plateau:** While Magneton (1050), Hypno (1076), and Golbat (1104) yield 65 EXP, Dodrio (1092) yielded 63 EXP in Battle 111, disproving a continuous monotonic plateau for 1050-1104. Discrete internal truncation and assembly division determine each species yield independently.
  - Effective divisor K scales from ~24..27 (N=6) down to ~16..17 (N=4), proportional to party size reduction.
  - Participant Share (Psyduck + Sweeper) = floor(E_half / 2) = floor(total_EXP / 4).
  - Traded Pokémon Boost: boosted = base + floor(base / 2) (e.g. 65 + 32 = 97 EXP; 56 + 28 = 84 EXP).
- **N=4 Yield Table:**
| Species | Level | Total EXP | Part Share (E/4) | Team Share (N=4) | Trainee Gain (Part+Team) | DUX Gain (Boosted) | Verification Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Golbat** | 46 | 1,104 | 276 | **65 EXP** | **341 EXP** | **97 EXP** | Verified (B100, B102, B104) |
| **Hypno** | 46 | 1,076 | 269 | **65 EXP** | **334 EXP** | **97 EXP** | Verified (B98, B103) |
| **Magneton** | 46 | 1,050 | 262 | **65 EXP** | **327 EXP** | **97 EXP** | Verified (B97, B101) |
| **Dodrio** | 49 | 1,092 | 273 | **63 EXP** | **336 EXP** | **94 EXP** | Verified (B111) |
| **Sandslash**| 52 | 1,188 | 297 | **Pending** | Pending | Pending | Pending Empirical Encounter |
| **Kadabra** | 49 | 1,008 | 252 | **63 EXP** | **315 EXP** | **94 EXP** | Verified (B107) |
| **Venomoth** | 49 | 952 | 238 | **56 EXP** | **294 EXP** | **84 EXP** | Verified (B99) |
| **Raichu** | 53 | 908 | 227 | **Pending** | Pending | Pending | Pending Empirical Encounter |
| **Parasect** | 52 | 950 | 237 | **59 EXP** | **296 EXP** | **88 EXP** | Verified (B105) |

### Expedition 10 Battle Log (Battles 109+):
| Battle | Opponent | Sweeper Used | Key Events | Part Share | Team Share (N=4) | Trainee Total | Psyduck EXP End |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B109**| Magneton Lv 46 | Mewtwo (Psychic) | Took 8 dmg on switch; OHKO with Psychic (PP 9/10) | 262 EXP | 65 EXP (DUX 97) | +327 EXP | 18,267 |
| **B110**| Venomoth Lv 49 | Mewtwo (Psychic) | Took 0 dmg on switch; OHKO with Psychic (PP 8/10) | 238 EXP | 56 EXP (DUX 84) | +294 EXP | 18,561 |
| **B111**| Dodrio Lv 49 | Blastoise (Surf) | Took 12 dmg (Fury Attack); OHKO with Surf (PP 14/15) | 273 EXP | 63 EXP (DUX 94) | +336 EXP | 18,897 |
| **B112**| Magneton Lv 46 | Mewtwo (Psychic) | Took 19 dmg (crit); OHKO with Psychic (PP 7/10) | 262 EXP | 65 EXP (DUX 97) | +327 EXP | 19,224 |
| **B113**| Golbat Lv 46 | Mewtwo (Psychic) | Confused on switch; OHKO with Psychic through confusion (PP 6/10) | 276 EXP | 65 EXP (DUX 97) | +341 EXP | 19,565 |
| **B114**| Golbat Lv 46 | Mewtwo (Psychic) | Took 0 dmg on switch; OHKO with Psychic (PP 5/10); **Psyduck grew to Lv 27!** | 276 EXP | 65 EXP (DUX 97) | +341 EXP | 19,906 |

### Psyduck Switch-Training Combat Protocol
- Vulnerability Profile: Psyduck has low defense compared to Lv 46-53 Cerulean Cave wild Pokémon. Any direct hit is lethal.
- Turn 1 Rule: NEVER attack with Psyduck. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Sweeper Matchups:
  - Poison / Bug / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu): Switch to Mewtwo (OMEGA Lv 73). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass (Dodrio, Sandslash, Parasect, Ditto, Hypno): Switch to Blastoise (SHELDON Lv 72). High Defense (197) absorbs physical hits; retaliates with STAB Surf / Ice Beam.
- Retreat Protocol: Trigger pit-stop when Mewtwo Psychic PP <= 3 or HP < 60, or Blastoise HP < 60 / Surf PP <= 3.

### Other Post-Game Evolution Candidates
1. SLOWPOKE (DOPEY Lv 15, Box 1): Medium Fast, target 50,653 EXP (Lv 37 Slowbro #080).
2. In-Game Trades: Route 2 Gatehouse (Abra -> Mr. Mime #122); Route 18 Gatehouse 2F (Slowbro -> Lickitung #108).
3. Evolution Stones: Celadon Dept Store 4F (Water, Fire, Leaf, Thunder ¥2,100 each). Money: ¥3056.
