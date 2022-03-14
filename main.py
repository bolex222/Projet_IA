GENERAL_DATA_URL = 'https://drive.google.com/file/d/1cUFu_HcarG_QuxBVQqfXWYdF4sTYEo0Q/view?usp=sharing'
MANAGER_SURVEY_DATA_URL = 'https://drive.google.com/file/d/1ACruOssglzmc0lh7rCcd51yKYPHhHyOS/view?usp=sharing'
EMPLOYEE_SURVEY_DATA_URL = 'https://drive.google.com/file/d/1OvMGx-8-b6tIAvkpHec7LeR1eh9WyPx8/view?usp=sharing'
IN_TIME_URL = 'https://drive.google.com/file/d/1GkQwfoUss19US_99RVsFv7De5Vhhq6y2/view?usp=sharing'
OUT_TIME_URL = 'https://drive.google.com/file/d/1ZVxVB-ytHUjtT5SpGvojD95FPFegCN7r/view?usp=sharing'


import pandas as pd
import requests
import io

# data download function
def import_data_from_GDrive_link(link):
    # generate download link
    dwn_url = 'https://drive.google.com/uc?id=' + link.split('/')[-2]
    response = requests.get(dwn_url)
    print(response)
    file_object = io.StringIO(response.content.decode('utf-8'))
    csv = pd.read_csv(file_object)
    return csv

def import_all_data():
    all_merged_data = import_data_from_GDrive_link(GENERAL_DATA_URL)
    # all_data_url = [MANAGER_SURVEY_DATA_URL, EMPLOYEE_SURVEY_DATA_URL, IN_TIME_URL, OUT_TIME_URL]
    all_data_url = []

    for url in all_data_url:
        current_data_set = import_data_from_GDrive_link(url)
        all_merged_data = pd.merge(all_merged_data, current_data_set, on='EmployeeID')

    return all_merged_data


data = import_all_data()
# print(data.head())