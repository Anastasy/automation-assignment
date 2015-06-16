from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import re
 
links_landing_titles = {
    "Features"   : "features",
    "Company"    : "values",
    "Community"  : "open sauce",
    "Solutions"  : "selenium testing",
    "Docs"       : "docs",
    "Enterprise" : "enterprise", 
    "Login"      : "login",
    "Pricing"    : "pricing",
    "Sign"       : "sign up",
    "Resources"  : "resources",
    }
    

class SauceLabsGlyphLinks(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []

    def test_sauce_labs_glyph_links(self):
        driver = self.driver

        for link in links_landing_titles:
            
            #open sauce labs home page
            driver.get(self.base_url)
            
            #click on glyph for drop down menu
            driver.find_element_by_css_selector("a.hamburger").click()
            
            #reg expression for dictionary keys
            newLink = (r'%s' % link)
            
            #click on high-level links
            driver.find_element_by_xpath('//nav[@id ="global"]//a[contains(text(), "%s")]' % newLink).click()
            
            #reg expression for dictionary values(expected titles)
            expected_title = re.compile(r'%s' %links_landing_titles[link],  re.IGNORECASE)
            
            #check if titles match
            try: self.assertRegexpMatches(driver.title, expected_title)
            
            #error if title doesn't match
            except AssertionError as e: self.verificationErrors.append(str(e))


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)







# full titles
'''
   "Docs" : "Sauce Labs Docs",
    "Enterprise" : "Sauce Labs: Enterprise-grade testing on Sauce", 
    "Login" : "Sauce Labs: Login",
    "Pricing" : "Sauce Labs: Pricing",
    "Sign" : "Sauce Labs: Sign Up for a Free Trial",
    "resources" : "resources"
'''
