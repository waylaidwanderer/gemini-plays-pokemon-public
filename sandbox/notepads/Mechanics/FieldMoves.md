# Field Moves & Hidden Machines (Generation 1 Retail)

## Mechanics & Menu Navigation
- **No Direct 'A' Interaction:** In retail Pokémon Red/Blue, pressing 'A' while facing a cuttable tree, boulder, or dark cave does NOT prompt the player to use field moves. Field moves MUST be manually selected through the party Pokémon menu.
- **Menu Execution Sequence:**
  1. Press `Start` to open the Start menu.
  2. Select `POKEéMON` (2nd option from top).
  3. Navigate to the party member knowing the desired field move.
  4. Press `A` to open the Pokémon's command menu.
  5. Select the field move (e.g. `CUT`, `FLASH`, `SURF`, `STRENGTH`, `DIG`, `TELEPORT`) at the top of the menu above STATS / SWITCH.
  6. The move animation executes in the overworld, clearing or affecting the target obstacle, and the menu closes automatically.

## Registered Field Moves & Party Users
- **HM02 FLY:**
  - Badge Requirement: Thunderbadge (Lt. Surge) - earned Turn 3632.
  - Obtained: From girl in Route 16 Secret House [Turn 28787].
  - Function: Warps player instantly to any previously visited Pokémon Center town across Kanto.
  - Designated User: Farfetch'd (DUX).
  - Party Move Submenu Order: When selecting DUX from the party Pokémon menu, CUT is Option 1 and FLY is Option 2 (pressing Down once navigates from CUT to FLY) [Empirically verified Turn 37217].
  - Fly Map Navigation Controls & Mechanics:
    - When using HM02 Fly from the party Pokémon menu, the Kanto regional map appears with a list of previously visited Pokémon Centers / destinations.
    - Cycling through destinations is controlled via Up and Down directional inputs. Pressing Up advances forward cyclically through the destination list (Pallet -> Viridian -> Pewter -> Cerulean -> Lavender -> Vermilion -> Celadon -> Fuchsia -> Cinnabar -> Indigo -> Saffron -> Pallet), while pressing Down cycles backward in reverse order.
    - The destination list wraps around continuously in both directions.
    - Spatial 2D directional navigation (Left/Right) is disabled on the Fly map; selection operates strictly as a cyclic 1D list of registered sites.
    - Pressing 'A' confirms flight to the selected destination, instantly transporting the player outside that city/facility's Pokémon Center or entrance threshold. Pressing 'B' cancels Fly and returns to the overworld [Empirically verified Turns 28805-28811].
  - Outdoor Restriction: HM02 Fly cannot be cast indoors, inside buildings, or inside forest dungeons (attempting to use Fly inside Indigo Plateau lobby yields '[POKEeMON] can't FLY here.' [Empirically verified Turn 28857]; attempting to use Fly inside Viridian Forest yields '[POKEeMON] can't FLY here.' [Empirically verified Turn 32104]). The player must exit outdoors to an open-sky exterior route before using Fly.
- **HM01 CUT:**
  - Badge Requirement: Cascadebadge (Misty) - earned Turn 2077.
  - Designated User: Farfetch'd (DUX).
  - Usage: Cuts down small bushy trees in the overworld (e.g., Vermilion Gym entrance, Route 2 passages, Cerulean City southern barrier at (19, 28)). Cut trees respawn upon reloading the map or entering/exiting buildings.
- **HM05 FLASH:**
  - Badge Requirement: Boulderbadge (Brock) - earned Turn 594.
  - Obtained: From Prof. Oak's Aide in Route 2 eastern gatehouse [Turn 3846].
  - Function: Illuminates pitch-black caves (specifically Rock Tunnel).
  - Designated User: Drowzee (SANDMAN).
  - Compatibility: Psychic, Electric, and select Normal-type Pokémon can learn HM05 Flash.
- **TM28 DIG:**
  - Designated User: Diglett (DIGBY).
  - Function: In caves/dungeons, warps player back to the last visited Pokémon Center (equivalent to an Escape Rope). In battle, powerful 2-turn Ground STAB move.

## Field Items (Poké Flute)
- **No Direct 'A' Interaction for Poké Flute:** In Generation 1 retail, pressing 'A' while facing the sleeping Snorlax only displays "A sleeping POKEéMON blocks the way!" and closes without prompting to play the flute. The POKEé FLUTE must be manually selected and used from the Bag menu (START -> ITEM -> POKEé FLUTE -> USE) while standing adjacent to Snorlax [Verified Turn 6971].

## Bicycle Physics & Locomotion Mechanics
- **Bicycle Movement Speed:** On the Bicycle, player movement speed is doubled (256 px/sec vs 128 px/sec on foot; standard theoretical values, exact pixel velocity pending dedicated frame-by-frame measurement).
- **Perpendicular Turn Mechanics & Input Buffering:** When mounted on the Bicycle, a single isolated directional input while facing a perpendicular direction turns the player in place without advancing a step (empirically confirmed Turns 4046-4054). However, chaining directional inputs in a multi-button sequence buffers continuous locomotion, overriding turn-in-place mechanics and immediately advancing full strides into the perpendicular direction (empirically confirmed Turn 13078: ['Right' x4, 'Up'] advanced 2 tiles north across the perpendicular input to (37, 29)).
- **Discrete Inputs vs Buffered Strides:** Depending on input timing and buffering, bicycle locomotion may advance 1 or 2 grid tiles per directional input. Chained inputs frequently buffer continuous 2-tile strides.
- **Precision Alignment & Navigation:** When navigating tight single-tile gaps or aligning with precision between obstacles, dismounting the Bicycle to foot locomotion guarantees strict 1-tile step precision.
- **Collision Truncation:** Riding into a collision boundary truncates movement immediately at the obstacle boundary.
- **Bicycle State Preservation Across Map Warps:** In Generation 1 retail, mounting the Bicycle outdoors sets an internal riding state. Entering an indoor area, gatehouse, or cave where cycling is prohibited forces the on-foot walking sprite, but the mounted bicycle status is preserved in memory. Upon exiting back outdoors to an area where cycling is permitted, the player automatically resumes riding the Bicycle without needing to re-select it from the Bag. Using the Bicycle from the Bag immediately upon exiting will dismount it ('BLUE got off the BICYCLE.') rather than mount it. [Empirically confirmed Turns 25420-25432 on Route 4 exit]

## HM03 SURF Mechanics & Empirical Findings
- **Badge Requirement:** Soulbadge (Koga) - mandatory.
- **Direct Surf from Bicycle:** In retail Pokémon Blue, the player can initiate the field move SURF directly from the party menu while mounted on the Bicycle. The game does not prompt or require manual dismounting beforehand; executing SURF transitions the player directly into the Surfing state. [Empirically confirmed Turns 13644-13645]
- **East Shoreline Launch:** Surfing can be initiated facing west into an eastern shoreline tile (empirically confirmed Turn 13645 at Pallet Town (8, 15) facing (7, 15)).
- **Overworld Surf Zero PP Consumption:** In retail Pokémon Blue, surfing in the overworld does not consume move PP (empirically confirmed Turn 34016).

## HM04 STRENGTH Mechanics (Generation 1 Retail)
- **Badge Requirement:** Rainbowbadge (Erika) - earned Turn 6800.
- **Designated User:** Geodude (ROCKY).
- **Displacement Physics:** In retail Gen 1, walking into a boulder with active Strength shifts the boulder 1 tile away into the target empty space while the player remains stationary on their current tile [Empirically confirmed Turns 29700-29706]. To push the boulder a second time in the same direction, the player must take an independent walking step forward into the vacated tile before pushing into the boulder again.
- **Pit Hole Interaction:** Pushing a boulder into an unfilled pit hole causes the boulder to fall through the hole to the floor below, filling the obstacle on the lower level and permanently clearing it from the current floor.
- **Strength Status Reset on Map Transitions:** In retail Generation 1 Pokémon, changing maps/floors via ladders, stairs, or doorways immediately resets the active status of HM04 Strength [Empirically verified Turns 20452, 20525, 20559, 30447].
