# 1. Party Composition & Strategy
- **SPARKY (Pikachu):** Electric Sweeper. Fast, good for paralysis support.
- **SPROUT (Oddish):** Grass/Poison Utility. Good for status effects (Stun Spore, Leech Seed).
- **THISTLE (Nidoran♀):** Physical Attacker. Double Kick is key for Rock types.
- **PIP (Pidgeotto):** Flying Attacker. Good speed and decent damage.
- **PARCH (Sandshrew):** Ground Type. Under-leveled, has Dig.
- **SHELLSHOCK (Squirtle):** Water Type. Gift Pokémon, in PC.
- **LUMIN (Clefairy):** Normal Type. In PC.

# 2. S.S. Anne - Current Objective
- **Primary Goal:** Find the Captain on an upper deck to get HM CUT.
- **Secondary Goal:** Find the stairs leading to the upper decks.
- **Key Discoveries:**
    - **HM STRENGTH:** A Super Nerd on B1F (Room entered from (24,4)) mentioned his Machoke has STRENGTH to move big rocks. This is likely the HM.
    - **Waiter (2F, (4,5)):** Does not provide healing. I need to find the correct rest spot.
    - **Rival:** A battle with BLAZe is expected before reaching the Captain.

# 3. General Gameplay Insights
- **Systematic Exploration:** Verify location names (`map_id`) after warping *before* documenting.
- **NPC Interaction:** Non-battling/defeated trainers are impassable walls. Some event NPCs offer gifts.
- **Game Mechanics:**
    - Poison deals 1 HP damage every 4 steps.
    - Level-capped Pokémon show fake EXP gain.
    - Non-volatile status conditions are cured after trainer battles.
    - PC System: 'SOMEONE's PC' is for Pokémon, 'Gem's PC' is for Items.
    - HM CUT: Used by pressing 'A' on a tree, not from a menu.

# 4. Battle Intel
## Gym Leaders
- **Brock (DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Misty (DEFEATED):** Psyduck (Lv 19), Goldeen (Lv 18), Starmie (Lv 21).
## Rival BLAZe
- **@ Cerulean City:** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).

# 5. Untested Hypotheses & Plans
- **Underground Path Item:** Girl mentioned people lose things in the tunnel.
- **Saffron City Access:** The gatehouse guard is thirsty. I probably need to find him a drink.

# 6. Agent Development Log
- **Pathfinder Agent Failures (S.S. Anne):** The agent has repeatedly failed on this ship.
    - **1F Failure:** Failed to find path from (32, 9) to (37, 9).
    - **B1F Failure:** Failed to path around a defeated Sailor at (3, 14), treating him as walkable.
- **Pathfinder Agent Overhaul:** The agent's system prompt has been rewritten to explicitly treat ALL objects (including defeated trainers) as impassable, with Pikachu as the only exception. This needs to be tested.

# 7. Training Goals
- **Post S.S. Anne:** PARCH (Lv 12) and THISTLE (Lv 16) need training.

# 8. Item & TM Usage Plan
- **TM44 (Rest):** Plan to teach to PARCH, replacing POISON STING.
- **TM08 (Body Slam):** Plan to teach to THISTLE, replacing Tackle.

# 9. Future Agent Ideas
- **Progression Blocker Agent:** An agent to analyze key items, map data, and NPC dialogue to identify specific requirements for overcoming story-based obstacles (e.g., the thirsty Saffron guard).