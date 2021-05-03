import numpy as np
from tabulate import tabulate
from distribution import distribution_fun
from characteristics import characteristic, get_characterisrics_template

sample_size = [10, 100, 1000]
loc, scale = 0.0, 1.0
EXP_NUM = 1000


def DE(data):
    return np.var(data), np.mean(data)


def calculate_mean_value(data):
    answer = {}
    value = {}
    for el in characteristic:
        value['d'], value['e'] = DE(data[el])
        answer[el] = value.copy()
    return answer


def calculation_exp():
    sample_res = {}
    answer = {}
    result = {}
    for dist in distribution_fun:
        for size in sample_size:
            result.clear()
            result = get_characterisrics_template()
            for i in range(EXP_NUM):
                sample = distribution_fun[dist](size)
                for el in characteristic:
                    result[el].append(characteristic[el](sample))
            sample_res[str(size)] = calculate_mean_value(result)
        answer[dist] = sample_res.copy()
    return answer


def show_results(dist, name):
    res_d = []
    res_e = []
    res_begin = []
    res_end = []
    rows = []
    headers = [name, "x_", "med(x)", "z_R", "z_Q", "z_tr"]
    for size in dist:
        res_d.clear()
        res_e.clear()
        res_begin.clear()
        res_end.clear()
        res_e.append(" E(z) =  " + str(size))
        res_d.append(" D(z) =  " + str(size))
        res_begin.append("E(z)-\sqrt(D(z))")
        res_end.append("E(z)+\sqrt(D(z))")
        for ch in dist[size]:
            res_d.append(np.around((dist[size])[ch]['d'], decimals=4))
            res_e.append(np.around((dist[size])[ch]['e'], decimals=4))
            res_begin.append(np.around((dist[size])[ch]['e'] - np.sqrt((dist[size])[ch]['d']), decimals=4))
            res_end.append(np.around((dist[size])[ch]['e'] + np.sqrt((dist[size])[ch]['d']), decimals=4))
        rows.append(res_e.copy())
        rows.append(res_d.copy())
        rows.append(res_begin.copy())
        rows.append(res_end.copy())
        rows.append(["", "", "", "", "", ""])
    print(tabulate(rows, headers, tablefmt="latex"))


if __name__ == '__main__':
    answer = calculation_exp()
    for key in distribution_fun:
        show_results(answer[key], key)
        print("\n")
