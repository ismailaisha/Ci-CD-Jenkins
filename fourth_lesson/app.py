import sys
from analyzer import analyze_text

if len(sys.argv) < 2:
    print("Usage: python app.py 'your text'")
    sys.exit()

text = sys.argv[1]
result = analyze_text(text)

print("Text analysis result")
print("Words:", result["words"])
print("Characters:", result["characters"])
print("Characters without spaces:", result["characters_without_spaces"])