
def is_feasible(i, item, ordered_job):
    idx = -1
    for j in range(i, 0, -1):
        # print("if", i, j, item[2], i - 1)
        if ordered_job[j-1][2] <= j:
            continue
        else:
            # print("here", j, item[2])
            if j <= item[2]:
                idx = j
            break
    return idx


def job_sequencing(jobs=None):
    """
    jobs is provided as a list of list as
    [[job, profit, deadline]]
    :param jobs:
    :return:
    """
    if not jobs:
        jobs = [['J1', 60, 2], ['J2', 100, 1], ['J3', 20, 3], ['J4', 40, 5], ['J5', 20, 4]]
        # jobs = [['J3', 20, 2], ['J1', 60, 3], ['J2', 100, 1],  ['J4', 40, 2], ['J5', 20, 1]]
    n_inc_order = sorted(jobs, key = lambda x: x[1], reverse=True)
    ordered_job = []
    i = 0
    for it, item in enumerate(n_inc_order):
        if i >= item[2]:
            idx = is_feasible(i, item, ordered_job)
            if idx >= 0:
                ordered_job.insert(idx-1, item)
                i += 1
        else:
            ordered_job.append(item)
            i += 1
    return ordered_job
