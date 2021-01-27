# Pico y Placa predictor
## Description:
This is a project built with Python 3. It is a "Pico y Placa" predictor, which predicts whether or not a vehicle with a plate number ending in a certain digit is allowed to circulate on according to the rules listed below.

*Vehicles with plates ending in the numbers cannot circulate on the following days between the time periods 07:00 - 09:30 and 16:00 - 19:30:*

Mon | Tue | Wed | Thu | Fri | Sat | Sun 
----|-----|-----|-----|-----|-----|-----
1, 2 | 3, 4 | 5, 6 | 7, 8 | 9, 0 | No Restrictions | No Restrictions 

In this minimalistic approach to building a Pico y Placa predictor there are four main files and a folder:
* rules.py - contains the rules that the predictor will be based on.
* predictor.py - contains all the methods to deduce whether or not a vehincle with a given plate number is allowed to circulate.
* utilities.py - contains all the complimentary functions that allow to format or validate the input data.
* main.py - allows to test the project on console.
* "tests" folder - contains a detailed test suite built to put each implemeted method to the test. 

## Run the code:
To run this project, this repository should be cloned or downloaded. Once the repository is in a local folder, the project can be executed on console using the following command on any terminal or IDE with Python 3:

`python main.py`

To run the test suite, the following command should be used:

`python -m unittest -v tests.test_suite`

