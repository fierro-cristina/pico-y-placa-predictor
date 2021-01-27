# Pico y Placa predictor: Description
This is a project built with Python 3. It is a "Pico y Placa" predictor, which predicts whether or not a vehicle with a plate number ending in a certain digit is allowed to circulate on according to the following rules:

## Plates ending in the following numbers cannot circulate between the time periods 07:00 - 09:30 and 16:00 - 19:30 on the following days:

Mon | Tue | Wed | Thu | Fri | Sat | Sun 
----|-----|-----|-----|-----|-----|-----
1, 2 | 3, 4 | 5, 6 | 7, 8 | 9, 0 | N/A | N/A 

In this minimalistic approach to building a Pico y Placa predictor there are four main files:
* rules.py - contains the rules that the predictor will be based on.
* predictor.py - contains all the methods to deduce whether or not a vehincle with a given plate number is allowed to circulate.
* utilities.py - contains all the complimentary functions that allow to format or validate the input data.
* main.py - allows to test the project on console.
The "tests" folder contains a detailed test suite built to put each implemeted method to the test. 

# Run the code:
To run this project on console, this repository should be cloned or downloaded. Once the repository is in a local folder, the project can be executed on console using the following command on any terminal or IDE with Python 3:

`<$python main.py>`

To run the test suite, the following command should be used:

`<$python -m unittest -v tests.test_suite>`

