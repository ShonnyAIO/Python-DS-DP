import os


class MoveFileCommand(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        os.rename(self.src, self.dst)

    def undo(self):
        os.rename(self.dst, self.src)


stack = []
stack.append(MoveFileCommand('hello.txt', 'foo.txt'))
stack.append(MoveFileCommand('foo.txt', 'bar.txt'))

stack.pop().undo()
stack.pop().undo()
