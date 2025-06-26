# Pokémon Crystal Journey

## Current Quest
- Visit Mr. Pokémon on Route 30, past Cherrygrove City, for Professor Elm.

## Long-term Goal
- Become the Pokémon League Champion.

## Mechanics & Discoveries
- **POKéGEAR:** Received from Mom. Has a Phone feature.
- **POTION:** Heals a Pokémon for 20 HP.
- **Route 29 Ledges:** The western section of Route 29 has one-way ledges preventing eastward travel from that area.
- **Held Items (Berries):** Some Pokémon can hold items like Berries, which they can use automatically in battle to heal themselves when their HP gets low.
- **Smokescreen:** Lowers the opponent's accuracy.
- **CUT_TREE:** These small trees are impassable and require the HM 'Cut' to be removed.
- **Warp Mechanics:** Some warp tiles may require stepping off of them and then back on to activate.
- **Self-Correction:** The path to Cherrygrove City is through Route 29. My initial assumption that it was a dead end was incorrect.
- **Route 46:** This route is a dead-end when approached from the south due to one-way ledges.

## Agent Development
- **`exploration_agent`:** This agent has required multiple refinements.
  - **v1:** Failed to avoid obstacles like 'HEADBUTT_TREE'.
  - **v2:** Failed to avoid 'WALL' tiles.
  - **v3:** Generated inefficient, looping paths.
  - **v4:** Failed by pathing into a HEADBUTT_TREE.
  - **v5:** Failed again by pathing into a HEADBUTT_TREE due to a contradictory prompt.
  - **v6:** Clarified that 'unseen' tiles are obstacles and cannot be part of the path.
- **`pathfinder_agent`:** Refined to correctly treat 'unseen' tiles as traversable.

## Wild Pokémon Encounters
### Route 29 (Tall Grass)
- **Hoppip** (Lv. 2-3): Knows Splash
- **Sentret** (Lv. 2-3): Knows Tackle
- **Pidgey** (Lv. 2-3): Knows Tackle
- **Rattata** (Lv. 2): Knows Tackle
- **Hoothoot** (Lv. 3): Knows Tackle

## Important NPCs
- **Professor Elm** (New Bark Town): Gave me Hestia and his phone number.
- **Mom** (New Bark Town): Gave me the POKéGEAR.
- **MR. POKEMON** (Route 30): Elm's acquaintance.

- **Pokémon Evolution:** Pokémon can gain experience in battle and change their form (evolve).