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
          figure1=str(self.figure*1.00+273.15)
          form1='K'
          figure2=str(self.figure*9/5+32.00)
          form2='F'
          print(form1+"="+figure1)
          print(form2+"="+figure2)
