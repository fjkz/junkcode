class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        elms = path.split("/")
        for elm in elms:
            if elm == '' or elm == '.':
                continue
            if elm == '..':
                if path_stack:
                    path_stack.pop()
                continue
            path_stack.append(elm)
        return '/' + '/'.join(path_stack)
