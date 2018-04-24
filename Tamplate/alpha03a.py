def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':1,'t3':5}
    if not param:
        param = defult_param
    
    alpha03a=dv.add_formula('alpha03a',
                            "-(Rank(Ts_Mean(volume*vwap,%s))+Rank(Ts_Sum(close/Delay(close,%s),%s)))/2"%(param['t1'],param['t2'],param['t3'])
                            ,is_quarterly=False,add_data=False)

    return alpha03a

