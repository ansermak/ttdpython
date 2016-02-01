from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Masha has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box (Masha's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, she is taking to a new URL,
        #, and now the page lists "1: Buy peacock feathers" as
        # an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)
        masha_list_url = self.browser.current_url
        self.assertRegex(masha_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box invitin her to add another item. She
        # enters "Use peacock feathers to make a fly" (Masha is very
            # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')

        self.fail('Finish the test!')

        # Now a new user, Denis, comes along to the site

        ## We use a new browser session to make sure that no information
        ## of Masha's is coming throught from cookies etc #
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Denis visits the home page. There is no sign of Masha's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Denis starts a new list by entering a new item. He is less
        # interesting than Masha
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Denis gets his own unique URL
        denis_list_url = self.browser.current_url
        self.assertRegex(denis_list_url, '/lists/.+')
        self.assertNotEqual(denis_list_url, masha_list_url)

        # Again, there is no trace of Masha's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both got back to sleep
