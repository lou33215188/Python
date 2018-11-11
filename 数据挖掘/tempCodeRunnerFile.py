import numpy
import matplotlib.pyplot as plt
import os
import csv

_MAX__NUMER = 6


xLabelDateList = []
yLabelDateList = []


def testFile(expdatefilename='fuck-hzfFORexp.csv'):    # expdatefilename为指定的数据文件
    if expdatefilename not in os.listdir():
        expdatecsv = open(expdatefilename, 'a', newline="")
        csv_writer = csv.writer(expdatecsv)
        expdatecsv.close()
        for index in range(0, _MAX__NUMER):
            xLabelDate = index*0.5
            voltageDate = float(input("Input data"+str(xLabelDate)+':'))
            csv_writer.writerow([xLabelDate, voltageDate])
    else:
        csv_file = open(expdatefilename, 'r')
        csv_reader = csv.reader(csv_file)
        print(csv_file)
        if csv_reader.line_num < _MAX__NUMER:
            csv_file_size = csv_reader.line_num
            print(csv_file_size)
            for index in range(csv_file_size, _MAX__NUMER):
                xLabelDate = index*0.5
                voltageDate = float(input("Input data"+str(xLabelDate)+':'))
                csv_writer.writerow([xLabelDate, voltageDate])
    drawPic(expdatefilename)


def drawPic(expdatefilename='fuck-hzfFORexp.csv'):
    plt.figure(figsize=(12, 6))
    csv_file = open(expdatefilename, 'r')
    csv_reader = csv.reader(csv_file)
    for item in csv_reader:
        print(item)
        xLabelDateList.append(float(item[0]))
        yLabelDateList.append(float(item[1]))

    plt.plot(xLabelDateList, yLabelDateList, color='red', linewidth=2, label='h')
    plt.xlabel('横轴:电压', fontproperties='FangSong', fontsize=20, color='r')
    plt.ylabel('纵轴:电流', fontproperties='FangSong', fontsize=20, color='b')
    plt.show()

def getPeak():
    pass


def main():
    testFile()


if __name__ == '__main__':
    main()
