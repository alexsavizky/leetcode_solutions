def count_visited_nodes_v1(edges):
    """
    Initial intuitive solution
    leet code submit result -> Time Limit Exceeded
    i assume because of O(E^2)
    """
    nodes_count = 0
    colors = ['w'] * len(edges)  # paint nodes in black if visited
    answer = [0] * len(edges)
    for i in range(len(edges)):  # O(E)
        j = i
        while colors[j] == 'w':  # O(E)
            nodes_count += 1
            colors[j] = 'b'
            j = edges[j]
        answer[i] = nodes_count
        colors = ['w'] * len(edges)
        nodes_count = 0
    # to sum up O(E^2)
    return answer


def count_visited_nodes_v2(edges):
    """
    second  solution
    because |E| = |V| -> there is no vortex with two children
    -> there is no 2 paths in circles -> the value of each node
    in given circle will all have the same c_v_n value
    now we solve this problem with this idea


    leet code submit result ->
    runtime - 1174ms beats 87.06%
    memory - 34.92 beats 89.41%

    """
    nodes_count = 0
    colors = ['w'] * len(edges)     # paint nodes in black if visited
    answer = [0] * len(edges)
    for i in range(len(edges)):     # O(E)
        if answer[i] == 0:          # ensure we don't visit nodes that we visited in the past
            j = i
            path = []
            while colors[j] == 'w':
                path.append(j)
                nodes_count += 1
                colors[j] = 'b'
                j = edges[j]

            # 3 option to get black node
            # first option - a perfect circle  1->2->3->1
            if j == path[0]:
                for k in path:  # O(E) but when we give values to nodes in the answer array we
                    # make sure not to visit them again
                    answer[k] = nodes_count

            # second option - collide with a known value
            elif answer[j] != 0:
                for k in path:  # O(E) but when we give values to nodes in the answer array we
                    # make sure not to visit them again
                    answer[k] = nodes_count + answer[j]
                    nodes_count -= 1

            # third option - inner circle
            else:
                inner_circle_count = 1
                temp_path = path
                circle = []
                temp_stack_value = temp_path.pop()
                circle.append(temp_stack_value)
                while j != temp_stack_value:
                    inner_circle_count += 1
                    temp_stack_value = temp_path.pop()
                    circle.append(temp_stack_value)
                for k in path:
                    if j == k:
                        break
                    answer[k] = nodes_count
                    nodes_count -= 1
                for k in circle:
                    answer[k] = inner_circle_count
            nodes_count = 0
    return answer


"""
test section
"""
edges = [8, 17, 14, 8, 14, 12, 16, 11, 4, 14, 19, 6, 8, 8, 2, 10, 2, 1, 1, 18]
expected = [5, 2, 2, 5, 3, 6, 4, 6, 4, 3, 5, 5, 5, 5, 2, 6, 3, 2, 3, 4]
if count_visited_nodes_v2(edges) == expected:
    print(True)
else:
    print(False)
