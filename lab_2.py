class Pagination():
    list = {}
    size = 0
    total_page = 1

    def __init__(self, my_list, size):
        self.list = list(my_list)
        self.size = size

    def getVisibleItems(self):
        current_page = 1
        for i in range(0,len(self.list), self.size):
            for j in range(i,self.size*current_page):
                if j == len(self.list):
                    break
                print(self.list[j], end=' ')
            if i % self.size == 0:
                current_page += 1
            print()

    def firstPage(self):
        for i in range(self.size):
            print(self.list[i], end=' ')
        print()

    def lastPage(self):
        size = len(self.list) % self.size
        for i in range(len(self.list) - size, len(self.list)):
            print(self.list[i], end=' ')
        print()

    def goToPage(self, number_page:int):
        for i in range(self.size * (number_page-1), self.size * number_page):
            if i == len(self.list):
                    break
            print(self.list[i], end=' ')
        print()

    def nextPage(self):
        if self.__check_next == False:
            return
        self.total_page += 1
        self.goToPage(self.total_page)

    def prevPage(self):
        if self.__check_prev == False:
            return
        self.total_page -= 1
        self.goToPage(self.total_page)

    def __check_next(self):
        if self.total_page == self.size:
            return False
        else:
            return True

    def __check_prev(self):
        if self.total_page == 1:
            return False
        else:
            return True

def main():
    alphabet_list = "abcdefghijklmnopqrstuvwxyz"
    p = Pagination(alphabet_list, 10)

    print('all pages: ')
    p.getVisibleItems()

    print('first page:')
    p.firstPage()

    print('last page: ')
    p.lastPage()

    print('go to page 3: ')
    p.goToPage(3)

    print('next: ')
    p.nextPage()

    print('prev: ')
    p.prevPage()

if __name__ == "__main__":
    main()
