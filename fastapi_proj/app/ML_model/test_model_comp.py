import os
import pytest

def test_version():
    # Import the package
    import model

    # Get the version from the package
    version = model.__version__

    # Assert that the version is what you expect
    assert version == "0.5.0"
