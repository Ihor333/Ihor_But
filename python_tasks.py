#task 1
def filter_list(list_of_elem):
    list_of_elem = [i for i in list_of_elem if type(i) != str]
    return list_of_elem

#task 2
def first_non_repeating_letter(word):
    while len(word) != 0:
        letter = word[0]
        new_word = [i for i in word if i.lower() != letter.lower()]
        if len(new_word) == len(word)-1:
            return letter
        word = new_word
    return None

#task 3
def digital_root(n):
    res = 0
    while n > 0:
        digit = n % 10
        res = res + digit
        n = n // 10
    if(res>9):
        return digital_root(res)
    else:
        return res

# task 4
def pairs_number(arr, target):
    pairs_count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]+arr[j] == target and i != j:
                pairs_count += 1
    pairs_count /= 2
    return int(pairs_count)

#task 5
def party_list(str):
    str = str.split(';')
    res = []
    for i in str:
        i = i.upper().split(':')
        i[0], i[1] = i[1], i[0]
        res.append(i[0]+', '+i[1])
    res = sorted(res)
    str = ''
    for i in res:
        str += '('+i+'),'
        str = str.strip(',')
    return str

#task 6
def nextBigger(number):
    number_list = list(str(number))
    number_list.sort(reverse = True)
    bigger_number = int(''.join(number_list))
    if(bigger_number>number):
        return bigger_number
    else:
        return -1
#task 7
def ip_conventor(ip):
    ip = '{:032b}'.format(ip)
    ip = list(str(ip))
    total_res = ''
    for i in range (4):
        result = ''
        for j in range (i*8,i*8+8):
             result+=ip[j]
        total_res+=str(int(result,base=2))+'.'
    total_res = total_res.strip('.')
    return total_res

print("Task results")
print("Task 1",
    "\nTest #1\nSTR: [1,2,'a','b']","\nACT:", filter_list([1,2,'a','b']), "\nEXP: [1,2]",
    "\n\nTest #2\nSTR: [1,'a','b',0,15]","\nACT:", filter_list([1,'a','b',0,15]), "\nEXP: [1,0,15]",
    "\n\nTest #3\nSTR: [1,2,'aasf','1','123',123]","\nACT:", filter_list([1,2,'aasf','1','123',123]), "\nEXP: [1,2,123]")
print("__________________________________________")
print("Task 2",
      "\nTest #1\nSTR: stress","\nACT:",first_non_repeating_letter('stress'),"\nEXP: t",
      "\n\nTest #2\nSTR: sTreSS","\nACT:",first_non_repeating_letter('sTreSS'),"\nEXP: T",
      "\n\nTest #3\nSTR: SsTt","\nACT:",first_non_repeating_letter('SsTt'),"\nEXP: None")
print("__________________________________________")
print("Task 3",
      "\nTest #1\nSTR: 16","\nACT:",digital_root(16),"\nEXP: 7",
      "\n\nTest #2\nSTR: 942","\nACT:",digital_root(942),"\nEXP: 6",
      "\n\nTest #3\nSTR: 132189","\nACT:",digital_root(493193),"\nEXP: 2")
print("__________________________________________")
print("Task 4",
      "\nTest #1\nSTR: [1, 3, 6, 2, 2, 0, 4, 5], 5","\nACT:",pairs_number([1, 3, 6, 2, 2, 0, 4, 5], 5),"\nEXP: 4",
      "\n\nTest #2\nSTR: [1, 3, 6, 2, 2, 0, 4, 5], 4","\nACT:",pairs_number([1, 3, 6, 2, 2, 0, 4, 5], 4),"\nEXP: 3")
print("__________________________________________")
print("Task 5",
      "\nTest #1\nSTR: Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill",
      "\nACT:", party_list('Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill'),
      "\nEXP: (CORWILL, ALFRED)(CORWILL, FIRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)")

print("__________________________________________")
print("Task 6",
      "\nTest #1\nSTR: 1234","\nACT:",nextBigger(1234),"\nEXP: 4321",
      "\n\nTest #2\nSTR: 2071","\nACT:", nextBigger(2071),"\nEXP: 7210",
      "\n\nTest #3\nSTR: 9", "\nACT:", nextBigger(9), "\nEXP: -1"
      "\n\nTest #4\nSTR: 211", "\nACT:", nextBigger(211), "\nEXP: -1")
print("__________________________________________")
print("Task 7",
      "\nTest #1\nSTR: 2149583361","\nACT:", ip_conventor(2149583361),"\nEXP: 128.32.10.1",
      "\n\nTest #2\nSTR: 3421","\nACT:",ip_conventor(3421),"\nEXP: 0.0.13.93",
      "\n\nTest #3\nSTR: 0","\nACT:",ip_conventor(0),"\nEXP: 0.0.0.0")