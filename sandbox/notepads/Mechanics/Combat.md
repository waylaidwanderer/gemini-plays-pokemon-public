# Combat Mechanics (Generation 1 Retail)

## Battle UI & Controls
- **Move Cursor Memory:** Within the same battle, the move selection menu remembers the last selected move slot across turns and across enemy Pokémon faintings (empirically confirmed Turn 3049 vs Rival RED: Slot 3 Bubblebeam remained selected after Pidgeotto fainted).
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
- **Tactical Preparation Synthesis (Turns 2881 & 2911):**
  - **Lt. Surge Counter:** Rocky (Geodude Lv 8). Rock/Ground typing walls Electric attacks and resists Normal attacks. Plan: Train Rocky to Lv 18–21 and teach TM28 (Dig) for an effortless sweep.
  - **Rival RED Counter:** [Defeated, Turn 3056 - see S.S. Anne Empirical Combat Log below].

- **Team Utility:**
  - Dux (Farfetch'd Lv 5): Normal/Flying STAB against Grass types, designated Cut user.
  - Fungi (Paras Lv 10): Train to Lv 13 for status powders (Spore line at Lv 27).

## Route 6 Empirical Combat Log (Turns 2668 - 2695)
- **Bug Catcher Elijah [Turn 2668]:** Roster: Butterfree Lv 20 (Yield: 685 EXP, Prize: ¥200). Sheldon Lv 28 used Bubblebeam (OHKO).
- **Jr. Trainer ♀ Nancy [Turn 2682]:** Roster: Pidgey Lv 16 (187 EXP), Pidgey Lv 16 (187 EXP), Pidgey Lv 16 (187 EXP). Prize: ¥320. Sheldon used Bubblebeam/Bite.
- **Jr. Trainer ♂ Ricky [Turn 2695]:** Roster: Spearow Lv 16 (198 EXP), Raticate Lv 16 (397 EXP). Prize: ¥320. Sheldon used Bubblebeam/Bite.

## S.S. Anne Empirical Combat Log
- **Gentleman [Turn 2842 - 2850] (Cabin 1 at 11, 4):**
  - Roster: Nidoran♂ Lv 19 (Yield: 243 EXP), Nidoran♀ Lv 19 (Yield: 240 EXP). Prize: ¥1330.
  - Combat: Sheldon Lv 29 used Bubblebeam on Nidoran♂ (Critical Hit, OHKO). Sheldon Lv 29 used Bubblebeam on Nidoran♀ (OHKO). Sheldon took 0 damage (HP 79/79). Bubblebeam PP: 20 -> 18.

- **Youngster Tyler [Turn 2871 - 2875] (Cabin 4 at 11, 8):**
  - Roster: Nidoran♂ Lv 21 (Yield: 270 EXP). Prize: ¥315. Pre-battle: "I love POKéMON! Do you?". Defeat: "Wow! You're great!".
  - Combat: Sheldon Lv 29 used Bubblebeam (Critical Hit, OHKO). Sheldon took 0 damage (HP 79/79). Bubblebeam PP: 18 -> 17.
- **Lass Ann [Turn 2894 - 2908] (Cabin 4 at 13, 11):**
  - Roster: Pidgey Lv 18 (Yield: 211 EXP), Nidoran♀ Lv 18 (Yield: 226 EXP). Prize: ¥270.
  - Pre-battle: "I collected these POKéMON from all around the world!". Defeat: "Oh no! I went around the world for these!".
  - Combat: Pidgey used Quick Attack (dealt 5 dmg, Sheldon HP 79 -> 74/79). Sheldon Lv 29 used Bubblebeam (OHKO). Sheldon used Bubblebeam on Nidoran♀ (OHKO). Sheldon grew to Lv 30 (HP 76/81, Atk 54, Def 65, Spd 54, Spc 56). Bubblebeam PP: 17 -> 15.
- **Fisherman Dale [Turn 2964 - 2977] (2F Cabin 2 at 13, 4):**
  - Roster: Goldeen Lv 17 (Yield: 403 EXP), Tentacool Lv 17 (Yield: 382 EXP), Goldeen Lv 17 (Yield: 403 EXP). Prize: ¥595.
  - Pre-battle: "Check out what I fished up!". Defeat: "FISHERMAN: I'm all out!".
  - Combat: Sheldon Lv 30 used Bite on Goldeen 1 (dealt ~75%, Goldeen flinched). Sheldon used Bite on Goldeen 1 (OHKO). Sheldon used Bite on Tentacool (OHKO). Sheldon used Bite on Goldeen 2 (dealt ~75%, Goldeen used Tail Whip). Sheldon used Bite on Goldeen 2 (OHKO). Sheldon took 0 damage (HP 76/81). Bite PP: 25 -> 21. Bubblebeam PP: 15/20 (conserved).
- **Gentleman [Turn 2978 - 2984] (2F Cabin 2 at 11, 2):**
  - Roster: Pikachu Lv 23 (Yield: 403 EXP). Prize: ¥1610.
  - Pre-battle: "Competing against the young keeps me youthful.". Defeat: "GENTLEMAN: Good fight! Ah, I feel young again!".
  - Combat: Pikachu used Quick Attack (dealt 5 dmg, Sheldon HP 76 -> 71/81). Sheldon Lv 30 used Bite (Pikachu down to ~15%). Sheldon used Bite (OHKO). Sheldon took 5 damage total (HP 71/81). Bite PP: 21 -> 19. Bubblebeam PP: 15/20 (conserved).
- **Gentleman [Turn 2994 - 3005] (2F Cabin 4 at 1, 14):**
  - Roster: Growlithe Lv 17 (Yield: 331 EXP), Ponyta Lv 17 (Yield: 553 EXP). Total EXP: 884. Prize: ¥1190.
  - Pre-battle: "Which do you like, a strong or a rare POKéMON?". Defeat: "GENTLEMAN: I must salute you!".
  - Combat: Sheldon Lv 30 used Water Gun on Growlithe (OHKO). Sheldon Lv 30 used Water Gun on Ponyta (OHKO). Sheldon grew to Lv 31 (HP 74/84, Atk 56, Def 67, Spd 56, Spc 58). Declined Withdraw to preserve moveset. Water Gun PP: 25 -> 23. Bubblebeam PP: 15/20 (conserved). Bite PP: 19/25 (conserved).
- **Lass [Turn 3007 - 3011] (2F Cabin 4 at 2, 12):**
  - Roster: Rattata Lv 18 (Yield: 219 EXP), Pikachu Lv 18 (Yield: 315 EXP). Total EXP: 534. Prize: ¥270.
  - Pre-battle: "I never saw you at the party.". Defeat: "LASS: Take it easy!".
  - Combat: Sheldon Lv 31 used Bite on Rattata (OHKO). Sheldon Lv 31 used Bite on Pikachu (OHKO). Sheldon took 0 damage (HP 74/84). Bite PP: 19 -> 17. Bubblebeam PP: 15/20 (conserved). Water Gun PP: 23/25 (conserved).
- **Rival RED [Turn 3042 - 3056] (S.S. Anne 2F Corridor at 36, 8):**
  - Roster: Pidgeotto Lv 19 (Yield: 459 EXP), Raticate Lv 16 (Yield: 397 EXP), Kadabra Lv 18 (Yield: 558 EXP), Ivysaur Lv 20. Prize: ¥1300.
  - Pre-battle: "Bonjour! BLUE! Imagine seeing you here!...". Defeat: "Humph! At least you're raising your POKéMON!".
  - Combat: Sheldon Lv 31 used Bubblebeam on Pidgeotto (OHKO). Sheldon used Bubblebeam on Raticate (OHKO). Sheldon used Bite on Kadabra (OHKO). Sheldon used Bite on Ivysaur, Ivysaur used Vine Whip (dealt 17 dmg, Sheldon HP 74 -> 57/84), Sheldon used Bite (Ivysaur fainted).
  - Outcome: Decisive victory. Total damage taken: 17 HP. Bubblebeam PP: 15 -> 13. Bite PP: 16 -> 14.

- **Sailor [Turn 3111 - 3128] (B1F Cabin 2 at 2, 11):**
  - Roster: Horsea Lv 17 (Yield: 301 EXP), Shellder Lv 17 (Yield: 352 EXP), Tentacool Lv 17 (Yield: 382 EXP). Total EXP: 1035 EXP. Prize: ¥510.
  - Pre-battle: "My sailor's pride is at stake!". Defeat: "SAILOR: Your spirit sank me!".
  - Combat: Sheldon Lv 31 used Bite on Horsea (took 1 dmg from Bubble, Sheldon grew to Lv 32). Sheldon Lv 32 used Bite on Shellder (took 3 dmg from Tackle), then Bite (Critical Hit, OHKO). Sheldon Lv 32 used Bite on Tentacool (Critical Hit, OHKO).
  - Outcome: Decisive victory. HP: 55/86. Bite PP: 13 -> 9. Money: ¥17190 -> ¥17700.

- **Sailor [Turn 3130 - 3136] (B1F Cabin 2 at 0, 13):**
  - Roster: Shellder Lv 21 (Yield: 436 EXP). Prize: ¥630.
  - Pre-battle: "You know what they say about sailors and fighting!". Defeat: "SAILOR: Right! Good fight, mate!".
  - Combat: Sheldon Lv 32 used Bite (took 4 dmg from Tackle), then Bite (KO). Sheldon took 4 damage total (HP 51 -> 47/86). Bite PP: 8 -> 6/25.
  - Outcome: Decisive victory. HP: 47/86. Bite PP: 6/25. Money: ¥17700 -> ¥18330.
