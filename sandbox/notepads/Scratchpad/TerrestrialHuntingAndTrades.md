# Scratchpad: Terrestrial Hunting & Trade Planning
## Completed: Golduck (#055) at Lv 33 [Turn 39381, Verified Turn 39387]
- Completed Pokémon: GOLDUCK (MIGRAINE Lv 33, Water, #055)
  - Current Empirical EXP: 36,010 [Turn 39376].
  - Milestone Reached: Lv 33 achieved! Stats: Attack 51, Defense 41, Speed 51, Special 51 [Turn 39377]. Evolution in progress!
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP MILESTONE ACHIEVED: Level 33 reached! Evolution to Golduck (#055) in progress.
- Sweepers: Blastoise (SHELDON Lv 73) / Mewtwo (OMEGA Lv 73)

### Completed Expedition 13 Archive (N=4)
- Summary: 9 battles (B149-B157) completed; Trainee gained 2,970 EXP and grew to Level 32 (34,032 EXP, 1,905 EXP remaining to Lv 33 Golduck). Mewtwo sustained PAR from Thunder Wave in B157; pit-stop executed Turn 39268-39271 at Cerulean Center to cure PAR and restore 100% HP/PP. Verified N=4 yields documented in Combat.md and N=4 Yield Table below.

### Expedition 14 Systematic Encounter Log (N=4)
| Battle | Turn | Opponent | Sweeper | Sweeper Damage Taken | Sweeper End HP / PP | Trainee Gain | DUX Gain | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B158** | 39310 | Hypno Lv 46 | Blastoise (Surf) | 0 (Poison Gas Turn 1) | Blastoise 233/233 HP, 14/15 PP, PSN | +334 EXP (269+65) | +97 EXP | OHKO with STAB Surf. |
| **B159** | 39318 | Magneton Lv 46 | Mewtwo (Psychic) | 12 (took 12 dmg on switch) | Mewtwo 242/254 HP, 9/10 PP | +327 EXP (262+65) | +97 EXP | OHKO with STAB Psychic. |
| **B160** | 39328 | Golbat Lv 46 | Mewtwo (Psychic) | 0 (Haze Turn 1) | Mewtwo 242/254 HP, 8/10 PP | +341 EXP (276+65) | +97 EXP | OHKO with super-effective STAB Psychic. |
| **B161** | 39340 | Hypno Lv 46 | Blastoise (Surf x2) | 158 (took 14 PSN + 63 crit Psychic Turn 1, 14 PSN + 67 crit Psychic Turn 2) | Blastoise 67/233 HP, 13/15 PP, PSN | +334 EXP (269+65) | +97 EXP | 2HKO with Surf after 2 consecutive enemy critical Psychics. |
| **B162** | 39362 | Magneton Lv 46 | Mewtwo (Psychic) | 8 (took 8 dmg on switch) | Mewtwo 234/254 HP, 7/10 PP | +327 EXP (262+65) | +97 EXP | OHKO with STAB Psychic. |
| **B163** | 39371 | Kadabra Lv 49 | Mewtwo (Swift) | 9 (took 9 dmg on switch) | Mewtwo 225/254 HP, 7/10 PP | +315 EXP (252+63) | +94 EXP | OHKO with Swift! Trainee reached 36,010 EXP and leveled to 33! |

### Active Expedition 14 Sweeper Attrition & Condition Log:
- Primary Sweeper: MEWTWO (OMEGA) [Lv 73, Psychic]
  - Status: Healthy, HP: 225 / 254 [Battle 163 Turn 39376]
  - Stats: Attack 186, Defense 169, Speed 215, Special 254
  - Active Move PP: Psychic (7/10), Swift (19/20), Barrier (30/30), Recover (20/20)
  - Protocol Trigger Check: Healthy / Green (HP > 60, Psychic > 3, zero status afflictions). Evolution milestone reached.
- Secondary Sweeper: BLASTOISE (SHELDON) [Lv 73, Water]
  - Status: Poisoned (PSN), HP: 67 / 233 [Battle 161 Turn 39349]
  - Stats: Attack 174, Defense 201, Speed 173, Special 180
  - Active Move PP: Surf (13/15), Ice Beam (10/10), Body Slam (15/15), Double-Edge (15/15)
  - Protocol Trigger Check: Blastoise HP at 67; primary sweeper Mewtwo at full capacity (242 HP, 8 Psychic PP, 0 status) can solo final 569 EXP (~1-2 battles).
- Support / Flyer: FARFETCH'D (DUX) [Lv 22, Boosted EXP]
  - Status: Healthy, HP: 59 / 59 [Verified Battle 146 Screen Turn 39053]


### EXP.ALL N=4 Party Dilution Model & Verified Yields
- **Setup:** 4-member party: Psyduck (Slot 1), Mewtwo (Slot 2), Blastoise (Slot 3), Farfetch'd (Slot 4).
- **Disproven Continuous Formulas & 65 EXP Plateau:** While Sandslash (1188) yields 74 EXP (matching floor(1188/16)), strict floor(E/16) is definitively FALSIFIED by Golbat (observed 65 vs 69 predicted), Hypno (observed 65 vs 67 predicted), and Dodrio (observed 63 vs 68 predicted). Similarly, a continuous 65 EXP plateau is disproven by Dodrio's 63 EXP. Discrete assembly division routines and truncation determine each species yield independently without a single global closed-form equation.
  - Effective divisor K scales from ~24..27 (N=6) down to ~16..17 (N=4), proportional to party size reduction.
  - Participant Share (Psyduck + Sweeper) = floor(E_half / 2) = floor(total_EXP / 4).
  - Traded Pokémon Boost: boosted = base + floor(base / 2) (e.g. 65 + 32 = 97 EXP; 56 + 28 = 84 EXP).
- **N=4 Yield Table:**
| Species | Level | Total EXP | Part Share (E/4) | Team Share (N=4) | Trainee Gain (Part+Team) | DUX Gain (Boosted) | Verification Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Golbat** | 46 | 1,104 | 276 | **65 EXP** | **341 EXP** | **97 EXP** | Verified (B100, B126, B130) |
| **Hypno** | 46 | 1,076 | 269 | **65 EXP** | **334 EXP** | **97 EXP** | Verified (B98, B134, B141) |
| **Magneton** | 46 | 1,050 | 262 | **65 EXP** | **327 EXP** | **97 EXP** | Verified (B97, B132, B137) |
| **Dodrio** | 49 | 1,092 | 273 | **63 EXP** | **336 EXP** | **94 EXP** | Verified (B111, B124, B135) |
| **Sandslash**| 52 | 1,188 | 297 | **74 EXP** | **371 EXP** | **111 EXP** | Verified (B120, B123) |
| **Kadabra** | 49 | 1,008 | 252 | **63 EXP** | **315 EXP** | **94 EXP** | Verified (B107, B136) |
| **Venomoth** | 49 | 952 | 238 | **56 EXP** | **294 EXP** | **84 EXP** | Verified (B99, B110, B122, B133) |
| **Raichu** | 53 | 908 | 227 | **53 EXP** | **280 EXP** | **79 EXP** | Verified (B146) |
| **Ditto** | 53 | ~763 | ~190 | **N/A** | N/A | N/A | Absent from 1F Entrance Cavern encounter table (160 battles verified). |
| **Parasect** | 52 | 950 | 237 | **59 EXP** | **296 EXP** | **88 EXP** | Verified (B105, B106, B140) |

### Psyduck Switch-Training Combat Protocol
- Vulnerability Profile: Psyduck has low defense compared to Lv 46-53 Cerulean Cave wild Pokémon. Any direct hit is lethal.
- Turn 1 Rule: NEVER attack with Psyduck. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Sweeper Matchups:
  - Bug / Poison / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu, Kadabra): Switch to Mewtwo (OMEGA Lv 73). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass & Specific Targets (Dodrio, Sandslash, Parasect [4x Ice Beam], Ditto, Hypno [Def 70]): Switch to Blastoise (SHELDON Lv 73). High Defense (201) absorbs physical hits; retaliates with STAB Surf / Ice Beam.
- Retreat Protocol:
  - Immediate Trigger: Mewtwo Psychic PP <= 3 or HP < 60; Blastoise HP < 60 or Surf PP <= 3; or if either active sweeper sustains an incapacitating status condition (PAR, SLP, FRZ).
  - Poison (PSN) Handling:
    - Blastoise HP > 100: Continue training without pit-stop; Blastoise and Mewtwo share combat duties per standard matchups.
    - Blastoise HP 60�100: Continue training without pit-stop, BUT designate Mewtwo as the sole combat sweeper for all encounters to protect Blastoise from further combat damage. Pacing overworld steps drains only 1 HP per 4 steps, safely sustaining the final ~1-2 battles to reach Level 33 Golduck.
    - Blastoise HP < 60, or Mewtwo sustains PSN: Trigger pit-stop immediately.

### Other Post-Game Evolution Candidates
1. SLOWPOKE (DOPEY Lv 15, Box 2): Medium Fast, target 50,653 EXP (Lv 37 Slowbro #080).
2. In-Game Trades: Route 2 Gatehouse (Abra -> Mr. Mime #122); Route 18 Gatehouse 2F (Slowbro -> Lickitung #108).
3. Evolution Stones: Celadon Dept Store 4F (Water, Fire, Leaf, Thunder ¥2,100 each). Money: ¥3,056.