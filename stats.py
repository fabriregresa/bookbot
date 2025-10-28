def get_num_words(text):
   words = text.split()
   return len(words)

def get_char_count(text):
   text = text.lower()
   chars = {}

   for char in text:
      if char in chars:
         chars[char] +=1
      else:
         chars[char] = 1
   
   return chars

def sort_characters(char_count_dict):
   sorted_list = []
   for char, num in char_count_dict.items():
      sorted_list.append({"char":char, "num": num})
   
   def sort_on(item):
      return item["num"]
   
   sorted_list.sort(reverse=True, key= sort_on)
   return sorted_list

