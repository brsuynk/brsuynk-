"""Utility functions for computing statistics over text."""

from collections import Counter
import re


def word_count(text: str) -> int:
    """Return the number of words in text."""
    return len(text.split())


def char_count(text: str, include_spaces: bool = True) -> int:
    """Return the number of characters in text."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def sentence_count(text: str) -> int:
    """Return the number of sentences in text."""
    # TODO: handle abbreviations (e.g. "Dr.", "U.S.A.") to avoid false splits
    sentences = re.split(r"[.!?]+", text.strip())
    return len([s for s in sentences if s.strip()])


def most_common_words(text: str, n: int = 5) -> list[tuple[str, int]]:
    """Return the n most common words and their counts."""
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    return Counter(words).most_common(n)


def average_word_length(text: str) -> float:
    """Return the average length of words in text."""
    words = re.findall(r"\b[a-zA-Z0-9]+\b", text)
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)


def reading_time_seconds(text: str, wpm: int = 200) -> float:
    """Estimate reading time in seconds assuming a given words-per-minute rate."""
    # TODO: add support for adjusting wpm based on text complexity (Flesch score)
    return word_count(text) / wpm * 60


def flesch_reading_ease(text: str) -> float:
    """Compute the Flesch Reading Ease score for text.

    Score ranges: 90-100 very easy, 60-70 standard, 0-30 very difficult.
    Formula: 206.835 - 1.015*(words/sentences) - 84.6*(syllables/words)
    """
    # TODO: implement syllable counting per word
    raise NotImplementedError("flesch_reading_ease is not yet implemented")


def _count_syllables(word: str) -> int:
    """Count syllables in a single word using a heuristic approach."""
    # TODO: replace with a proper CMU pronunciation dictionary lookup
    word = word.lower().strip(".,!?;:")
    if not word:
        return 0
    vowels = "aeiouy"
    count = 0
    prev_was_vowel = False
    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel
    # silent 'e' at end
    if word.endswith("e") and count > 1:
        count -= 1
    return max(1, count)
