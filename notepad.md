# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Prepare for and defeat Brock in the Pewter City Gym.
*   **Tertiary Goal:** Explore Pewter City to find resources (money, items), information, investigate 'Reachable Unseen Tiles', and the 'Reachable Undiscovered Map Connection' to the East.

# Pewter City Strategy
*   **Financial Priority:** Current funds are very low (¥156). Need to prioritize defeating trainers in Pewter City for money to afford Potions (¥200 each) and other supplies.
*   **Oddish Training for Brock (CRITICAL):** ODDISH (Lv7) needs significant training and ideally a Grass-type damaging move to be effective against Brock's Geodude (Lv10) and Onix (Lv14). Relying on Tackle or PoisonPowder will be ineffective. Investigate Oddish's upcoming level-up moves or consider if other Pokémon might be needed.
*   **Exploration:** Thoroughly explore Pewter City, interact with NPCs, check buildings for items/information, and clear all 'Reachable Unseen Tiles'. Investigate the eastern map connection.
*   **Map Markers:** Consistently use map markers for defeated trainers, used warps, and key locations within Pewter City as they are discovered.

# Pokémon Center Tasks (Next Visit)
*   **Agent Management (Priority):
    *   Use `pathing_script_analyzer_agent` on the A* script and `advanced_pathfinder_agent` logic to diagnose failures.
    *   Formally mark `advanced_pathfinder_agent` for deletion or major overhaul; cease current usage.
    *   **Resolve `direct_pathing_agent` Status (CRITICAL):** Verify if this agent was deleted, never properly defined, or if I'm confusing it with the A* `run_code` script. If it doesn't exist or was a misremembered name for the A* script, remove these notes. If it *was* a distinct agent that got deleted or was faulty, document this clearly.
    *   **Low-Usage Agent Review (CRITICAL DECISIONS NEEDED):** Decisively re-evaluate `item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`. Improve their prompts/utility for active use, or delete them to free up agent slots (currently at 10/10 limit).
    *   **Address 'New Agent Ideas':** Make decisions on defining (requires deletion of existing agent) or discarding 'Route Progress Analyzer Agent' and 'Risk Assessor Agent' ideas.
    *   Test `move_validator_agent` and `npc_interaction_planner_agent` further.
*   **Financial Planning:** Re-assess funds and purchase Potions if affordable.

# Current Pokémon Status
*   SPROUT (ODDISH): Lv7 (25/25 HP, EXP: 262). (Stats: Attack 13, Defense 13, Speed 10, Special 15).
    *   Moves: TACKLE (34 PP), POISONPOWDER (34 PP).
*   SPBARKY (PIKACHU): Lv12 (39/39 HP, no status). Current EXP: 1728. **AT LEVEL CAP (12) FOR 0 BADGES. CANNOT GAIN MORE EXP UNTIL 1ST BADGE IS EARNED.**
    *   Moves: THUNDERSHOCK (30 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP).

# Inventory & Finances
*   POKé BALL x2
*   Money: ¥156 (Potions cost ¥200)

# Hard Mode Rules & ROM Hack Changes (Summary)
*   Battle Style: Set. No items in battle. Level caps apply (current cap 0 badges: 12. Brock's Ace Onix Lv14 -> cap before Brock: 14).
*   HMs: Forgettable, menu use, not PC storable. All 151 obtainable. Trade evos by level. Smarter AI. Tougher bosses. EXP. All early. Potions heal 10HP. Wild battles: no money, only EXP (if not capped).

# Navigation Strategy & Best Practices (CRITICAL - MUST ADHERE)
*   **Meticulous Tile-by-Tile Verification (ABSOLUTE PRIORITY):** Before *any* movement segment, consult map memory (XML) and verify `navigable="true"` and `type` of *every single tile*. XML is sole truth for player movement.
*   **Extremely Short, Verifiable Segments:** Path segments MUST be 3-5 tiles max, or single clear small areas. Each chunk 100% confirmed navigable from XML *before* execution.
*   **Focus on Continuous Open Corridors:** Prioritize verified open corridors based on XML, not distant coordinates across unverified terrain.
*   **Map Marker Usage (IMMEDIATE & ABSOLUTE):** *Immediately* mark confirmed dead ends (🚫), key navigational turns/points (📍), and important warps (🚪) after discovery/use. Essential for spatial understanding.
*   **Pikachu Interaction:** If a direct path avoiding Pikachu's tile can be identified, it's more efficient than stepping onto his tile and immediately changing direction.
*   **`navigable="false"` is Absolute (CRITICAL LESSON):** If XML shows `navigable="false"`, it is IMPASSABLE by player, regardless of tile type or NPC status. Trust `navigable` attribute.

# Recent Events & Observations
*   **Viridian Forest Navigation (Pre-Pewter):** Multiple wild encounters (Pidgey, Oddish, Rattata) while navigating Viridian Forest and Route 2. Successfully ran from all. Sand-Attack spam from Pidgey made ODDISH's accuracy very low in one battle.
*   **Agent Deletions (Turn 3665):** `battle_strategist_agent` and `financial_planner_agent` were deleted.

# Archived Learnings & Notes (For Brevity - Refer to older full notes if needed)
*   Older battle logs, detailed early game event triggers, specific NPC dialogue not immediately relevant to current objectives, detailed A* script failure logs (to be addressed by `pathing_script_analyzer_agent`).
*   Repel Mechanics: Lead Pokémon level must be *strictly greater* than wild Pokémon level for Repel to be effective in this ROM hack.
*   `exploration_planner` Misuse: Agent is strictly for 'Reachable Unseen Tiles', not for paths to known, seen tiles.
*   System Warnings: Avoid mixing directional and action buttons.