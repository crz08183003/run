#调用TempConvert类
from ex3 import TempConver
TempForm=input("请选择温度格式（'C'摄氏度，'F'华氏度，'K'开尔文）：")
Figure=input("请输入数值：")
Figure=float(Figure)
temp=TempConver(Figure,TempForm)
temp.change()
