def run_formula(dv, param = None):
    defult_param = {'t1':20,'t2':5}
    if not param:
        param = defult_param
        
    alpha04a=dv.add_formula('alpha04a',
                            "-(Ts_Mean(vwap*volume,%s)+Ts_Mean(vwap*volume,%s))/2"%(param['t1'],param['t2'])
                            ,is_quarterly=False,add_data=False)

    return alpha04a

