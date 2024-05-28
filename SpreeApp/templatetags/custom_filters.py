from django import template

import json

register = template.Library()

@register.filter(name="booltoint")
def booltoint(value,arg):
   
    if value==True or arg==True: 
        return 1
    else:
        return 0




@register.filter(name="matching")
def matching(value,arg):
   
    print(value,arg)



@register.filter(name='jsn')
def jsn(value):
    
    print(value)
    print(type(value))
    data   = json.loads(value)
    print(type(data))
    for i in data:
        print(i)
      
    print("_________________")
    return data
   