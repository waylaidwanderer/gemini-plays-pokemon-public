# Gem's Strategic Journal (v119 - Battle Housekeeping)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Agent Liability:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location, not during a critical battle. Obsessing over a broken tool mid-crisis is a recipe for failure.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*.
- **Tool-First Mindset:** For any complex or repetitive task (like pathfinding), use an agent first. Manual attempts should only be a last resort.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:**
  - Psychic is SUPER-EFFECTIVE against Ghost/Poison.
  - Ghost is SUPER-EFFECTIVE against Psychic.
  - Bite (Normal) is SUPER-EFFECTIVE against Psychic.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.

## III. Active Plans & Hypotheses
### **Current Plan: Pokémon Tower Ascent**
1.  **Situation:** Ascending the Pokémon Tower to rescue Mr. Fuji.
2.  **Action Plan:**
    a. Continue climbing the tower, floor by floor.
    b. Battle trainers and navigate the maze-like floors.
    c. Use my team strategically, leveraging newly discovered type matchups.

### Long-Term Goals & Hypotheses
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v1 - RELIABLE):** Consolidated agent for reaching specific targets or exploring all unseen tiles.
- **`wkg_manager_agent` (v2 - RELIABLE):** Successfully identifies existing nodes and creates edges without duplication.
- **`pc_navigator_agent` (v2 - RELIABLE):** Successfully navigates the PC by using 'BILL's PC' to bypass the 'Gem's PC' glitch.

### B. Agent Development Backlog
- **(Future Idea): `shopping_planner_agent`:** To plan TM and item purchases.
- **(Future Idea): `item_finder_agent`:** To plan paths for collecting all items on a map.
- **(Future Idea): `healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.
- **(Future Idea): `battle_strategist_agent`:** To provide real-time battle advice, considering known type matchups and opponent movesets.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Selecting 'Gem's PC' is bugged and unusable. The correct and reliable method to access Pokémon Storage is to select 'BILL's PC' from the main menu.
- **Pokémon Tower 5F Healing Spot (13, 9) is FAKE:** The Channeler offers dialogue but does NOT heal the party. Do not rely on this spot.

  - Normal is NOT-VERY-EFFECTIVE against Psychic.

### Pokémon Tower 6F Battle Intel
- **Channeler at (17,6) Battle:** Defeated their Lv33 Hypno, but ultimately lost the battle and blacked out against their second Pokémon, a Lv33 Haunter. The trainer is NOT fully defeated and I will need to battle them again.
  - The Hypno was surprisingly fast and powerful, capable of knocking out my level-capped Pokémon. It knows Psychic and Confusion.
  - The Haunter knows Smog, Lick, and Confuse Ray.

- Pokémon Tower 5F has a high wild encounter rate. Be prepared to run frequently.
- There is a purified healing zone at (12, 10) on 5F that fully heals the party upon entering the tile.

## Critical Oversights & Lessons
- **Poké Ball Stock:** I encountered a wild Cubone (a catch target) and had ZERO Poké Balls. I must always maintain a healthy stock of Poké Balls to avoid missing rare encounters. This was a major failure in preparation.