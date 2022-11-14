from functools import reduce
responses=['Welcome to smart Rocky  calculator','My name is Rocky','Thanks','sorry,I am not understand']
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
                pass
    return(l)
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1

def big(a,b):
    return a if a>b else b
def small(a,b):
    return a if a<b else b
def add(a,b):
    return a+b
  
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def end():
    print(responses[2])
    input('press enter key to exit')
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
def help():
    print('list of valid commands')
    for k  in operations:
        print(k)
    for k in commands:
        print(k)
operations={'PLUS':add,'ADD':add,'ADITION':add,'SUM':add,'MINUS':sub,'SUBTRACT':sub,'DIFFRENCE':sub,'SUB':sub,'PRODUCT':multiply,
            'MULTIPLICATION':multiply,'MULTIPLY':multiply,'MULTIPLE':multiply,'DIVIDE':division,'DIVISION':division,'LCM':lcm,'HCF':hcf,'BIG':big,
            'MAX':big,'GREATER':big,'SMALL':small,'LES':small,'MINIMUM':small}
commands={'NAME':myname,'END':end,'EXIT':end,'CLOSE':end,'HELP':help}
def main():
    print(responses[0])
    print(responses[1])
    while True:
        print()
        text=input('enter some text: ')
        for word in text.split(' '):
            if word.upper() in operations.keys():
                try:
                    r1=extract_numbers_from_text(text)
                    r=reduce(operations[word.upper()],r1)
                    print(r)
                except:
                    print('something is wrong please retry')
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
            
        else:
            sorry()
if __name__=='__main__':
    main()





















        
