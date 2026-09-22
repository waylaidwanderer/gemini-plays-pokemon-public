# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target Pok�mon: PSYDUCK (MIGRAINE Lv 20, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 9,503 [Turn 37696]. Psyduck reached Level 21!
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (26,434 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 72)

### Active Expedition Sweeper Attrition & Condition Log (Post-Battle 76, Turn 37623):
- Trainee: PSYDUCK (MIGRAINE) [Lv 21, Water, Lead Slot]
  - Status: Healthy [Level Up Turn 37696]
  - HP: 54 / 54 [Empirically Verified Turn 37632 Battle Screen]
  - EXP: 9,503 (1,145 to Lv 22) [Level 21 Achieved!]
  - Stats: Attack 33, Defense 27, Speed 33, Special 32 [Empirically Verified Lv 21 Turn 37696 Screen]
- Primary Sweeper: BLASTOISE (SHELDON) [Lv 72, Water]
  - HP: 155 / 229 [Battle 75]
  - Status: Poisoned (PSN, Battle 82)
  - Active Move PP: Surf (12/15), Ice Beam (10/10), Body Slam (15/15), Double-Edge (15/15)
- Reserve Sweeper: MEWTWO (OMEGA) [Lv 72, Psychic]
  - HP: 101 / 249 [Battle 77 Dodrio crit]
  - Status: Healthy
  - Active Move PP: Psychic (4/10), Swift (20/20), Barrier (30/30), Recover (20/20)
- Protocol Trigger Check:
  - Mewtwo HP: 101 (> 60 trigger). Psychic PP: 4 (> 3 trigger).
  - Blastoise HP: 155 (> 60 trigger). Surf PP: 12 (> 3 trigger).
  - Status: Safe to continue switch-training in Cerulean Cave 1F.

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



### Exp. All Empirical Model Audit & Observations Across Battles 1-76
- Mathematical Model Analysis:
  - Participant Share is strictly: floor(floor(E / 2) / n_participants) = floor(E / 4) for 2 participants.
  - Exp. All Base Share (Empirically Observed Range E/24 to E/27):
    - Golbat (E=1104, base=46 = E/24.0) [B1,6-8,12,17,20,29,32,38,40,44,48,55,58,64,66,67,68]
    - Kadabra (E=1008, base=42 = E/24.0) [B2,16,25,72]
    - Raichu (E=908, base=37 = E/24.5) [B19,35,53,60]
    - Dodrio (E=1092, base=42 = E/26.0) [B3,18,26,30,36,37,59,70]
    - Magneton (E=1050, base=39 = E/26.9) [B13,22,27,31,50,61,62]
    - Sandslash (E=1188, base=44 = E/27.0) [B5,9,10,14,23,56,65]
    - Venomoth (E=952, base=35 = E/27.2) [B15,21,28,33,34,52,71,76]
    - Parasect (E=950, base=37 = E/25.7) [B41, B42, B46]
    - Hypno (E=1076, base=39 = E/27.6) [B4,11,24,39,43,45,47,49,51,54,57,63,69,73,74,75]
    The exact assembly division mechanism causing division by 24-27 remains an unproven hypothesis pending formal disassembly review.
  - Boosted Exp. All Share strictly adheres to Gen 1 integer arithmetic: boosted = base + floor(base / 2) (100% verified across all 61 battles!).

### Psyduck Switch-Training Combat Protocol
- Vulnerability Profile: Psyduck (Water, Lv 15, HP 42, Attack 24, Defense 20, Speed 24, Special 24) has very low stats compared to Lv 46-53 Cerulean Cave wild Pokémon. Any hit will be lethal.
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
   - Celadon Dept Store 4F: Water Stone, Fire Stone, Leaf Stone, Thunder Stone purchasable for ¥2,100 each.
   - Current Bag/PC Stones: Moon Stone x1 in PC. Money: ¥3056.

### Expedition 5 Summary Log (Psyduck Trainee, Battles 62-73, Turns 37360-37514):
- Battles Fought: 12 (B62 Magneton, B63 Hypno, B64 Golbat, B65 Sandslash, B66 Golbat, B67 Golbat, B68 Golbat, B69 Hypno, B70 Dodrio, B71 Venomoth, B72 Kadabra, B73 Hypno).
- Total EXP Gained by Psyduck: 3,736 EXP (grew from Lv 15 [3,375 EXP] to Lv 19 [7,111 EXP]).
- Lv 19 Verified Stats: Attack 30, Defense 24, Speed 30, Special 30, HP 51/51.
- All Exp. All yields 100% verified and integrated into model above.
- Pit Stop: Executed at Turn 37542 (Full heal with Nurse Joy in Cerulean City).

### Expedition 6 Battle Log (Psyduck Trainee, Battles 74+):
- Battle 74 (Exp 6 Battle 1, Turn 37586): Defeated Wild Hypno Lv 46. Blastoise Surf (OHKO).
  - Psyduck: 308 EXP (269 participant + 39 team share) -> New EXP: 8,000 (1,261 to Lv 21).
  - DUX: 58 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 39 EXP each.
  - Formula audit: 100% consistent with verified Hypno model.
- Battle 75 (Exp 6 Battle 2, Turn 37603): Defeated Wild Hypno Lv 46. Blastoise Surf (2HKO).
  - Psyduck: 308 EXP (269 participant + 39 team share) -> New EXP: 8,000 (1,261 to Lv 21).
  - DUX: 58 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 39 EXP each.
  - Formula audit: 100% consistent with verified Hypno model.
- Battle 76 (Exp 6 Battle 3, Turn 37623): Defeated Wild Venomoth Lv 49. Mewtwo STAB Psychic (OHKO).
  - Psyduck: 273 EXP (238 participant + 35 team share) -> New EXP: 8,000 (Grew to Lv 20!).
    - Lv 20 Stats: Attack 31, Defense 25, Speed 31, Special 31 [Empirically Verified Turn 37623 Screen].
  - DUX: 52 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 35 EXP each.
  - Formula audit: 100% consistent with verified Venomoth model.- Battle 77 (Exp 6 Battle 4, Turn 37637): Defeated Wild Dodrio Lv 49. Mewtwo STAB Psychic (OHKO).
  - Psyduck: 315 EXP (273 participant + 42 team share) -> New EXP: 8,315 (946 to Lv 21).
  - DUX: 63 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 42 EXP each.
  - Formula audit: 100% consistent with verified Dodrio model (E=1092, participant=273, base=42).
- Battle 78 (Exp 6 Battle 5, Turn 37651): Defeated Wild Raichu Lv 53. Mewtwo STAB Psychic (OHKO).
  - Psyduck: 264 EXP (227 participant + 37 team share) -> New EXP: 8,579 (682 to Lv 21).
  - DUX: 55 EXP (boosted).
  - OMEGA: 264 EXP (227 participant + 37 team share).
  - VEE, ROCKY, SHELDON: 37 EXP each.
  - Formula audit: 100% consistent with verified Raichu model (E=908, participant=227, base=37).
- Battle 79 (Exp 6 Battle 6, Turn 37667): Defeated Wild Magneton Lv 46. Mewtwo STAB Psychic (OHKO).
  - Psyduck: 301 EXP (262 participant + 39 team share) -> New EXP: 8,880 (381 to Lv 21).
  - DUX: 58 EXP (boosted).
  - OMEGA: 301 EXP (262 participant + 39 team share).
  - VEE, ROCKY, SHELDON: 39 EXP each.
  - Formula audit: 100% consistent with verified Magneton model (E=1050, participant=262, base=39).
- Battle 80 (Exp 6 Battle 7, Turn 37679): Defeated Wild Magneton Lv 46. Mewtwo STAB Psychic (OHKO).
  - Psyduck: 301 EXP (262 participant + 39 team share) -> New EXP: 9,181 (80 to Lv 21).
  - DUX: 58 EXP (boosted).
  - OMEGA: 301 EXP (262 participant + 39 team share).
  - VEE, ROCKY, SHELDON: 39 EXP each.
  - Formula audit: 100% consistent with verified Magneton model (E=1050, participant=262, base=39).
- Battle 81 (Exp 6 Battle 8, Turn 37696): Defeated Wild Golbat Lv 46. Mewtwo STAB 2x SE Psychic (OHKO).
  - Psyduck: 322 EXP (276 participant + 46 team share) -> New EXP: 9,503 (Grew to Level 21!).
  - DUX: 69 EXP (boosted).
  - OMEGA: 322 EXP (276 participant + 46 team share).
  - VEE, ROCKY, SHELDON: 46 EXP each.
  - Formula audit: 100% consistent with verified Golbat model (E=1104, participant=276, base=46).
