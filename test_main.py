from main import main
import pytest
import sys
from io import StringIO

def test_main_output():

    captured_output = StringIO()
    sys.stdout = captured_output
    

    main()
    
    output = captured_output.getvalue()

    sys.stdout = sys.__stdout__
    

    expected_output = "Hello World\nPython Programming\n"
    assert output == expected_output, f"Expected '{expected_output}' but got '{output}'"