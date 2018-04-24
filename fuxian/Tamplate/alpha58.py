def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
    
    t = param['t']
    
    alpha58=dv.add_formula('alpha58',"Ts_Sum(If(close>Delay(close,1),1,0),%s)/%s*100"%(t,t)
                           ,is_quarterly=False,add_data=False)

    return alpha58