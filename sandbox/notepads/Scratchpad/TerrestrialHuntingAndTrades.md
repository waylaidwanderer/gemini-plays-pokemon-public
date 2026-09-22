# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target Pok�mon: PSYDUCK (MIGRAINE Lv 20, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 9,503 [Turn 37696]. Psyduck reached Level 21!
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (26,434 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 72)

### Active Expedition Sweeper Attrition & Condition Log (Post-Battle 82, Turn 37711):
- Trainee: PSYDUCK (MIGRAINE) [Lv 21, Water, Lead Slot]
  - Status: Healthy
  - HP: 56 / 56 [Verified Lv 21 Turn 37701 Screen]
  - EXP: 9,811 (837 to Lv 22) [Level 21 Achieved!]
  - Stats: Attack 33, Defense 27, Speed 33, Special 32 [Empirically Verified Lv 21 Turn 37696 Screen]
- Primary Sweeper: BLASTOISE (SHELDON) [Lv 72, Water]
  - HP: 139 / 229 [Battle 82]
  - Status: Poisoned (PSN, Battle 82)
  - Active Move PP: Surf (11/15), Ice Beam (10/10), Body Slam (15/15), Double-Edge (15/15)
- Reserve Sweeper: MEWTWO (OMEGA) [Lv 72, Psychic]
  - HP: 97 / 249 [Battle 83 Psybeam]
  - Status: Paralyzed (PAR, Battle 78)
  - Active Move PP: Psychic (4/10), Swift (20/20), Barrier (30/30), Recover (20/20)
- Protocol Trigger Check:
  - Mewtwo HP: 97 (> 60 trigger). Psychic PP: 4 (> 3 trigger).
  - Blastoise HP: 139 (> 60 trigger). Surf PP: 11 (> 3 trigger).
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



### Exp. All Empirical Model Audit & Observations Across Battles 1-82
- Mathematical Model Analysis:
  - Participant Share is strictly: floor(floor(E / 2) / n_participants) = floor(E / 4) for 2 participants.
  - Exp. All Base Share (Empirically Observed Range E/24 to E/27):
    - Golbat (E=1104, base=46 = E/24.0) [B1,6-8,12,17,20,29,32,38,40,44,48,55,58,64,66,67,68,81]
    - Kadabra (E=1008, base=42 = E/24.0) [B2,16,25,72]
    - Raichu (E=908, base=37 = E/24.5) [B19,35,53,60,78]
    - Dodrio (E=1092, base=42 = E/26.0) [B3,18,26,30,36,37,59,70,77]
    - Magneton (E=1050, base=39 = E/26.9) [B13,22,27,31,50,61,62,79,80]
    - Sandslash (E=1188, base=44 = E/27.0) [B5,9,10,14,23,56,65]
    - Venomoth (E=952, base=35 = E/27.2) [B15,21,28,33,34,52,71,76]
    - Parasect (E=950, base=37 = E/25.7) [B41, B42, B46]
    - Hypno (E=1076, base=39 = E/27.6) [B4,11,24,39,43,45,47,49,51,54,57,63,69,73,74,75,82]
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

### Expedition 6 Summary Log (Psyduck Trainee, Battles 74-82, Turns 37579-37711):
- Battles Fought: 9 (B74 Hypno, B75 Hypno, B76 Venomoth, B77 Dodrio, B78 Raichu, B79 Magneton, B80 Magneton, B81 Golbat, B82 Hypno).
- Total EXP Gained by Psyduck: 2,700 EXP (grew from Lv 19 [7,111 EXP] past Lv 20 to Level 21 [9,811 EXP]).
- Lv 21 Verified Stats: HP 56/56, Attack 33, Defense 27, Speed 33, Special 32.
- Trainee Progress: 837 EXP remaining to Level 22 (10,648 EXP); 26,126 EXP to Level 33 Golduck (35,937 EXP).
- Primary Sweeper Blastoise: HP 141/229, Status PSN, Surf PP 11/15.
- Reserve Sweeper Mewtwo: HP 101/249, Status PAR, Psychic PP 4/10.
- Protocol Status: Safe to continue training (both sweepers HP > 60, primary PP > 3).
