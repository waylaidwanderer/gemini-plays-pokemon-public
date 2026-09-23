# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-Train Slowpoke (DOPEY) to Slowbro (#080)
- Expedition Start Turn: Turn 39435
- Target: SLOWPOKE (DOPEY Lv 21, Water/Psychic, Lead Slot 1)
  - Starting Level: 15 (Baseline EXP: 3,375)
  - Current Level: 21 (EXP: 9,632, 1,016 to Lv 22)
  - Target Milestone: Lv 37 Slowbro (#080) at 37^3 = 50,653 EXP (+41,021 EXP required).
  - Subsequent Trade: Enables Route 18 Gatehouse 2F trade for Lickitung (#108).
- Party Architecture & Slot Allocation (Verified Turn 39444):
  - Slot 1: SLOWPOKE (DOPEY Lv 21) - Trainee / Lead
  - Slot 2: MEWTWO (OMEGA Lv 73) - Primary Sweeper (1 Down input in combat)
  - Slot 3: FARFETCH'D (DUX Lv 24) - Support (Fly / Cut)
  - Slot 4: BLASTOISE (SHELDON Lv 73) - Secondary Sweeper

### Expedition 15 Systematic Encounter Log (N=4)
*Summary B165-B170 (Turns 39482-39571): Switch-trained Slowpoke from Lv 15 (3,375 EXP) to Lv 18 (5,324 EXP). Pit-stop taken Turn 39585.*
*Summary B171-B179 (Turns 39622-39713): Switch-trained Slowpoke from Lv 18 (5,324 EXP) to Lv 20 (8,310 EXP). Verified Lv 20 stats: 33/33/13/26. Pit-stop taken Turn 39721.*
*Summary B180-B182 (Turns 39754-39779): Switch-trained Slowpoke from Lv 20 (8,310 EXP) to Lv 21 (9,305 EXP). Pit-stop 3 taken Turn 39799: PAR cured, Mewtwo 254/254 HP & 10/10 PP restored.*

| Battle | Turn | Opponent | Sweeper | Sweeper Damage Taken | Sweeper End HP / PP | Trainee Gain | DUX Gain | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B183** | 39901 | Magneton Lv 46 | Mewtwo (Psychic) | 12 (Thundershock) | Mewtwo 242/254 HP (PAR), 9/10 Psychic PP, 20/20 Swift PP | +327 EXP (262+65) | +97 EXP | Thundershock dealt 12 dmg; Mewtwo broke PAR and STAB Psychic OHKOed! Slowpoke at 9,632 EXP (1,016 to Lv 22). |

*Pit-stop 4 taken Turn 39929: PAR cured, Mewtwo 254/254 HP & 10/10 PP restored. Slowpoke at 9,632 EXP (1,016 to Lv 22).*

### EXP.ALL N=4 Party Dilution Model & Verified Yields
- Setup: 4-member party: Trainee (Slot 1), Mewtwo (Slot 2), Farfetch'd (Slot 3), Blastoise (Slot 4).
- (Individual base yield figures permanently documented in Mechanics/Combat.md)

### Slowpoke Switch-Training Combat Protocol
- Vulnerability Profile: Slowpoke (Lv 15) has low stats compared to Lv 46-53 wild Pokémon. Lethal danger from any hit.
- Turn 1 Rule: NEVER attack with Slowpoke. Immediately switch to designated sweeper on Turn 1.
- In-Battle Switching Relative Coordinates:
  - To Primary Sweeper MEWTWO: Cursor on Slot 1 -> press Down x1 -> select OMEGA (Slot 2).
  - To Secondary Sweeper BLASTOISE: Cursor on Slot 1 -> press Down x3 -> select SHELDON (Slot 4).
- Sweeper Matchups:
  - Mewtwo (OMEGA, Slot 2): Golbat, Venomoth, Magneton, Raichu, Kadabra. STAB Psychic guarantees rapid OHKOs.
  - Hypno Special Protocol: In Gen 1, Psychic resists Psychic (0.5x). Mewtwo's 254 Special deals ~65% damage with non-critical Psychic (OHKOs on ~25.4% crit). If Hypno survives Turn 2 Psychic, finish with SWIFT (Move 1, 20/20 PP) on Turn 3 to conserve Psychic PP (saving 1 PP per Hypno encounter).
  - Blastoise (SHELDON, Slot 4): Dodrio, Sandslash, Parasect (4x Ice Beam). High defense (201) absorbs physical hits; retaliates with STAB Surf / Ice Beam.
- Sweeper Redundancy & Secondary Sweeper Utilization:
  - Blastoise (SHELDON Lv 73, 233 HP, 15 Surf, 10 Ice Beam) is fully combat-ready.
  - If Mewtwo sustains PAR, poison, or runs low on Psychic PP (<= 3), do NOT retreat! Immediately transfer active sweeper duties to Blastoise (Slot 4: press Down x3 from Slot 1 in switch menu) and continue training encounters!
  - If a sweeper is put to sleep, use the Poké Flute in-battle from the Bag menu for an immediate zero-cost wake-up.
- Refined Retreat Protocol (Preventing Macro-Traversal Stagnation):
  - Trigger a pit-stop ONLY when BOTH sweepers are depleted (e.g. Mewtwo Psychic <= 2 AND Blastoise Surf <= 2, or both sweepers below 60 HP).

### Other Post-Game Evolution Candidates
1. In-Game Trades: Route 2 Gatehouse (Abra -> Mr. Mime #122); Route 18 Gatehouse 2F (Slowbro -> Lickitung #108).
2. Evolution Stones: Celadon Dept Store 4F (Water, Fire, Leaf, Thunder ¥2,100 each). Money: ¥3,056.
