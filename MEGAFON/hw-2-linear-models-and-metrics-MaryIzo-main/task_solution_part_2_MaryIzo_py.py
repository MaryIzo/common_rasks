import numpy as np

file = np.loadtxt('HW2_labels.txt', delimiter = ',')
y_predict, y_true = file[:,:2], file[:,-1]
print(y_predict.shape, y_true.shape)


def accuracy_score(y_true, y_predict, percent=None):
    P_0 = np.hstack(y_predict[:, :1].copy())  # Если вероятность принадлежать 0 < 0.05 относим к единице
    P_1 = np.hstack(y_predict[:, 1:].copy())  # Если вероятность принадлежать 1 > 0.5 относим к единице

    if (percent == None):
        alpha = 0.5  # считаем порог вероятности, если percent = 0
    else:
        N = int((percent * len(P_0)) / 100)  # считаем чему равен в количестве такой процент топа

        alpha = sorted(P_0, reverse=True)[N - 1:N][0]  # Как в лекции рассказали, сортируем по вероятности,
        # выбираем топ percent, и находим порог как самую маленькую в-ть в топе

    # print(alpha)
    y = (P_0 < alpha) * 1  # переделываем в единички и нули y_predict с учетом порога

    tptn_sum = (((y - y_true) == 0) * 1).sum()  # tp+tn

    acc = tptn_sum / len(y_true)

    return acc


def precision_score(y_true, y_predict, percent=None):
    P_0 = np.hstack(y_predict[:, :1].copy())  # Если вероятность принадлежать 0 < 0.05 относим к единице
    P_1 = np.hstack(y_predict[:, 1:].copy())  # Если вероятность принадлежать 1 > 0.5 относим к единице

    if (percent == None):
        alpha = 0.5  # считаем порог вероятности, если percent = 0
    else:
        N = int((percent * len(P_0)) / 100)  # считаем чему равен в количестве такой процент топа

        alpha = sorted(P_0, reverse=True)[N - 1:N][0]  # Как в лекции рассказали, сортируем по вероятности,
        # выбираем топ percent, и находим порог как самую маленькую в-ть в топе

    # print(alpha)
    y = (P_0 < alpha) * 1  # переделываем в единички и нули y_predict с учетом порога

    tp = ((((y_0 - y_true) == 0) * (y_0 == 1)) * 1).sum()
    fp = ((((y_0 - y_true) != 0) * (y_0 == 1)) * 1).sum()
    prec = tp / (tp + fp)

    return prec


def recall_score(y_true, y_predict, percent=None):
    P_0 = np.hstack(y_predict[:, :1].copy())  # Если вероятность принадлежать 0 < 0.05 относим к единице
    P_1 = np.hstack(y_predict[:, 1:].copy())  # Если вероятность принадлежать 1 > 0.5 относим к единице

    if (percent == None):
        alpha = 0.5  # считаем порог вероятности, если percent = 0
    else:
        N = int((percent * len(P_0)) / 100)  # считаем чему равен в количестве такой процент топа

        alpha = sorted(P_0, reverse=True)[N - 1:N][0]  # Как в лекции рассказали, сортируем по вероятности,
        # выбираем топ percent, и находим порог как самую маленькую в-ть в топе

    # print(alpha)
    y = (P_0 < alpha) * 1  # переделываем в единички и нули y_predict с учетом порога

    tp = ((((y_0 - y_true) == 0) * (y_0 == 1)) * 1).sum()
    fn = ((((y_0 - y_true) != 0) * (y_0 == 0)) * 1).sum()
    rec = tp / (tp + fn)

    return rec


def lift_score(y_true, y_predict, percent=None):
    P_0 = np.hstack(y_predict[:, :1].copy())  # Если вероятность принадлежать 0 < 0.05 относим к единице
    P_1 = np.hstack(y_predict[:, 1:].copy())  # Если вероятность принадлежать 1 > 0.5 относим к единице

    if (percent == None):
        alpha = 0.5  # считаем порог вероятности, если percent = 0
    else:
        N = int((percent * len(P_0)) / 100)  # считаем чему равен в количестве такой процент топа

        alpha = sorted(P_0, reverse=True)[N - 1:N][0]  # Как в лекции рассказали, сортируем по вероятности,
        # выбираем топ percent, и находим порог как самую маленькую в-ть в топе

    # print(alpha)
    y = (P_0 < alpha) * 1  # переделываем в единички и нули y_predict с учетом порога

    tp = ((((y_0 - y_true) == 0) * (y_0 == 1)) * 1).sum()
    # tn = ((((y_0-y_true)==0)*(y_0==0))*1).sum()
    fp = ((((y_0 - y_true) != 0) * (y_0 == 1)) * 1).sum()
    fn = ((((y_0 - y_true) != 0) * (y_0 == 0)) * 1).sum()

    prec = tp / (tp + fp)
    lift = prec / ((tp + fn) / len(y_true))

    return lift


def f1_score(y_true, y_predict, percent=None):
    P_0 = np.hstack(y_predict[:, :1].copy())  # Если вероятность принадлежать 0 < 0.05 относим к единице
    P_1 = np.hstack(y_predict[:, 1:].copy())  # Если вероятность принадлежать 1 > 0.5 относим к единице

    if (percent == None):
        alpha = 0.5  # считаем порог вероятности, если percent = 0
    else:
        N = int((percent * len(P_0)) / 100)  # считаем чему равен в количестве такой процент топа

        alpha = sorted(P_0, reverse=True)[N - 1:N][0]  # Как в лекции рассказали, сортируем по вероятности,
        # выбираем топ percent, и находим порог как самую маленькую в-ть в топе

    # print(alpha)
    y = (P_0 < alpha) * 1  # переделываем в единички и нули y_predict с учетом порога

    tp = ((((y_0 - y_true) == 0) * (y_0 == 1)) * 1).sum()
    tn = ((((y_0 - y_true) == 0) * (y_0 == 0)) * 1).sum()
    fp = ((((y_0 - y_true) != 0) * (y_0 == 1)) * 1).sum()
    fn = ((((y_0 - y_true) != 0) * (y_0 == 0)) * 1).sum()

    prec = tp / (tp + fp)
    rec = tp / (tp + fn)

    f1 = 2 * ((prec * rec) / (prec + rec))

    return f1


accuracy_score(y_true, y_predict, percent=90)
precision_score(y_true, y_predict, percent=10)
recall_score(y_true, y_predict, percent=None)
lift_score(y_true, y_predict, percent=10)
f1_score(y_true, y_predict, percent=None)