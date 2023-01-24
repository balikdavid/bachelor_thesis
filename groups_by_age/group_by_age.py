import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
"""
#Male histogram
gender_tmc_data = excel_data.loc[:,['gender','TMC']]

males_df = gender_tmc_data[(gender_tmc_data['gender'] == 'M')]
female_df = gender_tmc_data[(gender_tmc_data['gender'] == 'F')]
print(males_df)

659     B   3.C     2011-01-29  2021-06-28  10(y)   4(m) --> hodne krajni hodnota ve veku, o 1 den mu nebylo 5 mesicu --> ok
"""



def age_count(excel_data):
    """
    return df with calculated age in months and years for every person below
    """
    date1 = excel_data.loc[:,['datum narození','datum testu']]
    #in next steps i can take only int because we want accuracy to months, not weeks so i can gave weeks up
    date1['date_diff_months'] = ((date1['datum testu'] - date1['datum narození'])  / np.timedelta64(1, 'M')).astype(int) 
    date1['years'] = (date1['date_diff_months'] / 12).astype(int)
    date1['months'] = date1['date_diff_months'] % 12

    return date1.loc[:,['years','months']]



def get_group(*limits,ex_data): #(y1,m1,y2,m2) --> lower limit, upper limit
    age_count_df = age_count(ex_data)
    all_df = ex_data.join(age_count_df)
    group_by_age = all_df.loc[(all_df['years'] == limits[0]) & (all_df['months'] >= limits[1]) & (all_df['months'] <= limits[3])]
    #print(group_by_age.drop(columns=['years','months']))
    return group_by_age.drop(columns=['years','months'])
    
    
    

if __name__ == '__main__':
    excel_data = pd.read_excel('../Data_1_11_2022_anonymizovana_data.xlsx',sheet_name='List1')

    
    gr1 = get_group(6,4,6,7,ex_data=excel_data)
    gr2 = get_group(6,8,6,11,ex_data=excel_data)
    
    gr3 = get_group(7,0,7,3,ex_data=excel_data)
    gr4 = get_group(7,4,7,7,ex_data=excel_data)
    gr5 =get_group(7,8,7,11,ex_data=excel_data)
    gr6=get_group(8,0,8,5,ex_data=excel_data)
    gr7=get_group(8,6,8,11,ex_data=excel_data)
    gr8=get_group(9,0,9,5,ex_data=excel_data)
    gr9=get_group(9,6,9,11,ex_data=excel_data)
    gr10=get_group(10,0,10,5,ex_data=excel_data)
    gr11=get_group(10,6,10,11,ex_data=excel_data)
    
    #print(gr1)
    
    with pd.ExcelWriter(r'../Student_groups_by_age.xlsx', engine='openpyxl', mode='a') as writer:
       gr1.to_excel(writer, sheet_name = 'Group1' ,index = False)
       gr2.to_excel(writer, sheet_name = 'Group2',index = False)
       gr3.to_excel(writer, sheet_name = 'Group3',index = False)
       gr4.to_excel(writer, sheet_name = 'Group4',index = False)
       gr5.to_excel(writer, sheet_name = 'Group5',index = False)
       gr6.to_excel(writer, sheet_name = 'Group6',index = False)
       gr7.to_excel(writer, sheet_name = 'Group7',index = False)
       gr8.to_excel(writer, sheet_name = 'Group8',index = False)
       gr9.to_excel(writer, sheet_name = 'Group9',index = False)
       gr10.to_excel(writer, sheet_name = 'Group10',index = False)
       gr11.to_excel(writer, sheet_name = 'Group11',index = False)
    
    
    """
      with pd.ExcelWriter(r'../Data_1_11_2022_anonymizovana_data.xlsx', engine='openpyxl', mode='a') as writer:
       gr1.to_excel(writer, sheet_name = 'Group1' ,index = false)
       gr2.to_excel(writer, sheet_name = 'Group2')
       gr3.to_excel(writer, sheet_name = 'Group3')
       gr4.to_excel(writer, sheet_name = 'Group4')
       gr5.to_excel(writer, sheet_name = 'Group5')
       gr6.to_excel(writer, sheet_name = 'Group6')
       gr7.to_excel(writer, sheet_name = 'Group7')
       gr8.to_excel(writer, sheet_name = 'Group8')
       gr9.to_excel(writer, sheet_name = 'Group9')
       gr10.to_excel(writer, sheet_name = 'Group10')
       gr11.to_excel(writer, sheet_name = 'Group11')
    
    
    
    """
  
        
    
    
    #starsi deti
    #print(get_group(11,0,11,11,ex_data=excel_data))
    #print(get_group(12,0,11,11,ex_data=excel_data))
    d = get_group(11,0,11,11,ex_data=excel_data)
    #print(d)
    d_dates = d.loc[:,['datum narození','datum testu']]
    #df = df.assign(wrong_time=rounded_time.astype('datetime64[ns]'))
    dd_dates_ok = d_dates.assign(datum_narozeni=d_dates['datum narození'].astype('datetime64[ns]'),datum_testu=d_dates['datum testu'].astype('datetime64[ns]'))
    #print(dd_dates_ok)
    
    #testing save data frame into excel
    
        
        
        
    """
    with pd.ExcelWriter(r'Data_1_11_2022_anonymizovana_data.xlsx', engine='openpyxl', mode='a') as writer:  
    get_group(11,0,11,11,ex_data=excel_data).to_excel(writer, sheet_name='DATA_OUT')
        
        
        
    data2 =  pd.read_excel('Data_1_11_2022_anonymizovana_data.xlsx',sheet_name='DATA_OUT')
    print(data2)
    
    """

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    SPATNA FUNKCE -> NEBERE V POTAZ DEN PSANI TESTU
    def age_six_four_to_six_seven(excel_data):
 
    6.4 - 6.7 
   
    #dates = excel_data.loc[:,['datum narození']] #rok-mesic-den
    #df[df['date_of_birth'] < pd.Timestamp(date(2002,1,1))]
    #pd.Timestamp(date(2015,10,1))
    #pd.Timestamp(date(2016,1,1))
    date_from = pd.Timestamp(date(2015,10,1))#rok,mesic,den --> todle brat jako params od kdy do kdy a tim padem staci 1 jedina funkce
    date_to = pd.Timestamp(date(2016,2,1))
    dates_ok = excel_data[
                (excel_data['datum narození'] >= date_from) &
                (excel_data['datum narození'] < date_to)
                ]
                          
    return dates_ok

    """
    

   





