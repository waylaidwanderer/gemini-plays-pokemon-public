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

- **Empirically Verified Battle EXP Calculations:**

  - Magneton Lv 46: Total EXP 1,050. 2 participants without Exp. All -> Base share s_EXP = 525 (native), boosted = 787 (traded). (With Exp. All (N=6): participant share = 262, team base share = 39) [Empirically verified across 7+ battles, including Battles 13, 22, 62 (Turn 37360)].

  - Golbat Lv 46: Total EXP 1,104. 2 participants without Exp. All -> Base share s_EXP = 552 (native), boosted = 828 (traded). (With Exp. All (N=6): participant share = 276, team base share = 46) [Empirically verified across 18+ battles, including Battles 1, 6-8, 64, 66, 67 (Turn 37419)].

  - Hypno Lv 46: Total EXP 1,076. 2 participants without Exp. All -> Base share s_EXP = 538 (native), boosted = 807 (traded) [Empirically verified Turn 35570]. (With Exp. All (N=6): participant share = 269, team base share = 39) [Empirically verified across 12+ battles, including Battles 4, 11, 63 (Turn 37375)].

  - Kadabra Lv 49: Total EXP 1,008. 2 participants without Exp. All -> Base share s_EXP = 504 (native), boosted = 756 (traded). (With Exp. All (N=6): participant share = 252, team base share = 42) [Empirically verified across 4+ battles, including Battles 2, 16, 25, 72 (Turn 37495)].

  - Dodrio Lv 49: Total EXP 1,092. 2 participants without Exp. All -> Base share s_EXP = 546 (native), boosted = 819 (traded). (With Exp. All (N=6): participant share = 273, team base share = 42) [Empirically verified across 8+ encounters, including Battles 3, 18, 70 (Turn 37468)].

  - Sandslash Lv 52: Total EXP 1,188. 2 participants without Exp. All -> Base share s_EXP = 594 (native), boosted = 891 (traded). (With Exp. All (N=6): participant share = 297, team base share = 44) [Empirically verified across 7+ battles, including Battles 5, 9, 65 (Turn 37396)].

  - Parasect Lv 52: Total EXP 950. 2 participants without Exp. All -> Base share s_EXP = 475 (native), boosted = 712 (traded) [Empirically verified Turn 35207]. (With Exp. All (N=6): participant share = 237, team base share = 37) [Empirically verified across 3+ battles].

  - Raichu Lv 53: Total EXP 908. With Exp. All (N=6): participant share = 227, team base share = 37, traded share = 55 [Empirically verified across 4+ battles].

  - Venomoth Lv 49: Observed Total EXP Variance:

    - Without Exp. All (Turn 33856): Total EXP = 966 (standard formula floor(138 * 49 / 7) = 966). 3 participants yielded exactly 322 EXP each (floor(966 / 3) = 322).

    - With Exp. All (N=6, Battle 15): Total EXP = 952. Participant share = 238, team base share = 35 [Empirically verified across 7+ battles, including Battles 15, 21, 28, 33, 34, 52, 71 (Turn 37484)]. Note: 7 separate empirical battles confirm this yield is 100% deterministic and invariant for this Cerulean Cave encounter slot.



- **In-Battle Party Sub-Menu:** When selecting a non-active Pokémon from the in-battle party menu, a sub-menu appears with: `SWITCH` (default cursor), `STATS`, `CANCEL`. Pressing A on `SWITCH` confirms the switch [Empirically verified Turn 34716].



## EXP.ALL Empirical Distribution & Observed Yields (Generation 1 Retail)

- **Exp. All Distribution & Participant Sharing:**

  - Participant Share: `floor(floor(E / 2) / n_participants) = floor(E / 4)` for 2 battle participants [Empirically verified across 108+ battles].

  - Traded Pokémon Boost on Exp. All Share: Strictly integer arithmetic `boosted_share = base_share + floor(base_share / 2)` (e.g. 65 + 32 = 97 EXP, 59 + 29 = 88 EXP, 63 + 31 = 94 EXP).

- **Empirical Team Base Shares Under N=6 (Full Party):**

  - Golbat (E=1104): 46 EXP [23 empirical encounters verified]

  - Kadabra (E=1008): 42 EXP [4 empirical encounters verified]

  - Dodrio (E=1092): 42 EXP [11 empirical encounters verified]

  - Hypno (E=1076): 39 EXP [20 empirical encounters verified]

  - Magneton (E=1050): 39 EXP [10 empirical encounters verified]

  - Parasect (E=950): 37 EXP [5 empirical encounters verified]

  - Raichu (E=908): 37 EXP [5 empirical encounters verified]

  - Venomoth (E=952): 35 EXP [10 empirical encounters verified]



## Participant Share & Empirical Yields Under N=4 (4-Member Party)

- **Participant Share & Team Yields (2 Participants, N=4 Party):**

  - Participant Share: In retail Gen 1 with Exp. All active, when 2 party members participate in battle, the participant pool is half the total EXP (floor(E / 2)), divided equally between the 2 participants:

    `participant_share = floor(floor(E / 2) / 2) = floor(E / 4)`.

- **Empirically Verified Participant Shares (N=4 Party):**

  - Sandslash Lv 52 (E=1188): Participant share = 297 EXP, Team base share = 74 EXP (Total trainee gain = 371 EXP) [Verified B188 Turn 40059]

  - Golbat Lv 46 (E=1104): Participant share = 276 EXP, Team base share = 65 EXP (Total trainee gain = 341 EXP) [Verified B190 Turn 40077]

  - Dodrio Lv 49 (E=1092): Participant share = 273 EXP, Team base share = 63 EXP (Total trainee gain = 336 EXP) [Verified B189 Turn 40068]

  - Hypno Lv 46 (E=1076): Participant share = 269 EXP, Team base share = 65 EXP (Total trainee gain = 334 EXP) [Verified B191 Turn 40096]

  - Magneton Lv 46 (E=1050): Participant share = 262 EXP, Team base share = 65 EXP (Total trainee gain = 327 EXP) [Verified B192 Turn 40116]

  - Kadabra Lv 49 (E=1008): Participant share = 252 EXP, Team base share = 63 EXP (Total trainee gain = 315 EXP) [Verified B107, B136]

  - Venomoth Lv 49 (E=952): Participant share = 238 EXP, Team base share = 56 EXP (Total trainee gain = 294 EXP) [Verified B99, B110, B122]

  - Parasect Lv 52 (E=950): Participant share = 237 EXP, Team base share = 59 EXP (Total trainee gain = 296 EXP) [Verified B184 Turn 39983]

  - Raichu Lv 53 (E=908): Participant share = 227 EXP, Team base share = 53 EXP (Total trainee gain = 280 EXP) [Verified B146]





## Field Items in Battle

- **In-Battle Poké Flute Usage (Empirically Verified Turns 33850 & 39237):**

  - Using the Poké Flute from the in-battle Bag menu plays the tune and displays 'All sleeping POKéMON woke up!', awakening all sleepers (player and opponent).

  - Action Economy Cost: Using the flute consumes the player's combat turn, allowing the opponent to execute an attack that turn. Use only when active sweeper cannot act.
