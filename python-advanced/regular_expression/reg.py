# Lint as: python3
"""TODO(utkarshtiwari): DO NOT SUBMIT without one-line documentation for reg."""

import re

def main():
  string = 'xyz123d4'
  if (re.search('123', string)):
    print('Match found!!')
  else:
    print('Match not found!!')

  string_2 = 'abr123tczqx12'
  print(string_2,'---->', re.search('ab[rtz]', string_2)) #matches any single character in a character class []
    
  #matches any character from a range using hyphen
  print('ABXc23sdk --->', re.search('[a-z]', 'ABXc23sdk'))
  print('123 --->', re.search('[a-z]','123'))

  #The character class can be repeated to match a sequence of single characters
  print('ABXc23sdk --->', re.search('[a-z][0-9]', 'ABXc23sdk')) #matches any single digit followed by any lowercase character
  print('ABXcD23sdk --->', re.search('[a-z][0-9]', 'ABXcD23sdk'))

  print('a032---->', re.search('[0-9a-zA-Z]', 'a032')) #matches hexadecimal characters
  print('Hij----->', re.search('[0-9a-fA-Z]','Hij'))

  #Complement a character class by using ^ or '\A'
  print('utkarsHT---->', re.search('[^0-9a-z]', 'utkars1HT')) #matches the character without numbers or lowercase
  print('utkarsht---->', re.search('[^0-9a-z]', 'utkarsh1t'))

  #if these special metacharacters are to be included for pattern matching
  print('abc-xyz---->', re.search('[-abc]', 'abc-xyz')) #accepts '-' as a character if placed first or last or suceeded by '\'
  print('abc-123---->', re.search('[123-]', 'abc-123'))
  print()
  
  print('[xyz]---->', re.search('[]]', '[xyz]')) #if ']' to be accepted as a character, pass it at front or suceeded by '\'
  print('[ab12]---->', re.search('[\[]', '[ab12]'))
  print('abc*xyz---->', re.search('[+*|]', '[abc*xyz]')) #other metacharacters lose their meanings inside '[]'
  print()
 
  # dot(.), \w, \W, \d, \D metacharacters
  print('fooxbar---->', re.search('foo.bar', 'fooxbar')) #dot metacharacter matches any single character except newline
  print('foo\\nbar---->', re.search('foo.bar', 'foo\nbar'))
  print()

  print('#*7abc(---->', re.search('\w', '#*7abc(')) #Matches any word character like alphabet, numbers and '_'
  print('#$%@%^---->', re.search('\w', '#$%@%^'))
  print()
 
  print('#*7abc(---->', re.search('\W', '#*7abc(')) #Matches any characters except word characters
  print('7abc---->', re.search('\W', '7abc'))
  
  print('#*7abc(---->', re.search('\d', '#*7abc(')) #Matches a decimal digit
  print('#*7abc(---->', re.search('\D', '#*7abc(')) #Does not mactch a decimal digit

  print('foo\\nbar---->', re.search('\s', 'foo\nbar')) #Matches whitespace characters
  
  print('foo\\nbar---->', re.search('bar$', 'foo\nbar')) #'$' or '\Z'matches the characters at the end of a string
  print('barfoo---->', re.search('bar$', 'barfoo'))
  print('foor---->', re.search('bar$', 'foor')) #The string must end with all the characters which precedes "$" in given regex
  print()

  print('foo\\nbar---->', re.search(r'foo\b', 'foo\nbar')) #'\b' matches a word boundary either at the end or starting of a word.
  print('foo\\nbar---->', re.search(r'\bbar', 'foo\nbar'))
  print('foobar---->', re.search(r'\bbar', 'foobar'))
  print('foo bar bav---->', re.search(r'\bbar\b', 'foo bar bav'))
  print('foobarbav---->', re.search(r'\bbar\b', 'foobarbav'))
  print('foo\\nbar---->', re.search('\Bbar\B', 'foobarbav')) #'\B' works opposite of '\b'
  print()

  print('foobar---->', re.search('foo-*bar', 'foobar')) #'*' is a quantifier that matches if the character preceeding it has zero or more occurences.
  print('foo-bar---->', re.search('foo-*bar', 'foo-bar')) 
  print('foo---bar---->', re.search('foo-*bar', 'foo---bar'))
  print()
  
  print('foobar---->', re.search('foo-+bar', 'foobar')) #'+' matches if character preceeding it has one or more occurences.
  print('foo-bar---->', re.search('foo-+bar', 'foo-bar'))
  print()
  
  print('foobar---->', re.search('foo-?bar', 'foobar')) #'?' matches if preceeding characater occurs either once or not at all.
  print('foo-bar---->', re.search('foo-?bar', 'foo-bar'))
  print('foo---bar---->', re.search('foo-?bar', 'foo---bar'))
  print()

  print('Explaining the lazy versions of +, *, ?:')
  """ Here the * metacharacter follows a greedy approach to select the '>' character by selecting all the '>'
      characters up until the end. To follow a non-greeedy approach we use lazy versions of '*' i.e '*?' """
  print('<utk> <abc> <xyz>---->', re.search('<.*>', '<utk> <abc> <xyz>'))
  print('<utk> <abc> <xyz>---->', re.search('<.*?>', '<utk> <abc> <xyz>'))

  """ Following the greedy approach, the '?' will match the maximum possible occurence i.e one k. """
  print('utk?---->', re.search('tk?', 'utkkkk')) #The '?' always follows either zero or one occurence of preceeding character
  print('utkkkk---->', re.search('tk??', 'utkkkk'))

  print('Explaining the use of {} acting as metacharacter')
  """ {} act as a metacharacter only when they are of formats - {m,n}, {m,}, {,n}, {,} where m,n are lower and
      upper bounds of number of occurences of a preeceding character"""
  
  print('utk---->', re.search('utk{2,5}', 'utk'))
  print('utkk---->', re.search('utk{2,5}', 'utkk'))
  print('utkkkkk---->', re.search('utk{2,5}', 'utkkkkk'))

  """NOTE: If the occurences of {m,n} of a preeceding character is checked in between two strings than it takes a greedy
     approach and matches n occurences of the character if the string has more than n occurences of that character"""
  print('ukkkkkkt---->', re.search('uk{2,5}t', 'ukkkkkkt'))
  print('utkkkkkk---->', re.search('utk{2,5}?', 'utkkkkkk')) #lazy version {m,n}?
  
  print('Grouping construct')
  print('utkutkutk---->', re.search('(utk)+', 'utkutkutk')) #Treats the character in () as a single unit
  print('utkutk utk---->', re.search('(utk)+', 'utk utk utk'))
  print('utk---->', re.search('(utk)?', 'utk'))

  print('123---->', re.search('(foo(bar)+)?(\d\d\d)?', '123')) #We can create complex regex with the help of grouping constructs
  print('ukkkkkkt---->', re.search('(foo(bar)+)?(\d\d\d)?', 'foobar'))
  print()
  
  print('Capturing grouping constructs')
  print('utk,abc,def,123---->', re.search('(\w+),(\w+),(\w+),(\w+)', 'utk,abc,def,123'))
  string = re.search('(\w+),(\w+),(\w+),(\w+)', 'utk,abc,def,123')
  print('string.groups() will return:', string.groups()) #groups() will return a tuple containing all the matches separated by commas
  print('string.group(index) will return:', string.group(1)) 
  
  #will return a single value of the tuple returned from groups() based on the index value passed
  print('string.group(index) will return:', string.group(2)) 
  print('string.group(index1, index2) will return:', string.group(1, 2))
  
if __name__ == '__main__':
  main()
