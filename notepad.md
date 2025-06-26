# Pokémon Crystal Journey

## Current Plan
- **Objective:** Return to Professor Elm in New Bark Town with the MYSTERY EGG.
- **Route:** Head south from Route 30, through Cherrygrove City, and west through Route 29 to reach New Bark Town.

## Current Quest
- Bring the MYSTERY EGG to Professor Elm.

## Long-term Goal
- Become the Pokémon League Champion.

## Key Items
- **POKéGEAR:** Received from Mom. Has a Phone feature.
- **POKéDEX:** Received from Professor Oak. Automatically records data on Pokémon.
- **MYSTERY EGG:** Received from Mr. Pokémon. Needs to be taken to Professor Elm.

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
- **Professor Elm** (New Bark Town): Gave me Hestia and his phone number. Wants to see the MYSTERY EGG.
- **Mom** (New Bark Town): Gave me the POKéGEAR.
- **MR. POKEMON** (Route 30): Gave me the MYSTERY EGG.
- **Professor Oak** (met at Mr. Pokémon's House): Gave me the POKéDEX.

## Radio Broadcasts
- **Professor Oak's Pokémon Talk:** Abra may be seen around Route 35.

## Puzzle Solutions
- **Cherrygrove House Lock:** Became stuck at (3, 1). Solution was to turn to face the TV at (2, 1) and interact with it ('A' button). This triggered a text box, and after closing it, movement was restored.

## Self-Corrections & Failed Hypotheses
- The path to Cherrygrove City is through Route 29. My initial assumption that it was a dead end was incorrect.

## Agent & Exploration Plan
- Design a new `situational_awareness_agent` that combines exit analysis with general exploration data to replace the `route_analyzer_agent`.
- Explore the unvisited houses in Cherrygrove City: the one at (17, 7) and the Guide Gent's house at (25, 9).