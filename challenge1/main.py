from src.data_loader import get_test_base_data
from src.data_loader import get_train_base_data
from src.data_loader import get_test_base_data_merged
from src.data_loader import get_train_base_data_merged
from src.model import get_pipeline
from src.evaluate import evaluate_model

if __name__ == '__main__':

    print("Inicjalizacja modeli...")
    pipline_base = get_pipeline()
    pipline_merged_types = get_pipeline()

    print("Ładowanie danych...")
    X_train, y_train = get_train_base_data()
    X_train_merged, y_train_merged = get_train_base_data_merged()
    X_test, y_test = get_test_base_data()
    X_test_merged, y_test_merged = get_test_base_data_merged()

    print("Trenowanie modeli")
    pipline_base.fit(X_train, y_train)
    pipline_merged_types.fit(X_train_merged, y_train_merged)

    print("Ewaluacja modeli")
    evaluate_model(pipline_base, X_test, y_test, "Base")
    evaluate_model(pipline_merged_types, X_test_merged, y_test_merged, "Merged types")
