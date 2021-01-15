#### Usecase ####
# a dataframe has a column with paragraph text - we need to search a pattern in the paragraph column 
# and form a new df with all the other column values (full row value)

# create empty dataframe
#template to have pattern search in the paragraph column
pattern_extract = pd.DataFrame([])

pattern_list = ['pattern1', 'pattern2', 'pattern3', 'pattern4']
for word in pattern_list:
    pattern_extract = pattern_extract.append(df[df['paragraph'].str.contains(word)== True].assign(Pattern=word))

df_data = pattern_extract
#reset the index as per the new dataframe
df_data.index = np.arange(len(df_data))
