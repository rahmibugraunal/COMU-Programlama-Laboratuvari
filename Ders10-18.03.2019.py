# Burglar Game

"""        value    weight    value/weight
clock      175     10           17.5
painting    90      9           10
radio       20      4            5
vase        50      2           25
book        10      1           10
computer   200     20           10  """


class item(object):
  def __init__(self,n,v,w):
    self.name=n
    self.value=v
    self.weight=w

def steal(capacity):
  item1=item("Vase",50,2)
  item2=item('Table',175,10)
  item3=item("Television",200,20)
  item4=item("Chair",90,9)
  item5=item("Book",10,1)
  item6=item("Radio",20,4)
  items=[item1,item2,item3,item4,item5,item6]
  weight=0
  value=0
  maxv=0
  array=[]
  array2=[]
  for i in range(0,len(items)):
    if(items[i].weight<=capacity):
      value=items[i].value
      weight=items[i].weight
      array.append(items[i].name)
    for j in range(i+1,len(items)):
      if(weight+items[j].weight<=capacity):
        value+=items[j].value
        weight+=items[j].weight
        array.append(items[j].name)
    if(value>maxv):
      maxv=value
      array2=array.copy()
    weight=0
    value=0
    array.clear()
  return array2,maxv

bag=steal(20)
print(bag)
