from Code.config import *

"""
This script is composed by the classes "EnvReader" and "EnvLogReader" that 
are importing the dataframes of the sensor data for the measured data and the
log-transformed data.

"""


class EnvReader:
    """
        The class 'EnvReader' has the function to read the
        'env_python.csv' csv file. Making  it reusable for other codes.
    """

    def __init__(self, csv_file_name="env_python.csv", delimiter=","):
        """
        param csv_file_name: csv file with the environmental data.
        param delimiter: separator in the csv file.
        """
        self.sep = delimiter
        self.data = csv_file_name
        self.read_data(csv_file_name)

    def read_data(self, csv_file_name):
        """
        Reading the csv file and creating a pandas dataframe.
        param: csv_file_name:csv file with the environmental data.
        """

        self.data = pd.read_csv(csv_file_name,
                                header=0,
                                sep=self.sep,
                                usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                names=["Date", "Conductivity",
                                       "ODO - mg/l", "ORP mV",
                                       "Turbidity - FNU", "pH",
                                       "SSC (1s) - mg/l", "Campaign",
                                       "Q - m3/s", "V - m/s"])

    def __call__(self, csv_file_name, *args, **kwargs):
        print()

    """
     It is used to make the object callable (as a function),
     so if we have an instance x that defines __call__(self, csv_file_name)
     we can do x(csv_file_name), which is actually a shortcut to
     x.__call__ (csv_file_name).
     """


# y = EnvReader()
# x = y.data
# print(x)

class EnvLogReader:
    """
        The class 'EnvLogReader' has the function to read the
        'df_env_log_10.csv' csv file. Making  it reusable for other codes.
    """

    def __init__(self, csv_file_name="df_env_log_10.csv", delimiter=","):
        """
        param csv_file_name: csv file with the log-transformed environmental
         data.
        param delimiter: separator in the csv file.
        """
        self.sep = delimiter
        self.log_data = csv_file_name
        self.read_data(csv_file_name)

    def read_data(self, csv_file_name):
        """
        Reading the csv file and creating a pandas dataframe.
        param: csv_file_name:csv file with the log-transformed environmental
        data.
        """

        self.log_data = pd.read_csv(csv_file_name,
                                    header=0,
                                    sep=self.sep,
                                    usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                    names=["Conductivity",
                                           "ODO - mg/l", "ORP mV",
                                           "Turbidity - FNU",
                                           "pH", "SSC (1s) - mg/l", "Q - m3/s",
                                           "V - m/s", "Campaign", "Date"])

    def __call__(self, csv_file_name, *args, **kwargs):
        print()

    """
     It is used to make the object callable (as a function), 
     so if we have an instance x that defines __call__(self, csv_file_name) 
     we can do x(csv_file_name), which is actually a shortcut to 
     x.__call__ (csv_file_name).
     """

# y = EnvLogReader()
# x = y.log_data
# print(x)
