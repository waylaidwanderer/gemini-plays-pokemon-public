# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-Train Slowpoke (DOPEY) to Slowbro (#080)
- Expedition Start Turn: Turn 39435
- Target: SLOWPOKE (DOPEY Lv 17, Water/Psychic, Lead Slot 1)
  - Starting Level: 15 (Baseline EXP: 3,375)
  - Current Level: 17 (EXP: 5,030, 802 to Lv 18)
  - Target Milestone: Lv 37 Slowbro (#080) at 37^3 = 50,653 EXP (+45,623 EXP required).
  - Subsequent Trade: Enables Route 18 Gatehouse 2F trade for Lickitung (#108).
- Party Architecture & Slot Allocation (Verified Turn 39444):
  - Slot 1: SLOWPOKE (DOPEY Lv 17) - Trainee / Lead
  - Slot 2: MEWTWO (OMEGA Lv 73) - Primary Sweeper (1 Down input in combat)
  - Slot 3: FARFETCH'D (DUX Lv 23) - Support (Fly / Cut)
  - Slot 4: BLASTOISE (SHELDON Lv 73) - Secondary Sweeper

### Expedition 15 Systematic Encounter Log (N=4)
| Battle | Turn | Opponent | Sweeper | Sweeper Damage Taken | Sweeper End HP / PP | Trainee Gain | DUX Gain | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B165** | 39482 | Sandslash Lv 52 | Blastoise (Surf) | 4 (Poison Sting Turn 1) | Blastoise 229/233 HP, 14 Surf PP | +371 EXP (297+74) | +111 EXP | OHKO with STAB Surf! Trainee at 3,746 EXP (350 to Lv 16). |
| **B166** | 39493 | Hypno Lv 46 | Mewtwo (Psychic) | 10 (Headbutt on T1 switch) | Mewtwo 234/254 HP, 9/10 Psychic PP | +334 EXP (269+65) | +97 EXP | STAB Psychic OHKO! Trainee at 4,080 EXP (16 to Lv 16). |
| **B167** | 39507 | Magneton Lv 46 | Mewtwo (Psychic) | 10 (Turn 1 switch) | Mewtwo 224/254 HP, 8/10 Psychic PP | +327 EXP (262+65) | +97 EXP | STAB Psychic OHKO! Slowpoke reached 4,407 EXP and GREW TO LEVEL 16! Stats: 27/27/11/21. |
| **B168** | 39543 | Magneton Lv 46 | Mewtwo (Psychic) | 9 (Turn 1 switch) | Mewtwo 215/254 HP, 7/10 Psychic PP | +327 EXP (262+65) | +97 EXP | STAB Psychic OHKO! Slowpoke at 4,734 EXP (179 to Lv 17). |
| **B169** | 39554 | Parasect Lv 52 | Blastoise (Ice Beam) | 8 (Leech Life Turn 1) | Blastoise 221/233 HP, 9/10 Ice Beam PP | +296 EXP (237+59) | +88 EXP | 4x Ice Beam OHKO! Slowpoke grew to LEVEL 17! Stats: Atk 28, Def 29, Spd 11, Spc 22. |

### EXP.ALL N=4 Party Dilution Model & Verified Yields
- Setup: 4-member party: Trainee (Slot 1), Mewtwo (Slot 2), Farfetch'd (Slot 3), Blastoise (Slot 4).
- Participant Share: floor(total_EXP / 4).
- Traded Pokémon Boost (DUX): boosted = base + floor(base / 2).
- N=4 Verified Base Team Yields:
  - Golbat Lv 46: Part 276 EXP, Team 65 EXP (Total Trainee: +341 EXP, Dux: +97 EXP)
  - Hypno Lv 46: Part 269 EXP, Team 65 EXP (Total Trainee: +334 EXP, Dux: +97 EXP)
  - Magneton Lv 46: Part 262 EXP, Team 65 EXP (Total Trainee: +327 EXP, Dux: +97 EXP)
  - Dodrio Lv 49: Part 273 EXP, Team 63 EXP (Total Trainee: +336 EXP, Dux: +94 EXP)
  - Sandslash Lv 52: Part 297 EXP, Team 74 EXP (Total Trainee: +371 EXP, Dux: +111 EXP)
  - Kadabra Lv 49: Part 252 EXP, Team 63 EXP (Total Trainee: +315 EXP, Dux: +94 EXP)
  - Venomoth Lv 49: Part 238 EXP, Team 56 EXP (Total Trainee: +294 EXP, Dux: +84 EXP)
  - Raichu Lv 53: Part 227 EXP, Team 53 EXP (Total Trainee: +280 EXP, Dux: +79 EXP)
  - Parasect Lv 52: Part 237 EXP, Team 59 EXP (Total Trainee: +296 EXP, Dux: +88 EXP)

### Slowpoke Switch-Training Combat Protocol
- Vulnerability Profile: Slowpoke (Lv 15) has low stats compared to Lv 46-53 wild Pokémon. Lethal danger from any hit.
- Turn 1 Rule: NEVER attack with Slowpoke. Immediately switch to designated sweeper on Turn 1.
- In-Battle Switching Relative Coordinates:
  - To Primary Sweeper MEWTWO: Cursor on Slot 1 -> press Down x1 -> select OMEGA (Slot 2).
  - To Secondary Sweeper BLASTOISE: Cursor on Slot 1 -> press Down x3 -> select SHELDON (Slot 4).
- Sweeper Matchups:
  - Mewtwo (OMEGA, Slot 2): Golbat, Venomoth, Magneton, Raichu, Kadabra, Hypno. STAB Psychic / Swift guarantees rapid OHKOs.
  - Blastoise (SHELDON, Slot 4): Dodrio, Sandslash, Parasect (4x Ice Beam). High defense (201) absorbs physical hits; retaliates with STAB Surf / Ice Beam.
- Retreat Protocol:
  - Trigger pit-stop if Mewtwo Psychic PP <= 3 or HP < 60; Blastoise HP < 60 or Surf PP <= 3; or if any sweeper sustains incapacitating status (PAR, SLP, FRZ, PSN).

### Other Post-Game Evolution Candidates
1. SLOWPOKE (DOPEY Lv 17, Lead Slot 1): ACTIVE TARGET -> switch-training to Lv 37 Slowbro (#080, 50,653 EXP). Enables Route 18 Lickitung trade.
2. In-Game Trades: Route 2 Gatehouse (Abra -> Mr. Mime #122); Route 18 Gatehouse 2F (Slowbro -> Lickitung #108).
3. Evolution Stones: Celadon Dept Store 4F (Water, Fire, Leaf, Thunder ¥2,100 each). Money: ¥3,056.