# Pokémon Crystal Journey

## Current Plan
- **Objective:** Visit Mr. Pokémon on Route 30.
- **Route:** Head north from Cherrygrove City to find the entrance to Route 30. Explore the route until I find Mr. Pokémon's house.

## Current Quest
- Visit Mr. Pokémon on Route 30, past Cherrygrove City, for Professor Elm.

## Long-term Goal
- Become the Pokémon League Champion.

## Mechanics & Discoveries
### System Mechanics
- **POKéGEAR:** Received from Mom. Has a Phone feature.
- **Warp Mechanics:** Some warp tiles may require stepping off of them and then back on to activate.
- **Pokémon Evolution:** Pokémon gain experience in battle and can change their form (evolve).
### Environmental Mechanics
- **Route 29 Ledges:** The western section of Route 29 has one-way ledges preventing eastward travel from that area.
- **Route 46:** This route is a dead-end when approached from the south due to one-way ledges.
- **CUT_TREE:** These small trees are impassable and require the HM 'Cut' to be removed.
### Battle Mechanics
- **Held Items (Berries):** Some Pokémon can hold items like Berries, which they can use automatically in battle to heal themselves when their HP gets low.
- **Smokescreen:** Lowers the opponent's accuracy.
### Item Effects
- **POTION:** Heals a Pokémon for 20 HP.

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

## Radio Broadcasts
- **Professor Oak's Pokémon Talk:** Abra may be seen around Route 35.

## Puzzle Solutions
- **Cherrygrove House Lock:** Became stuck at (3, 1). Solution was to turn to face the TV at (2, 1) and interact with it ('A' button). This triggered a text box, and after closing it, movement was restored.

## Self-Corrections & Failed Hypotheses
- The path to Cherrygrove City is through Route 29. My initial assumption that it was a dead end was incorrect.

## Agent & Exploration Plan
- Design a new `situational_awareness_agent` that combines exit analysis with general exploration data to replace the `route_analyzer_agent`.
- Explore the unvisited houses in Cherrygrove City: the one at (17, 7) and the Guide Gent's house at (25, 9).