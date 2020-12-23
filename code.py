def job_sequencing():
    # given = [[job, profit, deadline]]
    given = [['J3', 20, 2], ['J1', 60, 3], ['J2', 100, 1],  ['J4', 40, 2], ['J5', 20, 1]]
    n_inc_order = sorted(given, key= lambda x: x[1], reverse=True)

    job_list = []

    i = 0
    for item in n_inc_order:
        if i >= item[2]: # testing with deadline
            for j in range(i, 0, -1):
                if job_list[j-1][2] <= j:
                    continue
                else:
                    if j <= item[2]:
                        job_list.insert(j-1, item)
                        i += 1
                    break
        else:
            job_list.append(item)
            i += 1
    return job_list
