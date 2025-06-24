# Gem's Pokémon Crystal Adventure!

## Current Plan & Strategy
- **Current Objective:** Explore Route 46 to find a path to Cherrygrove City.

## Discoveries & Mechanics
- **Headbutt Trees:** Some trees are 'HEADBUTT_TREE' type, likely for the move Headbutt.
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).

## World Knowledge & NPCs
- **New Bark Town:** A Fisher at (12, 9) mentioned Prof. Elm discovered new Pokémon.
- **Route 29:** A Youngster at (27, 16) is blocking the southern path. Interaction attempts from multiple sides have failed.

## Lessons Learned
- **Check Notes:** Be diligent about checking my own notes and map markers before exploring to avoid getting lost on already-identified dead ends.
- **Pivot Faster:** If a path is blocked by an unmovable/un-interactive NPC after 1-2 attempts, assume it's a story-based barrier and pivot to exploration instead of repeatedly trying to get past.

## Unverified Assumptions & Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon?
- **Ledge Mechanics:** Are ledges in this ROM hack strictly one-way?
- **Youngster Block:** The Youngster at (27, 16) is a temporary obstacle that will move after a future story event is triggered.

## Agent Development Notes
- **Consolidate Agents:** The `map_scout_agent` and `town_explorer_agent` have redundant functions. I should merge them into a single, more flexible `exploration_agent`.