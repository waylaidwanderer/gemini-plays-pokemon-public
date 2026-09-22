# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-train Krabby (PINCHY Lv 26 -> Lv 28 Kingler #099) in Cerulean Cave 1F with Exp. All
- Krabby Starting EXP: 3,375 EXP (Current: 19,030 EXP, Target: 21,952 EXP, 2,922 EXP needed for Lv 28 Kingler)
- Switch Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 72)

### Cerulean Cave 1F EXP Yield Table (Live Exp. All Yields: Participant + Team Share, 100% Empirically Verified)
| Species | Level | Total Wild EXP | Krabby Total Gain (Part+Team) | DUX Gain (Boosted) | Primary Sweeper Strategy |
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



### Exp. All Empirical Model Audit & Observations Across Battles 1-51
- Mathematical Model Analysis:
  - Participant Share is strictly: floor(floor(E / 2) / n_participants) = floor(E / 4) for 2 participants.
  - Exp. All Base Share (Empirically Observed Range E/24 to E/27):
    - Golbat (E=1104, base=46 = E/24.0) [B1,6-8,12,17,20,29,32,38,40,44,48]
    - Kadabra (E=1008, base=42 = E/24.0) [B2,16,25]
    - Raichu (E=908, base=37 = E/24.5) [B19,35]
    - Dodrio (E=1092, base=42 = E/26.0) [B3,18,26,30,36,37]
    - Magneton (E=1050, base=39 = E/26.9) [B13,22,27,31,50]
    - Sandslash (E=1188, base=44 = E/27.0) [B5,9,10,14,23]
    - Venomoth (E=952, base=35 = E/27.2) [B15,21,28,33,34]
    - Parasect (E=950, base=37 = E/25.7) [B41, B42, B46]
    - Hypno (E=1076, base=39 = E/27.6) [B4,11,24,39,43,45,47,49,51]
    The exact assembly division mechanism causing division by 24-27 remains an unproven hypothesis pending formal disassembly review.
  - Boosted Exp. All Share strictly adheres to Gen 1 integer arithmetic: boosted = base + floor(base / 2) (100% verified across all 51 battles!).

### Krabby Switch-Training Combat Protocol
- Vulnerability Profile: Krabby (Water, Lv 25, HP 56, Attack 64, Defense 57, Speed 35, Special 21) has severe vulnerability to Special attacks (Electric, Grass, Psychic) due to its low Special stat (21) and modest HP (56). Any Special hit from Cerulean Cave wild Pokémon will deal massive or lethal damage.
- Turn 1 Rule: NEVER attack with Krabby. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Sweeper Matchups:
  - Poison / Bug / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu): Switch to Mewtwo (OMEGA Lv 72). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass (Dodrio, Sandslash, Parasect, Ditto, Hypno): Switch to Blastoise (SHELDON Lv 72). High Defense (197) absorbs physical hits; retaliates with STAB Surf / 2x Ice Beam.
- PP Budget & Pit-Stop Protocol:
  - Retreat Triggers: Active sweeper reaching primary SE PP <= 3 (Mewtwo Psychic <= 3 triggers immediate pit stop to restore PP) or HP < 60, or major persistent status (PAR) combined with low PP. Pit stop completed at Turn 36884 (full party restore).

### Other Post-Game Evolution Candidates
1. PSYDUCK (MIGRAINE Lv 15, Box 2):
   - Growth Group: Medium Fast (EXP = Level^3)
   - Target EXP: 35,937 EXP (Lv 33 Golduck #055)
   - Prerequisite Status: Caught, stored in Box 2.
2. SLOWPOKE (DOPEY Lv 15, Box 2):
   - Growth Group: Medium Fast (EXP = Level^3)
   - Target EXP: 50,653 EXP (Lv 37 Slowbro #080)
   - Prerequisite Status: Caught, stored in Box 2.
3. In-Game Trades:
   - Route 2 Gatehouse: Trade Abra for Mr. Mime (MARCEL, #122).
     - Prerequisite Status: Wild Abra NOT yet caught (unobtained asset). Needs hunting on Route 24 or Route 8.
   - Route 18 Gatehouse 2F: Trade Slowbro for Lickitung (MARC, #108).
     - Prerequisite Status: Slowpoke owned (Box 2), but not yet evolved into Slowbro (unobtained asset).
4. Evolution Stones:
   - Celadon Dept Store 4F: Water Stone, Fire Stone, Leaf Stone, Thunder Stone purchasable for Â¥2,100 each.
   - Current Bag/PC Stones: Moon Stone x1 in PC. Money: Â¥3,056.


### Battle Log (Expeditions 1-3 Summary & Active Log):
- Expedition 4 (Active): Krabby switch-training with EXP.ALL in Cerulean Cave 1F.
  - Battles 1-5 Summary: Historical switch-grind with EXP.ALL against Golbat, Kadabra, Dodrio, Hypno, and Sandslash. All empirical EXP yields verified and consolidated in the Model Audit table above.
  - Battles 6-22 Consolidated Summary: Grinded Krabby from Lv 17 to Lv 21 (10,239 EXP, learned ViceGrip at Lv 20; DUX grew to Lv 11, ROCKY to Lv 12). Swept Golbat (B6-8,12,17,20), Sandslash (B9-10,14), Hypno (B11), Magneton (B13,22), Venomoth (B15,21), Kadabra (B16), Dodrio (B18), Raichu (B19). Healed at Cerulean Center after B20.
  - Battles 23-46 Consolidated Summary: Grinded Krabby from Lv 21 to Lv 25 (17,483 EXP, reached Lv 22 in B24, Lv 23 in B29, Lv 24 in B34, Lv 25 in B40; learned Guillotine at Lv 25; DUX grew to Lv 12 in B26, Lv 13 in B34, Lv 14 in B43; ROCKY grew to Lv 13 in B23, Lv 14 in B32, Lv 15 in B42). Swept Sandslash Lv 52 (B23), Hypno Lv 46 (B24, B39, B43, B45), Kadabra Lv 49 (B25), Dodrio Lv 49 (B26, B30, B36, B37), Magneton Lv 46 (B27, B31), Venomoth Lv 49 (B28, B33, B34), Golbat Lv 46 (B29, B32, B38, B40, B44), Raichu Lv 53 (B35), Parasect Lv 52 (B41, B42, B46). All EXP distributions verified.  - Battles 47-51 Consolidated Summary: Grinded Krabby from Lv 25 (17,483 EXP) to Lv 26 (19,030 EXP, 653 to Lv 27, 2,922 to Lv 28 Kingler; leveled up in B47; DUX grew to 58 EXP share; VEE leveled up to Lv 26 in B48). Swept Hypno Lv 46 (B47, B49, B51), Golbat Lv 46 (B48), Magneton Lv 46 (B50) using Mewtwo. Mewtwo afflicted with PSN in B51 (160/249 HP). All EXP distributions and formula ratios 100% verified across 51 battles.
