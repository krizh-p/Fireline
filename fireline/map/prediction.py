from typing import List
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plot
import data

def export_prediction(lng: List[float], lat: float) -> List[dict]:
    export = []
    for i in range(len(lng)):
        export.append({"LONG": lng[i], "LAT": lat[i], "NAME": f"User {i+1}"})
    return export      


#Train AI with Linear Regression
def train(prediction_data: dict[List]):
    #Create list of Long's & Lat's
    dataframe = pd.DataFrame(prediction_data)
    dataframe = dataframe[["LONG", "LAT"]]
    #X-coordinated(Longitude)
    X = dataframe[["LONG"]]
    print(type(X))
    #Y-coordinate(Latitude)
    Y = dataframe["LAT"]

    # Create LinearRegression Model
    model = linear_model.LinearRegression()

    #Train AI & Predict
    model.fit(X, Y)
    predictions = model.predict(X)
    #Visualize
    plot.scatter(X, Y, label='Data Points')
    plot.plot(X, predictions, color='red', label='Linear Regression Line')
    plot.xlabel('X-coordinate')
    plot.ylabel('Y-coordinate')
    plot.legend()
    plot.title('Linear Regression for Coordinates')
    plot.show()

    #Create list of predicted points
    lngs, lats = []
    num_predicts = 3
    for i in range(-1, -1*num_predicts):
        lngs.append(X.values[i], predictions[-1])
    
    #Export points to Map
    export_prediction(lngs, lats)

def main():
    spread = data.prediction_data()
    prediction = train(spread)

if __name__ == '__main__':
    main()