def run_formula(dv):
    alpha06a=dv.add_formula('alpha06a',
                            "Rank((close/TEMA5)-1)",
                            is_quarterly=False,add_data=False)

    return alpha06a   