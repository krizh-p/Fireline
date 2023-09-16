from typing import List
import numpy as np
import sklearn
from sklearn import linear_model
import data

#Train AI with Linear Regression
def train(prediction_data: List[dict]):
    #Create list of Long's & Lat's
    long_list = []
    lat_list = []
    for fire in prediction_data:
        #MAYBE SPLIT UP DATA BASED ON closeness (by 10)
        long_list.append([fire["LONG"]])
        lat_list.append([fire["LAT"]])
    
    print(f"Long List: {long_list}\n\n Latt List: {lat_list}")

    #Convert to NumPy Array (Enhanced Array)
    longitude = np.array(long_list)
    latitude = np.array(lat_list)

    #Set values for training & testing w/ long and lat
    long_train, long_test, lat_train, lat_test = sklearn.model_selection.train_test_split(longitude, latitude, test_size = 0.1)

    #Create LinearRegression Model
    model = linear_model.LinearRegression()
    #Train model
    model.fit(long_train, lat_train)
    #Accuracy
    accuracy = model.score(long_test, lat_test)
    print(accuracy)

    #Make Prediction Longitude
    spread = model.predict(long_test)
    for i in range(10):
        print(f"Prediction Long: {spread[i]}\nLatitude Test:  {lat_test[i]} \nLongitude Test: {long_test[i]}\n") 
    
    #Make Prediction Longitude
    spread1 = model.predict(lat_test)
    for i in range(10):
        print(f"Prediction Lat: {spread1[i]}\nLatitude Test:  {lat_test[i]} \nLongitude Test: {long_test[i]}\n") 


def main():
    spread = data.prediction_data()
    prediction = train(spread)

if __name__ == '__main__':
    main()