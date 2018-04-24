def run_formula(dv, param = None):
    defult_param = {'t':10}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha08a=dv.add_formula('alpha08a',
                            "-Ts_Sum(If((MA5>MA10) && (MA20>MA60),1,0),%s)"%(t)
                            ,is_quarterly=False,add_data=False)

    return alpha08a     
