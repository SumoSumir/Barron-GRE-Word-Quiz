# %% Cell 1
# python -m vevn BarronGre
# for Windows: BarronGre/Scripts/activate.bat
# for Ubuntu/Mac: source BarronGre/bin/activate
# pip install tabula-py
# %% Cell 2
import tabula 
file1="Barrons GRE wordlist.pdf" #file path to barron pdf, rename if needed
# table = tabula.read_pdf(file1,pages='all')#multiple_table=True
tabula.convert_into(file1, "Barron_csv_fileFull.csv",pages='all')

#%% Cell 3
import pandas
import random
csvData=pandas.read_csv("Barron_csv_fileFull.csv",usecols=[0,1],
names=['word','definition']) #error_bad_lines=False
# print(csvData.columns)
lowerLimit=int(input("Enter lower limit:"))
if lowerLimit<0:
    lowerLimit=0
upperLimit=int(input("Enter upper limit:"))
if upperLimit>csvData.shape[0]:
    upperLimit=csvData.shape[0]
userInput=1
wordCount=0
while userInput!=0:
    randomInteger=random.randint(lowerLimit,upperLimit)
    print("Words is : \033[1;32m",csvData['word'][randomInteger],"\033[00m")
    try:
        userInput=int(input("Press any key to continue and get the definition,\nPress 0 to exit"))
    except ValueError:
        wordCount=wordCount+1
    print("\n \033[1;32m",csvData['word'][randomInteger],"\033[00m : \033[91m",csvData['definition'][randomInteger],"\033[00m\n")
    print("Words Completed So Far:",wordCount,"\n\n")
 
# %%
