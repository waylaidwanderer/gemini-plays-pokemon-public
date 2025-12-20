# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Buy Flower Mail for Kenya.
  - **Status:** Cherrygrove Mart does not sell it. Going to Violet City.
- **Secondary Goal:** Deliver Kenya to Route 31.
- **Tertiary Goal:** Travel to Mahogany Town (Route 42).
- **Party:** Muscle (41), Garnet (28), Hematite (15), Azurite (13), Lapis (12), Mistral (13).
- **Boxed:** Kenya (10, Box 1), Rocky (21, Box 3).

## Quests
- **Webster:** Deliver mail to Route 31. (Current Mail status: Missing. Need Flower Mail).
- **Jasmine:** Cured. Returned to Gym. (Completed).

## Tile Mechanics
- **FLOOR/WATER:** Traversable (Surf for water).
- **WALL/OBSTACLE:** Impassable.
- **DOOR/WARP:** Transitions map.

## Navigation Log
- **Recent Progress:**
  - Obtained SecretPotion in Cianwood.
  - Cured Amphy in Olivine Lighthouse.
  - Defeated Leader Jasmine (Mineral Badge).
  - Attempted Fly to Violet City, landed in Cherrygrove.

## Gyms & Badges
- **Zephyr, Hive, Plain, Fog, Storm, Mineral.**
- **Next:** Glacier Badge (Mahogany Town).

## Notes
- **Tool Note:** `slow_press` defined for sticky menus.
- **Battle Note:** Muscle's last move was Slot 4.
- **Menu Mechanics:** Observed cursor memory in the Party Menu. It remembered the last position (Mistral, Slot 5) instead of resetting to Slot 1.
- **Navigation Update:** Fly attempt to Violet City failed (landed in Cherrygrove).
- **Hypothesis:** Input timing issue.
- **Plan:** Retrying Fly with a segmented approach. Step 1: Open Fly Map. Step 2: Navigate.
- **Menu Correction:** Accidentally entered Item Use menu instead of Fly.
- **Action:** Backing out to Overworld to retry Fly sequence from scratch.
- **Input Note:** Used `press_sequence` to send 5 B inputs to ensure full menu exit.
- **Fly Map Navigation:** Confirmed cursor memory works (Start->Up->A->A->A got us back to Fly map with Mistral selected).
- **Action:** Attempting `Left` (Cherrygrove) -> `Up` (Violet) -> `A` (Confirm) to Fly.
- **Location:** Violet City Mart.
- **Action:** Buying Flower Mail from Clerk.
- **Events:** Received a phone call from Wade (Bug Catcher). He talked about his Pokemon growing fast and a wild Poliwag escaping.
- **Plan:** Buying Flower Mail first, then will visit PC to swap party and get Kenya.
- **Issue:** Flower Mail is missing from inventory list despite attempted purchase.
- **Hypothesis:** Purchase was cancelled or failed.
- **Action:** Returning to Violet City Mart to buy it again.
- **Quest Status:** Kenya is in party. Just need the mail.
- **Purchase Error Analysis:** Reviewed previous turn history. After selecting "1" Flower Mail, I likely pressed 'B' during the confirmation prompt ("That will be ¥50. OK?"), cancelling the transaction.
- **Correction Plan:** This time, I must press 'A' *twice* after selecting the item: once to confirm quantity (1), and once to confirm the purchase.
- **Buy Strategy:** Using `Up` wrapping (A -> Up -> Up -> A) to quickly select Flower Mail from the bottom of the list.
- **Verification:** Will check the "How many?" screen to ensure "FLOWER MAIL" is the selected item before confirming purchase.
- **Observation:** Fisher rejected mail.
- **Hypothesis:** Trying Cooltrainer M at (32, 9).
- **Action:** Talking to him to see if he is the recipient.
- **Interaction:** Talking to Cooltrainer M at (34, 8).
- **Hypothesis:** He might be the mail recipient since the Fisher rejected it.
- **Context:** The Fisher was sleeping, which matches Webster's description, but he rejected the mail. Checking other NPCs to be sure.
- **Analysis:** Fisher asked "You have MAIL for me?" but then said "This MAIL isn't for me."
- **Deduction:** Fisher IS the recipient. The rejection is due to the mail itself.
- **Hypothesis:** The quest requires the specific message "DARK CAVE leads to another road" (original mail content).
- **Plan:** Checking Youngster now to be 100% sure. Then will try rewriting the mail on Kenya to match the original message.
- **Action:** Talking to Youngster at (9, 5) to verify if he is the recipient.
- **Contingency:** If Youngster is not the recipient, I will assume the Fisher is the correct target but requires the specific mail message ("DARK CAVE leads to another road").
- **Plan:** If Youngster fails, I will rewrite the mail on Kenya to match the original message.
- **Status:** Fisher rejected blank Flower Mail. Confirmed he is the recipient.
- **Plan:** Fly to Violet City, buy new Flower Mail, write "DARK CAVE leads to another road", and return.
- **Reason:** Need to rewrite mail message, which requires a fresh mail item (current one is attached and can't be edited easily without swapping).
- **Navigation:** Using Fly to bypass obstacles (Ledge/Cut Tree) blocking the path back to Violet City.
- **Observation:** Screen says "Currently selected destination: New Bark Town".
- **Action:** Using `slow_press` [Left, Up, A] to Fly to Violet City.
- **Goal:** Return to Violet City to modify the Flower Mail message to "DARK CAVE leads to another road".