# Celadon City Location Records (Map 0_6)
- **Map Transition**: Entered Celadon City (Map 0_6) from Route 7 (Map 0_18) on Turn 29595, appearing at (49, 10).
- **Warp Connection**: Seamless connection to Route 7 is located at (49, 10) on the eastern boundary of Celadon City.
- **Physical Landmarks**:
  - The floor pattern is yellow/orange checkered pavement.
  - Trees (TYPE_2889) line the borders of the pathway at (49, 12)-(49, 14) and (49, 6)-(49, 9).
  - Walkable pavement (TYPE_3fe2) extends westward through row 10 and row 11: (48, 10), (47, 10), (46, 10), (45, 10) and (48, 11), (47, 11), (46, 11), (45, 11).
- **Celadon Pokémon Center (Map 0_133)**: Door entrance at (41, 9) on Map 0_6 warps to (3, 7) on Map 0_133, facing Up.
- **Celadon Mansion (Condominiums) 1F (Map 0_128)**: Entrance door located at (24, 9) on Map 0_6 warps player to (4, 11) on Map 0_128, facing Up. Red carpet exit warp is at (5, 11).
  - **NPCs & Objects**:
    - Wandering Manager Grandma NPC (SPRITE_4081) resides behind the counter (row 8), moving horizontally between columns 0 and 7.
    - Snorlax Doll on table/floor: Located at (0, 8) in the room.
- **Game Corner**: (28, 19) (Visited, Map 0_135). Entering this door warps the player to the massive 20x18 Game Corner interior.
- **Diner**: (33, 19) (Visited, Map 0_137). Entering this door warps the player to the 10x8 Diner interior.
- **Gate at (33, 21)**: Tested on Turn 32547. Confirmed to be solid, impassable wall/post structure (TYPE_2889). No path exists directly north through this tile; one must go around to the eastern opening at (36, 21)-(37, 21) to enter the plaza.
- **Overworld Boundaries & Plaza Walkways**:
  - The northern horizontal street (Rows 10-14) is separated from the southern plaza (containing the Game Corner and Diner) by a continuous horizontal building roof and fence barrier (TYPE_2889) extending across Rows 15-18 on Columns 24-35.
  - To bypass this barrier and access the southern plaza from the north, players must walk East along Row 14 to Columns 36-37, which forms a completely open, 2-tile wide vertical bypass corridor.
  - Rows 20 and 22 are completely open checkered pavement (TYPE_3fe2) across Columns 32-41, providing horizontal walkways within the plaza to navigate around building facades.
  - Row 21 contains gates and posts (TYPE_2889) at Columns 32, 34, 35, 38, 40, and 41, but Columns 36-37 remain open for north-south passage.

## Celadon Department Store Database (Map ID 0_122 - 0_136)
- **Main Entrance**: Located on Celadon City Map 0_6 at (10, 13) (Turn 29690).

### 1F: Service Counter (Map 0_122)
- **Stairs (UP)**: Verified at (12, 1) (leads to 2F)
- **Elevator Door**: Verified at (1, 1) (leads to Elevator Cabin Map 0_127)
- **Directory Sign (11, 4)**: 
  - 1F: SERVICE COUNTER
  - 2F: TRAINER'S MARKET
  - 3F: TV GAME SHOP
  - 4F: WISEMAN GIFTS
  - 5F: DRUG STORE
  - ROOFTOP SQUARE: VENDING MACHINES
- **NPCs & Dialogue**:
  - Receptionist (8, 3) (Behind counter at (8, 4)): "Hello! Welcome to CELADON DEPT. STORE. The board on the right describes the store layout." (Spoken to on Turn 29710)

### 2F: Trainer's Market (Map 0_123)
- **Stairs (DOWN)**: (12, 1) (leads to 1F)
- **Elevator Door**: (1, 1)
- **Left Cashier (6, 3) (Behind counter at (6, 4))**: Sells TMs.
  - Inventory (Turn 29744 - Fully Verified):
    - TM32 (Double Team): ¥1000
    - TM33 (Reflect): ¥1000
    - TM02 (Razor Wind): ¥2000
    - TM07 (Horn Drill): ¥2000
    - TM37 (Egg Bomb): ¥2000
    - TM01 (Mega Punch): ¥3000
    - TM05 (Mega Kick): ¥3000
    - TM09 (Take Down): ¥3000
    - TM17 (Submission): ¥3000
- **Right Cashier (5, 3) (Behind counter at (5, 4))**: Sells standard items.
  - Inventory (Turn 29763 - Fully Verified):
    - GREAT BALL: ¥600
    - SUPER POTION: ¥700
    - REVIVE: ¥1500
    - SUPER REPEL: ¥500
    - ANTIDOTE: ¥100
    - BURN HEAL: ¥250
    - ICE HEAL: ¥250
    - AWAKENING: ¥200
    - PARLYZ HEAL: ¥200
- **NPCs & Dialogue**:
  - Customer at (19, 5): Bald man. "SUPER REPEL keeps weak POKéMON at bay... It's more effective than standard REPEL!" (Spoken to on Turn 29726)
  - Customer at (14, 3): Fat guy. [Wandering]

### 3F: TV Game Shop (Map 0_124)
- **Elevator Door**: (1, 1)
- **Stairs**: Escalator at (12, 1) goes UP. Escalator at (16, 1) goes DOWN (leads to 2F on Turn 30045).
- **NPCs & Dialogue**:
  - Customer NPC (2, 5): "You can identify POKéMON you got in trades by their ID Numbers!" (Spoken to on Turn 30022)
  - Trade NPC (7, 2): "All right! My buddy's going to trade me his KANGASKHAN for my GRAVELER!" (Spoken to on Turn 30025)
  - Trade NPC (8, 2): "Come on GRAVELER! ... GRAVELER turned into a different POKéMON! ... It's Golem!" (Spoken to on Turn 30029)
    - **Trade Evolution Insight**: The dialogue confirms that Graveler evolved into Golem upon being traded. This proves that trade-evolutions function identical to vanilla mechanics in this ROM.
  - Youngster with green shirt (11, 6): "Captured POKéMON are registered with an ID No. and OT, the name of the Original Trainer that caught it!" (Spoken to on Turn 30039)
  - Super Nerd NPC (16, 5): "Oh, hi! I finally finished POKéMON! Not done yet? This might be useful!" (Spoken to across row 4 wood counter on Turn 30056 and 30073). Gave us TM18 (Counter).
- **Shop Counters**: Row 4 has counters. Row 7 has green cashier tiles at (17, 7) and (19, 7).
  - **Empirical Audit (Turn 30056)**: Standing at row 3 facing Down, every counter spot was tested. Verified no active cashiers stand on the green tiles and no items can be purchased on 3F.

### 4F: Wiseman Gifts (Map 0_125)
- **Elevator Door**: (1, 1)
- **Stairs**: Escalator at (12, 1) goes UP. Escalator at (16, 1) goes DOWN (leads to 3F).
- **NPCs & Dialogue**:
  - Youngster NPC (met at (18, 2) on Turn 29976): "I heard something useful. You can run from wild POKéMON by distracting them with a POKé DOLL!"
- **Shop Counters**: Row 3 has counters. Row 4 has green cashier tiles at (3, 4), (5, 4), (7, 4), (9, 4), (13, 4), (15, 4), and (17, 4).
  - **Empirical Audit (Turns 29977 - 30006)**: Standing at row 2 facing Down, every single cashier tile was tested. All tests yielded no textboxes. Conclusion: No cashiers are active on 4F.

### 5F: Drug Store (Map 0_136)
- **Elevator Door**: (1, 1)
- **Left Cashier (5, 3) (Behind counter at (5, 4))**: Sells Battle Items.
  - Inventory (Turn 29844 - Fully Verified):
    - X ACCURACY: ¥950
    - GUARD SPEC.: ¥700
    - DIRE HIT: ¥650
    - X ATTACK: ¥500
    - X DEFEND: ¥550
    - X SPEED: ¥350
    - X SPECIAL: ¥350
- **Right Cashier (6, 3) (Behind counter at (6, 4))**: Sells Vitamins.
  - Inventory (Turn 29815 - Fully Verified):
    - HP UP: ¥9800
    - PROTEIN: ¥9800
    - IRON: ¥9800
    - CARBOS: ¥9800
    - CALCIUM: ¥9800

### Rooftop Square (Map 0_137 / 0_138)
- **Vending Machines (Rooftop)**: Purchased Saffron Guard Drinks (Turn 29885 - 29921)
  - FRESH WATER: ¥200
  - SODA POP: ¥300
  - LEMONADE: ¥350
- **Expected Wallet Change**: Gained 1x of each drink. Wallet went from ¥46393 to ¥45543. (Verified in Bag on Turn 30078).

### Elevator Cabin (Map 0_127)
- **Warp Connection**: Standing at (3, 1) facing Up and pressing A on the control panel at (3, 0) opens the floor selector. Exiting Down from row 3 warps back to the chosen floor's elevator landing at (1, 1).