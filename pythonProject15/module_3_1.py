
calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    stringup=string.upper()
    stringlow=string.lower()
    print ('(',len(string),',','"', stringup, '"',',','"', stringlow,'"',')')
    count_calls()
def is_contains(string, list_to_search):
    string = string.lower()
    for x in range(len(list_to_search)):
        list_to_search[x] = list_to_search[x].lower()
        x += 1
    i=0
    z=0
    for z in range(len(list_to_search)):
        if string == list_to_search[z]:
            i += 1
        z += 1
    if i>=1:
        print ('True')
    else:
        print ('False')
    count_calls()




string_info("Capybara")
string_info('Armageddon')
is_contains('Urban', ['ban','BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
