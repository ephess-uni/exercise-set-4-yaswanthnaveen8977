import os

def get_data_file_path(file_name: str) -> str:
    """
    get_data_file_path returns the absolute path to the a filename in the data directory
    in the root folder of this repository--regardless of where the main program is called
    from.

    Parameters
    ----------
    file_name : str
        The name of the file--excluding path.

    Returns
    -------
    str
        The absolute path to the desired file if the file exists. Raises FileNotFound
        error otherwise.
    """
    root_directory, _ = os.path.split(__file__)
    full_path = os.path.abspath(
        os.path.join(
            root_directory,
            '..',
            'data',
            file_name
        )
    )

    if not os.path.exists(full_path):
        raise FileNotFoundError(f'Filename {file_name} not found in {root_directory}')

    return full_path
