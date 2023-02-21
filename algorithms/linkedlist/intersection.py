"""
   This function takes two lists and returns the node they have in common, if any.
   In this example:
   1 -> 3 -> 5
               \
                7 -> 9 -> 11
               /
   2 -> 4 -> 6
   ...we would return 7.
   Note that the node itself is the unique identifier, not the value of the node.
   """
import unittest


class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


def intersection(h1, h2,flags):

    count = 0
    flag = None
    h1_orig = h1
    h2_orig = h2

    while h1 or h2:
        flags[0] = True
        count += 1

        if not flag and (h1.next is None or h2.next is None):
            flags[1] = True
            # We hit the end of one of the lists, set a flag for this
            flag = (count, h1.next, h2.next)
        else:
            flags[2] = True
        if h1:
            flags[3] = True
            h1 = h1.next
        else:
            flags[4] = True
        if h2:
            flags[5] = True
            h2 = h2.next
        else:
            flags[6] = True

    long_len = count    # Mark the length of the longer of the two lists
    short_len = flag[0]

    if flag[1] is None:
        flags[7] = True
        shorter = h1_orig
        longer = h2_orig
    elif flag[2] is None:
        flags[8] = True
        shorter = h2_orig
        longer = h1_orig
    else:
        flags[9] = True

    while longer and shorter:
        flags[10] = True
        while long_len > short_len:
            flags[11]  = True
            # force the longer of the two lists to "catch up"
            longer = longer.next
            long_len -= 1

        if longer == shorter:
            flags[12] = True
            # The nodes match, return the node
            return longer
        else:
            flags[13] = True
            longer = longer.next
            shorter = shorter.next

        print(flags)
        i = 0
        for flag in flags:
            if flag:
              i += 1

        ratio =  i / len(flags)
        print(ratio)
    return None

class TestSuite(unittest.TestCase):
    
    def test_intersection_1(self):

        # create linked list as:
        # 1 -> 3 -> 5
        #            \
        #             7 -> 9 -> 11
        #            /
        # 2 -> 4 -> 6
        a1 = Node(1)
        b1 = Node(3)
        c1 = Node(5)
        d = Node(7)
        a2 = Node(2)
        b2 = Node(4)
        c2 = Node(6)
        e = Node(9)
        f = Node(11)

        a1.next = b1
        b1.next = c1
        c1.next = d
        a2.next = b2
        b2.next = c2
        c2.next = d
        d.next = e
        e.next = f

        val = intersection(a1, a2, flags).val

        self.assertEqual(7, val)

    def test_intersection_2(self):
        
            # create linked list as:
            # 1 
            #     \        
            #         4 -> 5         
            #        /    
            # 2 -> 3
            a1 = Node(1)
            a2 = Node(2)
            b2 = Node(3)
            d = Node(4)
            e = Node(5)
                

            a1.next = d
            a2.next = b2
            b2.next = d
            d.next = e

            val = intersection(a1, a2, flags).val

            self.assertEqual(4, val)

    def test_intersection_3(self):
        
        # create linked list as:
        # 1 -> 3
        #             
        #         4         
        #     /    
        # 2
        a1 = Node(1)
        b1 = Node(2)
        a2 = Node(3)
        d = Node(4)

        a1.next = b1
        b1.next = d
        a2.next = d
        
        val = intersection(a1, a2, flags).val

        self.assertEqual(4, val)        

if __name__ == '__main__':
    flags =[False for i in range(14)] # For DIY Coverage report
    unittest.main()
    print(flags)
