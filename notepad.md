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
- **Inventory:** Contains FLOWER MAIL (3 in Bag).

## Quests
- **Webster's Mail:** Delivering Kenya (Spearow) to Route 31. Recipient is the Fisher at (13, 16).
  - Status: Mail message likely incomplete ("DARK CAVE leads"). Verifying now.
  - Plan: If incorrect, buy new Flower Mail at Violet Mart and rewrite.
- **Jasmine:** Completed.

## Navigation Log
- **Recent:** Obtained Storm Badge (Cianwood), Mineral Badge (Olivine). Fly to Violet City successful.
- **Next:** Route 31 (Deliver Mail) -> Fly Ecruteak -> Route 42 -> Mahogany Town.

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
- **Mail Correction Step 3:** Typing failed or uncertain. Assuming bad/lost mail.
- **Current Plan:**
  1. Enter Violet City Mart.
  2. Buy 3x FLOWER MAIL (ensure supply).
  3. Open Party -> Kenya.
  4. If Kenya holding mail: TAKE MAIL.
  5. GIVE fresh FLOWER MAIL.
  6. Write "DARK CAVE leads to another road".
- **Mail Typing:** Starting input of "DARK CAVE".
- **Sequence:** D -> A -> R -> K -> Space -> C -> A -> V -> E.
- **Mail Typing:** Typed "DARK CAVE".
- **Next:** Space -> lower case switch -> "leads".
- **Target String:** "DARK CAVE leads to another road".
- **Mail Typing:** Typed "DARK CAVE l".
- **Next Chunk:** "eads to ".
- **Remaining:** "another road".
- **Mail Typing:** Typing "another road".
- **Verification:** Will verify text on screen before confirming with END.
- **Correction:** Accidentally gave mail to Lapis (Turn 8325/8326).
- **Current Action:** Finishing mail on Lapis (navigating to END).
- **Next Steps:**
  1. Clear "Made LAPIS hold..." text.
  2. Enter Party Menu.
  3. Select Lapis -> MAIL -> TAKE (Send to PC).
  4. Exit to Pack.
  5. Select Flower Mail -> GIVE -> Kenya.
  6. Type "DARK CAVE leads to another road".