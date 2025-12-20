# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.
- **Immediate Action:** Fly to Violet City.
  1. **Current State:** Reading Mail (Verified Correct: "DARK CAVE LEADS TO ANOTHER ROAD").
  2. **Sequence:**
     - `B`: Close Message.
     - `B`: Exit Mail Menu (Back to Party).
     - `Up`: Select Mistral.
     - `A`: Open Menu.
     - `Fly`: Select Fly (Scroll down if needed).
     - `Violet City`: Select Destination.
  3. **Target:** Sleeping Man (Cooltrainer M) on Route 31 (near Dark Cave).
- **Route Info:** Must approach Fisher/Sleeping Man from the West (Violet City side).
- **Mail Status:** Verified Correct (Original Message). Fisher rejected it, so he is WRONG recipient.
- **Route Info:** Must approach Fisher/Sleeping Man from the West (Violet City side).
- **Route Info:** Must approach Fisher from the West (Violet City side).
- **Mail Status:** Fixed. Kenya holding correct mail.
- **Previous Attempt:** Delivered to Fisher (Rejected: "This MAIL isn't for me").

## Party Status
- **Team:** Muscle (41), Garnet (28), Hematite (15), Azurite (13), Lapis (12), Mistral (13), Kenya (10).
- **Inventory:** Contains FLOWER MAIL (3 in Bag).

## Quests
- **Webster's Mail:** Delivering Kenya (Spearow) to Route 31. Recipient is the Fisher at (17, 7).
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
- **Action:** Fix Kenya's Mail (Kenya already holding mail).
- **Plan:**
  1. Back out to Overworld.
  2. Open Party Menu.
  3. Select Kenya -> MAIL -> TAKE (Save to PC).
  4. Open Pack -> Flower Mail -> GIVE -> Kenya.
  5. Write "DARK CAVE leads to another road".
- **Note:** Lapis also holding mail (mistake), fix later.
- **Mail Progress:** Typing "DARK CAVE ".
- **Cursor End Position:** Space (Row 2, Col 6).
- **Next Step:** Switch to lower case, type "leads to another road".
- **Mail Typing:** Toggled lower case.
- **Typed:** "leads ".
- **Next Chunk:** "to another".
- **Mail Typing:** Typed "DARK CAVE leads".
- **Next Chunk:** " to an".
- **Plan:** Space -> t -> o -> Space -> a -> n.
- **Correction:** Failed to type mail (exited to Pack by mistake).
- **Current State:** In Pack -> TM/HM Pocket -> Teach Fly?
- **Action:** Cancel "Teach Fly", navigate back to Items Pocket.
- **Next:** Find Flower Mail -> Give -> Kenya.
- **Status Update:** Kenya has a Mail (likely blank/cancelled). Lapis has a Mail. Inventory: 1 Flower Mail left.
- **Confirmed Plan:**
  1. Exit to Overworld.
  2. Party -> Kenya -> TAKE MAIL (Send to PC).
  3. Pack -> Flower Mail -> GIVE -> Kenya.
  4. Write "DARK CAVE leads to another road".
- **Mail Typing:** Typing "another road".
- **Cursor End Position:** 'd' (Row 2, Col 3).
- **Next Step:** Verify text "DARK CAVE leads to another road", then Select END.
- **Observation:** Fisher at (17, 7) rejected the mail ("This MAIL isn't for me").
- **Hypothesis:** The intended recipient is the "Sleeping Man" (Cooltrainer M) at (33, 9) near Dark Cave.
- **Plan:** Close menu, travel East to (33, 9), and deliver mail to the Cooltrainer.