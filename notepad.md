# Gem's Pokémon Crystal Adventure!

## Current Mission
- **Primary Objective:** Return to Professor Elm's lab in New Bark Town with the MYSTERY EGG.

## Game Mechanics & Quirks
- **Headbutt Trees:** Some trees are 'HEADBUTT_TREE' type and are impassable.
- **Dialogue Triggers:** Some dialogues might loop until another specific NPC in the room is spoken to (e.g., Elm's Lab).
- **Wild Encounters:** Can be triggered on 'FLOOR' tiles if they are adjacent to 'TALL_GRASS' tiles. (Observed on Route 30).
- **One-Way Paths:** The gatehouse between Route 29 and Route 46 appears to be a one-way path. After exiting into Route 29, the door becomes a wall.
- **Buggy Battle:** The trainer battle with the Youngster at (5, 26) on Route 30 was buggy. It got stuck in a dialogue loop and then ended abruptly by moving my character. If this happens again, I should try moving the cursor in the battle menu as a diagnostic step.

## Agent Performance & Lessons
- **Trust Agents:** I must trust my agents' calculations over my own intuition, especially when they suggest a counter-intuitive path.
- **Systematic Updates:** When a new game mechanic is discovered (e.g., an impassable tile type), ALL relevant agents must be updated immediately to prevent repeated errors.

## World Knowledge & NPCs
- **New Bark Town:** A Fisher at (12, 9) mentioned Prof. Elm discovered new Pokémon.

## Unverified Assumptions & Hypotheses
- **Mom's Healing:** Can Mom heal my Pokémon?
- **Ledge Mechanics:** Are ledges in this ROM hack strictly one-way?
- **Youngster Block:** The Youngster at (27, 16) on Route 29 was a temporary obstacle that moved after the Mr. Pokémon quest was initiated.
- **Cherrygrove Mart:** Is the Poké Mart still inaccessible?

## To-Do & Reminders
- **WKG Data Integrity:** Only record data in the World Knowledge Graph that is directly confirmed from the Game State Information. Do not assume values like `destination_entry_point`.

- **Shifting Route:** Route 29 appears to be a dynamic map where tiles change every few steps, requiring constant re-routing.

## Unverified Assumptions & Hypotheses (Post-Reflection)
- **Route 29 Shifting:** Is it truly random, or is there a pattern (time-based, step-based)?
- **Teacher on Route 29:** Does the Teacher at (15, 11) have information about the shifting route?
- **Alternate Paths:** Is there a more stable, alternative route to New Bark Town that I've missed?
- **Pathfinder Limitations:** Could the pathfinder be given constraints (e.g., avoid certain zones) to find a better, if not shorter, path?

- **Failed Hypothesis:** The Teacher at (15, 11) on Route 29 does not provide information about the shifting tiles. Interaction failed despite being adjacent and facing her.