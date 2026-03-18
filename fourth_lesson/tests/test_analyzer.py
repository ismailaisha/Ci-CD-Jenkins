import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analyzer import analyze_text



def test_analyze_text():
    result = analyze_text("hello world")

    assert result["words"] == 2
    assert result["characters"] == 11
    assert result["characters_without_spaces"] == 10