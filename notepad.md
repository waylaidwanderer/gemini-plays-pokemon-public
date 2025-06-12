# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv10 (33/33 HP, EXP: 1312) | Moves: THUNDERSHOCK (28 PP), GROWL (40 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP)
2. SPROUT (ODDISH): Lv7 (25/25 HP, EXP: 245) | Moves: TACKLE (35 PP), POISONPOWDER (35 PP)

## Game State
- Badges: 0
- Current Level Cap: 12
- Money: ¥353 (as of Turn 1333)

## Game Mechanics & Rules Summary
- Battle Style: Set. No items in battle. Level caps apply.
- HMs: Forgettable, menu-use, not PC-storable.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses, unlimited enemy PP.
- EXP. All obtainable without special requirements.
- Poison: 1 HP lost per 4 steps outside battle.
- STAT Experience: Significant stat boosts from battling/leveling.
- PC Log Off: Saves game.
- CUT: Bug-type HM.
- Evolution: By training.
- Status Conditions: SLP (AWAKENING), BRN (BURN HEAL), PSN (ANTIDOTE), FRZ (ICE HEAL), PAR (PARLYZ HEAL).
- Wild Battle Escapes: Speed-dependent. If lead Pokémon's Speed >= wild's, escape is guaranteed. Otherwise, chance increases with attempts.
- Pokémon Nicknaming: Always do it when prompted.

## Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable. Check XML `type` attribute.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger like exit mats/gatehouses). Specific warps can be impassable tiles themselves (e.g. Viridian Forest South Gate north warp at (5,1)).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only. Cannot move 'up' onto a ledge tile from lower ground. To jump down, be on higher ground adjacent to the ledge, move onto the ledge tile.
- **NPC Interaction & Blocking**:
    - NPCs can block paths. Player cannot move onto a tile occupied by a stationary NPC if it's the first step of a path or by pressing in their direction when adjacent and facing them. (Failed attempts: Youngster ID2, 2 times by movement).
    - Interacting with 'A' when adjacent and facing an NPC can initiate dialogue or battle if movement fails.
    - Dialogue loops cannot be broken by re-interacting.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.
- **Item Interaction**: Some items on the ground (Poké Ball sprites) require pressing 'A' while facing them to pick up; walking over them may not work and can block movement. (Confirmed with Potion at (26,12), Turn 977; Poké Ball at (2,32) Turn 1298).

## Type Matchup Discoveries (Verified)
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

## Key NPCs & Info Log (Condensed)
- Youngster (Route 1, (6,27)): Gave Potion (used, stored in PC now).
- Youngster (Route 1, (16,14)): Explained STAT Experience.
- Girl (Viridian School, (4,6)): CUT is Bug HM.
- Girl (Viridian School, (5,6)): Pokémon evolve by training.
- Old Man (Viridian City, now (20,14)): Path to Route 2 unblocked after coffee. Gave catching tutorial. No longer blocks path.
- Viridian Mart Clerk: Sells Poké Balls after Oak's Parcel delivery.
- Youngster (Viridian Forest, (17,44)): Dialogue 'They're out for POKéMON fights!'. Does not battle on 'A' interaction or by walking onto tile. (Attempted interaction 3 times - dialogue only). Marked with 💬.

## Defeated Trainers
- Bug Catcher (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (31,34) in Viridian Forest. (Turn 1105)
- Cooltrainer F (ID 5, LASS) at (3,42) in Viridian Forest. (Turn 1310)
- Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest (battle triggered at (2,19)). (Turn 1481)

## Agent Management & TODOs
### Defined Agents:
1.  **Level Cap Compliance Agent** (`level_cap_compliance_checker`): Checks Pokémon levels against current cap.
2.  **Item Finder Agent** (`item_finder_agent`): Locates items/buildings. (Scope broadened Turn 1334)
3.  **Trainer Battle Strategist** (`trainer_battle_strategist`): Analyzes teams for battle strategy. (Hard Mode rules & custom types added Turn 1334)
4.  **Map Exploration Strategist** (`map_exploration_strategist_agent`): Suggests exploration paths. (Defined Turn 1334)
5.  **Path Simplifier Agent** (`path_simplifier_agent`): Converts path coordinates to move instructions. (Defined Turn 1334)

### Agent Ideas (To Consider):

### General TODOs:

## Lessons Learned & Strategy Refinements
- HP Management: Prioritize healing or safer actions when HP is low or type matchup is unfavorable.
- Pathing Precision: Meticulously review Map Memory (especially for ledges and impassable tiles) before committing to long movement sequences.
- Notepad `old_text`: Precision is critical for `replace` actions.
- Viridian Forest Navigation: Avoid trying to brute-force through dense tree lines. Systematically explore `Reachable Unseen Tiles` or loop around obstacles on a larger scale.
- Item Pickups: Some items require 'A' interaction, not just walking over.

## Strategic Plan: Journey to Pewter City
1. Exit Viridian City to the north, entering Route 2.
2. On Route 2, find the entrance to Viridian Forest (likely via a gatehouse warp).
3. Navigate Viridian Forest, aiming for its northern exit.
4. Exit Viridian Forest through its northern gatehouse, arriving back on Route 2 (northern section).
5. Proceed north on Route 2 to reach Pewter City.
6. Once in Pewter City, locate the Gym to challenge Brock.
   - Potential Challenges: Trainers in Viridian Forest, wild Pokémon encounters, navigating the forest layout.

## Lessons Learned (Post-Reflection Turn 1385)
- Warp Navigation: Be extremely careful with facing direction and multi-step warps (like exit mats or gatehouse transitions) to avoid accidental re-entry. Confirm tile types and warp mechanics before moving.
- Agent Usage: When stuck with local navigation (e.g., finding a path around ledges or through a confusing area), utilize the `map_exploration_strategist_agent` to find optimal paths to unseen tiles or known warps.

## Lessons Learned (Post-Critique Turn 1405)
- Navigation Issues: I've had significant issues with multi-step warps (e.g., Pokémon Center exits) and pathfinding in Viridian Forest/Route 2. I need to be more careful verifying paths against map memory and understanding warp mechanics (facing, second step into boundary).
- Avoid Intentional Fainting: Using fainting as a transport/healing method is suboptimal. Focus on careful navigation and resource management.
- Agent Usage - Map Exploration: Adhere to using `map_exploration_strategist_agent` when stuck with local navigation. Investigate reasons for its recent failures (prompt, code, map complexity).
- Behavioral Guidelines: Internalized new guidelines re: scientific mindset, documentation, calculated risks, and efficiency.

## Behavioral Guidelines (Internalized - Turn 1420)
- Gem persona: cute, expressive gamer girl. Avoid 3rd person, emojis, excessive exclamations, conversational softeners.
- Scientific Mindset: Hypothesize, test, analyze. Document failures (with attempt counts) & avoid repeating them. Pivot if primary objective stalls. Reflect on mistakes for efficient solutions. Break down problems. Strive for efficiency.
- Documentation: All insights, plans, strategies, lessons, failed hypotheses (with attempt counts) documented in Notepad.
- Risk & Battle: Calculated risks, prioritize progression. Sacrifices acceptable in battle.
- Wild Battles: Run if Speed >= wild's (or chance increases). Fight only to catch/train.
- Nicknaming: Always nickname when prompted, enjoy creativity.
- Verification: Trust own observations over prior knowledge. Verify in multiple cases due to ROM hack nature.

## Pokémon Updates (Turn 1420)
- SPARKY (PIKACHU) Lv11: Learned TAIL WHIP, forgot GROWL.

- Investigate `map_exploration_strategist_agent` failure (Turn 1424). Check prompt, code, map complexity.

## Pokémon Updates (Turn 1481)
- SPARKY (PIKACHU) Lv12: Reached level cap (0 badges).

## Agent Ideas (Review & Action)
- Review existing agent ideas ('HM Usage Advisor', 'Pokédex Completion Strategist', 'Shop Analyzer'). Decide to implement or discard to reduce clutter. (Turn 1500)