from Code.config import *


class StatisticsReader:
    """
        The class 'UrsachenReader' has the function to read the
        'todo_python.csv' csv file. Making  it reusable for others
        water distribution designing codes.
    """

    def __init__(self, csv_file_name="statist_python.csv", delimiter=","):
        """
        param csv_file_name: csv file with the ursachen data.
        param delimiter: separator in the csv file.
        """
        self.sep = delimiter
        self.data_statist = csv_file_name
        self.read_data(csv_file_name)

    def read_data(self, csv_file_name):
        """
        Reading the csv file and creating a pandas dataframe.
        param: csv_file_name:csv file with the ursachen data.
        """

        self.data_statist = pd.read_csv(csv_file_name,
                                        header=0,
                                        sep=self.sep,
                                        usecols=[0, 1, 2, 3, 7, 9, 13, 15, 19,
                                                 21, 25, 27, 31, 33, 37, 39,
                                                 43,
                                                 45, 49, 51, 55, 57, 61, 63,
                                                 67, 69, 73, 75, 79, 81, 85,
                                                 87, 91, 93, 97, 99, 103, 105],
                                        names=["Campaign",
                                               "Q - m3/s",
                                               "V - m/s", "SSC(15s)-mg/l SD",
                                               "SSC(15s)-mg/l Inter",
                                               "SSC(1s)-mg/l SD",
                                               "SSC(1s)-mg/l Inter",
                                               "Turbidity-FNU SD",
                                               "Turbidity-FNU Inter",
                                               "ODO-mg/l SD",
                                               "ODO-mg/l Inter",
                                               "ORP-mV SD",
                                               "ORP-mV Inter",
                                               "Conductivity SD",
                                               "Conductivity Inter",
                                               "pH SD",
                                               "pH Inter",
                                               "Na-mg/l SD",
                                               "Na-mg/l Inter",
                                               "Mg-mg/l SD",
                                               "Mg-mg/l Inter",
                                               "Al-mg/l SD",
                                               "Al-mg/l Inter",
                                               "Si_2-mg/l SD",
                                               "Si_2-mg/l Inter",
                                               "P-mg/l SD",
                                               "P-mg/l Inter",
                                               "S-mg/l SD",
                                               "S-mg/l Inter",
                                               "K-mg/l SD",
                                               "K-mg/l Inter",
                                               "Mn-mg/l SD",
                                               "Mn-mg/l Inter",
                                               "Fe-mg/l SD",
                                               "Fe-mg/l Inter",
                                               "Pb-mg/l SD",
                                               "Pb-mg/l Inter",
                                               "Grain size"]

                                        )

    def __call__(self, csv_file_name, *args, **kwargs):
        print()

    """
     It is used to make the object callable (as a function), 
     so if we have an instance x that defines __call__(self, csv_file_name) 
     we can do x(csv_file_name), which is actually a shortcut to 
     x.__call__ (csv_file_name).
     """

#
# x = StatisticsReader()
# y = x.data_statist
# writer = pd.ExcelWriter('test1.xlsx')
# y.to_excel(writer)
# writer.save()
