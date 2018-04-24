def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':2,'t3':5}
    if not param:
        param = defult_param
    
    alpha114=dv.add_formula('alpha114',
                            "((Rank(Delay(((high-low)/(Ts_Sum(close,%s)/%s)),%s))*Rank(Rank(volume)))/(((high-low)/(Ts_Sum(close,%s)/%s))/(vwap-close)))"%(param['t1'],param['t1'],param['t2'],param['t3'],param['t3'])
                            ,is_quarterly=False,add_data=False)

    return alpha114

