import json

data = json.load(open('sample-data.json'))

print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
for i in data['imdata']:
    print(i['l1PhysIf']['attributes']['dn'], end = ' ' * (50 - len(i['l1PhysIf']['attributes']['dn']) + 1))
    print(i['l1PhysIf']['attributes']['descr'], end = ' ' * (20 - len(i['l1PhysIf']['attributes']['descr']) + 1))
    print(i['l1PhysIf']['attributes']['speed'], end = ' ' * (6 - len(i['l1PhysIf']['attributes']['speed']) + 4))
    print(i['l1PhysIf']['attributes']['mtu'], end = ' ' * (6 - len(i['l1PhysIf']['attributes']['mtu'])))
    print()