import numpy
import pandas as pd


def filter_temp(df_temp):
    df = df_temp.copy()
    df.loc[(df.TEM_MIN < -20.0) | (df.TEM_MIN > 60.0), "TEM_MIN"] = numpy.nan
    df.loc[(df.TEM_INS < -20.0) | (df.TEM_INS > 60.0), "TEM_INS"] = numpy.nan
    df.loc[(df.TEM_MAX < -20.0) | (df.TEM_MAX > 60.0), "TEM_MAX"] = numpy.nan
    return df


def filter_pto(df_pto):
    df = df_pto.copy()
    df.loc[(df.PTO_MIN < -20.0) | (df.PTO_MIN > 60.0), "PTO_MIN"] = numpy.nan
    df.loc[(df.PTO_INS < -20.0) | (df.PTO_INS > 60.0), "PTO_INS"] = numpy.nan
    df.loc[(df.PTO_MAX < -20.0) | (df.PTO_MAX > 60.0), "PTO_MAX"] = numpy.nan
    return df


def filter_press(df_press):
    df = df_press.copy()
    df.loc[df.PRE_MIN <= 0, "PRE_MIN"] = numpy.nan
    df.loc[df.PRE_INS <= 0, "PRE_INS"] = numpy.nan
    df.loc[df.PRE_MAX <= 0, "PRE_MAX"] = numpy.nan
    return df


def filter_umid(df_umid):
    df = df_umid.copy()
    df.loc[df.UMD_MIN < 0, "UMD_MIN"] = numpy.nan
    df.loc[df.UMD_INS < 0, "UMD_INS"] = numpy.nan
    df.loc[df.UMD_MAX < 0, "UMD_MAX"] = numpy.nan
    return df


def filter_ven(df_ven):
    df = df_ven.copy()
    df.loc[df.VEN_DIR < 0, "VEN_DIR"] = numpy.nan
    df.loc[df.VEN_RAJ < 0, "VEN_RAJ"] = numpy.nan
    df.loc[df.VEN_VEL < 0, "VEN_VEL"] = numpy.nan
    return df


def filter_prec(df_prec):
    df = df_prec.copy()
    df.loc[df.CHUVA < 0, "CHUVA"] = numpy.nan
    return df


def filter_radia(df_rad):
    df = df_rad.copy()
    df.loc[df.RAD_GLO < 0, "RAD_GLO"] = 0
    return df


def treat_df(row_data):
    df = row_data.copy()
    df = df.drop(columns=["Unnamed: 23"])
    df["HR_MEDICAO"] = df["HR_MEDICAO"].apply(lambda x: int(float(x.replace(":", "")[0:4]) / 100.))
    df["DT_MEDICAO"] = pd.to_datetime(df["DT_MEDICAO"], format="%Y-%m-%d").dt.date
    return df
