# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds to heal FLAREE and purchase essential supplies.
*   **Tertiary Goal:** Reach Route 3 to identify trainers for battling.

# Game Mechanics & Strategy
*   **Ledge Mechanics:** One-way (downwards only). Cannot move UP onto a ledge from a lower Y.
*   **Movement Mechanic:** 1st press TURNS if not facing, 2nd press MOVES. **Pikachu Movement:** Pikachu does not block movement. If not facing Pikachu and attempting to move onto Pikachu's tile, the first directional input *towards* Pikachu causes the player to turn and face Pikachu. A *second* directional input towards Pikachu is then required to step onto Pikachu's tile. This applies only when moving *into* Pikachu's current tile; normal movement applies otherwise. If already facing Pikachu, one press moves onto the tile.
*   **Level Cap:** 0 badges = Lv12. EXP gain stops at cap. Wild battles give no money.
*   **Data Trust:** Game State Information is absolute truth. Prioritize XML map data over screen annotations for tile properties. Trust Map Sprites for NPC locations each turn.
*   **Pathing & Navigation (CRITICAL UPDATE):** 
    *   For any movement in the eastern half of Pewter City (approx. X > 25), use `scripted_event_tracker_agent` for *every single step* if near Youngster (ID 5) trigger zones.
    *   Break down all multi-step paths into very small, verifiable segments (1-3 logical moves). Meticulously calculate button presses for each segment. Consider `move_validator_agent` for complex sequences once more familiar with it.
    *   Avoid overshooting coordinates. Be precise.
*   **Map Marker Usage:** 🚫 (dead ends/impassable), 📍 (nav points), 🚪 (used warps), ☠️ (defeated trainers), ❗/💁 (event NPCs/blockers), 🚧 (ledges).
*   **Battle Strategy:** Use `select_battle_option` tool for main battle menu. FLAREE (6 HP) must not battle until healed.

# Party Updates (Pewter City - Turn 5301)
*   SPBARKY (PIKACHU): Lv12 (38/39 HP, EXP: 1728) | Moves: THUNDERSHOCK (29 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP) (Level Cap Reached)
*   FLAREE (VULPIX): Lv8 (6/26 HP, EXP: 704) | Moves: EMBER (12 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP) - Critically low HP. Must be healed before any battles.
*   SPROUT (ODDISH): Lv12 (33/37 HP, EXP: 973) | Moves: TACKLE (30 PP), POISONPOWDER (35 PP), LEECH SEED (10 PP) (Level Cap Reached)

# Key Journey Events & Map Discoveries (Consolidated)
*   **Pewter City Navigation & Events (Ongoing & CRITICAL):**
    *   **Youngster (ID 5) Gym Escort Event:** This NPC (currently at (36,17) per Map Sprites) triggers an escort to the Gym, blocking eastward progress. This has happened repeatedly (Turns ~5247, ~5270, 5287, 5299, 5300). Trigger zones are more extensive/complex than initially assumed. Known/suspected trigger coordinates: (36,17), (35,17), (30,19), (34,19), (36,18), (38,19), (38,20). My mental model of this event is flawed and requires extreme caution.
    *   **New Avoidance Strategy:** Attempt a route significantly further south (e.g., row 26 or 27) to reach Route 3. Use `scripted_event_tracker_agent` for *every single step* once east of X=25. Validate all paths carefully.
    *   **Dynamic Tile Changes:** Certain tiles change state (e.g., column 35, (34,20) Police Sign, (27,15)). Pewter PC non-functional.
    *   **Known Impassable Areas/Blockers:** Column X=22 (rows 22, 25-27), Police Notice Sign (34,20), specific tiles like (19,19-21), (18,18), (15,18), (11,22), (35,21), (35,23).
    *   **Pewter City Trainers (All Non-Battling for Funds / Already Defeated):** JR.TRAINER♂ (Gym, Defeated), Brock (Lost), Cool Trainer M (18,26), Super Nerds (24,26 & 28,18).
*   **Route 2 Exploration:** Caught FLAREE. Navigated ledges. No trainers found for funds yet.
*   **Viridian Forest Training:** SPROUT reached Lv12 cap. FLAREE gained some EXP. Defeated various trainers. Blacked out once.
*   **Early Game:** Pallet Town, Route 1, Viridian City explorations. Delivered Oak's Parcel, got Pokédex.

# Agent Management & Usage Plan
*   **Agents to Define:**
    *   `potion_purchase_optimizer_agent`: Defined.
*   **Agents to Use Proactively:**
    *   `scripted_event_tracker_agent`: For *every step* in eastern Pewter City near Youngster zones.
    *   `route_progress_analyzer_agent`: Upon reaching Route 3.
    *   `battle_log_analyzer_agent`: After next significant trainer battle.
    *   `move_validator_agent`: For complex pathing once more comfortable.
    *   `npc_interaction_planner_agent`: For any crucial NPC interactions.
*   **Agent Ideas (Low Priority / Review):** `team_builder_agent` prompt seems okay for now. (Discarded `rom_hack_mechanics_discoverer_agent` and `battle_strategy_advisor_agent` as per critique to avoid stale notes).
*   **Past Agent Actions:** `notepad_query_agent` defined. Several agents defined/deleted for space previously.

# Inventory & Finances
*   POKé BALL x1
*   Money: ¥156 (Critically Low - need funds for healing FLAREE)

# Pokedex Status
*   Caught: 3/151 (PIKACHU, ODDISH, VULPIX)

# Map Marker Tasks (Pewter City, Map ID 2 unless specified)
*   **Add ❗ (Event Trigger/Obstacle):**
    *   (36,17) - Youngster (ID 5) Escort Trigger (Primary Location)
    *   (35,17) - Youngster (ID 5) Escort Trigger
    *   (30,19) - Youngster (ID 5) Escort Trigger
    *   (34,19) - Youngster (ID 5) Escort Trigger
    *   (36,18) - Youngster (ID 5) Escort Trigger
    *   (38,19) - Youngster (ID 5) Escort Trigger
    *   (38,20) - Youngster (ID 5) Escort Trigger (New)
    *   (34,20) - Police Notice Sign (Dynamic Obstacle)
*   **Add ☠️ (Defeated Trainer):**
    *   PEWTER_GYM (Map ID 3), (4,7) - JR.TRAINER♂ (Cool Trainer M)
*   **Delete Redundant 🚫 Markers (where tile type is already 'impassable' or NPC presence is clear in XML and marker adds no new strategic info):**
    *   (32,13), (18,15), (23,18), (19,20), (12,22), (14,22), (23,24), (31,25), (13,26), (15,26), (20,30), (30,24), (19,19), (26,18), (35,26), (23,17), (18,22), (28,18) (Super Nerd tile).

# Hindsight & Lessons Learned (Critique Incorporated)
*   **Youngster Event (Pewter City):** My avoidance strategies have been consistently ineffective. Future attempts MUST use a route significantly further south (e.g., row 26/27) and employ `scripted_event_tracker_agent` for *every single step* in the eastern half of the city (X > 25). My mental model of his trigger zones is flawed.
*   **Pathing Calculation:** Multi-step path plans often miscalculate button presses vs. game moves. Must break paths into 1-3 logical moves or use `move_validator_agent`. Avoid overshooting coordinates.
*   **Agent Usage:** Must proactively use defined agents (`route_progress_analyzer`, `battle_log_analyzer`) and act on agent definition plans (e.g., `potion_purchase_optimizer_agent`).
*   **Data Integrity:** Always prioritize Game State Information (Map Sprites, XML data) over memory or assumptions, especially for dynamic elements like NPC positions or tile states.

# Pewter City Navigation (Update Turn 5431)
*   Player at (34,21) was blocked by sign at (34,20). Event tracker warned of proximity to Youngster trigger at (34,19). 
*   New plan: Move Down to (34,22) (Pikachu's tile, requires 2 Down presses due to facing Up). Then Left to (33,22), then Up to (33,19). Will use `scripted_event_tracker_agent` before moving from (33,19) towards (34,19) due to known trigger at (34,19).