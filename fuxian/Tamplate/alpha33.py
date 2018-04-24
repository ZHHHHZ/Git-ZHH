def run_formula(dv, param = None):
    defult_param = {'t1':5,'t2':5,'t3':5,'t4':240,'t5':20,'t6':5}
    if not param:
        param = defult_param
    
    alpha33=dv.add_formula('alpha33',
                           "((((-1*Ts_Min(low,%s))+Delay(Ts_Min(low,%s),%s))*Rank(((Ts_Sum(Return(close,1),%s)-Ts_Sum(Return(close,1),%s))/220)))*Ts_Rank(volume,%s))"%(param['t1'],param['t2'],param['t3'],param['t4'],param['t5'],param['t6'])
                           ,is_quarterly=False,add_data=False)

    return alpha33
