from pathlib import Path


def create_metadata(filepath):

    path = Path(filepath)

    return {

        "filename": path.name,

        "extension": path.suffix,

        "filepath": str(path),

    }