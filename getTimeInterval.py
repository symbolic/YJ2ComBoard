#-*- coding: utf-8 -*-

import sys
import math

def power(base, n):				#16进制转10进制：base = 256,
	if n == 1:
		return 1
	return base*power(base, n-1)

def hex_decimal(hex, n = 0):		#16进制转换成10进制，n为小数点个数, 返回值str
	temp = hex.split(' ')
	b = 0
	for i in range(len(temp)):
		b += string.atoi(temp[i], 16) * power(256, len(temp)-i)

	if n:
		return str(b/power(10, n+1))
	else:
		return str(b)

def bcd_decimal(hex, n = 0):		#BCD转换成10进制，n为小数点个数, 返回数值
	temp = hex.split(' ')
	b = 0
	for i in range(len(temp)):
		b += int(temp[i]) * power(100, len(temp)-i)
		
	if n:
		return b/power(10, n+1)
	else:
		return b

def time_second(time):			#时间转换成秒， 返回值int
	second = 0
	time_list = time.split(':')
	for i in range(len(time_list)):
		second += int(time_list[i])*power(60, len(time_list)-i)

	return second

def time_span(time1, time2):	#计算时间间隔，返回值int

	return math.fabs(time_second(time2) - time_second(time1))

def getTimeInterval():
	fp_src = open(sys.argv[1], 'r')
	dest = open('result.txt', 'w')
	
	oneline = fp_src.readline()
	lastTimeString = ''
	while oneline:
		timeString = oneline.split(' ')[0]
		if lastTimeString == '':
			lastTimeString = timeString
		
		if time_span(lastTimeString, timeString) > 10:
			dest.write(lastTimeString + '\t' + timeString + '\t' + 
			str(time_span(timeString, lastTimeString)) + '\n')
		
		lastTimeString = timeString	
		oneline = fp_src.readline()
		
	fp_src.close()
	dest.close()
	
def main():
	getTimeInterval()

if __name__ == '__main__':
	main()