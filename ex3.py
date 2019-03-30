#先创造一个类，在主函数中调用，就像string一样
#类本身要有构造函数和fun函数用来转换格式
class TempConver:

  figure=0
  form='C'

  def __init__(self,figure,form):
      self.figure=figure
      self.form=form

  def change(self):
      if self.form=='C':
          figureK=str(self.figure*1.00+273.15)
          form1='K'
          figureF=str(self.figure*9/5+32.00)
          form2='F'
          print(form1+"="+figureK)
          print(form2+"="+figureF)
      elif self.form=='F':
          figureC=str((self.figure-32)*5/9)
          figureC=float(figureC)
          figureK=str(figureC+273.15)
          print('C'+"="+figureC)
          print('K'+"="+figureK)
      else:
          figureC=str(self.figure-273.15)
          figureF=str((figureC-32)*5/9)
          print('C'+"="+figureC)
          print('F'+"="+figureF)
