# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Level up SPARKY to Lv14 to better challenge Brock.
*   **Tertiary Goal:** 

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
*   **Potion Usage (REVISED):** SPARKY should be healed with Potions proactively outside of battle if HP is low and a Pokémon Center isn't immediately accessible, especially before engaging trainers or exploring deep into an area. Relying solely on Pokémon Centers for healing can lead to blackouts if unexpected battles occur or poison takes its toll.
*   **Map Connections:** ALWAYS double-check the *direction* (North, South, East, West) and *destination* of a map connection in the Game State Information before committing to a route. A wrong turn can lead to significant detours (e.g., Route 22 instead of Route 2).
*   **Trainer Battle Initiation (CRITICAL):** Battles are primarily triggered by entering a trainer's direct line of sight. Observe their facing direction and move onto a tile directly in front of them. Repeatedly pressing 'A' or trying to step on their tile when not in their LoS is ineffective. Dialogue loops can sometimes be broken with 'B' or by moving away. Non-battling NPCs may still have trainer sprites.
*   **Exploration Planner Paths:** If the `exploration_planner` provides a very long or scattered path, consider breaking it into smaller, logical segments or re-running the planner after a short manual move to a new area. This can lead to more manageable and efficient exploration.
*   **Type Matchups (CRITICAL REMINDER):** Pay closer attention to type matchups. Electric-type moves (like THUNDERSHOCK) are NOT VERY EFFECTIVE against Grass/Poison types like Oddish. This was a critical error leading to SPARKY taking unnecessary damage and getting poisoned.
*   **Status Conditions (Poison):** Poison is a serious threat in Hard Mode, especially with no in-battle items. If SPARKY gets poisoned, prioritize reaching a Pokémon Center or using an Antidote (if available) ASAP. Do not continue to battle or explore extensively while poisoned, as the damage accumulates quickly and can lead to fainting.
*   **Short-Range Pathing & Interaction:** Improve observation of immediate surroundings (NPCs, obstacles) to avoid wasted turns. Verify navigability and facing before committing to paths or interactions, especially in confined spaces.

# Hard Mode Rules
*   Battle Style: Set.
*   No items in battle.
*   Level caps apply (Lt. Surge's cap is 24).

# Key Game Changes (ROM Hack)
*   HMs: Forgettable, usable from menu, not storable in PC.
*   All 151 Pokémon obtainable.
*   Trade evos by level.
*   Smarter AI, anti-sweep.
*   Tougher boss fights.
*   Dynamic scaling Gyms 4-6.
*   EXP. All available early.

# General Ledge Navigation Principles
*   **Problem:** Ledges block upward movement.
*   **Strategy:** To bypass upward ledges, find a path AROUND. Move away from the ledges (laterally or downwards) to find a clear corridor or grass patch allowing ascent *above* the problematic ledges. Then, navigate laterally above and descend as needed. Verify ledge properties in map memory and visually inspect. Critically evaluate agent-provided paths for ledge issues.
*   **Agent Use for Ledges:** If manual pathing or `exploration_planner` struggles with complex verticality/blockages by ledges, consider using `map_analyzer_agent` to query for clear paths or alternative exits (e.g., 'Find a path from (X,Y) to (A,B) avoiding upward ledges').

# Agent Development & Pathing Strategy (**REVISED POST-CRITIQUE & BLACKOUT - FURTHER REVISED**)
## Active Agents
*   `exploration_planner`: Analyzes map XML and reachable unseen tiles for efficient exploration. (Continue using, but break down long paths. Ensure Pikachu's health is stable before long explorations. Be cautious about the length of paths requested or followed without intermediate verification, especially in maze-like environments. Request paths to closer, intermediate waypoints or only execute a very small number of initial steps from a long path before re-evaluating.)
*   `map_analyzer_agent`: Analyzes map XML to answer specific questions. (Use proactively for navigation issues, pathfinding queries if stuck, or understanding blockages. Consider using for finding shorter paths if manual pathing seems convoluted. When using for complex routes, request paths to closer, intermediate waypoints or only execute a very small number of initial steps from a long path before re-evaluating.)
*   `pathing_script_analyzer_agent`: Analyzes pathing scripts. (Use to diagnose and begin fixing the `run_code` pathing script when at a Pokemon Center or safe location.)
*   `battle_strategist_agent`: Assists with Hard Mode boss fight planning. (Use for upcoming tough trainers or Gym Leaders. Test this agent to assess its effectiveness.)
*   `item_finder_agent`: Searches map for items. (Use to find remaining items in an area. Test this agent to assess its effectiveness.)
*   `leveling_training_advisor_agent`: Advises on optimal grinding spots, Pokemon to train, and EV training strategies based on current party, level cap, known areas/trainers, and game mode (e.g., Hard Mode restrictions). (Use when preparing for gym leaders or if general leveling is needed. Test this agent to assess its effectiveness.)
*   `pokedex_completer_agent`: Suggests targets for Pokedex completion. (Defined - test effectiveness)
*   `team_builder_agent`: Suggests ideal team compositions for major challenges. (Defined - test effectiveness)
## Pathing Script (`run_code`) Behavior (**CRITICAL - DO NOT USE UNTIL FIXED - IMMEDIATE ACTION REQUIRED**)
*   The `run_code` script for path generation is **FUNDAMENTALLY FLAWED** and **UNRELIABLE**.
    *   **NEW STRATEGY (MANDATORY):** **DO NOT USE THIS SCRIPT for any path longer than 1-2 easily verifiable steps.** Prioritize **MANUAL NAVIGATION**. If stuck, use `map_analyzer_agent` to query for paths.
    *   **IMMEDIATE NEXT STEP (WHEN AT A POKEMON CENTER OR SAFE LOCATION):** Use the `pathing_script_analyzer_agent` to diagnose and begin fixing the `run_code` pathing script. This is the **ABSOLUTE HIGHEST PRIORITY** and must be addressed at the very next opportunity when not actively grinding or in a dangerous area (e.g., next Pokémon Center visit). Continued deferral is unacceptable.

# Map Discoveries
*   **Pallet Town:** Reachable, undiscovered map connection south at (4,18) or (3,18).
*   **Viridian City:** The Old Man tutorial for catching Pokémon opens the path to Route 22 (West), NOT Route 2 (North).

# Critical Route Information
*   **Route 2 (NORTH of Viridian City):** Leads to Viridian Forest, then Pewter City (Brock). THIS IS THE CORRECT PATH.
*   **Route 22 (WEST of Viridian City):** Leads to the Pokemon League. THIS IS A DETOUR if aiming for Pewter City.

# Viridian Forest Notes
*   Youngster (ID 1, VIRIDIANFOREST_YOUNGSTER1) at (17,44): Confirmed non-battling NPC after direct interaction. Path north appears to be around this NPC via (16,44) or (18,44).
*   Youngster (ID 10, VIRIDIANFOREST_YOUNGSTER6) at (28,41): Confirmed non-battling NPC. Dialogue: "You should carry extras!". Blocks direct westward movement along row 41.
*   Bug Catcher (ID 3, VIRIDIANFOREST_YOUNGSTER3) at (28,20): **Defeated**.
*   Items Collected:
    *   Potion at (26,12) - Collected (Turn 981).
    *   Potion at (13,30) - Collected (Turn 1905).
*   Inventory:
    *   POKé BALL x3
    *   POTION x2
    *   ANTIDOTE x0 (Used one on Turn 2056 on SPARKY after Oddish battle)

# Battle Notes
*   SPARKY learned TAIL WHIP, replacing GROWL at Lv11 (Turn 1004).
*   Defeated by Bug Catcher (ID: VIRIDIANFOREST_YOUNGSTER5) at (17,18) in Viridian Forest after its Caterpie and Metapod. SPARKY fainted due to poison and accumulated damage, resulting in a blackout. Returned to Viridian City Pokemon Center. (Turn 1104)
*   Defeated Lass (Cool Trainer F, ID 5) at (3,42) in Viridian Forest. Her Pokemon: NIDORAN♀ Lv6, NIDORAN♂ Lv6. SPARKY was at 26/39 HP after the battle. Got ¥90.
*   Defeated Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest. His Pokemon: Pinsir Lv8, Metapod Lv9. Got ¥90.
*   Defeated Youngster (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (28,34) in Viridian Forest. His Pokemon: Weedle Lv6, Kakuna Lv6. SPARKY was at 39/39 HP. Got ¥90.
## Wild Encounters (Viridian Forest - Grinding for Brock)
    *   Defeated Wild Weedle Lv4 (Turn 2021), got 29 EXP. SPARKY's HP: 39/39. Not poisoned.
    *   Defeated Wild Weedle Lv4 (Turn 2027), got 29 EXP. SPARKY's HP: 39/39. SPARKY not poisoned.
    *   Defeated Wild Metapod Lv6 (Turn 2036), got 61 EXP. SPARKY's HP: 39/39. SPARKY not poisoned.
    *   Defeated Wild Weedle Lv4 (Turn 2040), got 29 EXP. SPARKY's HP: 39/39. SPARKY not poisoned.
    *   Defeated Wild Weedle Lv4 (Turn 2042), got 29 EXP. SPARKY's HP: 39/39. SPARKY not poisoned.
    *   Defeated Wild Metapod Lv6 (Turn 2044), got 61 EXP. SPARKY's HP: 39/39. SPARKY not poisoned.
    *   Defeated Wild Oddish Lv6 (Turn 2055), got 66 EXP. SPARKY's HP: 37/39. SPARKY was poisoned by POISONPOWDER. Used ANTIDOTE (Turn 2056).

# Pewter City Prep
*   Find out Brock's Ace level / level cap for Hard Mode. (Onix Lv14 is Ace, cap is 14)
*   Plan party composition/training for Brock.
*   Test battle_strategist_agent and leveling_training_advisor_agent before challenging Brock.

# Pewter City Museum Notes (COMPLETED)
*   Paid ¥50 to enter.
*   **Museum 1F NPCs & Items:**
    *   Attendant at (10,5): Sells tickets.
    *   Old Man (Gambler sprite, ID 1) at (2,5): "That is one magnificent fossil!"
    *   All tiles seen, all NPCs spoken to.
*   **Museum 2F NPCs & Items:**
    *   Scientist (ID 3) at (8,6): "We have a space exhibit now."
    *   Brunette Girl (ID 4) at (12,6): "I want a PIKACHU! It's so cute! I asked my Daddy to catch me one!"
    *   Hiker (ID 5) at (13,6): "I'd love to get that strong looking PIKACHU off you! Too bad it looks so attached. They've been hard to find lately!"
    *   Youngster (ID 1) at (8,8): On the warp tile to 1F (no unique dialogue).
    *   Gramps (ID 2) at (1,6): "July 20, 1969! The 1st lunar landing! I bought a color TV to watch it!"
    *   Sign at (3,6) MUSEUM2F_MOON_STONE_SIGN is impassable.
    *   Sign at (12,3) MUSEUM2F_SPACE_SHUTTLE_SIGN.
    *   All tiles seen, all NPCs spoken to.

# Viridian City Notes
*   Youngster (no ID in map sprites, but observed) at (31,26) can block the path to the Mart if approaching from the east along row 26. Need to go around via row 27 if blocked.

# General Strategy Notes
*   Break down long agent-generated paths (e.g., from `map_analyzer_agent` or `exploration_planner`) into shorter, verifiable segments (e.g., 5-10 steps, or to an intermediate landmark). Re-evaluate after each segment, especially in complex/maze-like areas.
*   **Proactive Healing & Poison Management (REINFORCED - CRITICAL ERROR):** Blacking out due to poison and accumulated damage from poor battle choices is unacceptable. If SPARKY is poisoned, prioritize healing (Antidote if available, Potion if HP is low, or retreat to a Pokémon Center) *before* further exploration or difficult battles. Do not rely on nearly fainting before healing. Use Potions more liberally outside of battle to maintain high HP.
*   **Type Matchups (REINFORCED - CRITICAL ERROR):** THUNDERSHOCK is NOT VERY EFFECTIVE against Grass/Poison types (e.g., Oddish). QUICK ATTACK (Normal) is neutral and often a better choice for consistent damage in such cases. Must internalize type charts.

# Pewter City Notes
*   Cool Trainer F (PEWTERCITY_COOLTRAINER_F) at (9,16) is non-battling. Dialogue: "It's rumored that CLEFAIRYs came from the moon! They appeared after MOON STONE fell on MT.MOON." She does not gatekeep the Gym.

# Pewter City Mart Notes
*   Youngster (PEWTERMART_YOUNGSTER) at (4,5): "A shady old man got me to buy this really weird fish POKéMON! It's totally weak and it cost ¥500!" (Likely referring to Magikarp).

# Pewter City Gym Notes
*   Gym Guide says Brock's lead is GEODUDE (Rock Throw), and he also has an ONIX (Bind).
*   **CRITICAL: Electric attacks are HARMLESS to Brock's Ground-type POKéMON.**
*   SPARKY's Thundershock and Thunder Wave will be useless. Must rely on Quick Attack and Tail Whip.
*   Brock's Ace (Onix) is Lv14. Level cap for Hard Mode is 14.
*   Defeated JR.TRAINER♂ (Cool Trainer M sprite, ID 2, PEWTERGYM_COOLTRAINER_M) at (4,7) in Pewter Gym. Pokémon: Diglett Lv9, Sandshrew Lv9. Prize: ¥180. SPARKY healed to full HP (39/39) after battle.

# Brock Battle Attempt 1 (FAILURE - Blackout)
*   Challenged Brock. SPARKY Lv12 vs Geodude Lv10 & Onix Lv14.
*   Strategy: Multiple Tail Whips then Quick Attack.
*   Outcome: SPARKY fainted to Geodude's Rock Throw after several turns. Geodude used Defense Curl multiple times, negating Tail Whips. Quick Attack did minimal damage even with -3 Defense. SPARKY's HP dropped too quickly.
*   Blacked out and returned to Pewter City Pokemon Center. Money halved (¥392 -> ¥196).
*   **Conclusion:** Current strategy with SPARKY alone at Lv12 is not viable. Need to level up SPARKY to Lv14, find a new team member effective against Rock/Ground, or significantly revise the strategy.

# Leveling Plan for Brock (Post-Blackout 1) - REVISED
*   **Objective:** Level SPARKY from Lv12 to Lv14 (level cap).
*   **Strategy REVISED:** Grind wild Pokémon in Viridian Forest.
*   **Pewter City Trainer Outcomes (ALL NON-BATTLING/SCRIPTED):
    1.  Cool Trainer M (PEWTERCITY_COOLTRAINER_M) at (18,26) - Dialogue only.
    2.  Super Nerd (PEWTERCITY_SUPER_NERD1) at (28,18) - Dialogue only.
    3.  Youngster (PEWTERCITY_YOUNGSTER) at (36,17) - Scripted event, led to Gym, no battle.
    4.  Cool Trainer F (PEWTERCITY_COOLTRAINER_F) at (9,16) - Dialogue only.
*   **Conclusion:** No trainer EXP in Pewter City. Viridian Forest is the sole grinding spot for now.

# EXP Tracking
*   SPARKY (PIKACHU) - Lv12
*   Current EXP: 2010 (after Pidgey battle on Turn 2071; Needs 734 more for Lv14 cap)
*   EXP to Lv13: 2197 (Needs 187 more)
*   EXP to Lv14 (CAP): 2744 (Needs 734 more)

*   **Future Agent Testing/Development:**
    *   Test `pokedex_completer_agent` and `team_builder_agent` to assess their utility when appropriate (e.g., before major Pokedex hunting sessions or team reshuffles for Gyms).
    *   Consider developing a `direct_pathing_agent` focused on simple, direct A-to-B movement if the main `run_code` script proves too difficult to fix quickly. This could serve as a more reliable short-term navigation aid for straightforward paths.

# Reflection Notes (Turn 2039 - Updated Turn 2055)
*   **EXP Tracking:** Game state EXP display for party Pokémon often lags behind actual EXP gained from battles. My manual tracking in the notepad based on battle log messages is more reliable.
*   **System Warnings (Mixed Buttons):** I've been frequently receiving a 'System Warning: You tried to mix directional and action buttons in the same sequence.' This truncates my intended movement paths. I must be more careful to ensure `buttons_to_press` contains *only* directional buttons for multi-step movements. Interaction buttons (A, B) or 'tool' calls must be in separate turns.
*   **Notepad Organization:** Added a 'Wild Encounters' sub-section under 'Battle Notes' for better clarity. Added an 'Inventory' sub-section under 'Viridian Forest Notes'.
*   **Pathing Script:** Fixing the `run_code` pathing script using `pathing_script_analyzer_agent` remains a high-priority task for the next visit to a Pokémon Center or other safe, non-grinding location.