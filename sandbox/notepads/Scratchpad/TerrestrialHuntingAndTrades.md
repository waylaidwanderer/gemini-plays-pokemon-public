# Scratchpad: Terrestrial Hunting & Trade Planning
## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target Pokémon: PSYDUCK (MIGRAINE Lv 26, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 18,561 [Turn 38339]. Psyduck at Level 26.
  - Milestone Next: Lv 27 = 27^3 = 19,683 EXP (1,122 EXP remaining, ~3 battles).
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (17,376 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 73) / Mewtwo (OMEGA Lv 73)

### Active Expedition 10 Sweeper Attrition & Condition Log:
- Trainee: PSYDUCK (MIGRAINE) [Lv 26, Water, Lead Slot]
  - Status: Healthy, HP: 67 / 67 [Verified Lv 26 Screen Turn 38240]
  - EXP: 18,561 (1,122 to Lv 27 milestone at 19,683 EXP)
  - Stats: Attack 40, Defense 32, Speed 40, Special 40 [Verified Lv 26 Screen Turn 38240]
- Primary Sweeper: MEWTWO (OMEGA) [Lv 73, Psychic]
  - Status: Healthy, HP: 246 / 254
  - Stats: Attack 186, Defense 169, Speed 215, Special 254
  - Active Move PP: Psychic (8/10), Swift (20/20), Barrier (30/30), Recover (20/20)
  - Protocol Trigger Check: Mewtwo Psychic PP = 8. Status: Full PP / Green.
- Secondary Sweeper: BLASTOISE (SHELDON) [Lv 73, Water]
  - Status: Healthy, HP: 233 / 233 [Fully Restored Nurse Joy Turn 38287]
  - Stats: Attack 174, Defense 201, Speed 173, Special 180 [Verified Lv 73 Screen Turn 38238]
  - Active Move PP: Surf (15/15), Ice Beam (10/10), Body Slam (15/15), Double-Edge (15/15)
  - Protocol Trigger Check: Blastoise HP = 233, Surf PP = 15. Status: Full PP / Green.
- Support / Flyer: FARFETCH'D (DUX) [Lv 19, Boosted EXP]
  - Status: Healthy, HP: 52 / 52 [Verified Screen Turn 38300]


### EXP.ALL N=4 Party Dilution Model & Predictions (Expedition 9)
- **Setup:** 4-member party: Psyduck (Slot 1), Mewtwo (Slot 2), Blastoise (Slot 3), Farfetch'd (Slot 4).
- **65 EXP Plateau Phenomenon:** Encounters with total EXP between 1,050 and 1,104 all yield exactly 65 team base share (Magneton E=1050 -> 65; Hypno E=1076 -> 65; Golbat E=1104 -> 65).
  - Effective divisor K scales from ~24..27 (N=6) down to ~16..17 (N=4), proportional to party size reduction.
  - Participant Share (Psyduck + Sweeper) = floor(E_half / 2) = floor(total_EXP / 4).
  - Traded Pokémon Boost: boosted = base + floor(base / 2) (e.g. 65 + 32 = 97 EXP; 56 + 28 = 84 EXP).
- **N=4 Yield Table:**
| Species | Level | Total EXP | Part Share (E/4) | Team Share (N=4) | Trainee Gain (Part+Team) | DUX Gain (Boosted) | Verification Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Golbat** | 46 | 1,104 | 276 | **65 EXP** | **341 EXP** | **97 EXP** | Verified (B100, B102, B104) |
| **Hypno** | 46 | 1,076 | 269 | **65 EXP** | **334 EXP** | **97 EXP** | Verified (B98, B103) |
| **Magneton** | 46 | 1,050 | 262 | **65 EXP** | **327 EXP** | **97 EXP** | Verified (B97, B101) |
| **Dodrio** | 49 | 1,092 | 273 | **65 EXP** | **338 EXP** | **97 EXP** | Predicted (65 EXP Plateau) |
| **Sandslash**| 52 | 1,188 | 297 | **Pending** | Pending | Pending | Pending Empirical Encounter |
| **Kadabra** | 49 | 1,008 | 252 | **63 EXP** | **315 EXP** | **94 EXP** | Verified (B107) |
| **Venomoth** | 49 | 952 | 238 | **56 EXP** | **294 EXP** | **84 EXP** | Verified (B99) |
| **Raichu** | 53 | 908 | 227 | **Pending** | Pending | Pending | Pending Empirical Encounter |
| **Parasect** | 52 | 950 | 237 | **59 EXP** | **296 EXP** | **88 EXP** | Verified (B105) |

### Expedition 9 Battle Log (Compact Summary, Battles 97-108):
| Battle | Opponent | Sweeper Used | Key Events | Part Share | Team Share (N=4) | Trainee Total | Psyduck EXP End |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B97** | Magneton Lv 46 | Mewtwo (Psychic) | Took 8 dmg; OHKO | 262 EXP | 65 EXP (DUX 97) | +327 EXP | 14,394 |
| **B98** | Hypno Lv 46 | Blastoise (Surf/Ice) | Took 40 dmg; 2-hit KO | 269 EXP | 65 EXP (DUX 97) | +334 EXP | 14,728 |
| **B99** | Venomoth Lv 49 | Mewtwo (Psychic) | Poké Flute woke sleep; OHKO; Mewtwo Lv 73 | 238 EXP | 56 EXP (DUX 84) | +294 EXP | 15,022 |
| **B100**| Golbat Lv 46 | Mewtwo (Psychic) | 0 dmg taken; OHKO | 276 EXP | 65 EXP (DUX 97) | +341 EXP | 15,363 |
| **B101**| Magneton Lv 46 | Mewtwo (Psychic) | Confused by Supersonic; OHKO; **Psyduck Lv 25** | 262 EXP | 65 EXP (DUX 97) | +327 EXP | 15,690 |
| **B102**| Golbat Lv 46 | Mewtwo (Psychic) | 0 dmg taken; OHKO | 276 EXP | 65 EXP (DUX 97) | +341 EXP | 16,031 |
| **B103**| Hypno Lv 46 | Blastoise (Surf x2) | Blastoise took 52 dmg (crit); 2-hit Surf KO | 269 EXP | 65 EXP (DUX 97) | +334 EXP | 16,365 |
| **B104**| Golbat Lv 46 | Mewtwo (Psychic) | Golbat move failed; OHKO with Psychic (PP 4/10) | 276 EXP | 65 EXP (DUX 97) | +341 EXP | 16,706 |
| **B105**| Parasect Lv 52 | Blastoise (Ice Beam) | Blastoise took 34 dmg on switch; OHKO with Ice Beam | 237 EXP | 59 EXP (DUX 88) | +296 EXP | 17,002 |
| **B106**| Parasect Lv 52 | Blastoise (Ice Beam) | Blastoise took 7 dmg on switch; OHKO with Ice Beam | 237 EXP | 59 EXP (DUX 88) | +296 EXP | 17,298 |
| **B107**| Kadabra Lv 49 | Blastoise (Surf) | Kadabra used Reflect; OHKO with Surf; **Psyduck Lv 26**, **Sheldon Lv 73** | 252 EXP | 63 EXP (DUX 94) | +315 EXP | 17,613 |
| **B108**| Magneton Lv 46 | Mewtwo (Psychic) | Mewtwo confused, snapped out; OHKO with Psychic (PP 3/10); **Retreat Trigger** | 262 EXP | 65 EXP (DUX 97) | +327 EXP | 17,940 |

### Expedition 10 Battle Log (Battles 109+):
| Battle | Opponent | Sweeper Used | Key Events | Part Share | Team Share (N=4) | Trainee Total | Psyduck EXP End |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B109**| Magneton Lv 46 | Mewtwo (Psychic) | Took 8 dmg on switch; OHKO with Psychic (PP 9/10) | 262 EXP | 65 EXP (DUX 97) | +327 EXP | 18,267 |
| **B110**| Venomoth Lv 49 | Mewtwo (Psychic) | Took 0 dmg on switch; OHKO with Psychic (PP 8/10) | 238 EXP | 56 EXP (DUX 84) | +294 EXP | 18,561 |

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
