from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Books', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("I've Read", header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a book you have read'
        )

        inputbox.send_keys('Shantaram')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == "1. Shantaram" for row in rows)
        )

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

