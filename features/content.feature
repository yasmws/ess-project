Feature: Content

Scenario: adding new evaluation
Given I am logged  as user  “Paulo”
And I am at the "Reservation History" page
When I add “5 stars” for reservation in hotel “ Dalhousie Castle”
And I save the changes 
Then I am still at the "Reservation History" page
And I can see in hotel “ Dalhousie Castle” reservation “5 Stars” evaluation

Scenario: See the evaluation in hotel profile
Given I am logged as user  “qin” 
And I am do a evaluation for “Stanley Hotel”
When I change the page to “Stanley Hotel Profile”
Then I can see my evaluation for the reservation at “Stanley Hotel” in “23/09/2023” 
	
Scenario: adding new evaluation comment but not add any star
Given I am logged as user  “Robert”
And I am at the "Reservation History" page
When I do not add any “stars” for reservation in hotel “ Cecil hostel”
And add “comment” try save the changes
Then I am still at the "Reservation History" page
And I can not save the changes

Scenario: Try change a evaluation
Given I am logged as user  “Sara” 
And have a evaluation for the reservation at “Ahwahnee Hotel” on “30/02/2023”
When I am go to "Reservation History"
And try change my review at “Ahwahnee Hotel” from “30/02/2023”
Then I can change any parameter in evaluation. 

Scenario Add evaluation
Given A user exist in data bank named “Jonh” and Password “Doe”
And the user “Jonh” have a finish reservation at hotel “ Hotel California”
When I do login with that user 
and I do “POST” request  to “../stars”  with data ”5” in star field content
and empty data in comment field content
Then  the date was saved in system