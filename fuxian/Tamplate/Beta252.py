def run_formula(dv): 
    from jaqs_fxdayu.data.dataservice import LocalDataService
    dataview_folder = r'F:/data'
    ds = LocalDataService(fp = dataview_folder)
    def RM(A):
        c=ds.index_daily(universe=['000300.SH'],start_date=20170101,end_date=20180101,fields='close')
        b=dv.get_ts('close')
        df=c[0]

        for i in range (1,len(b.columns)):
            df.insert(i,i,df['close'])
        df.index=b.index
        df.columns=b.columns
    
        A=df
        return A

    RM=dv.add_formula('RM',"Return(RM(close),1)",is_quarterly=False,add_data=True,register_funcs={"RM":RM})
    
    Beta252=dv.add_formula('Beta252',
                           "Covariance(Return(close,1),Return(RM,1),252)/(StdDev(RM,252)^2)"
                           ,is_quarterly=False,add_data=False)

    return Beta252

