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

## Saffron & Silph Co. Resources & PP Tracker (Updated Turn 40653)
- **SPARKY (PIKACHU Lv 25)**: HP 59/59 | THUNDERBOLT: 15/15, GROWL: 40/40, THUNDER WAVE: 20/20, QUICK ATTACK: 30/30
- **ROCKY (GEODUDE Lv 15)**: HP 41/41 | TACKLE: 35/35, DEFENSE CURL: 40/40
- **BIRBIE (PIDGEOTTO Lv 18)**: HP 55/55 | GUST: 35/35, SAND-ATTACK: 15/15, QUICK ATTACK: 30/30, FLY: 15/15
- **BUGGY (BUTTERFREE Lv 13)**: HP 43/43 | TACKLE: 35/35, STRING SHOT: 40/40, CONFUSION: 25/25
- **GEMMY (BLASTOISE Lv 50)**: HP 163/163 | DIG: 10/10, TAIL WHIP: 30/30, BITE: 24/25, WATER GUN: 16/25
- **PETAL (BELLSPROUT Lv 13)**: HP 39/39 | VINE WHIP: 10/10, GROWTH: 40/40, WRAP: 20/20, CUT: 30/30

## Combat Readiness & Floor Search Protocol
- **Lead Combat Order**: GEMMY (Blastoise L50) leads for maximum type safety and level advantage.
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

## Systematic Elevator Sweep Routing Protocol (Updated Turn 40653)
- **Objective**: Methodically clear the remaining floors of Silph Co. in ascending order to optimize EXP and resource collection before challenging Giovanni on 11F.
- **Step 1 (6F)**: Cleared.
- **Step 2 (8F)**: Ride the elevator to 8F. Fully explore the floor on foot, unlock all Card Key doors, defeat all trainers, and check for items.
- **Step 3 (10F)**: Cleared (both trainers Travis and Rocket Grunt defeated; TM26 and Rare Candy collected).
- **Step 4 (7F)**: Ride the elevator to 7F. Fully explore and sweep 7F on foot, defeat all trainers, collect items, and log any discovered warps.
- **Step 5 (11F - Final)**: Ride the elevator to 11F. Confront the final Rocket Grunts, unlock the President's boardroom, defeat Boss Giovanni, and rescue the President to claim the Master Ball!

## Socratic Quest Tracking & Agent Status (Turn 40653)
- **Quest Start**: Turn 38843 (Exploration of Silph Co.)
- **Current Turn**: Turn 40653
- **Elapsed Time**: 1810 turns of active navigation and exploration.

## Warp-Sweep Integration Protocol (Turn 40094)
- **Rule**: Step-by-step exploration of Saffron Silph Co. utilizes both elevator sweep and warp mapping.
- **Warp Policy**: When a warp tile is discovered during a floor sweep, do NOT ignore it. Instead:
  1. **Clear Immediate Area**: Ensure there are no active trainers or items in the immediate vicinity of the warp tile before stepping on it.
  2. **Step and Map**: Step on the warp tile and immediately use `warp_network_tracker` to map its bidirectional connection.
  3. **Assess Destination**:
     - If the destination is on an uncleared floor (e.g. 4F), and there are active trainers or items nearby, clear them immediately to secure the landing zone.
     - If the destination is a sealed room (e.g. containing an item or friendly NPC), complete the room's objectives first.
  4. **Resume Sweeping**: Warp back to the origin floor and resume the elevator sweep. This guarantees 100% thorough clearance of all floors without leaving unmapped gaps.

## Silph Co. 10F Floor Clearance Progress (Turn 40653)
- Warp Landing: (13, 7)
- Card Key Doors: (10, 8) and (11, 8) (Unlocked Turn 40173)
- Defeated Scientist Travis at (10, 2) on Turn 40229.
- Defeated Rocket Grunt at (3, 9) on Turn 40537.
- Collected Rare Candy at (4, 14) on Turn 40627.
- Collected TM26 at (2, 12) on Turn 40640.
- **Socratic Route from (3, 7) to Elevator at (18, 0)**:
  1. From (3, 7), walk north 4 steps to (3, 3) to reach the horizontal corridor on row 3: `Up, Up, Up, Up`
  2. Walk east 10 steps along row 3 to (13, 3): `Right * 10`
  3. Walk south 5 steps down column 13 to (13, 8): `Down * 5` (This connects us to the central room)
  4. Walk east 5 steps along row 8 to column 18, reaching (18, 8): `Right * 5`
  5. Walk north 8 steps up column 18 to (18, 0), which is the elevator doors: `Up * 8`
  - *Passability check*: No solid partitions are present on row 8 between columns 13 and 18, making this route fully open and passable!