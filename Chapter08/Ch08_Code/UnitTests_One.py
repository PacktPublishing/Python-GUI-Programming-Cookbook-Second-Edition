'''
May 2017
@author: Burkhard
'''

import unittest
from Ch08_Code.LanguageResources import I18N

class GuiUnitTests(unittest.TestCase):
    
    def test_TitleIsEnglish(self):
        i18n = I18N('en')
        self.assertEqual(i18n.title, 
                         "Python Graphical User Interface")
        
#==========================                          
if __name__ == '__main__':
    unittest.main()
    
    

