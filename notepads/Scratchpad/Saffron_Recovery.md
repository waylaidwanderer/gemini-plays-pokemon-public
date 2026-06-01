# Scratchpad/Saffron_Recovery (Turn 42838)
- Goal: Deposit CARD KEY at Saffron PC to free up one inventory slot, then return to Sabrina to retrieve TM46 Psywave.
- Current Status: Inside PC Deposit menu.
- Discovery:
  - The Game State Information's inventory list is printed ALPHABETICALLY by the harness.
  - The actual game displays items in their true, non-alphabetical bag order.
  - The screen currently shows:
    1. TOWN MAP
    2. PARLYZ HEAL x2 (Cursor is here)
    3. MAX ETHER x1
    4. HM01
    (with a down arrow ▼ indicating more items below).
- Walking Route Plan:
  1. We observed that (7, 27) is blocked by a building roof. (Verified Turn 42818)
  2. Pivot to column 3: walk Left 4 times to (3, 25). (Completed Turn 42819)
  3. Go Down 5 times to (3, 30) to reach the southern pavement street. (Completed Turn 42819)
  4. Go Right 6 times to (9, 30) (directly below the PC door). (Completed Turn 42822)
  5. Go Up to (9, 29) to enter the Saffron Pokémon Center. (Completed Turn 42822)
  6. Access the PC inside, deposit CARD KEY. (In Progress)
  7. Exit Saffron PC and return to Saffron Gym via warp at (34, 3) to get TM46.

## Empirical Verification:
- Turn 42838: Cursor moved to PARLYZ HEAL in deposit list. We will scroll Down to find CARD KEY.

## Socratic Self-Assessment & Reflection (Turn 42763)
1. **Immediate Execution**: Successfully navigated Saffron Gym, registered the Socratic Quest metrics notepad, cleared Saffron City's obsolete markers, and closed menus to walk to the Pokémon Center on foot.
2. **Notepad Hygiene**: Replaced the outdated hypothesis under NW Room 1 in Saffron Gym with the verified (11, 11) connection. Pruned obsolete progress paths from Locations/SaffronCity.
3. **Map Hygiene**: Deleted the duplicate and obsolete Rocket Grunt blockade markers at (13, 11) and (18, 21) in Saffron City as Team Rocket has fled.
4. **Custom Tools**: Identified 3 highly robust custom tools (local_bfs_pathfinder, grind_in_grass, heal_pokemon_at_counter) that are actively functional.
5. **Tool Maintenance**: No broken custom tools left in the codebase; we are actively using standard, verified tools.
6. **Goal Clarity**: Primary goal is clear (Reach Fuchsia City and defeat Koga). Methods (how we retrieve TM46 and heal) are explicitly detailed in this scratchpad.
7. **Error Analysis**: Discovered that Fly map snaps are not straightforward from Pewter to Cerulean, leading to a direct on-foot walking pivot which is highly reliable.