# Combat Mechanics (Generation 1 Retail)

## Battle UI & Controls
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

## Boss Battle Tactics & Preparation (Audited Turn 2766)
- **Team Utility:**
  - Dux (Farfetch'd Lv 5): Normal/Flying STAB against Grass types, designated Cut user.
  - Fungi (Paras Lv 10): Train to Lv 13 for status powders (Spore line at Lv 27).

## S.S. Anne Empirical Combat Log
- **Rival RED [Turn 3042 - 3056] (S.S. Anne 2F Corridor at 36, 8):**
  - Roster: Pidgeotto Lv 19 (Yield: 459 EXP), Raticate Lv 16 (Yield: 397 EXP), Kadabra Lv 18 (Yield: 558 EXP), Ivysaur Lv 20. Prize: ¥1300.
  - Pre-battle: "Bonjour! BLUE! Imagine seeing you here!...". Defeat: "Humph! At least you're raising your POKéMON!".
  - Combat: Sheldon Lv 31 used Bubblebeam on Pidgeotto (OHKO). Sheldon used Bubblebeam on Raticate (OHKO). Sheldon used Bite on Kadabra (OHKO). Sheldon used Bite on Ivysaur, Ivysaur used Vine Whip (dealt 17 dmg, Sheldon HP 74 -> 57/84), Sheldon used Bite (Ivysaur fainted).
  - Outcome: Decisive victory. Total damage taken: 17 HP. Bubblebeam PP: 15 -> 13. Bite PP: 16 -> 14.

## Vermilion Gym Empirical Combat Log (Turn 3274 - 3287)
- **Rocker [Turn 3274 - 3287] (Vermilion Gym at 3, 8):**
  - Roster: Voltorb Lv 20 (Yield: 441 EXP), Magnemite Lv 20 (Yield: 381 EXP), Voltorb Lv 20 (Yield: 441 EXP). Total EXP: 1263 EXP. Prize: ¥500.
  - Pre-battle: "I'm a lightweight, but I'm good with electricity!". Defeat: "ROCKER: Fried!".
  - Combat: Sheldon Lv 33 used Bubblebeam on Voltorb 1 (OHKO). Sheldon Lv 33 used Bubblebeam on Magnemite (took 3 dmg from Tackle, HP 89 -> 86/89), Sheldon used Bubblebeam (KO, grew to Lv 34, HP 86 -> 88/91, Atk 61, Def 74, Spd 62, Spc 63). Sheldon Lv 34 used Bubblebeam on Voltorb 2 (Critical Hit, OHKO).
  - Outcome: Decisive victory. HP: 88/91. Bubblebeam PP: 20 -> 16/20. Money: ¥21835 -> ¥22335.

- **Sailor [Turn 3292 - 3299] (Vermilion Gym at 0, 10):**
  - Roster: Pikachu Lv 21 (Yield: 369 EXP), Pikachu Lv 21 (Yield: 369 EXP). Total EXP: 738 EXP. Prize: ¥630.
  - Pre-battle: "This is no place for kids!". Defeat: "SAILOR: Wow! Surprised me!".
  - Combat: Sheldon Lv 34 used Bite on Pikachu 1 (OHKO). Sheldon Lv 34 used Bite on Pikachu 2 (OHKO). Sheldon took 0 damage (HP 88/91). Bite PP: 25 -> 23/25.
  - Outcome: Decisive victory. HP: 88/91. Bite PP: 23/25. Money: ¥22335 -> ¥22965.

- **Gentleman [Turn 3302 - 3304] (Vermilion Gym at 9, 6):**
  - Roster: Pikachu Lv 23 (Yield: 403 EXP). Prize: ¥1610.
  - Pre-battle: "When I was in the Army, LT.SURGE was my strict CO!". Defeat: "GENTLEMAN: Stop! You're very good!".
  - Combat: Sheldon Lv 34 used Bubblebeam (OHKO). Sheldon took 0 damage (HP 88/91). Bubblebeam PP: 16 -> 15/20.
  - Outcome: Decisive victory.

- **Gym Leader Lt. Surge [Turn 3612+] (Vermilion Gym):**
  - Opponent Roster: Voltorb Lv 21, Pikachu Lv 18, Raichu Lv 24.
  - Combat: Voltorb used Tackle (dealt 10 dmg, DIGBY HP 36 -> 26/36). DIGBY used Dig (underground dodged Sonicboom, then emerged with super-effective STAB OHKO!). Voltorb fainted.
  - Pikachu used Growl (failed while Digby underground), Surge used X Speed. DIGBY used Dig (super-effective STAB OHKO!). Pikachu fainted.
  - Raichu used Thunderbolt (no effect on Ground), then Surge used X Speed. Raichu used Thundershock (no effect). DIGBY used Dig (super-effective 2HKO!). Raichu fainted. DIGBY grew to Lv 19! Prize: ¥2376. Decisive victory!