def pleaseConform(caps):
    start = forward = backward = 0 
    intervals = []
    for i in range(1, len(caps)):
        if caps[start] != caps[1]:
            intervals.append(start, i-1, caps[start]) 
            if caps[start] == 'f':
                forward += 1
            else:
                backward += 1
            start = i 
    intervals.append((start, len(caps)-1, caps[start]))
    if caps[start] == 'f':
        forward += 1 
    else:
        backward += 1 
    if forward < backward:
        flip = 'f'
    else: 
        flip = 'b'
    for t in intervals:
        if t[2] == flip:
            print('People in positions', t[0], 'through', t[1], 'flip your caps!')


