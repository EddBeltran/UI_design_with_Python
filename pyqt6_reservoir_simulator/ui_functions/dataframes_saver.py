import pandas as pd
#from openpyxl import load_workbook
import numpy as np

##----------------------------------------ESTA FUNCION ALMACENA LOS DATOS EN COLUMNAS DE UN ARCHIVO .XLSX
#def SAVE_4COLUMS_XLSX(filename, sheet, col1_name, col1, col2_name, col2, col3_name, col3, col4_name, col4):
#    #------ CLEAR SHEET CONTENT
#    wb = load_workbook(filename)
#    if sheet in wb.sheetnames:
#        std=wb.get_sheet_by_name(sheet)
#        wb.remove_sheet(std)
#    wb.save(filename)
#    
#    n1 = np.array(col1, dtype=object)
#    n2 = np.array(col2)
#    n3 = np.array(col3)
#    n4 = np.array(col4)
#    
#    dif = abs(len(col1) - len(col3))
#    
#    if len(col1) > len(col3):
#        col3 = np.append(n3, np.zeros(dif) + np.nan)
#        col4 = np.append(n4, np.zeros(dif) + np.nan)
#        
#    else:
#        col1 = np.append(n1, np.zeros(dif) + np.nan)
#        col2 = np.append(n2, np.zeros(dif) + np.nan)
#    
#    print(len(col1), len(col3))
#    
#    df = pd.DataFrame()
#    writer = pd.ExcelWriter(filename, mode='a')
#    df[col1_name] = col1;    df[col2_name] = col2
#    df[col3_name] = col3;  df[col4_name] = col4
#        
#    df.to_excel(writer, index = False, sheet_name = sheet)
#    writer.save()



def save_two_columns(filename, first_column_array, second_column_array):#, first_column_name="Column 1", second_column_name="Column 2"):      
    df = pd.DataFrame({
        'Column 1': first_column_array,
        'Column 2': second_column_array
        })

    df.to_csv(filename, index=False)
    print("broo")

    #df = pd.DataFrame()
    #df_writer = pd.ExcelWriter(filename, mode='a')
    #df[first_column_name] = first_column_array
    #df[second_column_name] = second_column_array
    #    
    #df.to_excel(df_writer, index = False)#, sheet_name = sheet_name)
    #df_writer.save()


#def SAVE_DATAFRAME_XLSX(filename, sheet, dataframe):
#    #------ CLEAR SHEET CONTENT
#    wb = load_workbook(filename)
#    if sheet in wb.sheetnames:
#        std=wb.get_sheet_by_name(sheet)
#        wb.remove_sheet(std)
#    wb.save(filename)
#       
#    df = dataframe
#    writer = pd.ExcelWriter(filename, mode='a')
#    df.to_excel(writer, index = False, sheet_name = sheet)
#    writer.save()
    




#def SAVE_CELLS_XLSX(filename, sheet, row_x, col_x, cell_value):
#    
#    wb = load_workbook(filename,read_only=False, keep_vba= True)
#    if sheet in wb.sheetnames:
#        std=wb[sheet]
#        cell = col_x + str(row_x)
#        std[cell]  = cell_value
#        #std.cell(row = row_x, column = col_x).value  = cell_value
#    
#    wb.save(filename)


