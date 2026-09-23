# Scratchpad: Terrestrial Hunting & Trade Planning

## Active Goal: Switch-Train Slowpoke (DOPEY) to Slowbro (#080)
- Expedition Start Turn: Turn 39435
- Target: SLOWPOKE (DOPEY Lv 21, Water/Psychic, Lead Slot 1)
  - Starting Level: 15 (Baseline EXP: 3,375)
  - Current Level: 21 (EXP: 10,255, 393 to Lv 22)
  - Target Milestone: Lv 37 Slowbro (#080) at 37^3 = 50,653 EXP (+40,398 EXP required).
  - Subsequent Trade: Enables Route 18 Gatehouse 2F trade for Lickitung (#108).
- Party Architecture & Slot Allocation (Verified Turn 39444):
  - Slot 1: SLOWPOKE (DOPEY Lv 21) - Trainee / Lead
  - Slot 2: MEWTWO (OMEGA Lv 73) - Primary Sweeper (1 Down input in combat)
  - Slot 3: FARFETCH'D (DUX Lv 24) - Support (Fly / Cut)
  - Slot 4: BLASTOISE (SHELDON Lv 73) - Secondary Sweeper

### Expedition 15 Systematic Encounter Log (N=4)
*Summary B165-B170 (Turns 39482-39571): Switch-trained Slowpoke from Lv 15 (3,375 EXP) to Lv 18 (5,324 EXP). Pit-stop 1 taken Turn 39585.*
*Summary B171-B179 (Turns 39622-39713): Switch-trained Slowpoke from Lv 18 (5,324 EXP) to Lv 20 (8,310 EXP). Pit-stop 2 taken Turn 39721.*
*Summary B180-B183 (Turns 39754-39914): Switch-trained Slowpoke from Lv 20 (8,310 EXP) to Lv 21 (9,632 EXP). Pit-stops 3 & 4 taken (Mewtwo PAR cured, HP/PP fully restored). Slowpoke at 9,632 EXP (1,016 to Lv 22).*

| Battle | Turn | Opponent | Sweeper | Sweeper Damage Taken | Sweeper End HP / PP | Trainee Gain | DUX Gain | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B184** | 39975 | Parasect Lv 52 | Blastoise (Ice Beam) | 0 (Growth) | Blastoise 233/233 HP, 9/10 Ice Beam PP | +296 EXP (237+59) | +88 EXP | Turn 1 switch Slowpoke to Blastoise (absorbed Growth). Turn 2 Ice Beam 4x OHKO! Slowpoke at 9,928 EXP (720 to Lv 22). Mewtwo kept at 10/10 Psychic PP! |
| **B185** | 39998 | Magneton Lv 46 | Mewtwo (Psychic) | 11 (Thundershock) | Mewtwo 243/254 HP, 9/10 Psychic PP | +327 EXP (262+65) | +97 EXP | Turn 1 switch Slowpoke to Mewtwo (absorbed Thundershock 11 dmg, no PAR). Turn 2 STAB Psychic OHKO! Slowpoke at 10,255 EXP (393 to Lv 22). |

### Slowpoke Switch-Training Combat Protocol
- Vulnerability Profile: Slowpoke (Lv 21) has low stats compared to Lv 46-53 wild Pokémon. Lethal danger from any hit.
- Turn 1 Rule: NEVER attack with Slowpoke. Immediately switch to designated sweeper on Turn 1.
- In-Battle Switching Relative Coordinates:
  - To Primary Sweeper MEWTWO: Cursor on Slot 1 -> press Down x1 -> select OMEGA (Slot 2).
  - To Secondary Sweeper BLASTOISE: Cursor on Slot 1 -> press Down x3 -> select SHELDON (Slot 4).

### Sweeper Role & Matchup Profiles
- **MEWTWO (OMEGA Lv 73 - 254 Special, 215 Speed):**
  - **Mandatory Exclusive Targets:** Magneton Lv 46, Raichu Lv 53. (STAB Psychic guarantees rapid OHKOs; protects Blastoise from lethal Electric moves).
  - **Optimal Targets:** Golbat Lv 46, Venomoth Lv 49, Kadabra Lv 49.
  - **Hypno Special Protocol:** In Gen 1, Psychic resists Psychic (0.5x). Mewtwo deals ~65% with non-crit Psychic (OHKO on ~25.4% crit). If Hypno survives Turn 2, finish with SWIFT (Move 1, 20/20 PP) on Turn 3 to conserve Psychic PP.
- **BLASTOISE (SHELDON Lv 73 - 201 Defense, 180 Special, 233 HP):**
  - **Verified Target Matchup:**
    - Parasect Lv 52: 4x Ice Beam OHKO [Empirically Verified Battle 184 Turn 39982; 0 damage taken].
  - **Hypothesized Target Matchups (To Be Empirically Audited in Expedition 15):**
    - Golbat Lv 46: Projected 2x Ice Beam OHKO.
    - Dodrio Lv 49: Projected 2x Ice Beam OHKO; 201 Def absorbs Drill Peck.
    - Sandslash Lv 52: Projected 2x STAB Surf OHKO.
    - Kadabra Lv 49: Projected STAB Surf / Body Slam OHKO against frail 45 Def; 180 Special tanks Psybeam.
    - Hypno Lv 46: Projected STAB Surf / Body Slam chunking against 80 Def.
  - **Dangerous Matchups (AVOID):** Magneton Lv 46, Raichu Lv 53 (2x Electric damage; always route these to Mewtwo).
- **In-Battle Poké Flute Usage (Empirically Verified Turns 33850 & 39237):**
  - Using the Poké Flute from the in-battle Bag menu plays the tune and displays 'All sleeping POKéMON woke up!', awakening all sleepers (player and opponent).
  - Action Economy Cost: Using the flute consumes the player's combat turn, allowing the opponent to execute an attack that turn. Use only when active sweeper cannot act.
- **Refined Retreat Protocol (Preventing Macro-Traversal Stagnation):**
  - Do NOT retreat upon Mewtwo sustaining paralysis or running low on PP if Blastoise is healthy.
  - Transfer active sweeping to Blastoise for physical/ice-weak encounters (Golbat, Dodrio, Sandslash, Parasect, Kadabra).
  - Trigger a pit-stop ONLY when BOTH sweepers are depleted (e.g. Mewtwo Psychic <= 2 AND Blastoise Surf <= 2, or both sweepers below 60 HP).

### Other Post-Game Evolution Candidates
1. In-Game Trades: Route 2 Gatehouse (Abra -> Mr. Mime #122); Route 18 Gatehouse 2F (Slowbro -> Lickitung #108).
2. Evolution Stones: Celadon Dept Store 4F (Water, Fire, Leaf, Thunder ¥2,100 each). Money: ¥3,056.
