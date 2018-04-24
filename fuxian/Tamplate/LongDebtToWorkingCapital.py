def run_formula(dv):
    LongDebtToWorkingCapital=dv.add_formula('LongDebtToWorkingCapital_J',
                                            "tot_non_cur_liab/(tot_cur_assets-tot_cur_liab)"
                                            ,is_quarterly=True,add_data=False)

    return LongDebtToWorkingCapital 
