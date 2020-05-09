"""
Cengage student.py
"""
class Student(object):
    """represents a student"""

    def __init__(self, name, number):
        """Constructor creates a sStudent with the given name and
        number of scores and sets all scores to 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student name"""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i-1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i-1]

    def getAverage(self):
        """Return the average score"""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student"""
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))



