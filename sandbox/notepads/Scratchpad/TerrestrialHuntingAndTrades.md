# Scratchpad: Terrestrial Hunting & Trade Planning

- Expedition Start Turn: Turn 39435
- Target: SLOWPOKE (DOPEY Lv 25, Water/Psychic, Lead Slot 1)
  - Starting Level: 15 (Baseline EXP: 3,375)
  - Current Level: 25 (Atk 41, Def 41, Spd 15, Spc 32 [Verified Turn 40288]; EXP: ~17,222, 354 to Lv 26)
  - Target Milestone: Lv 37 Slowbro (#080) at 37^3 = 50,653 EXP
### Expedition 15 Systematic Encounter Log (N=4)
*Summary B165-B183 (Turns 39482-39914): Switch-trained Slowpoke from Lv 15 (3,375 EXP) to Lv 21 (9,632 EXP). Defeated 19 encounters. Mewtwo and Blastoise maintained with 4 pit-stops.*

*Summary B184-B202 (Turns 39975-40286): Switch-trained Slowpoke from Lv 21 (9,632 EXP) to Lv 25 (15,865 EXP). Defeated 19 encounters across 4 levels. Mewtwo reached Lv 74.*
*Summary B203-B206 (Turns 40296-40354): Defeated Golbat Lv 46 x3 and Hypno Lv 46. Slowpoke gained 1,357 EXP, reaching ~17,222 EXP (354 to Lv 26). Blastoise reached Lv 74. Pit-Stop 5 executed Turn 40361 at Cerulean Pokémon Center (cured Mewtwo PSN, full HP/PP restored).*

| Battle | Turn | Opponent | Sweeper | Sweeper Damage Taken | Sweeper End HP / PP | Trainee Gain | DUX Gain | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **B203** | 40296 | Golbat Lv 46 | Blastoise (Ice Beam) | 0 (None/Fail) | Blastoise 91/233 HP, 4/10 Ice Beam PP | +341 EXP (276+65) | +97 EXP | Turn 1 switch Slowpoke to Blastoise (took 0 dmg). Turn 2 2x super-effective Ice Beam OHKO! Slowpoke at ~16,206 EXP (1,370 to Lv 26). |
| **B204** | 40314 | Golbat Lv 46 | Blastoise (Ice Beam) | 0 (Haze) | Blastoise 91/233 HP, 3/10 Ice Beam PP | +341 EXP (276+65) | +97 EXP | Turn 1 switch Slowpoke to Blastoise (Golbat Haze, 0 dmg). Turn 2 2x super-effective Ice Beam OHKO! Slowpoke at ~16,547 EXP (1,029 to Lv 26). |
| **B205** | 40330 | Hypno Lv 46 | Blastoise (Body Slam) | 9 (Headbutt) | Blastoise 82/233 HP, 12/15 Body Slam PP | +334 EXP (269+65) | +97 EXP | Turn 1 switch Slowpoke to Blastoise (took 9 dmg). Turn 2 Body Slam dealt ~80% (Hypno Meditate). Turn 3 Body Slam KO! Slowpoke at ~16,881 EXP (695 to Lv 26). |
| **B206** | 40343 | Golbat Lv 46 | Blastoise (Ice Beam) | 23 (Conf/Self) | Blastoise 59/233 HP, 2/10 Ice Beam PP | +341 EXP (276+65) | +97 EXP | Turn 1 switch Slowpoke to Blastoise (Confuse Ray). Turn 2 Sheldon hurt in confusion (23 dmg), Golbat used Haze (cured confusion!). Turn 3 2x super-effective Ice Beam Crit OHKO! Slowpoke at ~17,222 EXP (354 to Lv 26). |

### Slowpoke Switch-Training Combat Protocol
- Vulnerability Profile: Slowpoke (Lv 25) has low stats compared to Lv 46-53 wild PokÃ©mon. Lethal danger from any hit.
- Turn 1 Rule: NEVER attack with Slowpoke. Immediately switch to designated sweeper on Turn 1.
- In-Battle Switching Relative Coordinates:
  - To Primary Sweeper MEWTWO: Cursor on Slot 1 -> press Down x1 -> select OMEGA (Slot 2).
  - To Secondary Sweeper BLASTOISE: Cursor on Slot 1 -> press Down x3 -> select SHELDON (Slot 4).

### Sweeper Role & Matchup Profiles
- **Sweeper Baselines (Post-Heal Turn 40361):**
  - **MEWTWO (OMEGA Lv 74):** Psychic STAB sweeper. Status: Healthy, HP 259/259. Stats: Atk 190, Def 173, Spd 220, Spc 260. Moves: Swift (20/20), Psychic (10/10), Barrier (30/30), Recover (20/20).
    - **Primary Targets:** Magneton Lv 46, Raichu Lv 53 (Psychic OHKO; protects Blastoise from 2x Electric damage). Also available for fast neutral OHKOs.
  - **BLASTOISE (SHELDON Lv 74):** Physical/Special tank sweeper. Status: Healthy, HP 237/237. Stats: Atk 177, Def 204, Spd 176, Spc 183. Moves: Double-Edge (15/15), Body Slam (15/15), Surf (15/15), Ice Beam (10/10).
    - **Primary Targets:** Golbat Lv 46 (Ice Beam OHKO), Parasect Lv 52 (Ice Beam OHKO), Sandslash Lv 52 (Surf OHKO), Dodrio Lv 49 (Ice Beam OHKO), Hypno Lv 46 (Body Slam 2HKO), Kadabra Lv 49 (Body Slam OHKO), Venomoth Lv 49 (Ice Beam/Surf OHKO).
  - **In-Battle Poké Flute Usage (Empirically Verified Turns 33850 & 39237):**
    - Using the Poké Flute from the in-battle Bag menu plays the tune and displays 'All sleeping POKéMON woke up!', awakening all sleepers (player and opponent).
    - Action Economy Cost: Using the flute consumes the player's combat turn, allowing the opponent to execute an attack that turn. Use only when active sweeper cannot act.

- **Proactive Sweeper Retreat Protocol (Safety Margin & Contingency):**
  - Electric Contingency / Immediate Cutoff: If Mewtwo expends its final Psychic PP (reaches 0 PP), immediately initiate a pit-stop after that battle. Never risk an Electric encounter without Mewtwo's Psychic available.
  - Attrition Buffer: If Mewtwo's HP falls below 100 HP from overworld poison, immediately initiate a pit-stop (preserving a safe 40 HP cushion above the 60 HP danger line).
  - Blastoise Margin: If Blastoise HP falls below 70 HP OR if Blastoise (Surf + Ice Beam) combined PP <= 5, trigger an immediate pit-stop.
  - Pit-Stop Execution: Step outside Cerulean Cave to Cerulean City exterior -> Fly to Cerulean Pokémon Center -> Nurse Joy fully heals party (clearing poison, restoring all PP/HP) -> Bike north across bridge to Route 24 -> Surf south into canal -> Re-enter Cerulean Cave 1F.
