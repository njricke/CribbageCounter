class CribbageHand:
    def __init__(self, c1, c2, c3, c4, f):

        #Check for duplicate cards
        self.cardList = [c1.name, c2.name, c3.name, c4.name, f.name]
        for c in self.cardList:
            if self.cardList.count(c) > 1:
                print('Error- Duplicate card entered')
                exit()

        self.suitList = [c1.suit, c2.suit, c3.suit, c4.suit, f.suit]
        self.numberList = [c1.number, c2.number, c3.number, c4.number, f.number]
        self.sortedNumbers = sorted(self.numberList)
        self.valueList = [c1.value, c2.value, c3.value, c4.value, f.value]
        self.numberSet = set(self.numberList)
        self.totalPoints = 0

    def count_flush(self):
        if self.suitList.count(self.suitList[0]) == 5:
            print('You have a flush for 5 points!')
            return 5
        elif self.suitList[0:-1].count(self.suitList[0]) == 4:
            print('You have a flush for 4 points!')
            return 4
        else:
            return 0

    def count_nobs(self):
        if 11 in self.numberList:
            suitOfJack = self.suitList[self.numberList.index(11)] #Find the suit of the Jack
            nobs = suitOfJack == self.suitList[-1]  #Compare the suit of Jack to suit of flipCard
            if nobs:
                #print('You have nobs for 1 point!')
                return 1
        else:
            return 0

    def count_15s(self):
        results = [seq for i in range(len(self.valueList), 0, -1) for seq in itertools.combinations(self.valueList, i) if sum(seq) == 15]
        if len(results) == 1:
            #print('You have {} fifteen for {} points'.format(len(results), len(results) * 2))
            return (2 * len(results))
        elif len(results) >= 1:
            #print('You have {} fifteens for {} points'.format(len(results), len(results) * 2))
            return (2 * len(results))
        else:
            return 0

    def count_pairs(self):
        pairPoints = 0
        for number in self.numberSet:
            if self.numberList.count(number) == 2:
                pairPoints += 2

            elif self.numberList.count(number) == 3:
                pairPoints += 6

            elif self.numberList.count(number) == 4:
                pairPoints += 12

        return pairPoints

    def count_runs(self):

        def run_of_five(): #returns a list of run of 5 combinations found in hand
            run_of_five_combos = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), (4, 5, 6, 7, 8), (5, 6, 7, 8, 9),
                                  (6, 7, 8, 9, 10), (7, 8, 9, 10, 11), (8, 9, 10, 11, 12), (9, 10, 11, 12, 13)]
            run_of_five_results = list(itertools.combinations(self.sortedNumbers, 5))
            runs = 0

            for result in run_of_five_results:
                for combo in run_of_five_combos:

                    if list(result) == list(combo):
                        return runs + 1
            return runs

        def run_of_four(): #returns a list of run of 4 combinations found in hand
            run_of_four_combos = [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6), (4, 5, 6, 7), (5, 6, 7, 8), (6, 7, 8, 9),
                                  (7, 8, 9, 10), (8, 9, 10, 11), (9, 10, 11, 12), (10, 11, 12, 13)]
            run_of_four_results = list(itertools.combinations(self.sortedNumbers, 4))
            runs = 0
            for result in run_of_four_results:
                for combo in run_of_four_combos:
                    if list(result) == list(combo):
                        runs += 1
                        if runs == 2:
                            return runs
            return runs

        def run_of_three(): #returns a list of run of 3 combinations found in hand
            run_of_three_combos = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (5, 6, 7), (6, 7, 8), (7, 8, 9),
                                   (8, 9, 10), (9, 10, 11), (10, 11, 12), (11, 12, 13)]

            run_of_three_results = list(itertools.combinations(self.sortedNumbers, 3))
            runs = 0
            for result in run_of_three_results:
                for combo in run_of_three_combos:
                    if list(result) == list(combo):
                        runs += 1
                        if runs == 3:
                            return runs
            return runs


        def check_runs():
            if run_of_five() > 0:
                return 5
            elif run_of_four() > 0:
                if run_of_four() == 1:
                    return 4
                elif run_of_four() == 2:
                    return 8
            elif run_of_three() > 0:
                return (run_of_three() * 3)
            else:
                return 0

        return check_runs()

    def count_points(self):

        print('Flush: {}'.format(self.count_flush()))
        print('Nobs: {}'.format(self.count_nobs()))
        print('15s: {}'.format(self.count_15s()))
        print('Pairs: {}'.format(self.count_pairs()))
        print('Runs: {}'.format(self.count_runs()))

        totalPoints = self.count_flush() + self.count_nobs() + self.count_15s() + self.count_pairs() + self.count_runs()

        return totalPoints
