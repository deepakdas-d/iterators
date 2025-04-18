#Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.
import os

def findfiles(directory):
    for root,dir, files in os.walk(directory):#os.walk function helps us to traverse through a directory
        for file in files:
            yield os.path.join(root, file)

path = "D:\python\modulus"  
for filepath in findfiles(path):
        print(filepath)
#### output
# D:\python\modulus\problem1.py
# D:\python\modulus\problem2.py
# D:\python\modulus\problem3.py
# D:\python\modulus\problem4.py
# D:\python\modulus\sample.txt
# D:\python\modulus\.git\COMMIT_EDITMSG
# D:\python\modulus\.git\config
# D:\python\modulus\.git\description
# D:\python\modulus\.git\HEAD
# D:\python\modulus\.git\index
# D:\python\modulus\.git\hooks\applypatch-msg.sample
# D:\python\modulus\.git\hooks\commit-msg.sample
# D:\python\modulus\.git\hooks\fsmonitor-watchman.sample
# D:\python\modulus\.git\hooks\post-update.sample
# D:\python\modulus\.git\hooks\pre-applypatch.sample
# D:\python\modulus\.git\hooks\pre-commit.sample
# D:\python\modulus\.git\hooks\pre-merge-commit.sample
# D:\python\modulus\.git\hooks\pre-push.sample
# D:\python\modulus\.git\hooks\pre-rebase.sample
# D:\python\modulus\.git\hooks\pre-receive.sample
# D:\python\modulus\.git\hooks\prepare-commit-msg.sample
# D:\python\modulus\.git\hooks\push-to-checkout.sample
# D:\python\modulus\.git\hooks\sendemail-validate.sample
# D:\python\modulus\.git\hooks\update.sample
# D:\python\modulus\.git\info\exclude
# D:\python\modulus\.git\logs\HEAD
# D:\python\modulus\.git\logs\refs\heads\main
# D:\python\modulus\.git\logs\refs\remotes\origin\main
# D:\python\modulus\.git\objects\05\722a59f3ccb3d7f46920fc97926fa3f98f666b
# D:\python\modulus\.git\objects\23\895347b1605f6b93c76df33e49cc74ad34c6c6
# D:\python\modulus\.git\objects\2c\0de2bca69028d111ff0e6560fc41823fde00e8
# D:\python\modulus\.git\objects\41\f8024ef615e6c1312bf64769d698db5684f856
# D:\python\modulus\.git\objects\51\58b1f2e785c0c0c7c974c253fc81d6335efb10
# D:\python\modulus\.git\objects\9a\a435a33f58cb7359699bb142beaab9caf8a0f8
# D:\python\modulus\.git\objects\b6\16f54577764bd9b85d9c6ee15441cd576aa908
# D:\python\modulus\.git\refs\heads\main
# D:\python\modulus\.git\refs\remotes\origin\main