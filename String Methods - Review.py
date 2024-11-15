highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
#1First, start by printing highlighted_poems to the terminal and see how it displays.
#print(highlighted_poems)
#2The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication. Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.
highlighted_poems_list = highlighted_poems.split(",")
#3Print highlighted_poems_list, how does the structure of the data look now?
#print(highlighted_poems_list)
#4Start by creating a new empty list, highlighted_poems_stripped. Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped.
highlighted_poems_stripped = [] 
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
#5Print highlighted_poems_stripped.
#print(highlighted_poems_stripped)
#6Next we want to break up all the information for each poem into it’s own list, so we end up with a list of lists. Create a new empty list called highlighted_poems_details.
highlighted_poems_details = []
#7Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.
for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(":"))
print(highlighted_poems_details)
#8Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists. Create three new empty lists, titles, poets, and dates.
titles = []
poets = []
dates = []
#9Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates. For example, for the poem The Shadow (1915) by William Carlos Williams your code should be adding "The Shadow" to titles, "William Carlos Williams" to poets, and "1915" to dates.
for i in highlighted_poems_details:
  contador = 0
  for j in i:
    if contador == 0:
      titles.append(j)
      contador += 1
    elif contador == 1:
      poets.append(j)
      contador += 1
    else:
      dates.append(j)
      contador = 0
  
print(titles)
print(poets)
print(dates)
#10Finally, write a for loop that uses .format() to print out the following string for each poem: The poem TITLE was published by POET in DATE.

def elpepe(title,poet,date):
  return "The poem {} was published by {} in {}".format(title,poet,date)

for i in range(0,len(titles)):
  print(elpepe(titles[i],poets[i],dates[i]))
