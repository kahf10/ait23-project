import pandas as pd


def tsrt(series):
    """
    Method to handle outliers using the three sigma rule of thumb
    @:param series: Pandas series of a single user's data
    """
    sigma = series.std()
    mean = series.mean()
    ndf = series.copy()
    for i in range(1, len(series) - 1):
        if series.iloc[i] > 3 * sigma + mean or series.iloc[i] < mean - 3 * sigma:
            ndf.iloc[i] = (series.iloc[i - 1] + series.iloc[i + 1]) / 2
    return ndf


def preprocess_mean(df):
    """
    Filters the data set by removing rows with too much missing data as well as willing null values with
    the mean of their respective rows
    @:param df: Pandas dataframe to be preprocessed
    """
    valuecount = df.shape[1] - 2
    drop = []
    for i in range(df.shape[0]):  # Checks to see the percentage of missing values
        percentage = (df.iloc[i].isna().sum()) / valuecount
        if percentage > 0.5:  # If above 50%, the row will be dropped later
            drop.append(i)

    # Dropping the rows
    for i in reversed(drop):
        df.drop(df.index[i], inplace=True)

    # Filling the null values with the mean of the row
    df = df.where(df.notna(), df.mean(axis=1), axis=0)

    return df


def preprocess_outliers(df):
    """
    Sifts through the dataframe and handles outliers by replacing each row with the output of tsrt()
    @:param df: Pandas dataframe
    """
    for i in range(df.shape[0]):
        df.iloc[i][2:] = tsrt(df.iloc[i][2:])
    return df


def main(df):
    """
    Main preprocessing method
    @:param df: Original pandas dataframe
    :return: Preprocessed csv file
    """
    df = preprocess_mean(df)
    df = preprocess_outliers(df)
    df.to_csv("output.csv")


df = pd.read_csv("sgcc_data.csv")

if __name__ == "__main__":
    main(df)
