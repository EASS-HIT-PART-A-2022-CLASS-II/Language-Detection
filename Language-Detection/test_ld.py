import os
import os.path
import pytest
@pytest.mark.skipif(not os.path.exists('Language-Detection/trained_pipeline-0.5.0.pkl'), reason="File does not exist")
def test_file_exists():
    assert os.path.exists('Language-Detection/trained_pipeline-0.5.0.pkl') == True
