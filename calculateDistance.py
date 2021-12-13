import Levenshtein as lev

def calculateDistance(i, threadAddressCount, addressCount, addresses, data):
    start = i * threadAddressCount
    for n in range(threadAddressCount):
        if (start + n < addressCount):
            for x in range(addressCount):
                ratio = lev.ratio(addresses[start + n].lower(), addresses[x].lower())
                if (ratio > 0.6):
                    data[(start + n, x)] = ratio
