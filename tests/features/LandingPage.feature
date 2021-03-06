@LandingPage
Feature: Verify UI and functionality of the Sign In Page

    Background: Fire-up the browser
        Given START 'Chrome' browser

	###########################################
	#				Landing Page              #
	###########################################
	@Done
 	Scenario: Verify the HackerRank logo is displayed on the sign in page
 		Given navigate to "hr_prod_url" page
 		Then validate the "hackerrank_logo" is displayed on the "HomePage" page

	@Done
	Scenario: Verify the the list of elements are displayed on the sign in page
		Given navigate to "hr_prod_url" page
		Then validate the following top navigation elements are displayed on the home page
			| **List of Selectors** 	|
			| top_nav_developers		|
			| top_nav_for_companies		|
			| top_nav_for_school		|
			| top_nav_login_button		|
			| top_nav_signup_button 	|

    @Done
    Scenario: Verify the user is navigated to the login page when clicking the login button
      Given navigate to "hr_prod_url" page
      When the user clicks the "top_nav_login_button" button on the "HomePage" page
      Then validate the user is navigated to the "hr_login_url" page

    @Done
    Scenario: Verify the user is navigated to the sign-up page when clicking the sign-up button
      Given navigate to "hr_prod_url" page
      When the user clicks the "top_nav_signup_button" button on the "HomePage" page
      Then validate the user is navigated to the "hr_signup_url" page

    @Done @asdf
    Scenario: Verify the user is navigated to the Solutions page when clicking the "For Companies" top navigation button
      Given navigate to "hr_prod_url" page
      When the user clicks the "top_nav_for_companies" button on the "HomePage" page
      Then validate the user is navigated to the "hr_products_url" page