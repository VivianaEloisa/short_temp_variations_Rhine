from config import *

"""
This python script is composed by the classes "ChemicalReader", 
"ChemLogReader", "ChemPCReader" and "SSCReader" that read all the data frames 
related to the chemical data.
"""


class ChemicalsReader:
    """
        The class 'ChemicalsReader' has the function to read the
        'chemicals_python.csv' csv file. Making  it reusable for other
        codes.
    """

    def __init__(self, csv_file_name="chemicals_python.csv", delimiter=","):
        """
        param csv_file_name: csv file with the chemicals data.
        param delimiter: separator in the csv file.
        """
        self.sep = delimiter
        self.chemical_data = csv_file_name
        self.read_data(csv_file_name)

    def read_data(self, csv_file_name):
        """
        Reading the csv file and creating a pandas dataframe.
        param: csv_file_name:csv file with the chemicals data.
        """

        self.chemical_data = pd.read_csv(csv_file_name,
                                         header=0,
                                         sep=self.sep,
                                         usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8,
                                                  9, 10, 11, 12, 13, 14, 15],
                                         names=["Date",
                                                "Na - mg/l",
                                                "Mg - mg/l",
                                                "Al - mg/l",
                                                "Si2 - mg/l",
                                                "P - mg/l",
                                                "S - mg/l",
                                                "K - mg/l",
                                                "Mn - mg/l",
                                                "Fe - mg/l",
                                                "Pb - mg/l",
                                                "SSC(15s) - mg/l",
                                                "Campaign",
                                                "Q - m3/s",
                                                "V - m/s",
                                                "Grain Size"])

    def __call__(self, csv_file_name, *args, **kwargs):
        print()

    """
     It is used to make the object callable (as a function),
     so if we have an instance x that defines __call__(self, csv_file_name)
     we can do x(csv_file_name), which is actually a shortcut to
     x.__call__ (csv_file_name).
     """


# y = ChemicalsReader()
# x = y.chemical_data
# print(x)


class ChemLogReader:
    """
        The class 'ChemLogReader' has the function to read the
        'df_chem_log_10.csv' csv file. Making  it reusable for other
        codes.
    """

    def __init__(self, csv_file_name="df_chem_log_10.csv", delimiter=","):
        """
        param csv_file_name: csv file with the log-transformed chemicals data.
        param delimiter: separator in the csv file.
        """
        self.sep = delimiter
        self.chemical_log_data = csv_file_name
        self.read_data(csv_file_name)

    def read_data(self, csv_file_name):
        """
        Reading the csv file and creating a pandas dataframe.
        param: csv_file_name:csv file with the chemicals data.
        """

        self.chemical_log_data = pd.read_csv(csv_file_name,
                                             header=0,
                                             sep=self.sep,
                                             usecols=[1, 2, 3, 4, 5, 6, 7,
                                                      8, 9, 10, 11, 12, 13, 14,
                                                      15, 16],
                                             names=["Na - mg/l",
                                                    "Mg - mg/l",
                                                    "Al - mg/l",
                                                    "Si2 - mg/l",
                                                    "P - mg/l",
                                                    "S - mg/l",
                                                    "K - mg/l",
                                                    "Mn - mg/l",
                                                    "Fe - mg/l",
                                                    "Pb - mg/l",
                                                    "SSC(15s) - mg/l",
                                                    "Q - m3/s",
                                                    "V - m/s",
                                                    "Grain Size",
                                                    "Campaign",
                                                    "Date"])

    def __call__(self, csv_file_name, *args, **kwargs):
        print()

    """
     It is used to make the object callable (as a function),
     so if we have an instance x that defines __call__(self, csv_file_name)
     we can do x(csv_file_name), which is actually a shortcut to
     x.__call__ (csv_file_name).
     """


# y = ChemLogReader()
# x = y.chemical_log_data
# print(x)

class ChemPCReader:
    """
        The class 'ChemPCReader' has the function to read the
        'scores_chem_pca.csv' csv file. Making  it reusable for other
        codes.
    """

    def __init__(self, csv_file_name="scores_chem_pca.csv",
                 delimiter=";"):
        """
        param csv_file_name: csv file with the log-transformed chemicals data.
        param delimiter: separator in the csv file.
        """
        self.sep = delimiter
        self.chemical_pca_data = csv_file_name
        self.read_data(csv_file_name)

    def read_data(self, csv_file_name):
        """
        Reading the csv file and creating a pandas dataframe.
        param: csv_file_name:csv file with the PCA data.
        """

        self.chemical_pca_data = pd.read_csv(csv_file_name,
                                             header=0,
                                             sep=self.sep,
                                             usecols=[1, 2, 3, 4, 5, 6, 7, 8],
                                             names=["PC1", "PC2", "PC3", "PC4",
                                                    "PC5", "PC6", "Campaign",
                                                    "Date"])

    def __call__(self, csv_file_name, *args, **kwargs):
        print()

    """
     It is used to make the object callable (as a function),
     so if we have an instance x that defines __call__(self, csv_file_name)
     we can do x(csv_file_name), which is actually a shortcut to
     x.__call__ (csv_file_name).
     """


# y = ChemPCReader()
# x = y.chemical_pca_data
# print(x)

class SSCReader:
    """
    Author: Viviana Eloisa Quezada Dominguez
        The class 'SSCReader' has the function to read the
        'ssc_test_camp.csv' csv file. Making  it reusable for other
        codes.
    """

    def __init__(self, csv_file_name="ssc_test_camp.csv",
                 delimiter=";"):
        """
        param csv_file_name: csv file with the log-transformed chemicals data.
        param delimiter: separator in the csv file.
        """
        self.sep = delimiter
        self.ssc_data = csv_file_name
        self.read_ssc(csv_file_name)

    def read_ssc(self, csv_file_name):
        """
        Reading the csv file and creating a pandas dataframe.
        param: csv_file_name:csv file with the PCA data.
        """

        self.ssc_data = pd.read_csv(csv_file_name,
                                    header=0,
                                    sep=self.sep,
                                    usecols=[0, 1, 2],
                                    names=["test", "pred", "Campaign"
                                           ])

    def __call__(self, csv_file_name, *args, **kwargs):
        print()

    """
     It is used to make the object callable (as a function), 
     so if we have an instance x that defines __call__(self, csv_file_name) 
     we can do x(csv_file_name), which is actually a shortcut to 
     x.__call__ (csv_file_name).
     """

# y = SSCReader()
# x = y.ssc_data
# print(x)
