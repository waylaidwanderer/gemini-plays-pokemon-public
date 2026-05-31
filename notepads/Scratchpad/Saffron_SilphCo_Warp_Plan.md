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

## Southern Routing & Warp Avoidance Plan (3F)
- **Goal**: Systematically explore the southern rooms/hallways (rows 12-16, columns 18-27) while avoiding premature warp triggers.
- **Warp Location**: There is an active warp tile at (27, 15) in the southeast corner of row 15.
- **Avoidance Strategy**: Restrict horizontal movement on row 15 to columns 18 to 26. Do not step onto (27, 15).
- **Exploration Path**:
  1. From (28, 8), walk Down to (28, 12).
  2. Walk Left to (19, 12).
  3. Walk Down 2 steps to (19, 14) (entering the southern corridor).
  4. Walk East along row 14 to (26, 14) and row 15 to (26, 15) to check for any items or hidden NPCs.
  5. Once verified clear, we can proceed to use the warp tile at (23, 11) or (27, 15) as planned.

## Saffron & Silph Co. Resources & PP Tracker (Initialized Turn 38824)
- **SPARKY (PIKACHU Lv 24)**: HP 57/57 | THUNDERBOLT: 15/15, GROWL: 40/40, THUNDER WAVE: 20/20, QUICK ATTACK: 30/30
- **ROCKY (GEODUDE Lv 15)**: HP 41/41 | TACKLE: 35/35, DEFENSE CURL: 40/40
- **BIRBIE (PIDGEOTTO Lv 18)**: HP 55/55 | GUST: 35/35, SAND-ATTACK: 15/15, QUICK ATTACK: 30/30, FLY: 15/15
- **BUGGY (BUTTERFREE Lv 13)**: HP 43/43 | TACKLE: 35/35, STRING SHOT: 40/40, CONFUSION: 25/25
- **GEMMY (BLASTOISE Lv 47)**: HP 134/153 | DIG: 6/10, TAIL WHIP: 30/30, BITE: 19/25, WATER GUN: 25/25
- **PETAL (BELLSPROUT Lv 13)**: HP 39/39 | VINE WHIP: 10/10, GROWTH: 40/40, WRAP: 20/20, CUT: 30/30

## Silph Co. 3F Systematic Search Protocol (Turn 39035)
- **Goal**: Clear all trainers and map all doors and warps on Silph Co. 3F.
- **Search Pattern**:
  1. Walk west along row 1 from (20, 1) to (16, 1) and explore the western boundary.
  2. Map any Card Key doors ('🚪') and warp tiles ('🌀') in the western rooms.
  3. Head south through column 18-20 vertical passage to explore the southern rooms.
  4. Track and record any warps using warp_network_tracker.
  5. Clear all Grunts/Scientists for EXP before taking any new warp tiles.
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
- **Turn 38908**: Found the stairs on 1F at (26, 0)! Navigating to (26, 1) and walking Up into (26, 0) to transition to Silph Co. 2F.

## Combat Readiness & Floor Search Protocol
- **Lead Combat Order**: GEMMY (Blastoise L46) leads for maximum type safety and level advantage. Saffron's enemies (Poison, Ground, Normal) are highly vulnerable to DIG and WATER GUN. SPARKY (Pikachu L24) is held in reserve.
- **Floor Search Protocol**:
  1. **Clear Floor**: Clear all Grunts and Scientists on each newly entered floor first to prevent ambush and gain experience.
  2. **Explore Rooms**: Systematically check every room and container on the current floor before utilizing warp tiles.
  3. **Priority Objectives**: Locate the Card Key (expected on 5F or adjacent floor) to unlock Silph Co.'s electronic doors.
  4. **Map Hygiene**: Immediately define a '🪜' marker for stairs and a '🚪' marker for elevator doors upon discovery.
- Warp 3: Silph Co. 1F Map 0_181 (26, 0) -> Silph Co. 2F Map 0_207 (24, 1) [Stairs Up]
- Note: Stairs Down on Silph Co. 2F are at (24, 0). Stairs Up to 3F are verified to be at (26, 0) on 2F (Turn 39018).
- Strategic Decision (Turn 38942): Socratic Analysis of Upper Floor Exploration
  - Issue: We unexpectedly warped from 2F (13, 3) to 8F (3, 15).
  - Decision: Warp back to 2F immediately to resume bottom-up floor clearance.
  - Rationale: High risk of encountering locked card-key doors on 8F without the Card Key (expected on 5F or adjacent floors). Exploring out of sequence would result in wasted movement, potential dead-ends, and unnecessary resource depletion.
- **Turn 39053**: Arrived on 3F at (26, 1) from 2F stairs.
- **Turn 39062**: Explored west corridor to (4, 3). Confirmed warp tile at (3, 3) (TYPE_dd92). Confirmed that the room at (8, 5) is blocked on the north by a wall at (8, 4).
- **Turn 39070**: Heading back east to find the vertical passage to the south and clear any trainers.
- **Turn 39138**: Verifying southern/eastern areas of 3F. Approached and spoke to Scientist at (24, 8) (non-combatant NPC). To avoid taking the warp at (23, 11) prematurely, we are walking around it via column 22 down to row 12 to explore the southeast corner (columns 24-28) first.