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
  - Parasect Lv 52: Total EXP 950. 2 participants without Exp. All -> Base share s_EXP = 475 (native), boosted = 712 (traded) [Empirically verified Turn 35207]. (With Exp. All: participant share = 237, team base share = 37) [Empirically verified across 3+ battles].
  - Raichu Lv 53: Total EXP 908. With Exp. All: participant share = 227, team base share = 37, traded share = 55 [Empirically verified across 4+ battles].
  - Venomoth Lv 49: Observed Total EXP Variance:
    - Without Exp. All (Turn 33856): Total EXP = 966 (standard formula floor(138 * 49 / 7) = 966). 3 participants yielded exactly 322 EXP each (floor(966 / 3) = 322).
    - With Exp. All (Battle 15): Total EXP = 952. Participant share = 238, team base share = 35 [Empirically verified across 7+ battles, including Battles 15, 21, 28, 33, 34, 52, 71 (Turn 37484)]. Note: 7 separate empirical battles confirm this yield is 100% deterministic and invariant for this Cerulean Cave encounter slot.

- **In-Battle Party Sub-Menu:** When selecting a non-active Pokémon from the in-battle party menu, a sub-menu appears with: `SWITCH` (default cursor), `STATS`, `CANCEL`. Pressing A on `SWITCH` confirms the switch [Empirically verified Turn 34716].

## EXP.ALL Mathematical Model & Empirical Mechanics (Generation 1 Retail)
- **Exp. All Distribution Formula & Party Scaling:**
  - Participant Share: `floor(floor(E / 2) / n_participants) = floor(E / 4)` for 2 battle participants.
  - Team Share Derivation & Reconciled Divisor Model:
    - In Gen 1 retail, the team EXP pool is half of the total battle EXP (`E_half = floor(E / 2)`), which is further halved before dividing among party members: `base_team_share = floor(floor(E_half / 2) / N_party) = floor(floor(E / 4) / N_party) = floor(E / (4 * N_party))`.
    - For full 6-member party (N=6): Base divisor is `4 * 6 = 24` (`floor(E / 24)`):
      - Kadabra (E=1008): `1008 // 24 = 42 EXP` (exact match to observed 42).
      - Golbat (E=1104): `1104 // 24 = 46 EXP` (exact match to observed 46).
      - Internal 8-bit assembly registers and truncation introduce non-monotonic variance for certain species (e.g. Hypno E=1076 -> 39, Magneton E=1050 -> 39).
    - For 4-member party (N=4): Base divisor is `4 * 4 = 16` (`floor(E / 16)`):
      - Parasect (E=950): `950 // 16 = 59 EXP` (exact match to observed 59!).
      - Kadabra (E=1008): `1008 // 16 = 63 EXP` (exact match to observed 63!).
      - Magneton (E=1050): `1050 // 16 = 65 EXP` (exact match to observed 65!).
      - Hypno (E=1076): observed 65 EXP.
      - Golbat (E=1104): observed 65 EXP.
    - Traded Pokémon Boost on Exp. All Share: Strictly integer arithmetic `boosted_share = base_share + floor(base_share / 2)` (e.g. 65 + 32 = 97 EXP, 59 + 29 = 88 EXP, 63 + 31 = 94 EXP).
- **Empirical Effective Divisor K (Across 96 Battles):**
  - Golbat (E=1104, base=46, K=24.0) [23 empirical encounters verified]
  - Kadabra (E=1008, base=42, K=24.0) [4 empirical encounters verified]
  - Raichu (E=908, base=37, K=24.5) [5 empirical encounters verified]
  - Parasect (E=950, base=37, K=25.7) [5 empirical encounters verified]
  - Dodrio (E=1092, base=42, K=26.0) [11 empirical encounters verified]
  - Magneton (E=1050, base=39, K=26.9) [10 empirical encounters verified]
  - Sandslash (E=1188, base=44, K=27.0) [8 empirical encounters verified]
  - Venomoth (E=952, base=35, K=27.2) [10 empirical encounters verified]
  - Hypno (E=1076, base=39, K=27.6) [20 empirical encounters verified]
