import os
import tarfile
import urllib

down_root = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
housing_path = os.path.join("datasets", "housing")
housing_url = down_root + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_ur = housing_url, housing_pat = housing_path):
    os.makedirs(housing_pat, exist_ok= True)
    tgz_path = os.path.join(housing_pat, "housing.tgz")
    urllib.request.urlretrieve(housing_ur, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path= housing_pat)
    housing_tgz.close()

import pandas as pd

fetch_housing_data()
def load_housing_data(housing_pat = housing_path):
    csv_path = os.path.join(housing_pat, "housing.csv")
    return pd.read_csv(csv_path)


