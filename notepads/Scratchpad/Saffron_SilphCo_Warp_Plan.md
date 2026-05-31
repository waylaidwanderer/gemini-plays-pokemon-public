# Saffron City & Silph Co. Systematic Warp-Logging Strategy

## Overview & Cognitive Safeguards
Saffron City and Silph Co. (11 floors) contain a massive, complex network of over 30 warp tiles. Navigating this blindly or relying purely on short-term memory will cause cognitive bloat, backtrack loops, and wasted turns. To prevent this, we will systematically log every warp transition using our specialized custom agent: `warp_network_tracker`.

## Logging Protocol
1. **Identify and Check**: Before stepping on any warp tile, verify our current map ID and coordinate.
2. **Execute and Record**: Step on the warp tile. Once we spawn at the destination, immediately:
   - Call the `warp_network_tracker` agent with `action_type="record_warp"`.
   - Provide `current_map_id`, `current_position` (the warp's origin), and `warp_destination_map_id`, `warp_destination_position` (the spawn location).
3. **Verify in Scratchpad**: Maintain a secondary high-level floor transition index in this scratchpad to maintain quick overworld context.
4. **Route Planning**: When seeking specific objectives (like finding the Card Key on B5F, or reaching Giovanni on 11F), call `warp_network_tracker` with `action_type="plan_warp_route"` to query the database and receive an automated sequence of coordinates to follow.

## High-Level Floor-by-Floor Silph Co. Objectives
- **Target 1**: Obtain the Card Key (traditionally on 5F or adjacent floors).
- **Target 2**: Unlock doors using the Card Key to access locked rooms and valuable items.
- **Target 3**: Defeat Boss Giovanni on 11F to clear Silph Co. Defeating Giovanni here will clear Team Rocket from Saffron City and unlock the Saffron Gym!
- **Target 4**: Defeat Sabrina at Saffron Gym.

## Active Route & Progress Log
- **Turn 38726**: Captured Snorlax at Route 16 (26, 10). Nicknamed SNOOZY and sent to PC Box 1.
- **Turn 38817**: Entered Saffron Gatehouse West (Map 0_76) at (0, 4). Heading east to enter Saffron City.

## Saffron Overworld Entry & Search Protocol
1. **Entry**: Enter Saffron City (Map 0_10) by walking East from Route 7 (19, 10) to spawn at Saffron City (0, 18).
2. **Pathing to Silph Co.**: From (0, 18), navigate east and south to the Silph Co. Head Office entrance door at (18, 21).
3. **Guard Verification**: Confirm that the Team Rocket Grunt previously at (18, 22) has fled (following our victory over Giovanni in the Rocket Hideout).
4. **Entrance**: Enter the Silph Co. building at (18, 21).

## Saffron & Silph Co. Resources & PP Tracker (Initialized Turn 38824)
- **SPARKY (PIKACHU Lv 24)**: HP 57/57 | THUNDERBOLT: 15/15, GROWL: 40/40, THUNDER WAVE: 20/20, QUICK ATTACK: 30/30
- **ROCKY (GEODUDE Lv 15)**: HP 41/41 | TACKLE: 35/35, DEFENSE CURL: 40/40
- **BIRBIE (PIDGEOTTO Lv 18)**: HP 55/55 | GUST: 35/35, SAND-ATTACK: 15/15, QUICK ATTACK: 30/30, FLY: 15/15
- **BUGGY (BUTTERFREE Lv 13)**: HP 43/43 | TACKLE: 35/35, STRING SHOT: 40/40, CONFUSION: 25/25
- **GEMMY (BLASTOISE Lv 46)**: HP 150/150 | DIG: 10/10, TAIL WHIP: 30/30, BITE: 25/25, WATER GUN: 25/25
- **PETAL (BELLSPROUT Lv 13)**: HP 39/39 | VINE WHIP: 10/10, GROWTH: 40/40, WRAP: 20/20, CUT: 30/30
- **Key Healing/Support Items**:
  - GREAT BALL: 20
  - HYPER POTION: 10
  - POTION: 5
  - LEMONADE: 1
  - ELIXER: 1
  - ETHER: 1
  - MAX ETHER: 1
  - PARLYZ HEAL: 2
  - POKé FLUTE: 1 (Infinite-use awake)
- **Turn 38828**: Successfully arrived in Saffron City (Map 0_10) at (0, 18). Planning path to Silph Co. Head Office entrance at (18, 21).
- **Turn 38837**: Discovered that (5, 21) is a solid TYPE_2889 wall blocking direct South movement from (5, 20). Workaround path: Left to (3, 20), Down to (3, 22), then East along Row 22.