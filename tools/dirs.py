from pathlib import Path

BASE_DIRECTORY = Path(__file__).parents[1]

def find_file(*path, string=False):
    """
    Find a file given the path components. This is a utility function that can be used throughout 
    VIBE for development and ease of use when creating paths to files. 

    Parameters:
    --------------
        `*path`:
            Variable number of path components.
        `string` : bool
            If True, return the file path as a string. If False, return a Path object.

    Returns:
    ---------
        `str` or `Path`: 
            The file path as a string if `string` is True, otherwise a Path object.
    """
    
    path = Path(BASE_DIRECTORY, *path)
    return str(path) if string else path
