
class Student:
    numofStudent = 0
    

    def __str__(self):
        strval = f'Name: {self._name:>10} \t Scores: '
        for i in range(len(self._scores)):
            strval += str(self._scores[i]) + '\t'
        return strval


def main():
    sc1 = [100, 100, 100]
    sc2 = [90, 90, 90]

    s1 = Student('James', sc1)
    s2 = Student('Mary', sc2)
    print(s1)
    print(s2)
    print(f'Total number of students: {Student.numofStudent}')
    print(f'Difference between s1 and s2 scores: {s1-s2}')

    print(s1 > s2)
    print(s1 < s2)


if __name__ == '__main__':
    main()
