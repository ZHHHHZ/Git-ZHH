def run_formula(dv):
    Kurtosis120=dv.add_formula('Kurtosis120',
                               "Ts_Kurtosis(Return(close,1),120)",
                               is_quarterly=False,add_data=False)

    return Kurtosis120
