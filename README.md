
#  IMDb Website Automation Test - Frontend
This repository contains automated tests for the IMDb website's frontend using Selenium and Selenium Grid. The test cases cover various functionalities of the website's home page, menu, search, rating, watchlist, sign-in, language, browser trailers, and social media apps.

##  Prerequisites
Ensure that the following tools are installed on your machine:

-  Python (version 3.x)
-  Selenium
-  WebDriver
-  Selenium Grid

##  Test Cases
###  Home Page
-  Verify the presence of elements on the home page.
-  Navigate to different sections of the home page.
###  Menu
-  Open the menu and verify the options.
  -  Navigate to different sections from the menu.
-  Most Popular Movies
  -   Access the most popular movies section.
  -  Verify the presence of movie listings.
  -  Number of Ratings
  -  Check the number of ratings for a specific movie.
-  Top 250 TV Shows
  -  Access the Top 250 TV shows section.
  -  Verify the presence of TV show listings.
  -  Rate a movie or TV show.
  -  Verify the updated rating.
###  Search
-  All
  -  Perform a general search.
  -  Verify the search results.
  -  Search Movie
  -  Search for a specific movie.
  -  Verify the movie details in the search results.
###  Watchlist
-  Adding Movie: Add a movie to the watchlist.
  -  Verify the movie is added successfully.
-  Deleting Movie: Remove a movie from the watchlist.
  -  Verify the movie is removed successfully.
###  Sign In
-  Login with an IMDb Account
  -  Log in with a valid IMDb account.
  -  Verify successful login.
-  Sign In with Google
  -  Log in with a Google account.
  -  Verify successful login.
###  Language
-  Change the website language to English.
-  Change the website language to Français (France).
###  Browser Trailers
-  Play a video.
-  Mute the video.
-  Unmute the video.
-  Enter fullscreen mode.
###  Social Media Apps
-  Go to Instagram.
-  Go to YouTube.
