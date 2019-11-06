from .context import deeplearning
from deeplearning import modules
import unittest

class testModules(unittest.TestCase):
    """Test the methods for the module.py module"""

    def setUp(self):
        self.linearmodule = modules.LinearModule()

