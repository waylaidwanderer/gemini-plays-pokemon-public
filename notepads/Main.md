# Pokémon Blue Playthrough Dashboard

## Directory
- `Locations/PalletTown` - Permanently verified Pallet Town location records.
- `Locations/Route1` - Permanently verified Route 1 connections and layout features.
- `Locations/ViridianCity` - Permanently verified Viridian City connections and buildings.
- `Locations/PewterCity` - Permanently verified Pewter City location, gym, and connection records.
- `Locations/Route3` - Permanently verified Route 3 connections, pathing, and bidirectional ledge gaps.
- `Mechanics/General` - Verified game mechanics and controls.
- `Locations/SSAnne` - Verified S.S. Anne records, cabins, and trainers.

## Notepad Management Protocol (One-In, One-Out)
- To adhere to the 10 loaded notepad limit:
  1. Before loading a new region's notepad, audit current active notepads.
  2. If the loaded count is 9 or 10, identify completed/distant regions (e.g., SSAnne, VermilionCity) to unload.
  3. Execute `unload_notepads` to archive completed notepads before loading new ones.

## Active Progression Plan
- **Koga Defeated!** Obtained the Soul Badge. Overworld SURF is unlocked!
- **Erika Defeated!** Obtained the Rainbow Badge on Turn 74198. Overworld STRENGTH is unlocked!
- **Cinnabar Island Journey (Starts Turn 74291)**:
  - From Fuchsia City (West side), navigate South to Route 19.
  - Interact with the water and use GEMMY's (L59 BLASTOISE) SURF move to swim South.
  - Navigate Route 19 and Route 20 (Westward) to reach Seafoam Islands.
  - Navigate through Seafoam Islands' puzzle chambers and exit West to Cinnabar Island.
  - Defeat Gym Leader Blaine at Cinnabar Gym to secure the Volcano Badge.