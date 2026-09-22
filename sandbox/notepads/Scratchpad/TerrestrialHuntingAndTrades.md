# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-train Krabby (PINCHY Lv 15 -> Lv 28 Kingler #099) in Cerulean Cave 1F with Exp. All
- Krabby Starting EXP: 3,375 EXP (Current: 6,603 EXP, Target: 21,952 EXP, 15,349 EXP needed for Lv 28 Kingler)
- Switch Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 72)

### Cerulean Cave 1F EXP Yield Table (2 Participants Without Exp. All, * = Empirically Tested in Current Run)
| Species | Level | Total Wild EXP | Participant Base Share (50% Native) | Traded Share (Boosted) | Primary Sweeper Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Raichu*** | 53 | 922 | **461 EXP** | 691 EXP | Mewtwo (Swift / Psychic) |
| **Venomoth*** | 49 | 966 | **483 EXP** | 724 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Magneton*** | 46 | 1,050 | **525 EXP** | 787 EXP | Mewtwo (STAB Psychic OHKO) |
| **Hypno*** | 46 | 1,076 | **538 EXP** | 807 EXP | Mewtwo (STAB Psychic / Swift) |
| **Golbat*** | 46 | 1,104 | **552 EXP** | 828 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Sandslash*** | 52 | 1,188 | **594 EXP** | 891 EXP | Blastoise (STAB Surf 2x SE OHKO) / Mewtwo |
| **Kadabra*** | 49 | 1,008 | **504 EXP** | 756 EXP | Blastoise (Surf / Body Slam) / Mewtwo |
| **Parasect*** | 52 | 950 | **475 EXP** | 712 EXP | Blastoise (Ice Beam 2x SE OHKO) |
| **Dodrio*** | 49 | 1,092 | **546 EXP** | 819 EXP | Mewtwo (STAB Psychic OHKO) |
| **Ditto** (Historical) | 53 | 454 | **227 EXP** | 340 EXP | Blastoise / Mewtwo |

- Note on Historical Entries: Only Ditto remains marked (Historical) as an unverified approximation. Raichu, Venomoth, Magneton, Hypno, Golbat, Sandslash, Kadabra, Parasect, and Dodrio (*) are all 100% empirically verified in the current run.
- Average Yield per Cerulean Cave 1F battle (with EXP.ALL): ~350-400 EXP for Krabby (~45-50 battles for 18,577 EXP needed for Lv 28 Kingler).


### Exp. All Empirical Model Audit & Observations Across Battles 1-5
- Empirical Exp. All Distribution Records (2 Active Participants, 6 Party Members):
  - Battle 1 (Golbat Lv 46, E = 1,104, Part Pool = 552): Participant Share = 276 EXP, Exp. All Base Share = 46 EXP (DUX = 69 EXP)
  - Battle 2 (Kadabra Lv 49, E = 1,008, Part Pool = 504): Participant Share = 252 EXP, Exp. All Base Share = 42 EXP (DUX = 63 EXP)
  - Battle 3 (Dodrio Lv 49, E = 1,092, Part Pool = 546): Participant Share = 273 EXP, Exp. All Base Share = 42 EXP (DUX = 63 EXP)
  - Battle 4 (Hypno Lv 46, E = 1,076, Part Pool = 538): Participant Share = 269 EXP, Exp. All Base Share = 39 EXP (DUX = 58 EXP)
  - Battle 5 (Sandslash Lv 52, E = 1,188, Part Pool = 594): Participant Share = 297 EXP, Exp. All Base Share = 44 EXP (DUX = 66 EXP)
- Mathematical Model Analysis:
  - Participant Share is strictly: floor(floor(E / 2) / n_participants) = floor(E / 4) for 2 participants.
  - Exp. All Base Share (Unproven Hypothesis): In-game base share yields range empirically from E / 24 to E / 27 across observed battles. The underlying assembly division registers causing this variation remain an unproven hypothesis pending formal register verification.
  - Boosted Exp. All Share strictly adheres to Gen 1 integer arithmetic: boosted = base + floor(base / 2) (100% verified across all 5 battles!).

### Krabby Switch-Training Combat Protocol
- Vulnerability Profile: Krabby (Water, Lv 15, HP 38, Special 15, Defense 42, Speed 23) has catastrophic vulnerability to Special attacks (Electric, Grass, Psychic) due to its minimal Special stat (15) and low HP (38). Any Special hit from Cerulean Cave wild Pokémon will instantly OHKO Krabby.
- Turn 1 Rule: NEVER attack with Krabby. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Exp. All Mechanics Note: The exact integer arithmetic formula for Exp. All distribution in retail Gen 1 remains an unverified hypothesis pending dedicated testing in upcoming battles.
- Exp. All Integration: Once Exp. All is claimed from Route 15 Gatehouse, Krabby will automatically receive passive EXP from every defeated opponent without needing to enter battle directly, eliminating OHKO risks. If placed in battle and switched out, Krabby earns both active participant share and passive Exp. All share.
- Sweeper Matchups:
  - Poison / Bug / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu): Switch to Mewtwo (OMEGA Lv 71). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass (Dodrio, Sandslash, Parasect, Ditto, Hypno): Switch to Blastoise (SHELDON Lv 72). High Defense (197) absorbs physical hits; retaliates with STAB Surf / 2x Ice Beam.
- PP Budget & Pit-Stop Protocol:
  - Blastoise: Surf 13/15, Ice Beam 8/10, Body Slam 15/15, Double-Edge 15/15.
  - Mewtwo: Psychic 9/10, Swift 20/20, Recover 20/20.
  - Retreat triggers: Sweeper HP < 60, primary SE PP <= 3, or Freeze status.

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

### Grinding Notes
- Input Buffering Caution: Rapidly buffering consecutive 'A' presses across menu transitions can trigger unintentional move selections (e.g., Slot 1 Double-Edge). Chunk inputs cleanly with 'B' or pauses to verify menu states.

### Battle Log (Expeditions 1-3 Summary & Active Log):
- Expeditions 1-3 Summary: Historical grind completed; Paras (#046) evolved into Parasect (#047), verifying Pokédex at 50 caught.
- Expedition 4 (Active): Krabby switch-training with EXP.ALL in Cerulean Cave 1F.
  - Battles 1-5 Summary: Historical switch-grind with EXP.ALL against Golbat Lv 46 (+322 EXP), Kadabra Lv 49 (+294 EXP), Dodrio Lv 49 (+315 EXP, PINCHY Lv 16, ROCKY Lv 9), Hypno Lv 46 (+308 EXP, DUX Lv 7, Leer declined), and Sandslash Lv 52 (+341 EXP, PINCHY Lv 17). All empirical EXP yields verified and consolidated in the Model Audit table above.
  - Battles 6-8 (Wild Golbat Lv 46 x3): Blastoise OHKOed with 2x SE Ice Beam (took 0 dmg from Haze in B6 & B8, 8 dmg from Wing Attack in B7, HP 160/229).
    - Yields per battle: PINCHY +322 EXP (276 part + 46 Exp. All), SHELDON +322 EXP, DUX +69 EXP (traded), OMEGA/VEE/ROCKY +46 EXP each.
    - Milestones: DUX reached Lv 8 (B6), ROCKY reached Lv 10 (B6), PINCHY reached Level 18 (B8, Atk 47, Def 42, Spd 26, Spc 16, HP 42/42 verified). PINCHY total EXP: 5,921.
  - Battle 9: Wild Sandslash Lv 52. Turn 1 switched Krabby to Blastoise (took 10 dmg from Fury Swipes, HP 150/229). Turn 2 Blastoise OHKOed Sandslash with STAB 2x SE Surf (Surf PP 12/15).
    - Empirical EXP.ALL Distribution Results:
      - Participant Pool (50% of E): PINCHY (297 EXP) + SHELDON (297 EXP) = 594 EXP. Total battle E = 1,188 (Sandslash base exp = 160, Lv 52).
      - Exp. All Team Pool: Base share = 44 EXP (PINCHY, OMEGA, VEE, ROCKY, SHELDON).
      - Traded DUX (Boosted): 66 EXP (44 + floor(44/2) = 66).
      - PINCHY Net Gain: 297 + 44 = 341 EXP (Krabby EXP: 5,921 -> 6,262, only 597 to Lv 19!).

  - Battle 10: Wild Sandslash Lv 52. Turn 1 switched Krabby to Blastoise (took 15 dmg from 3-hit Fury Swipes, HP 135/229). Turn 2 Blastoise OHKOed Sandslash with STAB 2x SE Surf (Surf PP 11/15).
    - Empirical EXP.ALL Distribution Results:
      - Participant Pool (50% of E): PINCHY (297 EXP) + SHELDON (297 EXP) = 594 EXP. Total battle E = 1,188.
      - Exp. All Team Pool: Base share = 44 EXP (PINCHY, OMEGA, VEE, ROCKY, SHELDON).
      - Traded DUX (Boosted): 66 EXP (44 + floor(44/2) = 66).
      - PINCHY Net Gain: 297 + 44 = 341 EXP (Krabby EXP: 6,262 -> 6,603, only 256 to Lv 19!).