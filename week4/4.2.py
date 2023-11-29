def hashs(data, bucket):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % bucket


class HashBucket:
    fixedList = []
    overflowList = []
    len = 0
    bucket = 0
    def __init__(self, value, bucket):
        for x in range(value):
            self.fixedList.append("empty")
        self.len = value
        self.bucket = value//bucket
        self.bucketAmount = value//self.bucket

    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.bucketAmount
    
    def insert(self, data):
        desiredSlot = self.hash(data)
        counter = desiredSlot*self.bucket
        stopPoint = desiredSlot*self.bucket + self.bucket
        while stopPoint >= self.len:
            stopPoint -= self.len
        while True:
            if self.fixedList[counter] == "empty" or self.fixedList[counter] == data:
                self.fixedList[counter] = data
                break
            else:
                counter += 1
                if counter >= self.len:
                    counter = 0
            if counter == stopPoint:
                self.overflowList.append(data)
                break

    def print(self):
        for x in self.fixedList:
            if x != "empty":
                print(x, end=" ")
        #print("overflow:", end=" ")       
        for x in self.overflowList:
            if x != "empty":
                print(x, end=" ")        
        print("")

    def printBucket(self, value):
        for x in range(len(self.fixedList)):
            if self.fixedList[x] != "empty" and value*self.bucket <= x and x < value*self.bucket+self.bucket:
                print(self.fixedList[x], end=" ")
        print("")        

    def delete(self, data):
        desiredSlot = self.hash(data)
        counter = desiredSlot*self.bucket
        stopPoint = desiredSlot*self.bucket + self.bucket
        while stopPoint >= self.len:
            stopPoint -= self.len
        while True:
            if self.fixedList[counter] == data:
                self.fixedList[counter] = "empty"
                break
            else:
                counter += 1
                if counter >= self.len:
                    counter = 0
            if counter == stopPoint:
                for x in range(len(self.overflowList)):
                    if self.overflowList[x] == data:
                        self.overflowList.pop(x)
                        break
                break


#
#table = HashBucket(8, 4)
#table.insert("BM40A1500")
#table.insert("fOo")
#table.insert("123")
#table.insert("Bar1")
#table.insert("10aaaa1")
#table.insert("BM40A1500")
#table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
#table.delete("fOo")
#table.delete("Some arbitary string which is not in the table")
#table.delete("123")
#table.print()   # BM40A1500 Bar1 10aaaa1

#print("\n")

#table2 = HashBucket(10, 5)
#table2.insert("buttermilk")
#table2.insert("shim")
#table2.insert("resolvend")
#table2.insert("cheiromegaly")
#table2.insert("premillennialise")
#table2.insert("finebent")
#print(hashs("buttermilk", 5))
#print(hashs("shim", 5))
#print(hashs("resolvend", 5))
#print(hashs("cheiromegaly", 5))
#print(hashs("premillennialise", 5))
#print(hashs("finebent", 5))
#table2.print() # buttermilk shim resolvend premillennialise cheiromegaly finebent
print("")

table3 = HashBucket(10, 5)
table3.insert("buttermilk")
table3.insert("shim")
table3.insert("resolvend")
table3.insert("cheiromegaly")
table3.insert("premillennialise")
table3.insert("finebent")
#print(hashs("resolvend", 10//5))
#print(hashs("buttermilk", 10//5))
#table3.printBucket(0)
#table3.printBucket(1)
table3.print() #buttermilk shim resolvend premillennialise cheiromegaly finebent
table3.delete("buttermilk")
table3.delete("cores")
table3.delete("cheiromegaly")
table3.delete("iodations")
table3.print() #shim resolvend premillennialise finebent
table3.insert("iodations")
table3.insert("tirrlie")
table3.insert("comous")
table3.insert("discursiveness")
table3.insert("flabbergasts")
#table3.printBucket(0)
#print(hashs("flabbergasts", 10//5))
table3.insert("rename")
table3.insert("softhead")
table3.print() #iodations discursiveness softhead comous rename shim resolvend premillennialise flabbergasts finebent tirrlie

print("")