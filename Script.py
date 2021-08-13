import pandas as pd
import Sort as sort
import time

def output_sheet(list):
    df = pd.DataFrame(list).T
    df = df.rename(columns={0: 'Um', 1: 'Duque', 2: 'Trinca', 3: 'Quadra', 4: 'Quina', 5: 'Sena' }, index={0: 'Quantidade'})
    df.to_excel("output.xlsx",sheet_name='Sheet_name_1')  

colunas = int(input('Insira o número de linhas: ')) - 1

start_time = time.time()

data = pd.read_excel('Lot. Resultados até 2004 - 2020.xlsx', sheet_name = 'Avaliação', usecols = 'S:AQ', 
                    nrows=colunas, skiprows=1, header=None)

data.columns = range(0, 25)

#linha 0 igual a linha 2 no excel
#coluna 0 igual a coluna S no excel

row_list = [0] * 15

counter_row_list = 0 
for i in range(colunas): 
    for j in range(25): 
        if ( pd.notnull(data.loc[i,j]) ): 
            row_list[counter_row_list] = data.loc[i,j] #store df in array
            counter_row_list += 1

        if( j == 24):
            counter_row_list = 0
            sort.find_sequence(row_list)

output_sheet(sort.sequence)

print("--- %s seconds ---" % (time.time() - start_time)) #execution time
print("Finalizado")

input('')