def probabilidades(fonte, alfabeto):
    prob = {}
    for letra in alfabeto:
        prob.update({letra: 1})
    for elemento in fonte:
        prob[elemento] += 1

    return prob


def shannon_fano(dict):
    def shannon_fano_rec(pair, dict):
        if (len(pair[0]) > 1):
            pair[0] = shannon_fano_rec(split(pair[0], dict), dict)
        if (len(pair[1]) > 1):
            pair[1] = shannon_fano_rec(split(pair[1], dict), dict)

        return [pair[0], pair[1]]

    ordered_keys = sorted(dict, key=dict.get, reverse=True)
    result_array = shannon_fano_rec(split(ordered_keys, dict), dict)
    result = decodeArray(result_array)
    return result


def split(ordered_keys, dict):
    result = []
    right_sum = sum(list(map(lambda x: dict[x], ordered_keys)))
    left_sum = 0

    while right_sum - left_sum > 0:
        last_diff = right_sum - left_sum
        first_key = ordered_keys[0]
        right_sum -= dict[first_key]
        left_sum += dict[first_key]
        if right_sum - left_sum > 0:
            ordered_keys.pop(0)
            result.append(first_key)
        else:
            if abs(last_diff) > abs(right_sum - left_sum):
                ordered_keys.pop(0)
                result.append(first_key)

    return [result, ordered_keys]


def decodeArray(arr):
    result = {}

    def decodeArrayRec(arr, num):
        if (len(arr[0]) == 1):
            result[arr[0][0]] = num + '0'
        else:
            decodeArrayRec(arr[0], num + '0')

        if (len(arr[1]) == 1):
            result[arr[1][0]] = num + '1'
        else:
            decodeArrayRec(arr[1], num + '1')

    decodeArrayRec(arr, '')
    return result
