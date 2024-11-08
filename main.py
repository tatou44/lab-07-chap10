# class students:

from typing import List
class Student:

    numofstudent = 0  # to count students

    def __init__(self, name: str, scores: List[int]):     # added a type hint to scores
        self._name = name
        self._scores = scores        

        # increamenting the number of students:
        Student.numofstudent = Student.numofstudent + 1

    # defining getters and setters to get values of attributes and set new values to attributes:

    # For name:
    @property
    def name(self):                           # getter
        return self._name
    @name.setter
    def name(self, newname: str):             # setter
        self._name = newname
    
    # For scores:
    @property
    def scores(self):                         # getter 
        return self._scores
    @scores.setter
    def scores(self, newscores: List[int]):   # setter
        self._scores = newscores



    # define method to compute summation of students scores:
    def S_totalscores(self):    # # to be used on the gt, lt methods later for comparaison.
        return sum(self._scores)     
    
    # define method to compute the average score of student:
    def S_avg(self):       # to be used on the substract method later for comparaison.

        if self._scores:   # if the list 'scores' is not empty.
           return self.S_totalscores() / len(self._scores) 

        else:              # if the list 'scores' is empty
            return 0       # return zero.

    # implementing gt and lt methods to compare students based on the scores summation 'S_totalscores':

    # Greater then method:
    def __gt__(self, other):

        if isinstance(other, Student):
            return self.S_totalscores() > other.S_totalscores()

        return NotImplemented    

    # Less then method:
    def __lt__(self, other):
        
        if isinstance(other, Student):
            return self.S_totalscores() < other.S_totalscores()

        return NotImplemented  

    # Subtraction method (compares students based on average score):
    def __sub__(self, other):
        if isinstance(other, Student):
            return self.S_avg() - other.S_avg()
        
        return NotImplemented


    # implementing the string represntation method for the attributes name and scores:
    def __str__(self):
        # Join the scores list into a string with space separation
        scores_str = ' '.join(map(str, self.scores))  # map(str, self._scores) converts each score to a string.

        return f'Name: {self.name:>10}\tScores: {scores_str}'
    
    '''
    def __str__(self):
        strval = f'Name: {self._name:>10} \t Scores: '
        for i in range(len(self._scores)):
            strval += str(self._scores[i]) + '\t'
        return strval
    '''

def main():
    sc1 = [100, 100, 100]
    sc2 = [90, 90, 90]

    s1 = Student('James', sc1)
    s2 = Student('Mary', sc2)
    print(s1)
    print(s2)
    print(f'Total number of students: {Student.numofstudent}')
    print(f'Difference between s1 and s2 scores: {s1-s2}')

    print(s1 > s2)
    print(s1 < s2)


if __name__ == '__main__':
    main()
