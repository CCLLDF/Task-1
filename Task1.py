import numpy as np
import csv

infilename = "index.csv"
outfilename = "statistic.csv"


def mean(massive):
    return sum(massive)/len(massive)

def disp(massive):
    array = []
    m = mean(massive)
    for i in massive:
        array=np.append(array,(i-m)**2)
    return mean(array)

def mediana(array):
     array = sorted(array)
     if (len(array)%2==0):
          res = (array[len(array)//2] + array[len(array)//2 - 1])/2
     else:
          res = array[len(array)//2]
     return res


# def cor(massive1,massive2):
#         cov = mean(massive1*massive2)-mean(massive1)*mean(massive2)
#         cor = cov/(disp(massive1)*disp(massive2))**0.5
#         return cor


def main():
     infl_rate = np.array([])
     unemploy_rate = np.array([])
     GPD = np.array([])
     EFFR = np.array([])
     names = ["GPD","EFFR","infl_rate","unemploy_rate"]


     with open(infilename,"r", newline = "") as file:
         reader = csv.DictReader(file)

         for row in reader:
             if row["Effective Federal Funds Rate"] and row["Real GDP (Percent Change)"] and row["Unemployment Rate"] and row["Inflation Rate"]:
                 EFFR=np.append(EFFR,float(row["Effective Federal Funds Rate"])) 
                 GPD=np.append(GPD,float(row["Real GDP (Percent Change)"])) 
                 unemploy_rate=np.append(unemploy_rate,float(row["Unemployment Rate"]))      
                 infl_rate=np.append(infl_rate,float(row["Inflation Rate"])) 

         matrix = [GPD,EFFR,infl_rate,unemploy_rate]

     with open(outfilename, "w", newline="") as file:
          columns = ["name","disp","mean","med"]
          writer = csv.DictWriter(file,fieldnames = columns)
          writer.writeheader()

          for i in range(len(names)):
                  writer.writerow(
                {
                    "name": names[i],
                    "disp": disp(matrix[i]),
                    "mean": mean(matrix[i]),
                    "med": mediana(matrix[i])
                }
            )

if __name__ == '__main__':
    main()

