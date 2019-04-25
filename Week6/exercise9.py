import numpy as np

x = [26, 28, 30, 32]
y = [148, 164, 168, 183]

def predict(x):
    return 6*x + 10


def rmse(predict, ylabel):
    return np.sqrt(((predict-ylabel)**2).mean())

def rmse_val(predict_result, y):
    return rmse(np.array(predict_result), np.array(y))

predict_result = []
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print('input=%.f, output=%.f,prediction=%.f' % (x[i], y[i], predict(x[i])))

print('rmse최종값:'+str(rmse_val(predict_result, y)))