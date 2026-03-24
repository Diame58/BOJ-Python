import sys

input=sys.stdin.readline

color = int(input())

if 620 <= color <= 780:
    print("Red")
elif 590 <= color < 620:
    print("Orange")
elif 570 <= color < 590:
    print("Yellow")
elif 495 <= color < 570:
    print("Green")
elif 450 <= color < 495:
    print("Blue")
elif 425 <= color < 450:
    print("Indigo")
elif 380 <= color < 425:
    print("Violet")
