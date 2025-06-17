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
- **Pathfinder/Map Explorer Agents:** These agents are fundamentally flawed. They repeatedly fail to navigate simple maps (Vermilion City, Fan Club) by attempting to path through water or getting blocked by what appear to be invisible barriers. They require a complete overhaul. Refinements to prompts have been ineffective.

## 7. The Fan Club Paradox
- **Problem:** Game state insists tiles on the west side of the Fan Club are 'reachable', but all manual and agent-based attempts to cross the room have failed over ~20 turns. This suggests an invisible barrier or a non-obvious trigger is required to proceed.
- **Hypothesis 1 (Failed):** Path exists around the southern edge of the furniture. (Attempted ~5 times, failed).
- **Hypothesis 2 (New):** Interacting with my own Pikachu is the trigger to unblock the path.