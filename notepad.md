# 1. Party Composition & Strategy
- **SPARKY (Pikachu):** Electric Sweeper. Fast, good for paralysis support.
- **SPROUT (Gloom):** Grass/Poison Utility. Good for status effects.
- **THISTLE (Nidoran♀):** Physical Attacker.
- **PIP (Pidgeotto):** Flying Attacker.
- **PARCH (Sandshrew):** Ground Type Wall.
- **SHELLSHOCK (Squirtle):** Water Type. Gift Pokémon, in PC.
- **LUMIN (Clefairy):** Normal Type. In PC.

# 2. Agent Development Log
- **NOTE:** Make better use of existing agents (`explorer_agent`, `progression_blocker_agent`) before creating new ones.

# 3. Current Objective: Vermilion Gym Puzzle
- **Goal:** Find two switches hidden in trash cans to open the door to Lt. Surge.
- **Mechanic:** Finding an incorrect can resets the puzzle, randomizing the switch locations again.
- **Confirmed Mechanic:** The second switch is ALWAYS in a can immediately adjacent (N, S, E, or W) to the first switch. Finding an incorrect can resets both.

# **Gym Puzzle Attempt Log**
- **Attempt 1:** Found first switch at (10, 12). Failed second switch at (8, 12). **PUZZLE RESET.**
- **Attempt 2:** Failed first switch at (6, 12). **PUZZLE RESET.**
- **Attempt 3:** Failed first switch at (4, 12). **PUZZLE RESET.**
- **Attempt 4:** Failed first switch at (2, 12). **PUZZLE RESET.**
- **Attempt 5 (Current):** Failed first switch at (2, 10). **PUZZLE RESET.**

# 4. Completed Milestones
- **Brock (DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Misty (DEFEATED):** Psyduck (Lv 19), Goldeen (Lv 18), Starmie (Lv 21).
- **Rival BLAZe (@ Cerulean City):** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).
- **Rival BLAZe (@ S.S. Anne):** Krabby (Lv 19), Raticate (Lv 20), Weepinbell (Lv 22), Sandshrew (Lv 21), Eevee (Lv 24).
- **S.S. Anne:** All trainers defeated, kitchen puzzle solved, Captain event triggered, HM01 CUT obtained.

# 5. General Gameplay Insights
- **Systematic Exploration:** Prioritize `Reachable Unseen Tiles`.
- **Battle Preparation:** Heal and restore PP before major battles.
- **Game Mechanics:**
    - Poison deals 1 HP damage every 4 steps.
    - Level-capped Pokémon show fake EXP gain.
    - Non-volatile status conditions are cured after trainer battles.
    - PC System: 'SOMEONE's PC' is for Pokémon, 'Gem's PC' is for Items.
    - The S.S. Anne might leave after I get HM Cut (Confirmed, it left).