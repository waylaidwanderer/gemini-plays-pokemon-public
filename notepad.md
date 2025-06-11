# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Train SPROUT (Oddish) to a safer level (e.g., Lv 8-10) in Viridian Forest grass by having it lead battles, prioritizing its safety due to low HP.
*   **Tertiary Goal:** Safely defeat Youngster (ID 6) at (14,18) in Viridian Forest for money and additional EXP, but only after SPROUT is at a safer HP/level and a clear path to an adjacent tile is identified.

# Agent Performance & Development
*   **Pathing Script (`run_code` - URGENT HIGH PRIORITY):** Fixing the `run_code` A* pathing script (which failed on Turn 3097 by suggesting a move into an impassable tile) is critical. Use `pathing_script_analyzer_agent` at the *very next safe opportunity* (e.g., Pokémon Center). Current navigation difficulties are heavily impacted by its failure.
*   **`direct_pathing_agent` Issues (CRITICAL):** This agent (which does not use `run_code`) has repeatedly shown critical issues:
    *   When Pikachu is on the target tile, it often *only turns the player* instead of executing the full two-step move (turn then step) required.
    *   It frequently fails to correctly generate paths involving an initial turn followed by a move (e.g., player facing Up, target is Right, agent might only output 'Right' for the turn, not 'Right', 'Right' for turn then move).
    *   It is unreliable for these scenarios. Manual input or a fixed/new agent is preferred.
*   **Agent Management Timing:** Define, update, or test agents only when in a safe, non-time-sensitive location (e.g., Pokémon Center).
*   **Agent Usage Reminder:** Be more proactive in using existing agents, especially for navigation, item finding, and battle strategy.
*   **Active Agents to Test/Utilize:** `exploration_planner`, `map_analyzer_agent`, `battle_strategist_agent`, `item_finder_agent`, `leveling_training_advisor_agent`, `pokedex_completer_agent`, `team_builder_agent`, `direct_pathing_agent`, `financial_planner_agent`.

# Current Pokémon Status
*   SPROUT (ODDISH): Lv7 (8/25 HP - CRITICALLY LOW, EXP: 262). (Stats: Attack 13, Defense 13, Speed 10, Special 15).
    *   Moves: TACKLE (23 PP), POISONPOWDER (33 PP).
*   SPBARKY (PIKACHU): Lv12 (37/39 HP, no status). Current EXP: 1728. **AT LEVEL CAP (12) FOR 0 BADGES. CANNOT GAIN MORE EXP UNTIL 1ST BADGE IS EARNED. (Game may display EXP gain message, but actual EXP value remains unchanged).**
    *   Moves: THUNDERSHOCK (28 PP), TAIL WHIP (30 PP), QUICK ATTACK (29 PP), THUNDER WAVE (20 PP).

# Training Strategy Notes
*   **SPROUT Training (CRITICAL):** SPROUT's HP is often low. When training, prioritize its survival. Have SPROUT participate for one turn (e.g., PoisonPowder or one attack if safe) then **immediately switch to SPARKY** to secure the KO and EXP. Fainting SPROUT negates the training effort and wastes resources.
*   **Financial Priority:** Current funds are very low (¥96). Need to prioritize defeating trainers for money to afford Potions (¥200 each) and other supplies.

# Inventory & Finances
*   POKé BALL x2
*   REPEL x10
*   Money: ¥96
*   **Note:** Potions cost ¥200.

# Hard Mode Rules
*   Battle Style: Set.
*   No items in battle.
*   Level caps apply (current cap with 0 badges is 12. Brock's Ace Onix is Lv14; the cap before fighting him will be 14. Lt. Surge's cap is 24).

# Key Game Changes (ROM Hack)
*   HMs: Forgettable, usable from menu, not storable in PC.
*   All 151 Pokémon obtainable.
*   Trade evos by level.
*   Smarter AI, anti-sweep.
*   Tougher boss fights.
*   Dynamic scaling Gyms 4-6.
*   EXP. All available early.
*   Potions heal 10 HP.
*   Wild Pokémon battles do not award money, only EXP (if not level capped).

# Map Discoveries & Navigation
*   **Pallet Town:** Reachable, undiscovered map connection south at (4,18) or (3,18).
*   **Viridian City Old Man:** Tutorial for catching Pokémon opens path to Route 22 (West).
*   **Critical Route Information:**
    *   Route 2 (NORTH of Viridian City): Leads to Viridian Forest, then Pewter City (Brock).
    *   Route 22 (WEST of Viridian City): Leads to the Pokemon League.
*   **Pewter City Pokecenter Warp:** Entrance at (14,26). When exiting to (14,27) or (15,27) and moving north, move to column 16+ first.
*   **Tricky Warp Navigation (CRITICAL):** For warps that can be re-entered immediately: one-action-per-turn for entry (move on, turn, enter). Upon arrival, *immediately* move one step away from arrival warp.
*   **Route 2 North Gate Warp (4,12) to Viridian Forest North Gate (SOLVED):** Triggered by being on (4,12) and pressing DOWN.
*   **Map Obstacles & Trainer Behavior:**
    *   Youngster (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest, despite being defeated, blocks the path south with dialogue.

# Battle Mechanics & Observations
*   **EXP Tracking (Precise):** Record GameState EXP *before* and *after* a battle. If a Pokémon is level-capped, verify that its actual EXP value does not change, even if an EXP gain message is displayed.
*   **Lead Pokémon Anomaly (ROM Hack):** Game may send out a different Pokémon than the one in the first party slot at the start of a wild battle. Requires manual switching.

# Pewter City Gym Notes
*   Gym Guide: Brock's lead GEODUDE (Rock Throw), also has ONIX (Bind). Electric attacks harmless.
*   Brock's Ace (Onix) is Lv14. Level cap is 14 for this fight.
*   Defeated JR.TRAINER♂ (Cool Trainer M sprite, ID 2, PEWTERGYM_COOLTRAINER_M) at (4,7). (Diglett Lv9, Sandshrew Lv9). ¥180.

# Archived Learnings & Battle History
*   **Event Triggers & Key Interactions (Early Game):**
    *   Rival Battle 1 (Oak's Lab): Triggered by attempting to leave lab after Pikachu.
    *   Pikachu Following: After first rival battle.
    *   Town Map: Rival SPB mentioned his sister has one.
    *   Oak's Parcel: From Viridian PokeMart clerk. Delivered to Oak.
    *   Pokédex: From Oak after parcel delivery.
*   **Lessons Learned (Early Game):**
    *   Ledge Mechanics: One-way down. Cannot move up or sideways onto them from lower Y.
    *   Route 1 Sign (10,28): Impassable.
    *   Follower Pokemon block if approached non-facing.
    *   Potion Usage (ROM Hack): Heal 10 HP.
    *   Map Connections: Double-check direction/destination.
    *   Trainer Battle Initiation: Line of sight.
    *   Type Matchups: Electric not very effective vs. Grass/Poison.
    *   Status Conditions (Poison): Prioritize healing.
    *   System Warnings (Mixed Buttons): Avoid.
    *   NPC Interaction: Adjacent navigable tile.
    *   Map Verification: Check navigability for entire path.
    *   Financial Planning: Verify costs/funds before travel.
    *   Shop Menu Interaction: Explore quantity options.
*   **Battle Notes (Archive):**
    *   SPARKY learned TAIL WHIP, replacing GROWL at Lv11.
    *   Blackout: Defeated by Bug Catcher (ID 6, VIRIDIANFOREST_YOUNGSTER5) at (17,18) in Viridian Forest (Turn 1104).
    *   Defeated Lass (Cool Trainer F, ID 5) at (3,42) in Viridian Forest. (NIDORAN♀ Lv6, NIDORAN♂ Lv6). ¥90.
    *   Defeated Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest. (Pinsir Lv8, Metapod Lv9). ¥90.
    *   Defeated Youngster (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (31,34) in Viridian Forest. (Weedle Lv6, Kakuna Lv6). ¥90.
    *   Defeated Bug Catcher (ID 3, VIRIDIANFOREST_YOUNGSTER3) at (31,20) in Viridian Forest.
    *   Thunder Wave Inconsistency (Pidgey): Failed vs Lv8, worked vs Lv7. Likely accuracy.
*   **Brock Battle Attempt 1 (FAILURE - Blackout):**
    *   SPARKY Lv12 vs Geodude Lv10 & Onix Lv14. Fainted to Geodude's Rock Throw. Money halved (¥392 -> ¥196).
    *   Conclusion: SPARKY alone at Lv12 not viable. Needs Lv14, new team member, or revised strategy.
*   **Critique Lesson (Turn 2626 - Archived):** Consistently verify path navigability tile-by-tile in Map Memory for any planned route, especially longer ones. Break down manual pathing into shorter, verifiable segments (e.g., 3-5 steps). Prioritize fixing/using pathing agents. Confirm item prices and funds *before* shop visits. Re-evaluate shop menu interaction for quantity adjustments.

# Battle Mechanics & Observations
*   SPROUT's POISONPOWDER (Lv7 Oddish) failed against a wild Lv4 WEEDLE in Viridian Forest. (Turn 3143)

- **Pokémon Center Agent Tasks:** Define `advanced_pathfinder_agent`. Use `pathing_script_analyzer_agent` on the existing `run_code` A* script.

*   **`advanced_pathfinder_agent` Failure (Turn 3171 & 3172):** The newly defined `advanced_pathfinder_agent` failed on its first two attempts (from (7,26) in Viridian Forest). Both times it suggested moving 'Down' into tile (7,27), which is impassable. This agent is currently unreliable and requires investigation/fixing.
*   **`advanced_pathfinder_agent` Failure (Turn 3177):** The agent, called from (3,26) to target (17,48), generated a 125-step path. The path failed after 5 successful steps when the player was at (5,23) facing Up, attempting to move to (5,22), which is an impassable tile. This is the third consecutive failure of this agent, indicating severe issues with its pathing logic or map interpretation.

*   **`advanced_pathfinder_agent` Failure (Turn 3185):** Agent provided a 125-step path from (13,30) to (17,48). After the first two steps ('Left', 'Left') to reach (12,30) facing Left, the system reported 'Your attempt to move Left from (12, 30) was blocked.' However, the agent's *next* planned move was 'Up' to (12,29) (a navigable tile). This suggests a critical disconnect in path execution or system interpretation. Agent is currently highly unreliable.