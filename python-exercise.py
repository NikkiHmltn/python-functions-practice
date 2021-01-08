def tripler(array):
    result = []
    for i in range(len(array)):
        num = array[i]
        result.append(num * 3)

    print(result)

tripler([2,3,4])

def odd_range(end):
    arr = []
    for i in list(range(end)):
        if i % 2 != 0:
            arr.append(i)
    print(arr)

odd_range(10)

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
             print(False)
        else:
            print(True)

is_prime(10)

def cat_builder(name, color, toys): 
  cat = {
    "name": name,
    "color": color,
    "toys": toys
  } 
  print(cat) 

cat_builder("pookey", "black", "catnip ball")

def valuePair(obj1, obj2, key):
    val1 = {obj1:key}
    val2 = {obj2:key}
    arr = [val1, val2]
    print(arr)

valuePair("lime", "lemon", "fruit")


obj1 = {"company":"General Assembly"}

def does_key_exist(obj, key):
    if key in obj.keys():
      return True
    else: 
        return False

print(does_key_exist(obj1, "name"))


ppl = [
  {"name": 'Khalid Robinson', "age": 22},
  {"name": 'Ariel Winter', "age": 20},
  {"name": 'Post Malone', "age": 25},
  {"name": 'Willow Smith', "age": 17}
 ]

def adults(people):
   names = []
   for i in people:
        person = i
        if person["age"] >= 18: 
            names.append(person["name"])
            print(names)
    

adults(ppl)

