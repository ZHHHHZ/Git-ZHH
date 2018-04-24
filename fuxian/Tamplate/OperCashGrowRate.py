def run_formula(dv):
    OperCashGrowRate=dv.add_formula('OperCashGrowRate_J',
                                    "(TTM(net_cash_flows_oper_act)/Delay(TTM(net_cash_flows_oper_act),4))-1"
                                    ,is_quarterly=True,add_data=False)

    return OperCashGrowRate 
