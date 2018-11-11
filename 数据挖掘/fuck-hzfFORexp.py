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
        for index in range(0, _MAX__NUMER):
            xLabelDate = index*0.5
            voltageDate = float(input("Input data"+str(xLabelDate)+':'))
            csv_writer.writerow([xLabelDate, voltageDate])
    else:
        csv_file = open(expdatefilename, 'r')
        csv_reader = csv.reader(csv_file)

    drawPic(expdatefilename)

'''       if csv_reader.line_num < _MAX__NUMER:
            csv_file_size = csv_reader.line_num
            print(csv_file_size)
            for index in range(csv_file_size, _MAX__NUMER):
                xLabelDate = index*0.5
                voltageDate = float(input("Input data"+str(xLabelDate)+':'))
                print([xLabelDate, voltageDate])
                csv_writer.writerow([xLabelDate, voltageDate])'''

def drawPic(expdatefilename='fuck-hzfFORexp.csv'):
    plt.figure(figsize=(12, 6))
    csv_file = open(expdatefilename, 'r')
    csv_reader = csv.reader(csv_file)
    for item in csv_reader:
        print(item)
        try:
            xLabelDateList.append(float(item[0]))
            yLabelDateList.append(float(item[1]))
        except IndexError:
            pass
    plt.plot(xLabelDateList, yLabelDateList, color='blue', linewidth=2, label='h')
    plt.xlabel('横轴:Ug2k(V)', fontproperties='FangSong', fontsize=20, color='r')
    plt.ylabel('纵轴:Ia(uA)', fontproperties='FangSong', fontsize=20, color='b')
    plt.plot(22.0, 1.60, 'ko')
    plt.text(21.0, 1.80, '(22.0,1.60)')
    plt.plot(30.5, 6.05, 'ko')
    plt.text(29.5, 6.25, '(30.5,6.05)')
    plt.plot(41.5, 12.00, 'ko')
    plt.text(40.5, 12.20, '(41.5,12.00)')
    plt.plot(53.0, 17.60, 'ko')
    plt.text(52.0, 17.80, '(53.0,17.60)')
    plt.plot(65.0, 23.29, 'ko')
    plt.text(64.0, 23.49, '(65.0,23.29)')
    plt.plot(77.5, 26.92, 'ko')
    plt.text(76.5, 27.12, '(77.5,26.92)')

    plt.show()

def getPeak():
    pass


def main():
    testFile()


if __name__ == '__main__':
    main()
