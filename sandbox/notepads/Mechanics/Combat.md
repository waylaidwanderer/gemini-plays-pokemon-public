# Combat Mechanics (Generation 1 Retail)



## Battle UI & Controls

- **Asleep Move Selection Mechanic:** In Generation 1 retail, selecting FIGHT while the active Pokémon is asleep does NOT open the move selection menu. It immediately triggers the turn, printing '[POKéMON] is fast asleep!' and decrementing the sleep counter [Empirically verified Turn 33848].

- **Move Cursor Memory:** Within the same battle, the move selection menu remembers the last selected move slot across turns and across enemy Pokémon faintings (empirically confirmed Turn 3049 vs Rival RED: Slot 3 Bubblebeam remained selected after Pidgeotto fainted). At the start of each new battle, the move cursor always re-initializes to Slot 1 (empirically confirmed Turns 3144, 3160, 3175).

- **Shift Style Prompt:** When an opposing Pokémon faints in trainer battles, the game asks "Will BLUE change POKéMON?". Default cursor is YES. Pressing B automatically selects NO and retains current Pokémon.

- **Top Battle Menu:** Pressing B on the main battle menu (`FIGHT`, `ITEM`, `PKMN`, `RUN`) does nothing and cannot accidentally trigger unwanted actions [Empirically verified repeatedly across battles, e.g. Turns 35895, 35907].

- **Trainer Battles:** Fleeing (`RUN`) is impossible in trainer battles [Empirically verified Turn 58 vs Rival RED].

- **Battle Bag Cursor Memory:** Within the same battle, the in-battle Item Bag menu remembers the last selected item slot across combat turns (empirically confirmed Turn 29002 vs Zapdos: selecting ITEM re-opened directly on Slot 11 ULTRA BALL x36 without resetting to Slot 1).

- **Battle Reset of Menu Cursor Memory:** Entering and exiting any battle (wild or trainer) immediately re-initializes both the overworld Start menu cursor to Slot 1 (POKéDEX) and the Bag menu cursor to Slot 1. Menu cursor persistence only applies across consecutive overworld menu sessions without intervening battles [Empirically confirmed Turns 12354-12357].

- **Input Buffering Caution Across Battle Transitions:** Rapidly buffering consecutive 'A' presses across battle text, command menus, and move menus can cause the game engine to register premature move confirmations (e.g. selecting Move Slot 1 Double-Edge). Inputs across battle menu transitions should be chunked cleanly with pauses or verified single presses.



## Stat & Damage Mechanics

- **Psychic vs. Psychic Resistance (Gen 1 Retail):** In Generation 1 retail, Psychic-type Pokémon resist Psychic-type attacks, taking 0.5x damage ('It's not very effective...'). Even with Mewtwo's 254 Special and STAB, non-critical Psychic deals ~65% damage to wild Hypno Lv 46 (Special ~125), requiring a 2-turn KO or a critical hit [Empirically verified across Battles 175 (Turn 39668), 177 (Turn 39692), and 178 (Turn 39702)].

- **Special Stat:** Gen 1 combines Special Attack and Special Defense into a single Special stat [Empirically verified across all stat screens and damage calculations].

- **Physical Types:** Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost [Standard Gen 1 game engine specification].

- **Special Types:** Water, Grass, Fire, Ice, Electric, Psychic, Dragon [Standard Gen 1 game engine specification].

- **STAB:** Same-Type Attack Bonus provides a 1.5x multiplier to damage [Standard Gen 1 game engine specification].

- **Priority:** Quick Attack has +1 priority [Standard Gen 1 game engine specification].



## Obedience

- **Original Trainer Pokémon:** Starter Pokémon and Pokémon caught by the player never disobey, regardless of level or badge count. (Empirically verified across 41,000+ turns: Starter Blastoise SHELDON at Lv 74 and wild-caught Mewtwo OMEGA at Lv 74 obey 100% of commands in all battles without disobedience).
- **Traded / Outsider Pokémon:** Traded Pokémon (e.g. Farfetch'd DUX, OT ELYSSA IDNo 54183) are subject to badge obedience caps (Cascadebadge: Lv 30, Rainbowbadge: Lv 50, Soulbadge: Lv 70, Earthbadge: All Pokémon obey). Verified: With Earthbadge obtained [Turn 15111], all traded Pokémon obey unconditionally up to Lv 100.



## Experience Distribution & Traded Pokémon Boost

- **Multi-Participant EXP Sharing:** When multiple Pokémon participate in defeating an opposing Pokémon (e.g. entering battle and switching out before fainting), the total battle EXP is divided equally among all non-fainted participants via integer division (`s_EXP = floor(total_EXP / num_participants)`).

- **Solo Sweeper Passive EXP.ALL Distribution (Gen 1 Engine):**
  - **Empirical Variance Note:** While the theoretical formula floor(floor(Total_EXP / 2) / N) serves as a baseline, in-game observations reveal integer truncation nuances in the retail assembly routine (e.g., Hypno Lv 46 yields 131 EXP vs predicted 134, Dodrio Lv 49 yields 133 EXP vs predicted 138). Yields should be verified against observed battle text.
  - When a single lead Pokémon sweeps without switching, participant share = `floor(Total_EXP / 2)`.
  - EXP.ALL distributes the remaining half among all party members: `s_expall = floor(floor(Total_EXP / 2) / N)`.
  - Traded Pokémon receive: `s_expall + floor(s_expall / 2)`.

- **Native vs. Traded Pokémon EXP Yields:**

  - **Native Pokémon (OT matches player):** Receives exactly the base share `s_EXP`.

  - **Traded / Outsider Pokémon (boosted EXP):** Receives `boosted_EXP = s_EXP + floor(s_EXP / 2)`.

- **Traded Pokémon Boost Formula (Gen 1 Assembly Implementation):**

  - In Generation 1 retail, the 1.5x OT boost multiplier is calculated via integer arithmetic: half of the participant's base share is computed via integer division (`floor(s_EXP / 2)`) and added directly back to `s_EXP`:

    `boosted_EXP = s_EXP + floor(s_EXP / 2)`

  - This explains why integer truncation does not match floating-point multiplication (e.g., base share 525 yields `525 + floor(262.5) = 525 + 262 = 787`, perfectly matching observed in-game yields).

- **Empirical Solo-Sweeper EXP.ALL Yields (N=4 Party: Solo Lead [Mewtwo / Sheldon], DUX Traded, Inactive Members):**
  - Solo sweep yields are determined strictly by the defeated Pokémon species/level and party size, invariant to which Pokémon acts as the solo sweeper (empirically confirmed: Sheldon lead Turn 43499 yielded identical 553 EXP sweeper / 133 EXP.ALL trainee share vs Dodrio Lv 49).

| Species | Level | Total EXP | Solo Sweeper Share | Native Trainee Share | Traded Trainee Share | Verification Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sandslash | 52 | 1,188 | 601 EXP | 148 EXP | 222 EXP | Verified Turns 43309, 43395, 43414 |
| Golbat | 46 | 1,104 | 558 EXP | 138 EXP | 207 EXP | Verified Turns 43277, 43361, 43371 |
| Dodrio | 49 | 1,106 | 553 EXP | 133 EXP | 199 EXP | Verified Turn 43353 |
| Hypno | 46 | 1,076 | 538 EXP | 131 EXP | 196 EXP | Verified Turn 43318 |
| Magneton | 46 | 1,050 | 525 EXP | 131 EXP | 196 EXP | Verified Turn 43421 |
| Kadabra | 49 | 1,008 | 504 EXP | 126 EXP | 189 EXP | Verified Turn 43516 |
| Venomoth | 49 | 952 | 476 EXP | 119 EXP | 178 EXP | Verified Turn 43340 |
| Parasect | 52 | 950 | 475 EXP | 118 EXP | 177 EXP | Verified Turns 43378, 43405 |
| Raichu | 53 | 908 | 454 EXP | 113 EXP | 169 EXP | Verified Turn 43441 |

- **In-Battle Party Sub-Menu:** When selecting a non-active Pokémon from the in-battle party menu, a sub-menu appears with: `SWITCH` (default cursor), `STATS`, `CANCEL`. Pressing A on `SWITCH` confirms the switch [Empirically verified Turn 34716].

## Field Items in Battle

- **In-Battle Poké Flute Usage (Empirically Verified Turns 33850 & 39237):**

  - Using the Poké Flute from the in-battle Bag menu plays the tune and displays 'All sleeping POKéMON woke up!', awakening all sleepers (player and opponent).

  - Action Economy Cost: Using the flute consumes the player's combat turn, allowing the opponent to execute an attack that turn. Use only when active sweeper cannot act.

## Generation 1 Capture Mechanics & Empirical Boundaries
- **Base Catch Rate vs. Actual Full-HP Capture Probability:** In Generation 1 retail, a Pokémon's base catch rate (e.g. 255 for Pidgey, Caterpie, Bellsprout, Weedle) does NOT equate to a 100% guaranteed capture at full HP with a basic Poké Ball. In the Gen 1 capture routine, full-health targets without status conditions face an initial random threshold test (`R1`) where failure leads to a breakout check.
- **Empirical Breakout Verification:** Across multiple wild trials with maximum BCR 255 targets at full HP with basic Poké Balls:
  - Pidgey Lv 13 (Turn 42480): broke free after 3 shakes on Ball 1; captured on Ball 2.
  - Bellsprout Lv 12 (Turn 42586): broke free after 3 shakes on Ball 1; captured on Ball 2.
  - Weedle Lv 3 (Turn 42694-42724): broke free after 3 shakes on Balls 1, 2, and 3; captured on Ball 4.
  - Caterpie Lv 3 (Turn 42749-42762): broke free after 3 shakes on Balls 1, 2, 3, and 4; captured on Ball 5.
  - Rattata Lv 3 (Turn 43083): captured on Ball 1 with 0 breakouts at full HP.
  Across these N=4 encounters and 12 total ball throws, 9 out of 12 throws resulted in 3-shake breakouts at full HP (observed capture frequency of ~25-35% in this sample size), showing that capture is not guaranteed at full HP and budgeting 3-5 balls per target species is recommended.