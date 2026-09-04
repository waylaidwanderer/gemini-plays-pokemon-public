# Combat Mechanics & Tactical Guidelines

## Turn Priority & Item Mechanics
- Move Execution Order: Strictly determined by Speed stat under neutral conditions. Higher Speed acts first. When Speed stats are identical (Speed tie), turn priority is resolved randomly (50/50) each turn (empirically confirmed Turns 456 & 458: Sheldon at Speed 15 and Trainer Weedle Lv 9 alternated move priority under neutral conditions, demonstrating an empirical Speed tie).
- In-Battle Item Priority: Bag item usage (e.g. Potion) possesses top execution priority (+1 priority), resolving at the beginning of the turn before any Pokémon moves, irrespective of Speed.
- Item Effects: Potion restores exactly 20 HP to the designated Pokémon.
- Potion Tactical Doctrine: Conserve Potions unless active Pokémon HP <= 5 and opponent possesses lethal KO potential on the current turn. When HP <= 5 and enemy attack cannot be prevented by outspeeding and knocking out the target, item priority ensures 100% survival.

## Battle Menu & Cursor Memory
- Move Selection Cursor Memory: During consecutive attack turns within a single battle, the move menu cursor retains its position from the previously confirmed attack (e.g. executing Bubble from Slot 3 leaves the cursor at Slot 3 on the following turn). It does NOT automatically reset to Slot 1.
- Testing Boundary: Empirically verified across consecutive attack executions with Bubble, Tail Whip, and Tackle, AND verified to persist after navigating through the ITEM submenu to use a Potion (Turn 399). Behavior after PKMN submenu or aborting actions remains unverified.
- Battle Initialization Reset: At the start of a new battle, the move selection cursor resets to Slot 1 (Tackle), regardless of what move was used in previous encounters. Verified on Turn 437.

## Stat Stage Modifiers
- Tail Whip: Decreases target Defense by 1 stage per application (Stage -1 = approx. 2/3 Defense, Stage -2 = approx. 1/2 Defense). Verified: Lv 6 Weedle took 11-12 damage from Tackle at -1 Defense vs ~6-8 at neutral Defense.
- Bubble Secondary Effect: Has a chance to lower target Speed by 1 stage (observed to drop enemy Weedle's Speed on Turns 381, 385, and 462).
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

## Enemy Offensive Damage Bounds against Sheldon (Defense 17)
- Wild Route 1-2 targets (Lv 3-4 Pidgey Gust / Rattata Tackle): 3-4 HP damage.
- Forest Bug Pokémon (Lv 6 Weedle Poison Sting / Caterpie Tackle): 2-3 HP damage (Critical hit deals ~4 HP).
- Status Affliction Risk: Poison Sting inflicts Poison on hit (~20-30% chance). Poison deals periodic 1/16 max HP damage in battle and 4 HP every 4 overworld steps.

## Experience & Growth Curves
- Level Milestones (Medium-Slow Curve):
  - Level 7: 318 EXP
  - Level 8: 482 EXP (Learns Bubble, fills Slot 3)
  - Level 9: 703 EXP
- Defeat Yields:
  - Wild Rattata Lv 3: 24 EXP | Lv 4: 32 EXP
  - Wild Pidgey Lv 3: 23 EXP | Lv 4: ~23-28 EXP
  - Trainer Weedle Lv 6: 66 EXP
  - Trainer Caterpie Lv 6: ~66 EXP
  - Trainer Weedle Lv 9: 99 EXP
- Level 10 Stats: Max HP 29, Attack 17, Defense 20, Speed 17, Special 17 (reached on Turn 466)
- Battle Move Menu Layout: The 4 moves are arranged in a single vertical 4-line list (Slot 1 at top, Slot 2 second, Slot 3 third, Slot 4 fourth), NOT a 2x2 grid. Pressing "Down" from Slot 1 moves to Slot 2, not Slot 3. To reach Slot 3 from Slot 1 requires pressing "Down" twice.
- Trainer Diglett Lv 11: 190 EXP