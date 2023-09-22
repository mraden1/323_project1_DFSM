class deterAutoMach:
    """Builds a deterministic auto machine"""

    def __init__(self):
        self.inpString = ''
        self.start_state = stateType()

    def createMachine(self, start_state):
        self.start_state = start_state

    def printResult(self):
        if self.start_state.getFinal():
            print('String Accepted')
        else:
            print('String not accepted')

    def setString(self):
        inp = input(
            "Enter a string of characters from the alphabet terminating with '$'")
        self.inpString = inp

    def runMachine(self):
        self.setString()
        self.my_keys = list(self.start_state.trans.keys())

        for item in self.inpString:
            if self.checkForEnd(item):
                return self.printResult()
            elif self.checkForValid(item):
                self.start_state = self.start_state.getTrans(item)
            else:
                return self.printInvalidInput()

    def checkForEnd(self, endItem):
        return endItem == '$'

    def checkForValid(self, str_element):
        if self.my_keys.count(str_element) > 0:
                return True
        else:
                return False

    def printInvalidInput(self):
        print('The input had invalid values not part of language')


class stateType:
        def __init__(self):
                self.trans = {}
                self.isFinal = False

        def setTrans(self, trans):
                self.trans = trans

        def setFinal(self, myBool):
                self.isFinal = myBool
                
        def getFinal(self):
                return self.isFinal

        def getTrans(self, str_let):
                return self.trans[str_let]

        def statePrint(self):
                print(self, self.trans, self.isFinal)


q0 = stateType()
q1 = stateType()
q2 = stateType()
q3 = stateType()
q4 = stateType()

q0.setTrans({'a': q1, 'b': q4})
q1.setTrans({'a': q2, 'b': q1})
q2.setTrans({'a': q3, 'b': q2})
q2.setFinal(True)
q3.setTrans({'a': q4, 'b': q3})
q3.setFinal(True)
q4.setTrans({'a': q4, 'b': q4})

D = deterAutoMach()
D.createMachine(q0)
D.runMachine()
