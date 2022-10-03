import flask

from config.config import get_upload_folder, get_allowed_extensions


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in get_allowed_extensions()
    )


def upload_file():
    # TODO make sure there are no conflicts in saved files

    if "file" not in flask.request.files:
        flask.abort(400, description="No file part in the request")
    file = flask.request.files["file"]
    if file.filename is None or file.filename == "":
        flask.abort(400, "No selected file")
    else:
        filename = str(file.filename)
    if allowed_file(file.filename):
        hashed_filename = str(hex(hash(filename.split(".")[0]))) + ".jpg"
        image_path = get_upload_folder() / hashed_filename
        try:
            file.save(image_path)
        except FileNotFoundError as e:
            print(e)
            flask.abort(500, "File could not be saved")
        return {"image_url": f"/api/files/{hashed_filename}"}
    else:
        flask.abort(
            400,
            description=(
                "File extension not allowed. "
                f"Allowed extensions are: {get_allowed_extensions()}"
            ),
        )


def get_file(file_name):
    # TODO: 404 if file does not exist
    image_path = get_upload_folder() / file_name
    return flask.send_file(image_path)
