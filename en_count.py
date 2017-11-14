#computeFrequency.py
import turtle

#变量count控制输出高频词的个数
#列表data[]用于统计词频，列表words[]用于记录一行中出现的单词
#定义x轴y轴扩大的倍数
count = 10
data = []
words = []
xScale = 30
yScale = 6

#将一行的符号替换为空格的函数replacePunctuations()
#参数为文本的一行
def replacePunctuations(line):
	for char in line:
		if char in "~`@#$%^&*()_+=<>?,.:;{}[]|\'""!":
			line = line.replace(char,"")
	return line	
			
#统计一行的词频的函数processLine()，
#参数为文本的一行line和统计词频的字典wordCounts
#是不是可以将wordCounts转化为全局变量？？？
def processLine(line, wordCounts):
	line = replacePunctuations(line)
	words = line.split()
	#print(words)
	for word in words:
		#print(type(word))
		if word in wordCounts:
			wordCounts[word] += 1
		else:
			wordCounts[word] = 1

#画线段drawLine(pen,x1,y1,x2,y2)
#pen表示画笔
#x1、y1和x2、y2分别表示线段的两个端点
def drawLine(pen, x1 , y1, x2, y2):
	pen.penup()
	pen.goto(x1,y1)
	pen.down()
	pen.goto(x2, y2)

#写字drawText（pen,x,y,text）
#pen表示画笔
#x、y表示线段的起始点
#text表示要写的文字
def drawText(pen, x, y, text):
	#出错，想的太简单了
	pen.up()
	pen.goto(x, y)
	pen.down()
	pen.write(text)

#画一个矩形drawRectangle(pen,x,y)

#x、y表示柱体的起始点（左下角的点）
def drawRectangle(pen, x, y):
	x = x * xScale
	y = y * yScale
	drawLine(pen, x-5 , 0, x-5, y)
	drawLine(pen, x-5 , y, x+5, y)
	drawLine(pen, x+5 , y, x+5, 0)
	drawLine(pen, x+5 , 0, x-5, 0)
	
#画多个柱体drawBar(pen)
#pen表示画笔
def drawBar(pen):
	for i in range(count):
		drawRectangle(pen, i+1, data[i])

#画统计图drawGraph(pen)
#pen表示画笔
def drawGraph(pen):
	#绘制x/y轴
	drawLine(pen, 0 ,0 ,360, 0)
	drawLine(pen, 0 ,0 ,0 ,300)
	#绘制x轴上的描述
	for i in range(count):
		print(str(words[i])+"\t"+str(i))
		i = i + 1
		#i += i
		drawText(pen, i*xScale-4, -20, words[i-1])
		drawText(pen, i*xScale-4, data[i-1]*yScale+10, str(data[i-1]))
	drawBar(pen)

#main()函数
#定义词频统计字典wordCounts，字典是引用类型，不用return返回
#读取英文文件，将文本统一大小写再遍历每一行
#词频排序
#关闭文件
#初始化画笔pen
#画统计图

def main():
	##读取英文文件，将文本统一大小写再遍历每一行
	file_name = input("请输入你要统计的文件名：")
	infile = open(file_name, 'r',encoding='UTF-8')
	wordCounts = {}
	for line in infile:
		processLine(line.lower(), wordCounts)
	pairs = list(wordCounts.items())
	items = [[x, y] for (y, x) in pairs]
	items.sort(reverse = True)
	for i in range(10):
		#print(items[i][1] + "\t" + str(items[i][0]))
		
		#words和data实际上是画图用到
		words.append(items[i][1])
		data.append(items[i][0])
	infile.close()
	print(words)
	print(data)
	##设置画笔参数
	turtle.title("词频统计图")
	#setup(width, height, start_x, start_y)
	turtle.setup(900, 750 ,0 ,0)
	pen = turtle.Turtle()
	pen.hideturtle()
	drawGraph(pen)
if __name__ == "__main__":
	main()
