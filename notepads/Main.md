# Pokémon Blue Playthrough Dashboard

## Main Objectives
(Tracking is managed automatically by the game state)

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

## Post-Rescue Progression Plan (Turn 38767)
4. **Saffron City & Silph Co. Progression**: Head to Saffron City to clear Silph Co., rescue the Silph President, defeat Boss Giovanni, and challenge Sabrina at Saffron Gym!
5. **Fuchsia City Progression**: Traverse Cycling Road or Route 12 south to Fuchsia City to challenge Gym Leader Koga.