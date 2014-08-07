import sys
from rat import rat


def decrypt(fcyphertext,fsample):
    
    c = open(fcyphertext,'r')
    s = open(fsample, 'r')
    
    cyphertext = c.read()
    sample = s.read()
    
    cyphertext_freq = dict()
    sample_freq = dict()
    
    alphabet = "qwertyuiopasdfghjklmnbvcxz"
    
    for a in alphabet:
    	cyphertext_freq[a] = 0
    	sample_freq[a] = 0
        
        
    for letter in cyphertext:
        if (97 <= ord(letter.lower()) < 123):
            cyphertext_freq[letter.lower()] += 1
            
    for letter in sample:
        if (97 <= ord(letter.lower()) < 123):
            sample_freq[letter.lower()] += 1

    c_max = {
        "value" : 0,
        "key" : 'a'
    }
    s_max = {
        "value" : 0,
        "key" : None
    }
    s_max2 = {
        "value" : 0,
        "key" : None
    } 	
    s_max3 = {
        "value" : 0,
        "key" : None
    } 

    for k in cyphertext_freq:
        if(c_max["value"] < cyphertext_freq[k]):
            c_max["value"] = cyphertext_freq[k]
            c_max["key"] = k


    for k in sample_freq:
        if(s_max["value"] < sample_freq[k]):
            s_max3["value"] = s_max2["value"]
            s_max2["value"] = s_max["value"]
            s_max["value"] = sample_freq[k]
            s_max3["key"] = s_max2["key"]
            s_max2["key"] = s_max["key"]
            s_max["key"] = k
        elif(s_max2["value"] < sample_freq[k]):
            s_max3["value"] = s_max2["value"]
            s_max2["value"] = sample_freq[k]
            s_max3["key"] = s_max2["key"]
            s_max2["key"] = k
        elif(s_max3["value"] < sample_freq[k]):
            s_max3["value"] = sample_freq[k]
            s_max3["key"] = k


    s_max_keys = [s_max["key"],s_max2["key"],s_max3["key"]]
    for a in s_max_keys:
        if(ord(a) > ord(c_max["key"])):
            plain = rat(fcyphertext, ord(a) - ord(c_max["key"]))
        else:
            plain = rat(fcyphertext, (ord(a) - ord(c_max["key"])+26))
        output = open(r'attempt_'+a+'.txt', 'w')
        output.write(plain)
        output.close()
        

decrypt(sys.argv[1], sys.argv[2])


