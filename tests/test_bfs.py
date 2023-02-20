from algorithms.bfs import (
    count_islands,
    maze_search,
    ladder_length
)

import unittest


class TestCountIslands(unittest.TestCase):

    def test_count_islands(self):
        flags = [False for _ in range(10)]

        grid_1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
        self.assertEqual(1, count_islands(grid_1, flags))
        grid_2 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 1]]
        self.assertEqual(3, count_islands(grid_2, flags))
        grid_3 = [[1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1],
                  [0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0]]
        self.assertEqual(3, count_islands(grid_3, flags))
        grid_4 = [[1, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 0, 0]]
        self.assertEqual(5, count_islands(grid_4, flags))

        branches_taken = 0
        for flag in flags:
            if flag == True:
                branches_taken += 1
        branch_coverage = branches_taken/len(flags)

        print("Branches taken: " + str(branches_taken))
        print("Branch coverage: " + str(branch_coverage))


class TestMazeSearch(unittest.TestCase):

    def test_maze_search(self):
        grid_1 = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1],
                  [1, 1, 1, 0, 1, 1]]
        self.assertEqual(14, maze_search(grid_1))
        grid_2 = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
        self.assertEqual(-1, maze_search(grid_2))


class TestWordLadder(unittest.TestCase):

    def test_ladder_length(self):

        # hit -> hot -> dot -> dog -> cog
        self.assertEqual(5, ladder_length('hit', 'cog', ["hot", "dot", "dog",
                                          "lot", "log"]))

        # pick -> sick -> sink -> sank -> tank == 5
        self.assertEqual(5, ladder_length('pick', 'tank',
                                          ['tock', 'tick', 'sank', 'sink',
                                           'sick']))

        # live -> life == 1, no matter what is the word_list.
        self.assertEqual(1, ladder_length('live', 'life', ['hoho', 'luck']))

        # 0 length from ate -> ate
        self.assertEqual(0, ladder_length('ate', 'ate', []))

        # not possible to reach !
        self.assertEqual(-1, ladder_length('rahul', 'coder', ['blahh',
                                           'blhah']))


if __name__ == "__main__":
    unittest.main()
