# library
import csv

# 開啟 CSV 檔案
with open('output.csv', newline='', encoding="utf-8") as csvFile:

  # 1.直接讀取：讀取 CSV 檔案內容
  rows = csv.reader(csvFile)

  # 2.自訂分隔符號：讀取 CSV 檔案內容
  rows = csv.reader(csvFile, delimiter=',')

  # 迴圈輸出 每一列
  for row in rows:
    print(row)