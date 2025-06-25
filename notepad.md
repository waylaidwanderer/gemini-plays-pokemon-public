# Gem's Pokémon Crystal Adventure!

## Game Mechanics & Quirks
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles (Observed on Route 30).
- **Ledge Mechanics:** Can move sideways (left/right) along 'HOP_DOWN' tiles. Jumping down ledges is a one-way action.
- **'Shadowing' NPCs:** Some NPCs follow the player onto the same tile, preventing direct interaction. They are not solid obstacles; the player can move through them, and the NPC will simply teleport to the new tile. (Observed on Route 30 and in New Bark Town).

## Lessons Learned
- **Agent Refinement is Key:** Agents are not perfect on the first try. Trust, but verify and refine.
- **Trust Documentation:** My own map markers and notes are reliable.
- **Pivoting Strategy:** When all documented paths are confirmed blocked, I must pivot to a new hypothesis rather than repeating failed attempts. Stagnation is inefficiency.
- **World Knowledge Graph:** I MUST use `manage_world_knowledge` to record every inter-map transition immediately.
- **One-Way Routes:** Both Route 30 and Route 46 are one-way paths from north to south, making it impossible to travel north from Cherrygrove City via these routes. This was confirmed by my `map_analyst` agent and manual verification.

## Re-Exploration Plan
My path north is blocked. I will systematically re-explore all known locations to find a new way forward.

### Checklist & Plan:
- **[X] New Bark Town (24_4):**
  - [ ] Interact with Teacher at (0, 9). (Attempt failed due to shadowing bug).
  - [X] Re-check Elm's Lab (24_5). (Completed - no new info).
  - [X] Re-check my house (24_6, 24_7). (Interaction with Mom is impossible due to a persistent shadowing bug. All other interactables checked. Concluding this location is fully explored for now.)
  - [X] Re-check Elm's house (24_9). (Completed - Teacher NPC has a persistent shadowing bug, preventing interaction. Other objects already checked.)
- **[ ] Route 29 (24_3):**
  - [ ] Re-check all NPC dialogue.
  - [ ] Investigate the CUT tree at (30, 9) again.
- **[ ] Route 46 (5_9):**
  - [X] Confirmed one-way path south. No further exploration needed here.
- **[ ] Cherrygrove City (26_3):**
  - [ ] Re-check all NPC dialogue in every house (26_5, 26_6, 26_7, 26_8).
  - [ ] Re-check the Guide Gent at (32, 6).
- **[ ] Route 30 (26_1):**
  - [X] Confirmed one-way path south. No further exploration needed here.
  - [ ] Re-check Mr. Pokémon's House (26_10) and Berry House (26_9).

## Pokémon Locations
- **Route 34:** Jigglypuff (Source: Radio)
- **Route 42:** Raticate (Source: Radio)
- **Route 45:** Graveler (Source: Radio)

## Current Bugs & Blockers
- **Shadowing NPCs:** Certain NPCs (Mom, Teacher in Elm's House, Fisher in New Bark) will occupy the same tile as the player, preventing interaction. Leaving and re-entering the map does not seem to fix this consistently.

- **Cooltrainer & Youngster (Route 29):** Both exhibit the shadowing bug, preventing interaction.