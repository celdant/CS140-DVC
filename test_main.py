from main import main
import pytest
import sys
from io import StringIO

def test_main_output():
    # Redirect stdout to capture print statements
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Run the main function
    main()
    
    # Get the output
    output = captured_output.getvalue()
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    # Check if the output matches expected
    expected_output = "Hello World\nCS140: Python Programming\n"
    assert output == expected_output, f"Expected '{expected_output}' but got '{output}'"