import pandas as pd


def delete_columns_na(input_file, output_file, delete_columns, drop_na = True):
    """
    Function to preprocess a raw dataframe. It can delete one or more columns and 
    drops NA values.

    Arguments:
    input_file -- String Path to the csv file of the titanic dataset (The csv separator should be ";").
    output_file -- String Path where the new csv of the new process data is going to be saved.
    delete_columns -- List of colums to delete of the dataframe.
    drop_na -- Set True to drop all NA values.

    Returns:
    A .csv of the processed dataframe in the specified location. 
    """

    data = pd.read_csv(input_file, sep = ";")
    data.drop(delete_columns, axis = 1, inplace=True) 
    
    if drop_na == True:
        data.dropna(inplace=True)
    else:
        pass
    
    return data.to_csv(output_file, index=False)

    