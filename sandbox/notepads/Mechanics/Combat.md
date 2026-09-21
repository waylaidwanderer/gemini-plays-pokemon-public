# Combat Mechanics (Generation 1 Retail)

## Battle UI & Controls
- **Start Menu Cursor Memory:** In Generation 1 retail, the overworld Start menu remembers the last selected menu item across overworld sessions (empirically confirmed Turns 3985-3986: hovering on POKéMON causes the Start menu to re-open on POKéMON on the next press).
- **Move Cursor Memory:** Within the same battle, the move selection menu remembers the last selected move slot across turns and across enemy Pokémon faintings (empirically confirmed Turn 3049 vs Rival RED: Slot 3 Bubblebeam remained selected after Pidgeotto fainted). At the start of each new battle, the move cursor always re-initializes to Slot 1 (empirically confirmed Turns 3144, 3160, 3175).
- **Shift Style Prompt:** When an opposing Pokémon faints in trainer battles, the game asks "Will BLUE change POKéMON?". Default cursor is YES. Pressing B automatically selects NO and retains current Pokémon.
- **Top Battle Menu:** Pressing B on the main battle menu (`FIGHT`, `ITEM`, `PKMN`, `RUN`) does nothing and cannot accidentally trigger unwanted actions.
- **Trainer Battles:** Fleeing (`RUN`) is impossible in trainer battles.
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
- **Multi-Participant EXP Sharing:** When multiple Pokémon participate in defeating an opposing Pokémon (e.g. entering battle and switching out before fainting), the total battle EXP is divided equally among all participants who did not faint during the battle.
- **Traded Pokémon Boost (OT Multiplier):** Traded Pokémon (different Original Trainer / ID) receive a 1.5x multiplier (boosted EXP) on their earned share.
- **Empirical EXP Verification (Cerulean Cave 1F Wild Battles):**
  - Turn 33501: Wild Lv 46 Magneton defeated by Sailor (traded Seel) + Omega (Mewtwo). Total EXP ~1,049 split 2 ways (524 base each). Sailor earned 787 boosted EXP (524 * 1.5 = 786). Omega earned 525 EXP.
  - Turn 33519: Wild Lv 46 Golbat defeated by Sailor (traded Seel) + Sheldon (Blastoise). Total EXP ~1,116 split 2 ways (558 base each). Sailor earned 837 boosted EXP (558 * 1.5 = 837). Sheldon earned 558 EXP.
  - Turn 33530: Wild Lv 46 Magneton defeated by Sailor (traded Seel) + Omega (Mewtwo). Sailor earned 787 boosted EXP. Omega earned 525 EXP.
  - Turn 33579: Wild Lv 46 Hypno defeated by Sailor (traded Seel) + Sheldon (Blastoise). Total EXP ~1,076 split 2 ways (538 base each). Sailor earned 807 boosted EXP. Sheldon earned 538 EXP.
  - Turn 33589: Wild Lv 49 Kadabra defeated by Sailor (traded Seel) + Sheldon (Blastoise). Total EXP ~1,008 split 2 ways (504 base each). Sailor earned 756 boosted EXP. Sheldon earned 504 EXP.
