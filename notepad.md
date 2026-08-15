<h1><code>Main</code></h1>

# Pokémon Blue - Main Dashboard

## Current Status
- Player: BLUE
- Badges: 0/8
- Location: Pewter Gym (x=4, y=6)
- Current Objective: Defeat Gym trainer and Gym Leader Brock for the Boulder Badge

## Notepads Index
- `Team`: Current Pokémon party, movesets, stats, nicknames
- `Quests`: Story progression and side tasks
- `Locations/PalletTown`: Points of interest, NPC dialogues, items
- `Locations/Route1`: Route 1 layout, points of interest, wild encounters
- `Locations/ViridianCity`: Viridian City buildings, Mart catalog, Old Man
- `Locations/ViridianForest`: Forest layout, 3 Bug Catchers, items
- `Locations/PewterCity`: Pewter City points of interest, Pokémon Center, Pewter Gym


<hr>

<h1><code>Team</code></h1>

# Current Party & Team Strategy

## Active Party
1. HYDROS (Squirtle) - Lv 13
   - Stats (Verified at Lv 13): Max HP 37 (HP: ~25/37 in battle, Healthy - Grew to Lv 13 Turn 299)
   - Type: Water
   - Moves: Tackle (35/35), Tail Whip (30/30), Bubble (~26/30)
   - Role: Starter & primary Water/Ice special attacker

## Planned Nicknaming Strategy
- Every captured Pokémon will receive a thoughtful, unique nickname.

## Inventory & Resources (Verified Turn 273)
- Money: ¥783 (Prize money from Jr. Trainer pending)
- Key Items: Town Map, Pokédex
- Consumables:
  - 1x Antidote (Status cure: Poison - 1 consumed Turn 237, 1 found at (25, 11) Turn 239, 1 consumed Turn 273)
  - 1x Potion (Restores 20 HP)
  - 5x Poké Ball (Standard catch rate)


<hr>

<h1><code>Locations/PalletTown</code></h1>

# Pallet Town - Points of Interest & Notes

## Buildings
- Player's House (2F Bedroom with PC containing 1x Potion; 1F Mom)
- Rival's House (Daisy - gave Town Map)
- Professor Oak's Pokémon Research Lab (Oak, 3 Poké Balls on table, Rival)

## Key Items & Triggers
- PC in Bedroom: Item storage (Potion obtained)
- Starter Pokémon: 3 Poké Balls on research table

<hr>

<h1><code>Quests</code></h1>

# Quest Log & Story Progression

## Main Quests
- [x] Receive Starter Pokémon from Oak (Squirtle nicknamed HYDROS)
- [x] Deliver Oak's Parcel to Oak & receive Pokédex + 5 Poké Balls
- [x] Obtain Town Map from Daisy in Pallet Town
- [ ] Defeat Gym Leader Brock in Pewter City (Boulder Badge)

## Side Quests & Deliveries
- (None yet)

<hr>

<h1><code>Locations/Route1</code></h1>

# Route 1 - Points of Interest & Notes

## Connections
- South: Pallet Town (y=35)
- North: Viridian City (y=0)

## Verified NPCs & Points of Interest
- Ledge boy NPC: Located at (17, 13) [Observed Turn 57]. Explains jumping down ledges to return south quickly.

## Empirical Wild Encounters
- Rattata: Lv 2 [Turn 50], Lv 4 [Turn 81]
- Pidgey: Lv 2 [Turn 59], Lv 5 [Turn 72]
- Ledge opening at y=19: Pass-through opening located at (9, 19) allows northward passage past the central ledge. [Verified Turn 187]

<hr>

<h1><code>Locations/ViridianCity</code></h1>

# Viridian City - Points of Interest & Notes

## Connections
- South: Route 1 (y=35)
- North: Route 2 / Viridian Forest (y=0)

## Buildings & Verified Points of Interest
- Pokémon Center: Located at (23, 25) [Observed Turn 65]. Heals party for free.
- Pokémart: Located at (29, 19) [Observed Turn 66].
  - Catalog: Poké Ball (¥200), Antidote (¥100), Parlyz Heal (¥200), Burn Heal (¥250).
  - Purchased 2x Antidote for ¥200 [Turn 200].
- North path: Old Man located at (18, 5) [Observed Turn 105] unblocks Route 2 north.

<hr>

<h1><code>Locations/ViridianForest</code></h1>

# Viridian Forest - Points of Interest & Notes

## Connections
- South: Route 2 Gatehouse (y=47) [Verified Turn 123]
- North: Pewter City Gatehouse (heading north)

## Verified Trainers
- Bug Catcher #1: Located at (30, 33) facing west, triggered at (26, 33) [Turn 145, Defeated Turn 155]. Team: Weedle Lv 6 (observed moves: String Shot, Poison Sting), Caterpie Lv 6 (observed moves: String Shot). Reward: ¥60.
- Bug Catcher #2: Located at (30, 19) facing west, triggered at (26, 19) [Turn 163, Defeated Turn 229]. Team: Weedle Lv 7, Kakuna Lv 7, Weedle Lv 7. Reward: ¥70.
- Bug Catcher #3: Located at (2, 18) facing south in far-west exit corridor [Turn 261, Defeated Turn 267]. Team: Weedle Lv 9. Reward: ¥90.

## Empirical Wild Encounters
- Caterpie Lv 3 [Turn 129], Lv 4 [Turn 156]
- Metapod Lv 6 [Turn 257]

## Items & Layout
- Entrance at south-center (17, 47)
- South-west area (x=1..8, y=30..43) is an enclosed pocket/dead end with tall grass
- Central-west area (x=11..16, y=32..33) has signpost at (16, 32) and item ball visible at (12, 29) accessible from north
- Main path leads east from entrance (x=18+) and winds north along the east side
- Friendly NPC located at (27, 40) (advises carrying extra Poké Balls)
- Signpost at (24, 40)
- Main eastern highway runs north along columns 26-27
- Item ball at (25, 11): Antidote [Collected Turn 239, Verified in Bag Turn 245]
- Far-west exit corridor: Accessed via horizontal opening at row 22-24 (columns 2-8)


<hr>

<h1><code>Locations/PewterCity</code></h1>

# Pewter City - Points of Interest & Notes

## Connections
- South: Route 2 / Viridian Forest (y=35) [Entered Turn 285]
- East: Unexplored path to the east

## Buildings & Verified Points of Interest
- Pokémon Center: Located at (13, 25) [Verified Turn 286] - Free party healing & PC access
- Pokémart: Located at (23, 17) [Verified Turn 291]
- Pewter Gym: Located at (16, 17) [Verified Turn 291, Entered Turn 296]
  - Interior Entrance: (4, 13)
  - Statues at (3, 10) and (6, 10)
  - Gym Guide NPC at (7, 10)
  - Gym Leader: Brock (at north end)

## Verified Trainers & NPCs
- Citizen NPC: Located at (17, 25) outside Pokémon Center [Observed Turn 286]
- Nurse Joy: Located at (3, 1) inside Pokémon Center [Healed party Turn 287]
- Gym Guide NPC: Located at (7, 10) inside Pewter Gym [Turn 296]
- Jr. Trainer ♂: Located at (3, 6) inside Pewter Gym, triggered at (4, 6) [Turn 297, In Battle Turn 297-301]. Team: Diglett Lv 11, Sandshrew Lv 11.


<hr>