from mlops_projet.data.load import load_bank_data

def test_shape():
    df = load_bank_data()
    assert "y" in df.columns

def test_target_column():
    df = load_bank_data()
    assert "y" in df.columns