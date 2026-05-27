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
- [ ] Defeat Vermilion Gym Leader Lt. Surge and earn the Thunder Badge

## Backtrack-Healing Strategy (Vermilion Gym):
- **Strategy**: Clear all Gym trainers first (Dwayne at (1, 10), Tucker at (3, 8), and the third trainer). Once all trainers are defeated, instead of solving the trash can puzzle with damaged/PP-depleted Pokémon, we will walk out of the Gym and heal at the Vermilion Pokémon Center.
- **Why**: This provides a free, full heal for GEMMY and SPARKY. We can then return to Vermilion Gym to solve the trash can puzzle with 100% full health and movesets, preventing lock-reset or battle failures and ensuring maximum safety before the Lt. Surge boss fight!
- **Verification Rule**: Never leave the Pokémon Center until the party's HP and PP values in the Game State are explicitly checked and verified at 100%.
- **Status**: All three Gym trainers are 100% defeated, and our team is fully healed at the Pokémon Center (Turn 18576)! We are now ready to tackle the trash can puzzle.

## Directory
- `Locations/PalletTown` - Permanently verified Pallet Town location records.
- `Locations/Route1` - Permanently verified Route 1 connections and layout features.
- `Locations/ViridianCity` - Permanently verified Viridian City connections and buildings.
- `Locations/PewterCity` - Permanently verified Pewter City location, gym, and connection records.
- `Locations/Route3` - Permanently verified Route 3 connections, pathing, and bidirectional ledge gaps.
- `Mechanics/General` - Verified game mechanics and controls.
- `Locations/SSAnne` - Verified S.S. Anne records, cabins, and trainers.
- `Scratchpad/SSAnne_Sweep` - Active S.S. Anne exploration, battle logs, and progress.
- `Scratchpad/Surge_SSAnne_Strategy` - Active strategy for S.S. Anne and Lt. Surge's Gym.