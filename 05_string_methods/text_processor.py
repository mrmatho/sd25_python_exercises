"""
Text Message Processor - String Methods Exercise
"""


def normalize_text(text: str) -> str:
    """
    Normalize text by removing whitespace (spaces, etc) and converting to lowercase.
    
    Args:
        text: The text to normalize
    
    Returns:
        The normalized text (trimmed and lowercase)
    """
    # TODO: Strip whitespace and convert to lowercase
    pass


def count_words(text: str) -> int:
    """
    Count the number of words in the text.
    
    Args:
        text: The text to count words in
    
    Returns:
        The number of words
    """
    # TODO: Split the text and count the words
    pass


def is_shouting(text: str) -> bool:
    """
    Check if the text is shouting (all uppercase).
    
    Args:
        text: The text to check
    
    Returns:
        True if the text is all uppercase (ignoring non-letters), False otherwise
    """
    # TODO: Check if the text is all uppercase
    # Hint: Filter out non-letters first
    pass


def censor_word(text: str, word: str) -> str:
    """
    Replace all occurrences of a word with asterisks (case-insensitive).
    
    Args:
        text: The text to censor
        word: The word to replace
    
    Returns:
        The censored text
    """
    # TODO: Replace all occurrences of the word (case-insensitive)
    # Hint: You may need to work with a lowercase version for comparison
    pass


def create_acronym(phrase: str) -> str:
    """
    Create an acronym from the first letter of each word.
    
    Args:
        phrase: The phrase to create an acronym from
    
    Returns:
        The acronym in uppercase
    """
    # TODO: Split the phrase, take first letter of each word, join and uppercase
    pass


def reverse_words(text: str) -> str:
    """
    Reverse the order of words in the text.
    
    Args:
        text: The text to reverse
    
    Returns:
        The text with words in reverse order
    """
    # TODO: Split the text, reverse the list, and join back together
    pass


def is_valid_email(email: str) -> bool:
    """
    Check if the email is valid (simple validation).
    
    Args:
        email: The email to validate
    
    Returns:
        True if valid, False otherwise
    """
    # TODO: Check for exactly one @, characters before/after @, and at least one . after @
    pass


def extract_numbers(text: str) -> list[int]:
    """
    Extract all numbers from the text.
    
    Args:
        text: The text to extract numbers from
    
    Returns:
        A list of integers found in the text
    """
    # TODO: Split the text, check each word if it's a number, convert and collect
    pass
