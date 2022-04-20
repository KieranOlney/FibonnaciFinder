def main():
    finish = False
    print("Welcome to the Fibonnaci & Tribonnaci number finder")
    while finish == False:
        print("If you would like to find a Fibonnaci number please enter 1, If you would like to find a Tribonnaci number please enter 2")
        userPick = int(input("Fibonnaci/Tribonnaci : "))
        if userPick == 1:
            fibNumberWanted = input("Please Enter the Number in the Sequence that you'd Like: ")
            fibList = genFibonnaci(fibNumberWanted)
            fibonnaciNumber = fibList[int(fibNumberWanted)-1]
            print("The Fibonnaci number at "+fibNumberWanted+"th in the sequence is: ",fibonnaciNumber)
            saveSequence("fibonnaciSequence.txt",fibList,fibNumberWanted)
            isFin = input("\nIf you would like to exit the program please type 'EXIT' :")
            if isFin.upper() == "EXIT":
                finish = True

        elif userPick == 2:
            tribSig = []
            tribSigAdd = int(input("Please enter the First number of the Tribonnaci Signature : "))
            tribSig.append(tribSigAdd)
            tribSigAdd = int(input("Please enter the Second number of the Tribonnaci Signature : "))
            tribSig.append(tribSigAdd)
            tribSigAdd = int(input("Please enter the Third number of the Tribonnaci Signature : "))
            tribSig.append(tribSigAdd)
            tribNumberWanted = int(input("Please Enter the Number in this Sequence that you'd Like: "))
            tribList = genTribonnaci(tribSig,tribNumberWanted)
            tribNumber = tribList[int(tribNumberWanted)-1]
            print("The Tribonnaci number at "+str(tribNumberWanted)+"th in the sequence is: ",tribNumber)
            print(tribList)
            saveSequence("tribonnaciSequence.txt",tribList,tribNumberWanted)
            isFin = input("\nIf you would like to exit the program please type 'EXIT' :")
            if isFin.upper() == "EXIT":
                finish = True     
        else: print("Sorry I did not recognise that, Please input your selection again.")
        
    return

def genFibonnaci(length):
    fibnumbers = [0,1]
    for i in range(int(length)):
        sum = fibnumbers[i] + fibnumbers[i+1]
        fibnumbers.append(sum) 
    return fibnumbers

def genTribonnaci(signature, length):
    tribNumbers = []
    if len(signature) != 3:
        print(len(signature))
        print("sig length too short")
        return tribNumbers
    if signature == [0,0,0]:
        print("signature invalid")
        return tribNumbers
    if int(length) <= 0:
        print("length invalid")
        return tribNumbers
    tribNumbers = signature
    for i in range(length):
        sum = tribNumbers[i] + tribNumbers [i+1] + tribNumbers[i+2]
        tribNumbers.append(sum)
    return tribNumbers

def saveSequence(fileName,sequence,numberChosen):
    saveFile = open(fileName,"w")
    saveFile.write(str(sequence)+"|"+str(numberChosen))
    saveFile.close()
    return 

main()