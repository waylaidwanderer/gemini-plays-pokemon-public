# Saffron City & Silph Co. Systematic Warp-Logging Strategy
- **Silph Co. Entry Turn**: Turn 38843 (Sunday, May 31, 2026)

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
- **Turn 38853**: Stood at (13, 11) in Silph Co. 1F facing Up. Socratic Test: Pressed 'A' on elevator door at (13, 10) on 1F. Resulted in no dialogue or menu, proving the elevator is non-functional or uncallable from 1F. We must find the stairs to proceed.

## Saffron & Silph Co. Resources & PP Tracker (Initialized Turn 38824)
- **SPARKY (PIKACHU Lv 24)**: HP 57/57 | THUNDERBOLT: 15/15, GROWL: 40/40, THUNDER WAVE: 20/20, QUICK ATTACK: 30/30
- **ROCKY (GEODUDE Lv 15)**: HP 41/41 | TACKLE: 35/35, DEFENSE CURL: 40/40
- **BIRBIE (PIDGEOTTO Lv 18)**: HP 55/55 | GUST: 35/35, SAND-ATTACK: 15/15, QUICK ATTACK: 30/30, FLY: 15/15
- **BUGGY (BUTTERFREE Lv 13)**: HP 43/43 | TACKLE: 35/35, STRING SHOT: 40/40, CONFUSION: 25/25
- **GEMMY (BLASTOISE Lv 48)**: HP 109/156 | DIG: 2/10, TAIL WHIP: 30/30, BITE: 14/25, WATER GUN: 25/25
- **PETAL (BELLSPROUT Lv 13)**: HP 39/39 | VINE WHIP: 10/10, GROWTH: 40/40, WRAP: 20/20, CUT: 30/30

## Silph Co. 5F Systematic Search Protocol (Turn 39216)
- **Goal**: Clear all trainers, identify Card Key gates, and find the Card Key item on Silph Co. 5F.
- **Search Pattern**:
  1. Explore the western hallway by walking west on Row 1 from (16, 1) to (3, 1).
  2. Map any Card Key doors ('🚪') and warp tiles ('🌀') in the western rooms.
  3. **Detour Protocol**: Since Scientist Beau at (8, 3) is a solid, impassable obstacle in Gen 1, bypass him by walking Up to (8, 1), Right to column 13 at (13, 1), and then Down column 13 to (13, 5) to explore the southern and central sections.
  4. Track and record any new warps using warp_network_tracker.
  5. Avoid stepping onto any warp tiles until all trainers on the floor are cleared and the Card Key is found.
  6. **Eastern Corridor Bypass & Southern Corridor Routing Plan (Turn 39333)**: We are currently on the west side of the solid column 27 partition wall. The southern corridor (row 16) contains a Poké Ball item at (21, 16) (the potential Card Key), but is blocked directly by the wall at (26, 15). To access row 16, we must backtrack north up column 26 to row 9 (or further up), walk east across column 27, then walk south down column 28 to row 16, and finally walk west to (21, 16).
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
## Combat Readiness & Floor Search Protocol
- **Lead Combat Order**: GEMMY (Blastoise L46) leads for maximum type safety and level advantage. Saffron's enemies (Poison, Ground, Normal) are highly vulnerable to DIG and WATER GUN. SPARKY (Pikachu L24) is held in reserve.
- **Floor Search Protocol**:
  1. **Clear Floor**: Clear all Grunts and Scientists on each newly entered floor first to prevent ambush and gain experience.
  2. **Explore Rooms**: Systematically check every room and container on the current floor before utilizing warp tiles.
  3. **Priority Objectives**: Locate the Card Key (expected on 5F or adjacent floor) to unlock Silph Co.'s electronic doors.
  4. **Map Hygiene**: Immediately define a '🪜' marker for stairs and a '🚪' marker for elevator doors upon discovery.
- **Gen 1 Defeated Sprite Solidity & Trapping Risk**:
  - In Gen 1, defeated trainer sprites remain solid, physical overworld obstacles that never disappear or become passable.
  - Constrain Backtracking: If we defeat a trainer in a narrow 1-tile wide corridor, that trainer permanently plugs that corridor, blocking any future bidirectional backtracking.
  - Positioning Safety Protocol:
    1. When approaching a trainer in a 1-tile wide corridor, NEVER fight them inside the corridor if there is only one exit.
    2. If possible, trigger the battle from a wider chamber or from an angle that leaves at least one parallel passable lane.
    3. If we must fight them, verify that we have already fully searched both sides of the corridor, or that we have an alternative route (e.g., stairs, elevator, or a parallel corridor) to return to the rest of the floor.

- **Turn 39186**: Entered Silph Co. Elevator (Map 0_236) from 4F (20, 0). Attempting to use the elevator to go to 5F to look for the Card Key.

- **Turn 39276**: Socratic Analysis of Southwest Compartment Accessibility
  - Observation: Inspected the west side from (19, 8). Identified a Card Key door at (15, 10) and (15, 11) (TYPE_a83b).
  - Boundary Scan: Column 15 is blocked by solid walls at (15, 9) (TYPE_2889) and (15, 12) (TYPE_2889).
  - Conclusion: The western compartments on rows 10-13 (including columns 5-6) are completely sealed off from the eastern section by this column 15 partition and the Card Key doors. They cannot be bypassed on foot without the Card Key. We must proceed with our eastern and southern search to locate the Card Key first.
- **Turn 39354**: Tested solidity of defeated Rocket Grunt at (28, 2) by pressing Down from (28, 1). Result: Stayed at (28, 1) with zero tiles visited, proving (28, 2) is solid and impassable.
- **Warp Bypass Plan (Turn 39356)**: Walk to (27, 3) to trigger the warp, record destination with warp_network_tracker, and then warp back and step Right to (28, 3) to bypass the Grunt and access the southern corridor (row 16) and item (21, 16).