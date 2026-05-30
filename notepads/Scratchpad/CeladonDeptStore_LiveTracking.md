# Celadon Department Store Live Tracking

## 1F: Service Counter
- **Directory Sign (11, 4)**: Read on Turn 29712:
    - 1F: SERVICE COUNTER
    - 2F: TRAINER'S MARKET
    - 3F: TV GAME SHOP
    - 4F: WISEMAN GIFTS
    - 5F: DRUG STORE
    - ROOFTOP SQUARE: VENDING MACHINES
- **Receptionist (8, 3)**: Behind counter at row 4. Dialogue: "Hello! Welcome to CELADON DEPT. STORE. The board on the right describes the store layout." (Spoken to on Turn 29710)
- **Elevator Doors**: Located at (19, 3), (19, 4), (19, 5) on 1F? Let's verify.
- **Stairs / Escalators**: [To be found]

## Financial Tracking & Wallet Audit
- Starting Wallet: ¥46393 (Turn 29714)
- Purchases Log:
  - Turn 29885: 1x FRESH WATER (¥200). Wallet went from ¥46393 to ¥46193. Verified in bag.
  - Turn 29893: 1x SODA POP (¥300). Wallet went from ¥46193 to ¥45893. Verified in bag.
  - Turn 29921: 1x LEMONADE (¥350). Wallet went from ¥45893 to ¥45543. Verified in bag.
- Expected Ending Wallet: ¥45543
- Actual Ending Wallet: [To be verified]

## Saffron Gatehouse Passability Testing Protocol
- **Objective**: Identify which drink (Fresh Water, Soda Pop, or Lemonade) unlocks Saffron City.
- **Protocol**:
  1. Travel to Route 7 Saffron Gatehouse (Map 0_77) via Route 7 (Map 0_18).
  2. Speak to the Gatehouse Guard.
  3. Record the exact dialogue script.
  4. Observe which drink is consumed and whether access to Saffron City is unlocked.
  5. Log the outcome in 'Locations/CeladonCity' and 'Locations/Route7'.

## Floor-by-Floor Live Layout Mapping

### 1F: Service Counter (Map 0_122)
- Stairs (UP): Verified at (12, 1) (leads to 2F)
- Elevator: Verified at (1, 1)
- Receptionist: (8, 3) over counter (8, 4)
- Directory Board: (11, 4)

### 5F: Drug Store (Map 0_136)
- **Elevator (DOWN)**: (1, 1) (leads to Elevator Cabin Map 0_127)
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

### 2F: Trainer's Market (Map 0_123)
- **Stairs (DOWN)**: (12, 1) (leads to 1F)
- **Stairs (UP)**: [To be found - escalators are separate]
- **Elevator Door**: (1, 1) (leads to Elevator Cabin Map 0_127)
- **NPCs**:
  - Customer at (19, 5): Bald man. Dialogue: "SUPER REPEL keeps weak POKéMON at..." (Spoken to on Turn 29726)
  - Customer at (14, 3) (moving): Fat guy. Dialogue: [To be spoken to]
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

### Elevator Cabin (Map 0_127)
- **Map Transition**: Entered by walking into the elevator doorway on 2F (Map 0_123) at (1, 1) on Turn 29768, spawning at (1, 3) facing Down.
- **Warp Connection (Exit)**: Stepping Down from row 3 (e.g. at (1, 3) or (2, 3)) warps back to the selected floor's elevator landing on the main floor (tested on Turn 29786: warped back to 2F (Map 0_123) at (1, 1), stepping to (1, 2) facing Down).
- **Control Panel**: Located at (3, 0) (looks like a panel graphic on the top-right wall). Must stand at (3, 1) facing Up and press A to choose floors.
### 4F: Wiseman Gifts (Map 0_125)
- **Elevator Door**: (1, 1) (leads to Elevator Cabin Map 0_127)
- **Stairs**: [To be verified if UP/DOWN]
- **NPCs**:
  - NPC at (9, 5): Youngster sprite. Dialogue: [To be spoken to]
  - NPC at (14, 2): Youngster sprite. Dialogue: [To be spoken to]
- **Shop counters**: Row 3 has counters. Row 4 has green cashier tiles at (7, 4), (9, 4), (13, 4), and (15, 4).