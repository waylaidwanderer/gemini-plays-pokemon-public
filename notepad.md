# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds (¥) for Potions and train SPROUT (Oddish) to an effective level for the Gym battle.
*   **Tertiary Goal:** Systematically explore all 'Reachable Unseen Tiles' in Pewter City and investigate the 'Reachable Undiscovered Map Connection' to the East.

# Pewter City Strategy
*   **Immediate Priority (CRITICAL):** Systematically explore 'Reachable Unseen Tiles' (currently 14 listed, mostly in N/NW) using `exploration_planner_agent` to find trainers for money (current: ¥156) and items. This is more achievable than repeated failed attempts to reach distant locations like the Pokémon Center across complex terrain.
*   **Financial Priority:** Defeat trainers for money to afford Potions (¥200 each) and other supplies.
*   **Oddish Training for Brock:** SPROUT (ODDISH Lv7) needs significant training and ideally a Grass-type damaging move. The current level cap for 0 badges is 12. If Brock is faced, the cap becomes 14 (his Onix's level).
*   **Map Markers:** Consistently use map markers for defeated trainers (☠️), used warps (🚪), key locations (📍), non-battling NPCs (ℹ️), and confirmed dead ends (🚫).

# Pokémon Center Tasks (Next Visit)
*   **Heal Pokémon.**
*   **Agent Management (Priority):
    *   Use `pathing_script_analyzer_agent` on the A* script and `advanced_pathfinder_agent` logic to diagnose failures. Formally mark `advanced_pathfinder_agent` for deletion or major overhaul; cease current usage. Resolve status of `direct_pathing_agent`.
    *   **Low-Usage Agent Review (CRITICAL DECISIONS NEEDED):** Decisively re-evaluate `item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`. Improve their prompts/utility for active use, or delete them to free up agent slots (currently at 10/10 limit).
    *   **Address 'New Agent Ideas':** Make decisions on defining (requires deletion of existing agent) or discarding 'Route Progress Analyzer Agent' and 'Risk Assessor Agent' ideas.
    *   Test `npc_interaction_planner_agent` further.
*   **Financial Planning:** Re-assess funds and purchase Potions if affordable.

# Current Pokémon Status
*   SPROUT (ODDISH): Lv7 (25/25 HP, EXP: 262). Moves: TACKLE, POISONPOWDER.
*   SPBARKY (PIKACHU): Lv12 (39/39 HP, EXP: 1728). **AT LEVEL CAP (12).** Moves: THUNDERSHOCK, TAIL WHIP, QUICK ATTACK, THUNDER WAVE.

# Inventory & Finances
*   POKé BALL x2
*   Money: ¥156

# Hard Mode Rules & ROM Hack Changes (Summary)
*   Battle Style: Set. No items in battle. Level caps apply (current 0 badges: 12. Brock's Ace Onix Lv14 -> cap before Brock: 14).
*   HMs: Forgettable, menu use, not PC storable. All 151 obtainable. Trade evos by level. Smarter AI. Tougher bosses. EXP. All early.

# Navigation Strategy & Best Practices (CRITICAL - MUST ADHERE)
*   **Meticulous Tile-by-Tile Verification (ABSOLUTE PRIORITY):** Before *any* movement segment, consult map memory (XML) and verify `navigable="true"` and `type` of *every single tile*. XML is sole truth for player movement.
*   **Extremely Short, Verifiable Segments:** Path segments MUST be 3-5 tiles max, or single clear small areas. Each chunk 100% confirmed navigable from XML *before* execution.
*   **Use `move_validator_agent` (CRITICAL):** Before executing *any* planned path segment longer than a single step, use `move_validator_agent` to confirm path validity against the map XML. This is essential to prevent wasted turns.
*   **Focus on Continuous Open Corridors:** Prioritize verified open corridors based on XML, not distant coordinates across unverified terrain.
*   **Map Marker Usage (IMMEDIATE & ABSOLUTE):** *Immediately* mark confirmed dead ends (🚫), key navigational turns/points (📍), and important warps (🚪) after discovery/use. Essential for spatial understanding.
*   **Pikachu Interaction:** If a direct path avoiding Pikachu's tile can be identified, it's more efficient than stepping onto his tile and immediately changing direction.
*   **`navigable="false"` is Absolute:** If XML shows `navigable="false"`, it is IMPASSABLE by player, regardless of tile type or NPC status. Trust `navigable` attribute.
*   **Agent Utilization for Exploration:** Use `exploration_planner_agent` to generate paths for 'Reachable Unseen Tiles'.

# Recent Events & Observations (Last ~50 turns)
*   **Pewter City Arrival & Gym Guide:** Reached Pewter City. Youngster NPC at (36,17) led me to the Gym entrance at (12,19). He is not a battlable trainer. Marked Gym entrance (🏛️) and Youngster (💁).
*   **Navigation Issues:** Multiple failed attempts to navigate Pewter City, particularly towards the Pokémon Center, due to blocked paths and not strictly adhering to short, verified segments or using `move_validator_agent`.
*   **Cool Trainer F Interaction:** Cool Trainer F at (9,16) is not a trainer; provided info about Mt. Moon. Marked as (ℹ️).
*   **Current Location:** (15,21) in Pewter City, facing Down. Pikachu at (15,20).

# Archived Learnings & Notes (Condensed)
*   Older battle logs, detailed early game event triggers, specific NPC dialogue not immediately relevant, detailed A* script failure logs (to be addressed by `pathing_script_analyzer_agent`). Repel Mechanics: Lead Pokémon level must be *strictly greater* than wild Pokémon level for Repel to be effective. `exploration_planner` Misuse: Agent is strictly for 'Reachable Unseen Tiles', not for paths to known, seen tiles. System Warnings: Avoid mixing directional and action buttons.

# Post-Critique Learnings & Adjustments (Turn 3800)
*   **`move_validator_agent` Usage (CRITICAL - NON-NEGOTIABLE):** MUST use `move_validator_agent` for *every single* multi-step path planned. No exceptions. This is to prevent further wasted turns from hitting impassable tiles, signs, or ledges incorrectly.
*   **`exploration_planner_agent` Contingency:** If `exploration_planner_agent` returns an empty path when reachable unseen tiles exist (as in Turn 3777), I must manually plan the exploration of those tiles using short, validated segments.
*   **Financial Priority (Reiteration):** Finding and defeating trainers for money (current: ¥156) remains a top priority for Potions and supplies.
*   **Agent Management (Pokémon Center):** The plan to review, improve, or delete underused agents (`item_finder_agent`, `pokedex_completer_agent`, `team_builder_agent`, `leveling_training_advisor_agent`), resolve `direct_pathing_agent` status, and address 'New Agent Ideas' at the next Pokémon Center visit is still active and crucial.
*   **Map Knowledge Update:** `move_validator_agent` confirmed tile (32,13) in Pewter City is impassable (Turn 3800). This blocks direct southward travel from (32,3) beyond (32,12).