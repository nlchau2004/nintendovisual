For Workout Project 4, I decided to use two APIs to use as data for my graphs. The main function contains the interactive
functionality for the code. When initially ran, the code will generate the data by using the REST APIs to scrape from the
web. Afterwards, the user is prompted to choose a dataset to graph. There are three options: "Pokemon", "Smash", or "Quit."
Any other option will result in raising an AssertionError that has been handled.

I have provided two images of the graphs that were created as a result of this program. The image with the "Pokemon" labeling
shows a graph that uses the original 151 Pokemon. The y-axis is the current 16 types of Pokemon that can exists, while the
x-axis is the amount of pokemon that are categorized in that type. One thing to note is that dual-type pokemon will be counted
for both types, so keep that in mind. The second image, labeled with "Smash", shows a graph that uses Smash Ultimate characters
up to Min-Min (This is because the API hasn't been updated for up to Sora). The y-axis is the series that are in collaboration
and the x-axis is the amount of characters representing their series. Since there aren't characters that originate from multiple
series, they are only counted for one series. 
