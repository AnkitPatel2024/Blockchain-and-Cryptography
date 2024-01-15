from zksk import Secret, DLRep
from zksk import utils
#from zksk import composition

def ZK_equality(G,H):

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    r1 = Secret(utils.get_random_num(bits=128))
    m = Secret(utils.get_random_num(bits=1))

    C1 = r1.value*G
    C2 = r1.value*H + m.value*G

    r2 = Secret(utils.get_random_num(bits=128))
    D1 = r2.value*G
    D2 = r2.value*H + m.value*G

    #Generate a NIZK proving equality of the plaintexts  
    
    #stmt1 = DLRep(D1, r2 * G) & DLRep(D2-G, r2 * H) & DLRep(C1, r1 * G) & DLRep(C2-G, r1 * H)
    #stmt2 = DLRep(C1, r1 * G) & DLRep(D1, r2 * G) & DLRep(C2-G, r1 * H) & DLRep(D2-G, r2 * H)
    #stmt3 = DLRep(C1, r1 * G) & DLRep(C2-m*G, r1 * H) & DLRep(D1, r2 * G) & DLRep(D2-m*G, r2 * H)
    stmt3 = DLRep(C1, r1*G) & DLRep(C2, r1*H+m*G) & DLRep(D1, r2*G) & DLRep(D2, r2*H+m*G)
    #print(stmt3)

    zk_proof = stmt3.prove() 
    

    #Return two ciphertexts and the proof
    return (C1,C2), (D1,D2), zk_proof


