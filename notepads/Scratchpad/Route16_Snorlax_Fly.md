# Scratchpad for Route 16 Snorlax and HM02 (FLY) Quest
- **Start Turn**: 38245
- **Starting Timestamp**: Sunday, May 31, 2026 at 10:23 AM PDT
- **Last Updated Turn**: 38732

## Snorlax Capture & FLY (HM02) Quest - COMPLETED
- Snorlax at Route 16 (26, 10) was successfully captured on Turn 38726.
- BIRBIE (Pidgeotto L18) successfully learned FLY on Turn 38493.
- BICYCLE successfully obtained on Turn 38568.

## Snorlax Battle Summary (Turns 38649 - 38726)
- **Turn 38649**: Initiated Snorlax battle using Poké Flute. SPARKY paralyzed Snorlax with Thunder Wave before fainting.
- **Turn 38650-38725**: GEMMY (Blastoise) tanked hits and chipped Snorlax. Snorlax used REST twice (falling asleep at full HP each time). We threw Great Balls during the sleep windows.
- **Turn 38726**: Successfully captured Snorlax L30 using a Great Ball while it was asleep! (21 Great Balls remaining).

## Macro-Routing Plan: Fuchsia City vs. Silph Co. (Socratic Challenge)
- **Decision**: We will prioritize immediately flying back to Saffron City to clear Silph Co., rescue the Silph President, defeat Boss Giovanni, and challenge Sabrina at Saffron Gym!
- **Reasoning & Prerequisites**:
  1. We already have the BICYCLE, so we can access Cycling Road whenever we want.
  2. Cleared Saffron Gatekeepers earlier, so we have permanent city access.
  3. Silph Co. is heavily occupied by Team Rocket, and clearing it is the critical milestone that unlocks the Saffron Gym and allows Mr. Fuji's quest to feel narratively complete.
  4. Gemmy is at Level 46, which is very high and capable of leading us through Silph Co. with ease.
- **Next Steps**:
  1. Complete Snorlax capture screens and nickname Snorlax.
  2. Delete Snorlax map marker and clean up notepads.
  3. Walk east to Route 16 / Celadon City and heal at a Pokémon Center (to restore Sparky and Gemmy).
  4. Use FLY to fly to Saffron City (or walk/bike east to Saffron).
  5. Enter Silph Co. and begin systematic warp mapping using `warp_network_tracker`.

## Resources & PP Tracker (Turn 38732)
- **GEMMY (BLASTOISE L46)**: HP 98/150
  - DIG PP: 7/10
  - TAIL WHIP PP: 30/30
  - BITE PP: 22/25
  - WATER GUN PP: 12/25
- **BIRBIE (PIDGEOTTO L18)**: HP 55/55
  - GUST PP: 35/35
  - SAND-ATTACK PP: 15/15
  - QUICK ATTACK PP: 30/30
  - FLY PP: 15/15
- **SPARKY (PIKACHU L24)**: HP 0/57 (Fainted)
  - THUNDERBOLT PP: 15/15
  - GROWL PP: 40/40
  - THUNDER WAVE PP: 19/20
  - QUICK ATTACK PP: 30/30
- **PETAL (BELLSPROUT L13)**: HP 39/39 (knows CUT, PP 30/30)
- **Great Balls**: 21
- **Hyper Potions**: 10
- **Potions**: 5
- **Poké Flute**: 1/1 (Key Item)
- **Silph Scope**: 1/1 (Key Item)

## Paralysis Speed Recovery Protocol
- In Gen 1, curing paralysis removes the status icon but does NOT automatically recalculate the Speed stat. The 25% Speed penalty persists until the Pokémon is switched out or a stat-modifying move is used. Switching out and back in forces the game engine to recalculate Speed, fully restoring its 100% baseline stat.