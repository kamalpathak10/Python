#Reference https://sourcemaking.com/design_patterns/strategy/python/1

class Strategy:
    def getModel(self):
        pass

    def predict(self, model, data):
        pass


class Algo1(Strategy):
    def getModel(self):
        model = "Alog1_model"
        return model

    def predict(self, model, data):
        return model + ":" + data + ":Prediction"


class Algo2(Strategy):
    def getModel(self):
        model = "Alog2_model"
        return model

    def predict(self, model, data):
        return model + ":" + data + ":Prediction"


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def buildModel(self):
        return self._strategy.getModel()

    def predictModel(self, model, data):
        return self._strategy.predict(model, data)


myData = "This is my Data"
strategyObj1 = Algo1()
contextObj1 = Context(strategyObj1)
model1 = contextObj1.buildModel()
print(contextObj1.predictModel(model1, myData))


strategyObj2 = Algo2()
contextObj2 = Context(strategyObj2)
model2 = contextObj2.buildModel()
print(contextObj2.predictModel(model2, myData))

