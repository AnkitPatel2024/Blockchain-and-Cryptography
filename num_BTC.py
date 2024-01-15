import math

def num_BTC(b):

    if b <= 210000:
        bitcoins = float(b *50)
        return bitcoins

    else:
        bloc_rewarded = 0
        bloc_toberewarded = b -bloc_rewarded
        bloc_reward = 50
        bitcoins = 0

        while (bloc_toberewarded > 0) :
            if bloc_toberewarded > 210000 :
                bitcoins = float (bitcoins+  (bloc_reward * 210000))
                bloc_reward = bloc_reward *0.5
                bloc_toberewarded = bloc_toberewarded - 210000

            elif bloc_toberewarded < 210000:
                bitcoins = float(bitcoins+  (bloc_reward * bloc_toberewarded))
                bloc_toberewarded = 0

            elif bloc_toberewarded == 210000:
                bitcoins = float (bitcoins+  (bloc_reward * 210000))
                bloc_reward = bloc_reward *0.5
                bloc_toberewarded = bloc_toberewarded - 210000

    return bitcoins

#print(num_BTC(210000))
#print(num_BTC(420000))
