import inflect

p = inflect.engine()
# Add the list of lyrics
lyrics = ["Adieu", "Adieu"]
while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    # Add the input to list of lyric
    lyrics.append(name)

lyrics[2] = "to " + lyrics[2]
if len(lyrics) == 3:
    new_lyrics = p.join(lyrics, conj="to")
elif len(lyrics) == 4:
    new_lyrics = p.join(lyrics, final_sep="and")
else:
    new_lyrics = p.join(lyrics)
print(new_lyrics)
