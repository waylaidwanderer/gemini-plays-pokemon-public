# Viridian City Location Records
- Permanently verified map connections, buildings, and POIs in Viridian City.

## Connections:
- South exit connects to Route 1 (Map 0_12) at Viridian City Column X=20 and X=21 (Row Y=35).
- North exit leads towards Route 2 / Viridian Forest.
- West exit leads to Route 22.

## Key Buildings & POIs:
- Pokémon Center: Located on Columns X=22 to X=24, with its entrance door at (23, 25).
- Trainer School: Located on Columns X=20 to X=23, rows Y=14 to Y=15, with its entrance door at (21, 15). Inside (Map 0_43), there is a student at (3, 5) and teacher at (4, 1).
- Poké Mart: Located on Columns X=29 to X=32, rows Y=17 to Y=19, with its entrance door at (29, 19) and "MART" sign at (30, 19).
  - Inside (Map 0_42), the clerk at (1, 4) hands over OAK's PARCEL (delivered on Turn 461) and subsequently sells standard items.
  - Verified Shop Inventory (Turn 832):
    1. POKE BALL (¥200)
    2. ANTIDOTE (¥100)
    3. PARLYZ HEAL (¥200)
    4. BURN HEAL (¥250)
    5. CANCEL
  - Note: Potions are NOT sold at the Viridian City Poké Mart.
- Turn 1619: Successfully entered Viridian City (Map 0_1) from Route 2.
  - Current Position: (18, 0) facing Down.
  - Team: GEMMY (SQUIRTLE) Level 7, 10/24 HP. BIRBIE (PIDGEY) Level 4, 13/18 HP.
  - Goal: Walk to the Pokémon Center to heal our team.
  - Pokémon Center location: Door is at (23, 25).
  - Let's check our path to the Pokémon Center in Viridian City. We need to navigate from (18, 0) to (23, 25).
  - First, let's look at the current screen around (18, 0):
    - Rows 0, 1, 2, 3, 4:
      - Column 18: (18, 0) TYPE_3fe2, (18, 1) TYPE_3fe2, (18, 2) TYPE_3fe2, (18, 3) TYPE_3fe2, (18, 4) TYPE_3fe2.
      - Column 17: (17, 0) TYPE_3fe2, (17, 1) TYPE_3fe2, (17, 2) TYPE_3fe2, (17, 3) TYPE_3fe2, (17, 4) TYPE_3fe2.
      - Column 19: (19, 0) TYPE_3fe2, (19, 1) has some text or sprite? No, wait! (19, 1) is TYPE_2889 (looks like a signpost or corner of tree/wall). Wait, on the screen (19, 1) has a graphic (looks like a signpost).
      - Columns 20-23: TYPE_2889 (trees, impassable).
      - Columns 14-16: TYPE_2889 (trees, impassable).
    - So we can walk Down along column 17, 18, or 19.
    - Let's plan our route down to the Pokémon Center:
      - We can walk Down along column 18.
      - Let's step Down to (18, 4). This is 4 steps Down.
      - Let's execute this.