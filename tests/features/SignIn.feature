@SignIn
Feature: Verify UI and functionality of the Sign In Page

    Background: Fire-up the browser
        Given START 'chrome' browser

	###########################################
	#				Sign In                   #
	###########################################
	@Done @asdf
 	Scenario: Verify the HackerRank logo is displayed on the sign in page
 		Given navigate to "hr_prod_url" page
 		Then validate the "hr_logo" is displayed on the sign in page


