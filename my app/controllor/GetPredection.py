

def GetPredection (model, Input: list):

    resurt = {
                0 : 'Iris-setosa',
                1 : 'Iris-versicolor',
                2 : 'Iris-virginica',
    }

    predections = model.predict([Input])[0]

    return resurt[predections]