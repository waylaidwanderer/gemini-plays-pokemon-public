# Combat Mechanics & Tactical Guidelines

## Turn Priority & Item Mechanics
- Move Execution Order: Strictly determined by Speed stat under neutral conditions. Higher Speed acts first. When Speed stats are identical (Speed tie), turn priority is resolved randomly (50/50) each turn.
- In-Battle Item Priority: Bag item usage (e.g. Potion) possesses top execution priority (+1 priority), resolving at the beginning of the turn before any Pokémon moves, irrespective of Speed.
- Item Effects: Potion restores exactly 20 HP to the designated Pokémon.
- Potion Tactical Doctrine: Conserve Potions unless active Pokémon HP <= 5 and opponent possesses lethal KO potential on the current turn. When HP <= 5 and enemy attack cannot be prevented by outspeeding and knocking out the target, item priority ensures 100% survival.

## Battle Menu & Cursor Memory
- Move Selection Cursor Memory: During consecutive attack turns within a single battle, the move menu cursor retains its position from the previously confirmed attack (e.g. executing Bubble from Slot 3 leaves the cursor at Slot 3 on the following turn). It does NOT automatically reset to Slot 1.
- Move Selection Cursor Memory across Enemy Sendouts: Within a single trainer battle, when the opponent sends out a new Pok�mon after a faint, the move menu cursor retains its position from the previously confirmed attack rather than resetting to Slot 1 (empirically verified on Turn 1815: cursor was at Slot 4 WATER GUN after KOing Rattata with Water Gun on Turn 1812).
- Testing Boundary: Empirically verified across consecutive attack turns with Bubble, Tail Whip, and Tackle, AND verified to persist after navigating through the ITEM submenu to use a Potion. Behavior after PKMN submenu or aborting actions remains unverified.
- Battle Initialization Reset: At the start of a new battle, the move selection cursor resets to Slot 1 (Tackle), regardless of what move was used in previous encounters.
- Main Battle Menu Cursor Memory: The primary 4-choice battle menu (FIGHT, PKMN, ITEM, RUN) retains its position from the previously confirmed action. Specifically, using an Item leaves the cursor on ITEM on subsequent turns, rather than resetting to FIGHT.
- Battle Bag Menu Cursor Memory: Opening the ITEM menu during battle retains the cursor position from the previously confirmed item (empirically verified on Turn 1195: cursor was on POKé BALL at Slot 2 after using a Poké Ball on Turn 1192).
- Battle Move Menu Layout: The 4 moves are arranged in a single vertical 4-line list (Slot 1 at top, Slot 2 second, Slot 3 third, Slot 4 fourth), NOT a 2x2 grid. Pressing "Down" from Slot 1 moves to Slot 2. Pressing "Down" from Slot 4 wraps around to Slot 1. Pressing "Up" from Slot 1 wraps around to Slot 4. It does NOT clamp at the boundaries.
- Shift Mode Switch Prompt: In Gen 1, the switch prompt ('Will <PLAYER> change POKéMON?') defaults the cursor to YES. Pressing 'B' immediately declines the prompt (acts as NO) without needing to navigate down.
## Stat Stage Modifiers
- Tail Whip: Decreases target Defense by 1 stage per application (Stage -1 = approx. 2/3 Defense, Stage -2 = approx. 1/2 Defense). Verified: Lv 6 Weedle took 11-12 damage from Tackle at -1 Defense vs ~6-8 at neutral Defense.
- Bubble Secondary Effect: Has a chance to lower target Speed by 1 stage.
- String Shot: Lowers target Speed by 1 stage.

## Verified Damage Ranges & Combat Bounds
- Sheldon (Squirtle Lv 7-8, Attack 13-14, Defense 15-17, Special 13-15):
  - Tackle (Normal, Physical, Power 35, Acc 95%):
    - Against neutral Lv 3-4 wild targets (Pidgey, Rattata): 6-8 HP damage (~35-50% max HP).
    - Against -1 Defense Lv 6 targets: 11-12 HP damage (~60% max HP).
  - Bubble (Water, Special, Power 20 + STAB = 30, Acc 100%):
    - Against neutral Lv 6 Bug/Poison (Weedle): ~8-9 HP damage (~45% max HP).
    - Against neutral Lv 6 Bug (Caterpie): ~15-16 HP damage (~75-80% max HP).
  - Critical Hits: Deal approximately double regular damage, ignoring positive defense stages.
- Sheldon Lv 10-11 Combat Bounds (Attack 17-18, Defense 20-22, Special 17-19):
  - Bubble vs Lv 11 Diglett (Ground, Special ~16): Deals 20-22 damage.
  - Bubble vs Lv 11 Sandshrew (Ground, Special ~15): Deals 16-18 damage (~50% max HP).
  - Enemy Diglett Lv 11 Scratch vs Defense 20: 5 damage on normal hit, 8 damage on critical hit.
  - Enemy Sandshrew Lv 11 Scratch vs Defense 22: 9 damage on critical hit.
  - Enemy Sandshrew Lv 11 Scratch vs Sheldon (Defense 37): 3 HP damage.
  - Bubble (Sheldon Lv 17, Special 32) vs Trainer Sandshrew Lv 11: deals 22 damage on turn 1, KO on turn 2.
  - Enemy Zubat Lv 11 Leech Life vs Sheldon (Defense 39): 1 HP damage.
  - Bubble (Sheldon Lv 18, Special 33) vs Trainer Zubat Lv 11: deals ~14-16 damage (~55% max HP).
- Enemy Offensive Damage Bounds against Sheldon (Defense 25-27):
  - Trainer Pidgey Lv 9 Gust: 5 HP damage on normal hit, 9-10 HP damage on critical hit.
  - Sand-Attack: lowers accuracy by 1 stage per hit (caps at stage -6).

- Enemy Offensive Damage Bounds against Sheldon (Defense 17):
  - Wild Route 1-2 targets (Lv 3-4 Pidgey Gust / Rattata Tackle): 3-4 HP damage.
  - Forest Bug Pokémon (Lv 6 Weedle Poison Sting / Caterpie Tackle): 2-3 HP damage (Critical hit deals ~4 HP).
  - Status Affliction Risk: Poison Sting inflicts Poison on hit (~20-30% chance). Poison deals periodic 1/16 max HP damage in battle and 4 HP every 4 overworld steps.

## Experience & Growth Curves
- Level Milestones:
  - Level 7: 318 EXP
  - Level 8: 482 EXP (Learns Bubble, fills Slot 3)
  - Level 9: 703 EXP
  - Level 10: Max HP 29, Attack 17, Defense 20, Speed 17, Special 17
  - Level 11: Max HP 31, Attack 18, Defense 22, Speed 18, Special 19
  - Level 12: Stats unverified
  - Level 13: Max HP 35, Attack 20, Defense 25, Speed 20, Special 21
  - Level 14: Max HP 37, Attack 22, Defense 27, Speed 22, Special 23
  - Level 15: Max HP 39, Attack 23, Defense 29, Speed 23, Special 24 (Learns Water Gun, fills Slot 4)
  - Level 16 (Squirtle): Max HP 41, Attack 24, Defense 30, Speed 24, Special 25
  - Level 16 (Wartortle): Max HP 46 (Current HP scaled to 34 / 46)
  - Level 17: Max HP 49, Attack 31, Defense 37, Speed 31, Special 32
  - Level 18: Max HP 51, Attack 32, Defense 39, Speed 33, Special 33
  - Level 19: Max HP 54, Attack 34, Defense 41, Speed 34, Special 35
  - Level 20: Max HP 56, Attack 36, Defense 44, Speed 36, Special 37
  - Level 21: Max HP 58, Attack 38, Defense 46, Speed 38, Special 39
  - Level 22: Max HP 61, Attack 39, Defense 48, Speed 39, Special 41

## Defeat Yields
- Wild Rattata Lv 3: 24 EXP | Lv 4: 32 EXP
- Wild Pidgey Lv 3: 23 EXP | Lv 4: ~23-28 EXP
- Trainer Weedle Lv 6: 66 EXP
- Trainer Caterpie Lv 6: ~66 EXP
- Trainer Pidgey Lv 9: 105 EXP
- Trainer Weedle Lv 9: 99 EXP
- Trainer Kakuna Lv 9: 136 EXP
- Trainer Kakuna Lv 11: 166 EXP
- Trainer Caterpie Lv 9: 102 EXP
- Trainer Metapod Lv 9: 138 EXP
- Trainer Metapod Lv 11: 169 EXP
- Trainer Caterpie Lv 10: 112 EXP
- Trainer Caterpie Lv 11: 124 EXP
- Trainer Rattata Lv 10: 121 EXP
- Trainer Nidoran♂ Lv 10: 127 EXP
- Trainer Rattata Lv 11: 133 EXP
- Trainer Raticate Lv 16: 397 EXP
- Trainer Weedle Lv 10: 111 EXP
- Trainer Weedle Lv 11: 121 EXP
- Trainer Diglett Lv 11: 190 EXP
- Trainer Sandshrew Lv 11: 219 EXP
- Trainer Zubat Lv 11: 126 EXP
- Trainer Zubat Lv 12: 138 EXP
- Trainer Ekans Lv 12: 159 EXP
- Trainer Oddish Lv 11: 183 EXP
- Trainer Bellsprout Lv 11: 198 EXP
- Trainer Ekans Lv 11: 145 EXP
- Leader Geodude Lv 12: 220 EXP
- Trainer Jigglypuff Lv 14: 228 EXP
- Leader Onix Lv 14: 324 EXP
## Party Member Reference: Rocky (Geodude)
- Level 8 Caught Stats: Max HP 26, Attack 19, Defense 22, Speed 9, Special 11
- Moves: Tackle (PP 35/35)
- EXP: 314 total, 105 to Lv 9 (Medium Slow experience curve: 419 EXP at Lv 9)