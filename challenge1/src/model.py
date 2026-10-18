from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline

def get_pipeline():
    clf = MLPClassifier(random_state=42)
    return Pipeline([('classifier',clf)])