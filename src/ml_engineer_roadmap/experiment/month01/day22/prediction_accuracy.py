import numpy as np

def prediction_accuracy(actual, predicted):
    if actual is None or predicted is None:
        return None
        
    if len(actual) != len(predicted):
        raise ValueError("长度不一致")
        
    if len(actual) == 0:
        return None
        
    actual_arr = np.array(actual)
    predicted_arr = np.array(predicted)
    
    result = actual_arr == predicted_arr
    correct_rate = result.sum() / len(actual_arr)
    
    return correct_rate