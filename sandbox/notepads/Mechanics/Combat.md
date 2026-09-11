# Combat Mechanics (Generation 1 Retail)

## Battle UI & Controls
- **Start Menu Cursor Memory:** In Generation 1 retail, the overworld Start menu remembers the last selected menu item across overworld sessions (empirically confirmed Turns 3985-3986: hovering on POKéMON causes the Start menu to re-open on POKéMON on the next press).
- **Move Cursor Memory:** Within the same battle, the move selection menu remembers the last selected move slot across turns and across enemy Pokémon faintings (empirically confirmed Turn 3049 vs Rival RED: Slot 3 Bubblebeam remained selected after Pidgeotto fainted). At the start of each new battle, the move cursor always re-initializes to Slot 1 (empirically confirmed Turns 3144, 3160, 3175).
- **Shift Style Prompt:** When an opposing Pokémon faints in trainer battles, the game asks "Will BLUE change POKéMON?". Default cursor is YES. Pressing B automatically selects NO and retains current Pokémon.
- **Top Battle Menu:** Pressing B on the main battle menu (`FIGHT`, `ITEM`, `PKMN`, `RUN`) does nothing and cannot accidentally trigger unwanted actions.
- **Trainer Battles:** Fleeing (`RUN`) is impossible in trainer battles.
- **Bag Menu Navigation:** The Item Bag scrolling list does NOT wrap vertically from top to bottom (pressing Up at Item 1 stops at Item 1 and does not wrap to CANCEL, empirically confirmed Turn 3069).
- **Party Menu Cursor Memory:** In Generation 1 retail, the overworld Party Pokémon menu remembers the last selected party member across overworld sessions (empirically confirmed Turn 8260).
- **Battle Reset of Menu Cursor Memory:** Entering and exiting any battle (wild or trainer) immediately re-initializes both the overworld Start menu cursor to Slot 1 (POKéDEX) and the Bag menu cursor to Slot 1 (OLD ROD). Menu cursor persistence only applies across consecutive overworld menu sessions without intervening battles [Empirically confirmed Turns 12354-12357].

## Stat & Damage Mechanics
- **Special Stat:** Gen 1 combines Special Attack and Special Defense into a single Special stat.
- **Physical Types:** Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost.
- **Special Types:** Water, Grass, Fire, Ice, Electric, Psychic, Dragon.
- **STAB:** Same-Type Attack Bonus provides a 1.5x multiplier to damage.
- **Priority:** Quick Attack has +1 priority.

## Obedience
- **Original Trainer Pokémon:** Starter Pokémon and Pokémon caught by the player never disobey, regardless of level or badge count. Badge obedience limits (e.g. Cascadebadge Lv 30) only apply to traded / outsider Pokémon.


## Verified Battle Mechanics & Engine Findings
- **Pre-Poison / Status Shielding Mechanic:** In Generation 1 retail, a Pokémon with an active major status condition (PSN, PAR, SLP, BRN, FRZ) is completely immune to all other major status conditions. Specifically, entering battle with standard PSN (dealing flat 1/16 HP = 10 HP/turn) shields the Pokémon from lethal compounding Badly Poisoned (Toxic) and Sleep (Hypnosis). Note: During the Koga gym battle (Turns 12161-12176), Koga's team was swept before selecting Toxic/Hypnosis directly, so this principle relies on standard Gen 1 engine status exclusivity rather than direct combat execution against those specific moves.