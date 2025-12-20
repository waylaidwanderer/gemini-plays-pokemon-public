# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Fisher on Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.
- **Immediate Action:** Verify Kenya's Mail Message.
  1. Exit Mart.
  2. Open Party Menu.
  3. Select Kenya -> CHECK MAIL.
  4. If message is "DARK CAVE leads to another road", go to Route 31.
  5. If incorrect, use the spare Flower Mail in bag to rewrite.

## Party Status
- **Team:** Muscle (41), Garnet (28), Hematite (15), Azurite (13), Lapis (12), Mistral (13), Kenya (10).
- **Inventory:** Contains FLOWER MAIL (1 in Bag, 1 on Kenya).

## Quests
- **Webster's Mail:** Delivering Kenya (Spearow) to Route 31. Recipient is the Fisher at (13, 16).
  - Status: Mail message likely incomplete ("DARK CAVE leads"). Verifying now.
  - Plan: If incorrect, buy new Flower Mail at Violet Mart and rewrite.
- **Jasmine:** Completed.

## Navigation Log
- **Recent:** Obtained Storm Badge (Cianwood), Mineral Badge (Olivine). Fly to Violet City successful.
- **Next:** Route 31 -> Route 44? No, Route 31 -> Route 32 -> Union Cave? No, Mahogany is East of Ecruteak (Route 42) or East of Violet (Route 31 -> 30 -> 29 -> ?).
  - Actually, Mahogany Town is East of Ecruteak (Surf across Route 42).
  - Wait, why am I delivering mail *now*? Because I am here.
  - After delivering mail, I should Fly to Ecruteak and go East to Route 42.

## Gyms & Badges
- **Obtained:** Zephyr, Hive, Plain, Fog, Storm, Mineral.
- **Next:** Glacier Badge (Mahogany Town).

## Mechanics Notes
- **Menu Cursor:** May remember position. Always verify.
- **Mail:** "Take Mail" puts it in bag. "Give Mail" allows writing message.
### Reflection (Turn 8266)
- **Execution:** No lapsed tasks.
- **Notepad:** Organized and up to date.
- **Map:** Markers are accurate.
- **Automation:** Tools are sufficient.
- **Goals:** Clear path: Enter Mart -> Buy Mail -> Write "DARK CAVE leads to another road" -> Deliver.
- **Error Analysis:** Previous `Up` input only turned the character. Now facing Up at (9, 18). Must press `Up` again to enter Mart at (9, 17).
- **Hypothesis:** Fisher rejected mail because the message "DARK CAVE leads" was incomplete. Original message was "DARK CAVE leads to another road". Restoring the full message should fix this.
## Tile Mechanics
- **FLOOR:** Traversable.
- **WALL:** Impassable.
- **MART_SHELF:** Impassable.
- **COUNTER:** Impassable. Interactable across it.
- **WARP_CARPET_DOWN:** Exit warp.
- **Mail Correction Step 2:** Failed typing "DARK CAVE leads..." (Result was "DARK CAV!O...").
- **Current Status:** Checking Kenya's mail in Party Menu to confirm garbage text.
- **Next Steps:**
  1. If text is garbage: TAKE MAIL (sends to PC).
  2. Buy new FLOWER MAIL from Mart (currently in Violet Mart).
  3. GIVE new mail to Kenya.
  4. Write "DARK CAVE leads to another road" carefully.