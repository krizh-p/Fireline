from typing import List
import numpy as np
import sklearn
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plot
import data

#Train AI with Linear Regression
def train(prediction_data: dict[List]):
    #Create list of Long's & Lat's
    dataframe = pd.DataFrame(prediction_data)
    dataframe = dataframe[["LONG", "LAT"]]
    #X-coordinated(Longitude)
    X = dataframe[["LONG"]]
    #Y-coordinate(Latitude)
    Y = dataframe["LAT"]

    # Create LinearRegression Model
    model = linear_model.LinearRegression()

    #Train AI
    model.fit(X, Y)

    #Visualize
    plot.scatter(X, Y, label='Data Points')
    plot.plot(X, model.predict(X), color='red', label='Linear Regression Line')
    plot.xlabel('X-coordinate')
    plot.ylabel('Y-coordinate')
    plot.legend()
    plot.title('Linear Regression for Coordinates')
    plot.show()

def main():
    spread = data.prediction_data()
    prediction = train(spread)

if __name__ == '__main__':
    main()