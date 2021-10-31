allBinares = {
    'EQUAL': lambda param, columnID: lambda var: param==var[columnID],
    'NOT_EQUAL': lambda param, columnID: lambda var: param!=var[columnID],
    'MORE_EQUAL': lambda param, columnID: lambda var: param<=var[columnID],
    'LESS_EQUAL': lambda param, columnID: lambda var: param>=var[columnID],
    'LESS': lambda param, columnID: lambda var: param>var[columnID],
    'MORE': lambda param, columnID: lambda var: param<var[columnID]
}
