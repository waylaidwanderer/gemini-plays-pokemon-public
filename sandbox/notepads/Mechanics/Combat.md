# Combat Mechanics & Observations

## Battle Engine & Turn Priority
- Move Order: Determined strictly by Speed stat. Sheldon (Lv 7, Speed 13) consistently outspeeds Route 1 wild Pokémon (Lv 2-4 Rattata/Pidgey).
- Item Priority: Bag item usage (e.g. Potion) executes at turn start before Pokémon moves.

## Strategy
- Route 1: Defeat wild Pidgey/Rattata with Tackle for EXP toward Lv 8 (Bubble).
- Conserve Potions unless HP <= 5.
## Stat Modifiers & Stage Divisors
- Tail Whip: Decreases target Defense by 1 stage per use (-1 stage = 2/3 Defense, -2 stages = 1/2 Defense).
  - Verified: Lv 4 Rattata Tackle dealt 6 damage to Sheldon at -2 Defense vs ~3-4 damage at neutral Defense.

## Damage Ranges (Squirtle Tackle)
- Against Lv 3-4 Route 1 wild targets (neutral): Tackle deals ~6-7 HP per hit (~35-50% max HP), yielding consistent 2-to-3-hit KOs.
- Critical Hits: Double effective level in damage calculation, dealing ~50% bonus damage.

## Verified Encounter Observations (Turns 196-200)
- Enemy: Wild Pidgey (Lv 3) on Route 1.
- Player: Squirtle (SHELDON) Lv 7 (Attack 13, Defense 15, Speed 13, Special 13).
- Tackle Damage: Dealt ~55% on hit 1; regular Tackle dealt ~45% on hit 2 (KO in 2 hits).
- Enemy Attack: Pidgey Gust Critical Hit dealt 3 damage, regular Gust dealt 3 damage (HP 17 -> 11).
- Experience: Awarded 23 EXP upon defeat.

## Verified Encounter Observations (Turns 248-253)
- Enemy: Wild Rattata (Lv 4) on Route 1.
- Player: Squirtle (SHELDON) Lv 7 (Attack 13, Defense 15 -> dropped to stage -2 via Tail Whip).
- Battle Flow:
  - Turn 249: Sheldon Tackle dealt ~40% HP; Rattata used Tail Whip (-1 Def).
  - Turn 250: Sheldon Tackle dealt ~35% HP; Rattata used Tail Whip (-2 Def).
  - Turn 251: Sheldon Tackle dealt ~20% HP (Rattata survived with ~1-2 HP); Rattata Tackle dealt 6 damage to -2 Def Sheldon (HP 11 -> 5).
  - Turn 252: Sheldon Tackle KO'd Rattata!