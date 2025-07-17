# I. Core Principles & Lessons Learned
- **Immediate Action is Non-Negotiable:** Deferring tasks like tool fixes, agent creation, or documentation is a critical failure. All such actions must be performed in the current turn.
- **Systematic Hypothesis Testing:** When faced with a puzzle, I must form single, testable hypotheses and design minimal experiments. I will document each test, its outcome, and my conclusion to avoid repeated failures.
- **Trust But Verify Agents:** Agents provide powerful plans, but they may lack complete information. Follow their plans, but be prepared to pivot and gather more data when a plan fails.

# II. Game Intel
## A. Confirmed ROM Hack Mechanics
- **Type Effectiveness:**
    - Super Effective (2x): Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
    - Not Very Effective (0.5x): Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
    - Immune (0x): Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.

## B. Tile Mechanics & Movement Rules
- **ground:** Standard walkable tile.
- **impassable:** Walls, objects, and other barriers. Cannot be entered.
- **open_gate:** A previously closed gate that is now open and acts as `ground`.
- **closed_gate:** An impassable gate that is currently visible on the screen.
- **gate_offscreen:** A gate (either open or closed) that is not currently visible. Treat as potentially open for pathfinding unless a marker indicates otherwise.
- **warp:** A tile that transports the player to another location.

# IX. Pokémon Mansion Puzzle Log (Agent v1)
## Agent's Strategic Plan
1.  On 1F, press the Switch at (3,6).
2.  Take the warp at (6,11) to 2F.
3.  On 2F, press the Switch at (3,12).
4.  Take the main warp at (7,2) to 3F.
5.  On 3F, press the Switch at (11,6).
6.  Descend by taking the warp at (7,3) to 2F, then the warp at (6,12) on 2F to return to 1F.
7.  On 1F, navigate to the warp at (22,24) to access the basement.
8.  **Hypothesis Test:** To resolve the paradox of the reachable but closed-off western corridor, interact with the wall directly south of the closed Western Entrance Gates at (10,7) and (10,8). This wall may be a hidden passage.
9.  Explore the basement, using the newly discovered hidden passage if necessary, to find and press the Switch at (19,26).
10. Continue exploring the basement to find and press the Switch at (21,4).
11. With the basement switches activated, the Northern Gates at (17,17) & (18,17) should now be open. Proceed through them.
12. Find and collect the Secret Key from the area behind the Northern Gates.
- **hole:** A warp tile that leads to a lower map area.