import sys

from helper import *
class Seating:
    def __init__(self,request,sum):
        self.smallest_available_row=0
        # self.smallest_available_size=20
        self.seat = [ [0]*20 for i in range(10)]
        self.request=request
        self.total_n=sum
        self.result=dict()

    def print_result(self):
        print(self.result)
        return self.result
    def print_request(self):
        print(self.request)
    def _check_first_available_seat(self,cur_row,n):

        while 0 not in self.seat[cur_row]:
            cur_row+=1
        s = self.seat[cur_row].index(0)
        temp_s= s
        while  not self._check_no_unavailable_seat(cur_row,s,s+n):

            if s+ n >19:
                self.smallest_available_row=cur_row
                cur_row+=1
                s=self.seat[cur_row].index(0)
            else:
                s = self.seat[cur_row][temp_s:].index(0)
        if s+ n==19:
            self.smallest_available_row+=1
        return cur_row,s
    def _check_no_unavailable_seat(self,cur_row,start, end):
        if end > 19:
            return False
        if 1 not in self.seat[cur_row][start:end+1]:
            return True
        return False
    #place the larger group first.
    def greedy_alg(self):
        cur_row=0
        for r,n in sorted(self.request.items(), key = lambda item :item[1], reverse = True):
            cur_row, first_empty= self._check_first_available_seat(cur_row,n)

            if cur_row+1<10 and 0 in self.seat[cur_row+1]:
                first_empty_s = self.seat[cur_row+1].index(0)
            if first_empty>first_empty_s:
                cur_row+=1
                first_empty = self.seat[cur_row].index(0)
            self.result[r] = [ chr(cur_row + 65) + str(first_empty+i) for i in range(n+1)]
            for i in range(-1,n+3):
                if first_empty+i>=0:
                    if first_empty+i>=20:
                        break
                    self.seat[cur_row][first_empty+i]=1
                    if cur_row-1>=0 and i not in [n+2,n+3]:
                        self.seat[cur_row-1][first_empty + i] = 1
                    if cur_row + 1 <= 9 and (i !=n+2 and i!=n+3):
                        self.seat[cur_row + 1][first_empty + i] = 1
            cur_row=self.smallest_available_row




def store_input():
    temp_request=dict()
    sum = 0
    with open(sys.argv[1], 'r') as f:
        while True:
            contents = f.readline()
            if not contents:
                break
            s = contents.split(" ")
            n= int(s[1])
            r = int(s[0][1:])
            sum+= n
            if exceed_capacity(sum,s[0]):
                break
            if is_valid_amount(n,s[0]):
                temp_request[r]= n-1

        return Seating(temp_request,sum)
def output_in_text(seating):
    with open("output.txt", 'w') as f:
        for r, n in sorted(seating.result.items(), key=lambda item: item[0]):
            f.write("R"+ str(r).zfill(3)+" "+" ".join(n) + "\n")





if __name__ == '__main__':
    a= set(range(10))
    print(a-{1})
    seating = store_input()
    seating.print_request()
    seating.greedy_alg()
    seating.print_result()
    output_in_text(seating)

