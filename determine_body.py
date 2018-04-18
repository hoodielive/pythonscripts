scenario = ['face', 'face', 'physique', 'physique', 'face', 'physique', 'face'] 


determinebody = []

def figureTheBody(scenario):
    start = face = physique = 0
    for figure in range(1, len(scenario)): 
        if scenario[start] != scenario[figure]:
            determinebody.append((start, figure - 1, scenario[start])) 
            if scenario[start] == 'face':
                face += 1
            else:
                physique += 1
            start = figure 
    determinebody.append((start, len(scenario) - 1, scenario[start])) 
    if scenario[start] == 'face':
        face += 1 
    else:
        physique += 1

    if face < physique:
        flip = 'face'
    else:
        flip = 'physique'
    for t in determinebody:
        if t[2] == flip:
            print('Girls in positions', t[0], 'through', 'figures in', t[1])

figureTheBody(scenario)
    



