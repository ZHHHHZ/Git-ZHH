def run_formula(dv):
    alpha07a=dv.add_formula('alpha07a',
                            "eps_diluted2+tot_compreh_inc_parent_comp/total_share+(surplus_rsrv+undistributed_profit)/total_share"
                            ,is_quarterly=False,add_data=False)

    return alpha07a 

