def queen(n, m):

    boards = []
    boards.append((16, 300))

    for x in range(m):
        boards2 = []
        for z in range(len(boards)):
            for y in range(n**n):
                shift = y //(n)
                mod = y % (n)
                continueValue = 0

                for j in range(2, len(boards[z])):
                    if shift == boards[z][j][0]:
                        continueValue = 1
                        break
                    if mod == boards[z][j][1]:
                        continueValue = 1
                        break
                    #if (boards[z][j][0] - shift + (boards[z][j][1] - mod))%2 == 0:
                    #    continueValue = 1
                    #    break
                
                if continueValue == 1:
                    continue
                
                variation = transferValues(boards[z])
                variation.append((shift, mod))
                boards2.append(variation)
        boards = transferValues(boards2)
        
#    for x in boards:
#        print(x)
    # faulty = 0
    # for x in boards:
        
    #     locationList = []
    #     shift = 0
    #     for y in x:
    #         if "d" in y:
    #             mod = 0
    #             for z in y:
    #                 if z == "d":
    #                     location = []
    #                     location.append(shift)
    #                     location.append(mod)
    #                     locationList.append(transferValues(location))
    #                 mod += 1
    #         shift += 1
        
    #     shiftList = []
    #     modList = []
    #     for y in locationList:
    #         if y[0] not in shiftList:
    #             shiftList.append(y[0])
    #         else:
    #             faulty += 1
    #             break
    #         if y[1] not in modList:
    #             modList.append(y[1])
    #         else:
    #             faulty += 1
    #             break


    return len(boards)

def transferValues(listValues):
    transferList = []
    for x in listValues:
        transferList.append(x)
    return transferList

print(queen(1, 1))
#print(queen(4, 4))  # 2
#print(queen(4, 2))  # 44
#print(queen(6, 4))  # 982
#print(queen(7, 2))  # 700
#print(queen(8, 8))  # 92