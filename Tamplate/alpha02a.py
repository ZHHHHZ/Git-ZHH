def run_formula(dv, param = None):
    defult_param = {'t':1}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha02a=dv.add_formula('alpha02a',
                            "-(Rank(turnover_ratio)+Rank(close/Delay(close,%s)-1))/2"%(t)
                            ,is_quarterly=False,add_data=False)
    return alpha02a      
