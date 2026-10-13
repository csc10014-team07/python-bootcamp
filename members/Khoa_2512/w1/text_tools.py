def word_count(text: str) -> dict[str, int]:
    temp= text.replace(",", "").replace("!", "").replace(".", "").replace("?", "").replace(";", "").replace(":", "").lower().split()
    thisdict={}
    for x in temp:
        count=0
        for y in temp:
            if x==y:
                count+=1
        thisdict.update({x: count})
    return thisdict
 . , ! ? ; :
def top_k(text:str, k:int)->list[tuple[str, int]]:
    my_dict=word_count(text)
    mylist=list(my_dict.items())
    mylist.sort(key=lambda x: (-x[1], x[0]))
    return mylist[:k]

print(top_k("Git is fun. Git is fast!", 2))
