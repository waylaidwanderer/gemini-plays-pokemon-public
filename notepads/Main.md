# Pokémon Blue Playthrough Dashboard

## Main Objectives
- [x] Choose first Pokémon (Turn 81 - Squirtle!)
- [x] Reach Viridian City Poké Mart to get Oak's Parcel (Turn 247)
- [x] Deliver Oak's Parcel to Professor Oak (Turn 461)
- [x] Get Pokédex from Professor Oak (Turn 464)
- [x] Get Town Map from Daisy in Pallet Town (Turn 507)
- [x] Return to Viridian City to buy Poké Balls (Turn 825)
- [x] Capture additional wild Pokémon (Pidgey, Rattata, etc.) to build our team
- [x] Navigate north through Route 2 and enter Viridian Forest Gatehouse (Turn 2082)
- [x] Explore Viridian Forest to find and capture Caterpie (Turn 2125)
- [x] Navigate to Pewter City (Turn 3717)
- [x] Defeat Pewter Gym Leader Brock and earn the Boulder Badge (Turn 4083)
- [x] Clear all Route 3 Trainers (Turn 4752)
- [x] Restock items at Pewter Poké Mart (Turn 4848)
- [x] Traverse Mt. Moon to reach Route 4 (Turn 11116)
- [x] Reach Cerulean City (Turn 11225)
- [x] Recover TM28 Dig (Turn 14431) and teach to GEMMY (Turn 14445)
- [x] Defeat Cerulean Gym Leader Misty and earn the Cascade Badge (Turn 14547)
- [x] Board S.S. Anne and obtain HM01 Cut from the Captain (Turn 17395)
- [x] Solve Vermilion Gym's trash can lock puzzle (Turn 19471)

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
  - **Specific Milestone**: Upon entering Rock Tunnel, we will proactively unload `Locations/CeruleanCity` and `Locations/Route9` to free up slots for the highly detailed `Scratchpad/RockTunnel_Pathfinding` and future Lavender Town / Celadon City records. This keeps our active context clean and focused on our immediate surroundings.