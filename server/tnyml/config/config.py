from pathlib import Path


def get_upload_folder():
    UPLOAD_FOLDER = (
        Path(__file__).parent.parent.parent / "public" / "user" / "uploads"
    )
    return UPLOAD_FOLDER


def get_allowed_extensions():
    ALLOWED_EXTENSIONS = {"jpg", "jpeg"}
    return ALLOWED_EXTENSIONS
