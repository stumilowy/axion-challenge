import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from src.tools import get_clothes_mapping

def evaluate_model(pipeline, X_test, y_test, model_name="model"):
    y_pred = pipeline.predict(X_test)

    labels = np.unique(np.concatenate([np.asarray(y_test), y_pred]))
    clothes_mapping = get_clothes_mapping()
    names = [clothes_mapping[label] for label in labels]

    print(f"=== {model_name} ===")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, labels=labels, target_names=names))

    cm = confusion_matrix(y_test, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=names)
    disp.plot(cmap=plt.cm.Blues, xticks_rotation=45)
    plt.title(f"Confusion Matrix - {model_name}")
    plt.tight_layout()
    plt.show()
