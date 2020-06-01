
class CustomException(Exception): #defining our own custom exceptions which will be an instance of Exception class
  pass

class Connection:
  def __init__(self, name):
   self.name = name
  
  def connect(self, data):
   print(data,'connecting...')
   #raise RuntimeError
   raise CustomException
  
  def close(self):
   print('Connection closed!')

def division(x, y):
  try:
    connection = Connection('Utkarsh Tiwari')
    connection.connect('Utkarsh')
    result = x/y
  except ZeroDivisionError:
    print('A number cannot be divided by zero')

  except AttributeError:
    print(AttributeError)
    print('Attribute is not defined')

  except RuntimeError:
    print('A runtime error has occured!')

  except CustomException:
    print('Custom Exception occured!')

  else:
    print('Division result:', result) 
    print('This part runs if no exception found!')

  finally:
    connection.close()
    raise BaseException #We can raise the last logged exception raised by just stating 'raise'

division(4, 0)
