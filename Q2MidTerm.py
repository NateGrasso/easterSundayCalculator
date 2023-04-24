#MidTerm Essay Question 2
#Nathan Grasso
#CSC 119473
#Description: A program that takes a given year and calculates the date for Easter Sunday
### 
#process using Carl Friedrich Gauss algorithm
year = int(input("Enter year: "))
stepA= year % 19
stepB= year // 100
stepC = year % 100
stepD = stepB // 4
stepE = stepB % 4
stepG = (8 * stepB + 13)//25
stepH = (19 * stepA + stepB - stepD - stepG + 15) % 30
stepJ = stepC // 4
stepK = stepC % 4
stepM = (stepA + 11 * stepH) // 319
stepR = (2 * stepE + 2 * stepJ - stepK - stepH + stepM + 32) % 7
stepN = (stepH - stepM + stepR + 90) // 25
stepP = (stepH - stepM + stepR + stepN + 19) % 32
#Result
print("Easter Sunday: ",stepN,"/", stepP,"/",year)