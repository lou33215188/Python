# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 18:46:05 2018

@author: 王磊
"""

gradePoint = []
print("input 0 to the credit to end this program !")
sumCredit = 0
sumGradePoint = 0
endGradePoint = 0


while(1):
     myCredit = int(input("Please input your credit :"))
     if myCredit == 0:
          break
     myGradePoint = float(input("Please input your grade point :"))
     gradePoint.append([myCredit,myGradePoint])

for eachCredit,eachGradePoint in gradePoint:
     sumCredit += eachCredit
     sumGradePoint += eachCredit*eachGradePoint

endGradePoint = sumGradePoint/sumCredit
print("SumCredit:", str(sumCredit))
print("SumGradePoint", str(sumGradePoint))
print("EndGradePoint", str(endGradePoint))
