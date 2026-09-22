# Combat Mechanics (Generation 1 Retail)

## Battle UI & Controls
- **Asleep Move Selection Mechanic:** In Generation 1 retail, selecting FIGHT while the active Pokémon is asleep does NOT open the move selection menu. It immediately triggers the turn, printing '[POKÃ©MON] is fast asleep!' and decrementing the sleep counter [Empirically verified Turn 33848].
- **Start Menu Cursor Memory:** In Generation 1 retail, the overworld Start menu remembers the last selected menu item across overworld sessions (empirically confirmed Turns 3985-3986: hovering on POKÃ©MON causes the Start menu to re-open on POKÃ©MON on the next press).
- **Move Cursor Memory:** Within the same battle, the move selection menu remembers the last selected move slot across turns and across enemy Pokémon faintings (empirically confirmed Turn 3049 vs Rival RED: Slot 3 Bubblebeam remained selected after Pidgeotto fainted). At the start of each new battle, the move cursor always re-initializes to Slot 1 (empirically confirmed Turns 3144, 3160, 3175).
- **Shift Style Prompt:** When an opposing Pokémon faints in trainer battles, the game asks "Will BLUE change POKÃ©MON?". Default cursor is YES. Pressing B automatically selects NO and retains current Pokémon.
- **Top Battle Menu:** Pressing B on the main battle menu (`FIGHT`, `ITEM`, `PKMN`, `RUN`) does nothing and cannot accidentally trigger unwanted actions [Empirically verified repeatedly across battles, e.g. Turns 35895, 35907].
- **Trainer Battles:** Fleeing (`RUN`) is impossible in trainer battles [Empirically verified Turn 58 vs Rival RED].
- **Bag Menu Navigation:** The Item Bag scrolling list does NOT wrap vertically from top to bottom (pressing Up at Item 1 stops at Item 1 and does not wrap to CANCEL, empirically confirmed Turn 3069).
- **Battle Bag Cursor Memory:** Within the same battle, the in-battle Item Bag menu remembers the last selected item slot across combat turns (empirically confirmed Turn 29002 vs Zapdos: selecting ITEM re-opened directly on Slot 11 ULTRA BALL x36 without resetting to Slot 1).
- **Party Menu Cursor Memory:** In Generation 1 retail, the overworld Party Pokémon menu remembers the last selected party member across overworld sessions (empirically confirmed Turn 8260).
- **Battle Reset of Menu Cursor Memory:** Entering and exiting any battle (wild or trainer) immediately re-initializes both the overworld Start menu cursor to Slot 1 (POKÃ©DEX) and the Bag menu cursor to Slot 1. Menu cursor persistence only applies across consecutive overworld menu sessions without intervening battles [Empirically confirmed Turns 12354-12357].
- **Input Buffering Caution Across Battle Transitions:** Rapidly buffering consecutive 'A' presses across battle text, command menus, and move menus can cause the game engine to register premature move confirmations (e.g. selecting Move Slot 1 Double-Edge). Inputs across battle menu transitions should be chunked cleanly with pauses or verified single presses.

## Stat & Damage Mechanics
- **Special Stat:** Gen 1 combines Special Attack and Special Defense into a single Special stat [Empirically verified across all stat screens and damage calculations].
- **Physical Types:** Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost [Standard Gen 1 game engine specification].
- **Special Types:** Water, Grass, Fire, Ice, Electric, Psychic, Dragon [Standard Gen 1 game engine specification].
- **STAB:** Same-Type Attack Bonus provides a 1.5x multiplier to damage [Standard Gen 1 game engine specification].
- **Priority:** Quick Attack has +1 priority [Standard Gen 1 game engine specification].

## Obedience
- **Original Trainer Pokémon:** Starter Pokémon and Pokémon caught by the player never disobey, regardless of level or badge count. Badge obedience limits (e.g. Cascadebadge Lv 30) only apply to traded / outsider Pokémon.

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
  - Magneton Lv 46: Total EXP 1,050. 2 participants without Exp. All -> Base share s_EXP = 525 (native), boosted = 787 (traded). (With Exp. All: participant share = 262, team base share = 39) [Empirically verified across 7+ battles, including Battles 13, 22, 62 (Turn 37360)].
  - Golbat Lv 46: Total EXP 1,104. 2 participants without Exp. All -> Base share s_EXP = 552 (native), boosted = 828 (traded). (With Exp. All: participant share = 276, team base share = 46) [Empirically verified across 18+ battles, including Battles 1, 6-8, 64, 66, 67 (Turn 37419)].
  - Hypno Lv 46: Total EXP 1,076. 2 participants without Exp. All -> Base share s_EXP = 538 (native), boosted = 807 (traded) [Empirically verified Turn 35570]. (With Exp. All: participant share = 269, team base share = 39) [Empirically verified across 12+ battles, including Battles 4, 11, 63 (Turn 37375)].
  - Kadabra Lv 49: Total EXP 1,008. 2 participants without Exp. All -> Base share s_EXP = 504 (native), boosted = 756 (traded). (With Exp. All: participant share = 252, team base share = 42) [Empirically verified across 4+ battles, including Battles 2, 16, 25, 72 (Turn 37495)].
  - Dodrio Lv 49: Total EXP 1,092. 2 participants without Exp. All -> Base share s_EXP = 546 (native), boosted = 819 (traded). (With Exp. All: participant share = 273, team base share = 42) [Empirically verified across 8+ encounters, including Battles 3, 18, 70 (Turn 37468)].
  - Sandslash Lv 52: Total EXP 1,188. 2 participants without Exp. All -> Base share s_EXP = 594 (native), boosted = 891 (traded). (With Exp. All: participant share = 297, team base share = 44) [Empirically verified across 7+ battles, including Battles 5, 9, 65 (Turn 37396)].
  - Parasect Lv 52: Total EXP 950. 2 participants without Exp. All -> Base share s_EXP = 475 (native), boosted = 712 (traded) [Empirically verified Turn 35207]. (With Exp. All: participant share = 237, team base share = 37) [Empirically verified Battles 41, 42, 46].
  - Raichu Lv 53: Total EXP 908. With Exp. All: participant share = 227, team base share = 37, traded share = 55 [Empirically verified Battles 19, 35, 53, 60].
  - Venomoth Lv 49: Observed Total EXP Variance:
    - Without Exp. All (Turn 33856): Total EXP = 966 (standard formula floor(138 * 49 / 7) = 966). 3 participants yielded exactly 322 EXP each (floor(966 / 3) = 322).
    - With Exp. All (Battle 15): Total EXP = 952. Participant share = 238, team base share = 35 [Empirically verified across 7+ battles, including Battles 15, 21, 28, 33, 34, 52, 71 (Turn 37484)]. Note: 6 separate empirical battles confirm this yield is 100% deterministic and invariant for this Cerulean Cave encounter slot.

- **In-Battle Party Sub-Menu:** When selecting a non-active Pokémon from the in-battle party menu, a sub-menu appears with: `SWITCH` (default cursor), `STATS`, `CANCEL`. Pressing A on `SWITCH` confirms the switch [Empirically verified Turn 34716].
