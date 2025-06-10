# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Level up SPARKY to Lv14.
*   **Tertiary Goal:** Reach Pewter City to enable restocking on Potions.

# Event Triggers & Key Interactions
*   **Rival Battle 1 (Oak's Lab):** Triggered by attempting to leave the lab after receiving Pikachu and Oak's speech.
*   **Pikachu Following:** After the first rival battle, Oak mentions Pikachu dislikes Poké Balls. SPARKY will then follow.
*   **Town Map:** Rival SPB mentioned he'd get one from his sister and tell her not to lend one to me. I should check Rival's house in Pallet Town for a Town Map.
*   **Oak's Parcel:** Obtained from the Viridian City PokeMart clerk. Delivered to Professor Oak.
*   **Pokédex:** Obtained from Professor Oak after delivering the parcel. Mission is to complete it.
*   **Viridian City Old Man (Coffee):** Blocks path west to Route 22. After dialogue about coffee, he moves and offers a catching tutorial (failed).

# Lessons Learned
*   **Ledge Mechanics (CRITICAL - REVISED & REINFORCED):**
    *   Ledges are strictly ONE-WAY: you can only JUMP DOWN them.
    *   You CANNOT move UP onto a ledge from a lower Y-coordinate.
    *   You CANNOT step onto the SIDE of a ledge if you are at a lower Y-coordinate than the ledge itself.
    *   To bypass upward ledges, you MUST find a path AROUND them. This often means going significantly south/west/east, then using specific ground corridors or grass patches to ascend, then moving horizontally above the problematic ledges before jumping down.
*   The sign at (10,28) on Route 1 is IMPASSABLE and acts like a wall.
*   Follower Pokemon can block movement if approached from a non-facing direction, requiring an extra turn to step onto their tile.
*   **Potion Usage (REVISED - ROM HACK CHANGE):** Potions in this ROM hack heal only 10 HP. SPARKY should be healed proactively outside of battle if HP is low and a Pokémon Center isn't immediately accessible, especially before engaging trainers or exploring deep into an area. 
*   **Map Connections:** ALWAYS double-check the *direction* (North, South, East, West) and *destination* of a map connection in the Game State Information before committing to a route.
*   **Trainer Battle Initiation (CRITICAL):** Battles are primarily triggered by entering a trainer's direct line of sight. Observe their facing direction and move onto a tile directly in front of them.
*   **Type Matchups (CRITICAL REMINDER):** Pay closer attention to type matchups. Electric-type moves (like THUNDERSHOCK) are NOT VERY EFFECTIVE against Grass/Poison types like Oddish.
*   **Status Conditions (Poison - CRITICAL):** Poison is a serious threat in Hard Mode. If SPARKY gets poisoned, prioritize reaching a Pokémon Center or using an Antidote ASAP. **DO NOT CONTINUE TO BATTLE OR GRIND WHILE POISONED.** This was a critical error leading to blackouts.
*   **System Warnings (Mixed Buttons):** Consistently receiving 'mixed buttons' warnings. Must ensure `buttons_to_press` contains *only* directional buttons for multi-step movements. Interaction buttons (A, B) or 'tool' calls must be in separate turns.

# Hard Mode Rules
*   Battle Style: Set.
*   No items in battle.
*   Level caps apply (Lt. Surge's cap is 24, Brock's Ace Onix is Lv14, so cap is 14).

# Key Game Changes (ROM Hack)
*   HMs: Forgettable, usable from menu, not storable in PC.
*   All 151 Pokémon obtainable.
*   Trade evos by level.
*   Smarter AI, anti-sweep.
*   Tougher boss fights.
*   Dynamic scaling Gyms 4-6.
*   EXP. All available early.
*   Potions heal 10 HP (observed Turn 2353).

# Agent Development & Pathing Strategy
*   **Active Agents to Test/Utilize:** `exploration_planner`, `map_analyzer_agent`, `battle_strategist_agent`, `item_finder_agent`, `leveling_training_advisor_agent`, `pokedex_completer_agent`, `team_builder_agent`, `direct_pathing_agent`, `rom_hack_mechanic_investigator_agent`.
*   **Pathing Script (`run_code`):** Fixing the `run_code` pathing script using `pathing_script_analyzer_agent` is a high-priority task for the next visit to a Pokémon Center.
*   **Agent Management Timing:** Define, update, or test agents only when in a safe, non-time-sensitive location (e.g., Pokémon Center).

# Map Discoveries
*   **Pallet Town:** Reachable, undiscovered map connection south at (4,18) or (3,18).
*   **Viridian City:** The Old Man tutorial for catching Pokémon opens the path to Route 22 (West), NOT Route 2 (North).

# Critical Route Information
*   **Route 2 (NORTH of Viridian City):** Leads to Viridian Forest, then Pewter City (Brock). THIS IS THE CORRECT PATH.
*   **Route 22 (WEST of Viridian City):** Leads to the Pokemon League. THIS IS A DETOUR if aiming for Pewter City.

# Inventory
*   POKé BALL x3
*   POTION x0 (Used last one on Turn 2353 on SPARKY)
*   ANTIDOTE x0 (Used one on Turn 2056 on SPARKY after Oddish battle)

# Battle Notes
*   **EXP Tracking (Simplified):** Record GameState EXP at start of battle + EXP gained from battle.
*   SPARKY learned TAIL WHIP, replacing GROWL at Lv11.
*   Blackout: Defeated by Bug Catcher (ID 6, VIRIDIANFOREST_YOUNGSTER5) at (17,18) in Viridian Forest (Turn 1104).
*   Defeated Lass (Cool Trainer F, ID 5) at (3,42) in Viridian Forest. (NIDORAN♀ Lv6, NIDORAN♂ Lv6). ¥90.
*   Defeated Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest. (Pinsir Lv8, Metapod Lv9). ¥90.
*   Defeated Youngster (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (28,34) in Viridian Forest. (Weedle Lv6, Kakuna Lv6). ¥90.
*   Defeated Bug Catcher (ID 3, VIRIDIANFOREST_YOUNGSTER3) at (28,20) in Viridian Forest.
*   **Thunder Wave Inconsistency (Pidgey):** THUNDER WAVE failed against a Lv8 Pidgey (Turn 2187), but successfully paralyzed a Lv7 Pidgey (Turn 2343). The first failure might have been due to accuracy (a simple miss) rather than type immunity.

# Pewter City Gym Notes
*   Gym Guide: Brock's lead GEODUDE (Rock Throw), also has ONIX (Bind). Electric attacks harmless.
*   Brock's Ace (Onix) is Lv14. Level cap is 14.
*   Defeated JR.TRAINER♂ (Cool Trainer M sprite, ID 2, PEWTERGYM_COOLTRAINER_M) at (4,7). (Diglett Lv9, Sandshrew Lv9). ¥180.

# Brock Battle Attempt 1 (FAILURE - Blackout)
*   SPARKY Lv12 vs Geodude Lv10 & Onix Lv14. Fainted to Geodude's Rock Throw. Geodude used Defense Curl. Money halved (¥392 -> ¥196).
*   **Conclusion:** SPARKY alone at Lv12 is not viable. Needs to be Lv14, find a new team member, or revise strategy.

# Current Pokémon Status
*   SPARKY (PIKACHU): Lv12 (35/39 HP). Current EXP: 1789. PP: THUNDERSHOCK 13/30.
    *   Moves: THUNDERSHOCK (13 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP).
*   **EXP to Lv13 (Target: 2197 total):** 408 EXP needed (2197 - 1789).
*   **EXP to Lv14 (Target: 2744 total):** 955 EXP needed (2744 - 1789).

*   **Refined Agent Usage Strategy (Post-Critique Turn 2408):**
    *   Utilize `direct_pathing_agent` more frequently for short, straightforward navigation to minimize manual input errors and 'mixed buttons' warnings.
    *   Confirm and prioritize using `pathing_script_analyzer_agent` at the next Pokémon Center visit to fix the main `run_code` pathing script.
    *   Actively re-evaluate and use other defined agents based on the current situation:
        *   `exploration_planner` for new, complex areas.
        *   `battle_strategist_agent` before major battles.
        *   `item_finder_agent` when specifically searching for items.
    *   Regularly assess the utility of all agents. If an agent is consistently unused or not providing value, consider deleting it to manage the 10-agent limit and maintain focus on effective tools.
*   **Note on 'Mixed Buttons' Warnings with `direct_pathing_agent`:** Still receiving these warnings even when the agent's output is only directional buttons and executed in a separate turn. Will monitor and ensure `path_plan` is populated when executing agent-generated moves. The issue might be with how the system interprets the sequence, or a deeper misunderstanding on my part about turn structure for tool outputs.