"""Functions to parse a file containing student data."""



def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    houses = set()
    the_file = open(filename)
    for line in the_file:
      line_list = line.split("|")
      if line_list[2] != "":
        houses.add(line_list[2])
    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []
    the_file = open(filename)
    for line in the_file:
      line_list = line.split("|")
      full_name = f'{line_list[0]} {line_list[1]}'
      line_list[4] = line_list[4][:-1]
      if line_list[2] != "":
        if cohort == 'All':
          students.append(full_name)
        elif cohort == line_list[4]:
          students.append(full_name)

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    the_file = open(filename)

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []
    students = []
    
    house_dict = {
      "Dumbledore's Army": dumbledores_army,
      'Gryffindor': gryffindor,
      'Hufflepuff': hufflepuff,
      'Ravenclaw': ravenclaw,
      'Slytherin': slytherin,
      "G": ghosts,
      "I": instructors
    }
    for line in the_file:
      line_list = line.split("|")
      full_name = f'{line_list[0]} {line_list[1]}'
      line_list[4] = line_list[4][:-1]
      if line_list[2] == "":
        house_dict[line_list[4]].append(full_name)
      else:
        house_dict[line_list[2]].append(full_name)
        

    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    the_file = open(filename)
    all_data = []
    for line in the_file:
      line_list = line.split("|")
      line_list[4] = line_list[4][:-1]
      full_name = f'{line_list[0]} {line_list[1]}'
      new_list = [full_name] + line_list[2:]
      line_tuple = tuple(new_list)
      all_data.append(line_tuple)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    data = all_data(filename)
    for person in data:
      if person[0] == name:
        return person[3]
        break

def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    the_file = open(filename)
    all_data =[]
    last_names = []
    duplicates = set()
    for line in the_file:
      line_list = line.split("|")
      line_tuple = tuple(line_list)
      all_data.append(line_tuple)
    for person in all_data:
      if person[1] in last_names:
        duplicates.add(person[1])
      else:
        last_names.append(person[1])
    return duplicates




def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """
    data = all_data(filename)
    housemates = set()
    for person in data:
      if name == person[0]:
        house = person[1]
        cohort = person[3]
        for person in data:
          if house == person[1] and cohort == person[3] and name != person[0]:
            housemates.add(person[0])
    return housemates


    


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
