import webbrowser

# List of 6 educational hyperlinks for CSE students
links = [
    "https://www.geeksforgeeks.org/",
    "https://leetcode.com/",
    "https://www.hackerrank.com/domains/tutorials/10-days-of-javascript",
    "https://www.coursera.org/browse/computer-science",
    "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/",
    "https://github.com/ossu/computer-science"
]

print("Opening six educational hyperlinks for Computer Science Engineering students:")
for url in links:
    print("Opening:", url)
    webbrowser.open(url)
