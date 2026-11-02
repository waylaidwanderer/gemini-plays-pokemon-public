# Location: Sootopolis Gym

## Overview
The 8th and final Pokémon Gym in Hoenn, specializing in Water-type Pokémon.
- Gym Leader: Juan (former mentor of Wallace, took over as Gym Leader).
- Badge: Rain Badge (allows HM07 Waterfall outside of battle, commands all Pokémon regardless of level).
- TM: TM03 Water Pulse.

## Gym Puzzle Mechanic: Ice Floors
- The Gym consists of three tiers of ice tile puzzles.
- Stepping on an ice tile turns it cracked.
- Stepping on all ice tiles in a tier exactly once (Hamiltonian path) raises the staircase to the next platform.
- Stepping on an already-cracked tile shatters the ice, causing the player to fall into the basement filled with trainers.
- A ladder in the basement returns to the start of the tier to retry.

## Progression Checklist - Sootopolis Gym
1. [x] Unlocked Sootopolis Gym entrance by quelling Groudon/Kyogre and speaking with Wallace (Turn 18699)!
2. [x] Entered Sootopolis Gym entrance lobby at (8, 25) (Turn 18700)!
3. [x] Consult Gym Guide at (7, 24) (Turn 18701).
4. [x] Solve Tier 1 Ice Puzzle (Turn 18712)!
5. [x] Solve Tier 2 Ice Puzzle (Turn 18831)!
6. [x] Solve Tier 3 Ice Puzzle (Turn 18884)!
7. [ ] Defeat Gym Leader Juan for the Rain Badge and TM03 Water Pulse.

## Discovered Topography & Navigation
- Entrance Lobby (rows 20..26, cols 5..11):
  - Entrance/Exit mat at (8..9, 25).
  - Gym Guide stationed at (7, 24).
  - Statues at (6, 23..24) and (10, 23..24).
  - Basement return ladder at (10, 22).
  - Central staircase up to Tier 1 at (8..9, 21..22).
- Tier 1 Ice Puzzle (rows 17..19, cols 7..9):
  - 3x3 grid with 2 rock obstacles at (9, 19) and (7, 17). Total: 7 ice tiles.
  - Start tile: (8, 19) from stairs at (8, 20).
  - Exit tile: (8, 17) leading up to stairs at (8, 16).
  - Verified Hamiltonian Path: Up -> Left -> Up -> Right -> Right -> Up -> Left -> Up to (8, 16).
- Tier 2 Ice Puzzle (rows 12..14, cols 5..11):
  - 7x3 grid with 2 rock obstacles at (6, 13) and (10, 13). Total: 19 ice tiles.
  - Start tile: (8, 14) entered from stair landing at (8, 15).
  - Exit tile: (8, 12) leading up to Tier 3 stairs at (8, 11).
  - Verified Hamiltonian Path: Up -> Left x3 -> Up x2 -> Right x2 -> Down -> Right x2 -> Down -> Right x2 -> Up x2 -> Left x3 -> Up to (8, 11).
- Tier 3 Ice Puzzle (rows 6..9, cols 3..13):
  - 11x4 grid with 6 rock obstacles at (5, 6), (9, 7), (12, 7), (4, 8), (7, 8), (11, 9). Total: 38 ice tiles.
  - Start tile: (8, 9) entered from stair landing at (8, 10).
  - Exit tile: (8, 6) leading up to Juan's staircase at (8, 5..3).
  - Verified Hamiltonian Path: Up -> Left x5 -> Up x3 -> Right -> Down -> Right -> Down -> Right -> Up x2 -> Right -> Down -> Right -> Down -> Right -> Down -> Right -> Up -> Right x2 -> Down -> Right -> Up x3 -> Left x2 -> Down -> Left -> Up -> Left x2 to (8, 6) -> Up to stairs!
## Basement Floor (Under Ice)
- Falling through cracked ice lands on snow platforms in the basement (dropped to 8, 12).
- Ice chutes connecting platforms are strictly ONE-WAY DOWNWARD slides (cannot be climbed).
- Trainers are stationed on snow platforms and challenge when stepping into their line of sight.
- Southern slide at (8, 14..16) leads down toward the southern platform where the return ladder to the entrance lobby is located.
- Defeated Lady Daphne (Luvdisc Lv 39 x2) & Pokéfan Annika (Feebas Lv 39 x2) in Double Battle at (8, 13) on Turn 18754. Prize: ¥10,920. Lilz leveled to Lv 29!
- Defeated Lass Andrea (Luvdisc Lv 40) at (7, 17) on Turn 18764. Prize: ¥640.
- Return ladder clearly located on southern basement platform at (11, 22).
- Defeated Beauty Connie (Goldeen Lv 40) at (9, 19) on Turn 18776. Prize: ¥3,200.