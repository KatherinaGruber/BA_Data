# This is a sample Python script.
import pandas as pd
import matplotlib.pyplot as plt

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

df1995 = pd.read_spss('Latinobarometro_1995_data_english_spss_v2014_06_27.sav')
df1996 = pd.read_spss('Latinobarometro_1996_datos_english_spss_v2014_06_27.sav')
df1997 = pd.read_spss('Latinobarometro_1997_datos_english_spss_v2014_06_27.sav')
df1998 = pd.read_spss('Latinobarometro_1998_datos_english_v2014_06_27.sav')
df2000 = pd.read_spss('Latinobarometro_2000_datos_eng_v2014_06_27.sav')
df2003 = pd.read_spss('Latinobarometro_2003_datos_eng_v2014_06_27.sav')
df2004 = pd.read_spss('Latinobarometro_2004_datos_eng_v2014_06_27.sav')
df2005 = pd.read_spss('Latinobarometro_2005_datos_eng_v2014_06_27.sav')
df2006 = pd.read_spss('Latinobarometro_2006_datos_eng_v2014_06_27.sav')
df2007 = pd.read_spss('Latinobarometro_2007_datos_eng_v2014_06_27.sav')
df2008 = pd.read_spss('Latinobarometro_2008_datos_eng_v2014_06_27.sav')
df2009 = pd.read_spss('Latinobarometro_2009_datos_eng_v2014_06_27.sav')
df2010 = pd.read_spss('Latinobarometro_2010_datos_eng_v2014_06_27.sav')
df2011 = pd.read_spss('Latinobarometro_2011_eng.sav')

venezuela1995 = df1995.loc[df1995['pais'] == 'Venezuela']
venezuela1996 = df1996.loc[df1996['pais'] == 'Venezuela']
venezuela1997 = df1997.loc[df1997['idenpa'] == 'Venezuela']
venezuela1998 = df1998.loc[df1998['idenpa'] == 'Venezuela']
venezuela2000 = df2000.loc[df2000['IDENPA'] == 'Venezuela']
venezuela2003 = df2003.loc[df2003['idenpa'] == 'Venezuela']
venezuela2004 = df2004.loc[df2004['idenpa'] == 'Venezuela']
venezuela2005 = df2005.loc[df2005['idenpa'] == 'Venezuela']
venezuela2006 = df2006.loc[df2006['idenpa'] == 'Venezuela']
venezuela2007 = df2007.loc[df2007['idenpa'] == 'Venezuela']
venezuela2009 = df2009.loc[df2009['idenpa'] == 'Venezuela']
venezuela2010 = df2010.loc[df2010['IDENPA'] == 'Venezuela']
venezuela2011 = df2011.loc[df2011['IDENPA'] == 'Venezuela']

Q1 = "Would you say that in [nation], in the last 5 years, the quality of health has gone down, gone up or stayed the same"
mapping_1 = {"Decreased a lot": 1, "Decreased a little": 2, "Increased a little": 3, "Increased a lot": 4}

Q2 = "how much access to healthcare do you have today?"
mapping_2 = {"1. Nothing": 1, "2": 1, "3": 2, "4": 2, "5": 2, "6": 3, "7": 3, "8": 3, "9": 4, "10. Everything": 4, }

Q3 = "Would you say that in [Country], in the last 12 months, the quality of health care has gone down, gone up or stayed the same?"
#mapping_1

Q4 = "Would you say that in [country], in the last 12 months, the quality of public hospitals has gone down, gone up or stayed the same?"
mapping_0 = {"Got a lot worse": 1, "Got somewhat worse": 2, "Somewhat improved": 3, "Improved a lot": 4}

Q5 = "Would you say that you are very satisfied, rather satisfied, not very satisfied or not at all satisfied with the healthcare you have access to?"
mapping_3 = {"Not at all satisfied": 1, "Not very satisfied": 2, "Rather satisfied": 3, "Very satisfied": 4}

Q6 = "How satisfied are you with the way hospitals work"
#mapping_3

avg1995 = pd.to_numeric(venezuela1995['p58a'].map(mapping_1)).mean()
avg1996 = pd.to_numeric(venezuela1996['p62a'].map(mapping_1)).mean()
avg1997 = pd.to_numeric(venezuela1997['bp16a'].map(mapping_2)).mean()
avg1998 = pd.to_numeric(venezuela1998['sp76a'].map(mapping_1)).mean()
avg2000 = pd.to_numeric(venezuela2000['P18ST.A'].map(mapping_0)).mean()
avg2003 = pd.to_numeric(venezuela2003['p25na'].map(mapping_3)).mean()
avg2004 = pd.to_numeric(venezuela2004['p39sta'].map(mapping_3)).mean()
avg2005 = pd.to_numeric(venezuela2005['p91sta'].map(mapping_3)).mean()
avg2006 = pd.to_numeric(venezuela2006['p80st.a'].map(mapping_3)).mean()
avg2007 = pd.to_numeric(venezuela2007['p57st.a'].map(mapping_3)).mean()
avg2009 = pd.to_numeric(venezuela2009['p71n.a'].map(mapping_3)).mean()
avg2010 = pd.to_numeric(venezuela2010['P65ST.A'].map(mapping_3)).mean()
avg2011 = pd.to_numeric(venezuela2011['P66ST.A'].map(mapping_3)).mean()

plt.figure(figsize=(10, 6))  # Set the figure size

averages = [avg1995, avg1996, avg1997, avg1998, avg2000, avg2003, avg2004, avg2005, avg2006, avg2007, avg2009, avg2010, avg2011]
years = [1995, 1996, 1997, 1998, 2000, 2003, 2004, 2005, 2006, 2007, 2009, 2010, 2011]

print(averages)

plt.plot(years, averages, marker='o')  # 'o' for markers

plt.xlabel('Year')
plt.ylabel('Average')
plt.title('Healthcare satisfaction: 1 = Not at all satisfied , 4 = Very satisfied')
plt.grid(True)
plt.show()

