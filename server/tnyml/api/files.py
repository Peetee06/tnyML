import flask

from config import config


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in config.get_allowed_extensions()
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
        image_path = config.get_upload_folder() / filename
        try:
            file.save(image_path)
        except FileNotFoundError as e:
            print(e)
            flask.abort(500, "File could not be saved")
        return {"image_url": f"/api/files/{filename}"}
    else:
        flask.abort(
            400,
            description=(
                "File extension not allowed. "
                f"Allowed extensions are: {config.get_allowed_extensions()}"
            ),
        )


def get_file(file_name):
    # TODO: 404 if file does not exist
    image_path = config.get_upload_folder()
    return flask.send_from_directory(image_path, file_name)
