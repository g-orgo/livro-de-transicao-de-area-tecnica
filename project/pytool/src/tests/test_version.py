from pytool.version import current_version


def test_current_version() -> None:
    assert current_version() == "0.1.0"
