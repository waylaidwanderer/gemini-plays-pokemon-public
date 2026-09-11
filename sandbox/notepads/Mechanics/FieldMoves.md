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
  - Designated User: Farfetch'd (DUX) - Slot 4 in current party.
  - Usage: Cuts down small bushy trees in the overworld (e.g., Vermilion Gym entrance, Route 2 passages, Cerulean City southern barrier at (19, 28)). Cut trees respawn upon reloading the map or entering/exiting buildings.
- **HM05 FLASH:**
  - Badge Requirement: Boulderbadge (Brock) - earned Turn 594.
  - Obtained: From Prof. Oak's Aide in Route 2 eastern gatehouse [Turn 3846].
  - Function: Illuminates pitch-black caves (specifically Rock Tunnel).
  - Designated User: Drowzee (SANDMAN) - Slot 6 in active party.
  - Empirical Compatibility Proof (Turn 4021): Party compatibility screen confirmed Slots 1-5 (Digby, Rocky, Fungi, Dux, Sheldon) are NOT ABLE; Drowzee (SANDMAN) is ABLE. Taught HM05 Flash into Move Slot 3 (PP 20/20).
- **TM28 DIG:**
  - Designated User: Diglett (DIGBY) - Slot 1 in current party.
  - Function: In caves/dungeons, warps player back to the last visited Pokémon Center (equivalent to an Escape Rope). In battle, powerful 2-turn Ground STAB move.

## Bicycle Locomotion Physics
- **Perpendicular Turn Mechanics:** When mounted on the Bicycle, an initial directional input while facing a perpendicular direction turns the player in place to face that direction without advancing a grid step (empirically confirmed Turns 4046, 4048, 4049, 4054). Subsequent directional inputs in the same direction advance one grid step per press.

## Field Items (Poké Flute)
- **No Direct 'A' Interaction for Poké Flute:** In Generation 1 retail, pressing 'A' while facing the sleeping Snorlax only displays "A sleeping POKéMON blocks the way!" and closes without prompting to play the flute. The POKé FLUTE must be manually selected and used from the Bag menu (START -> ITEM -> POKé FLUTE -> USE) while standing adjacent to Snorlax [Verified Turn 6971].
## Bicycle Stride & Parity Mechanics
- **Bicycle Movement Speed:** On the Bicycle, player movement speed is doubled (256 px/sec vs 128 px/sec on foot).
- **Rapid Input Stride Distance:** Buffered or held directional inputs on the Bicycle can advance 2 grid tiles per input along unobstructed roads [Verified Turns 11426-11428].
- **Coordinate Alignment Parity:** When traversing at 2 tiles per stride, coordinate parity is preserved (e.g. moving from an odd column like 33 or 13 keeps alignment strictly to odd columns: 13, 11, 9).
- **Parity Shifting via Obstacles:** Riding into a collision boundary (such as the col 5 stone fence from col 7) truncates the 2-tile stride into a single-tile step, shifting alignment parity from odd to even columns (e.g. landing on col 6, which enables reaching col 8 and col 10) [Verified Turn 11428].

## HM03 SURF Verification
- **Badge Requirement:** Soulbadge (Koga) - mandatory.
- **Empirical Proof (Turn 12037):** Facing the pond at (31, 22) in Fuchsia City, selecting SURF on Blastoise (SHELDON) displayed: "No! A new BADGE is required."
- **Strategic Implication:** Surf is strictly unusable before defeating Gym Leader Koga. The path to Fuchsia Gym and Pokémon Center cannot require Surf.