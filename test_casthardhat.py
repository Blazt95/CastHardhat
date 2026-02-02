# test_casthardhat.py
"""
Tests for CastHardhat module.
"""

import unittest
from casthardhat import CastHardhat

class TestCastHardhat(unittest.TestCase):
    """Test cases for CastHardhat class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CastHardhat()
        self.assertIsInstance(instance, CastHardhat)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CastHardhat()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
