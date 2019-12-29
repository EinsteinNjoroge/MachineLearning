# import keras
# import tensorflow
import pandas
import numpy

data = pandas.read_csv("data_set/student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences", "sex", "age"]]

item_to_predict = "age"
training_data = numpy.array(data)
expected_values = numpy.array(data[item_to_predict])

model_x, model_y, test_data_x, test_data_y = ""

print(expectedValues)
