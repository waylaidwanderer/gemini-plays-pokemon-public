# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-train Krabby (PINCHY Lv 24 -> Lv 28 Kingler #099) in Cerulean Cave 1F with Exp. All
- Krabby Starting EXP: 3,375 EXP (Current: 14,771 EXP, Target: 21,952 EXP, 7,181 EXP needed for Lv 28 Kingler)
- Switch Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 72)

### Cerulean Cave 1F EXP Yield Table (Live Exp. All Yields: Participant + Team Share, * = Tested)
| Species | Level | Total Wild EXP | Krabby Total Gain (Part+Team) | DUX Gain (Boosted) | Primary Sweeper Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Raichu*** | 53 | 908 | **264 EXP** (227+37) | 55 EXP | Mewtwo (STAB Psychic OHKO) |
| **Venomoth*** | 49 | 952 | **273 EXP** (238+35) | 52 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Magneton*** | 46 | 1,050 | **301 EXP** (262+39) | 58 EXP | Mewtwo (STAB Psychic OHKO) |
| **Hypno*** | 46 | 1,076 | **308 EXP** (269+39) | 58 EXP | Mewtwo (STAB Psychic / Swift) |
| **Golbat*** | 46 | 1,104 | **322 EXP** (276+46) | 69 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Sandslash*** | 52 | 1,188 | **341 EXP** (297+44) | 66 EXP | Blastoise (STAB Surf 2x SE OHKO) / Mewtwo |
| **Kadabra*** | 49 | 1,008 | **294 EXP** (252+42) | 63 EXP | Blastoise (Surf / Body Slam) / Mewtwo |
| **Parasect*** | 52 | 950 | **272 EXP** (237+35) | 52 EXP | Blastoise (Ice Beam 2x SE OHKO) |
| **Dodrio*** | 49 | 1,092 | **315 EXP** (273+42) | 63 EXP | Mewtwo (STAB Psychic OHKO) |
| **Ditto** (Historical) | 53 | 454 | **131 EXP** (113+18) | 27 EXP | Blastoise / Mewtwo |

- Note on Table Entries: Golbat, Sandslash, Hypno, Magneton, Kadabra, Dodrio, Venomoth, and Parasect (*) are empirically verified without Exp. All. Raichu was empirically verified with Exp. All in Battle 19 (participant share 227, team share 37); its 454 share without Exp. All is a calculated extrapolation. Only Ditto remains an unverified theoretical projection.


### Exp. All Empirical Model Audit & Observations Across Battles 1-35
- Mathematical Model Analysis:
  - Participant Share is strictly: floor(floor(E / 2) / n_participants) = floor(E / 4) for 2 participants.
  - Exp. All Base Share (Empirically Observed Range E/24 to E/27):
    - Golbat (E=1104, base=46 = E/24.0) [B1,6-8,12,17,20,29,32]
    - Kadabra (E=1008, base=42 = E/24.0) [B2,16,25]
    - Raichu (E=908, base=37 = E/24.5) [B19,35]
    - Dodrio (E=1092, base=42 = E/26.0) [B3,18,26,30]
    - Magneton (E=1050, base=39 = E/26.9) [B13,22,27,31]
    - Sandslash (E=1188, base=44 = E/27.0) [B5,9,10,14,23]
    - Venomoth (E=952, base=35 = E/27.2) [B15,21,28,33,34]
    - Hypno (E=1076, base=39 = E/27.6) [B4,11,24]
    The exact assembly division mechanism causing division by 24-27 remains an unproven hypothesis pending formal disassembly review.
  - Boosted Exp. All Share strictly adheres to Gen 1 integer arithmetic: boosted = base + floor(base / 2) (100% verified across all 35 battles!).

### Krabby Switch-Training Combat Protocol
- Vulnerability Profile: Krabby (Water, Lv 15, HP 38, Special 15, Defense 42, Speed 23) has catastrophic vulnerability to Special attacks (Electric, Grass, Psychic) due to its minimal Special stat (15) and low HP (38). Any Special hit from Cerulean Cave wild Pokémon will instantly OHKO Krabby.
- Turn 1 Rule: NEVER attack with Krabby. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Sweeper Matchups:
  - Poison / Bug / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu): Switch to Mewtwo (OMEGA Lv 72). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass (Dodrio, Sandslash, Parasect, Ditto, Hypno): Switch to Blastoise (SHELDON Lv 72). High Defense (197) absorbs physical hits; retaliates with STAB Surf / 2x Ice Beam.
- PP Budget & Pit-Stop Protocol:
  - Retreat Triggers: Either designated sweeper reaching primary SE PP <= 3 or HP < 60, or major persistent status (PAR) combined with low PP.

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
   - Celadon Dept Store 4F: Water Stone, Fire Stone, Leaf Stone, Thunder Stone purchasable for ¥2,100 each.
   - Current Bag/PC Stones: Moon Stone x1 in PC. Money: ¥3,056.


### Battle Log (Expeditions 1-3 Summary & Active Log):
- Expeditions 1-3 Summary: Historical grind completed; Paras (#046) evolved into Parasect (#047), verifying Pokédex at 50 caught.
- Expedition 4 (Active): Krabby switch-training with EXP.ALL in Cerulean Cave 1F.
  - Battles 1-5 Summary: Historical switch-grind with EXP.ALL against Golbat Lv 46 (+322 EXP), Kadabra Lv 49 (+294 EXP), Dodrio Lv 49 (+315 EXP, PINCHY Lv 16, ROCKY Lv 9), Hypno Lv 46 (+308 EXP, DUX Lv 7, Leer declined), and Sandslash Lv 52 (+341 EXP, PINCHY Lv 17). All empirical EXP yields verified and consolidated in the Model Audit table above.
  - Battles 6-22 Consolidated Summary: Grinded Krabby from Lv 17 to Lv 21 (10,239 EXP, learned ViceGrip at Lv 20; DUX grew to Lv 11, ROCKY to Lv 12). Swept Golbat (B6-8,12,17,20), Sandslash (B9-10,14), Hypno (B11), Magneton (B13,22), Venomoth (B15,21), Kadabra (B16), Dodrio (B18), Raichu (B19). Healed at Cerulean Center after B20.
    - Battles 23-37 Consolidated Summary: Grinded Krabby from Lv 21 to Lv 24 (14,771 EXP, reached Lv 22 in B24, Lv 23 in B29, Lv 24 in B34; DUX grew to Lv 12 in B26, Lv 13 in B34; ROCKY grew to Lv 13 in B23, Lv 14 in B32). Swept Sandslash Lv 52 (B23), Hypno Lv 46 (B24), Kadabra Lv 49 (B25), Dodrio Lv 49 (B26, B30, B36, B37), Magneton Lv 46 (B27, B31), Venomoth Lv 49 (B28, B33, B34), Golbat Lv 46 (B29, B32), Raichu Lv 53 (B35). Full party heal at Cerulean Center Turn 36688. B36-37: Dodrio Lv 49 swept by Mewtwo (Psychic), Krabby gained 315 EXP each (273+42). All EXP distributions verified.