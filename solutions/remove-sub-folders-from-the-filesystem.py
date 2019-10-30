from typing import List

# TLE 27 / 31 test cases passed.
# class Solution:
#     """
#     Slow. O(n^2).
#     """

#     def removeSubfolders(self, folder: List[str]) -> List[str]:

#         def is_subfolder(folder, subfolder):
#             if len(folder) > len(subfolder):
#                 return False
#             if folder == subfolder:
#                 return True
#             for i in range(len(folder)):
#                 if folder[i] != subfolder[i]:
#                     return False
#             return subfolder[i+1] == '/'

#         added = set()
#         for _folder in folder:
#             check = False
#             for _added in added:
#                 if is_subfolder(_folder, _added):
#                     check = True
#                     break
#                 elif is_subfolder(_added, _folder):
#                     break
#             else:
#                 added.add(_folder)
#             if check:
#                 added = {i for i in added if not is_subfolder(_folder, i)}
#                 added.add(_folder)
#         return list(added)


class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.terminal = False
        self.children = []


class Solution:
    """
    Trie tree + BFS
    """

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode('/')

        for folder_item in folder:
            node = root
            folder_item = folder_item.split('/')[1:]
            subdir = False
            for seg in folder_item:
                for child in node.children:
                    if seg == child.char:
                        if child.terminal:
                            subdir = True
                            break
                        node = child
                        break
                else:
                    new_node = TrieNode(seg)
                    node.children.append(new_node)
                    node = new_node
                if subdir:
                    # current dir is subdir. Abort
                    break
            else:
                node.terminal = True

        res = []
        queue = []
        parent = {}
        node = root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            for child in node.children:
                parent[child] = node
                if child.terminal:
                    segs = []
                    n = child
                    while n.char != '/':
                        segs.append(n.char)
                        n = parent[n]
                    segs = '/' + '/'.join(reversed(segs))
                    res.append(segs)
                else:
                    queue.append(child)
        return res


if __name__ == '__main__':
    solution = Solution()
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    res = solution.removeSubfolders(folder)
    print(sorted(res))

    folder = ["/a", "/a/b/c", "/a/b/d"]
    res = solution.removeSubfolders(folder)
    print(sorted(res))

    folder = ["/aa/ab/ac/ae", "/aa/ab/af/ag", "/ap/aq/ar/as", "/ap/aq/ar", "/ap/ax/ay/az",
              "/ap", "/ap/aq/ar/at", "/aa/ab/af/ah", "/aa/ai/aj/ak", "/aa/ai/am/ao"]
    res = solution.removeSubfolders(folder)
    print(sorted(res))
