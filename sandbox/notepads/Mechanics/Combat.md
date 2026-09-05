# Combat Mechanics (Generation 1 Retail)

## Battle UI & Controls
- **Move Cursor Memory:** Within the same battle, the move selection menu remembers the last selected move slot across turns.
- **Shift Style Prompt:** When an opposing Pokémon faints in trainer battles, the game asks "Will BLUE change POKéMON?". Default cursor is YES. Pressing B automatically selects NO and retains current Pokémon.
- **Top Battle Menu:** Pressing B on the main battle menu (`FIGHT`, `ITEM`, `PKMN`, `RUN`) does nothing and cannot accidentally trigger unwanted actions.
- **Trainer Battles:** Fleeing (`RUN`) is impossible in trainer battles.

## Stat & Damage Mechanics
- **Special Stat:** Gen 1 combines Special Attack and Special Defense into a single Special stat.
- **Physical Types:** Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost.
- **Special Types:** Water, Grass, Fire, Ice, Electric, Psychic, Dragon.
- **STAB:** Same-Type Attack Bonus provides a 1.5x multiplier to damage.
- **Priority:** Quick Attack has +1 priority.

## Obedience
- **Original Trainer Pokémon:** Starter Pokémon and Pokémon caught by the player never disobey, regardless of level or badge count. Badge obedience limits (e.g. Cascadebadge Lv 30) only apply to traded / outsider Pokémon.


## Boss Battle Tactics & Preparation (Audited Turn 2766)
- **Lt. Surge (Vermilion Gym):** Roster is Voltorb Lv 21, Pikachu Lv 18, Raichu Lv 24.
  - Threat: Raichu's high Special Thunderbolt threatens Water-types like Sheldon.
  - Hard Counter: Rocky (Geodude Lv 8). Rock/Ground typing provides complete immunity to Electric attacks and resistance to Normal moves (Mega Punch, Quick Attack).
  - Preparation Plan: Teach Rocky TM28 (Dig) and grind to Lv 20-22 for a guaranteed sweep.
- **S.S. Anne Rival RED:** Roster includes Pidgeotto Lv 19, Raticate Lv 16, Kadabra Lv 18, and Ivysaur Lv 20.
  - Lead Sheldon (Wartortle Lv 29) to defeat normal/psychic roster with Bubblebeam/Bite. Switch against Ivysaur.
- **Team Utility:**
  - Dux (Farfetch'd Lv 5): Normal/Flying STAB against Grass types, designated Cut user.
  - Fungi (Paras Lv 10): Train to Lv 13 for status powders (Spore line at Lv 27).
