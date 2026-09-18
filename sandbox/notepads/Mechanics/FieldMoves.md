# Field Moves & Hidden Machines (Generation 1 Retail)

## Mechanics & Menu Navigation
- **No Direct 'A' Interaction:** In retail Pokémon Red/Blue, pressing 'A' while facing a cuttable tree, boulder, or dark cave does NOT prompt the player to use field moves. Field moves MUST be manually selected through the party Pokémon menu.
- **Menu Execution Sequence:**
  1. Press `Start` to open the Start menu.
  2. Select `POKéMON` (2nd option from top).
  3. Navigate to the party member knowing the desired field move.
  4. Press `A` to open the Pokémon's command menu.
  5. Select the field move (e.g. `CUT`, `FLASH`, `SURF`, `STRENGTH`, `DIG`, `TELEPORT`) at the top of the menu above STATS / SWITCH.
  6. The move animation executes in the overworld, clearing or affecting the target obstacle, and the menu closes automatically.

## Registered Field Moves & Party Users
- **HM01 CUT:**
  - Badge Requirement: Cascadebadge (Misty) - earned Turn 2077.
  - Designated User: Farfetch'd (DUX).
  - Usage: Cuts down small bushy trees in the overworld (e.g., Vermilion Gym entrance, Route 2 passages, Cerulean City southern barrier at (19, 28)). Cut trees respawn upon reloading the map or entering/exiting buildings.
- **HM05 FLASH:**
  - Badge Requirement: Boulderbadge (Brock) - earned Turn 594.
  - Obtained: From Prof. Oak's Aide in Route 2 eastern gatehouse [Turn 3846].
  - Function: Illuminates pitch-black caves (specifically Rock Tunnel).
  - Designated User: Drowzee (SANDMAN).
  - Empirical Compatibility Proof (Turn 4021): Party compatibility screen confirmed Slots 1-5 (Digby, Rocky, Fungi, Dux, Sheldon) are NOT ABLE; Drowzee (SANDMAN) is ABLE. Taught HM05 Flash into Move Slot 3 (PP 20/20).
- **TM28 DIG:**
  - Designated User: Diglett (DIGBY).
  - Function: In caves/dungeons, warps player back to the last visited Pokémon Center (equivalent to an Escape Rope). In battle, powerful 2-turn Ground STAB move.

## Bicycle Locomotion Physics
- **Perpendicular Turn Mechanics & Input Buffering:** When mounted on the Bicycle, a single isolated directional input while facing a perpendicular direction turns the player in place without advancing a step (empirically confirmed Turns 4046-4054). However, chaining directional inputs in a multi-button sequence buffers continuous locomotion, overriding turn-in-place mechanics and immediately advancing full strides into the perpendicular direction (empirically confirmed Turn 13078: ['Right' x4, 'Up'] advanced 2 tiles north across the perpendicular input to (37, 29)).

## Field Items (Poké Flute)
- **No Direct 'A' Interaction for Poké Flute:** In Generation 1 retail, pressing 'A' while facing the sleeping Snorlax only displays "A sleeping POKéMON blocks the way!" and closes without prompting to play the flute. The POKé FLUTE must be manually selected and used from the Bag menu (START -> ITEM -> POKé FLUTE -> USE) while standing adjacent to Snorlax [Verified Turn 6971].
## Bicycle Stride & Parity Mechanics
- **Bicycle Movement Speed:** On the Bicycle, player movement speed is doubled (256 px/sec vs 128 px/sec on foot).
- **Discrete Inputs vs Buffered Strides:** Depending on input timing and buffering, bicycle locomotion may advance 1 or 2 grid tiles per directional input. Chained inputs frequently buffer continuous 2-tile strides.
- **Precision Alignment & Navigation:** When navigating tight single-tile gaps or aligning with precision between obstacles, dismounting the Bicycle to foot locomotion guarantees strict 1-tile step precision.
- **Collision Truncation:** Riding into a collision boundary truncates movement immediately at the obstacle boundary.
- **Bicycle State Preservation Across Map Warps:** In Generation 1 retail, mounting the Bicycle outdoors sets an internal riding state. Entering an indoor area, gatehouse, or cave where cycling is prohibited forces the on-foot walking sprite, but the mounted bicycle status is preserved in memory. Upon exiting back outdoors to an area where cycling is permitted, the player automatically resumes riding the Bicycle without needing to re-select it from the Bag. Using the Bicycle from the Bag immediately upon exiting will dismount it ('BLUE got off the BICYCLE.') rather than mount it. [Empirically confirmed Turns 25420-25432 on Route 4 exit]

## HM03 SURF Mechanics & Empirical Findings
- **Badge Requirement:** Soulbadge (Koga) - mandatory.
- **Direct Surf from Bicycle:** In retail Pokémon Blue, the player can initiate the field move SURF directly from the party menu while mounted on the Bicycle. The game does not prompt or require manual dismounting beforehand; executing SURF transitions the player directly into the Surfing state. [Empirically confirmed Turns 13644-13645]
- **East Shoreline Launch:** Surfing can be initiated facing west into an eastern shoreline tile (empirically confirmed Turn 13645 at Pallet Town (8, 15) facing (7, 15)).

## Map Transition Mechanics
- **Strength Status Reset on Map/Floor Change:** In retail Generation 1 Pokémon, changing floors via ladders, stairs, or map transitions immediately resets the active field move status of HM04 Strength to inactive. Strength must be re-cast from the party Pokémon menu on the new floor before boulders can be pushed [Empirically verified Turns 20452, 20525, 20559].