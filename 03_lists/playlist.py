"""
Playlist Manager - Lists Exercise
"""


def add_song(playlist: list[str], song: str) -> list[str]:
    """
    Add a song to the end of the playlist.
    
    Args:
        playlist: The current playlist
        song: The song to add
    
    Returns:
        The modified playlist
    """
    # TODO: Add the song to the playlist and return it
    pass


def remove_song(playlist: list[str], song: str) -> list[str]:
    """
    Remove the first occurrence of a song from the playlist.
    
    Args:
        playlist: The current playlist
        song: The song to remove
    
    Returns:
        The modified playlist (unchanged if song not found)
    """
    # TODO: Remove the song if it exists, then return the playlist
    pass


def get_song_at_position(playlist: list[str], position: int) -> str:
    """
    Get the song at a specific position in the playlist.
    
    Args:
        playlist: The current playlist
        position: The index position (0-based)
    
    Returns:
        The song at that position, or "Invalid position" if out of range
    """
    # TODO: Return the song at the given position or "Invalid position"
    pass


def get_first_three(playlist: list[str]) -> list[str]:
    """
    Get the first three songs from the playlist.
    
    Args:
        playlist: The current playlist
    
    Returns:
        A new list with the first three songs (or fewer if playlist is shorter)
    """
    # TODO: Return a slice of the first three songs
    pass


def reverse_playlist(playlist: list[str]) -> list[str]:
    """
    Return a reversed copy of the playlist.
    
    Args:
        playlist: The current playlist
    
    Returns:
        A new list with songs in reverse order
    """
    # TODO: Return a reversed copy of the playlist
    pass


def total_songs(playlist: list[str]) -> int:
    """
    Count the total number of songs in the playlist.
    
    Args:
        playlist: The current playlist
    
    Returns:
        The number of songs
    """
    # TODO: Return the length of the playlist
    pass


def contains_song(playlist: list[str], song: str) -> bool:
    """
    Check if a song is in the playlist.
    
    Args:
        playlist: The current playlist
        song: The song to search for
    
    Returns:
        True if the song is in the playlist, False otherwise
    """
    # TODO: Check if the song is in the playlist
    pass


def combine_playlists(playlist1: list[str], playlist2: list[str]) -> list[str]:
    """
    Combine two playlists into one.
    
    Args:
        playlist1: The first playlist
        playlist2: The second playlist
    
    Returns:
        A new list containing all songs from both playlists
    """
    # TODO: Combine the two playlists and return the result
    pass
