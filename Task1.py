import csv

infilename = "index.csv"
outfilename = "statistic.csv"


def mean(massive):
    if not(massive):
        return 0
    return sum(massive)/len(massive)


def disp(massive):
    if not(massive):
         return 0
    array = []
    m = mean(massive)
    for i in massive:
        array.append((i-m)**2)
    return mean(array)

def mediana(array):
     if not(array):
          return 0
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
     infl_rate = []
     unemploy_rate = []
     GPD = []
     EFFR = []
     names = ["GPD","EFFR","infl_rate","unemploy_rate"]

     try:
         with open(infilename,"r", newline = "") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Effective Federal Funds Rate"]:
                    EFFR.append(float(row["Effective Federal Funds Rate"])) 
                if row["Real GDP (Percent Change)"]:
                    GPD.append(float(row["Real GDP (Percent Change)"])) 
                if row["Unemployment Rate"]:
                    unemploy_rate.append(float(row["Unemployment Rate"]))   
                if row["Inflation Rate"]:
                    infl_rate.append(float(row["Inflation Rate"]))   
     except Exception:
         print("Файл не найден. Ошибка")
         return

     matrix = [GPD,EFFR,infl_rate,unemploy_rate]
     if not any(len(row) > 0 for row in matrix):
         print("Датасет пустой. Ошибка!")
         return
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

