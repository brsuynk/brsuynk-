import pytest
from text_stats import (
    word_count,
    char_count,
    sentence_count,
    most_common_words,
    average_word_length,
    reading_time_seconds,
)

SAMPLE = "Hello, world! This is a test. Testing, one, two, three."


def test_word_count():
    assert word_count("hello world foo") == 3


def test_char_count_with_spaces():
    assert char_count("hi there") == 8


def test_char_count_without_spaces():
    assert char_count("hi there", include_spaces=False) == 7


def test_sentence_count():
    assert sentence_count(SAMPLE) == 3


def test_most_common_words():
    text = "the cat sat on the mat the cat"
    words = dict(most_common_words(text, n=2))
    assert words == {"the": 3, "cat": 2}


def test_average_word_length_strips_punctuation():
    # Without punctuation stripping "Hello," would contribute 6 chars (with comma).
    # With stripping it should contribute 5 chars.
    result = average_word_length("Hello, world!")
    # "Hello" = 5, "world" = 5 → average = 5.0
    assert result == pytest.approx(5.0)


def test_average_word_length_empty():
    assert average_word_length("") == 0.0


def test_reading_time_seconds():
    text = " ".join(["word"] * 200)
    assert reading_time_seconds(text) == pytest.approx(60.0)
