def run_formula(dv, param = None):
    defult_param = {'t1':252,'t2':1,'t3':20,'t4':20}
    if not param:
        param = defult_param
    
    alpha10a=dv.add_formula('alpha10a',
                            "-((close-Delay(close,%s))/Delay(close,%s)+StdDev(close/Delay(close,%s),%s)*Sqrt(%s))"%(param['t1'],param['t1'],param['t2'],param['t3'],param['t4'])
                            ,is_quarterly=False,add_data=False)
  
    return alpha10a
