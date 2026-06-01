# Saffron Silph Co. 2F Verified Layout & Exploration Records (Map 0_207)

## Overview & Coordinates
- **Elevator**: Located at (18, 0)? Wait, let's check map markers: (20, 0) is elevator doors on this map. Let's verify coordinates of elevator on 2F.
- **Stairs**: Stairs Down to 1F at (24, 0), Stairs Up to 3F at (26, 0).
- **Cleared Status**: Under exploration.

## Verified Obstacles & Corridor Collisions
- Standard Silph Co. partitions.
- Card Key Door (SW Room) at (4, 10).
- Card Key Door (NW Room) at (4, 4).
- **Column 22 Partition Wall Bypass**: Row 16 is blocked on column 22 by a solid wall (TYPE_2889). However, Row 12 is a completely open horizontal corridor (TYPE_3fe2) spanning columns 21-28, allowing players to easily bypass the column 22 partition.

## Cleared Trainers & Spawns
- **Rocket Grunt**: Met and defeated at (24, 5) on Turn 38956.
- **Scientist**: Met and defeated at (24, 13) on Turn 41151 (static ☠️ marker defined).
- **Rocket Grunt**: Met and defeated at (16, 11) on Turn 41267 (object 4, static ☠️ marker defined).
- **Scientist Connor**: Standing at (5, 12) in the SW Room of the western compartment. Defeated on Turn 41635 (Grimer L26, Weezing L26, Koffing L26, Weezing L26).

## 2F Western Compartment Systematic Clearance Plan & Socratic Insights
- **Clearance Status**: SW Room cleared.
- **Remaining Steps**:
  1. Investigate the newly discovered warp tile at (9, 15).
  2. Explore the NW Room of the western compartment (rows 1-3, columns 1-8). Check all corners for items or hidden details.
- **Socratic Lesson on Hostage Battle Triggers**:
  - *Observation*: On Turn 41601, we spoke to the NPC at (5, 12) expecting friendly hostage dialogue ("Help! I'm a SILPH employee"), only to be immediately ambushed in a Scientist combat trainer battle.
  - *Analysis*: In Silph Co., Rocket Grunts and Scientists often disguise themselves as friendly employees or hide behind normal overworld dialogue, using deception as a battle trigger.
  - *Safety Protocol*: Always maintain 100% combat readiness (entire party fully healed and PP monitored) before interacting with ANY unverified NPC in a hostile region. Never assume an unverified sprite is safe just because of its visual appearance or initial text.

## Warp Transitions
- **Warp at (13, 3)**: Bidirectional warp connecting to Silph Co. 8F at (3, 15) (Verified Turn 41053).
- **Warp at (27, 15)**: Bidirectional warp connecting to Silph Co. 8F at (11, 5) (Verified Turn 41101).
- **Warp at (3, 3)**: Bidirectional warp connecting to Silph Co. 3F at (27, 3) (Verified Turn 41580).
- **Warp at (9, 15)**: Bidirectional warp connecting to Silph Co. 6F at (23, 3) (Verified Turn 41650).

## Friendly Hostage NPCs (Verified Non-Trainers)
- None (The NPC at (5, 12) who said "Help! I'm a SILPH employee" turned out to be Scientist Connor in disguise, initiating a battle).
## Newly Explored Western Compartment (Columns 0-10)
- **Access**: Accessed via warp at (27, 3) on Silph Co. 3F, which connects directly to (3, 3) on Silph Co. 2F (bidirectional warp verified on Turn 41580).
- **Layout**:
  - Warp tile at (3, 3) (labeled TYPE_dd92).
  - Row 3 is a horizontal corridor spanning columns 1 to 8.
  - Double Card Key electronic doors at (4, 4) and (5, 4).
  - Server rooms/desks on Row 1 (columns 2-8).

## 2F Western Compartment Clearance Completion & Transition Plan (Turn 41674)
- **Clearance Complete**: Both SW and NW rooms of the 2F western compartment are 100% cleared of all combatants, friendly hostages have been logged, and TM36 collected from (10, 1). There are no unvisited rooms, corners, or items left in columns 0-10.
- **Main Elevator Lobby Transition Plan**:
  1. Since a solid wall at column 11 physically isolates the western compartment from the main elevator lobby on 2F, we cannot transition on foot on this floor.
  2. Walk to the warp tile at (3, 3) in the NW Room.
  3. Step on (3, 3) to warp directly to Silph Co. 3F at (27, 3).
  4. From 3F (27, 3), we are in the open eastern section next to the stairs at (26, 0) and (24, 0).
  5. Walk to the elevator at (20, 0) on 3F, or use the stairs, to transition back to the main elevator lobby of 2F (or any other floor) and continue our systematic floor-by-floor sweep!