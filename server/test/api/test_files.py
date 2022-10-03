import pytest
import pathlib

from tnyml.api import files


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("test.jpg", True),
        ("test.jpeg", True),
        ("test", False),
        ("test.png", False),
        ("test.txt", False),
    ],
)
def test_allowed_file_should_return_true(filename, expected):
    assert expected == files.allowed_file(filename)


def test_upload_and_get_file(client):
    filename = "testfile.jpg"
    test_root_path = pathlib.Path(__file__).parent.parent
    testfile = test_root_path / "data" / filename

    test_image = testfile.open("rb")
    # need to specify tuple instead of just BytesIO to not send
    # full path to image. That would result in the original image to get
    # deleted on cleanup
    post_response = client.post(
        "/api/files", data={"file": (test_image, filename, "image/jpeg")}
    )
    assert post_response.status_code == 200

    image_url = post_response.json["image_url"]
    try:
        get_response = client.get(image_url)
        assert get_response.status_code == 200
        with open(testfile, "rb") as f:
            testfile_bytes = f.read()
            assert testfile_bytes == get_response.data
    finally:
        # remove created file again
        project_root_path = pathlib.Path(__file__).parent.parent.parent
        testfile_name = image_url.split("/api/files/")[-1]
        image_path = (
            project_root_path / "public" / "user" / "uploads" / testfile_name
        )
        image_path.unlink()
