import numpy as np
import graphene
import joblib

model_score = joblib.load('../models/model_score.joblib')

class Prediction(graphene.ObjectType):
  predicionScore = graphene.Float()

class Query(graphene.ObjectType):
    scoreClient = graphene.List(Prediction, 
                                indSalario=graphene.Float(), 
                                indPrestamo=graphene.Float(), 
                                indFormacion=graphene.Float())

    def resolve_scoreClient(self, info, indSalario, indPrestamo, indFormacion):
        input_ = np.array([[indSalario, indPrestamo, indFormacion]])
        return [Prediction(predicionScore=model_score.predict(input_)[0])]

def score_prediction(indSalario, indPrestamo, indFormacion):
    schema = graphene.Schema(query=Query)
    query = """
    {
        scoreClient(indSalario: """+indSalario+""", indPrestamo: """+indPrestamo+""", indFormacion: """+indFormacion+"""){
            predicionScore
        }
    }
    """
    result_ = schema.execute(query)
    return result_