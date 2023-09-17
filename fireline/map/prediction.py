from typing import List
import pandas as pd
from sklearn import linear_model


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

    #Train AI & Predict
    model.fit(X, Y)
    predictions = model.predict(X)
    
    #Create list of predicted points
    points = []
    num_predicts = 3
    for i in range(-1, -1*num_predicts):
        points.append({
            "LONG" : X.values[i],
            "LAT" : predictions[i],
            "NAME": f"User {i}"
        })
    return points