#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[3]:


def sed(pattern, replacement, fin, fout):
    finMem = open(sgb-words.txt)
    foutMem = open(fout, 'W+')
    for line in finMem:
        if pattern in line:
            print 'pattern found'
            newLine = line.replace(pattern,replacement)
            foutMem.write(newLine)
        else:
            foutMem.write(line)


# In[4]:


def sed(pattern, replacement, fin, fout):
    finMem = open(fin)
    foutMem = open(fout, 'W+')
    for line in finMem:
        if pattern in line:
            print (pattern found)
            newLine = line.replace(pattern,replacement)
            foutMem.write(newLine)
        else:
            foutMem.write(line)


# In[5]:


if __name__ == '__main__':
    print os.getcwd()
    pattern = 'oy'
    replacement = 'it'
    fin = "/localhost:8888/edit/sgb-words.txt"
    fout = "/localhost:8888/edit/words.txt"
    sed(pattern, replacement, fin, fout)


# In[6]:


from __future__ import print_function, division


# In[7]:


def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[8]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sgb-words.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[9]:


if __name__ == '__main__':
    main()


# In[10]:


def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[11]:


import os


# In[12]:


cwd = os.getcwd()


# In[13]:


cwd


# In[14]:


def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[15]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[16]:


if __name__ == '__main__':
    print os.getcwd()


# In[17]:


def sed(pattern, replace, file1, file2):
    fin = open(file1)
    lines = fin.readlines()
    new_file = open(file2, 'w')
    for line in lines:
        new_line = line.replace(pattern_str, replacement_str)
        new_file.write(new_line)
    new_file.close()
    except:
        print (Error)


# In[18]:


def sed(pattern, replace, file1, file2):
    fin = open(file1)
    lines = fin.readlines()
    new_file = open(file2, 'w')
    for line in lines:
        new_line = line.replace(pattern_str, replacement_str)
        new_file.write(new_line)
    new_file.close()


# In[19]:


def sed(pattern_string, replacement_string, file1, file2):
    for line in firstfile:
        if(line.strip() == pattern_string):
            secondfile.write(replacement_string + "\n")
        else:
            secondfile.write(line)
    except OSError:
        print(Error)
        exit()


# In[20]:


def sed(pattern_string, replacement_string, file1, file2):
    for line in firstfile:
        if(line.strip() == pattern_string):
            secondfile.write(replacement_string + "\n")
        else:
            secondfile.write(line)
except OSError:
    print(Error)
    exit()


# In[21]:


def sed(pattern_string,replacement_string,file1,file2):
    with open(file1,'r') as firstfile, open(file2,'a') as secondfile:
        try:
            for line in firstfile:
                if(line.strip() == pattern_string):
                    secondfile.write(replacement_string + "\n")
                else:
                    secondfile.write(line)
            except OSError:
                print(Error)
                exit()


# In[22]:


def sed(pattern_string,replacement_string,file1,file2):
    with open(file1,'r') as firstfile, open(file2,'a') as secondfile:
        try:
            for line in firstfile:
                if(line.strip() == pattern_string):
                    secondfile.write(replacement_string + "\n")
                else:
                    secondfile.write(line)
        except:
            print('Error!')
            exit()


# In[23]:


if __name__ == '__main__':
    pattern_string = "this"
    replacement_string = "replaced"
    file1 = "wordlist1000.txt"
    file2 = "secondfile.txt"
    sed(pattern_string,replacement_string,file1,file2)


# In[24]:


if __name__ == '__main__':
    pattern_string = "this"
    replacement_string = "replaced"
    file1 = "sgb-words.txt"
    file2 = "words.txt"
    sed(pattern_string,replacement_string,file1,file2)


# In[25]:


def sed(pattern_string,replacement_string,file1,file2):
    with open(file1,'r') as firstfile, open(file2,'a') as secondfile:
        try:
            for line in firstfile:
                if(line.strip() == pattern_string):
                    secondfile.write(replacement_string + "\n")
                else:
                    secondfile.write(line)
        except:
            print('Error!')


# In[26]:


if __name__ == '__main__':
    pattern_string = "this"
    replacement_string = "replaced"
    file1 = "sgb-words.txt"
    file2 = "words.txt"
    sed(pattern_string,replacement_string,file1,file2)


# In[27]:


from __future__ import print_function, division


# In[28]:


def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[29]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[30]:


if __name__ == '__main__':
    main()


# In[31]:


from __future__ import print_function, division


# In[32]:


def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[33]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[34]:


if __name__ == '__main__':
    main()


# In[35]:


from __future__ import print_function, division


# In[36]:


def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[37]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[38]:


if __name__ == '__main__':
    print(sed(pattern, replace, source, dest))


# In[39]:


if __name__ == '__main__':
    print(sed('pattern', 'replace', 'source', 'dest'))


# In[40]:


from __future__ import print_function, division


# In[41]:


def sed(pattern, replace, source, dest):
    fin = open(sgb-words.txt, 'r')
    fout = open(words.txt, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[42]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[43]:


if __name__ == '__main__':
    print(sed('pattern', 'replace', 'source', 'dest'))


# In[44]:


from __future__ import print_function, division


# In[45]:


def sed(pattern, replace, source, dest):
    fin = open('sgb-words.txt', 'r')
    fout = open('words.txt', 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[46]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[47]:


if __name__ == '__main__':
    print(sed('pattern', 'replace', 'source', 'dest'))


# In[48]:


if __name__ == '__main__':
   main()
   print(sed('pattern', 'replace', 'source', 'dest'))


# In[49]:


from __future__ import print_function, division


# In[50]:


def sed(pattern, replace, source, dest):
    pattern: string
    replace: string
    source: sgb-words.txt
    dest: words.txt
    fin = open(source, 'r')
    fout = open(dest, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[51]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[52]:


if __name__ == '__main__':
    main()
    print(sed('pattern', 'replace', 'source', 'dest'))


# In[53]:


from __future__ import print_function, division


# In[54]:


def sed(pattern, replace, source, dest):
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    fin = open('sgb-words.txt', 'r')
    fout = open('words.txt', 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[55]:


def sed(pattern, replace, source, dest):
    pattern: string
    replace: string
    source: sgb-words.txt
    dest: words.txt
    fin = open('sgb-words.txt', 'r')
    fout = open('words.txt', 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[56]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[57]:


if __name__ == '__main__':
    main()
    print(sed('pattern', 'replace', 'source', 'dest'))


# In[1]:


from __future__ import print_function, division


# In[2]:


def sed(pattern, replace, source, dest):
    pattern: string
    replace: string
    source: sgb-words.txt
    dest: words.txt
    fin = open('sgb-words.txt', 'r')
    fout = open('words.txt', 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[3]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sgb-words.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[4]:


if __name__ == '__main__':
    main()
    print(sed('pattern', 'replace', 'source', 'dest'))


# In[5]:


from __future__ import print_function, division


# In[6]:


def sed(pattern, replace, source, dest):
    pattern: string
    replace: string
    source: sgb-words.txt
    dest: words.txt
    fin = open('sgb-words.txt', 'r')
    fout = open('words.txt', 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    fin.close()
    fout.close()


# In[7]:


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'words.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


# In[8]:


if __name__ == '__main__':
    main()
    print(sed('pattern', 'replace', 'source', 'dest'))


# In[ ]:




