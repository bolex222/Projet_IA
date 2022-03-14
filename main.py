import numpy as np
import pandas as pd
import os
import math

from numpy.random import default_rng
random = default_rng(42) # stabilité du processus d'aléatoir d'une exécution à l'autre


DATA_BASE_URL = 'https://raw.githubusercontent.com/bolex222/Projet_IA/main/data/'
DATA_FOLDER = "./Data"
IMAGES_FOLDER = "./resources/images"

FOLDERS = [DATA_FOLDER, IMAGES_FOLDER]
CSV = ["general_data.csv", "manager_survey_data.csv", "employee_survey_data.csv", "in_time.csv", "out_time.csv"]

def createFolders():
    for folder in FOLDERS:
        if not os.path.isdir(folder):
            os.makedirs(folder)

# createFolders() # Creates all the folders used by our notebook

def loadData():
    list_dataframe = []
    for csv in CSV:
        list_dataframe.append(pd.read_csv(DATA_BASE_URL + csv))
    return list_dataframe

list_dataframe = loadData()


def prepare_dates(df_in, df_out):
    final_time_df = df_in

    cols = df_in.columns[1:]
    df_in[cols] = df_in[cols].apply(pd.to_datetime, errors='coerce')

    cols2 = df_out.columns[1:]
    df_out[cols2] = df_out[cols2].apply(pd.to_datetime, errors='coerce')

    df_in_no_id = df_in[df_in.columns[1:]]
    df_out_no_id = df_out[df_out.columns[1:]]

    final_time_df[df_in.columns[1:]] = df_out_no_id[df_out.columns[1:]] - df_in_no_id[df_in.columns[1:]]

    means_df = pd.DataFrame({'EmployeeID': final_time_df[final_time_df.columns[0]]})
    means_df['mean'] = final_time_df[final_time_df.columns[1:]].mean(axis=1)
    print(means_df)


prepare_dates(list_dataframe[3], list_dataframe[4])



def mergeData(dataframes):
    final_dataframe = dataframes.pop(0) # Get the first element of the array
    for dataframe in dataframes:
        final_dataframe = final_dataframe.merge(dataframe, how="inner", on="EmployeeID", validate="1:1")
    return final_dataframe

# merged_data = mergeData(list_dataframe)