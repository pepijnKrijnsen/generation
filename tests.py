import os
import unittest
import upload_blog_entry

class tester(unittest.TestCase):

    def testFirst(self):
        upload_blog_entry.main()

    def testPassedFilenameIsValidFile(self):
        os.system("python3 upload_blog_entry.py test.html")
        self.assertTrue(open("blog_date.html"))
        os.remove("blog_date.html")
        

if __name__ == "__main__":
    unittest.main()
