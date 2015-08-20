import hashlib

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return m.digest()

def to_binary(s):
    nested = [map(int, "{0:08b}".format(ord(x))) for x in s]
    return [i for j in nested for i in j]

def to_string(s):
    counter = 0
    val     = 0
    l       = len(s)
    ret     = list()
    
    while counter < l:
        val <<= 1
        val |= s[counter]
        
        if counter % 8 == 7:
            ret.append(chr(val))
            val = 0
            
        counter += 1
        
    return "".join(ret)
        
def op_inv(xx):
    return [1 - x for x in xx]

def op_lrot(xx):
    return xx[1:] + [xx[0]]

def op_rrot(xx):
    return [xx[-1]] + xx[:-1]

letters = [chr(x) for x in xrange(ord("A"), ord("Z") + 1)]
hashes  = dict()
for letter in letters:
    hashes[letter] = to_binary(md5(letter))

# print hashes
