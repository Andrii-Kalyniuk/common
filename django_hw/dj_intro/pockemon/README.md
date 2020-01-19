#DOD (definition of done)
+ Docker container with django
+ Test that cover endpoints
+ Create docker-compose

##Django Into
+ Create initial django app with health check route
+ Healthcheck route must be added to docker-compose
+ Add test to health check route
+ Implement root view with simple html page
+ This view should render a link to next page
+ Implement that shows data from another API in internet
+ This view must render the returned value(use fantasy about the message)
+ Render the link to index screen
+ Add integration tests that checks if the data is returned from API
+ Add negative case to tests when API returns data that can’t be parsed
