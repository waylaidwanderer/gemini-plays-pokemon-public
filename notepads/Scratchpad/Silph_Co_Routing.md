Silph Co Stair Connections:
- 1F UP(26,0) <-> 2F DOWN(24,1) (X shifts 26 <-> 24)
- 2F UP(24,0) -> 3F DOWN(24,1) (Same X)
- 3F UP(26,0) -> 4F DOWN(26,1) (Same X)
- 4F UP(24,0) -> 5F DOWN(14,1) (X shifts 24 -> 14)
- 5F UP(16,0) -> 6F DOWN(22,1) (X shifts 16 -> 22)
- 6F UP(16,0) -> 7F DOWN(14,1) (X shifts 16 -> 14)
- 7F UP(16,0) -> 8F DOWN(16,1) (Same X)
- 8F UP(14,0) -> 9F DOWN(8,1) (X shifts 14 -> 8)
- 9F UP(10,0) -> 10F DOWN(9,1) (X shifts 10 -> 9)
- 10F UP(14,9) -> 11F DOWN(14,1) (Found empirically)

Rule: Taking stairs UP from Floor N places you in front of the stairs DOWN on Floor N+1, and vice-versa.
I am continuing my ascent to map the stairs on every floor.