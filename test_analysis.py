import pytest
from src.analysis.sales_predictor import SalesPredictor
from src.utils.data_loader import GameDataLoader

@pytest.fixture
def sample_data():
    loader = GameDataLoader()
    return loader.load_raw_data().sample(100)

def test_sales_predictor(sample_data):
    predictor = SalesPredictor(sample_data)
    X_train, X_test, y_train, y_test = predictor.prepare_data()
    model = predictor.train_model(X_train, y_train)
    
    assert hasattr(model, 'predict'), "Model should have predict method"
    assert len(X_test) > 0, "Test set should not be empty"
    
def test_data_loader(sample_data):
    assert 'Global_Sales' in sample_data.columns
    assert len(sample_data) > 0
