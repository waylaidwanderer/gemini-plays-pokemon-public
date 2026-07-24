# UI and Border Rendering Mechanics

## Numeric Display Frame Border Quirk (Gen 1)
- **Description:** In numeric displays rendered near the right edge of the screen (such as the Poké Mart shop MONEY window), the vertical border of the frame is drawn using a tile that visually resembles a small, bold digit "1".
- **Visual Appearance:** On the far right of the MONEY window, column 19 on row 0 or row 1 contains this border tile. It renders directly to the right of the actual numbers, which can easily be misread as an extra digit "1" at the end of the money amount.
- **Rule/Verification:** Always ignore the rightmost vertical line in the MONEY display box when reading quantities. For example, if the screen displays "401" followed by the border "1", the actual amount of money is **¥401**, NOT ¥4011.
- **History:** This visual misreading occurred on Turn 1034 (reading ¥170 as ¥1701, or ¥1701 as ¥17011) and was repeated on Turn 1222 (reading ¥401 as ¥4011). Creating this permanent documentation prevents future hallucinations of this border pattern.