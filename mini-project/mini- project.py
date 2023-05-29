import tkinter as tk
from PIL import ImageTk, Image  
import pygame  
from moviepy.editor import VideoFileClip

###########""" this is the Dictionary containing the key as morse code and value as alphabet and numbers"""########

MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z','.----':'1','..---':'2'
    ,'...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'
    ,'-----':'0',' ':'/'
}

######################Createing GUI window and giveing the Title to window #########################################
window = tk.Tk()

window.title("Morse Code Converter")
window.geometry("1200x800")

######################### creating background image  #################################
bg_image=Image.open("backgroung.png")
bg_image=bg_image.resize((1200,800),Image.ANTIALIAS)

bg_photo=ImageTk.PhotoImage(bg_image)

background_lable=tk.Label(window,image=bg_photo)

background_lable.place(x=0,y=0,relwidth=1,relheight=1)
#background_lable.pack(fill='both',expand='yes')
##########################"""Create input label and text box"""###########################################
 
input_label = tk.Label(window,width=25, text="INPUT:",background="gray",font=('italic',12))
input_label.pack()
input_text = tk.Text(window, height=10, width=80,bg="sky blue")
input_text.pack()

############################# """Create output label and text box"""#########################################
output_label = tk.Label(window, text="Output:",background="gray",font=('italic',12))
output_label.pack()
output_text = tk.Text(window, height=5, width=60,bg="sky blue")
output_text.pack()

##################""" writing function to convert morse to english means by key printing value"""########################################
def convert_to_english():
    morse_code = input_text.get("1.0", "end-1c").split(' ')
    english = ' '
    for code in morse_code:
        if code in MORSE_CODE_DICT:
            english += MORSE_CODE_DICT[code]
        else:
            english += ' '
    output_text.delete("1.0", "end")
    output_text.insert("1.0", english)
    
############### To add button in  window  and giveing the commond which call the function###################### 
convert_to_english_button = tk.Button(window, text="Morse to English", command=convert_to_english,bg="yellow",font=('italic',12))
convert_to_english_button.pack()

############ Writing function which convert english to morse means by value printing key#################### 
def convert_to_morse():
    english = input_text.get("1.0", "end").upper()
    morse_code = ''
    for char in english:
        if char == ' ':
            morse_code += ' '
        elif char in MORSE_CODE_DICT.values():
            for code, letter in MORSE_CODE_DICT.items():
                if letter == char:
                    morse_code += code + ' '
                    break
    output_text.delete("1.0", "end")
    output_text.insert("1.0", morse_code)

############# To add button in  window  and giveing the commond which call the function###########################
convert_to_morse_button = tk.Button(window, text="English to Morse", command=convert_to_morse,bg="yellow",font=('italic',12))
convert_to_morse_button.pack()

######################### Sound is lodaing and applying condition for that sound ############################
def play_morse_code(morse):
    print(morse)
    pygame.mixer.init()
    pygame.mixer.music.load("dot.mp3")  
    pygame.mixer.music.set_volume()  
    

    for symbol in morse:
        pygame.mixer.music.play()
        if symbol == '.':
            pygame.time.wait(200)  
            
        elif symbol == '-':
            pygame.time.wait(600) 
        elif symbol == '/':
            pygame.time.wait(400)  

        pygame.mixer.music.stop()
        pygame.mixer.music.play()
####################### creating function which access dictionry and plya sound accourding to cond #############
def audio():
    english = input_text.get("1.0", "end").upper()
    morse_code = ''
    for char in english:
        if char == ' ':
            morse_code += ' '
        elif char in MORSE_CODE_DICT.values():
            for code, letter in MORSE_CODE_DICT.items():
                if letter == char:
                    morse_code += code + ' '
                    break
    play_morse_code(morse_code)  
    """ we are calling function to play audio"""
    
#################### creating button for playing audio 

translate_button = tk.Button(window, text="audio", command=audio,bg="yellow",font=('italic',12))
translate_button.pack()
##########################################################################################################

def play():
    video=VideoFileClip("To_Learn.mp4")
    video.preview()
    
open_button=tk.Button(window,text="play video",bg="yellow",command=play)
open_button.pack()

###########  adding img on window which help to read the morse code and typing morse code #########################

image = Image.open("1572272364.png")
image = image.resize((300,300))  
image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=image,width=300)
image_label.pack()

#####################################################################################################

###########################################################################################################
window.mainloop()

############################################################################################################