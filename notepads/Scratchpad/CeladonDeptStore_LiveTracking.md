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
- Expected Purchases:
  - 1x Fresh Water (¥200)
  - 1x Soda Pop (¥300)
  - 1x Lemonade (¥350)
  - Total expected cost: ¥850
- Expected Ending Wallet: ¥45543
- Actual Ending Wallet: [To be verified]

## Floor-by-Floor Live Layout Mapping

### 1F: Service Counter (Map 0_122)
- Stairs (UP): Verified at (12, 1) (leads to 2F)
- Elevator: Suspected at (1, 1) or nearby
- Receptionist: (8, 3) over counter (8, 4)
- Directory Board: (11, 4)

### 5F: Drug Store (Map 0_136)
- **Elevator (DOWN)**: (1, 1) (leads to Elevator Cabin Map 0_127)
- **Left Cashier (5, 3) (Behind counter at (5, 4))**: [To be spoken to]
- **Right Cashier (6, 3) (Behind counter at (6, 4))**: Sells Vitamins.
  - Inventory (Turn 29815 - Fully Verified):
    - HP UP: ¥9800
    - PROTEIN: ¥9800
    - IRON: ¥9800
    - CARBOS: ¥9800
    - CALCIUM: ¥9800

### 2F: Trainer's Market (Map 0_123)
- **Stairs (DOWN)**: (12, 1) (leads to 1F)
- **Stairs (UP)**: (16, 1) (leads to 3F)
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