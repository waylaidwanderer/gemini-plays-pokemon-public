# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.

## Quest: Deliver Kenya (Route 31)
- **Status:** Damage Control / Verification.
- **Current State:** Checking Kenya in Party Menu.
- **Action:** Inspecting Mail status.
- **Next Steps:**
    1. If Mail exists: Read it. Verify "Dark Cave leads to another road."
    2. If Mail is wrong/missing: Remove/Add and Type MANUALLY.
    3. Deliver to Fisher.

## Knowledge Base
- **Fisher (Route 31):** Rejected "DARK CAVE leads to another road." (All Caps), "DARK CAVE", and "Dark Cave leads to another road" (No Period).
- **Wade (Route 31):** Called (Turn 9576). Waiting on Route 31.
- **Dark Cave:** Connects Route 31, 45, 46. Needs Flash.

## Mechanics Log
- **Mail:** Prevents deposit. PC Full -> Mail goes to Bag. Must hold nothing to attach.
- **Inputs:** Pressing Start in Mail menu triggers Printer Error. Use B.
- **Lesson:** Pressing 'Start' in the Mail menu causes a "Printer Error" loop or crash behavior. Use 'B' to exit or 'END' to finish.
- **Menu Nav:** Cursor positions are remembered. Always verify position before confirming.
- **CRITICAL FAILURE (Turn 9804):** `write_mail_safe` tool desynchronized, exited mail menu, navigated to SAVE, and overwrote the save file.
- **Recovery:** Checking Kenya's status. Will revert to manual `slow_press` for all future typing.
- **Current Location:** (15, 7) Route 31.
- **Recovery Action:** Closing Start Menu (B) to reset state.
- **Next Step:** Open Party Menu manually to check Kenya's mail status.
- **Rule Update:** ALL future mail typing will be done via manual `slow_press` commands. No automation.