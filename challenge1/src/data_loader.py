import pandas as pd
import kagglehub
import os
from functools import cache
from src.tools import get_clothes_mapping

merge_target_types = ['Pullover','Coat','Shirt']
MERGED_LABEL = 10

@cache
def get_dataset_path():
    return kagglehub.dataset_download("zalando-research/fashionmnist")

def load_raw(split):
    return pd.read_csv(os.path.join(get_dataset_path(), f"fashion-mnist_{split}.csv"))

def get_train_base_data():
    return get_X_and_y(load_raw("train"))

def get_test_base_data():
    return get_X_and_y(load_raw("test"))

def get_train_base_data_merged():
    return get_X_and_y(merge_types(load_raw("train"), merge_target_types))

def get_test_base_data_merged():
    return get_X_and_y(merge_types(load_raw("test"), merge_target_types))

def get_X_and_y(df):
    X = df.drop('label',axis=1)
    y = df['label']
    return X, y

def merge_types(df, target_types):
    inverted_clothes_mapping = {v: k for k, v in get_clothes_mapping().items()}
    unknown = [item for item in target_types if item not in inverted_clothes_mapping]
    if unknown:
        raise ValueError(f"Nieznane typy: {unknown}")
    keys = [inverted_clothes_mapping[item] for item in target_types]
    mapping = dict.fromkeys(keys, MERGED_LABEL)
    df = df.copy()
    df['label'] = df['label'].replace(mapping)
    return df
