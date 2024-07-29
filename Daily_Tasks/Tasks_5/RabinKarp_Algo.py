'''
    Rabin-Karp algorithm for pattern matching
'''
 
def rabinKarpAlgo(text, patt):
    textLen = len(text)
    pattLen = len(patt)
    prime = 101
    indices = []
    patternHash =  0
    for i in range(pattLen):
        patternHash = (patternHash * 100 + ord(patt[i])) %  prime
   
    for i in range(textLen - pattLen + 1):
        if i < (textLen - pattLen):
            subStrHash = 0
            for j in range(pattLen):
                subStrHash = (subStrHash * 100 + ord(text[i+j])) %  prime
 
        if patternHash == subStrHash and text[i:i+pattLen] == patt:
            indices.append(i)
 
    return indices      
           
 
if __name__ == '__main__':  # Corrected this line
    text = 'AAAABAAABAAAABAABA'
    pat = 'AAA'
    res = rabinKarpAlgo(text, pat)
    print(f'Pattern: {pat}\tIndices: {res}')
