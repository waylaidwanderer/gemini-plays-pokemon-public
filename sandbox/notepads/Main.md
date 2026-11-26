# Main Notepad

## Game: Pokémon Emerald Version
- Protagonist: Female (May), Name: JADE
- Starter: Sceptile (Level 85, Male), Nickname: SAGE
- Status: Attempt 13 Active! Challenging Elite Four Drake in Room 4! SAGE Lv 85 (96/254 HP, ~166 Spe). Bag: 1 Revive, 1 Full Heal, 2 conscious anchors. Final Elite Four battle before Wallace!

## Party (100% Restored Upon Whiteout)
1. SAGE (Sceptile ♂, Level 85) - Lead! HP: 96/254. Max HP: 254. Atk 190, Def 137, SpA 207, SpD 186, Spe 250. Moves: Bullet Seed (6/30), Aerial Ace (0/20), Facade (13/20), Quick Attack (30/30). Status: OK (Active Battler).
2. LILZ (Lombre ♀, Level 30) - Moves: Dive (10/10), Waterfall (15/15), Surf (15/15), Flash (20/20). HP: 0/85. Status: FAINTED.
3. CIPHER (Kadabra ♂, Level 17) - Moves: Teleport (20/20), Confusion (25/25). HP: 0/41. Status: FAINTED.
4. COBALU (Aron ♂, Level 18) - Moves: Cut (30/30), Rock Smash (15/15), Dig (10/10), Strength (15/15). HP: 0/49. Status: FAINTED.
5. MOCHI (Wynaut ♂, Level 11) - Moves: Splash (40/40), Charm (20/20), Encore (5/5). HP: 42/42. Status: OK.
6. GUAVA (Tropius ♀, Level 30) - Moves: Razor Leaf (25/25), Stomp (20/20), Sweet Scent (20/20), Fly (15/15). HP: 101/101. Status: OK.

## Bag Highlights
- Badges: Stone, Knuckle, Dynamo, Heat, Balance, Feather, Mind, Rain. ALL 8 HOENN BADGES COLLECTED!
- Quick Claw: In Bag
- Macho Brace (received from Victoria Winstrate)
- Full Heal x1 (1 consumed Turn 26456, 1 consumed Turn 26600 to cure Freeze)
- Ultra Ball x0 (sold for ¥600)
- Revive x1 (2 consumed on SAGE, 1 consumed on Lilz)
- Hyper Potion x0
- Master Ball x1 (obtained in Team Aqua Hideout Archie's Office!)
- Money: ¥16,341 (earned ¥5,300 from Glacia)
- Key Items: Magma Emblem, Pokéblock Case, Go-Goggles, Pokédex, Running Shoes, Wailmer Pail, PokéNav (Match Call), Old Rod, Good Rod, Itemfinder, Mach Bike, Soot Sack

## Progression Checklist - Phase 14: Ever Grande City & The Pokémon League (Active)
1. [x] Scale Ever Grande City waterfall using HM07 Waterfall!
2. [x] Traverse Victory Road (COMPLETED Turn 23825)!
3. [x] Enter Pokémon League HQ and register permanent flight checkpoint!
4. [ ] Challenge the Elite Four:
    - [x] Elite Four Member #1 Sidney DEFEATED (Attempt 13, Turn 26675)!
    - [x] Elite Four Member #2 Phoebe DEFEATED (Attempt 13, Turn 26712)!
    - [x] Elite Four Member #3 Glacia DEFEATED (Attempt 13, Turn 26752)!
    - [ ] Elite Four Member #4 Drake
    - [ ] Champion Wallace

## Engine / Harness Mechanics Verified
- In-Battle Party Targeting Shift Mechanic: On the in-battle party targeting screen, the reserve column lists remaining party members with the active battler in the left box.
- Overgrow Threshold & Multiplier: Sceptile's Overgrow activates when HP is <= 1/3 max HP (<= 82 HP for Sage's 246 max HP), providing an immediate 1.5x damage multiplier to all Grass-type attacks!
- OHKO Move Level Mechanic in Gen 3: One-hit knockout moves like Sheer Cold automatically fail (0% accuracy) if the user's level is lower than the target's level (e.g. Walrein Lv 53 Sheer Cold has 0% accuracy against Sage Lv 81/82!).
- In-Battle Bag Item Usage Workflow: Using medicine from battle Bag requires THREE consecutive A presses: 1. Press A on item in Bag -> 2. Press A on pop-up [USE / CANCEL] -> 3. Party targeting screen loads -> press A to confirm target Pokémon.
- Move Menu Clamping for Slot 1 (Bullet Seed): Pressing Up then Left on the 2x2 move selection screen is 100% mathematically guaranteed to clamp cursor directly to Slot 1 (top-left, Bullet Seed).
- Move Menu Clamping for Slot 2 (Aerial Ace): Pressing Up then Right on the 2x2 move selection screen is 100% mathematically guaranteed to clamp cursor directly to Slot 2 (top-right, Aerial Ace).
- Move Menu Clamping for Facade (Slot 3): Pressing Down then Left on the 2x2 move selection screen is 100% mathematically guaranteed to clamp cursor directly to Slot 3 (bottom-left, Facade).
- Move Menu Clamping Guarantee: On the 2x2 move selection screen, pressing Down then Right is mathematically guaranteed to clamp the cursor directly onto Slot 4 (Quick Attack).
- In-Battle Sacrificial Revive Protocol: When the active ace faints, sending out a reserve Pokémon allows using a Revive from the Bag with absolute turn-start priority (+6).
- Party Swap Mechanic on Forced Replacement (Turn 26732 Discovery): In Gen 3 Pokémon Emerald, when a Pokémon faints and a replacement is chosen from the party screen, the incoming replacement swaps positions with the outgoing Pokémon in the party order. Because Lilz was sent in after Sage fainted in Room 2, Lilz became Slot 1 and Sage became Slot 2. Therefore, party targeting rows dynamically follow these swaps. Always verify the target's name plate on the screen before confirming item use!
- In-Battle Party Targeting Grid Verified Layout (Turn 26732 Visual Proof): On the in-battle party medicine targeting screen, the right column does NOT strictly put Slot 1 at Row 1. In Turn 26732 Frame 56, when Cipher was in the Left Box, Row 1 was LILZ (Lv 30) and Row 2 was SAGE (Lv 85, FNT). To target SAGE when Row 1 is Lilz, you MUST press Right then DOWN to Row 2! Always inspect the name tag in the highlighted box to confirm the target is SAGE before pressing A!
- Party Screen Visual & Cancel Navigation Mechanics (Turn 26740-26746 Discovery): In Gen 3 Pokémon Emerald's party screens, panel background colors indicate health status: Blue = Conscious, Orange/Red-Brown = Fainted. The actual cursor is indicated by a thick orange bounding box around the active panel. Pressing B on the party replacement screen jumps the cursor directly to the CANCEL button at the bottom-right. From CANCEL, pressing Up steps vertically up the right column (Row 5 -> Row 4 -> Row 3 -> Row 2 -> Row 1).
- Light Screen Physical Bypass: Light Screen only mitigates Special damage; physical moves like Facade and Quick Attack deal 100% full unmitigated damage.
- Anchor Sacrifice Clean Switch-In: Letting an active low-level anchor faint from the opponent's attack provides the ace a completely free switch-in without suffering switch-in damage.

- Grudge PP Absorption Strategy: When facing an opponent with Grudge (e.g. Phoebe's Banette #1), using an expendable move with low PP (e.g. Aerial Ace) to deliver the KO blow ensures Grudge only wipes the expendable move, completely protecting vital STAB moves (like Bullet Seed) from depletion.
- Battle Bag Medicine Layout: In the Battle Bag Items pocket, Full Heal is at Row 3 (directly above Revive at Row 4). Using Full Heal cures non-volatile status (such as Freeze) instantly on turn start.
- Level 83 Overgrow Threshold: At Level 83 (max HP 249), Sceptile's Overgrow activates at <= 83 HP (249 / 3 = 83), boosting all Grass-type moves by 1.5x.
- Party Replacement Screen Cursor Default: When the active Pokémon faints, the party replacement screen cursor defaults to the fainted Pokémon in the Left Box. To select the first reserve Pokémon (Slot 2, Lilz), press Right first to move to Row 1 of the Right Column.
- In-Combat Sacrificial Revive Execution Proof: Successfully executed Sacrificial Revive on Turn 26488 against Glacia's Ace Walrein Lv 53. Sending out reserve anchor (Lilz Lv 30) allows using Revive with +6 priority to restore SAGE to 124/249 HP. The anchor absorbs the opponent's incoming attack and faints, providing SAGE a free switch-in without switch-in damage.
- Facade Physical Damage vs Light Screen Proof: Verified on Turn 26493 that physical moves like Facade (70 BP) ignore Glalie's Light Screen, dealing ~75% max HP damage (~110 HP) to Glalie Lv 50.- Stat Stage Reset on Sacrificial Revive: Verified on Turn 26527 that when a Pokémon is revived and switched in, all prior stat drops (e.g. -1 Speed from Rock Tomb) are 100% reset to zero, restoring full base Speed.
- Drake Send-Out Order in Emerald: Drake sends out Shelgon Lv 52 (#1), Flygon Lv 53 (#2), Altaria Lv 54 (#3), Ace Salamence Lv 55 (#4), and Kingdra Lv 53 (#5).
- Aerial Ace Sand-Attack Bypass: Aerial Ace ignores accuracy and evasion modifiers, guaranteeing a 100% hit rate against Sand-Attack users (such as Sidney's Mightyena).
- Pokémon League Lobby Mart Navigation: From lobby entrance (9, 11), walk Up x6, Right x7, Up x1 to reach Mart counter (16, 4). Revives are sold at Row 6 for ¥1,500 each.

- Level 84 SAGE Benchmark: Max HP 251, Atk 187, Def 137, SpA 204, SpD 183, Spe 247. Overgrow activates at <= 83 HP.
- Protect Pressure PP Depletion: Attacking into an opponent's Protect while Pressure is active consumes 2 PP.
- Phoebe Grudge Protection Protocol: Aerial Ace must have >= 1 PP when Banette #1 enters so Grudge depletes Aerial Ace rather than STAB Bullet Seed.
- Battle Menu Cursor Persistence: After opening or using an item from the Bag in battle, the main battle menu cursor remains on BAG (FIGHT ▶BAG). To select FIGHT, you MUST press Left first!
- Overgrow Activation Proof: SAGE at 26/251 HP successfully has Overgrow active (<= 83 HP threshold), boosting Grass moves by 1.5x. Dusclops Lv 51 Ice Beam only dealt 31 dmg to Lv 84 SAGE.
- Party Replacement Screen Navigation: From Left Box, press Right to enter Right Column (Row 1). Press Down x4 to reach Row 5 (bottom party slot, Guava).
- Whiteout Currency Mechanics: Cash halved upon whiteout (¥5,383 -> ¥2,691). Revives sold at Mart Counter Row 6 for ¥1,500 each. Sidney rewards ¥4,900.
- Mart Purchase Confirmation Timing: In Pokémon Emerald Marts, the purchase quantity confirmation text ("Item? And you wanted X? That will be ¥Y.") requires ~1200ms to print before the [YES / NO] prompt is active. Pressing B prematurely cancels the purchase.
- Verified Attempt 13 Inventory: Physically confirmed in Bag on Turn 26657: Revive x4, Full Heal x1, Quick Claw x1, Macho Brace x1, Money ¥1,041.
- Level 85 SAGE Benchmark: Max HP 254, Atk 190, Def 137, SpA 207, SpD 186, Spe 250. Overgrow activates at <= 84 HP (254 / 3 = 84).