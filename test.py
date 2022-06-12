import FinanceDataReader as fdr
kosdaq_index = fdr.DataReader('KQ11', start='2022-06-09', end='2022-06-10')
print(kosdaq_index)