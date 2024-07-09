def num_buses_to_destination_v1(routes, source, target):
    """
    Initial intuitive solution
    leet code submit result -> Time Limit Exceeded
    """
    if source == target:
        return 0
    result = help_recursion(routes, source, target,1)
    if result:
        return result
    else:
        return -1


def help_recursion(routes, source, target, counter):
    source_list = []
    for i in range(len(routes)):
        if source in routes[i] and target in routes[i]:
            return counter
        if source in routes[i]:
            source_list.append(routes[i])
    results = []
    for i in source_list:
        new_routes = all_combination_from_source(i, routes)
        result = help_recursion(new_routes, source, target, counter + 1)
        if result is not None:
            results.append(result)
    if results:
        return min(results)
    else:
        return None


def all_combination_from_source(source, routes):
    new_comb = []
    no_change = routes.copy()
    no_change.remove(source)
    for i in routes:
        if set(i) & set(source) and i != source:
            new_comb.append(list(set(i + source)))
            j = i
            no_change.remove(j)
    return new_comb + no_change


routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source, target, counter = 15, 12, 1
print(num_buses_to_destination_v1(routes, source, target))
