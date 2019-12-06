# hello Python world!
# Sat Nov 16 10:35:19 2019
face0 = r'''
    | | |
 ----------
 |   二   |
8| ^.丁.^ |8
 |   喜   |
 ----------
'''

face1 = r'''
    | | |
 ----------
 |   二   |
8| 0 丁 0 |8
 |   怒   |
 ----------
'''

face2 = r'''
    | | |
 ----------
 |   二   |
8| ~.丁.~ |8
 |   哀   |
 ----------
'''

face3 = r'''
    | | |
 ----------
 |   二   |
8| ^o丁o^ |8
 |   乐   |
 ----------
'''

face4 = r'''
 ----------
 |   三   |
8| ~ 丁 ~ |8
 |   悲   |
 ----------
'''

# faces = [face0, face1, face2, face3, face4]
faces = {'play': face0, 'a': face1, 'joke': face2, 'on': face3, 'you': face4}


def face_show(faces):
    string = input("Please enter one word from 'play a joke on you':")
    if string:
        print(faces.get(string))


if __name__ == "__main__":
    face_show(faces)

