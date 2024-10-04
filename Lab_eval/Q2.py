import math

def manual_token(text):

    word_count = 0
    len_word= 0
    for words in text:
          if words != " ":
                for char in words:
                      len_word += 1
                      
            
          elif words == " ":
                word_count+= 1
    return word_count, len_word

text = "In a world of shadows and whispers, where time flows like a gentle stream, stories unfoldin the silence. Each moment is a brushstroke on the canvas of existence, painting emotions with hues of joy and sorrow. Nature's beauty surrounds us, reminding us of the fragile balance between light and darkness."

result,length = manual_token(text)
print(f"The number of tokens in the paragraph is : {result} and the average length = {length/result}")


