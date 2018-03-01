@SignIn
Feature: Verify UI and functionality of the Sign In Page

    Background: Fire-up the browser
        Given START 'chrome' browser

	###########################################
	#				Sign In                   #
	###########################################
	@Done
 	Scenario: Verify the HackerRank logo is displayed on the sign in page
 		Given navigate to "hr_prod_url" page
 		Then validate the "hackerrank_logo" is displayed on the sign in page

	@asdf
	Scenario: Verify the the list of elements are displayed on the sign in page
		Given navigate to "hr_prod_url" page
		Then validate the following top navigation elements are displayed on the home page
			| **List of Selectors** 	|
			| top_nav_developers		|
			| top_nav_for_companies		|
			| top_nav_for_school		|