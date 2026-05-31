# Scratchpad for Route 16 Snorlax and HM02 (FLY) Quest
- **Start Turn**: 38245
- **Starting Timestamp**: Sunday, May 31, 2026 at 10:23 AM PDT
- **Last Updated Turn**: 38524

## Snorlax Capture & FLY (HM02) Protocol
- Snorlax is at Route 16 (Map 0_27).
- We will play the Poké Flute to wake up Snorlax, initiate a Level 30 battle, paralyze it with SPARKY's Thunder Wave, weaken it, and capture it using Great Balls when it falls asleep via REST.
- BIRBIE (Pidgeotto L18) has successfully learned FLY on Turn 38493!

## Macro-Routing Plan (BICYCLE & Cycling Road)
- **Problem**: Standing at the western gatehouse, we cannot enter the Cycling Road (Routes 16, 17, 18) on foot. The game strictly requires a BICYCLE to enter this zone, even if Snorlax is cleared.
- **Strategy**:
  1. [COMPLETED] Use FLY to instantly fly from Route 16 to Cerulean City (Turn 38521).
  2. [COMPLETED] Visit the Cerulean Pokémon Center (Turn 38525) and access the PC terminal (Turn 38531).
  3. [COMPLETED] Withdraw the BIKE VOUCHER from stored items (Turn 38541).
  4. Walk to the Cerulean Bike Shop (located in the southwestern quadrant at (13, 25)) and redeem the BIKE VOUCHER for the BICYCLE (Current Objective).
  5. Once we have the BICYCLE, we will FLY back to Celadon City, walk west to Route 16, wake up Snorlax with the Poké Flute, capture it, and traverse the Cycling Road!

## PC Interaction Protocol (Withdraw BIKE VOUCHER)
1. Approach the PC terminal at (13, 4) in the Pokémon Center. (Completed!)
2. Press A to interact with the PC. (Completed!)
3. Select "GEM's PC" (Item Storage). (Completed!)
4. Select "WITHDRAW ITEM". (Completed!)
5. Find "BIKE VOUCHER" in the list of stored items. (Completed!)
6. Select "BIKE VOUCHER" and press A to withdraw 1x. (Completed!)
7. Select "CANCEL" to log out of the PC. (Completed!)

## Bag Inventory Space Analysis
- Maximum Bag Capacity: 20 item slots.
- Current Inventory: 18 unique item slots occupied (BIKE VOUCHER successfully withdrawn on Turn 38541).
- Items in Bag: Awakening, BIKE VOUCHER, Elixer, Ether, Great Ball, HM01, HM02, Hyper Potion, Lemonade, Max Ether, Parlyz Heal, Poké Flute, Potion, Rare Candy, Silph Scope, TM29, Town Map, X Accuracy (Total 18 slots).
- Space remaining: 2 slots.
- Action: Upon redeeming the BIKE VOUCHER at the Bike Shop, the voucher will be consumed and replaced by the BICYCLE in our inventory, keeping our bag occupancy stable at 18/20 slots! No inventory issues or discarding will occur.

## Post-Bicycle Snorlax Battle Preparation Plan
- **Transition back**: After getting the BICYCLE, we will open our Pokémon menu, select BIRBIE, and use FLY to go to Celadon City.
- **Walk to Route 16**: From Celadon City, we will walk west onto Route 16 (Row 10) to reach the sleeping Snorlax at (26, 10).
- **Team Re-ordering (Crucial Step)**: Before interacting with Snorlax, we must open our Pokémon menu and switch SPARKY (Pikachu L24) to the leading position!
  - **Reason**: We want SPARKY to lead so we can immediately use THUNDER WAVE on Turn 1 to paralyze Snorlax. This secures turn priority and lowers its capture threshold right away.
- **Battle Flow Strategy**:
  1. Turn 1: SPARKY uses THUNDER WAVE on Snorlax.
  2. Turn 2: Switch SPARKY out for GEMMY (BLASTOISE L46). In Gen 1, switching is +6 priority and occurs before Snorlax can act.
  3. GEMMY tanks any of Snorlax's attacks (Headbutt, etc.) effortlessly. We will use GEMMY's BITE or WATER GUN carefully to chip Snorlax's HP down into the red zone.
  4. Once Snorlax's HP is low, it will eventually use REST to heal and fall asleep.
  5. The moment Snorlax is asleep (resting), we will throw Great Balls! Sleep provides a 2.0x catch multiplier.
  6. If Snorlax wakes up, we can chip it again or wait for it to REST again, or just throw Great Balls. The permanent 25% Speed penalty from the initial paralysis will remain active even when Snorlax is awake/asleep, keeping GEMMY faster.

## Gen 1 Rest Status Override Mechanic (Snorlax Capture Prep)
- In Gen 1, Snorlax's REST move restores HP and replaces any current status (like Paralysis) with SLEEP.
- This status transition is highly advantageous for capture because SLEEP provides a 2.0x catch multiplier compared to PARALYSIS's 1.5x.
- However, due to the Gen 1 status override bug, while its status icon is cleared when waking up from REST (restoring catch rate to 1.0x), its 25% Speed penalty is NEVER recalculated and remains permanently throttled for the rest of the battle! Snorlax stays permanently slow.
- Therefore, our optimized strategy is to weaken Snorlax, apply Paralysis to throttle its Speed and keep it stable early, but focus on throwing Great Balls precisely during the window when it is sleeping via REST to leverage the maximum 2.0x catch multiplier.

## Resources & PP Tracker (Turn 38524)
- **GEMMY (BLASTOISE L46)**: HP 144/150
  - DIG PP: 7/10
  - TAIL WHIP PP: 30/30
  - BITE PP: 23/25
  - WATER GUN PP: 14/25
- **BIRBIE (PIDGEOTTO L18)**: HP 55/55
  - GUST PP: 35/35
  - SAND-ATTACK PP: 15/15
  - QUICK ATTACK PP: 30/30
  - FLY PP: 15/15
- **SPARKY (PIKACHU L24)**: HP 57/57
  - THUNDERBOLT PP: 15/15
  - GROWL PP: 40/40
  - THUNDER WAVE PP: 20/20
  - QUICK ATTACK PP: 30/30
- **PETAL (BELLSPROUT L13)**: HP 39/39 (knows CUT, PP 30/30)
- **Great Balls**: 30
- **Hyper Potions**: 10
- **Potions**: 5
- **Poké Flute**: 1/1 (Key Item)
- **Silph Scope**: 1/1 (Key Item)

## Socratic Challenge Empirical Verification (Turns 38406 - 38419)
- **Hypothesis**: The cuttable bush at (34, 9) on Route 16 (Map 0_27) leading to the northern secret path (and FLY) can be accessed and cut *before* waking up or defeating the Snorlax at (26, 10).
- **Testing Method**:
  1. Walked from (29, 10) on Route 16 to (34, 10) on Row 10 (Turns 38407 - 38408).
  2. Turned Up to face the bush at (34, 9) (Turn 38409).
  3. Opened the POKéMON menu, selected PETAL (Bellsprout L13), and used CUT (Turns 38411 - 38417).
- **Result**: The bush at (34, 9) was successfully cleared on Turn 38418, opening access to Row 9, Row 8, Row 7, and Row 6. Snorlax at (26, 10) remains undisturbed and sleeping on the main road.
- **Conclusion**: Yes! The northern secret path leading to HM02 (FLY) is fully accessible *without* having to capture or defeat Snorlax first. This confirms we can obtain FLY immediately!

- **Warp Door Empirical Test (Turn 38461)**: Standing at (9, 6) facing Up, attempted to walk north into (9, 5). Action failed with 0 tiles visited (collided), proving (9, 5) is a solid window/wall tile.
- **Warp Door Empirical Test (Hypothesis)**: The actual entrance door warp to the secret house is at (7, 5). Let's walk to (7, 6) and walk north into (7, 5) to verify.
- **Result (Turn 38471)**: Walked north from (7, 6) into (7, 5) and successfully warped into the Secret House (Map 0_188) at (2, 7). This confirms (7, 5) is the correct entrance warp coordinate.