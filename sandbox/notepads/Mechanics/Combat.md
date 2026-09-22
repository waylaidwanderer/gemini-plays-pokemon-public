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

## Stat & Damage Mechanics
- **Special Stat:** Gen 1 combines Special Attack and Special Defense into a single Special stat.
- **Physical Types:** Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost.
- **Special Types:** Water, Grass, Fire, Ice, Electric, Psychic, Dragon.
- **STAB:** Same-Type Attack Bonus provides a 1.5x multiplier to damage.
- **Priority:** Quick Attack has +1 priority.

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
  - Magneton Lv 46: Total EXP 1,050. 2 participants -> Base share `s_EXP = 525` (native), boosted = `787` (traded).
  - Golbat Lv 46: Total EXP 1,116. 2 participants -> Base share `s_EXP = 558` (native), boosted = `837` (traded).
  - Hypno Lv 46: Total EXP 1,076. 2 participants -> Base share `s_EXP = 538` (native), boosted = `807` (traded) [Empirically verified Turn 35570].
  - Kadabra Lv 49: Total EXP 1,008. 2 participants -> Base share `s_EXP = 504` (native), boosted = `756` (traded).
  - Ditto Lv 53: Total EXP 454. 2 participants -> Base share `s_EXP = 227` (native), boosted = `340` (traded).
  - Raichu Lv 53: Total EXP 922. 2 participants -> Base share `s_EXP = 461` (native), boosted = `691` (traded).
  - Sandslash Lv 52: Total EXP 1,202. 2 participants -> Base share `s_EXP = 601` (native) [Empirically verified Turn 35552].
  - Parasect Lv 52: Total EXP 950. 2 participants -> Base share `s_EXP = 475` (native) [Empirically verified Turn 35207].
  - Venomoth Lv 49: Total EXP 966. 3 participants -> Base share `s_EXP = floor(966 / 3) = 322` [Empirically verified Turn 33856].
  - Venomoth Lv 49: Total EXP 966. 2 participants -> Base share `s_EXP = 483` (native) [Empirically verified Turn 35362].

- **In-Battle Party Sub-Menu:** When selecting a non-active Pokémon from the in-battle party menu, a sub-menu appears with: `SWITCH` (default cursor), `STATS`, `CANCEL`. Pressing A on `SWITCH` confirms the switch [Empirically verified Turn 34716].