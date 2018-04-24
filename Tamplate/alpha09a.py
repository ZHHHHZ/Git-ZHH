def run_formula(dv):
    alpha09a=dv.add_formula('alpha09a',
                            "dupont_roa+taxes_surcharges_payable"
                            ,is_quarterly=True,add_data=False)

    return alpha09a    