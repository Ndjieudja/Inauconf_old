password = "(70Ȇ105ŀ102\x1A97ʷ101Q97\x1F50\x1B48F50\x1449"

key = list()
contener = str()

for el in range(len(password)):
    try:
        if type(password[el]) ==  type(password[el+1]) and el < len(password):
            contener =  contener + "{}".format(password[el+1])
        else:
            keys.append(contener)
        
    except Exception as error:
         continue

print(key, contener)