# Combat Mechanics (Generation 1 Retail)

## Battle UI & Controls
- **Start Menu Cursor Memory:** In Generation 1 retail, the overworld Start menu remembers the last selected menu item across overworld sessions (empirically confirmed Turns 3985-3986: hovering on POKéMON causes the Start menu to re-open on POKéMON on the next press).
- **Move Cursor Memory:** Within the same battle, the move selection menu remembers the last selected move slot across turns and across enemy Pokémon faintings (empirically confirmed Turn 3049 vs Rival RED: Slot 3 Bubblebeam remained selected after Pidgeotto fainted). At the start of each new battle, the move cursor always re-initializes to Slot 1 (empirically confirmed Turns 3144, 3160, 3175).
- **Shift Style Prompt:** When an opposing Pokémon faints in trainer battles, the game asks "Will BLUE change POKéMON?". Default cursor is YES. Pressing B automatically selects NO and retains current Pokémon.
- **Top Battle Menu:** Pressing B on the main battle menu (`FIGHT`, `ITEM`, `PKMN`, `RUN`) does nothing and cannot accidentally trigger unwanted actions.
- **Trainer Battles:** Fleeing (`RUN`) is impossible in trainer battles.
- **Bag Menu Navigation:** The Item Bag scrolling list does NOT wrap vertically from top to bottom (pressing Up at Item 1 stops at Item 1 and does not wrap to CANCEL, empirically confirmed Turn 3069).

## Stat & Damage Mechanics
- **Special Stat:** Gen 1 combines Special Attack and Special Defense into a single Special stat.
- **Physical Types:** Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost.
- **Special Types:** Water, Grass, Fire, Ice, Electric, Psychic, Dragon.
- **STAB:** Same-Type Attack Bonus provides a 1.5x multiplier to damage.
- **Priority:** Quick Attack has +1 priority.

## Obedience
- **Original Trainer Pokémon:** Starter Pokémon and Pokémon caught by the player never disobey, regardless of level or badge count. Badge obedience limits (e.g. Cascadebadge Lv 30) only apply to traded / outsider Pokémon.


- **Party Menu Cursor Memory:** In Generation 1 retail, the overworld Party Pokémon menu remembers the last selected party member across overworld sessions (empirically confirmed Turn 8260).
## Fuchsia Gym Combat Tactics (Leader Koga & Trainers)
- **Opponents:** Poison and Psychic Pokémon (Koffing, Muk, Weezing, Venomoth, Drowzee, Hypno).
- **Physical vs. Special Split:**
  - Koffing & Weezing possess massive physical Defense (Attack 60-90, Defense 95-120). Use Special Water/Ice attacks (Surf / Ice Beam) to bypass their Defense.
  - Muk has high HP and Special, but lower physical Defense. Double-Edge is optimal for securing fast physical knockouts on Muk.
- **Status & Hazard Mitigation:**
  - Koga's signature strategy revolves around Toxic (exponentially compounding Poison damage), Poison Gas, and Minimize/Smokescreen evasion stalls.
  - Retain Full Heals (5 in bag) to immediately purge Toxic/Poison or Sleep before compounding damage threatens Blastoise.
- **PP Conservation:**
  - Blastoise must enter Koga's Gym with fully restored PP (15 Surf, 15 Body Slam, 10 Ice Beam, 15 Double-Edge). Firing moves into Minimize/Smokescreen risks running out of PP and forcing Struggle.
