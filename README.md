# FireLine

## Inspiration

With the recent widespread fires, such as those in Hawaii and Canada, we realized that there is a great need for not only a better way to raise proactive awareness about fires in North America, but also develop an avenue for citizen science to contribute to firefighting. We wanted to create a platform that would provide reliable and up-to-date information on fire activity, as well as leverage the power of machine learning to detect and predict fires based on new, realtime data sourced from the community.

## What it does

FireLine is a web application that offers two main services:
- A map that displays the location, size, and status of fires in North America, based on 1.88 million meticulously collected data logs. Users can explore the map, with plans of adding further data visualization methods such as filtering by date, region, and fire type. Currently, they can also click on any fire to see more details, such as the cause, duration, and impact of the fire.
- During active fires, local community members can directly help contribute to the real time tracking of the fire by upload a photo of the fire; we parse data from users through the use of a **linear regression machine learning model** that predicts where the fire is most likely to spread based on the geological location of user submissions. This also helps us approximate the size of the fire in real time.

## How we built it

FireLane was built with love using the following technologies:
- HTML5, CSS3, and JavaScript for frontend development.
- Leaflet, an open source JavaScript library for map visualization.
- Django as a Python framework for Back-end Web Development.
- Python and Python libraries such as pandas, and scikit for data processing and machine learning.
- MongoDB Atlas to host and query 

## Accomplishments that we're proud of

Some of the accomplishments we’re proud of are:
- Creating a comprehensive and interactive map of fires in North America
- Querying and visualizing a dataset of over 1.88 million fires with MongoDB (our first time using it!)
- Developing a linear regression machine learning model using our dataset on fire to predict where a fire will spread, given a list of existing fire locations (sourced in realtime by users) (our first time as well!).
- Building a asthetically pleasing, accessible, user-friendly and responsive web application.

## What's next for FireLine
- We plan on continuing FireLine and implementing aspects of the web app that we could not get to within the 36-hour time limit. 
