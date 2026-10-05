import re

with open("scripts/deck_slides_p1.py", "r", encoding="utf-8") as f:
    p1 = f.read()

with open("scripts/deck_slides_p2.py", "r", encoding="utf-8") as f:
    p2 = f.read()

print("P1 slide indices:", re.findall(r'data-index="(\d+)"', p1))
print("P2 slide indices:", re.findall(r'data-index="(\d+)"', p2))

# Also print titles
titles1 = re.findall(r'<h[12] class="slide-title display">(.*?)</h[12]>', p1)
titles2 = re.findall(r'<h[12] class="slide-title display">(.*?)</h[12]>', p2)
print("\nP1 Titles:")
for i, t in enumerate(titles1, 1):
    print(f"  Slide {i:02d}: {t}")

print("\nP2 Titles:")
for i, t in enumerate(titles2, len(titles1) + 1):
    print(f"  Slide {i:02d}: {t}")
