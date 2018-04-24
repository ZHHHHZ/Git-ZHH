def run_formula(dv, param = None):
    defult_param = {'t1':13,'t2':2}
    if not param:
        param = defult_param
    
    def SMA(A,n,m):
        alpha = m/n
        return A.ewm(alpha=alpha, adjust=False).mean()

    alpha173=dv.add_formula('alpha173',
                            "3*SMA(close,%s,%s)-2*SMA(SMA(close,%s,%s),%s,%s)+SMA(SMA(SMA(Log(close),%s,%s),%s,%s),%s,%s)"%(param['t1'],param['t2'],param['t1'],param['t2'],param['t1'],param['t2'],param['t1'],param['t2'],param['t1'],param['t2'],param['t1'],param['t2'])
                            ,is_quarterly=False,add_data=False,register_funcs={"SMA":SMA})
    
    return alpha173
