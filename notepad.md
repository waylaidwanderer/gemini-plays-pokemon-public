# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv12 (38/38 HP, EXP: 1728) | Moves: THUNDERSHOCK (22 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (18 PP) - AT LEVEL CAP (0 Badges)
2. SPROUT (ODDISH): Lv7 (25/25 HP, EXP: 245) | Moves: TACKLE (35 PP), POISONPOWDER (35 PP)
3. PIP (PIDGEY): Lv7 (23/23 HP, EXP: 236) | Moves: GUST (35 PP), SAND-ATTACK (15 PP)

## Game State
- Badges: 0
- Current Level Cap: 12 (Next: 21 after 1st badge)

## Current Financial Status & Needs
- Money: ¥33 (Critically Low!)
- Needs: Earn Pokedollars for Potions, Poké Balls, other essentials.

## Training Priorities
- SPROUT (ODDISH): Lv7 -> Needs significant training for Brock (Rock/Ground).
- PIP (PIDGEY): Lv7 -> Needs training.
- SPARKY (PIKACHU): At cap, less effective vs Brock.

## Game Mechanics & Rules Summary
- Battle Style: Set. No items in battle. Level caps apply.
- HMs: Forgettable, menu-use, not PC-storable. CUT is Bug-type.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses, unlimited enemy PP.
- EXP. All obtainable without special requirements.
- Poison: 1 HP lost per 4 steps outside battle.
- STAT Experience: Significant stat boosts from battling/leveling.
- PC Log Off: Saves game.
- Evolution: By training.
- Status Conditions: SLP (AWAKENING), BRN (BURN HEAL), PSN (ANTIDOTE), FRZ (ICE HEAL), PAR (PARLYZ HEAL).
- Wild Battle Escapes: Speed-dependent. If lead Pokémon's Speed >= wild's, escape is guaranteed. Otherwise, chance increases with attempts.
- Pokémon Nicknaming: Always do it when prompted.
- DV Checking: Hold START, then press A on STATS in Pokémon menu.

## Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger like exit mats/gatehouses).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only.
- **NPC Interaction & Blocking**: Dialogue loops cannot be broken by re-interacting. NPCs can block paths.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.
- **Item Interaction**: Some items require 'A' interaction.

## Type Matchup Discoveries (Verified)
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

## Defeated Trainers
- Bug Catcher (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (31,34) in Viridian Forest. (Marker ☠️ set)
- Cooltrainer F (ID 5, LASS) at (3,42) in Viridian Forest. (Marker ☠️ set)
- Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest (battle triggered at (2,19)). (Marker ☠️ set)

## Agent Management & TODOs
### Defined Agents:
1.  **Level Cap Compliance Agent** (`level_cap_compliance_checker`)
2.  **Item Finder Agent** (`item_finder_agent`)
3.  **Map Exploration Strategist** (`map_exploration_strategist_agent`)
4.  **Path Simplifier Agent** (`path_simplifier_agent`)
5.  **WKG Transition Recorder Agent** (`wkg_transition_recorder_agent`)

### Agent Development - Prioritized:
1.  **Capability Checker Agent**: Implement next. (Input: HMs, badges, obstacle. Output: Can pass?)

### Agent Development - Future Consideration:
-   **Pokédex Completion Strategist**: Suggests where to hunt for new Pokémon. (Idea retained, low priority)

### Agent Review TODOs:
- `map_exploration_strategist_agent`: Review prompt/code due to frequent failures. Default to manual pathing if unreliable. **Decision: Review prompt after exploring Nidoran House, before seeking Gym.**
- `item_finder_agent`: Review prompt for better city building identification. Review utility - may delete if not serving purpose. **Decision: Review prompt and utility after exploring Nidoran House. If still unreliable, will delete.**

### General TODOs:
- Systematically mark used warps (both ends) with 🚪 emoji, noting destination map and coordinates/entry point, using WKG for reference. **(Active)**
- Actively seek info on Brock's Pokémon types/weaknesses. **(Active)**
- Be more proactive in using map markers for key NPC info (ℹ️) or strategic points. **(Active)**
- Prioritize earning money (currently ¥33) and training SPROUT (Lv7) & PIP (Lv7) once Pewter City is further explored. **(High Priority)**
- Develop a concrete training plan for SPROUT and PIP for Brock. **(High Priority)**

## Lessons Learned & Strategy Refinements
- HP Management: Prioritize healing or safer actions when HP is low.
- Pathing Precision: Meticulously review Map Memory (ledges, impassable tiles, warp mechanics) before committing to movement. **Verify current map_id and position from Game State frequently, especially after warps, to avoid hallucinations.**
- Notepad `old_text`: Precision is critical for `replace`.
- Warp Navigation: Be careful with facing direction and multi-step warps. Confirm tile types and warp mechanics. If an NPC is on a warp tile, try the other tile of a 2-wide warp or path around.
- Agent Usage: If an agent is unreliable, default to manual planning. Consider agents for specialized 'thinking' tasks or to automate repetitive WKG updates.
- WKG Workflow: Use the `wkg_transition_recorder_agent` for all inter-map transitions. Capture node IDs from `add_node` calls to streamline edge creation if doing manually.
- Nicknaming UI: Pay closer attention to avoid errors.
- Failed Hypotheses: Document attempts and number of failures. E.g., Exiting Pewter Mart - numerous failed attempts due to mislocating self or NPC blocking specific warp tiles. Successfully exited Pewter Mart by careful verification of map state, NPC positions, and adaptive pathing.

## Pewter City Exploration & Brock Prep Plan (Current Focus)
- **Immediate (Post-Museum):** Systematically explore all reachable unseen areas of Pewter City. Interact with ALL NPCs to find trainers to battle for money and EXP. Mark defeated trainers.
- **Training Strategy:** 
    - Prioritize SPROUT (Oddish) and PIP (Pidgey).
    - Identify trainers in Pewter City or on Route 2 (south of Pewter, if accessible and suitable) for EXP.
    - If wild Pokémon are the only option, target Pokémon SPROUT has an advantage against (e.g., Geodude if found, though unlikely before Brock). PIP can handle Bug/Grass types if any are present.
    - Aim for Lv10-12 for both SPROUT and PIP initially, then reassess based on Brock's known team.
- **Financial Strategy:**
    - Defeat every available trainer in Pewter City and nearby accessible routes.
    - Current funds: ¥33 (CRITICALLY LOW). Need at least ¥500-¥1000 for Potions and more Poké Balls.
- **Information Gathering (Brock):**
    - Ask NPCs in Pewter City about Brock, his Pokémon types (likely Rock/Ground), and any known weaknesses.
    - Check the Pewter Gym for any posted information or trainers who might give hints.
- **Item Acquisition:** Look for any free items or TMs in Pewter City that could aid against Rock/Ground types.

## Museum 1F Notes
- Entered from Pewter City (15,8) to Museum 1F (11,8).
- Ticket to main exhibit costs ¥50. Cannot afford with ¥33. Declined entry.
- Exploring alternative paths and the unvisited warp at (8,8).

- Museum 1F: After closing dialogue with the ticket seller (at (11,5)), player character is sometimes repositioned (e.g., from (10,5) to (10,6)). This is likely standard post-dialogue character repositioning, not a special 'pushback mechanic' or unique property of tile (10,5). Repeatedly triggered dialogue with ticket seller (turns 1735-1752+) due to not moving away from interaction zone after declining. Need to ensure moving clear of the counter area to avoid re-triggering.

## Museum 1F - Abandoned West Wing Exploration (Turn 1771)
- After a prolonged loop (approx. turns 1733-1770, over 30 turns) trying to navigate past the ticket seller at (11,5) and the tricky tile (10,5) to reach the unvisited warp at (8,8) in Museum 1F due to insufficient funds (¥33 vs ¥50 ticket), I've decided to abandon exploring that section for now.
- Exited Museum 1F via the (11,8) warp, arriving back in Pewter City at (15,8).
- Will re-evaluate museum exploration once I have more money or a clearer path. Current focus is exploring Pewter City itself.

## Pewter Nidoran House (Turn 1796)
- Entered Pewter Nidoran House (ID 55) from Pewter City (ID 2) via warp at (30,14) in Pewter City, arriving at (3,8) in Nidoran House (EP4). WKG updated.
- Current plan: Explore this house, interact with NPCs (Little Boy at (4,6), Nidoran M at (5,6)).
- Reminder: Prioritize reviewing `map_exploration_strategist_agent` and `item_finder_agent` prompts soon.

- Traded Pokémon (outsiders) grow fast but might ignore unskilled trainers. BADGEs help ensure they obey. (Learned in Pewter Nidoran House)

- Cooltrainer M at (18,26) in Pewter City mentioned Brock is 'totally into it!' (non-battling NPC).