import json

with open("sample-data.json", "r") as file:
    res = json.load(file)

print("Interface Status")
print("="*70)
print(f"{"DN":<43} {"Description":<13} {"Speed":<8} {"MTU":<7}")

for key in res['imdata']:
    a = key['l1PhysIf']['attributes']
    dn = a['dn']
    descr = a['descr']
    speed = a['speed']
    mtu = a['mtu']
    print(f"{dn:<25} {descr:<15} {speed:<6} {mtu:<3}")