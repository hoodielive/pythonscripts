#!/usr/bin/env python3 

import numpy

idx_to_token = list(set(tokens))

token_to_idx = { token: idx for idx, token in enumerate(idx_to_token) } 

one_hot = lambda token: [ 1 if i == token_to_idx[token] else 0 for i in range(len(idx_to_token)) ] 

print(encoded = np.asarray([one_hot(token) for token in tokens])) 
