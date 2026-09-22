# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-train Krabby (PINCHY Lv 22 -> Lv 28 Kingler #099) in Cerulean Cave 1F with Exp. All
- Krabby Starting EXP: 3,375 EXP (Current: 10,888 EXP, Target: 21,952 EXP, 11,064 EXP needed for Lv 28 Kingler)
- Switch Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 72)

### Cerulean Cave 1F EXP Yield Table (2 Participants Without Exp. All, * = Empirically Tested in Current Run)
| Species | Level | Total Wild EXP | Participant Base Share (50% Native) | Traded Share (Boosted) | Primary Sweeper Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Raichu*** | 53 | 908 | **454 EXP** | 681 EXP | Mewtwo (STAB Psychic OHKO) |
| **Venomoth*** | 49 | 952-966 | **476-483 EXP** | 714-724 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Magneton*** | 46 | 1,050 | **525 EXP** | 787 EXP | Mewtwo (STAB Psychic OHKO) |
| **Hypno*** | 46 | 1,076 | **538 EXP** | 807 EXP | Mewtwo (STAB Psychic / Swift) |
| **Golbat*** | 46 | 1,104 | **552 EXP** | 828 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Sandslash*** | 52 | 1,188 | **594 EXP** | 891 EXP | Blastoise (STAB Surf 2x SE OHKO) / Mewtwo |
| **Kadabra*** | 49 | 1,008 | **504 EXP** | 756 EXP | Blastoise (Surf / Body Slam) / Mewtwo |
| **Parasect*** | 52 | 950 | **475 EXP** | 712 EXP | Blastoise (Ice Beam 2x SE OHKO) |
| **Dodrio*** | 49 | 1,092 | **546 EXP** | 819 EXP | Mewtwo (STAB Psychic OHKO) |
| **Ditto** (Historical) | 53 | 454 | **227 EXP** | 340 EXP | Blastoise / Mewtwo |

- Note on Table Entries: Golbat, Sandslash, Hypno, Magneton, Kadabra, Dodrio, Venomoth, Parasect, and Raichu (*) are empirically verified in the current run (Raichu verified Battle 19: 454 native w/o Exp.All, 227 w/ Exp.All). Only Ditto remains a theoretical projection pending dedicated in-game test verification.


### Exp. All Empirical Model Audit & Observations Across Battles 1-24
  - Battles 6-8 (Golbat Lv 46 x3, E = 1,104, Part Pool = 552): Participant Share = 276 EXP, Exp. All Base Share = 46 EXP (DUX = 69 EXP)
  - Battles 9-10 (Sandslash Lv 52 x2, E = 1,188, Part Pool = 594): Participant Share = 297 EXP, Exp. All Base Share = 44 EXP (DUX = 66 EXP)
  - Battle 11 (Hypno Lv 46, E = 1,076, Part Pool = 538): Participant Share = 269 EXP, Exp. All Base Share = 39 EXP (DUX = 58 EXP)
  - Battle 12 (Golbat Lv 46, E = 1,104, Part Pool = 552): Participant Share = 276 EXP, Exp. All Base Share = 46 EXP (DUX = 69 EXP)
  - Battle 13 (Magneton Lv 46, E = 1,050, Part Pool = 525): Participant Share = 262 EXP, Exp. All Base Share = 39 EXP (DUX = 58 EXP)
  - Battle 14 (Sandslash Lv 52, E = 1,188, Part Pool = 594): Participant Share = 297 EXP, Exp. All Base Share = 44 EXP (DUX = 66 EXP)
  - Battle 15 (Venomoth Lv 49, E = 952, Part Pool = 476): Participant Share = 238 EXP, Exp. All Base Share = 35 EXP (DUX = 52 EXP)
  - Battle 16 (Kadabra Lv 49, E = 1,008, Part Pool = 504): Participant Share = 252 EXP, Exp. All Base Share = 42 EXP (DUX = 63 EXP)
  - Battle 17 (Golbat Lv 46, E = 1,104, Part Pool = 552): Participant Share = 276 EXP, Exp. All Base Share = 46 EXP (DUX = 69 EXP)
  - Battle 18 (Dodrio Lv 49, E = 1,092, Part Pool = 546): Participant Share = 273 EXP, Exp. All Base Share = 42 EXP (DUX = 63 EXP)
  - Battle 19 (Raichu Lv 53, E = 908, Part Pool = 454): Participant Share = 227 EXP, Exp. All Base Share = 37 EXP (DUX = 55 EXP)
  - Battle 20 (Golbat Lv 46, E = 1,104, Part Pool = 552): Participant Share = 276 EXP, Exp. All Base Share = 46 EXP (DUX = 69 EXP)
  - Battle 21 (Venomoth Lv 49, E = 952, Part Pool = 476): Participant Share = 238 EXP, Exp. All Base Share = 35 EXP (DUX = 52 EXP)
  - Battle 22 (Magneton Lv 46, E = 1,050, Part Pool = 525): Participant Share = 262 EXP, Exp. All Base Share = 39 EXP (DUX = 58 EXP)
  - Battle 23 (Sandslash Lv 52, E = 1,188, Part Pool = 594): Participant Share = 297 EXP, Exp. All Base Share = 44 EXP (DUX = 66 EXP)
  - Battle 24 (Hypno Lv 46, E = 1,076, Part Pool = 538): Participant Share = 269 EXP, Exp. All Base Share = 39 EXP (DUX = 58 EXP)
- Mathematical Model Analysis:
  - Participant Share is strictly: floor(floor(E / 2) / n_participants) = floor(E / 4) for 2 participants.
  - Exp. All Base Share (Unproven Hypothesis): In-game base share yields range empirically from E / 24 to E / 27 across observed battles. The underlying assembly division registers causing this variation remain an unproven hypothesis pending formal register verification.
  - Boosted Exp. All Share strictly adheres to Gen 1 integer arithmetic: boosted = base + floor(base / 2) (100% verified across all 24 battles!).

### Krabby Switch-Training Combat Protocol
- Vulnerability Profile: Krabby (Water, Lv 15, HP 38, Special 15, Defense 42, Speed 23) has catastrophic vulnerability to Special attacks (Electric, Grass, Psychic) due to its minimal Special stat (15) and low HP (38). Any Special hit from Cerulean Cave wild Pokémon will instantly OHKO Krabby.
- Turn 1 Rule: NEVER attack with Krabby. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Sweeper Matchups:
  - Poison / Bug / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu): Switch to Mewtwo (OMEGA Lv 71). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass (Dodrio, Sandslash, Parasect, Ditto, Hypno): Switch to Blastoise (SHELDON Lv 72). High Defense (197) absorbs physical hits; retaliates with STAB Surf / 2x Ice Beam.
- PP Budget & Pit-Stop Protocol:
  - Live Status: Blastoise (HP 185/229, Surf 13/15, Ice Beam 10/10); Mewtwo (HP 234/249 Healthy, Psychic 8/10, Swift 20/20, Recover 20/20).
  - Retreat Triggers: Sweeper HP < 60, primary SE PP <= 3, or Freeze status.

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
  - Battles 6-22 Consolidated Summary:
    - B6-B8: Wild Golbat Lv 46 x3 (PINCHY Lv 18, DUX Lv 8, ROCKY Lv 10).
    - B9-B10: Wild Sandslash Lv 52 x2 (DUX Lv 9, ROCKY Lv 11).
    - B11: Wild Hypno Lv 46 (PINCHY Lv 19).
    - B12-B13: Wild Golbat Lv 46, Wild Magneton Lv 46 (Mewtwo swept).
    - B14: Wild Sandslash Lv 52 (DUX Lv 10).
    - B15: Wild Venomoth Lv 49 (PINCHY Lv 20, learned ViceGrip).
    - B16: Wild Kadabra Lv 49 (ROCKY Lv 12).
    - B17-B18: Wild Golbat Lv 46, Wild Dodrio Lv 49 (Blastoise swept).
    - B19: Wild Raichu Lv 53 (PINCHY Lv 21, DUX Lv 11).
    - B20: Wild Golbat Lv 46 (Blastoise swept; pit-stop heal at Cerulean Center).
    - B21: Wild Venomoth Lv 49 (Mewtwo swept; +273 EXP).
    - B22: Wild Magneton Lv 46 (Mewtwo swept; +301 EXP, PINCHY reached 10,239 EXP).
    - B23: Wild Sandslash Lv 52 (Blastoise swept; +341 EXP, PINCHY reached 10,580 EXP, 68 to Lv 22; ROCKY Lv 13).
    - B24: Wild Hypno Lv 46 (Blastoise swept; +308 EXP, PINCHY grew to Lv 22 [Atk 57, Def 50, Spd 31, Spc 19, 10,888 EXP]).
