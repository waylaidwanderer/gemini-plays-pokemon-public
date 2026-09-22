# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Evolve Paras (FUNGI) into Parasect (#047)
- Target: Level 24 (13,824 EXP, Pokédex #047)
- Verified Starting State: Lv 10, HP 29/29, Atk 21, Def 16, Spd 11, Spc 18, EXP 1000, Move: Scratch (PP 35/35) [Turn 35442]
- Switch Sweepers: Blastoise (SHELDON Lv 71) / Mewtwo (OMEGA Lv 71)

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
- Average Yield per Cerulean Cave 1F battle: ~530 EXP (~23-24 battles to Lv 24 Parasect).

### Paras Switch-Training Combat Protocol
- Vulnerability Profile: Paras (Bug/Grass) suffers a catastrophic 4x weakness to Flying (Dodrio, Golbat) and 2x weaknesses to Fire, Poison, Bug, and Rock. At low levels, ANY attack from Cerulean Cave wild Pokémon will instantly OHKO Paras.
- Turn 1 Rule: NEVER attack with Paras. Immediately switch out to the designated sweeper on Turn 1.
- Sweeper Matchups:
  - Poison / Bug / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu): Switch to Mewtwo (OMEGA Lv 71). STAB Psychic / Swift guarantees rapid OHKOs.
  - Hypno Contingency: While Mewtwo is the primary Special counter, Blastoise is deployed to mitigate Mewtwo PSN attrition and preserve Psychic PP. Blastoise must use Surf or Body Slam (avoid Double-Edge to eliminate recoil damage).
  - Fast Physical / Ground / Normal / Grass (Dodrio, Sandslash, Parasect, Ditto): Switch to Blastoise (SHELDON Lv 71). High Defense (194) absorbs physical hits effortlessly; retaliates with STAB Surf / 2x Ice Beam.
- PP Budget & Pit-Stop Protocol:
  - Blastoise (SHELDON Lv 71): Surf 15 PP, Ice Beam 10 PP, Body Slam 15 PP, Double-Edge 15 PP (total 55 PP).
  - Mewtwo (OMEGA Lv 71): Psychic 10 PP, Swift 20 PP, Recover 20 PP (total 50 PP).
  - Combined High-Yield SE PP: 25 moves (Surf + Ice Beam) on Blastoise, 10 moves (Psychic) on Mewtwo = 35 primary OHKO moves.
  - Safe Grinding Window: ~18-20 battles per expedition before primary STAB PP runs low.
  - Pit-Stop Retreat Thresholds:
    1. HP Trigger: Sweeper HP < 60 (independent retreat trigger).
    2. PP Trigger: Blastoise Surf <= 3 PP AND Mewtwo Psychic <= 2 PP (compound PP depletion trigger).
    3. Status Trigger:
       - Freeze: Immediate retreat trigger upon battle conclusion.
       - Sleep: In-battle remedy via Poké Flute (Bag Slot 1, infinite use); no retreat needed unless compounded with low HP.
       - Poison: Increases HP retreat threshold to HP < 80.
       - Paralysis: Reduces Speed by 75% and incurs 25% full paralysis rate. Allowed to continue if Mewtwo HP >= 120 and Blastoise HP >= 80. If Mewtwo HP < 120 while paralyzed OR Blastoise HP < 80 while Mewtwo is paralyzed, trigger immediate retreat.
    4. Pit-Stop Execution Routine:
       a. Walk South to (24..25, 17) and step onto warp to exit Cerulean Cave onto canal apron at (4, 12).
       b. Open party menu -> Farfetch'd (DUX) -> FLY -> Cerulean City.
       c. Enter Pokémon Center, heal with Nurse Joy, return north via Route 24 canal.

### Other Post-Game Evolution Candidates
1. KRABBY (PINCHY Lv 15, Box 1 Slot 1):
   - Growth Group: Medium Fast (EXP = Level^3)
   - Target EXP: 21,952 EXP (Lv 28 Kingler #099)
   - Prerequisite Status: Caught, stored in Box 1 Slot 1.
2. PSYDUCK (MIGRAINE Lv 15, Box 2):
   - Growth Group: Medium Fast (EXP = Level^3)
   - Target EXP: 35,937 EXP (Lv 33 Golduck #055)
   - Prerequisite Status: Caught, stored in Box 2.
3. SLOWPOKE (DOPEY Lv 15, Box 2):
   - Growth Group: Medium Fast (EXP = Level^3)
   - Target EXP: 50,653 EXP (Lv 37 Slowbro #080)
   - Prerequisite Status: Caught, stored in Box 2.
4. In-Game Trades:
   - Route 2 Gatehouse: Trade Abra for Mr. Mime (MARCEL, #122).
     - Prerequisite Status: Wild Abra NOT yet caught (unobtained asset). Needs hunting on Route 24 or Route 8.
   - Route 18 Gatehouse 2F: Trade Slowbro for Lickitung (MARC, #108).
     - Prerequisite Status: Slowpoke owned (Box 2), but not yet evolved into Slowbro (unobtained asset).
5. Evolution Stones:
   - Celadon Dept Store 4F: Water Stone, Fire Stone, Leaf Stone, Thunder Stone purchasable for ¥2,100 each.
   - Current Bag/PC Stones: Moon Stone x1 in PC. Money: ¥3,056.

### Grinding Notes
- Ice Beam Typing: Bug is damaged normally (1x) by Ice in Gen 1, while Grass is weak (2x), making Ice Beam 2x Super Effective vs Parasect.
- Input Buffering Caution: Rapidly buffering consecutive 'A' presses across menu transitions can trigger unintentional move selections (e.g., Slot 1 Double-Edge). Chunk inputs cleanly with 'B' or pauses to verify menu states.

### Battle Log (Expeditions 1-14 Aggregated Summary):
- Expeditions 1-14 Summary: Defeated Sandslash Lv 52, Hypno Lv 46 x4, Venomoth Lv 49, Magneton Lv 46 x3, Kadabra Lv 49, Raichu Lv 53, Parasect Lv 52 x2 (14 battles total).
  - Starting State: Paras Lv 10 (1,000 EXP).
  - Current State: Paras Lv 20 (8,327 EXP, +7,327 EXP gained across 14 battles). Learned Leech Life!
  - Target State: Lv 24 Parasect (13,824 EXP). Remaining EXP: 5,497 EXP (934 to Lv 21).

- Expedition 2 Summary [Turns 35760-35840]: 7 battles completed (Battles 15-21: Magneton Lv 46, Hypno Lv 46 x3, Golbat Lv 46 x2, Venomoth Lv 49). Paras gained 3,738 EXP, grew from Lv 20 (8,327 EXP) to Lv 22 (12,065 EXP, verified HP 53/53). Pit-stop executed at Cerulean Pokémon Center; team 100% restored.
- Expedition 3 Target: Lv 24 Parasect (13,824 EXP). Starting at Lv 22 (12,065 EXP; 102 EXP to Lv 23, 1,759 EXP to Lv 24).
- Battle 22 (Exp 3 Battle 1) [Turn 35878]: Defeated wild Hypno Lv 46. Switched Paras to Blastoise per Hypno Contingency; Surf 2HKO (Surf 13/15, Blastoise HP 204/225). Paras gained 538 EXP (12,603 EXP) and GREW TO LEVEL 23! Remaining to Lv 24 Parasect: 1,221 EXP (~2-3 battles).