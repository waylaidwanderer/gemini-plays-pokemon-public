# Scratchpad: Terrestrial Hunting & Trade Planning
## Active Goal: Switch-Train Psyduck (MIGRAINE) to Golduck (#055) at Lv 33 (35,937 EXP)
- Target Pokémon: PSYDUCK (MIGRAINE Lv 31, Water, Medium Fast growth, Lead Slot 1)
  - Current Empirical EXP: 30,768 [Turn 39077].
  - Milestone Next: Lv 32 = 32^3 = 32,768 EXP (2,000 EXP remaining, ~6 battles).
  - Target: Lv 33 Golduck = 33^3 = 35,937 EXP (5,169 EXP remaining).
- Sweepers: Blastoise (SHELDON Lv 73) / Mewtwo (OMEGA Lv 73)

### Expedition 12 Systematic Encounter Log (N=4)
| Battle | Turn | Opponent | Sweeper | Sweeper Damage Taken | Sweeper End HP / PP | Trainee Gain | DUX Gain | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B141** | 38969 | Hypno Lv 46 | Blastoise (Surf) | 0 (Poison Gas failed Turn 1) | Blastoise 216/233 HP, 11/15 PP | +334 EXP (269+65) | +97 EXP | OHKO with Surf. |
| **B142** | 38985 | Golbat Lv 46 | Mewtwo (Psychic) | 29 (25 confusion + 4) | Mewtwo 201/254 HP, 6/10 PP | +341 EXP (276+65) | +97 EXP | Took 25 confusion dmg + 4; OHKO with Psychic. |
| **B143** | 39010 | Kadabra Lv 49 | Mewtwo (Swift) | 12 (took 12 dmg on switch) | Mewtwo 189/254 HP, 18/20 Swift, 6/10 PP | +315 EXP (252+63) | +94 EXP | Crit OHKO with Swift. |
| **B144** | 39024 | Sandslash Lv 52 | Blastoise (Surf) | 13 (took 13 dmg on switch) | Blastoise 203/233 HP, 10/15 Surf | +371 EXP (297+74) | +111 EXP | OHKO with Surf. Trainee grew to Lv 31 and learned Disable! |
| **B145** | 39040 | Dodrio Lv 49 | Blastoise (Surf) | 59 (took 59 crit dmg on switch) | Blastoise 144/233 HP, 9/15 PP | +336 EXP (273+63) | +94 EXP | OHKO with Surf. |
| **B146** | 39051 | Raichu Lv 53 | Mewtwo (Psychic) | 0 (Growl Turn 1) | Mewtwo 189/254 HP, 5/10 PP | +280 EXP (227+53) | +79 EXP | OHKO with Psychic. |
| **B147** | 39071 | Magneton Lv 46 | Mewtwo (Psychic) | 11 (took 11 dmg on switch) | Mewtwo 178/254 HP, 4/10 PP | +327 EXP (262+65) | +97 EXP | OHKO with Psychic. |

### Active Expedition 12 Sweeper Attrition & Condition Log:
- Primary Sweeper: MEWTWO (OMEGA) [Lv 73, Psychic]
  - Status: Healthy, HP: 178 / 254 [Verified Battle 147 Turn 39075]
  - Stats: Attack 186, Defense 169, Speed 215, Special 254
  - Active Move PP: Psychic (4/10), Swift (18/20), Barrier (30/30), Recover (20/20)
  - Protocol Trigger Check: Mewtwo Psychic PP = 4 (Green).
- Secondary Sweeper: BLASTOISE (SHELDON) [Lv 73, Water]
  - Status: Healthy, HP: 144 / 233 [Verified Battle 145 Turn 39044]
  - Stats: Attack 174, Defense 201, Speed 173, Special 180
  - Active Move PP: Surf (9/15), Ice Beam (8/10), Body Slam (15/15), Double-Edge (15/15)
  - Protocol Trigger Check: Blastoise HP = 144, Surf PP = 9 (Green).
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
| **Dodrio** | 49 | 1,092 | 273 | **63 EXP** | **336 EXP** | **94 EXP** | Verified (B111, B124, B135, B138) |
| **Sandslash**| 52 | 1,188 | 297 | **74 EXP** | **371 EXP** | **111 EXP** | Verified (B120, B123) |
| **Kadabra** | 49 | 1,008 | 252 | **63 EXP** | **315 EXP** | **94 EXP** | Verified (B107, B136) |
| **Venomoth** | 49 | 952 | 238 | **56 EXP** | **294 EXP** | **84 EXP** | Verified (B99, B110, B122, B133) |
| **Raichu** | 53 | 908 | 227 | **53 EXP** | **280 EXP** | **79 EXP** | Verified (B146) |
| **Ditto** | 53 | ~763 | ~190 | **Pending** | Pending | Pending | Pending Empirical Encounter |
| **Parasect** | 52 | 950 | 237 | **59 EXP** | **296 EXP** | **88 EXP** | Verified (B105, B106, B116, B139, B140) |

### Psyduck Switch-Training Combat Protocol
- Vulnerability Profile: Psyduck has low defense compared to Lv 46-53 Cerulean Cave wild Pokémon. Any direct hit is lethal.
- Turn 1 Rule: NEVER attack with Psyduck. Immediately switch out to the designated sweeper (Mewtwo or Blastoise) on Turn 1.
- Sweeper Matchups:
  - Bug / Poison / Electric / Flying / Psychic (Golbat, Venomoth, Magneton, Raichu, Kadabra): Switch to Mewtwo (OMEGA Lv 73). STAB Psychic / Swift guarantees rapid OHKOs.
  - Fast Physical / Ground / Normal / Grass & Specific Targets (Dodrio, Sandslash, Parasect [4x Ice Beam], Ditto, Hypno [Def 70]): Switch to Blastoise (SHELDON Lv 73). High Defense (201) absorbs physical hits; retaliates with STAB Surf / Ice Beam.
- Retreat Protocol: Trigger pit-stop when Mewtwo Psychic PP <= 3 or HP < 60, Blastoise HP < 60 / Surf PP <= 3, or if either sweeper sustains an uncurable status condition (PAR, SLP, FRZ, PSN).

### Other Post-Game Evolution Candidates
1. SLOWPOKE (DOPEY Lv 15, Box 2): Medium Fast, target 50,653 EXP (Lv 37 Slowbro #080).
2. In-Game Trades: Route 2 Gatehouse (Abra -> Mr. Mime #122); Route 18 Gatehouse 2F (Slowbro -> Lickitung #108).
3. Evolution Stones: Celadon Dept Store 4F (Water, Fire, Leaf, Thunder ¥2,100 each). Money: ¥3,056.
