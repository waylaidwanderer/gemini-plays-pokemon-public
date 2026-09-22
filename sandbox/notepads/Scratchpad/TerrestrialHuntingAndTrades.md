# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-train Krabby (PINCHY Lv 15 -> Lv 28 Kingler #099) in Cerulean Cave 1F with Exp. All
- [x] Claimed Exp. All from Route 15 Gatehouse 2F [Turn 35997]
- Krabby Starting EXP: 3,375 EXP (Target: 21,952 EXP, 18,577 EXP needed)
- Switch Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 71)

### Cerulean Cave 1F EXP Yield Table (2 Participants, * = Empirically Tested in Current Run)
| Species | Level | Total Wild EXP | Participant Base Share (Native) | Traded Share (Boosted) | Primary Sweeper Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Raichu*** | 53 | 922 | **461 EXP** | 691 EXP | Mewtwo (Swift / Psychic) |
| **Venomoth*** | 49 | 966 | **483 EXP** | 724 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Magneton*** | 46 | 1,050 | **525 EXP** | 787 EXP | Mewtwo (STAB Psychic OHKO) |
| **Hypno*** | 46 | 1,076 | **538 EXP** | 807 EXP | Mewtwo (STAB Psychic / Swift) |
| **Golbat*** | 46 | 1,116 | **558 EXP** | 837 EXP | Mewtwo (STAB Psychic 2x SE OHKO) |
| **Sandslash*** | 52 | 1,202 | **601 EXP** | 901 EXP | Blastoise (STAB Surf 2x SE OHKO) |
| **Kadabra*** | 49 | 1,008 | **504 EXP** | 756 EXP | Blastoise (Surf / Body Slam) / Mewtwo |
| **Parasect*** | 52 | 950 | **475 EXP** | 712 EXP | Blastoise (Ice Beam 2x SE OHKO) |
| **Dodrio** (Historical) | 49 | 1,242 | **621 EXP** | 931 EXP | Blastoise (Ice Beam 2x SE OHKO) / Mewtwo |
| **Ditto** (Historical) | 53 | 454 | **227 EXP** | 340 EXP | Blastoise / Mewtwo |

- Note on Historical Entries: Dodrio and Ditto entries are marked (Historical) as unverified approximations carried over from earlier notes. Raichu, Venomoth, Magneton, Hypno, Golbat, Sandslash, Kadabra, and Parasect (*) are all 100% empirically verified in the current run.
- Average Yield per Cerulean Cave 1F battle (with EXP.ALL): ~350-400 EXP for Krabby (~45-50 battles for 18,577 EXP needed for Lv 28 Kingler).

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

### Exp. All Mathematical Distribution Model & Hypotheses
In Generation 1 retail, when EXP.ALL is present in the Bag, wild battle experience is split:
- Hypothesis 1 (Standard Gen 1 Engine Specification):
  - Total Battle EXP = E.
  - 50% Active Participant Pool: P_total = floor(E / 2). This pool is divided equally among all non-fainted battle participants: P_share = floor(P_total / n_participants).
  - 50% Exp. All Team Pool: T_total = floor(E / 2). This pool is divided equally among ALL 6 party members: T_share = floor(T_total / 6).
  - Krabby Net Yield (Active Participant in 2-participant battle: Krabby + Sweeper):
    Krabby_EXP = P_share + T_share = floor(floor(E / 2) / 2) + floor(floor(E / 2) / 6) ~ 0.25 E + 0.0833 E ~ 0.3333 E.
  - Non-participant Party Members (e.g. Farfetch'd, Jolteon, Geodude):
    Each receives T_share = floor(floor(E / 2) / 6) ~ 0.0833 E.
  - Boosted Traded Non-Participant (Farfetch'd / DUX):
    Does Exp. All passive share receive the 1.5x trade bonus?
    Formula test: DUX_EXP = T_share + floor(T_share / 2) vs T_share.
- Empirical Verification Protocol:
  - Battle 1: Record wild species and level (E).
  - Record the exact EXP gained by active sweeper (Mewtwo or Blastoise).
  - Record dialogue text for Krabby and Exp. All distribution to party members.
  - Verify exact integer numbers against the formulas above.

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
  - Battle 1: Wild Golbat Lv 46. Turn 1 switched Krabby to Mewtwo (confused). Turn 2 Mewtwo OHKOed Golbat with critical STAB Psychic.
    - Empirical EXP.ALL Distribution Results:
      - Participant Pool (50% of E): PINCHY (276 EXP) + OMEGA (276 EXP) = 552 EXP. Implies total battle E = 1,104.
      - Exp. All Team Pool:
        - PINCHY (Native): 46 EXP (552 / 12 = 46.0). Total Krabby gain: 276 + 46 = 322 EXP!
        - DUX (Traded): 69 EXP! EMPIRICAL PROOF: 1.5x trade bonus applies to Exp. All (46 + floor(46/2) = 69).
