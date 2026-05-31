# Scratchpad for Route 16 Snorlax and HM02 (FLY) Quest
- **Start Turn**: 38245
- **Starting Timestamp**: Sunday, May 31, 2026 at 10:23 AM PDT
- **Last Updated Turn**: 38589

## Snorlax Capture & FLY (HM02) Protocol
- Snorlax is at Route 16 (Map 0_27).
- We will play the Poké Flute to wake up Snorlax, initiate a Level 30 battle, paralyze it with SPARKY's Thunder Wave, weaken it, and capture it using Great Balls when it falls asleep via REST.
- BIRBIE (Pidgeotto L18) has successfully learned FLY on Turn 38493!

## Macro-Routing Plan (BICYCLE & Cycling Road)
- **Problem**: Standing at the western gatehouse, we cannot enter the Cycling Road (Routes 16, 17, 18) on foot. The game strictly requires a BICYCLE to enter this zone, even if Snorlax is cleared.
- **Strategy**:
  5. Once we have the BICYCLE, we will FLY back to Celadon City, walk west to Route 16, wake up Snorlax with the Poké Flute, capture it, and traverse the Cycling Road! (Current Objective)

## Bag Inventory Space Analysis
- Maximum Bag Capacity: 20 item slots.
- Current Inventory: 18 unique item slots occupied (BICYCLE obtained on Turn 38568, replacing BIKE VOUCHER).
- Items in Bag: Awakening, BICYCLE, Elixer, Ether, Great Ball, HM01, HM02, Hyper Potion, Lemonade, Max Ether, Parlyz Heal, Poké Flute, Potion, Rare Candy, Silph Scope, TM29, Town Map, X Accuracy (Total 18 slots).
- Space remaining: 2 slots.

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

## Resources & PP Tracker (Turn 38589)
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

## Paralysis Contingency & Speed Recovery Protocol (Socratic Challenge)
- **Snorlax Body Slam Threat**: Snorlax L30 knows Body Slam, which has a 30% chance to paralyze in Gen 1.
- **Turn 1 Priority**: Pikachu L24 naturally outspeeds Snorlax L30. Therefore, SPARKY will execute THUNDER WAVE on Turn 1 *before* Snorlax can act, paralyzing Snorlax and reducing its Speed to 25% right away.
- **GEMMY Paralysis Contingency**: If our primary tank GEMMY (Blastoise L46) is paralyzed by Body Slam during the capture phase:
  - GEMMY L46 is extremely tanky, and even at 25% Speed (approx. 20-22 Speed), GEMMY still outspeeds the paralyzed Snorlax (approx. 7-10 Speed).
  - Since we have exactly 2 Parlyz Heals, this is sufficient. We will prioritize throwing Great Balls while Snorlax is asleep via REST.
- **Paralysis Speed Recovery Protocol**: If we choose to cure GEMMY's paralysis using a Parlyz Heal during the battle:
  1. Use Parlyz Heal from the Bag to clear the paralysis status icon.
  2. **Crucial Gen 1 Glitch Step**: Immediately switch GEMMY out of battle (e.g., to Rocky or Birbie) and then switch GEMMY back in!
  3. **Reasoning**: In Gen 1, curing paralysis removes the status icon but does NOT automatically recalculate the Speed stat. The 25% Speed penalty persists until the Pokémon is switched out or a stat-modifying move is used. Switching out and back in forces the game engine to recalculate GEMMY's Speed, fully restoring its 100% baseline stat!

## Snorlax Battle Log (Turns 38649 - 38671)
- **Turn 38649**: Initiated battle. SPARKY used Thunder Wave, paralyzing Snorlax.
- **Turn 38650-38660**: SPARKY fainted; switched to GEMMY (Blastoise L46). GEMMY has 129/150 HP.
- **Turn 38667**: Threw 1st GREAT BALL. Snorlax broke free and used Amnesia (Special rose). Great Balls remaining: 29.
- **Turn 38671**: Current state: Snorlax at ~40% HP (yellow/orange), paralyzed. Gemmy is out. Preparing to throw 2nd GREAT BALL.
- **Turn 38690**: Threw 3rd GREAT BALL. Snorlax broke free and used Headbutt, dealing 15 damage to GEMMY (Gemmy at 114/150 HP).
- **Turn 38696**: Opened Bag. Snorlax's HP is in the red zone (tiny sliver). Great Balls remaining: 27. Preparing to throw 4th GREAT BALL.