# Suicune Quest (Crystal)
- Milestone 1: Burned Tower (Seen).
- Milestone 2: Cianwood City (Seen). Defeated Eusine.
- Milestone 3: Route 42 (In Progress). Current attempt started turn 17600.
- Milestone 4: Route 36 (Next). Requirement: Complete Route 42 sighting.
- Milestone 5: Tin Tower (Final). Requirement: Clear Bell (OBTAINED) + all overworld sightings.

## Suicune Hunt Strategy
- Route 42: Approach the three fruit trees in the island center.
- Route 36: Enter from the Violet City side (East) after Route 42 is completed.
- Pokedex 'Area' confirms the next overworld sighting location.

## Suicune Trigger Hypothesis Testing (Route 42)
- Hypothesis 1: Standing at (28, 17) facing Up triggers the scene.
- Test: Move to (28, 17), face Up. [Turn 17613]
- Conclusion: Denied (No scene triggered).
- Hypothesis 2: Interacting with the middle fruit tree at (28, 16) triggers the scene.
- Test: Face (28, 16) and press A. [Turn 17614]
- Conclusion: Denied (Fruit tree interaction only).
- Hypothesis 3: Walking onto (27, 15) triggers the scene.
- Test: Move to (27, 15). [Turn 17615]
- Conclusion: Denied (No scene triggered).
- Hypothesis 4: Walking onto (28, 15) triggers the scene.
- Test: Move to (28, 15). [Turn 17616]
- Conclusion: Denied (No scene triggered).
- Hypothesis 5: Walking onto (29, 15) triggers the scene.
- Test: Move to (29, 15). [Turn 17617]
- Conclusion: Denied (No scene triggered).
- Hypothesis 6: Walking onto (30, 15) triggers the scene.
- Test: Move to (30, 15). [Turn 17618]
- Conclusion: Denied (No scene triggered).
- Hypothesis 7: Walking onto (30, 16) triggers the scene.
- Test: Move to (30, 16). [Turn 17623]
- Conclusion: Denied (No scene triggered).
- Hypothesis 8: Walking onto (30, 17) triggers the scene.
- Test: Move to (30, 17). [Turn 17624]
- Conclusion: Denied (No scene triggered).
- Hypothesis 9: Walking onto (29, 17) triggers the scene.
- Test: Move to (29, 17). [Turn 17625]
- Conclusion: Denied (No scene triggered).
- Hypothesis 10: Walking onto (27, 17) triggers the scene.
- Test: Move to (27, 17). [Turn 17626]
- Conclusion: Denied (No scene triggered).
- Hypothesis 11: Walking onto (26, 17) triggers the scene.
- Test: Move to (26, 17). [Turn 17627]
- Conclusion: Denied (No scene triggered).
- Hypothesis 12: Walking onto (26, 16) triggers the scene.
- Test: Move to (26, 16). [Turn 17628]
- Conclusion: Pending.

# Tile Mechanics (Global)
- FLOOR: Traversable collision type.
- WALL / FRUIT_TREE / COUNTER / HEADBUTT_TREE: Impassable collision types.
- TALL_GRASS: Traversable, triggers wild encounters.
- WATER: Impassable without Surf.
- LEDGE: One-way movement (verified South-only for standard ledges).
- WARP / DOOR / WARP_CARPET: Map transition.
- CUT_TREE: Impassable until CUT is used.
- ROCK: Impassable. Requires ROCK SMASH.
- VOID: Impassable map boundary.
- CAVE: Warp tile leading to an interior area.
- FLOOR_UP_WALL: Impassable wall tile that appears as a floor edge.

# PC Storage (Box 1)
- VORTEX (Poliwag 22), INTERCEPT (Yanma 12), ROCKY (Onix 6), EGG (CleFFA 5), XFDW (Meowth 16), FRITTATA (Togepi 5), SHUCKIE (Shuckle 15), Blarney (Sudowoodo 20).

# Key Observations
- Pokedex 'Area' tracks the current active overworld sighting location.
- Sightings are triggered by entering specific overworld zones.
- Ecruteak History: Two towers (Bell Tower/Tin Tower and Brass Tower/Burned Tower). Three Pokemon born of water, lightning, fire ran off.

# Items & Contacts
- Fire Stone: Route 36 (Alan).
- Rock Smash (Info): Route 36 (Fisher at 44, 9).
- Fisher Tully: Route 42. Gives items.
- Bug Catcher Arnie: Route 35. Reports Yanma swarms.