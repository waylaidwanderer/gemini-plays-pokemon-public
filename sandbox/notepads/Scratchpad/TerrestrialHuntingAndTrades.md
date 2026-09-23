# Scratchpad: Terrestrial Hunting & Trade Planning
## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target Pokémon: PSYDUCK (MIGRAINE Lv 25, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 17,002 [Turn 38207]. Psyduck at Level 25.
  - Milestone Next: Lv 26 = 26^3 = 17,576 EXP (574 EXP remaining, ~2 battles).
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (18,935 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 73)

### Active Expedition 9 Sweeper Attrition & Condition Log (Turn 38193, Battle 104 Golbat):
- Trainee: PSYDUCK (MIGRAINE) [Lv 25, Water, Lead Slot]
  - Status: Healthy, HP: 65 / 65
  - EXP: 17,002 (574 to Lv 26 milestone at 17,576 EXP)
  - Stats: Attack 39, Defense 31, Speed 39, Special 39
- Primary Sweeper: MEWTWO (OMEGA) [Lv 73, Psychic]
  - Status: Healthy, HP: 246 / 254
  - Stats: Attack 186, Defense 169, Speed 215, Special 254
  - Active Move PP: Psychic (4/10) [Updated Live Turn 38193], Swift (20/20), Barrier (30/30), Recover (20/20)
  - Protocol Trigger Check: Mewtwo Psychic PP = 4. Retreat trigger is <= 3 (1 Psychic remaining before pit-stop trigger).
- Secondary Sweeper: BLASTOISE (SHELDON) [Lv 72, Water]
  - Status: Healthy, HP: 103 / 229
  - Stats: Attack 171, Defense 197, Speed 171, Special 177
  - Active Move PP: Surf (12/15), Ice Beam (8/10), Body Slam (15/15), Double-Edge (15/15)
  - Protocol Trigger Check: Blastoise HP = 103 (> 60), Surf PP = 12 (> 3).
- Support / Flyer: FARFETCH'D (DUX) [Lv 18, Boosted EXP]
  - Status: Healthy, HP: 49 / 49
- Protocol Status: Green / Healthy (1 Psychic remaining before retreat trigger).

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
| **Sandslash**| 52 | 1,188 | 297 | **74 EXP** | **371 EXP** | **111 EXP** | Predicted |
| **Kadabra** | 49 | 1,008 | 252 | **63 EXP** | **315 EXP** | **94 EXP** | Predicted |
| **Venomoth** | 49 | 952 | 238 | **56 EXP** | **294 EXP** | **84 EXP** | Verified (B99) |
| **Raichu** | 53 | 908 | 227 | **56 EXP** | **283 EXP** | **84 EXP** | Predicted |
| **Parasect** | 52 | 950 | 237 | **59 EXP** | **296 EXP** | **88 EXP** | Verified (B105) |

### Expedition 9 Battle Log (Compact Summary, Battles 97-104):
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

### Psyduck Switch-Training Combat Protocol
- Vulnerability Profile: Psyduck has low defense compared to Lv 46-53 Cerulean Cave wild Pokémon. Any direct hit is lethal.
- Turn 1 Rule: NEVER attack with Psyduck. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Sweeper Matchups:
  - Poison / Bug / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu): Switch to Mewtwo (OMEGA Lv 73). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass (Dodrio, Sandslash, Parasect, Ditto, Hypno): Switch to Blastoise (SHELDON Lv 72). High Defense (197) absorbs physical hits; retaliates with STAB Surf / Ice Beam.
- Retreat Protocol: Trigger pit-stop when Mewtwo Psychic PP <= 3 (currently 4/10, 1 battle remaining) or HP < 60, or Blastoise HP < 60 / Surf PP <= 3.

### Other Post-Game Evolution Candidates
1. SLOWPOKE (DOPEY Lv 15, Box 1): Medium Fast, target 50,653 EXP (Lv 37 Slowbro #080).
2. In-Game Trades: Route 2 Gatehouse (Abra -> Mr. Mime #122); Route 18 Gatehouse 2F (Slowbro -> Lickitung #108).
3. Evolution Stones: Celadon Dept Store 4F (Water, Fire, Leaf, Thunder ¥2,100 each). Money: ¥3056.
