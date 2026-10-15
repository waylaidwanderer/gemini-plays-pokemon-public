# Main Notepad

## Game: Pokémon Emerald Version
- Protagonist: Female (May), Name: JADE
- Starter: Treecko / Grovyle (Level 16, Male), Nickname: SAGE
- Status: DEFEATED GYM LEADER ROXANNE! Earned the Stone Badge and TM39! Sage Lv 16 (HP 46/46), Lilz Lv 9 (HP 28/28), wallet ¥5708. Fully healed at Rustboro Center!

## Party
1. SAGE (Grovyle ♂, Level 16) [Held Item: Quick Claw] - Moves: Fury Cutter, Leer, Absorb, Quick Attack. HP: 46/46. Nature: Lonely. Ability: Overgrow.
2. LILZ (Lotad ♀, Level 9) - Caught on Route 102. Moves: Astonish, Growl, Absorb. HP: 28/28.

## Bag Highlights
- Stone Badge: Received from Roxanne! Enables HM01 Cut outside battle and boosts Attack.
- Quick Claw: Held by Sage!
- Potion x5 (1 promo Potion used to heal Sage to full HP, 4 bought in Rustboro)
- Great Ball x1 (gift from rescued Devon researcher)
- Premier Ball x1 (bonus for purchasing 10 Poké Balls)
- Ether x1 (collected from northwest grass in Petalburg Woods at 4, 8)
- Paralyze Heal x1 (collected from southwest grass in Petalburg Woods at 4, 26)
- Poké Ball x14 (gift from Brendan, 3 used on Lotad, 12 bought in Rustboro)
- Berries: Cheri Berry x2 (harvested from Route 104 North tree at 3, 25), Oran Berry x7 (2 from Route 102, 2 from Route 104 South, 2 from Route 104 North at 3, 23, 1 from flower shop Sister 3), Pecha Berry x2 (harvested from Route 102 trees at 24..25, 1..2)
- TMs & HMs: TM09 Bullet Seed (gift from boy outside Petalburg Woods), TM39 Rock Tomb (gift from Roxanne), HM01 Cut (gift from Cutter in Rustboro City)
- Money: ¥5708 (won ¥300 from Brendan, ¥80 from Calvin, ¥64 from Rick, ¥48 from Allen, ¥64 from Tiana, ¥1400 from Cindy, ¥48 from Lyle, ¥180 from Aqua Grunt, ¥96 from James, ¥1400 from Winston, ¥96 from Haley, ¥144 from Gina & Mia, ¥280 from Ivan, ¥160 from Josh, ¥448 from Tommy & Marc, ¥1500 from Roxanne, spent ¥2400 on 12 Poké Balls, ¥1200 on 4 Potions)
- Key Items: Pokédex, Running Shoes (Hold B to run outdoors), Wailmer Pail (gift from Pretty Petal Flower Shop sister at 6, 3)

## Littleroot Town & Route 101 Summary
- Player's House (East): 1F, 2F (Clock set 10:00 AM, Potion in PC).
- Rival's House (West): 1F, 2F (Met Brendan).
- Birch's Lab (South-West): Received Treecko (SAGE), Pokédex, and 5 Poké Balls.
- Route 101: Connects Littleroot Town to Oldale Town. South ledge at row 13 (x=7..11) is bypassed on west side via col 6 past signpost at (5, 9). Northbound path continues around central ledge.

## Oldale Town Layout
- Pokémon Center: West side of town (red roof, door at 6, 16). Checkpoint set!
- Poké Mart: East side of town (blue roof).
- Route 103: North exit of town (where Brendan was defeated).
- Route 102: West exit of town (footprint NPC now unblocked!).

## Progression History - Phase 1, 2 & 3 (Completed)
- Phase 1: Intro, clock set, PC Potion, rival meeting, Birch rescue, and Treecko (SAGE).
- Phase 2: Oldale Center visit, promo Potion from clerk, Brendan Rival Battle 1 won on Route 103 (Sage Lv 7), Pokédex + 5 Poké Balls from Birch/Brendan, Running Shoes received from Mom.
- Phase 3: Route 102 cleared (Calvin, Rick, Allen, Tiana defeated; caught Lotad LILZ), Petalburg City Gym visit with Dad, assisted Wally catching Ralts, Route 104 traversed (Cindy, Winston, Haley, Gina & Mia, Ivan defeated; Wailmer Pail and Bullet Seed obtained), Petalburg Woods cleared (rescued Devon researcher, defeated Aqua Grunt, Lyle, James), Rustboro City explored (Cut HM01 and Quick Claw obtained), Rustboro Gym cleared (Josh, Tommy & Marc, and Gym Leader Roxanne defeated; Stone Badge and TM39 Rock Tomb earned; Sage evolved to Grovyle Lv 16).

## Progression Checklist - Phase 4 (Active)
1. [x] Defeat Gym Leader Roxanne and earn Stone Badge & TM39 Rock Tomb.
2. [x] Sage evolved into Grovyle and learned Fury Cutter!
3. [x] Witness Devon Goods robbery outside Gym and speak with Devon Researcher.
4. [x] Heal party at Rustboro Pokémon Center (Sage HP 43/43, Lilz HP 28/28).
5. [x] Travel east through Rustboro City onto Route 116 toward Rusturf Tunnel.
6. [ ] Enter Rusturf Tunnel, defeat Team Aqua Grunt, and recover Devon Goods & rescue Peeko.
7. [ ] Return to Rustboro City; deliver Devon Goods to Devon Researcher; meet Mr. Stone at Devon Corp.
8. [ ] Receive PokéNav and Letter for Steven from Mr. Stone.
9. [ ] Return south through Route 104 to Mr. Briney's cottage to sail to Dewford Town.

## Route 102
- Overview: See Locations/Route102.md for detailed map topography, trainer locations, and verified landmarks.
- Status: Fully cleared! All 4 trainers defeated, berries harvested, and connected west to Petalburg City.

## Engine / Harness Mechanics Verified
- Map transitions/warps automatically abort pending movement sequences.
- Button sequences must place `sleep` strictly between button taps (no leading/trailing sleeps).
- In PC menu, Home PC directly opens player's item storage.
- Birch bag starter order: Left = Treecko, Middle = Torchic (default), Right = Mudkip.
- Poké Mart interior: Customer counter is at (1, 4), talk to shopkeeper from (1, 5) facing Up.
- Oldale Town Mart does not stock Poké Balls prior to receiving the Pokédex.
- Outdoor Mart clerk (with free promotional Potion sample) stands in the south-central area of Oldale Town near (14, 14).
- In Gen 3, all Grass-type moves (such as Absorb) are Special, so their damage is unaffected by physical Attack drops (Growl).
- Medicine use outside battle: Start -> BAG -> select item -> USE -> select Pokémon.
- Text speed set to FAST in game Options menu (verified turn 417).
- Berry harvesting: When inspecting ripe berry trees, the prompt "Do you want to pick the [BERRY]?" defaults cursor to YES. Pressing A confirms picking; pressing B cancels and leaves them unpicked. Interacting with empty soft loamy soil prompts to plant berries from the Bag.
- Mart purchasing bonus: Buying 10 or more Poké Balls at once awards 1 bonus Premier Ball.