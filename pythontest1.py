for i in range(10):
    if i % 2 == 0:
        print(i)
        continue
    i += 1
    print(i)
member = ["王\"磊\"", "牛逼", "六'六'六"]
for e in member:
    print(e, end=' ')
member.remove("牛逼")
for e in member:
    print(e, end=' ')
member.append("牛逼")
for e in member:
    print(e, end=' ')
del member[2]
for e in member:
    print(e, end=' ')
member.extend(["厉害厉害", "帅气帅气"])
for e in member:
    print(e, end=' ')
member.insert(0, "我要说")
for e in member:
    print(e, end=' ')
member.pop()
for e in member:
    print(e, end=' ')
