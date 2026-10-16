# Main Notepad

## Game: Pokémon Emerald Version
- Protagonist: Female (May), Name: JADE
- Starter: Treecko / Grovyle (Level 24, Male), Nickname: SAGE
- Status: Knuckle Badge and TM08 Bulk Up earned from Gym Leader Brawly! Sage is Lv 24 (HP 33/65). All 6 gym trainers and Leader Brawly defeated. Next: exit gym to Dewford Town, heal at Pokémon Center, and head north to Route 106 / Granite Cave with HM05 Flash enabled to find Steven and deliver the Letter.

## Party
1. SAGE (Grovyle ♂, Level 24) [Held Item: None] - Moves: Fury Cutter, Pursuit, Absorb, Quick Attack. HP: 65/65. Status: OK. Stats: Atk 40, Def 30, Sp.Atk 47, Sp.Def 43, Speed 55. Nature: Lonely. Ability: Overgrow.
2. LILZ (Lotad ♀, Level 9) - Caught on Route 102. Moves: Astonish, Growl, Absorb. HP: 28/28. Status: OK.
3. CIPHER (Abra ♂, Level 10) - Caught in Granite Cave B2F with Great Ball! Moves: Teleport. HP: 25/25. Status: OK.

## Bag Highlights
- Badges: Stone Badge (Roxanne), Knuckle Badge (Brawly - enables HM05 Flash outside battle, obedience up to Lv 30).
- Quick Claw: In Bag (swapped from Sage on turn 2735)
- Super Potion x0
- Potion x0
- Great Ball x1 (1 gift from rescued researcher in Petalburg Woods, 1 used on Abra)
- Premier Ball x1 (bonus for purchasing 10 Poké Balls)
- Ether x0 (sold for ¥600 at Rustboro Mart)
- Poké Ball x12 (verified in Bag on turn 2728)
- Berries: Cheri Berry x2, Oran Berry x3, Pecha Berry x2
- TMs & HMs: TM08 Bulk Up (gift from Brawly), TM09 Bullet Seed (boy on Route 104), TM39 Rock Tomb (Roxanne), HM01 Cut (Cutter), HM05 Flash (Granite Cave Hiker)
- Money: ¥1921 (earned ¥1900 from Brawly)
- Key Items: Pokédex, Running Shoes (Hold B to run outdoors), Wailmer Pail (Pretty Petal Flower Shop sister at 6, 3), Letter (for Steven in Dewford Town), PokéNav (with Match Call - Brawly registered!), Old Rod (Fisherman in Dewford Town)

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
6. [x] Enter Rusturf Tunnel, defeat Team Aqua Grunt, and recover Devon Goods & rescue Peeko.
7. [x] Return to Rustboro City; deliver Devon Goods to Devon Researcher; meet Mr. Stone at Devon Corp.
8. [x] Receive PokéNav and Letter for Steven from Mr. Stone.
9. [x] Return south through Route 104 to Mr. Briney's cottage to sail to Dewford Town.
10. [x] Speak to Fisherman in Dewford Town to receive the Old Rod.
11. [ ] Explore Granite Cave (Route 106), received HM05 Flash; deliver Letter to Steven.
12. [x] Defeat Gym Leader Brawly in Dewford Gym to earn the Knuckle Badge and TM08 Bulk Up.

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
- Match Call (PokéNav): Devon Researcher installs Match Call upon exiting Devon Corp. Contacts registered: #1 Mr. Stone, #2 Brendan (Rustboro south exit), #3 Dad / Norman (received incoming call during boat voyage to Dewford). When navigating PokéNav or phone calls, pressing B advances dialogue and safely cancels out of menus without triggering repeat calls.
- Field Move Mechanics: Teleport cannot be used inside dungeons or caves ('Can't use that here.'). Escape Ropes or walking must be used to exit.
- Battle Move Layout (Sage): Slot 1 (top-left) = Fury Cutter, Slot 2 (top-right) = Pursuit, Slot 3 (bottom-left) = Absorb, Slot 4 (bottom-right) = Quick Attack.
- Battle Move Memory: In Pokémon Emerald, opening the FIGHT menu automatically remembers and defaults cursor to the move used on the previous turn.