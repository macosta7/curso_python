# Exercício 5 - FreeCodeCamp - Python
## Sea Level Predictor

You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:

- Use Pandas to import the data from ```epa-sea-level.csv```. **Exercício 5.1**
- Use matplotlib to create a scatter plot using the ```Year``` column as the x-axis and the ```CSIRO Adjusted Sea Level``` column as the y-axis. **Exercício 5.2**
- Use the ```linregress``` function from ```scipy.stats``` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050. **Exercício 5.3**
- Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000. **Exercício 5.4**
- The x label should be ```Year```, the y label should be ```Sea Level (inches)```, and the title should be ```Rise in Sea Level```. **Exercício 5.5**

The boilerplate also includes commands to save and return the image.

Write your code in ```sea_level_predictor.py```. For development, you can use ```main.py``` to test your code.

The unit tests for this project are in ```test_module.py```. We imported the tests from ```test_module.py``` to ```main.py``` for your convenience.

Link GitPod: https://gitpod.io#snapshot/fc068c7e-925e-4ebe-8584-04af4302ff77