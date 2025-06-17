## 1. Party Composition & Strategy
- **SPARKY (Pikachu):** Electric Sweeper. Fast, good for paralysis support.
- **SPROUT (Oddish):** Grass/Poison Utility. Good for status effects (Stun Spore, Leech Seed).
- **THISTLE (Nidoran♀):** Physical Attacker. Double Kick is key for Rock types.
- **PIP (Pidgeotto):** Flying Attacker. Good speed and decent damage.
- **PARCH (Sandshrew):** Ground Type. Currently under-leveled.
- **LUMIN (Clefairy):** Normal Type. Currently in PC storage.
- **SHELLSHOCK (Squirtle):** Water Type. Newly acquired gift Pokémon, waiting to be added to party.

## 2. Gameplay Insights & Lessons
- **Systematic Exploration:** Verify location names (`map_id`) after warping *before* documenting. Avoid assumptions.
- **NPC Interaction:** Non-battling/defeated trainers are impassable walls. Some event NPCs offer gifts.
- **Game Mechanics:**
    - Poison deals 1 HP damage every 4 steps and can cause fainting.
    - Level-capped Pokémon show EXP gain, but it's a visual bug (no actual gain).
    - Non-volatile status conditions are cured after trainer battles.
    - PC System: 'SOMEONE's PC' is for Pokémon, 'Gem's PC' is for Items.
    - HM CUT: Used by pressing 'A' on a tree, not from a menu.
- **Agent Refinement:** Agents require precise instructions. Faulty agent logic (e.g., pathing through water) must be corrected immediately by refining system prompts.

## 3. Battle Intel
### Gym Leaders
- **Brock (DEFEATED):** Geodude (Lv 12), Onix (Lv 14).
- **Misty (DEFEATED):** Psyduck (Lv 19), Goldeen (Lv 18), Starmie (Lv 21).

### Rival BLAZe
- **@ Cerulean City:** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).

## 4. Key NPCs & Events
- **Bill (Route 25):** Gave S.S. Ticket after being cured.
- **Cerulean Rocket:** Stole TM28 (DIG), was defeated, opening path south.
- **Officer Jenny (Vermilion City):** Gave a gift Squirtle.
- **Pidgey House Kid (Vermilion City):** Mentions Team Rocket problems in Saffron City.

## 5. Untested Hypotheses & Plans
- **Underground Path Item:** Girl mentioned people lose things in the tunnel. Could be a hidden item.
- **Saffron City Access:** The gatehouse guard is thirsty. I probably need to find him a drink to pass.

## 6. Agent Development Log
- **Pathfinder Agent Overhaul:** The agent's pathing logic fails consistently on complex indoor maps (Fan Club, S.S. Anne). The issue seems to be its inability to correctly identify walkable paths around furniture and internal walls. Plan: A major system prompt rewrite is required. The new prompt will give the agent's Python script explicit, step-by-step instructions for building its impassable tile set, including handling objects, defeated trainers, and special cases like Pikachu. This should fix the core logic flaw.

## 7. The Fan Club Paradox (SOLVED)
- **Resolution:** The 'reachable' data was correct. The pathing agents were fundamentally flawed for this map layout, creating the illusion of an invisible wall. After numerous failed attempts, a careful manual path around the southern edge of the room successfully navigated to the west side. The Chairman provided the BIKE VOUCHER after listening to his story.

## 8. Training Goals
- **Post S.S. Anne:** PARCH (Lv 12) and THISTLE (Lv 16) are significantly under-leveled. A dedicated training session is needed to bring them up to par with the rest of the team.