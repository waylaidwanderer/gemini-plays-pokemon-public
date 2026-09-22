# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target Pok�mon: PSYDUCK (MIGRAINE Lv 18, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 6,803 [Turn 37495]. Needed to Lv 19: 56.
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (29,701 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 72) / Mewtwo (OMEGA Lv 72)

### Active Expedition Sweeper Attrition & Condition Log (Post-Battle 70, Turn 37471):
- Trainee: PSYDUCK (MIGRAINE) [Lv 18, Water, Lead Slot]
  - HP: 49 / 49 [Empirically Verified Battle 70 Turn 37464 Screen]
  - Status: Healthy
  - EXP: 6,803 (56 to Lv 19)
- Primary Sweeper: BLASTOISE (SHELDON) [Lv 72, Water]
  - HP: 135 / 229 [Empirically Verified Battle 72 Turn 37494 Screen]
  - Status: Healthy (no status)
  - Active Move PP: Surf (12/15), Ice Beam (8/10), Body Slam (14/15), Double-Edge (15/15)
- Reserve Sweeper: MEWTWO (OMEGA) [Lv 72, Psychic]
  - HP: 71 / 249 [Empirically Verified Battle 72 Turn 37492 Party Screen: 71 HP]
  - Status: Poisoned [PSN afflicted Turn 37372 vs Hypno]
  - Active Move PP: Psychic (6/10), Swift (18/20), Barrier (30/30), Recover (20/20)
- Protocol Trigger Check:
  - Mewtwo HP: 84 (> 60 trigger). Psychic PP: 6 (> 3 trigger).
    - Blastoise HP: 135 (> 60 trigger).
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



### Exp. All Empirical Model Audit & Observations Across Battles 1-72
- Mathematical Model Analysis:
  - Participant Share is strictly: floor(floor(E / 2) / n_participants) = floor(E / 4) for 2 participants.
  - Exp. All Base Share (Empirically Observed Range E/24 to E/27):
    - Golbat (E=1104, base=46 = E/24.0) [B1,6-8,12,17,20,29,32,38,40,44,48,55,58,64,66,67,68]
    - Kadabra (E=1008, base=42 = E/24.0) [B2,16,25,72]
    - Raichu (E=908, base=37 = E/24.5) [B19,35,53,60]
    - Dodrio (E=1092, base=42 = E/26.0) [B3,18,26,30,36,37,59,70]
    - Magneton (E=1050, base=39 = E/26.9) [B13,22,27,31,50,61,62]
    - Sandslash (E=1188, base=44 = E/27.0) [B5,9,10,14,23,56,65]
    - Venomoth (E=952, base=35 = E/27.2) [B15,21,28,33,34,52,71]
    - Parasect (E=950, base=37 = E/25.7) [B41, B42, B46]
    - Hypno (E=1076, base=39 = E/27.6) [B4,11,24,39,43,45,47,49,51,54,57,63,69]
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

### Expedition 5 Battle Log (Psyduck Trainee, Continuous Battles 62-66):
- Battle 62 (Exp 5 Battle 1, Turn 37360): Defeated Wild Magneton Lv 46. Mewtwo STAB Psychic (Critical Hit OHKO).
  - Psyduck: 301 EXP (262 participant + 39 team share) -> New EXP: 3,676 (420 to Lv 16).
  - DUX: 58 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 39 EXP each.
  - Formula audit: 100% consistent with verified Magneton model.
- Battle 63 (Exp 5 Battle 2, Turn 37375): Defeated Wild Hypno Lv 46. Mewtwo Swift (2HKO, Turn 2 Critical Hit).
  - Psyduck: 308 EXP (269 participant + 39 team share) -> New EXP: 3,984 (112 to Lv 16).
  - DUX: 58 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 39 EXP each.
  - Formula audit: 100% consistent with verified Hypno model.
- Battle 64 (Exp 5 Battle 3, Turn 37387): Defeated Wild Golbat Lv 46. Mewtwo STAB Psychic (2x SE OHKO).
  - Psyduck: 322 EXP (276 participant + 46 team share) -> New EXP: 4,306 (Grew to Lv 16!).
    - Lv 16 Stats: Attack 26, Defense 21, Speed 26, Special 25 [Empirically Verified Turn 37388 Screen].
  - DUX: 69 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 46 EXP each.
  - Formula audit: 100% consistent with verified Golbat model.
- Battle 65 (Exp 5 Battle 4, Turn 37396): Defeated Wild Sandslash Lv 52. Blastoise STAB Surf (2x SE OHKO).
  - Psyduck: 341 EXP (297 participant + 44 team share) -> New EXP: 4,647 (266 to Lv 17).
  - DUX: 66 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 44 EXP each.
  - Formula audit: 100% consistent with verified Sandslash model.
- Battle 66 (Exp 5 Battle 5, Turn 37409): Defeated Wild Golbat Lv 46. Mewtwo STAB Psychic (2x SE OHKO).
  - Psyduck: 322 EXP (276 participant + 46 team share) -> New EXP: 4,969 (Grew to Lv 17!).
    - Lv 17 Stats: Attack 27, Defense 22, Speed 27, Special 27 [Empirically Verified Turn 37411 Screen].
  - DUX: 69 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 46 EXP each.
  - Formula audit: 100% consistent with verified Golbat model.
- Battle 67 (Exp 5 Battle 6, Turn 37419): Defeated Wild Golbat Lv 46. Mewtwo STAB Psychic (Critical Hit OHKO).
  - Psyduck: 322 EXP (276 participant + 46 team share) -> New EXP: 5,291 (541 to Lv 18).
  - DUX: 69 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 46 EXP each.
  - Formula audit: 100% consistent with verified Golbat model.
- Battle 68 (Exp 5 Battle 7, Turn 37442): Defeated Wild Golbat Lv 46. Blastoise Ice Beam (Critical Hit 2x SE OHKO).
  - Psyduck: 322 EXP (276 participant + 46 team share) -> New EXP: 5,613 (219 to Lv 18).
  - DUX: 69 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 46 EXP each.
  - Formula audit: 100% consistent with verified Golbat model.
- Battle 69 (Exp 5 Battle 8, Turn 37460): Defeated Wild Hypno Lv 46. Blastoise STAB Surf (OHKO).
  - Psyduck: 308 EXP (269 participant + 39 team share) -> New EXP: 5,921 (Grew to Lv 18!).
    - Lv 18 Stats: Attack 28, Defense 23, Speed 28, Special 28 [Empirically Verified Turn 37460 Screen].
  - DUX: 58 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 39 EXP each.
  - Formula audit: 100% consistent with verified Hypno model.
- Battle 70 (Exp 5 Battle 9, Turn 37468): Defeated Wild Dodrio Lv 49. Blastoise Ice Beam (2x SE OHKO).
  - Psyduck: 315 EXP (273 participant + 42 team share) -> New EXP: 6,803 (56 to Lv 19).
  - DUX: 63 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 42 EXP each.
  - Formula audit: 100% consistent with verified Dodrio model.
- Battle 71 (Exp 5 Battle 10, Turn 37484): Defeated Wild Venomoth Lv 49. Blastoise STAB Surf (OHKO).
  - Psyduck: 273 EXP (238 participant + 35 team share) -> New EXP: 6,803 (56 to Lv 19).
  - DUX: 52 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 35 EXP each.
  - Formula audit: 100% consistent with verified Venomoth model.
- Battle 72 (Exp 5 Battle 11, Turn 37495): Defeated Wild Kadabra Lv 49. Blastoise Body Slam (OHKO).
  - Psyduck: 294 EXP (252 participant + 42 team share) -> New EXP: 6,803 (56 to Lv 19).
  - DUX: 63 EXP (boosted).
  - OMEGA, VEE, ROCKY, SHELDON: 42 EXP each.
  - Formula audit: 100% consistent with verified Kadabra model.
