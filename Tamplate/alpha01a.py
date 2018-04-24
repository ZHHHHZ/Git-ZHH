def run_formula(dv):
    alpha01a=dv.add_formula('alpha01a',"1/PB+1/PE",
                            is_quarterly=True
                            ,add_data=False)
    return alpha01a
