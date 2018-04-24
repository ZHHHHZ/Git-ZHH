def run_formula(dv):  
    alpha05a=dv.add_formula('alpha05a',
                            "-(Rank(PE)+Rank(float_mv))/2"
                            ,is_quarterly=False,add_data=False)
    
    return alpha05a
