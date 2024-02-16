def binpack(items, S):
    items.sort(reverse=True)
    bins = []
    filledBins = 0
    
    for item in items:
        filledUpToThis = True
        foundBucket = False
        if len(bins) %2 == 0 or len(bins) %5 == 0: 
            bins.sort(key=sum, reverse=True)
        for bin in range(filledBins, len(bins)):
            binSum = sum(bins[bin])
            if binSum == S and filledUpToThis:
                filledBins += 1
            elif binSum + item == S and filledUpToThis:
                filledBins += 1
            else:
                filledUpToThis == False
            if binSum + item <= S:
                bins[bin].append(item)
                foundBucket = True
                break
    
        if not foundBucket:
            bin = [item]
            bins.append(bin)
    return bins
        



if __name__ == "__main__":

    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    print("One feasible solution:")
    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")

    # A possible output:
    #   bin 1: [9]
    #   bin 2: [3, 3, 4]
    #   bin 3: [6, 3]
    #   bin 4: [10]
    #   bin 5: [6]
    #   bin 6: [8]
    #   bin 7: [6]
