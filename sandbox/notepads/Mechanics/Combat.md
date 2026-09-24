# Combat Mechanics (Generation 1 Retail)



## Battle UI & Controls

- **Asleep Move Selection Mechanic:** In Generation 1 retail, selecting FIGHT while the active Pokémon is asleep does NOT open the move selection menu. It immediately triggers the turn, printing '[POKéMON] is fast asleep!' and decrementing the sleep counter [Empirically verified Turn 33848].

- **Start Menu Cursor Memory:** In Generation 1 retail, the overworld Start menu remembers the last selected menu item across overworld sessions (empirically confirmed Turns 3985-3986: hovering on POKéMON causes the Start menu to re-open on POKéMON on the next press).

- **Move Cursor Memory:** Within the same battle, the move selection menu remembers the last selected move slot across turns and across enemy Pokémon faintings (empirically confirmed Turn 3049 vs Rival RED: Slot 3 Bubblebeam remained selected after Pidgeotto fainted). At the start of each new battle, the move cursor always re-initializes to Slot 1 (empirically confirmed Turns 3144, 3160, 3175).

- **Shift Style Prompt:** When an opposing Pokémon faints in trainer battles, the game asks "Will BLUE change POKéMON?". Default cursor is YES. Pressing B automatically selects NO and retains current Pokémon.

- **Top Battle Menu:** Pressing B on the main battle menu (`FIGHT`, `ITEM`, `PKMN`, `RUN`) does nothing and cannot accidentally trigger unwanted actions [Empirically verified repeatedly across battles, e.g. Turns 35895, 35907].

- **Trainer Battles:** Fleeing (`RUN`) is impossible in trainer battles [Empirically verified Turn 58 vs Rival RED].

- **Bag Menu Navigation:** The Item Bag scrolling list does NOT wrap vertically from top to bottom (pressing Up at Item 1 stops at Item 1 and does not wrap to CANCEL, empirically confirmed Turn 3069).

- **Battle Bag Cursor Memory:** Within the same battle, the in-battle Item Bag menu remembers the last selected item slot across combat turns (empirically confirmed Turn 29002 vs Zapdos: selecting ITEM re-opened directly on Slot 11 ULTRA BALL x36 without resetting to Slot 1).

- **Party Menu Cursor Memory:** In Generation 1 retail, the overworld Party Pokémon menu remembers the last selected party member across overworld sessions (empirically confirmed Turn 8260).

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

- **Native vs. Traded Pokémon EXP Yields:**

  - **Native Pokémon (OT matches player):** Receives exactly the base share `s_EXP`.

  - **Traded / Outsider Pokémon (boosted EXP):** Receives `boosted_EXP = s_EXP + floor(s_EXP / 2)`.

- **Traded Pokémon Boost Formula (Gen 1 Assembly Implementation):**

  - In Generation 1 retail, the 1.5x OT boost multiplier is calculated via integer arithmetic: half of the participant's base share is computed via integer division (`floor(s_EXP / 2)`) and added directly back to `s_EXP`:

    `boosted_EXP = s_EXP + floor(s_EXP / 2)`

  - This explains why integer truncation does not match floating-point multiplication (e.g., base share 525 yields `525 + floor(262.5) = 525 + 262 = 787`, perfectly matching observed in-game yields).

- **Unified Empirical EXP & Yield Lookup Table (Cerulean Cave 1F Encounters):**

| Species | Level | Total EXP (E) | 2 Part. Base Share (floor(E/2)) | N=4 Trainee Share (floor(E/4) + floor(floor(E/2)/4)) | N=4 Traded Share (floor(floor(E/2)/4) * 1.5) | N=6 Trainee Share (floor(E/4) + team) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sandslash | 52 | 1,188 | 594 | 297 + 74 = 371 EXP | 74 + 37 = 111 EXP | 297 + 44 = 341 EXP |
| Golbat | 46 | 1,104 | 552 | 276 + 65 = 341 EXP | 65 + 32 = 97 EXP | 276 + 46 = 322 EXP |
| Dodrio | 49 | 1,092 | 546 | 273 + 63 = 336 EXP | 63 + 31 = 94 EXP | 273 + 42 = 315 EXP |
| Hypno | 46 | 1,076 | 538 | 269 + 65 = 334 EXP | 65 + 32 = 97 EXP | 269 + 39 = 308 EXP |
| Magneton | 46 | 1,050 | 525 | 262 + 65 = 327 EXP | 65 + 32 = 97 EXP | 262 + 39 = 301 EXP |
| Kadabra | 49 | 1,008 | 504 | 252 + 63 = 315 EXP | 63 + 31 = 94 EXP | 252 + 42 = 294 EXP |
| Venomoth | 49 | 952 | 476 | 238 + 56 = 294 EXP | 84 EXP [Verified Screen Turn 42093] | 238 + 35 = 273 EXP |
| Parasect | 52 | 950 | 475 | 237 + 59 = 296 EXP | 59 + 29 = 88 EXP | 237 + 37 = 274 EXP |
| Raichu | 53 | 908 | 454 | 227 + 53 = 280 EXP | 53 + 26 = 79 EXP | 227 + 37 = 264 EXP |
| Ditto | 53 | 461 | 230 | 113 + 22 = 135 EXP | 22 + 11 = 33 EXP | -- |

- **In-Battle Party Sub-Menu:** When selecting a non-active Pokémon from the in-battle party menu, a sub-menu appears with: `SWITCH` (default cursor), `STATS`, `CANCEL`. Pressing A on `SWITCH` confirms the switch [Empirically verified Turn 34716].

## Field Items in Battle

- **In-Battle Poké Flute Usage (Empirically Verified Turns 33850 & 39237):**

  - Using the Poké Flute from the in-battle Bag menu plays the tune and displays 'All sleeping POKéMON woke up!', awakening all sleepers (player and opponent).

  - Action Economy Cost: Using the flute consumes the player's combat turn, allowing the opponent to execute an attack that turn. Use only when active sweeper cannot act.

## Generation 1 Capture Mechanics & Empirical Boundaries
- **Base Catch Rate vs. Actual Full-HP Capture Probability:** In Generation 1 retail, a Pokémon's base catch rate (e.g. 255 for Pidgey, Caterpie, Bellsprout, Weedle) does NOT equate to a 100% guaranteed capture at full HP with a basic Poké Ball. In the Gen 1 capture routine, full-health targets without status conditions face an initial random threshold test (`R1`) where failure leads to a breakout check.
- **Empirical Breakout Verification:** Both wild Pidgey Lv 13 (Turn 42480) and wild Bellsprout Lv 12 (Turn 42586)—both species having maximum BCR 255—broke free from basic Poké Balls at full HP after 3 shakes on Ball 1 before being captured on Ball 2. Full-health basic Poké Ball capture probability for BCR 255 targets is capped at roughly ~65–75%. Ball budgeting must always account for at least 2 Poké Balls per target even for BCR 255 species.