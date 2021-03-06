'''
Program:               Pattern Search and Replace Script
Author:                
Class:                 IT-140-T5093 Introduction to scripting 18EW5
Instructor             
Date:                  17 Jun 2018
Description:        A program that by the use of strings and assigned outcomes the software is able 
                    to find the outcome of command line. Finally, there are endless solutions to the problems
                    with a set of strings and expressions it is able to track the problem.
'''
import re
original_text='''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor.
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo.
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''
lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor.
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo.
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

results=re.findall(r"[^a-zA-Z0-9]",lorem_ipsum);
print(len(results))#no of non-alphanumeric characeters
occurance_sit_amet=re.findall(r"sit[\-|\:]amet",lorem_ipsum);
print(len(occurance_sit_amet))#no of sit-/:amet
replace_results=re.sub(r"sit[\-|\:]amet","sit amet",lorem_ipsum)
occurance_sit_amet=re.findall(r"(sit amet)+",replace_results);
print(len(occurance_sit_amet))#after replacing the no of sit amet
