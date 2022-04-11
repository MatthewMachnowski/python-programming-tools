from pandas import DataFrame

def get_xml():
    df = DataFrame([[1, 0], [5, 7]], columns=["a","b"])
    return df.to_xml()