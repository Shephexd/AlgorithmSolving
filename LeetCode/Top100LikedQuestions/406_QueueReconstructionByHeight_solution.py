class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


'''
INPUT: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

PROGRESS:
[[7, 0]]
[[7, 0], [7, 1]]
[[7, 0], [6, 1], [7, 1]]
[[5, 0], [7, 0], [6, 1], [7, 1]]
[[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

OUTPUT:[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
'''
