# pands-problem-sheet
# helloworld.py Week 01 task says 'Hello World!' 

# bank.py Week02 task converting cents to euro
# reference: https://www.adamsmith.haus/python/answers/how-to-format-a-float-as-currency-in-python
# https://www.w3schools.com/python/python_numbers.asp
# https://www.w3schools.com/python/ref_func_int.asp#:~:text=The%20int()%20function%20converts%20the%20specified%20value%20into%20an%20integer%20number.




# accounts.py Week03 Weekly task - account number hidden with asterisk
 # Reference for work: https://www.educative.io/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python
# https://realpython.com/python-map-function/
# https://www.simplilearn.com/tutorials/python-tutorial/map-in-python


# collatz.py Week 04
# references: https://www.angela1c.com/projects/problem_set_links/problem4/
# https://www.quora.com/What-is-the-difference-between-and-in-Python-6
# https://geekflare.com/floor-division-python/
# https://realpython.com/python-append/#:~:text=A%20call%20to%20.append(),items%20in%20the%20available%20space.&text=Lists%20are%20sequences%20that%20can,finally%20a%20floating%2Dpoint%20number.
# https://www.w3schools.com/python/ref_func_print.asp
# https://www.w3schools.com/python/python_tuples_unpack.asp#:~:text=Using%20Asterisk%20*&text=If%20the%20asterisk%20is%20added,the%20number%20of%20variables%20left.
# https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp


# weekday.py Week 05
# I didn't use external sources for this - I tried to rework the lab from Week 05 to apply to this, as described in the file.

# squareroot.py Week 06
# References: 
# https://www.angela1c.com/projects/problem_set_links/problem7/
# https://pythonhow.com/how/limit-floats-to-two-decimal-points/#:~:text=To%20limit%20a%20float%20to,resulting%20in%20the%20value%203.14.

# es.py Week 07
# I created a file called ulysses.txt, which includes an excerpt from James Joyce's Ulysses. I opened the file as a read document in python, following instructions from the lecture. I defined a function that counted the number of a particular letter, this can be changed depending on your letter of choice. I defined the 'lettercount' - ans = lettercount to allow me to add text and use the function method to return the answer to the number of times the letter 'e' appears in the execpt. 
# I used the sys module - sys.argv - to try to add the anme of the text to the python file from the command line. sys.argv is a simple list structure. It’s main purposes are:
# - It is a list of command line arguments.
# - len(sys.argv) provides the number of command line arguments.
# - sys.argv[0] is the name of the current Python script. 
# references: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# https://www.geeksforgeeks.org/command-line-arguments-in-python/


# Week 08 - weekly task Plotting
# I found this useful to talk through the task simply: https://www.sharpsightlabs.com/blog/numpy-random-normal/
# I also watched this video: https://www.youtube.com/watch?v=ufO_BScIHDQ
# Other references I looked at: 
# https://rowannicholls.github.io/python/graphs/ax_based/histograms.html
# https://www.geeksforgeeks.org/how-to-plot-a-dashed-line-in-matplotlib/
# https://realpython.com/python-histograms/
# https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
# To begin with, I imported numpy and matplotlib to work with plotting graphs.I had tried the scipy library as well after doing some reading but I don't think this was needed in the end so I removed it. 
# I defined the data set - normal_data - indicating a loc(mean) of 5, scale(stdev) of 2 and size of 1000. I can across those definitions (loc and scale) in my reading on the topic. I tried running the program without loc and scale, using just numbers i.e 5,2,1000 - and it also worked.
# I defined the xpoints and ypoints as demonstrated in the lecture on the topic. I noticed when I ran the array with range of 0-10, the plotted line only reached 9 on the graph. I heard in the youtube video referenced above that it often discounts the last point on the range so I changed the array to 0-11 to make sure the plotted line reached 10.
# I plotted the line, giving it a blue colour and dashed looked to make it stand out more, alongside the relevant label and legend.
# I labelled the x and y axes of the histogram and gave it a title, as was demonstrated in the lecture. 
# I gave the histogram some characteristics, such as a white colour and a black edge so that it worked nicely alongside the blue plotted line. I came across the coloredge function in my reading and thought it was a good way to define the lines. And I like the white background when running a colour through it. It looks cleaner visually than plotting a blue line through another colour for example.
# I saved off the graph as a .png as well, just for the fun.
